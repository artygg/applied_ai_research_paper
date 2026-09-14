#!/usr/bin/env python3
"""Generate index.html — the browsable, filterable source index — from data/sources.json."""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
recs = json.load(open(os.path.join(ROOT, "data", "sources.json"), encoding="utf-8"))

THEMES = [
    ("foundations", "Foundations", "The pre-LLM machine-learning stack"),
    ("adaptive-personalization", "Personalisation", "Birdbrain and the adaptive engine"),
    ("genai-features", "Generative AI features", "Max, Roleplay, Video Call, AI-authored content"),
    ("assessment-det", "Assessment (DET)", "AI in the Duolingo English Test"),
    ("fairness-validity", "Validity & fairness", "Bias, accents, proctoring, score meaning"),
    ("efficacy", "Efficacy", "Does it actually teach anyone anything"),
    ("reviews-meta", "Reviews & meta-analyses", "The synthesis layer"),
    ("datasets-reuse", "Datasets & reuse", "SLAM, STAPLE, HLR and what others built on them"),
    ("ethics-governance", "Ethics & governance", "Responsible AI, surveillance, dark patterns"),
    ("ethics-labour", "AI & labour", "Contractor cuts and the 'AI-first' pivot"),
    ("corporate-strategy", "Corporate & strategy", "Filings, portals, research infrastructure"),
    ("competitor", "Competitors", "Situating context"),
]

PROV = [
    ("duolingo", "Duolingo-authored"),
    ("mixed", "Mixed authorship"),
    ("independent", "Independent"),
    ("press", "Press / non-academic"),
]

payload = {
    "records": recs,
    "themes": [{"key": k, "label": l, "blurb": b} for k, l, b in THEMES],
    "provenances": [{"key": k, "label": l} for k, l in PROV],
}

CSS = """
:root{
  --paper:#F2F4F2; --surface:#FFFFFF; --sunken:#E7EAE7;
  --ink:#161B1A; --ink-2:#3E4746; --ink-3:#6B7674;
  --rule:#D3D9D6; --rule-soft:#E2E7E4;
  --accent:#0E5C54; --accent-soft:#D8E8E5; --accent-ink:#083B36; --accent-on:#F2F4F2;
  --p-duolingo:#A9701A; --p-mixed:#9E4B2C; --p-independent:#1F6F5C; --p-press:#5D6870;
  --shadow:0 1px 2px rgba(20,30,28,.07), 0 8px 24px -18px rgba(20,30,28,.5);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#0E1211; --surface:#161C1B; --sunken:#1D2523;
    --ink:#E9EDEB; --ink-2:#B4BEBB; --ink-3:#849290;
    --rule:#2A3432; --rule-soft:#222B29;
    --accent:#5BC5B6; --accent-soft:#17332F; --accent-ink:#A8E2D9; --accent-on:#08110F;
    --p-duolingo:#DFA94E; --p-mixed:#DA8763; --p-independent:#63C3A8; --p-press:#93A0A7;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -20px rgba(0,0,0,.9);
  }
}
:root[data-theme="dark"]{
  --paper:#0E1211; --surface:#161C1B; --sunken:#1D2523;
  --ink:#E9EDEB; --ink-2:#B4BEBB; --ink-3:#849290;
  --rule:#2A3432; --rule-soft:#222B29;
  --accent:#5BC5B6; --accent-soft:#17332F; --accent-ink:#A8E2D9; --accent-on:#08110F;
  --p-duolingo:#DFA94E; --p-mixed:#DA8763; --p-independent:#63C3A8; --p-press:#93A0A7;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -20px rgba(0,0,0,.9);
}

*{box-sizing:border-box}
body{
  background:var(--paper); color:var(--ink);
  font-family:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:15px; line-height:1.55; margin:0;
  -webkit-font-smoothing:antialiased;
}
a{color:inherit}
.wrap{max-width:1220px; margin:0 auto; padding:0 22px 72px}

/* ---------- masthead ---------- */
.mast{padding:44px 0 26px; border-bottom:1px solid var(--rule)}
.eyebrow{
  font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:11px;
  letter-spacing:.14em; text-transform:uppercase; color:var(--accent); margin:0 0 14px;
}
h1{
  font-family:Newsreader,Georgia,serif; font-weight:500; font-size:clamp(34px,5.2vw,54px);
  line-height:1.04; letter-spacing:-.015em; margin:0 0 16px; text-wrap:balance;
}
.standfirst{
  font-family:Newsreader,Georgia,serif; font-size:19px; line-height:1.5;
  color:var(--ink-2); max-width:62ch; margin:0 0 26px;
}
.standfirst em{color:var(--ink); font-style:italic}

.tallies{display:flex; flex-wrap:wrap; gap:0; border:1px solid var(--rule); border-radius:3px;
  background:var(--surface); overflow:hidden}
.tally{flex:1 1 128px; padding:13px 16px; border-right:1px solid var(--rule-soft)}
.tally:last-child{border-right:0}
.tally b{
  display:block; font-family:"IBM Plex Mono",monospace; font-variant-numeric:tabular-nums;
  font-size:23px; font-weight:600; letter-spacing:-.02em; line-height:1.2;
}
.tally span{font-size:11.5px; color:var(--ink-3); letter-spacing:.02em}

/* ---------- verification note ---------- */
.note{
  margin:22px 0 0; padding:13px 16px; background:var(--accent-soft);
  border-left:3px solid var(--accent); border-radius:0 3px 3px 0;
  font-size:13.5px; color:var(--accent-ink); max-width:78ch;
}
.note strong{font-weight:600}

/* ---------- layout ---------- */
.cols{display:grid; grid-template-columns:262px 1fr; gap:40px; margin-top:34px; align-items:start}
@media (max-width:860px){.cols{grid-template-columns:1fr; gap:26px}}

.rail{position:sticky; top:18px}
@media (max-width:860px){.rail{position:static}}
.rail-block + .rail-block{margin-top:24px; padding-top:20px; border-top:1px solid var(--rule-soft)}
.rail-h{
  font-family:"IBM Plex Mono",monospace; font-size:10.5px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--ink-3); margin:0 0 10px;
}
.search{
  width:100%; padding:9px 11px; font:inherit; font-size:14px; color:var(--ink);
  background:var(--surface); border:1px solid var(--rule); border-radius:3px;
}
.search::placeholder{color:var(--ink-3)}
.search:focus-visible{outline:2px solid var(--accent); outline-offset:1px; border-color:var(--accent)}

.chips{display:flex; flex-wrap:wrap; gap:6px}
.chip{
  font:inherit; font-size:12.5px; padding:5px 10px; cursor:pointer;
  background:var(--surface); color:var(--ink-2);
  border:1px solid var(--rule); border-radius:100px;
}
.chip:hover{border-color:var(--accent); color:var(--ink)}
.chip[aria-pressed="true"]{background:var(--accent); border-color:var(--accent); color:var(--accent-on)}
.chip:focus-visible{outline:2px solid var(--accent); outline-offset:2px}

.themelist{display:flex; flex-direction:column; gap:1px}
.tbtn{
  display:flex; align-items:baseline; justify-content:space-between; gap:10px; width:100%;
  font:inherit; font-size:13.5px; text-align:left; cursor:pointer; padding:6px 8px;
  background:transparent; color:var(--ink-2); border:0; border-radius:3px;
}
.tbtn:hover{background:var(--sunken); color:var(--ink)}
.tbtn[aria-pressed="true"]{background:var(--accent-soft); color:var(--accent-ink); font-weight:600}
.tbtn:focus-visible{outline:2px solid var(--accent); outline-offset:-2px}
.tbtn i{
  font-style:normal; font-family:"IBM Plex Mono",monospace; font-size:11.5px;
  font-variant-numeric:tabular-nums; color:var(--ink-3); flex:none;
}
.tbtn[aria-pressed="true"] i{color:var(--accent-ink)}

/* ---------- results ---------- */
.status{
  display:flex; align-items:baseline; justify-content:space-between; gap:16px; flex-wrap:wrap;
  padding-bottom:11px; border-bottom:1px solid var(--rule); margin-bottom:4px;
}
.count{font-family:"IBM Plex Mono",monospace; font-size:12.5px; color:var(--ink-3);
  font-variant-numeric:tabular-nums}
.count b{color:var(--ink); font-weight:600}
.sortsel{
  font:inherit; font-size:12.5px; padding:4px 8px; color:var(--ink-2);
  background:var(--surface); border:1px solid var(--rule); border-radius:3px;
}
.sortsel:focus-visible{outline:2px solid var(--accent); outline-offset:1px}

.grouphead{margin:30px 0 2px; padding-bottom:7px; border-bottom:1px solid var(--rule-soft)}
.grouphead:first-child{margin-top:14px}
.grouphead h2{
  font-family:Newsreader,Georgia,serif; font-weight:500; font-size:24px;
  letter-spacing:-.01em; margin:0; text-wrap:balance;
}
.grouphead p{margin:2px 0 0; font-size:12.5px; color:var(--ink-3)}

.item{
  padding:14px 0 15px 15px; border-bottom:1px solid var(--rule-soft);
  border-left:3px solid var(--bar); background:linear-gradient(90deg,var(--sunken),transparent 60px);
}
.item[data-prov="duolingo"]{--bar:var(--p-duolingo)}
.item[data-prov="mixed"]{--bar:var(--p-mixed)}
.item[data-prov="independent"]{--bar:var(--p-independent)}
.item[data-prov="press"]{--bar:var(--p-press)}

.item h3{font-size:15.5px; font-weight:600; line-height:1.35; margin:0 0 3px; text-wrap:balance}
.item h3 a{text-decoration:none; background-image:linear-gradient(var(--rule),var(--rule));
  background-size:100% 1px; background-repeat:no-repeat; background-position:0 100%}
.item h3 a:hover{color:var(--accent); background-image:linear-gradient(var(--accent),var(--accent))}
.item h3 a:focus-visible{outline:2px solid var(--accent); outline-offset:2px; border-radius:2px}

.byline{font-size:13px; color:var(--ink-2); margin:0 0 7px}
.byline .venue{font-style:italic}
.byline .yr{font-family:"IBM Plex Mono",monospace; font-variant-numeric:tabular-nums;
  color:var(--ink-3)}

.tags{display:flex; flex-wrap:wrap; gap:5px; margin-bottom:7px; align-items:center}
.tag{
  font-family:"IBM Plex Mono",monospace; font-size:10px; letter-spacing:.06em;
  text-transform:uppercase; padding:2px 6px; border-radius:2px;
  border:1px solid var(--rule); color:var(--ink-3); white-space:nowrap;
}
.tag.prov{color:var(--bar); border-color:var(--bar)}
.tag.pdf{color:var(--accent); border-color:var(--accent)}
.tag.warn{color:var(--p-mixed); border-color:var(--p-mixed)}
.tag.doi{text-transform:none; letter-spacing:0}
.tag a{text-decoration:none}
.tag a:hover{text-decoration:underline}

.note-line{font-size:13.5px; color:var(--ink-2); margin:0; max-width:72ch}
.note-line strong{color:var(--ink); font-weight:600}
.alt{font-family:"IBM Plex Mono",monospace; font-size:11px; color:var(--ink-3);
  margin:5px 0 0; word-break:break-all}
.alt a:hover{color:var(--accent)}

.empty{padding:52px 0; text-align:center; color:var(--ink-3)}
.empty p{margin:0 0 14px}

footer{margin-top:52px; padding-top:20px; border-top:1px solid var(--rule);
  font-size:12.5px; color:var(--ink-3); max-width:72ch}
footer code{font-family:"IBM Plex Mono",monospace; font-size:11.5px;
  background:var(--sunken); padding:1px 5px; border-radius:2px}

@media (prefers-reduced-motion:reduce){*{transition:none!important; animation:none!important}}
"""

JS = """
const D = window.__DATA__;
const state = {q:"", themes:new Set(), provs:new Set(), pr:false, pdf:false, sort:"year"};

const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const themeLabel = Object.fromEntries(D.themes.map(t => [t.key, t.label]));
const themeBlurb = Object.fromEntries(D.themes.map(t => [t.key, t.blurb]));
const provLabel  = Object.fromEntries(D.provenances.map(p => [p.key, p.label]));

function matches(r){
  if (state.themes.size && !state.themes.has(r.theme)) return false;
  if (state.provs.size  && !state.provs.has(r.provenance)) return false;
  if (state.pr  && !r.peer_reviewed) return false;
  if (state.pdf && !r.pdf) return false;
  if (state.q){
    const hay = (r.title+" "+r.authors+" "+r.venue+" "+r.note+" "+r.doi).toLowerCase();
    if (!state.q.split(/\\s+/).every(t => hay.includes(t))) return false;
  }
  return true;
}

function itemHTML(r){
  const tags = [];
  tags.push(`<span class="tag prov">${esc(provLabel[r.provenance])}</span>`);
  tags.push(`<span class="tag">${r.peer_reviewed ? "Peer-reviewed" : "Not peer-reviewed"}</span>`);
  if (r.pdf) tags.push('<span class="tag pdf">PDF</span>');
  if (r.status === "blocked") tags.push('<span class="tag warn">Opens in browser only</span>');
  if (r.doi) tags.push(`<span class="tag doi"><a href="https://doi.org/${esc(r.doi)}">doi:${esc(r.doi)}</a></span>`);
  const alt = r.alt_url ? `<p class="alt">Alt \\u2192 <a href="${esc(r.alt_url)}">${esc(r.alt_url)}</a></p>` : "";
  return `<article class="item" data-prov="${esc(r.provenance)}">
    <h3><a href="${esc(r.url)}">${esc(r.title)}</a></h3>
    <p class="byline">${esc(r.authors)} &middot; <span class="venue">${esc(r.venue)}</span> &middot; <span class="yr">${r.year}</span></p>
    <div class="tags">${tags.join("")}</div>
    <p class="note-line">${esc(r.note)}</p>${alt}
  </article>`;
}

function render(){
  const hits = D.records.filter(matches);
  const total = D.records.length;
  document.getElementById("count").innerHTML =
    `<b>${hits.length}</b> of ${total} sources` +
    (hits.length ? ` &middot; ${hits.filter(r=>r.peer_reviewed).length} peer-reviewed &middot; ${hits.filter(r=>r.pdf).length} with PDF` : "");

  const out = [];
  if (!hits.length){
    out.push('<div class="empty"><p>No sources match those filters.</p><button class="chip" id="reset">Clear all filters</button></div>');
  } else if (state.sort === "theme"){
    for (const t of D.themes){
      const g = hits.filter(r => r.theme === t.key);
      if (!g.length) continue;
      g.sort((a,b) => (b.peer_reviewed - a.peer_reviewed) || (b.year - a.year) || a.title.localeCompare(b.title));
      out.push(`<div class="grouphead"><h2>${esc(t.label)}</h2><p>${esc(t.blurb)} &middot; ${g.length} sources</p></div>`);
      out.push(...g.map(itemHTML));
    }
  } else {
    const g = hits.slice();
    if (state.sort === "year") g.sort((a,b) => (b.year - a.year) || a.title.localeCompare(b.title));
    else g.sort((a,b) => a.title.localeCompare(b.title));
    out.push(...g.map(itemHTML));
  }
  const res = document.getElementById("results");
  res.innerHTML = out.join("");
  const rst = document.getElementById("reset");
  if (rst) rst.addEventListener("click", clearAll);

  for (const b of document.querySelectorAll(".tbtn"))
    b.setAttribute("aria-pressed", state.themes.has(b.dataset.theme));
  for (const b of document.querySelectorAll(".chip[data-prov]"))
    b.setAttribute("aria-pressed", state.provs.has(b.dataset.prov));
  document.getElementById("f-pr").setAttribute("aria-pressed", state.pr);
  document.getElementById("f-pdf").setAttribute("aria-pressed", state.pdf);
}

function clearAll(){
  state.q=""; state.themes.clear(); state.provs.clear(); state.pr=false; state.pdf=false;
  document.getElementById("q").value = "";
  render();
}

function toggle(set, v){ set.has(v) ? set.delete(v) : set.add(v); }

document.getElementById("q").addEventListener("input", e => { state.q = e.target.value.trim().toLowerCase(); render(); });
document.getElementById("sort").addEventListener("change", e => { state.sort = e.target.value; render(); });
document.getElementById("f-pr").addEventListener("click", () => { state.pr = !state.pr; render(); });
document.getElementById("f-pdf").addEventListener("click", () => { state.pdf = !state.pdf; render(); });
document.getElementById("clear").addEventListener("click", clearAll);
for (const b of document.querySelectorAll(".tbtn"))
  b.addEventListener("click", () => { toggle(state.themes, b.dataset.theme); render(); });
for (const b of document.querySelectorAll(".chip[data-prov]"))
  b.addEventListener("click", () => { toggle(state.provs, b.dataset.prov); render(); });

render();
"""


def build():
    n = len(recs)
    pr = sum(1 for r in recs if r["peer_reviewed"])
    pdf = sum(1 for r in recs if r["pdf"])
    duo = sum(1 for r in recs if r["provenance"] in ("duolingo", "mixed"))
    ind = sum(1 for r in recs if r["provenance"] == "independent")
    years = [r["year"] for r in recs]

    theme_buttons = "\n".join(
        f'<button class="tbtn" data-theme="{k}" aria-pressed="false">'
        f'<span>{l}</span><i>{sum(1 for r in recs if r["theme"] == k)}</i></button>'
        for k, l, _ in THEMES
    )
    prov_chips = "\n".join(
        f'<button class="chip" data-prov="{k}" aria-pressed="false">{l}</button>'
        for k, l in PROV
    )

    html = f"""<title>Duolingo AI Research Index</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap">
<style>{CSS}</style>

<div class="wrap">
  <header class="mast">
    <p class="eyebrow">Literature inventory &middot; {min(years)}&ndash;{max(years)}</p>
    <h1>Duolingo AI Research Index</h1>
    <p class="standfirst">Every reachable article, paper, whitepaper and dataset connecting
      Duolingo and artificial intelligence. Built for a literature review, so each source
      carries the one thing a bibliography usually hides: <em>who wrote it</em>.</p>

    <div class="tallies">
      <div class="tally"><b>{n}</b><span>sources</span></div>
      <div class="tally"><b>{pr}</b><span>peer-reviewed</span></div>
      <div class="tally"><b>{pdf}</b><span>direct PDF</span></div>
      <div class="tally"><b>{duo}</b><span>Duolingo-authored</span></div>
      <div class="tally"><b>{ind}</b><span>independent</span></div>
    </div>

    <p class="note"><strong>Provenance is the point.</strong> A large share of the research on
      Duolingo&rsquo;s AI is written by Duolingo &mdash; including the only peer-reviewed study of its
      GPT-4 features. That does not make it wrong, but in-house and independent evidence should
      never be pooled without saying so. The coloured rule on each entry marks which is which.</p>
  </header>

  <div class="cols">
    <aside class="rail">
      <div class="rail-block">
        <p class="rail-h">Search</p>
        <input id="q" class="search" type="search" placeholder="Title, author, venue, note&hellip;" aria-label="Search sources">
      </div>
      <div class="rail-block">
        <p class="rail-h">Who wrote it</p>
        <div class="chips">{prov_chips}</div>
      </div>
      <div class="rail-block">
        <p class="rail-h">Filter</p>
        <div class="chips">
          <button class="chip" id="f-pr" aria-pressed="false">Peer-reviewed only</button>
          <button class="chip" id="f-pdf" aria-pressed="false">Has PDF</button>
          <button class="chip" id="clear">Clear all</button>
        </div>
      </div>
      <div class="rail-block">
        <p class="rail-h">Theme</p>
        <div class="themelist">{theme_buttons}</div>
      </div>
    </aside>

    <main>
      <div class="status">
        <p class="count" id="count" aria-live="polite"></p>
        <label class="count">Sort
          <select class="sortsel" id="sort">
            <option value="theme">by theme</option>
            <option value="year">newest first</option>
            <option value="title">A&ndash;Z</option>
          </select>
        </label>
      </div>
      <div id="results"></div>

      <footer>
        <p>Every URL in this index was checked programmatically; nothing is listed without a
        resolving link. <code>Opens in browser only</code> marks publishers that refuse scripted
        requests &mdash; SEC EDGAR, Duolingo&rsquo;s investor site, some paywalled outlets &mdash; where the
        link is live but a script cannot follow it. Peer-review status reflects the venue, not a
        judgement of quality; whitepapers, preprints and blog posts are included where they are
        the only account of a system, which for Duolingo&rsquo;s consumer AI is often the case.</p>
      </footer>
    </main>
  </div>
</div>

<script>window.__DATA__ = {json.dumps(payload, ensure_ascii=False)};</script>
<script>{JS}</script>
"""
    out = os.path.join(ROOT, "index.html")
    open(out, "w", encoding="utf-8").write(html)
    print(f"wrote {out} ({len(html)/1024:.0f} KB, {n} records)")


if __name__ == "__main__":
    build()

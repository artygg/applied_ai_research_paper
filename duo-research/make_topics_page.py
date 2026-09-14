#!/usr/bin/env python3
"""Render topics.html — the topic feasibility assessment — from data/topics.json."""
import html
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(ROOT, "data", "topics.json"), encoding="utf-8"))

INDEX_URL = "https://claude.ai/code/artifact/e81f9ef3-15af-4f7e-980d-51f152f087a9"

PROV_LABEL = {"duolingo": "Duolingo", "mixed": "Mixed", "independent": "Independent", "press": "Press"}
PROV_ORDER = ["duolingo", "mixed", "independent", "press"]

THEME_LABEL = {
    "foundations": "Foundations",
    "adaptive-personalization": "Personalisation",
    "genai-features": "Generative features",
    "assessment-det": "English Test",
    "fairness-validity": "Validity & fairness",
    "efficacy": "Efficacy",
    "reviews-meta": "Reviews & meta-analyses",
    "datasets-reuse": "Datasets & reuse",
    "ethics-governance": "Ethics & governance",
    "ethics-labour": "AI & labour",
    "corporate-strategy": "Corporate",
    "competitor": "Competitors",
}


def e(s):
    return html.escape(str(s), quote=True)


def meter(level, label=None):
    """Four-segment feasibility band. Structural, not chromatic — provenance owns the colour."""
    segs = "".join(
        f'<i class="seg{" on" if i < level else ""}"></i>' for i in range(4)
    )
    lab = f'<span class="meter-lab">{e(label)}</span>' if label else ""
    return f'<span class="meter" role="img" aria-label="Feasibility {level} of 4">{segs}</span>{lab}'


def provbar(prov, total):
    """Stacked composition bar: who wrote the sources this topic would rest on."""
    parts = []
    for k in PROV_ORDER:
        v = prov.get(k, 0)
        if not v:
            continue
        pct = 100 * v / total
        parts.append(
            f'<i class="pv pv-{k}" style="width:{pct:.4f}%" '
            f'title="{v} {e(PROV_LABEL[k])}"></i>'
        )
    return f'<span class="provbar" role="img" aria-label="{e(", ".join(f"{prov.get(k,0)} {PROV_LABEL[k].lower()}" for k in PROV_ORDER if prov.get(k)))}">{"".join(parts)}</span>'


def chart(timeline):
    """Grouped columns: sources published per year, by who wrote them."""
    yrs = timeline
    W, H = 720, 250
    PAD_L, PAD_R, PAD_T, PAD_B = 34, 8, 16, 46
    pw, ph = W - PAD_L - PAD_R, H - PAD_T - PAD_B
    top = 24  # above the max of 21
    band = pw / len(yrs)
    bw = band / 3 * 0.62
    gap = band / 3

    out = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="Sources per year by provenance, 2019 to 2026">']
    # gridlines + y labels
    for v in (0, 6, 12, 18, 24):
        y = PAD_T + ph - ph * v / top
        out.append(f'<line class="grid" x1="{PAD_L}" y1="{y:.1f}" x2="{W-PAD_R}" y2="{y:.1f}"/>')
        out.append(f'<text class="ax" x="{PAD_L-8:.1f}" y="{y+3.5:.1f}" text-anchor="end">{v}</text>')
    for i, row in enumerate(yrs):
        x0 = PAD_L + i * band
        for j, key in enumerate(("duolingo", "independent", "press")):
            v = row[key]
            h = ph * v / top
            x = x0 + band * 0.09 + j * gap
            y = PAD_T + ph - h
            cls = "pv-duolingo" if key == "duolingo" else ("pv-independent" if key == "independent" else "pv-press")
            out.append(f'<rect class="bar {cls}" x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" '
                       f'height="{max(h,0.8):.1f}"><title>{row["year"]}: {v} {key}</title></rect>')
            if v:
                out.append(f'<text class="val" x="{x+bw/2:.1f}" y="{y-4:.1f}" text-anchor="middle">{v}</text>')
        out.append(f'<text class="ax" x="{x0+band/2:.1f}" y="{H-PAD_B+20:.1f}" text-anchor="middle">{row["year"]}</text>')
    out.append("</svg>")
    return "".join(out)


def keylist(key):
    li = []
    for k in key:
        badge = ""
        if k["peer"] and k["prov"] == "independent":
            badge = '<b class="ld" title="Peer-reviewed and independent of Duolingo">load-bearing</b>'
        elif k["peer"]:
            badge = '<b class="pr">peer-reviewed</b>'
        li.append(
            f'<li><a href="{e(k["url"])}" target="_blank" rel="noopener">'
            f'<code class="sid pv-t-{k["prov"]}">{e(k["id"])}</code> '
            f'<span class="kt">{e(k["title"])}</span></a> '
            f'<span class="km">{e(k["venue"])}, {k["year"]}{"" if not badge else " · "}</span>{badge}</li>'
        )
    return "".join(li)


# ---------------------------------------------------------------- ledger

rows = []
for t in D["topics"]:
    kind = D["kinds"][t["kind"]]
    rows.append(f'''<tr data-kind="{e(t['kind'])}" data-level="{t['level']}">
 <th scope="row"><a href="#{e(t['slug'])}"><span class="rk">{t['rank']}</span><span class="rt">{e(t['title'])}</span></a>
   <span class="kind k-{e(t['kind'])}">{e(kind['label'])}</span></th>
 <td class="c">{t['n']}</td>
 <td class="c">{t['peer']}</td>
 <td class="c {'zero' if t['load'] == 0 else ''}">{t['load']}</td>
 <td class="c yr">{t['y0']}&ndash;{t['y1']}</td>
 <td class="bar-cell">{provbar(t['prov'], t['n'])}</td>
 <td class="v">{meter(t['level'], t['verdict'])}</td>
</tr>''')

# ---------------------------------------------------------------- dossiers

dossiers = []
for t in D["topics"]:
    kind = D["kinds"][t["kind"]]
    themes = " ".join(f'<span class="th">{e(THEME_LABEL.get(x, x))}</span>' for x in t["themes"])
    can = "".join(f"<li>{e(x)}</li>" for x in t["can"])
    cannot = "".join(f"<li>{e(x)}</li>" for x in t["cannot"])
    dossiers.append(f'''<article class="dossier" id="{e(t['slug'])}" data-kind="{e(t['kind'])}">
  <header>
    <p class="eyebrow"><span class="num">{t['rank']}</span> <span class="kind k-{e(t['kind'])}">{e(kind['label'])}</span> {meter(t['level'], t['verdict'])}</p>
    <h3>{e(t['title'])}</h3>
    <p class="q">{e(t['question'])}</p>
  </header>
  <div class="dgrid">
    <div class="dmain">
      <h4>What the sources can carry</h4>
      <ul class="can">{can}</ul>
      <h4>What they cannot</h4>
      <ul class="cannot">{cannot}</ul>
      <h4>Method that fits</h4>
      <p class="method">{e(t['method'])}</p>
      <p class="risk"><span>Watch for</span> {e(t['risk'])}</p>
    </div>
    <aside class="dside">
      <dl class="facts">
        <div><dt>Sources</dt><dd>{t['n']}</dd></div>
        <div><dt>Peer-reviewed</dt><dd>{t['peer']}</dd></div>
        <div><dt>Load-bearing</dt><dd class="{'zero' if t['load']==0 else 'hi'}">{t['load']}</dd></div>
        <div><dt>Since 2024</dt><dd>{t['recent']}</dd></div>
        <div><dt>Span</dt><dd class="yr">{t['y0']}&ndash;{t['y1']}</dd></div>
      </dl>
      {provbar(t['prov'], t['n'])}
      <p class="provline">{" · ".join(f"{t['prov'][k]} {PROV_LABEL[k].lower()}" for k in PROV_ORDER if t['prov'][k])}</p>
      <p class="themes">{themes}</p>
      <h5>Entry points</h5>
      <ol class="keys">{keylist(t['key'])}</ol>
    </aside>
  </div>
</article>''')

nv = []
for d in D["not_viable"]:
    nv.append(f'''<article class="nv">
  <h4>{e(d['title'])}</h4>
  <p class="nvstat"><span>{d['n']} sources</span><span>{d['peer']} peer-reviewed</span><span class="{'zero' if d['load']==0 else ''}">{d['load']} load-bearing</span></p>
  <p>{e(d['why'])}</p>
  <p class="instead"><span>Instead</span> {e(d['instead'])}</p>
</article>''')

kind_chips = "".join(
    f'<button class="chip" type="button" data-k="{e(k)}" aria-pressed="false">{e(v["label"])}</button>'
    for k, v in D["kinds"].items())

kind_defs = "".join(
    f'<div><dt class="kind k-{e(k)}">{e(v["label"])}</dt><dd>{e(v["blurb"])}</dd></div>'
    for k, v in D["kinds"].items())

ov = D["overall"]
strong = sum(1 for t in D["topics"] if t["level"] == 4)

HTML = f'''<title>Eleven Ways In</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;450;600&display=swap">
<style>
:root{{
  --paper:#F6F7F4; --panel:#FFFFFF; --sunk:#EDEFEA;
  --ink:#131A18; --ink-2:#3D4A46; --ink-3:#6B7873;
  --rule:#D8DDD6; --rule-2:#C3CAC1;
  --accent:#0E5C54; --accent-soft:#DCE9E5; --accent-on:#F4F7F5;
  --p-duolingo:#A9701A; --p-mixed:#9E4B2C; --p-independent:#1F6F5C; --p-press:#5D6870;
  --shadow:0 1px 2px rgba(19,26,24,.05);
  --measure:68ch;
}}
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="light"]){{
    --paper:#0D1211; --panel:#141B19; --sunk:#1A2321;
    --ink:#E5EAE6; --ink-2:#AFBAB5; --ink-3:#7E8B86;
    --rule:#28322F; --rule-2:#3A4642;
    --accent:#5BC5B6; --accent-soft:#183430; --accent-on:#07100E;
    --p-duolingo:#D9A24E; --p-mixed:#D3775A; --p-independent:#4FB79C; --p-press:#93A0A6;
    --shadow:0 1px 2px rgba(0,0,0,.3);
  }}
}}
:root[data-theme="dark"]{{
  --paper:#0D1211; --panel:#141B19; --sunk:#1A2321;
  --ink:#E5EAE6; --ink-2:#AFBAB5; --ink-3:#7E8B86;
  --rule:#28322F; --rule-2:#3A4642;
  --accent:#5BC5B6; --accent-soft:#183430; --accent-on:#07100E;
  --p-duolingo:#D9A24E; --p-mixed:#D3775A; --p-independent:#4FB79C; --p-press:#93A0A6;
  --shadow:0 1px 2px rgba(0,0,0,.3);
}}

*{{box-sizing:border-box}}
body{{
  background:var(--paper); color:var(--ink);
  font:450 16px/1.6 "IBM Plex Sans","Segoe UI",system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;
}}
.wrap{{max-width:1000px;margin:0 auto;padding:0 28px 96px}}
h1,h2,h3,h4,h5{{
  font-family:"Fraunces",Georgia,"Times New Roman",serif;
  font-variation-settings:"SOFT" 20,"WONK" 1;
  text-wrap:balance; margin:0; font-weight:600; letter-spacing:-.012em;
}}
p{{margin:0}}
a{{color:inherit}}
:focus-visible{{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}}
.mono,code{{font-family:"IBM Plex Mono",ui-monospace,monospace}}
.c,.yr,.facts dd,.val,.ax{{font-variant-numeric:tabular-nums}}

/* ---------- masthead ---------- */
.mast{{padding:64px 0 34px;border-bottom:2px solid var(--ink)}}
.mast .kicker{{
  font:500 11px/1 "IBM Plex Mono",monospace; letter-spacing:.14em; text-transform:uppercase;
  color:var(--ink-3); margin-bottom:20px;
}}
.mast h1{{font-size:clamp(38px,6.4vw,64px);line-height:1.02;font-weight:700;font-variation-settings:"SOFT" 12,"WONK" 1;max-width:15ch}}
.mast .dek{{margin-top:20px;max-width:var(--measure);font-size:18px;line-height:1.55;color:var(--ink-2)}}
.mast .dek strong{{color:var(--ink);font-weight:600}}

.tally{{display:flex;flex-wrap:wrap;gap:0;margin-top:30px;border-top:1px solid var(--rule)}}
.tally div{{flex:1 1 128px;padding:14px 18px 14px 0;border-right:1px solid var(--rule)}}
.tally div:last-child{{border-right:0}}
.tally dt{{font:500 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3)}}
.tally dd{{margin:7px 0 0;font-family:"Fraunces",serif;font-size:30px;font-weight:600;line-height:1;font-variant-numeric:tabular-nums}}
.tally dd small{{font-family:"IBM Plex Sans",sans-serif;font-size:12px;font-weight:450;color:var(--ink-3);display:block;margin-top:5px;letter-spacing:0}}

/* ---------- shared section head ---------- */
section{{margin-top:60px}}
.shead{{display:flex;align-items:baseline;gap:14px;border-bottom:1px solid var(--rule-2);padding-bottom:9px;margin-bottom:22px}}
.shead h2{{font-size:23px}}
.shead .note{{font-size:13px;color:var(--ink-3);margin-left:auto;text-align:right}}
.lede{{max-width:var(--measure);color:var(--ink-2);margin-bottom:22px}}

/* ---------- meter (structural, no hue) ---------- */
.meter{{display:inline-flex;gap:2.5px;vertical-align:middle}}
.meter .seg{{width:7px;height:13px;background:var(--rule-2);border-radius:1px}}
.meter .seg.on{{background:var(--accent)}}
.meter-lab{{margin-left:8px;font:500 11.5px/1 "IBM Plex Mono",monospace;letter-spacing:.02em;color:var(--ink-2);white-space:nowrap}}

/* ---------- provenance bar ---------- */
.provbar{{display:flex;width:100%;min-width:78px;height:9px;border-radius:1px;overflow:hidden;background:var(--sunk)}}
.pv{{display:block;height:100%}}
.pv-duolingo{{background:var(--p-duolingo)}}
.pv-mixed{{background:var(--p-mixed)}}
.pv-independent{{background:var(--p-independent)}}
.pv-press{{background:var(--p-press)}}
.pv-t-duolingo{{color:var(--p-duolingo)}}
.pv-t-mixed{{color:var(--p-mixed)}}
.pv-t-independent{{color:var(--p-independent)}}
.pv-t-press{{color:var(--p-press)}}

.legend{{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:16px;font-size:12.5px;color:var(--ink-2)}}
.legend span{{display:inline-flex;align-items:center;gap:7px}}
.legend i{{width:11px;height:11px;border-radius:1px;display:block}}

/* ---------- kind chips ---------- */
.kind{{
  display:inline-block;font:500 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.05em;
  padding:4px 7px;border:1px solid var(--rule-2);border-radius:2px;color:var(--ink-2);white-space:nowrap;
}}
.k-evidence{{border-color:var(--accent);color:var(--accent)}}
.filters{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:16px}}
.filters .lab{{font:500 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3);margin-right:4px}}
.chip{{
  font:500 12px/1 "IBM Plex Mono",monospace;padding:7px 11px;border:1px solid var(--rule-2);
  background:transparent;color:var(--ink-2);border-radius:2px;cursor:pointer;
}}
.chip:hover{{border-color:var(--ink-3);color:var(--ink)}}
.chip[aria-pressed="true"]{{background:var(--accent);border-color:var(--accent);color:var(--accent-on)}}

/* ---------- ledger ---------- */
.tablewrap{{overflow-x:auto;border:1px solid var(--rule);background:var(--panel);box-shadow:var(--shadow)}}
table{{border-collapse:collapse;width:100%;min-width:760px}}
thead th{{
  font:500 10px/1.3 "IBM Plex Mono",monospace;letter-spacing:.1em;text-transform:uppercase;
  color:var(--ink-3);text-align:left;padding:12px 12px 10px;border-bottom:1px solid var(--rule-2);
  vertical-align:bottom;font-weight:500;
}}
thead th.c{{text-align:center}}
tbody tr{{border-bottom:1px solid var(--rule)}}
tbody tr:last-child{{border-bottom:0}}
tbody tr.dim{{opacity:.26}}
tbody th{{font-weight:450;text-align:left;padding:13px 12px;max-width:400px}}
tbody th a{{text-decoration:none;display:block;margin-bottom:6px}}
tbody th a:hover .rt{{text-decoration:underline;text-decoration-color:var(--accent);text-underline-offset:3px}}
.rk{{font:600 11px/1 "IBM Plex Mono",monospace;color:var(--ink-3);margin-right:9px;vertical-align:1px}}
.rt{{font-size:14.5px;line-height:1.35;color:var(--ink)}}
tbody td{{padding:13px 12px;font-size:14px;color:var(--ink-2)}}
td.c{{text-align:center;font-weight:600;color:var(--ink);font-family:"IBM Plex Mono",monospace;font-size:13.5px}}
td.c.zero{{color:var(--ink-3);font-weight:400}}
td.yr{{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink-3);white-space:nowrap}}
td.bar-cell{{width:120px;min-width:100px}}
td.v{{white-space:nowrap}}

/* ---------- chart ---------- */
.chartbox{{border:1px solid var(--rule);background:var(--panel);padding:20px 18px 12px;box-shadow:var(--shadow)}}
.chart{{width:100%;height:auto;display:block}}
.chart .grid{{stroke:var(--rule);stroke-width:1}}
.chart .ax{{fill:var(--ink-3);font:500 10.5px "IBM Plex Mono",monospace}}
.chart .val{{fill:var(--ink-3);font:500 9px "IBM Plex Mono",monospace}}
.chart .bar.pv-duolingo{{fill:var(--p-duolingo)}}
.chart .bar.pv-independent{{fill:var(--p-independent)}}
.chart .bar.pv-press{{fill:var(--p-press)}}

/* ---------- dossiers ---------- */
.dossier{{border-top:1px solid var(--rule-2);padding:34px 0 8px}}
.dossier.hide{{display:none}}
.dossier > header{{max-width:var(--measure)}}
.eyebrow{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:12px}}
.num{{
  font-family:"Fraunces",serif;font-size:26px;font-weight:700;line-height:1;color:var(--accent);
  font-variant-numeric:tabular-nums;
}}
.dossier h3{{font-size:clamp(21px,2.6vw,27px);line-height:1.18}}
.q{{margin-top:12px;font-size:16.5px;color:var(--ink-2);border-left:2px solid var(--accent);padding-left:14px}}

.dgrid{{display:grid;grid-template-columns:minmax(0,1fr) 264px;gap:38px;margin-top:26px;align-items:start}}
.dmain{{max-width:var(--measure)}}
.dmain h4{{
  font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;letter-spacing:.11em;
  text-transform:uppercase;color:var(--ink-3);margin:22px 0 9px;font-variation-settings:normal;
}}
.dmain h4:first-child{{margin-top:0}}
.dmain ul{{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:7px}}
.dmain ul li{{position:relative;padding-left:22px;font-size:15px;line-height:1.5}}
.dmain ul li::before{{position:absolute;left:0;top:0;font-family:"IBM Plex Mono",monospace;font-size:13px}}
.can li::before{{content:"+";color:var(--accent);font-weight:600}}
.cannot li::before{{content:"\\2013";color:var(--ink-3)}}
.cannot li{{color:var(--ink-2)}}
.method{{font-size:15px;line-height:1.55;color:var(--ink-2)}}
.risk{{
  margin-top:22px;padding:13px 15px;background:var(--sunk);border-left:2px solid var(--p-mixed);
  font-size:14.5px;line-height:1.5;color:var(--ink-2);
}}
.risk span{{
  display:block;font:600 10px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;
  color:var(--p-mixed);margin-bottom:7px;
}}

.dside{{border-top:1px solid var(--rule-2);padding-top:14px;font-size:13px}}
.facts{{margin:0 0 16px}}
.facts div{{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px solid var(--rule)}}
.facts dt{{color:var(--ink-3);font-size:12.5px}}
.facts dd{{margin:0;font-family:"IBM Plex Mono",monospace;font-size:13px;font-weight:600;color:var(--ink)}}
.facts dd.hi{{color:var(--accent)}}
.facts dd.zero{{color:var(--ink-3);font-weight:400}}
.provline{{margin-top:8px;font:400 11.5px/1.5 "IBM Plex Mono",monospace;color:var(--ink-3)}}
.themes{{display:flex;flex-wrap:wrap;gap:5px;margin-top:12px}}
.th{{font-size:11px;padding:3px 7px;background:var(--sunk);color:var(--ink-2);border-radius:2px}}
.dside h5{{
  font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;letter-spacing:.11em;
  text-transform:uppercase;color:var(--ink-3);margin:20px 0 10px;font-variation-settings:normal;
}}
.keys{{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:11px}}
.keys li{{line-height:1.4}}
.keys a{{text-decoration:none;display:block}}
.keys a:hover .kt{{text-decoration:underline;text-underline-offset:2px}}
.sid{{font-size:11px;font-weight:600}}
.kt{{font-size:12.5px;color:var(--ink)}}
.km{{font-size:11px;color:var(--ink-3)}}
.ld{{font:600 10px/1 "IBM Plex Mono",monospace;color:var(--accent);letter-spacing:.03em}}
.pr{{font:400 10px/1 "IBM Plex Mono",monospace;color:var(--ink-3)}}

/* ---------- won't carry ---------- */
.nvlist{{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:0;border-top:1px solid var(--rule)}}
.nv{{padding:20px 22px 22px 0;border-right:1px solid var(--rule);max-width:46ch}}
.nv:last-child{{border-right:0}}
.nv h4{{font-size:16.5px;line-height:1.3;margin-bottom:10px}}
.nvstat{{display:flex;flex-wrap:wrap;gap:12px;font:500 11px/1 "IBM Plex Mono",monospace;color:var(--ink-3);margin-bottom:12px}}
.nvstat .zero{{color:var(--p-mixed)}}
.nv p{{font-size:14px;line-height:1.5;color:var(--ink-2)}}
.instead{{margin-top:12px;padding-top:11px;border-top:1px solid var(--rule)}}
.instead span{{
  display:block;font:600 10px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;
  color:var(--accent);margin-bottom:6px;
}}

/* ---------- method note ---------- */
.methodnote{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:26px 40px;max-width:900px}}
.methodnote p{{font-size:14.5px;line-height:1.6;color:var(--ink-2)}}
.methodnote h4{{font-size:16px;margin-bottom:8px}}
.kinddefs{{margin:0}}
.kinddefs div{{padding:11px 0;border-bottom:1px solid var(--rule)}}
.kinddefs dt{{margin-bottom:6px}}
.kinddefs dd{{margin:0;font-size:14px;line-height:1.5;color:var(--ink-2)}}

footer{{margin-top:56px;padding-top:20px;border-top:2px solid var(--ink);font-size:13px;color:var(--ink-3);
  display:flex;flex-wrap:wrap;gap:8px 24px;align-items:baseline}}
footer a{{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--accent-soft)}}
footer a:hover{{border-bottom-color:var(--accent)}}

@media (max-width:820px){{
  .dgrid{{grid-template-columns:1fr;gap:26px}}
  .dside{{max-width:var(--measure)}}
  .nv{{border-right:0;border-bottom:1px solid var(--rule);max-width:none;padding-right:0}}
  .nv:last-child{{border-bottom:0}}
}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>

<div class="wrap">

<header class="mast">
  <p class="kicker">Duolingo &amp; AI &middot; topic feasibility assessment &middot; {D['total']} sources</p>
  <h1>Eleven ways in</h1>
  <p class="dek">Every topic below is one somebody could reasonably propose. The question is not
  which sounds best — it is which the collected literature can actually carry. Each is scored on
  the count that decides it: <strong>load-bearing sources</strong>, meaning peer-reviewed and written
  by someone other than Duolingo.</p>
  <dl class="tally">
    <div><dt>Candidate topics</dt><dd>{len(D['topics'])}<small>plus 3 that will not carry</small></dd></div>
    <div><dt>Rated strong</dt><dd>{strong}<small>of {len(D['topics'])} assessed</small></dd></div>
    <div><dt>Peer-reviewed</dt><dd>{ov['peer']}<small>of {D['total']} sources</small></dd></div>
    <div><dt>Load-bearing</dt><dd>{ov['indep_peer']}<small>peer-reviewed &amp; independent</small></dd></div>
    <div><dt>Duolingo-authored</dt><dd>{ov['prov']['duolingo']}<small>{100*ov['prov']['duolingo']//D['total']}% of the corpus</small></dd></div>
  </dl>
</header>

<section>
  <div class="shead">
    <h2>The ledger</h2>
    <p class="note">Grouped by rating, then by claim type.<br>Click a title for the full assessment.</p>
  </div>
  <p class="lede">Two topics can hold the same number of sources and be worth completely different
  amounts, because they are not making the same kind of claim. A topic arguing that Duolingo teaches
  needs evidence Duolingo did not produce. A topic arguing about what Duolingo published needs
  Duolingo's own documents — there, first-party volume is the material, not a weakness. The rating
  below applies the test that matches the claim.</p>

  <div class="filters">
    <span class="lab">Filter</span>
    {kind_chips}
  </div>

  <div class="tablewrap">
  <table>
    <thead><tr>
      <th scope="col">Topic</th>
      <th scope="col" class="c">Sources</th>
      <th scope="col" class="c">Peer-<br>reviewed</th>
      <th scope="col" class="c">Load-<br>bearing</th>
      <th scope="col">Span</th>
      <th scope="col">Who wrote them</th>
      <th scope="col">Rating</th>
    </tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table>
  </div>
  <div class="legend">
    <span><i class="pv-duolingo"></i> Duolingo-authored</span>
    <span><i class="pv-mixed"></i> Mixed authorship</span>
    <span><i class="pv-independent"></i> Independent</span>
    <span><i class="pv-press"></i> Press &amp; corporate</span>
  </div>
</section>

<section>
  <div class="shead">
    <h2>Why the newest topics are the thinnest</h2>
    <p class="note">Sources per year by author, 2019&ndash;2026</p>
  </div>
  <p class="lede">Duolingo's own output (gold) leads in every year. Independent work (green) closes
  the gap around 2024 — but that is independent work on the <em>pre-generative</em> product, since
  peer review takes two to three years. Press coverage (grey) appears only in 2023 and peaks in 2025,
  tracking the AI-first controversy rather than any research. Anything shipped after 2023 is being
  discussed long before it is being studied.</p>
  <div class="chartbox">{chart(D['timeline'])}</div>
</section>

<section>
  <div class="shead">
    <h2>The assessments</h2>
    <p class="note">In ledger order</p>
  </div>
  {"".join(dossiers)}
</section>

<section>
  <div class="shead">
    <h2>Topics that will not carry</h2>
    <p class="note">Attractive, and unsupported</p>
  </div>
  <p class="lede">These come up naturally and should be ruled out early. In each case the absence
  is itself worth reporting — just not as a chapter of its own.</p>
  <div class="nvlist">{"".join(nv)}</div>
</section>

<section>
  <div class="shead"><h2>How the rating works</h2></div>
  <div class="methodnote">
    <div>
      <h4>Load-bearing sources</h4>
      <p>A source counts as load-bearing when it is peer-reviewed <em>and</em> written by someone with
      no Duolingo affiliation. Duolingo-authored work is not discounted as evidence about the company;
      it is discounted as independent corroboration of the company's claims. The three sources with
      mixed authorship never count as load-bearing, which is why they carry their own tag.</p>
      <p>Ratings run on four bands. An evidence claim reaches <em>strong</em> at twelve load-bearing
      sources across a base of fifteen or more; a corpus or discourse study reaches it on volume,
      first-party depth and a span of at least four years. The full scoring rule is in
      <code>analyse.py</code>, and the counts here are computed from the inventory rather than
      estimated.</p>
    </div>
    <div>
      <h4>Four kinds of claim</h4>
      <dl class="kinddefs">{kind_defs}</dl>
    </div>
  </div>
</section>

<footer>
  <span>Derived from the verified inventory of {D['total']} sources.</span>
  <a href="{INDEX_URL}" target="_blank" rel="noopener">Browse the full source index &rarr;</a>
  <span>Counts regenerate with <code>python analyse.py</code>.</span>
</footer>

</div>

<script>
(function () {{
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip"));
  var rows = Array.prototype.slice.call(document.querySelectorAll("tbody tr"));
  var dossiers = Array.prototype.slice.call(document.querySelectorAll(".dossier"));
  var active = null;

  function apply() {{
    rows.forEach(function (r) {{
      r.classList.toggle("dim", !!active && r.getAttribute("data-kind") !== active);
    }});
    dossiers.forEach(function (d) {{
      d.classList.toggle("hide", !!active && d.getAttribute("data-kind") !== active);
    }});
    chips.forEach(function (c) {{
      c.setAttribute("aria-pressed", String(c.getAttribute("data-k") === active));
    }});
  }}

  chips.forEach(function (c) {{
    c.addEventListener("click", function () {{
      var k = c.getAttribute("data-k");
      active = active === k ? null : k;
      apply();
    }});
  }});

  // A filtered-out dossier must not stay hidden when its anchor is followed.
  document.querySelectorAll("tbody th a").forEach(function (a) {{
    a.addEventListener("click", function () {{ active = null; apply(); }});
  }});
}})();
</script>
'''

out = os.path.join(ROOT, "topics.html")
open(out, "w", encoding="utf-8").write(HTML)
print(f"wrote {out} ({len(HTML)//1024} KB, {len(D['topics'])} topics + {len(D['not_viable'])} ruled out)")

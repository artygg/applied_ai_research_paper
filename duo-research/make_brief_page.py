#!/usr/bin/env python3
"""Render brief.html — the paper brief for "how does this business use AI".

Paper metadata (venue, year, url, provenance) is pulled from the verified
inventory so nothing here can drift from data/sources.json.
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
RECS = json.load(open(os.path.join(ROOT, "data", "sources.json"), encoding="utf-8"))
BY = {r["id"]: r for r in RECS}

INDEX_URL = "https://claude.ai/code/artifact/e81f9ef3-15af-4f7e-980d-51f152f087a9"
TOPICS_URL = "https://claude.ai/code/artifact/f4ef4e4e-d851-404a-b39d-9c23d947543f"

PROV_LABEL = {"duolingo": "Duolingo", "mixed": "Mixed", "independent": "Independent", "press": "Press"}


def e(s):
    return html.escape(str(s), quote=True)


# --------------------------------------------------------------- the six systems
# `doc` is how well the system is publicly documented, 0-4. The spread across
# these six rows is the paper's argument, so it is the one judgement call on
# the page that has to be defensible from the sources rather than asserted.
STACK = [
 dict(k="scheduling", name="Review scheduling", face="App",
      decides="Which word to put in front of you, and when",
      method="Half-life regression — a learned forgetting curve fitted on recall history, word difficulty and time since last practice",
      doc=4, docnote="Peer-reviewed, plus public data and reference code",
      ids=["settles16hlr", "tabibian19pnas"]),
 dict(k="personalisation", name="Difficulty personalisation", face="App",
      decides="How hard your next lesson is, and what it contains",
      method="Birdbrain — a per-learner ability model in the item-response tradition, deployed across every course",
      doc=1, docnote="One magazine article by staff. No paper, no model card, no audit",
      ids=["bicknell23spectrum"]),
 dict(k="engagement", name="Engagement optimisation", face="App",
      decides="When to send you a push notification",
      method="A sleeping/recovering bandit — contextual exploration over send times, optimising for return visits",
      doc=3, docnote="Published at KDD, no data release",
      ids=["yancey20kdd"]),
 dict(k="content", name="Content generation", face="App",
      decides="What the lessons themselves say",
      method="LLM generation constrained to a target CEFR proficiency band, then human review — the mechanism behind 148 courses in a year",
      doc=3, docnote="Method published at ACL Findings; the deployment is described only on the company blog",
      ids=["malik24acl"]),
 dict(k="conversation", name="Conversational practice", face="App",
      decides="What the AI tutor says back to you",
      method="GPT-4 behind Explain My Answer, Roleplay and Video Call, wrapped in scripted pedagogy",
      doc=1, docnote="One in-house self-report study and one outside analysis. No system paper",
      ids=["kittredge25selfeff", "harrison25tutor"]),
 dict(k="assessment", name="Test construction &amp; scoring", face="English Test",
      decides="Which items exist, what you score, and whether you cheated",
      method="Automatic item generation, transformer-based scoring, adaptive item selection over an IRT pool, plus LLM-cheating and proctoring detection",
      doc=4, docnote="A decade of peer-reviewed papers, two technical manuals, an in-house fairness audit",
      ids=["settles20tacl", "attali22reading", "yancey23bea", "niu24emnlp"]),
]

# --------------------------------------------------------------- the ten papers
READING = [
 dict(id="settles16hlr", layer="Review scheduling",
      read="The model at the base of the whole app: three feature groups, a fitted half-life, and an evaluation against the Leitner and Pimsleur heuristics it replaced.",
      load="low"),
 dict(id="tabibian19pnas", layer="Review scheduling",
      read="The independent challenge, and your one genuinely critical technical source. It reframes scheduling as control rather than prediction and beats Duolingo using Duolingo's released data. Read the framing; skip the proofs.",
      load="high"),
 dict(id="yancey20kdd", layer="Engagement optimisation",
      read="A bandit that optimises notification timing for return visits. Note the objective: this is AI aimed at retention, not learning. Your paper needs that distinction.",
      load="medium"),
 dict(id="settles20tacl", layer="Test construction",
      read="The single best overview of a complete deployed system: proficiency scales induced from text, items generated automatically, a test that adapts. If you read one paper closely, this one.",
      load="medium"),
 dict(id="attali22reading", layer="Test construction",
      read="Fully automated passage and question generation inside a live high-stakes test — an unusually concrete account of generative AI in production before ChatGPT existed.",
      load="medium"),
 dict(id="yancey23bea", layer="Scoring",
      read="GPT-4 rating essays on the CEFR scale, with human-rater agreement reported. Duolingo's first published LLM-scoring study, and useful evidence about where LLM scoring actually lands.",
      load="low"),
 dict(id="malik24acl", layer="Content generation",
      read="How you make an LLM write at a controlled proficiency level. This is the published method behind the AI-authored course expansion, so it carries a lot of your business section.",
      load="medium"),
 dict(id="niu24emnlp", layer="Integrity",
      read="Detecting GPT-written essays on the test. The closed loop worth pointing at: the same model class generates the items, scores the answers, and is the thing being defended against.",
      load="low"),
 dict(id="kittredge25selfeff", layer="Conversational practice",
      read="The only peer-reviewed study of Roleplay and Explain My Answer — in-house, self-report, and measuring confidence rather than proficiency. Read it for what it does not claim.",
      load="low"),
 dict(id="harrison25tutor", layer="Conversational practice",
      read="An outside look at the conversational tutor alongside competitors. Thin, and the only independent evidence there is, which is itself the point.",
      load="low"),
]

SUPPORT = [
 dict(id="10k-2025", why="The legally vetted version of the AI strategy, including the vendor-dependency risk the company discloses to investors. The most citable business source in the set."),
 dict(id="pr-148", why="The headline claim to test: twelve years for the first 100 courses, roughly one year for the next 148."),
 dict(id="blog-llmlessons", why="The content-generation pipeline described first-hand — the deployment story that malik24acl only gives the method for."),
 dict(id="blog-birdbrain", why="The original announcement of the personalisation model. Primary source for a system that has no paper."),
 dict(id="blog-max", why="The GPT-4 launch post, dated 14 March 2023. Fixes the start of the evidence clock."),
 dict(id="belzak25fairness", why="An in-house audit asking whether AI proctoring flags some nationalities more than others. Use it if you take the governance angle further."),
 dict(id="shortt23review", why="The canonical independent systematic review, 35 studies. Your outside anchor on whether any of this teaches."),
 dict(id="jiang24calico", why="The most-cited effectiveness study. Two authors are Duolingo employees — cite it, and say so."),
]

QUESTIONS = [
 dict(q="What AI systems does Duolingo actually run, and what does each one decide?",
      why="The descriptive backbone. Six systems, six decisions, six methods — and naming the decision each model makes keeps the section concrete rather than a list of buzzwords.",
      ids=["settles16hlr", "yancey20kdd", "settles20tacl", "malik24acl"]),
 dict(q="Is the AI documented in proportion to how many people it touches?",
      why="Your thesis, and the reason this is an analysis rather than a description. The test has a decade of peer-reviewed method papers; the app that 100M+ people open has a magazine article. Both facts are easy to evidence.",
      ids=["settles20tacl", "attali22reading", "bicknell23spectrum", "kittredge25selfeff"], key=True),
 dict(q="What changed when LLMs arrived — replacement, or another layer?",
      why="The interesting answer is 'addition'. The IRT and adaptive machinery from 2016-2020 is still load-bearing; LLMs were bolted on for generation and scoring. A good corrective to the assumption that generative AI replaced what came before.",
      ids=["settles16hlr", "settles20tacl", "yancey23bea", "malik24acl"], key=True),
 dict(q="What does the company use AI for that is not teaching?",
      why="Notification timing, cheating detection, proctoring, content cost. This is where a business-focused paper earns its keep — the AI that shows up in the cost structure rather than the lesson.",
      ids=["yancey20kdd", "niu24emnlp", "malik24acl"]),
 dict(q="Which AI claims does the business make, and what evidence sits behind them?",
      why="Set the 148-course announcement and the investor-facing language against the published evaluations. Some claims are well supported, some are not, and the difference is reportable.",
      ids=["pr-148", "10k-2025", "kittredge25selfeff", "harrison25tutor"]),
 dict(q="What risks does Duolingo itself name?",
      why="The 10-K discloses dependence on third-party model providers. Pair it with the in-house fairness audit and the cheating-detection work for a risk section grounded in the company's own documents.",
      ids=["10k-2025", "niu24emnlp", "belzak25fairness"]),
]

OUTLINE = [
 dict(s="Introduction", w=350, d="The company, why it is a good AI case, and the claim you will defend.", ids=["10k-2025"]),
 dict(s="The stack", w=900, d="Six systems, what each decides, and the method behind it. The descriptive core.",
      ids=["settles16hlr", "yancey20kdd", "settles20tacl", "attali22reading"]),
 dict(s="Before and after LLMs", w=650, d="What generative models added, and what they did not replace.",
      ids=["yancey23bea", "malik24acl", "settles20tacl"]),
 dict(s="AI that is not teaching", w=500, d="Engagement, integrity, proctoring, content cost. The business layer.",
      ids=["yancey20kdd", "niu24emnlp"]),
 dict(s="Claims and evidence", w=600, d="What the company says the AI achieves, set against what has been shown.",
      ids=["kittredge25selfeff", "harrison25tutor", "tabibian19pnas", "pr-148"]),
 dict(s="The documentation gap", w=500, d="Your argument section: visibility runs inverse to reach, and why that is a defensible reading.",
      ids=["bicknell23spectrum", "settles20tacl"]),
 dict(s="Conclusion", w=300, d="What a well-run AI company chooses to publish, and what that tells you.", ids=[]),
]

DEPTH = dict(
    title="If you want one section that is genuinely deep",
    body="Pick the scheduler and go one level further than description. The 2016 traces are public "
         "(13M user-word records on Harvard Dataverse), Duolingo's reference implementation ships "
         "with the Leitner, Pimsleur and logistic-regression baselines already wired up, and an "
         "independent PyTorch port exists to check yourself against. Reproducing the comparison "
         "table turns one section of the paper into your own result rather than a summary — and it "
         "sets up the PNAS critique, which beat that model using the very data release that made "
         "the critique possible. Budget an evening; scope it to the baseline table and say "
         "explicitly that the full optimal-control result is out of scope.",
    ids=["ds-hlr", "code-hlr", "avelar-hlr", "tabibian19pnas"])

LOAD_LABEL = {"low": "Light", "medium": "Moderate", "high": "Heavy"}
LOAD_N = {"low": 1, "medium": 2, "high": 3}


# --------------------------------------------------------------- render helpers

def cite(pid):
    r = BY[pid]
    return (f'<a class="cit pv-t-{r["provenance"]}" href="{e(r["url"])}" target="_blank" '
            f'rel="noopener" title="{e(r["title"])} — {e(r["venue"])}, {r["year"]}">{e(pid)}</a>')


def citelist(ids):
    return " ".join(cite(i) for i in ids)


def meter(n, of=4, cls=""):
    segs = "".join(f'<i class="seg{" on" if i < n else ""}"></i>' for i in range(of))
    return f'<span class="meter {cls}">{segs}</span>'


def loadmeter(k):
    return (f'<span class="load" title="Maths load: {LOAD_LABEL[k].lower()} — our read">'
            f'{meter(LOAD_N[k], 3, "sm")}<span class="ll">{LOAD_LABEL[k]}</span></span>')


stack_html = []
for s in STACK:
    thin = s["doc"] <= 1
    stack_html.append(f'''<article class="sys{' thin' if thin else ''}">
  <div class="sys-a">
    <p class="face f-{'test' if s['face'] != 'App' else 'app'}">{s['face']}</p>
    <h4>{s['name']}</h4>
    <p class="decides">{e(s['decides'])}</p>
  </div>
  <div class="sys-b"><p>{s['method']}</p></div>
  <div class="sys-c">
    <p class="docm">{meter(s['doc'])}<span>{e(s['docnote'])}</span></p>
    <p class="qcite">{citelist(s['ids'])}</p>
  </div>
</article>''')

reading_html = []
for n, item in enumerate(READING, 1):
    r = BY[item["id"]]
    reading_html.append(f'''<li class="rd">
  <div class="rd-n">{n}</div>
  <div class="rd-b">
    <p class="rd-role"><span class="tag">{e(item['layer'])}</span>{loadmeter(item['load'])}</p>
    <h4><a href="{e(r['url'])}" target="_blank" rel="noopener">{e(r['title'])}</a></h4>
    <p class="rd-meta"><code class="pv-t-{e(r['provenance'])}">{e(item['id'])}</code>
      <span>{e(r['venue'])}, {r['year']}</span>
      <span class="pv-t-{e(r['provenance'])}">{e(PROV_LABEL[r['provenance']])}</span>
      <span>{'peer-reviewed' if r['peer_reviewed'] else 'not peer-reviewed'}</span>
      {'<span>PDF</span>' if r['pdf'] else ''}</p>
    <p class="rd-read"><span>Read for</span> {e(item['read'])}</p>
  </div>
</li>''')

support_html = []
for s in SUPPORT:
    r = BY[s["id"]]
    support_html.append(f'''<li>
  <p class="sp-h"><code class="pv-t-{e(r['provenance'])}">{e(s['id'])}</code>
    <a href="{e(r['url'])}" target="_blank" rel="noopener">{e(r['title'])}</a></p>
  <p class="sp-m">{e(r['venue'])}, {r['year']}</p>
  <p>{e(s['why'])}</p>
</li>''')

q_html = []
for i, q in enumerate(QUESTIONS, 1):
    q_html.append(f'''<article class="qq{' key' if q.get('key') else ''}">
  <p class="qn">Q{i}{'<span class="spine">core</span>' if q.get('key') else ''}</p>
  <h4>{e(q['q'])}</h4>
  <p>{e(q['why'])}</p>
  <p class="qcite">{citelist(q['ids'])}</p>
</article>''')

total_w = sum(o["w"] for o in OUTLINE)
outline_html = []
for o in OUTLINE:
    outline_html.append(f'''<tr>
  <th scope="row">{e(o['s'])}</th>
  <td class="w">{o['w']}</td>
  <td>{e(o['d'])}</td>
  <td class="oc">{citelist(o['ids']) or '<span class="none">your own argument</span>'}</td>
</tr>''')

peer = sum(1 for i in READING if BY[i["id"]]["peer_reviewed"])
pdfs = sum(1 for i in READING if BY[i["id"]]["pdf"])
duo = sum(1 for i in READING if BY[i["id"]]["provenance"] == "duolingo")

HTML = f'''<title>How Duolingo Uses AI</title>
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
  --measure:66ch;
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
body{{background:var(--paper);color:var(--ink);
  font:450 16px/1.6 "IBM Plex Sans","Segoe UI",system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1000px;margin:0 auto;padding:0 28px 96px}}
h1,h2,h3,h4,h5{{font-family:"Fraunces",Georgia,serif;font-variation-settings:"SOFT" 20,"WONK" 1;
  text-wrap:balance;margin:0;font-weight:600;letter-spacing:-.012em}}
p{{margin:0}}
a{{color:inherit}}
:focus-visible{{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}}
code{{font-family:"IBM Plex Mono",ui-monospace,monospace}}
.w,.rd-n{{font-variant-numeric:tabular-nums}}

.pv-t-duolingo{{color:var(--p-duolingo)}}
.pv-t-mixed{{color:var(--p-mixed)}}
.pv-t-independent{{color:var(--p-independent)}}
.pv-t-press{{color:var(--p-press)}}

.meter{{display:inline-flex;gap:2.5px;flex:0 0 auto}}
.meter .seg{{width:7px;height:13px;background:var(--rule-2);border-radius:1px}}
.meter .seg.on{{background:var(--accent)}}
.meter.sm .seg{{width:6px;height:11px}}
.meter.sm .seg.on{{background:var(--ink-3)}}

.cit{{font:600 11px/1 "IBM Plex Mono",monospace;text-decoration:none;
  border-bottom:1px solid currentColor;padding-bottom:1px;opacity:.9}}
.cit:hover{{opacity:1}}
.qcite{{display:flex;flex-wrap:wrap;gap:5px 9px}}

/* ---------- masthead ---------- */
.mast{{padding:60px 0 32px;border-bottom:2px solid var(--ink)}}
.kicker{{font:500 11px/1 "IBM Plex Mono",monospace;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink-3);margin-bottom:20px}}
.mast h1{{font-size:clamp(36px,6vw,60px);line-height:1.03;font-weight:700;
  font-variation-settings:"SOFT" 12,"WONK" 1;max-width:14ch}}
.dek{{margin-top:20px;max-width:var(--measure);font-size:18px;line-height:1.55;color:var(--ink-2)}}
.dek strong{{color:var(--ink);font-weight:600}}
.tally{{display:flex;flex-wrap:wrap;margin-top:28px;border-top:1px solid var(--rule)}}
.tally div{{flex:1 1 116px;padding:13px 18px 13px 0;border-right:1px solid var(--rule)}}
.tally div:last-child{{border-right:0}}
.tally dt{{font:500 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3)}}
.tally dd{{margin:7px 0 0;font-family:"Fraunces",serif;font-size:28px;font-weight:600;line-height:1;font-variant-numeric:tabular-nums}}
.tally dd small{{font-family:"IBM Plex Sans",sans-serif;font-size:12px;font-weight:450;color:var(--ink-3);
  display:block;margin-top:5px;letter-spacing:0}}

section{{margin-top:58px}}
.shead{{display:flex;align-items:baseline;gap:14px;border-bottom:1px solid var(--rule-2);
  padding-bottom:9px;margin-bottom:22px;flex-wrap:wrap}}
.shead h2{{font-size:23px}}
.shead .note{{font-size:13px;color:var(--ink-3);margin-left:auto;text-align:right}}
.lede{{max-width:var(--measure);color:var(--ink-2);margin-bottom:24px}}

/* ---------- title block ---------- */
.titleblock{{border:1px solid var(--rule-2);background:var(--panel);padding:26px 28px;box-shadow:var(--shadow)}}
.titleblock .lab{{font:500 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.12em;text-transform:uppercase;
  color:var(--accent);margin-bottom:12px}}
.titleblock h3{{font-size:clamp(20px,2.7vw,28px);line-height:1.22;max-width:24ch}}
.titleblock .spinep{{margin-top:16px;max-width:var(--measure);font-size:16px;line-height:1.6;
  color:var(--ink-2);border-left:2px solid var(--accent);padding-left:15px}}
.alttitles{{margin-top:18px;padding-top:15px;border-top:1px solid var(--rule);
  font-size:13.5px;line-height:1.6;color:var(--ink-3)}}
.alttitles b{{font:600 10px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;
  display:block;margin-bottom:8px;color:var(--ink-3)}}
.alttitles span{{color:var(--ink-2);display:block;margin-bottom:5px}}

/* ---------- the stack ---------- */
.stack{{border-top:1px solid var(--rule-2)}}
.sys{{display:grid;grid-template-columns:minmax(180px,1fr) minmax(0,1.35fr) minmax(180px,1fr);
  gap:0 26px;padding:20px 0;border-bottom:1px solid var(--rule);align-items:start}}
.sys.thin{{background:var(--sunk);padding-left:16px;margin-left:-16px;border-left:2px solid var(--p-mixed)}}
.face{{font:600 9.5px/1 "IBM Plex Mono",monospace;letter-spacing:.1em;text-transform:uppercase;
  margin-bottom:8px}}
.f-app{{color:var(--p-duolingo)}}
.f-test{{color:var(--p-independent)}}
.sys h4{{font-size:17px;line-height:1.25}}
.decides{{margin-top:7px;font-size:13.5px;line-height:1.45;color:var(--ink-3)}}
.sys-b p{{font-size:14.5px;line-height:1.5;color:var(--ink-2)}}
.docm{{display:flex;align-items:flex-start;gap:10px;font-size:13px;line-height:1.45;color:var(--ink-2)}}
.docm .meter{{margin-top:2px}}
.sys-c .qcite{{margin-top:11px}}

/* ---------- reading list ---------- */
.readlist{{list-style:none;margin:0;padding:0}}
.rd{{display:grid;grid-template-columns:56px minmax(0,1fr);gap:0 20px;
  padding:22px 0;border-bottom:1px solid var(--rule)}}
.rd:first-child{{border-top:1px solid var(--rule-2)}}
.rd-n{{font-family:"Fraunces",serif;font-size:30px;font-weight:700;line-height:1;color:var(--accent)}}
.rd-b{{max-width:var(--measure);min-width:0}}
.rd-role{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:9px}}
.tag{{font:600 9.5px/1 "IBM Plex Mono",monospace;letter-spacing:.09em;text-transform:uppercase;
  padding:4px 7px;border:1px solid var(--rule-2);border-radius:2px;color:var(--ink-2)}}
.load{{display:inline-flex;align-items:center;gap:7px;color:var(--ink-3)}}
.ll{{font:400 11.5px/1 "IBM Plex Mono",monospace}}
.rd h4{{font-size:18.5px;line-height:1.3}}
.rd h4 a{{text-decoration:none}}
.rd h4 a:hover{{text-decoration:underline;text-decoration-color:var(--accent);text-underline-offset:3px}}
.rd-meta{{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;margin-top:9px;
  font:400 12px/1.4 "IBM Plex Mono",monospace;color:var(--ink-3)}}
.rd-meta code{{font-weight:600;font-size:11.5px}}
.rd-read{{margin-top:12px;font-size:15px;line-height:1.55;color:var(--ink-2)}}
.rd-read span{{font:600 10px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;text-transform:uppercase;
  color:var(--ink-3);margin-right:9px}}

/* ---------- questions ---------- */
.qgrid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(298px,1fr));gap:0;
  border-top:1px solid var(--rule)}}
.qq{{padding:20px 26px 22px 0;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule)}}
.qq.key{{background:var(--sunk);padding-left:20px;border-left:2px solid var(--accent)}}
.qn{{font:600 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;color:var(--ink-3);
  margin-bottom:10px;display:flex;align-items:center;gap:10px}}
.spine{{font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent-on);
  background:var(--accent);padding:3px 6px;border-radius:2px}}
.qq h4{{font-size:17px;line-height:1.32;margin-bottom:10px}}
.qq p{{font-size:14.5px;line-height:1.55;color:var(--ink-2)}}
.qq .qcite{{margin-top:12px}}

/* ---------- outline ---------- */
.tablewrap{{overflow-x:auto;border:1px solid var(--rule);background:var(--panel);box-shadow:var(--shadow)}}
table{{border-collapse:collapse;width:100%;min-width:700px}}
thead th{{font:500 10px/1.3 "IBM Plex Mono",monospace;letter-spacing:.1em;text-transform:uppercase;
  color:var(--ink-3);text-align:left;padding:12px;border-bottom:1px solid var(--rule-2);font-weight:500}}
tbody tr{{border-bottom:1px solid var(--rule)}}
tbody tr:last-child{{border-bottom:0}}
tbody th{{font-family:"Fraunces",serif;font-size:15.5px;font-weight:600;text-align:left;
  padding:14px 12px;white-space:nowrap}}
tbody td{{padding:14px 12px;font-size:14px;line-height:1.5;color:var(--ink-2);vertical-align:top}}
td.w{{font-family:"IBM Plex Mono",monospace;font-size:13px;color:var(--ink);font-weight:600;white-space:nowrap}}
td.oc{{width:186px}}
td.oc .qcite{{margin-top:0}}
.none{{font-size:12px;color:var(--ink-3);font-style:italic}}
tfoot td{{padding:12px;font:600 12px/1 "IBM Plex Mono",monospace;color:var(--ink-3);
  border-top:1px solid var(--rule-2)}}

/* ---------- support shelf ---------- */
.support{{list-style:none;margin:0;padding:0;display:grid;
  grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0;border-top:1px solid var(--rule)}}
.support li{{padding:17px 26px 19px 0;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule)}}
.sp-h{{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline;margin-bottom:5px}}
.sp-h code{{font-size:11px;font-weight:600}}
.sp-h a{{font-family:"Fraunces",serif;font-size:15px;font-weight:600;line-height:1.25;text-decoration:none}}
.sp-h a:hover{{text-decoration:underline;text-underline-offset:2px}}
.sp-m{{font:400 11px/1.4 "IBM Plex Mono",monospace;color:var(--ink-3);margin-bottom:8px}}
.support li p:last-child{{font-size:13.5px;line-height:1.5;color:var(--ink-2)}}

/* ---------- depth box ---------- */
.depth{{border:1px solid var(--accent);background:var(--accent-soft);padding:24px 26px;max-width:82ch}}
.depth h3{{font-size:19px;margin-bottom:11px}}
.depth p{{font-size:15px;line-height:1.6;color:var(--ink-2)}}
.depth .qcite{{margin-top:14px}}

.caveat{{margin-top:26px;max-width:82ch;padding:16px 18px;background:var(--sunk);
  border-left:2px solid var(--p-duolingo);font-size:14.5px;line-height:1.55;color:var(--ink-2)}}
.caveat b{{display:block;font:600 10px/1 "IBM Plex Mono",monospace;letter-spacing:.11em;
  text-transform:uppercase;color:var(--p-duolingo);margin-bottom:8px}}

footer{{margin-top:56px;padding-top:20px;border-top:2px solid var(--ink);font-size:13px;
  color:var(--ink-3);display:flex;flex-wrap:wrap;gap:8px 24px;align-items:baseline}}
footer a{{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--accent-soft)}}
footer a:hover{{border-bottom-color:var(--accent)}}

@media (max-width:860px){{
  .sys{{grid-template-columns:1fr;gap:12px}}
  .sys.thin{{margin-left:0}}
}}
@media (max-width:760px){{
  .rd{{grid-template-columns:38px minmax(0,1fr);gap:0 14px}}
  .rd-n{{font-size:22px}}
  .qq,.support li{{border-right:0;padding-right:0}}
}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>

<div class="wrap">

<header class="mast">
  <p class="kicker">Applied AI &middot; company case study &middot; ten papers</p>
  <h1>How Duolingo uses AI</h1>
  <p class="dek">Six AI systems, each making a different decision: what word you see next, when your
  phone buzzes, what the lesson says, what the tutor replies, and whether you passed the English
  test. They are all real and all deployed &mdash; but they are documented very unevenly, and
  <strong>the unevenness has a pattern worth arguing about</strong>.</p>
  <dl class="tally">
    <div><dt>Papers</dt><dd>10<small>{peer} peer-reviewed</small></dd></div>
    <div><dt>Direct PDFs</dt><dd>{pdfs}<small>no paywall to work around</small></dd></div>
    <div><dt>By Duolingo</dt><dd>{duo}<small>{10 - duo} independent</small></dd></div>
    <div><dt>Systems covered</dt><dd>{len(STACK)}<small>app and English Test</small></dd></div>
    <div><dt>Span</dt><dd>2016&ndash;25<small>pre-LLM to GPT-4</small></dd></div>
  </dl>
</header>

<section>
  <div class="shead"><h2>The paper</h2><p class="note">Title, and the claim underneath it</p></div>
  <div class="titleblock">
    <p class="lab">Proposed title</p>
    <h3>How Duolingo Uses AI: Six Systems and the Documentation Gap Between Them</h3>
    <p class="spinep">Duolingo publishes about its AI in inverse proportion to how many people that
    AI touches. The English Test &mdash; a few hundred thousand test-takers, high stakes &mdash; has
    a decade of peer-reviewed method papers, two technical manuals and an in-house fairness audit.
    The app, which more than a hundred million people open, has one magazine article for its
    personalisation model and a blog post for its content pipeline. Both halves of that are easy to
    evidence, which turns a description of the stack into an argument about it.</p>
    <p class="alttitles"><b>If you want a plainer title</b>
      <span>Artificial Intelligence at Duolingo: A Case Study of AI Across a Consumer Product and a High-Stakes Test</span>
      <span>From Spaced Repetition to Generative Tutors: A Decade of AI at Duolingo</span></p>
  </div>
</section>

<section>
  <div class="shead">
    <h2>The stack</h2>
    <p class="note">Six systems &middot; bars show how well each is publicly documented</p>
  </div>
  <p class="lede">This is the descriptive core of the paper, and the table where the argument
  becomes visible. Name the decision each model makes before naming the model &mdash; it keeps the
  section concrete, and it is what separates a case study from a list of features. The two shaded
  rows are the ones with almost nothing published behind them; both are consumer-facing.</p>
  <div class="stack">{"".join(stack_html)}</div>
</section>

<section>
  <div class="shead"><h2>The ten papers</h2><p class="note">In reading order</p></div>
  <p class="lede">Eight are written by Duolingo. For this assignment that is correct rather than a
  weakness &mdash; you are documenting how a company uses AI, and its own method papers are the
  primary sources. The two outside papers are there to keep you from writing a brochure: one beats
  Duolingo&rsquo;s scheduler using Duolingo&rsquo;s own data, and one is the only independent look
  at the conversational tutor that exists.</p>
  <ol class="readlist">{"".join(reading_html)}</ol>
</section>

<section>
  <div class="shead"><h2>The questions</h2><p class="note">Six, two of which carry the argument</p></div>
  <div class="qgrid">{"".join(q_html)}</div>
</section>

<section>
  <div class="shead">
    <h2>Suggested structure</h2>
    <p class="note">{total_w:,} words across {len(OUTLINE)} sections</p>
  </div>
  <div class="tablewrap">
    <table>
      <thead><tr>
        <th scope="col">Section</th><th scope="col">Words</th>
        <th scope="col">What it does</th><th scope="col">Draws on</th>
      </tr></thead>
      <tbody>{"".join(outline_html)}</tbody>
      <tfoot><tr><td>Total</td><td class="w">{total_w:,}</td>
        <td colspan="2">Cut &ldquo;AI that is not teaching&rdquo; first if you are over; keep the stack and the gap.</td></tr></tfoot>
    </table>
  </div>
  <p class="caveat"><b>The one thing to get right</b>
  Say once, early, that most of your sources are written by the company you are studying, and that
  this is appropriate for describing what the systems do but not for judging whether they work. Then
  hold that line. The moment the paper starts claiming Duolingo <em>teaches well</em>, you need
  {citelist(["shortt23review", "jiang24calico"])} and a different kind of evidence &mdash; and
  jiang24calico has Duolingo employees among its authors, so it needs the caveat too.</p>
</section>

<section>
  <div class="shead"><h2>Supporting sources</h2><p class="note">Cited, not read closely</p></div>
  <p class="lede">Business context, primary announcements, and the outside check. The 10-K is the
  most useful single item here: it is the only place the company states its AI strategy under legal
  liability, and it discloses the dependence on third-party model providers.</p>
  <ul class="support">{"".join(support_html)}</ul>
</section>

<section>
  <div class="shead"><h2>Going one level deeper</h2><p class="note">Optional, and it upgrades the paper</p></div>
  <div class="depth">
    <h3>{e(DEPTH['title'])}</h3>
    <p>{e(DEPTH['body'])}</p>
    <p class="qcite">{citelist(DEPTH['ids'])}</p>
  </div>
</section>

<footer>
  <span>Every paper verified against the source inventory.</span>
  <a href="{TOPICS_URL}" target="_blank" rel="noopener">Topic assessment &rarr;</a>
  <a href="{INDEX_URL}" target="_blank" rel="noopener">Full source index &rarr;</a>
  <span>Rebuild with <code>python make_brief_page.py</code>.</span>
</footer>

</div>
'''

out = os.path.join(ROOT, "brief.html")
open(out, "w", encoding="utf-8").write(HTML)
print(f"wrote {out} ({len(HTML)//1024} KB) — {len(STACK)} systems, {len(READING)} papers "
      f"({duo} Duolingo / {10-duo} independent, {peer} peer-reviewed), "
      f"{len(SUPPORT)} supporting, {total_w} words outlined")

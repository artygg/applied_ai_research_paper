#!/usr/bin/env python3
"""Score candidate research topics against the collected source base.

The decisive metric is `load` — sources that are BOTH peer-reviewed AND
independent of Duolingo. That is the count that determines whether a claim
can stand without leaning on the company's own evidence.
"""
import json, os, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
recs = json.load(open(os.path.join(ROOT, "data", "sources.json"), encoding="utf-8"))
BY = {r["id"]: r for r in recs}


def th(*names):
    return [r["id"] for r in recs if r["theme"] in names]


TOPICS = [
 dict(n="T1", kind="evidence", slug="efficacy",
  title="Does Duolingo teach? Twenty years of efficacy evidence, sorted by who paid for it",
  question="How strong is the evidence that Duolingo produces measurable language gains, and how much of it is independent of Duolingo?",
  ids=th("efficacy", "reviews-meta"),
  method="Systematic review extending Shortt et al. (2023), whose window closed at 2020. Code every study for design, sample, outcome measure and author affiliation; report Duolingo-authored and independent results separately rather than pooling them.",
  can=["Characterise the full 2020-2026 empirical record on Duolingo learning outcomes.",
       "Compare receptive against productive skill gains across independent studies.",
       "Show that self-published efficacy reports and peer-reviewed studies use systematically different designs and outcome measures.",
       "Test whether effect sizes differ by author affiliation - there are enough studies on both sides to try."],
  cannot=["Produce a defensible pooled effect size: outcome instruments range from Versant to in-house placement scores to self-report.",
          "Say anything about post-2023 generative features - almost no efficacy study covers them."],
  risk="jiang24calico, the most-cited 'does Duolingo work' study, has mixed Duolingo/academic authorship, which is why it carries provenance: mixed. A sensitivity analysis with and without it is not optional."),

 dict(n="T2", kind="evidence", slug="det",
  title="Building a validity argument for an AI-scored high-stakes test",
  question="How much of the Duolingo English Test's validity and fairness case is externally peer-reviewed, and how much rests on the company's own technical reports?",
  ids=th("assessment-det", "fairness-validity"),
  method="Validity-argument analysis in the Kane tradition. Map each inferential link - scoring, generalisation, extrapolation, decision - to the document that supports it, then mark each document peer-reviewed or self-published.",
  can=["Reconstruct the complete published validity argument from primary documents, including two technical manuals.",
       "Set the in-house case against twelve independent validity, fairness and accent-bias studies.",
       "Stage a real scholarly exchange: Burstein et al.'s responsible-AI case study against Johnson's direct rebuttal.",
       "Trace a single construct - interactive reading, or speaking - from item-generation paper to whitepaper to independent critique."],
  cannot=["Audit the scoring models. No item pool, no model weights, no subgroup error analysis beyond what the company reports.",
          "Compare against IELTS or TOEFL internals, which are equally closed."],
  risk="The 35 first-party DET sources will dominate any word count. Guard the ratio deliberately or the chapter becomes a summary of Duolingo's own case."),

 dict(n="T3", kind="gap", slug="genai-gap",
  title="Three years of Duolingo Max without an independent outcome study",
  question="What outcome evidence exists for the generative-AI features, and what explains the gap between shipping date and evidence date?",
  ids=th("genai-features") + ["li25chatbot", "ceai25twoyears", "discov26meta", "kittredge25selfeff", "catalan26lessons"],
  method="Reframe from efficacy review to evidence-gap analysis. Build a timeline of feature launches against the publication dates of any evaluation, and characterise what was published instead - engagement metrics, revenue framing, self-efficacy.",
  can=["Document the gap precisely, with dated primary sources on both sides.",
       "Show what a company publishes while it has no outcome evidence yet.",
       "Situate Duolingo in the wider generative-AI CALL literature, where meta-analyses already exist and Duolingo is largely absent."],
  cannot=["Answer whether Max, Roleplay or Video Call improve proficiency. Nobody has published that study.",
          "Treat kittredge25selfeff as outcome evidence - it is in-house, self-report, and measures self-efficacy."],
  risk="Only two independent peer-reviewed sources touch these features directly. Written as an efficacy review the topic collapses; written as a gap analysis it is one of the strongest here."),

 dict(n="T4", kind="evidence", slug="opendata",
  title="What open data bought: Duolingo's datasets and the research they made possible",
  question="What did releasing SLAM, STAPLE and the half-life regression traces produce, and what happened when the releases stopped?",
  ids=th("datasets-reuse") + ["settles16hlr", "yancey20kdd", "blog-birdbrain", "bicknell23spectrum"],
  method="Citation and reuse analysis of the four public datasets. Trace forward from each release into the downstream literature, then contrast with Birdbrain and the generative stack, where nothing was released.",
  can=["Show a decade of external work - knowledge tracing, fairness auditing, spaced-repetition optimisation, MT robustness - built on Duolingo data.",
       "Document that Duolingo's own model was beaten using its own data (tabibian19pnas) and independently replicated (avelar-hlr, papousek-hlr).",
       "Date the last release precisely: 2020. Nothing from the generative era has been opened.",
       "Argue open data as research infrastructure - a contribution that outweighs the company's own papers."],
  cannot=["Quantify how much of the knowledge-tracing field depends on Duolingo data without a formal bibliometric pass this collection does not contain.",
          "Explain why the releases stopped. No source states a reason."],
  risk="Twelve independent peer-reviewed sources make this solid, but half predate 2020. Frame it as a historical argument about openness, not a claim about current practice."),

 dict(n="T5", kind="corpus", slug="bibliometric",
  title="The frozen shop window: where Duolingo's research output went after 2021",
  question="What does the venue and volume of Duolingo's own publications reveal about where AI is load-bearing for the business?",
  ids=[r["id"] for r in recs if r["provenance"] == "duolingo"],
  method="Bibliometric analysis of the first-party corpus by venue, year, theme, peer-review status and author. Compare what the public research portal lists against what the same authors actually published.",
  can=["Demonstrate the portal has listed nothing since McCarthy et al., EMNLP 2021, while the same teams published at BEA, EMNLP, ACL Findings, PMLR and on arXiv through 2026.",
       "Quantify the reallocation from consumer-app research to assessment research.",
       "Show the whitepaper working as a genre: substantive, versioned, technically detailed, and outside peer review.",
       "Trace individual researchers across the shift using their public profiles."],
  cannot=["Claim the portal freeze was deliberate. It is equally consistent with neglect.",
          "Count unpublished internal research."],
  risk="Original work - nobody has published this analysis - which also means no prior methodology to lean on. Choose the bibliometric frame explicitly and state the corpus boundary."),

 dict(n="T6", kind="corpus", slug="aig",
  title="Automatic item generation and automated scoring as an applied NLP problem",
  question="What are the actual methods behind AI-driven test construction and scoring, and how did they change as LLMs arrived?",
  ids=["settles20tacl", "attali22reading", "mccarthy21", "yancey23bea", "yancey24bea", "naismith23bea",
       "malik24acl", "mulcaire25bea", "sharpnack24autoirt", "sharpnack24bandit", "sharpnack26irt",
       "sharpnack26s2a3", "vondavier26assembly", "vondavier26aquap", "runge24listening", "cai25pron",
       "cai25slate", "niu24emnlp", "niu25keystroke", "liao21", "liao22qa", "settles16hlr",
       "naismith25wnut", "cui23exercise", "qg21adaptive", "dkt23irt", "lak21vdkt", "vie18dfm"],
  method="Technical review. Read the method sections and trace the arc from logistic regression over hand-built features, to BERT-IRT, to GPT-4-based generation and scoring, noting which claims rest on held-out evaluation.",
  can=["Give a complete, well-documented technical account - this is the best-documented part of the whole Duolingo AI story.",
       "Show a clear methodological progression across a decade with named architectures and reported metrics.",
       "Connect the industrial work to the academic knowledge-tracing and question-generation literature."],
  cannot=["Verify reported results. No code or data accompanies the post-2020 papers.",
          "Cover the consumer app's models, which have no method papers at all."],
  risk="Almost entirely Duolingo-authored, and the peer-reviewed portion sits in workshop venues. Strong as a methods chapter, weak as evidence of quality."),

 dict(n="T7", kind="corpus", slug="governance",
  title="Responsible AI for the test, not for the app",
  question="Where does Duolingo's published AI governance apply, where does it stop, and does it meet its own stated standard?",
  ids=th("ethics-governance") + ["det-rai", "burstein25aime", "belzak25fairness", "johnson24devil", "pr-148", "blog-llmlessons"],
  method="Document and policy analysis. Read the Responsible AI Standards against the independent critiques, then test its scope against the products that fall outside it.",
  can=["Show the governance document covers the assessment product only, while the 148-course generative content push has no equivalent.",
       "Present a documented disagreement about what responsible-AI claims require - burstein24rai against johnson24devil - which is rare and citable.",
       "Connect to the wider critical literature on surveillance and algorithmic accountability in education."],
  cannot=["Assess compliance. There is no external audit of either product.",
          "Establish that the app has no internal standards - only that none is published."],
  risk="Document analysis, not empirical research. Works as a chapter; will not carry a whole dissertation."),

 dict(n="T8", kind="evidence", slug="gamification",
  title="Streaks, habits and the line between engagement design and dark patterns",
  question="Does the motivational architecture that drives Duolingo's retention also drive learning, and where does the critical literature say it stops helping?",
  ids=["espinosa26critical", "maass26habit", "mogavi22gamification", "shortt23review", "stockman22surveillance",
       "bjse25panopticon", "sudina25grit", "sudina23dose", "li23selfdirected", "li23selfmgmt",
       "cogent24autonomy", "cal25games", "xu25duovsgpt", "zeng24blackbox", "decoder-vonahn",
       "yancey20kdd", "plonsky23grit", "sumalinog26identity"],
  method="Thematic synthesis of the critical and motivational literature, anchored on the one first-party technical artefact that shows engagement being optimised directly: the notification bandit paper.",
  can=["Set a peer-reviewed habit-formation case study and a critical gamification analysis against the company's own optimisation paper and its CEO's stated goal.",
       "Use the dose-response and attrition studies to connect engagement mechanics to actual learning time.",
       "Make an argument about engagement optimisation as an AI application in its own right."],
  cannot=["Claim causation between specific mechanics and dropout. The designs are correlational or qualitative.",
          "Cover the current recommendation stack, which is undocumented."],
  risk="Thematically coherent but assembled across six themes. The AI connection is real - the bandit paper - but it has to be argued, not assumed."),

 dict(n="T9", kind="discourse", slug="aifirst",
  title="AI-first: a strategy announced before its evidence, and partly withdrawn before the evidence arrived",
  question="How did the AI-first pivot unfold, how was it received, and what does the arc show about AI adoption running ahead of proof?",
  ids=th("ethics-labour") + ["cnbc-productivity", "sl-q1-2025", "sl-q2-2026", "call-q1-2026", "10k-2025",
                             "nopriors-vonahn", "20vc-hacker", "wsj-hacker", "hardman-critique", "onlineedu-lowresource"],
  method="Discourse and case analysis over a dated primary-source chain: contractor cuts (Jan 2024), the memo (Apr 2025), the walk-back, the TikTok deletion, the 2026 retreat from AI-usage performance reviews. Read company statements against the filings.",
  can=["Reconstruct a complete, dated arc entirely from primary and contemporaneous sources.",
       "Contrast public messaging with what the 10-K and shareholder letters actually claim.",
       "Connect to a small peer-reviewed literature on generative AI in HRM and on teacher professional identity."],
  cannot=["Establish what happened internally. Nearly everything is press reporting on company statements.",
          "Quantify job losses beyond the reported 10% of contractors."],
  risk="Three peer-reviewed sources out of twenty-eight. This is a discussion chapter or a media-discourse study with an explicit method - it is not an empirical topic, and presenting it as one would be a mistake."),

 dict(n="T10", kind="evidence", slug="exemplar",
  title="The field's default exemplar: what it costs to study one company's product",
  question="Why is Duolingo simultaneously over-used as a case study and under-studied as a system, and what does that do to the field's conclusions?",
  ids=["rmal25ethics", "tf26scoping", "jiang24calico", "plonsky23grit", "blog-grant", "shortt23review",
       "kern24mlj", "thorne24mlj", "discov26prisma", "discov25samr", "pb22mall", "lee24meta",
       "ijlter25genai", "eric-multiling", "portal-research"],
  method="Methodological critique that uses the existing reviews as data: how often Duolingo appears, in what role, with what author affiliations, and with what access to the system under study.",
  can=["Cite a 2026 twenty-year scoping review finding Duolingo in 1.4% of empirical AI-in-language-learning studies.",
       "Draw on a published methodological critique of research using commercial apps.",
       "Use this collection's own provenance distribution as evidence - 107 Duolingo-authored against 80 independent - which is a defensible original contribution.",
       "Note that the company funds an external research grant programme."],
  cannot=["Prove that funding shaped findings. Nothing here supports that, and implying it would be unfair.",
          "Generalise to Babbel, Busuu or Memrise. There is one comparative study."],
  risk="Reflexive: the collection is both instrument and evidence. State that openly and describe how the inventory was built, or the argument is circular."),

 dict(n="T11", kind="gap", slug="speaking",
  title="Speaking is the least-studied skill and the hardest thing an AI tutor claims to teach",
  question="Does the field have instruments capable of evaluating a conversational AI tutor, and what would a rigorous Video Call study require?",
  ids=["duo-speak21", "duo-videocall-report", "blog-videocall", "harrison25tutor", "cai25pron", "cai25slate",
       "det-speaking", "runge24listening", "taylor24pron", "ceai25twoyears", "li25chatbot", "duo-conv24",
       "isbell24extrapolation", "kang24accent", "kang25attitudes", "discov26meta", "tajik25replika", "fountoulakis25"],
  method="Methodological review. Establish what the generative-AI CALL literature measures, show where speaking sits in that distribution, then specify the design an adequate Video Call evaluation would need.",
  can=["Cite systematic-review evidence that speaking is the least-studied skill in generative-AI language research.",
       "Contrast the assessment side's rigorous speaking-scoring work with the consumer side's absence of it.",
       "Propose a study design - a genuine contribution, since none exists."],
  cannot=["Evaluate Video Call. One conversational analysis and a withdrawn whitepaper are the entire direct evidence base.",
          "Use the Video Call efficacy report as a source: the PDF now returns AccessDenied and only the blog summary survives."],
  risk="Depends on a source that disappeared during collection. Worth reporting as a finding about self-published evidence, but it cannot be cited as data."),
]

NOT_VIABLE = [
 dict(title="Birdbrain and the personalisation engine, as a standalone topic",
      ids=th("adaptive-personalization"),
      why="Six sources, one independent peer-reviewed study, and no technical paper. The only substantive description of the model that touches every learner is a magazine article written by Duolingo staff. There is nothing to review.",
      instead="Fold it into T5 as the central absence, or into T4 as the counterexample to the open-data era."),
 dict(title="Duolingo against its competitors",
      ids=th("competitor") + ["kessler23babbel", "tajik25replika", "xu25duovsgpt", "fountoulakis25"],
      why="One peer-reviewed head-to-head comparison (Babbel), two ChatGPT comparisons and a listicle. Nowhere near enough for a comparative claim about the market.",
      instead="Use kessler23babbel as a single reference point inside T1 rather than building a chapter on it."),
 dict(title="The recommendation and content-sequencing stack",
      ids=["blog-innovations", "aws-duolingo", "bicknell23spectrum", "yancey20kdd"],
      why="Blog posts, a vendor case study and one KDD paper on notification timing. The sequencing machinery that shapes every session is undocumented in public.",
      instead="Report the absence itself in T5 or T7 - it is a finding, not a topic."),
]


def stats(ids):
    ids = list(dict.fromkeys(ids))
    missing = [i for i in ids if i not in BY]
    if missing:
        raise SystemExit(f"unknown ids: {missing}")
    g = [BY[i] for i in ids]
    pc = collections.Counter(r["provenance"] for r in g)
    yrs = [r["year"] for r in g]
    return dict(
        n=len(g),
        peer=sum(1 for r in g if r["peer_reviewed"]),
        load=sum(1 for r in g if r["peer_reviewed"] and r["provenance"] == "independent"),
        pdf=sum(1 for r in g if r["pdf"]),
        prov={k: pc.get(k, 0) for k in ("duolingo", "mixed", "independent", "press")},
        y0=min(yrs), y1=max(yrs),
        recent=sum(1 for r in g if r["year"] >= 2024),
        themes=sorted({r["theme"] for r in g}),
        key=[dict(id=r["id"], title=r["title"], year=r["year"], venue=r["venue"], url=r["url"],
                  peer=r["peer_reviewed"], prov=r["provenance"])
             for r in sorted(g, key=lambda r: (0 if (r["peer_reviewed"] and r["provenance"] == "independent") else 1,
                                               -r["year"], r["title"].lower()))[:6]],
        ids=ids)


KIND = {
    "evidence": ("Evidence claim",
        "Argues that something is true about learners or scores. Needs sources Duolingo did not write."),
    "corpus": ("Corpus study",
        "Argues about what was published, claimed or built. First-party documents are the primary data, not weak evidence."),
    "gap": ("Absence claim",
        "Argues that evidence is missing. Judged on how completely the record of what does exist can be pinned down."),
    "discourse": ("Discourse study",
        "Argues about how something was said and received. Primary and contemporaneous sources are the data."),
}


def verdict(t, s):
    """Feasibility depends on what kind of claim the topic makes.

    An evidence claim lives or dies on `load` - peer-reviewed sources written by
    someone other than Duolingo. A corpus or discourse study is asking what the
    company published or said, so first-party volume is the asset, not a liability.
    """
    kind = t["kind"]
    if kind == "evidence":
        if s["load"] >= 12 and s["n"] >= 15: return 4, "Strong"
        if s["load"] >= 8: return 3, "Workable"
        if s["load"] >= 3: return 2, "Reframe or fold in"
        return 1, "Framing only"
    if kind in ("corpus", "discourse"):
        first = s["prov"]["duolingo"] + s["prov"]["mixed"]
        span = s["y1"] - s["y0"]
        if s["n"] >= 25 and first >= 12 and span >= 4: return 4, "Strong"
        if s["n"] >= 15 and first >= 6: return 3, "Workable"
        if s["n"] >= 8: return 2, "Reframe or fold in"
        return 1, "Framing only"
    # gap: needs a complete record of what was shipped AND of the thin evidence
    if s["n"] >= 25 and s["load"] >= 4: return 3, "Workable"
    if s["n"] >= 15 and s["load"] >= 3: return 3, "Workable"
    if s["n"] >= 8: return 2, "Reframe or fold in"
    return 1, "Framing only"


def main():
    out = []
    for t in TOPICS:
        s = stats(t["ids"])
        lvl, label = verdict(t, s)
        out.append({**{k: v for k, v in t.items() if k != "ids"}, **s, "level": lvl, "verdict": label})
    KORDER = {"evidence": 0, "gap": 1, "corpus": 2, "discourse": 3}
    out.sort(key=lambda t: (-t["level"], KORDER[t["kind"]],
                           -(t["load"] if t["kind"] == "evidence" else t["n"]), -t["n"]))
    for i, t in enumerate(out, 1):
        t["rank"] = i

    nv = [{**{k: v for k, v in d.items() if k != "ids"}, **stats(d["ids"])} for d in NOT_VIABLE]

    years = sorted({r["year"] for r in recs if r["year"] >= 2019})
    timeline = [dict(year=y,
                     duolingo=sum(1 for r in recs if r["year"] == y and r["provenance"] in ("duolingo", "mixed")),
                     independent=sum(1 for r in recs if r["year"] == y and r["provenance"] == "independent"),
                     press=sum(1 for r in recs if r["year"] == y and r["provenance"] == "press"))
                for y in years]

    payload = dict(total=len(recs), kinds={k: dict(label=v[0], blurb=v[1]) for k, v in KIND.items()}, topics=out, not_viable=nv, timeline=timeline,
                   overall=dict(peer=sum(1 for r in recs if r["peer_reviewed"]),
                                indep_peer=sum(1 for r in recs if r["peer_reviewed"] and r["provenance"] == "independent"),
                                prov=dict(collections.Counter(r["provenance"] for r in recs))))
    json.dump(payload, open(os.path.join(ROOT, "data", "topics.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)

    print(f"{len(out)} topics scored -> data/topics.json")
    print(f"{'rk':>3} {'lvl':>3} {'n':>4} {'peer':>5} {'load':>5}  {'kind':<10} {'verdict':<20} title")
    for t in out:
        print(f"{t['rank']:>3} {t['level']:>3} {t['n']:>4} {t['peer']:>5} {t['load']:>5}  {t['kind']:<10} {t['verdict']:<20} {t['title'][:44]}")
    print()
    for d in nv:
        print(f"  not viable: n={d['n']:2d} load={d['load']}  {d['title'][:60]}")
    print()
    print("timeline", [(t["year"], t["duolingo"], t["independent"], t["press"]) for t in timeline])


if __name__ == "__main__":
    main()

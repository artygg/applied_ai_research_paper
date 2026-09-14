# Duolingo & AI — Sub-questions and Findings

Companion to [`sources.md`](sources.md). Each sub-question below names the sources that
actually bear on it, so you can see up front whether the evidence exists before committing
a chapter to it.

---

## Findings that emerged from building the collection

These are patterns in the *shape* of the literature, not claims from any single paper. They
came out of assembling the inventory and are, I think, the most interesting things here.

### 1. Duolingo's public research portal has been frozen since 2021 — but Duolingo never stopped publishing

`research.duolingo.com` lists 21 publications; the newest is McCarthy et al., EMNLP 2021.
Read alone, it suggests a research programme that wound down.

It didn't. It moved. Between 2023 and 2026 Duolingo published at BEA, EMNLP Industry,
Findings of ACL, W-NUT, AIME-Con, PMLR, *Frontiers in AI*, *Language Learning* and across
eight arXiv preprints — none of which appear on the portal. The work is real and ongoing;
the shop window is stale.

*Sources:* `portal-research`, `mccarthy21`, `yancey23bea`, `yancey24bea`, `malik24acl`,
`niu24emnlp`, `mulcaire25bea`, `sharpnack24autoirt`, `vondavier26aquap`, `sharpnack26s2a3`

### 2. The research moved to the assessment side, not the consumer side

Sort the post-2021 first-party output by theme and the split is stark: 35 sources on the
Duolingo English Test, versus a handful on the app that 100M+ people actually use. The
company publishes rigorously about the thing it sells to universities and sparingly about
the thing it sells to consumers.

A plausible reading: high-stakes assessment demands a public validity argument, and
consumer edtech does not. That asymmetry is worth stating explicitly — it shapes what any
literature review on "Duolingo AI" can conclude.

*Sources:* compare the `assessment-det` section (35) against `adaptive-personalization` (7)

### 3. Birdbrain — the AI that touches every learner — has never been peer-reviewed or externally audited

The only substantive public description of Duolingo's core personalisation model is a 2023
*IEEE Spectrum* article written by Duolingo staff. There is no paper, no model card, no
independent audit. Half-life regression, its 2016 predecessor, *has* been challenged
(Tabibian et al., PNAS 2019) and replicated — because Duolingo released the data. Birdbrain's
data was never released, and the scrutiny stopped accordingly.

*Sources:* `bicknell23spectrum`, `blog-birdbrain`, `settles16hlr`, `tabibian19pnas`,
`papousek-hlr`, `avelar-hlr`

### 4. The generative-AI features are the loudest part of the product story and the thinnest part of the evidence base

Duolingo Max launched in March 2023. As of September 2026, the only peer-reviewed study of
Max features (Roleplay, Explain My Answer) is Kittredge et al. 2025 — authored entirely by
Duolingo employees, self-report, and measuring *self-efficacy* rather than proficiency. The
nearest independent work is one SSRN technology review and one arXiv student-perception
case study.

There is a three-year gap between shipping a feature to millions of learners and any
independent evidence that it teaches.

*Sources:* `kittredge25selfeff`, `harrison25tutor`, `catalan26lessons`, `blog-max`,
`duo-videocall-report`

### 5. Duolingo's datasets have contributed more to the research community than its papers

SLAM (2018), STAPLE (2020), the half-life regression traces and the notification-bandit data
seeded a body of external work — knowledge tracing, fairness auditing, spaced-repetition
optimisation, even machine-translation robustness — much of which Duolingo had no hand in
and some of which contradicts it. Twenty-seven sources here reuse Duolingo data.

The releases stopped in 2020. Nothing from the generative-AI era has been opened up.

*Sources:* the `datasets-reuse` section (27), especially `tang24fairkt`, `cui23exercise`,
`tabibian19pnas`, `staple-robust`

### 6. Duolingo is under-studied relative to its size

A 2026 twenty-year scoping review found Duolingo appears in just **1.4%** of empirical
AI-in-language-learning studies. The most widely used language-learning product in history
is a rounding error in the literature about language-learning products.

*Sources:* `tf26scoping`, `shortt23review`, `rmal25ethics`

### 7. Responsible-AI governance covers the test, not the app

Duolingo published *Responsible AI Standards* — for the Duolingo English Test only. The
consumer app, which received the 148-course generative-AI content push, has no equivalent
document and no published model card. That asymmetry tracks finding #2 exactly.

*Sources:* `det-rai`, `burstein24rai`, `johnson24devil`, `det-blog-custodianship`

### 8. A whitepaper that search engines still index is no longer retrievable

The Video Call efficacy study (n=567 Japanese learners, Versant pre/post) is indexed by
title and URL, but the S3 object now returns `AccessDenied`. Only the blog summary remains
live. Worth a Wayback check before drawing conclusions — this could be an ordinary rename —
but it illustrates the wider problem with self-published evidence: it can be withdrawn
without a retraction notice, which is precisely what peer review and DOIs prevent.

*Sources:* `duo-videocall-report`

---

## Proposed sub-questions

Ordered by how well the collected sources can actually support them.

### Well-supported — start here

**Q1. What does Duolingo's AI actually do, and which parts are documented?**
Trace the stack: half-life regression (2016) → Birdbrain (2020) → GPT-4 Max features (2023)
→ LLM-authored course content (2024–25) → Video Call (2024–26). Then mark each component as
peer-reviewed, self-published, or marketing-only. The answer is a coverage map, and the gaps
are the finding.
*Draws on:* `foundations`, `adaptive-personalization`, `genai-features`

**Q2. Where did Duolingo's research output go after 2021, and what does the reallocation reveal?**
A venue-and-theme analysis over the 96 first-party sources. Consumer-app research thins;
assessment research accelerates. Argue what that says about where AI is load-bearing for
the business versus where it is load-bearing for learning.
*Draws on:* all `provenance = duolingo` records; findings #1 and #2

**Q3. How strong is the efficacy evidence, and who produced it?**
Split the 28 efficacy sources by provenance and compare effect sizes, sample sizes and
designs. Note that the most-cited "does it work" paper (Jiang et al., CALICO 2024) has mixed
Duolingo/academic authorship — flagged in the data as `provenance: mixed`. Shortt et al.
(2023) reviewed 2012–2020; extending it to 2026 is a genuine contribution.
*Draws on:* `efficacy`, `reviews-meta`, especially `shortt23review`, `jiang24calico`,
`llt24receptive`, `kessler23babbel`, `pb22mall`

**Q4. Has generative AI changed measured learning outcomes — or only engagement and revenue?**
The sharpest question in the set, because the honest answer appears to be "we don't know."
Contrast the in-house self-efficacy result against the absence of independent proficiency
evidence, then against the earnings-call framing of the same features.
*Draws on:* `kittredge25selfeff`, `harrison25tutor`, `catalan26lessons`, `xu25duovsgpt`,
`li25chatbot`, `call-q1-2026`, `sl-q2-2026`

### Supportable with care

**Q5. How much of the DET's validity argument is externally peer-reviewed versus self-published?**
The DET is the best-evidenced part of the Duolingo AI story and the sharpest test case:
automatic item generation, automated scoring, algorithmic proctoring. Set the 18 in-house
whitepapers against the independent validity and fairness studies — and stage the direct
exchange between Burstein et al.'s responsible-AI case study and Johnson's rebuttal.
*Draws on:* `assessment-det`, `fairness-validity`, especially `settles20tacl`,
`attali22reading`, `isaacs23validity`, `kang24accent`, `yao23fairness`, `burstein24rai`,
`johnson24devil`

**Q6. Do generatively-authored courses teach as well as human-authored ones?**
The 148-course launch is the largest natural experiment in AI-authored curriculum ever run.
Duolingo has published the *method* (Malik et al. 2024 on CEFR-controlled generation) but
not an outcome evaluation. Note the low-resource-language equity concern.
*Draws on:* `malik24acl`, `blog-llmlessons`, `blog-duoradio`, `pr-148`, `catalan26lessons`,
`onlineedu-lowresource`, `hardman-critique`

**Q7. Does the field have the instruments to evaluate a conversational AI tutor at all?**
Video Call is a speaking-practice feature, and the 2025 systematic review found speaking is
the least-studied skill in generative-AI language research (writing is 51.3%). The
methodological gap may be upstream of Duolingo entirely.
*Draws on:* `ceai25twoyears`, `li25chatbot`, `discov26meta`, `harrison25tutor`,
`duo-speak21`, `duo-videocall-report`

### Framing and discussion, rather than answerable

**Q8. "AI-first" as corporate strategy outrunning its evidence base.**
The April 2025 memo, the backlash, the walk-back, and the April 2026 retreat from
AI-usage-based performance reviews form a complete arc with dated primary sources. Read it
against Q4: the strategy was announced before the evidence existed, and partly retracted
before the evidence arrived.
*Draws on:* `ethics-labour` (18 sources), especially `snopes-memo`, `fortune-walkback`,
`fortune-2026retreat`, `tc-jobscrisis`, `oecd24incident`, `budhwar23hrm`

**Q9. What does it mean that the field's default exemplar is a company that controls its own data?**
Duolingo is over-represented as a case study and under-represented as a research subject,
its most-cited efficacy paper is co-authored by its own staff, and it funds an external
research-grant programme. There is a live methodological-ethics literature on exactly this.
*Draws on:* `rmal25ethics`, `tf26scoping`, `blog-grant`, `jiang24calico`, `plonsky23grit`

---

## Things worth chasing that this collection does not yet have

- **Bloomberg, 8 January 2024** — the originating scoop on the contractor cuts. Every later
  story cites it; the URL was not recovered.
- **The NYT Corner Office interview, August 2025** — referenced by TechCrunch, Fortune and
  Sherwood; the canonical nytimes.com URL was not found.
- **The original AI-first LinkedIn post** — no stable permalink. Snopes and Entrepreneur
  reproduce the full text and are the safer citations. A Wayback capture of the Duolingo
  company page from 28–30 April 2025 would be the ideal primary artifact.
- **The DET publications index** is client-rendered, so it could not be enumerated
  programmatically. The whitepapers here were recovered from S3 and Scholar profiles; a
  browser pass over `englishtest.duolingo.com/research/publications` would confirm
  completeness.
- **Wayback was unreachable** during collection, so no historical snapshots were captured —
  relevant to finding #8.
- **Two 2025/2026 *Language Testing* articles** (multi-stage interactive writing; adaptive
  speaking task) surfaced via author profiles but without confirmed DOIs, so they are not in
  the inventory.

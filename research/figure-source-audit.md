# Figure and table revision: source and production record

Prepared 16 September 2026 for the current Duolingo user-experience paper. This record concerns the visual revision. Earlier source logs remain historical records; their earlier page counts, reference counts, and manuscript scopes are not current validation results.

## What changed

The current paper originally had one TikZ diagram and three LaTeX tables, already numbered using LaTeX's counters. The revision gives them APA-style bold numbers and separate italic, descriptive titles above the visual, with explanatory notes below. It adds three original figures. The resulting paper has four figures and three tables, all cross-referenced in the prose.

The archived manuscript and the separate `duo-research` web pages were not treated as submission figures and were not edited. No application scripts or existing application behaviour were changed. New plotting code is isolated in `figures/render_charts.py`. Repeated descriptions of the timeline, workflows, and production statistics were shortened to integrate the visuals within the required 8–10-page Results body; the research questions and overall conclusions were retained for the separate strict review.

The layout retains the existing 11-point, two-column article design and one-inch margins. Paragraph spacing changed from 0.3 to 0.2 baselines, and the permitted top-float fraction increased so full-width tables can appear near the relevant text. Figure/table titles and notes use double spacing. No autoformatter or new test suite was used.

## Provenance by visual

| Visual | Type and purpose | Evidence and locator | Boundaries |
|---|---|---|---|
| Figure 1: Documented Workflows for Lesson Production and Video Call | Original two-panel TikZ schematic; makes the human/model roles and between-call information flow explicit. | Parker Henry's [lesson-production account](https://blog.duolingo.com/large-language-model-duolingo-lessons/), “What does AI look like in action?”, steps 1–3; and [Video Call account](https://blog.duolingo.com/ai-and-video-call/), “How we design each Video Call” and “Lily's memory.” Both full company pages inspected. | A descriptive workflow, not a recovered software architecture, a claim about training/fine-tuning, or an effectiveness finding. Lesson selection is not presented as the distinct DuoRadio production pipeline. |
| Figure 2: Analysis Samples in the 30-Day Video Call Study | Original grouped bar chart of reported analysis counts; percentages are simple calculations. | Kittredge, Lee, and Jiang (2025), [original report](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_video_call_improves_speaking_2025.pdf), Figure 2, printed p. 5; indexed original-report passage inspected. | Direct PDF retrieval returned 403. The full report was not newly downloaded. Analysis inclusion is not app retention, a treatment effect, or an intention-to-treat reanalysis. |
| Figure 3: Generative-AI Pathways and the Outcomes Visible in Public Sources | Existing analytical diagram, relabelled and source-qualified. | The paper's Tables 1–3 and the sources cited in them. | Output arrows distinguish reporting coverage; they do not assert causation or disclose internal optimisation weights. “Rarely evaluated” became “Limited public evidence,” and the long-term endpoint is explicitly feature effects. |
| Figure 4: Company-Reported Expansion of DuoRadio Content and Use | Original three-panel bar chart with separate, zero-based axes. | Luis Mas Castillo, Sophie Mackey, and Cindy Berger's [DuoRadio account](https://blog.duolingo.com/scaling-duoradio/), “Reaching More Learners Faster” and “Course content expansion.” Full company text inspected. | Company-reported descriptive values. The 15,000+ and 25+ values are plotted at the stated lower bound with the plus sign retained. No exact endpoint dates, learning effects, confidence intervals, or synthetic time series are invented. |
| Table 1: Generative-AI Changes by Date and Track | Existing dated chronology with separate source note. | Sources remain cited in individual rows. | The DuoRadio row now distinguishes its late-2023 launch, 2024 hackathon, and March-2025 scaling account. A source publication date is not substituted for the original product launch. |
| Table 2: Evidence on Learner Effects | Existing study appraisal table, with compact columns and explicit outcome definitions. | Sources cited in each row; key self-efficacy methods/results rechecked in the [original Frontiers article](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1499497/full). | Study units and analysis samples are not independent replications to be added. The Japanese study row distinguishes speaking advantage, stable willingness to communicate, and neutral confidence perceptions. |
| Table 3: Enrichment and Industrialisation Indicators | Existing analytical ledger, with explicit sources mapped to each area. | Existing paper sources; [management's reported call costs and rollout](https://www.fool.com/earnings/call-transcripts/2026/08/12/duolingo-duol-q2-2026-earnings-call-transcript/) and the [Q1 shareholder letter](https://investors.duolingo.com/static-files/ac220d7c-e313-4049-b309-1095fd24a86f), printed p. 4, rechecked. | The explanation row says free access was announced, avoiding an unverified universal account-level rollout. The episode increase retains a lower-bound qualification. No causal trade-off is claimed. |

All new visuals are original arrangements of factual information. No publisher figure, screenshot, logo, photograph, or distinctive illustration was copied or modified, so no reproduced-image permission or invented copyright notice is attached. The sources of the facts are credited in figure notes and the bibliography. Model-generated imagery was not used.

## Numeric inputs and calculations

`figures/visual-data.csv` is the complete numeric input for the two charts. It preserves units, qualifiers, citation keys, and source locators. `figures/render_charts.py` reads it directly; exported vector PDFs are checked in alongside the source so a normal LaTeX build does not require Python or Matplotlib.

For Figure 2:

| Analysis | Video Call | Regular lessons |
|---|---:|---:|
| Entered the 30-day conditions | 329 | 329 |
| Speaking analysis | 263 / 329 = 79.9% | 304 / 329 = 92.4% |
| Survey analysis | 261 / 329 = 79.3% | 297 / 329 = 90.3% |

The counts reconcile with the existing manuscript: 329 + 329 = 658; 263 + 304 = 567; 261 + 297 = 558. The gap between the initial and final counts combines study exclusions and missing follow-up. Nothing in this arithmetic shows which condition caused better learning.

For Figure 4, the inputs are 300 → 15,000+ episodes, 2 → 25+ courses, and 500,000 → 5,000,000 daily sessions. The last panel expresses sessions in millions per day. Each panel has its own labelled scale. The charts compare reported endpoints only; bar lengths are not used to compare unlike units across panels.

## Bibliographic metadata corrected

The original pages' visible headings and `author`/`article:published_time` metadata were inspected on 16 September. Publication and modification timestamps were kept distinct. The HTML sometimes supplies an SEO headline different from the visible H1; the paper retains the visible article title.

| Key | Correction |
|---|---|
| `roleplayDesign` | Parker Henry; 20 March 2024; Duolingo as site/publisher. |
| `explainFree` | Luis Mas Castillo; 1 January 2026; Duolingo as site/publisher. |
| `falstaff` | Duolingo Team; 14 January 2026; title aligned with the page's visible heading. |
| `falstaffResearch` | Audrey K. Kittredge and Xiangying Jiang; 10 March 2026. |
| `videoResearch` | Audrey K. Kittredge and Xiangying Jiang; 30 March 2026. |
| `duoradio` | Luis Mas Castillo, Sophie Mackey, and Cindy Berger; 11 March 2025. |

Retrieval dates were updated for these six records and for the two rechecked Henry workflow sources. No source was added merely to increase the reference count; it remains 45 distinct cited keys. These metadata corrections do not establish full-text verification of the remaining bibliography.

## APA basis

[Purdue OWL's APA 7 tables and figures guidance](https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/apa_tables_and_figures.html) was used for numbering, bold labels, italic titles, note placement, readable figure typography, and text callouts. The official APA figure/table pages were also requested, but the retrieved pages exposed only an iframe and did not supply usable guidance in this session. The school rubric requires APA acknowledgement and appropriate layout; it does not specify that this article must be converted into the complete APA student-paper template.

## Build and review

Normal build: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, with pdflatex, biber, and the packages declared in the preamble. The existing `latexmkrc` continues to produce `build/main.pdf`.

Optional chart regeneration: `python figures/render_charts.py`, with Matplotlib installed. Fonts use DejaVu Sans; black/grey fills and hatching distinguish series without depending on colour.

This workstation initially lacked the TeX tools on PATH. A temporary TinyTeX distribution and a temporary Python environment were used under `/tmp`, without changing project build settings or installing a system-wide toolchain. The bundled universal biber executable's ARM64 slice was extracted for execution because the system `lipo` launcher requested an unaccepted Xcode licence. No licence was accepted or system settings changed. Only the finished figure assets and paper outputs are project deliverables.

Final build/page/citation checks are recorded in `research/visual-validation.txt`. The separate `research/strict-rubric-review.md` records unresolved scholarly issues and course-process evidence; visual verification is not scholarly peer review.

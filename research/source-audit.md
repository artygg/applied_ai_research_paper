> Superseded for the current focused manuscript by `focused-review-audit.md`. Retained as historical provenance; the later audit also corrects the earlier self-efficacy cohort split.

> Historical audit of the September 9 technical draft. The September 11 user-experience rewrite supersedes its manuscript source count and scope; see `ux-review-audit.md` for current decisions and validation. Earlier records are retained for provenance.

# Source and requirement audit

Review date: September 9, 2026. This is a working verification record for the AI-assisted research draft in `main.tex`, not a preregistration or evidence of independent human review.

## September 9 update: new collection and verified additions

The paper now cites **42 distinct sources**: 32 in the original draft, plus 11 additions, minus the superseded FY2024 annual report. The original corpus account remains below to preserve the review history.

### What was actually supplied

`../duo-research/data/sources.json` contains **222 records with 222 unique IDs and primary URLs**, matching 96 + 81 + 45 records in the three part files. Its README says 223, so the count was recomputed rather than copied. The files contain annotations and bibliographic/link metadata, **not raw learner data, experimental outcomes, screenshots of model interactions, or full-text archives**. No empirical measurements were calculated from them.

The imported labels comprise 107 `duolingo`, 80 `independent`, 32 `press`, and 3 `mixed` records; 210 are labelled `verified` and 12 `blocked`. These are counts of supplied metadata, not validated estimates of the literature or results of this review's network checks. A URL's availability does not establish its authorship, peer-review status, or the truth of an annotation.

`inventory-review.csv` preserves a record-level disposition for all 222 leads:
- 11 entries supply newly cited sources with relevant passages verified.
- 5 entries match previously cited sources without a new source-level verification claim.
- 2 governance leads were investigated but not cited substantively.
- 204 remain discovery leads not added in this targeted update.

These are not PRISMA exclusion counts. Unselected entries were not all read in full; omission does not establish irrelevance, poor quality, or nonexistence. Exact-link matching was supplemented by the verified ACL DOI and versioned arXiv equivalents for the new additions. Research profiles, historical learning datasets, labour coverage, general effectiveness studies, and broad assessment literature were not automatically imported merely to increase the reference count.

### Source-to-claim map for additions

Canonical URLs and bibliographic details are recorded in `../references.bib`; original inventory URLs and access notes are in `inventory-review.csv`.

| Inventory ID | Citation key | Inspected primary material / locator | Use and limit |
|---|---|---|---|
| `malik24acl` | `malik2024` | ACL publisher PDF, Tables 1–2 and Sections 5–9 | Proficiency-control experiment. Not evidence of CALM deployment in consumer conversation. |
| `rive-lily` | `rive2025` | Rive interview, State Machine and technical-impact sections | Supplier-reported Lily animation implementation; not independent benchmarking. |
| `yancey23bea` | `yancey2023` | ACL PDF, Sections 2–3 | Calibrated essay scoring and group-sensitive evaluation; not feedback accuracy. |
| `catalan26lessons` | `catalan2026` | arXiv v2 HTML, Sections 3–4 | Five survey responses; no captured model outputs or causal feature comparison. |
| `blog-duoradio` | `duoradio` | Official article, scaling formula and evaluator sections | Offline generation/filtering/audio pipeline; not an asserted live-call architecture. |
| `det-blog-custodianship` | `custodianship2026` | Named-author article, February 26, 2026 | Governance argument, not an audit of consumer features. |
| `sl-q2-2026` | `shareholder2026` | Official shareholder-letter PDF, page 4 | Subscriber-access update; do not attribute the exact per-call cost/model claim to this passage. |
| `call-q1-2026`, **alternative URL only** | `earnings2026` | Q2 management transcript, August 5 event, answer to Nathan Feather | Management testimony hosted by The Motley Fool; not its editorial summary or an independent experiment. |
| `harrison25tutor` | `harrison2025` | SSRN abstract and metadata | Technology review; full text inaccessible. No detailed findings invented. |
| `duo-videocall-report` | `videoResearch` | Official research-summary webpage | Overlapping study summaries, not additional independent replications by default. |
| `10k-2025` | `annual2025` | SEC FY2025 filing, printed pages 39–40 | Updated risk disclosure; not evidence that risks materialized. |

For the transcript, management remarks were compared with the separate transcript on EarningsCall.biz. This cross-check does not replace checking the original audio and is not counted as another independent source. The call occurred **August 5, 2026**; the supplied hosting URL contains August 12. Because the exact webpage publication metadata was not exposed, the bibliography uses 2026 and identifies the call date in a note.

The targeted update additionally used the authors' official publication record and the official DET custodianship article to investigate standards references. The standards PDF did not yield a usable complete text. Its precise revision, report number, and claim of coverage are therefore not asserted from the inventory. A related arXiv record was inspected but not added as if a full standards audit had been performed. The consumer privacy page again exposed no substantive policy text.

### Corrections to the uploaded annotations

1. **Research is not deployment.** `malik24acl` describes a controllable-generation experiment. Its annotation's suggestion that this is the method behind deployed course content is not established by the inspected paper.
2. **Assessment is not consumer feedback.** `yancey23bea` is tagged as a generative feature but evaluates test essays. Its agreement statistic is not a percentage accuracy score for Explain My Answer.
3. **A supplier is not an independent reviewer.** Rive is a technology provider reporting a customer implementation. The paper uses its specific implementation evidence without importing the collection's generic `press` classification as independence.
4. **No absolute absence claims.** Statements such as “only peer-reviewed study,” “never audited,” or “no equivalent document” require a comprehensive search that was not conducted. They have not been added to the paper.
5. **No blanket end to open research releases.** The CALM paper states that code, data, and models are released. This prevents importing the collection's unqualified statement that no generative-era materials have been opened. It does not establish access to production app data.
6. **Correct source for cost and model claims.** The exact Video Call cost/model statement is in management's earnings-call answer, not the inspected shareholder-letter passage. Financial denominators, models, and evaluation protocols are not inferred where unspecified.
7. **Small external studies remain small.** Catalan et al. investigate perceptions; Harrison's abstract describes a technology review. Neither supports an independent causal efficacy or accuracy estimate.
8. **Documents are not independent studies.** The newer Video Call summary overlaps research already represented in the draft; the 42-source total is a bibliographic count.

### Interpretation and numeric safeguards

The revision retains reported measurement units and separates them from new proposals. CALM control error is a squared score difference, not learner improvement; its compute comparison rests on assumptions, not production invoices. Essay-rating agreement is a chance-adjusted statistic, not a feedback success percentage. Company cost claims remain attributed testimony. None of these findings supplies a feature-level accuracy rate or establishes that model substitution preserves educational outcomes.

The existing 8–10-page body requirement, English example structure, figure/table requirement, and APA setup remain in force. Layout and citation checks are reported at the end of this audit. The uploaded collection has not been edited or rebuilt: its original metadata and annotations remain available for comparison.

## Initial corpus and retrieval

The original reference list is preserved verbatim in `supplied-references.txt`. Bibliographic records, titles, and canonical URLs/DOIs are in `../references.bib`; the keys below connect this audit to the paper's citations.

- Starting list: 24 supplied URLs.
- Duplicate: the Feng et al. DOI and TU Delft PDF describe the same publication.
- Distinct supplied resources: 23.
- Excluded from substantive synthesis: the live Duolingo privacy page, whose policy text could not be inspected.
- Retained supplied resources: 22, including sources with partial access.
- Supplementary sources cited: 10.
- Total distinct sources cited in the initial draft: 32. The revision below expands this to 42.

Retrieval used supplied links, publisher and institutional equivalents, and targeted web searches for titles, DOIs, feature names, and technical terms. It did not use a systematic database export. The queries mentioned in the Method are examples of targeted retrieval, not a complete reproducible database-search strategy. A complete timestamped query-by-query log was not exported. Direct network retrieval through the shell was blocked; browser-tool retrieval and primary-source indexed passages provided the material used. Successful access to a page or PDF does not mean that every paragraph or table was reviewed.

No learners were recruited, product experiments conducted, API performance measured, independent second reviewer engaged, or meta-analysis calculated. The proposed metrics and process diagram are the review's analytical contributions, not observations of production infrastructure.

### Supplied sources retained

“Relevant text” means inspected source passages supporting the cited claims, not a full independent replication. Restricted access is explicitly identified below.

| Original URL position | Bibliography key | Source type | Access and permitted use |
|---|---|---|---|
| 1 | `openaiDuolingo` | Provider case study | Relevant text; historical model and feature attribution, not a current deployment inventory. |
| 2 | `roleplayDesign` | Product/engineering explanation | Relevant text; simplified prompt and dialogue examples, not internal source code. |
| 3 | `henry2025` | Named-author engineering explanation | Relevant text; prompt roles, dialogue stages, and transcript-derived context. |
| 4 | `videoCall` | Mutable product page | Relevant text; described interaction design, with version and availability caveats. |
| 5 | `explainFree` | Mutable product announcement | Relevant text; new availability and functionality, not an undisclosed backend attribution. |
| 6 | `falstaff` | Mutable product announcement | Relevant text; guided speaking design, not proof of universal rollout. |
| 7 | `kittredge2025self` | Journal study | Article text including relevant methods; self-report evidence kept separate from proficiency and accuracy. |
| 8 | `luo2026` | Journal study | Publisher PDF, abstract, and selected text; no uninspected numerical tables reconstructed. |
| 9 | `lin2024` | Journal study | Publisher author-page abstract; full article unavailable. No inferred sample details or effect sizes. |
| 10 | `du2024` | Systematic review | Publisher/institutional abstract-level material; not treated as Duolingo implementation evidence. |
| 11 | `lyu2025` | Meta-analysis | Publisher text and reported summary statistics; pooled chatbot effect not transferred to Duolingo. |
| 12 | `yan2024` | Multiple-case study | Primary indexed abstract and methods passages; access incomplete. Only inspected details used. |
| 13 | `gpt4` | Model technical report | Relevant report text; general capabilities and disclosure limits, not proprietary architecture reconstruction. |
| 14 | `visemes` | Engineering explanation | Relevant text; course-content animation pipeline, not verified live-call architecture. |
| 15 | `kittredge2025video` | Company research report | Indexed passages from the original report; full PDF retrieval unsuccessful. Verify against an uploaded complete copy. |
| 16 | `crosthwaite2026` | Scoping review | Publisher text; educational feedback research context, not product component validation. |
| 17 and 18 | `feng2024` | Speech-recognition research | Publisher/repository material; one deduplicated work. Not a test of Duolingo's recognizer. |
| 19 | `kobayashi2024` | NLP evaluation research | ACL publication record and abstract; measurement distinctions, not Duolingo benchmark scores. |
| 20 | `fathi2024` | Language-learning study | Publisher abstract/preview; Andy English Chatbot, not Duolingo or demonstrated GPT use. |
| 21 | `cefr` | Official framework resource | Council of Europe webpage; general framework reference, not a complete review of descriptor volumes. |
| 22 | `shi2024` | Systematic review | Publisher text including search scope; not all reviewed systems are generative AI. |
| 23 | `freeman2023` | Company pedagogical report | Report text; instructional rationale, not independent validation of subsequent features. |

### Supplied source not used substantively

| Original URL position | Resource | Disposition |
|---|---|---|
| 24 | Duolingo live privacy policy | Policy text inaccessible. No claim about current retention periods, vendor training permissions, or legal compliance. Upload a dated full copy for substantive analysis. |

The raw URL remains in `supplied-references.txt`. It is not inserted into the bibliography as if its contents had been reviewed.

### Supplementary sources

| Bibliography key | Source type | Purpose and boundary |
|---|---|---|
| `max` | Official product page | Feature context and reported human involvement; mutable text is not frozen to the original launch date. |
| `voices` | Official engineering page | Character-voice production context; no inference about the current live-call provider. |
| `finops` | Official engineering page | Reported infrastructure and cost optimization; not learning or latency measurements. |
| `highlights2025` | Official annual product summary | Described interface updates; not proof that every account has every option. |
| `falstaffResearch` | Company research summary | Limited beginner-learning context; allocation, sample, and effect estimates not supplied in inspected text. |
| `contentProduction` | Official engineering page | Distinguishes content production and exercise selection from live generative interaction. |
| `vaswani2017` | Original Transformer paper | General model foundations; does not disclose GPT-4's complete implementation. |
| `gpt4o` | Provider system card | General multimodal capabilities; not proof of Duolingo's end-to-end speech architecture. |
| `speakingOverview` | Official pedagogical explanation | Distinguishes ordinary speaking tasks from generative conversation. |
| `annual2024` (retired in update) | Company SEC filing | Replaced by `annual2025`, the FY2025 filing; original retrieval retained here for provenance. |

## Bibliographic and temporal safeguards

- Retrieval cutoff and issue year are different. Some articles published online in 2025 appear in 2026 journal issues; the bibliography follows the verified issue metadata.
- Historical GPT-4 attribution does not establish the model serving every current feature. The GPT-4o claim is limited to the 2025 study; the update adds a separately attributed 2026 management account of movement toward open-source models.
- Mutable product pages may contain updates added after their original launch. No exact current availability matrix is asserted.
- Missing personal bylines and dates have not been invented. Institutional attribution and `n.d.` are provisional fallbacks for pages whose metadata was unavailable through retrieval; check the visible original bylines and dates before submission.
- The `voices` record uses a descriptive page title where fuller title metadata was not exposed; confirm it on the original page.
- The video study's participant-flow figures are taken from indexed report passages rather than silently treating the analysed sample as everyone originally assigned. Check those passages, report date, and reported scale against a complete copy before submission.
- The paper does not assign undocumented architectures, prompts, speech vendors, retrieval infrastructure, or fine-tuning to consumer features. Fine-tuning is discussed where explicitly documented in the CALM research prototype, not inferred as a deployed feature component.

## Alignment with uploaded requirements

| Requirement | Uploaded source/location | Draft implementation |
|---|---|---|
| Abstract, introduction, method, results, conclusion/discussion, references | `../prism-uploads/APPENDIX 9 ASSESSMENT RESEARCH PAPER.pdf`, PDF page 4 | All sections present; English text follows the supplied Dutch example's organization. |
| 8–10-page body excluding introduction, method, conclusion, discussion, references | Assessment form, PDF page 4, footnote 3 | Compiled Results spans numbered pages 5–14: 10 pages. Total PDF is 22 pages including front matter and references. |
| Relevant figures and tables explicitly used | Assessment form, PDF page 4 | One discussed conceptual process diagram; three discussed tables on functions, claim boundaries, and proposed metrics. |
| APA referencing | Assessment form, PDF page 4 | `biblatex` APA with Biber; 42 cited entries. Missing webpage metadata remains a human verification item. |
| Relevance, research questions, scope, reading guide | Assessment form, PDF page 5 | Introduction explicitly covers each; focus is technologies and application, not a causal effectiveness verdict. |
| Explained sampling, collection, instruments, analysis | Assessment form, PDF page 5 | Method adapts these to a document review, with corpus accounting, extraction dimensions, and access limits. No learner sample invented. |
| Depth, source quality, synthesis | Assessment form, PDF page 5 | Results connects features, model boundaries, prompts, speech, memory, instructional design, and component-level limitations. |
| Standalone conclusions, reliability, validity, usefulness | Assessment form, PDF page 5 | Conclusion answers the questions; Discussion appraises reliability/validity and gives audience-specific recommendations. |
| Pair work and lecturer-approved proposal | `../prism-uploads/APPLIED AI MODULE BOOK V1.pdf`, research-paper guidance, PDF pages 47–48 | Two author fields retained. Actual names, numbers, and approval status must be supplied. |
| Week-3 peer review | Module book research-paper guidance | A real peer review must be completed and documented by the students; no claim of completion is made. |
| Example structure | `../Onderzoek .pdf` | Separate title/abstract/contents, two-column body, Method, Results, combined Conclusion and Discussion, References. |

These are alignment checks, not a guarantee of a grade or lecturer acceptance. The assignment's page wording is unusually specific; if the lecturer intends a different body definition, confirm it before altering the layout.

## Required human checks before submission

1. Supply both authors' names and student numbers, and confirm lecturer approval of the revised title and questions.
2. Check the course's AI-use and disclosure rules and retain an accurate authorship/process statement.
3. Obtain full copies of access-limited research, especially the Video Call report, before extending claims beyond inspected passages.
4. Upload the dated privacy-policy text if the paper should discuss actual data-retention or training permissions rather than identify the evidence gap.
5. Verify cited passages, personal bylines, dates, and bibliography formatting against original sources; refine the authors' analysis rather than treating this draft as independently verified scholarship.
6. Complete the required peer review and retain the actual evidence in the appropriate portfolio.

## Build check

Built with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` using Biber. Final LaTeX log has no undefined citation/reference warnings or overfull boxes. The revised diagram, technical-analysis page, metrics table, and bibliography page were rendered outside the project and visually checked. The revised PDF has 22 physical pages; Results occupies numbered pages 5–14 (10 pages). All 42 bibliography entries are cited, and all 222 inventory records have a recorded disposition. The source audit does not form part of the assessed page count.
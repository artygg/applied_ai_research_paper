# Source log: user-experience paper (`main.tex`)

Review date: 14 September 2026. This log accompanies the rewrite of the paper around the main question
*How does generative AI transform the Duolingo user experience?* and three sub-questions
(what changed / what can be shown / enrichment or industrialisation). It builds on the earlier audits in
this folder, which remain the record for sources verified on 9-11 September 2026.

The paper cites 45 sources. No learners were recruited, no product outputs were measured, and no pooled
estimates were calculated. This is AI-assisted targeted verification, not a systematic review or an
independent second-reviewer appraisal.

## Sources checked in this revision

| Key | Access on 14 Sep 2026 | Used for | Limit |
|---|---|---|---|
| `contentProduction` | Company blog, full text | Workflow: designer plans lesson, model drafts 10 exercises, designer keeps 3; experts have final say | Byline Parker Henry, dated 22 June 2023 (bib updated; inventory said 2024) |
| `duoradio` | Company blog, full text | Late-2023 launch; 2024 hackathon; evaluator prompts; 300 -> 15,000+ episodes, 2 -> 25+ courses, 500K -> 5M daily sessions, 99% cost saving | Company-reported figures; no listening-outcome measure in the account |
| `henry2025` | Company blog, full text | Learning Designers write system instructions; opener/first question/conversation/closer; post-call facts; CEFR level | Design description, not effect evidence |
| `malikTechcrunch2025` (new) | TechCrunch, full text | CEO contrast of ~12 years for first 100 courses vs ~1 year for ~150; beginner focus; Stories and DuoRadio; user criticism | Press report; user criticism is not a quality measurement |
| `courses2025` | IR release timed out in this session | Date and count, verified in `ux-review-audit.md` | Quote attributed to TechCrunch instead |
| `catalan2026` | arXiv v2 HTML | 5 software engineers (Philippines, Korean class); Qualtrics survey; general vs work scenarios; want personalisation | Authors do not verify which lessons were LLM-generated |
| `hardman2025` | Substack essay, full text | Human-AI collaboration framing; designer roles; call for guardrails against engagement over learning | Practitioner commentary |
| `toczauer` | OnlineEducation.com, full text | Michael Trucano (Brookings) on low-quality output, contextual relevance, translation, engagement vs learning | Secondary citation of interview testimony; undated page |
| `maass2026` (new) | Publisher page, abstract | 8-week iOS observational case study; streaks, freezes, social, reminders, rewards; retention vs dependency | Abstract-level |
| `espinosa2026` | SSRN blocked (403); abstract via search index | SDT + dark-patterns critique | Abstract-level, conceptual essay |
| `sudina2025` | Publisher blocked; abstract via search index | 601 beginners, 6 months; attrition best predicted by L2 grit perseverance of effort and log(age) | Direction of effects not stated in accessible text, so not claimed |
| `yancey2020` | Author PDF, full text | Hand-written templates; reward = lesson within 2 h; +0.5% DAU, +2% new-user retention | Pre-generative engagement optimisation |
| `earnings2026` | Motley Fool transcript | Video Call cost ~$0.30 -> under $0.01 with open-source models; DAU +23% YoY (Q2 2026); Super access | Management testimony, extracted via summarising fetch; verify wording against transcript before quoting |
| `saarela2026` | Springer blocked; abstract via search index + earlier audit | 51 studies; heterogeneity and small-study effects (earlier audit); moderators: informal settings, productive skills, less commonly taught languages | Moderator claims abstract-level |
| `liReview2025` | ScienceDirect blocked; abstract via DOAJ/search index | 144 articles 2023-2024; higher education 86.7%; EFL 86.1%; writing 42.4%; few longitudinal studies | **Correction:** inventory note said writing = 51.3%; the abstract says 42.4% |
| `lee2024` | University repository, abstract | 61 samples / 17 projects, N = 8,282; between-group d = 0.39, within-group d = 1.18; Duolingo named among platforms | AI-guided individualised learning, not generative AI |
| `zeng2024` | ERIC abstract | 20 Year 8 students, 6 weeks, questionnaires and interviews; activity-specific intrinsic motivation transfers | General app use |
| `zhao2024` | Publisher abstract via search index | Random assignment, Duolingo n = 33 vs HelloTalk n = 34, five weeks, WTC | WTC findings not accessed, so not claimed |
| `mohebbi2025` | Abstract via search index | 18 studies 2009-2024; gains in independence with explicit self-regulation instruction and scaffolding | Broad AI, not generative only |

Sources carried over from the focused paper (`kittredge2025self`, `kittredge2025video`, `videoResearch`,
`falstaffResearch`, `shareholderQ12026`, `wangConversation2024`, `celik2025`, `liTeacher2026`,
`loEngagement2024`, `yan2024`, `liMeta2025`, `liTask2026`, `harrison2025`, `xu2025`, `ouyang2024`,
`liBonk2025`, `shortt2023`, `freeman2023`, `maxLaunch`, `duocon2024`, `android2025`, `explainFree`,
`explainAccess2025`, `falstaff`, `roleplayDesign`, `malik2024`) rely on the checks in
`focused-review-audit.md` and `ux-review-audit.md`.

## Corrections to the outline supplied for this rewrite

- LLM-assisted lesson creation is documented from **22 June 2023**, not 2024.
- DuoRadio **launched in late 2023**; generative scaling followed in 2024.
- Video Call was **announced 24 September 2024** (Android expansion 16 January 2025), not 2025.
- Explain My Answer was **announced on 29 December 2025 as free from 1 January 2026**.
- Writing share in the 2023-2024 systematic review is **42.4%**, not 51.3%.
- `xu2025` cannot be used as evidence about generative features (exposure unverified), and its
  inventory sample/effect claims are not imported.
- `maass2026` was previously uncited because its text could not be obtained; its abstract is now
  accessible and is used at abstract level.

## Length requirement

The assessment form requires an 8-10 page body (Results only). The outline's ~3,500-word total would
give a Results section of roughly 5-6 pages in this layout, so the RQ proportions were kept
(RQ2 largest) but scaled up. Build and page checks are reported in the conversation / commit message.

## Remaining author checks

Author names, student numbers, lecturer approval of the new title and questions, course AI-use rules,
the required peer review, and a human check of the cited passages (especially abstract-level and
summarised-transcript sources above) remain outstanding.

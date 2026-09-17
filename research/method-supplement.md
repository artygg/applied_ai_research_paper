# Research-method supplement

Paper: *How Generative AI Transforms the Duolingo User Experience: What Changed, What Can Be Shown, and Whom It Serves*. Revision: 16 September 2026.

This supplement and [current-source-register.csv](current-source-register.csv) accompany the paper. They document a focused, purposive documentary review. The register was reconstructed on 16 September from the final citations, the existing inventory, and saved verification logs; it is not a contemporaneous screening export. It does not claim exhaustive retrieval, duplicate human extraction, learner observation, or a new meta-analysis.

## Selection and provenance

The discovery collection in `duo-research/data/sources.json` contains 222 records. The revised paper cites 45 documents. Of those, 32 have a documented link to 31 distinct inventory records; the other 13 are documented in targeted-retrieval logs without an identified inventory match. One inventory record (`pr-148`) links both a company release and a separate TechCrunch report. Another (`call-q1-2026`) has the cited Q2 transcript as its alternate URL. Neither should be mistaken for a duplicate publication. These are retrospective correspondence counts, not a search flow or exclusion count.

Matching used normalised DOI/URL equality first (scheme, `www.`, DOI resolver prefix and trailing slash ignored). Four matches required documented identity checks: the versioned Catalan arXiv paper, the Malik ACL identifier, the Zeng ERIC title/author record, and the Li research-map publisher record. The CSV identifies these exceptions. Unmatched does not necessarily mean newly discovered on a particular day: complete original discovery dates are not recorded.

Sources were retained for a dated product event or mechanism (RQ1), learner evidence or a relevant synthesis (RQ2), or an explicitly attributed interpretation/operational indicator (RQ3). Older baseline sources establish what generation changed. Documents concerning the English Test, non-language courses, or unrelated topics were outside scope. A general Duolingo study could remain as context when generative exposure was unverified, but was not coded as a feature evaluation. Commentary could inform an interpretation, but could not establish measured harm or benefit.

The unselected inventory leads were not all assessed in full. No count of full-text exclusions, comprehensive result sets, or screening agreement can be reconstructed. Historical source labels such as “verified” and annotations such as “only study” were not accepted as quality findings. Earlier sample, date, and writing-share errors were corrected against accessible original material; the CSV records consequential examples.

## Retrieval record

Historical logs preserve targeted original-source retrieval, including publisher/company pages, author-hosted PDFs, exact-title/DOI searches, and indexed original passages where direct downloads failed:

- `source-audit.md`: 9 September, including inventory disposition, original supplied references, and technical sources.
- `ux-review-audit.md`: 11 September, product chronology and broader learner evidence.
- `focused-review-audit.md`: 11 September, methods and measurement checks for direct and comparable studies.
- `ux-source-log.md`: 14 September, restoration of the user-experience scope and selected rechecks.
- `figure-source-audit.md`: 16 September, visual inputs, primary metadata, and calculations.

These files describe earlier versions. Their historical manuscript counts and verdicts must not be substituted for the current register. A date on a log identifies the recorded review session, not necessarily the first discovery date of every source.

The 11 September log records these targeted query strings:

```text
Duolingo "Video Call" confidence engagement study 2026 2025
"Duolingo Max" "Roleplay" "study" confidence independent
"ChatGPT" "learner engagement" "Yan" "2024" feedback
"ChatGPT" "engagement" "Lo" "Hew" "Jong" 2024 systematic review
"ChatGPT" "speaking" "self-efficacy" randomized trial language 2025
"ChatGPT" "voice" "anxiety" "willingness" language study 2025 2026
```

It also records exact-title/DOI queries and original-report URL-restricted searches for `confidence`, `658`, `567`, and `random`. No result counts, individual execution timestamps, or comprehensive database coverage are inferred from that record.

### Checks completed in the present substantive revision, 16 September

| Original source and locator | Access and finding | Revision decision |
|---|---|---|
| [Li et al., DOI 10.1111/jcal.70060](https://onlinelibrary.wiley.com/doi/10.1111/jcal.70060), abstract Methods/Results | Publisher abstract reports 41 experimental/quasi-experimental studies and 3,515 participants. The full-text link redirected to an abstract. The numerical effect is labelled only “ES”; the metric and detailed comparator/bias appraisal remain unresolved. | Omit the numerical effect and interval; retain the attributed positive finding and sample scope with an explicit access limit. |
| [Saarela et al., DOI 10.1007/s10791-026-10015-1](https://link.springer.com/article/10.1007/s10791-026-10015-1), Sections 3.1–3.3 and 4.1–4.4 | Original Methods/Results passages are accessible. Comparators include non-generative tools, ordinary instruction, and standard curricula. Section 4.3 gives an overall random-effects Hedges' g of 0.81 (95% CI 0.61–1.02), I² = 98.4%, and significant small-study effects. Section 4.1 gives different domain-specific estimates. | Identify the overall estimate and its exact section. Preserve bias and heterogeneity caveats; moderator patterns generate hypotheses rather than validate transfer to Duolingo. |
| [Henry's lesson-production account](https://blog.duolingo.com/large-language-model-duolingo-lessons/), opening explanation, “How AI helps us create lessons,” and Steps 1–3 | Original webpage explains text continuation, adaptive exercise selection, prompting, and human selection/editing. | Add a short mechanism explanation in the Introduction; retain the existing workflow figure. |
| [Maaß design case study](https://www.wr-publishing.org/index.php/ijmat/article/view/908), method and interpretation | Full publisher PDF obtained during the preceding strict review on 16 September; method describes eight-week iOS design observation in December 2025–January 2026. It is not a longitudinal learner cohort. | Attribute dependency as an interpretation and remove the paper's unsupported comparative outcome claim. This is use of the same-day inspected PDF, not another independent verification. |
| [Japanese Video Call report](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_video_call_improves_speaking_2025.pdf), Sections 2.2–2.3, Tables 1/3/4, and Conclusion | During the separate AI-agent review, further original indexed passages confirmed stratified random assignment, the Versant Speaking and Listening Test, an adapted nine-item pre/post WTC scale, and post-only confidence perceptions. Table 4 gives mean total learning hours over 30 days: 13.05 for 263 analysed call users, 9.11 for 304 controls. | Give randomisation explicit credit while retaining post-assignment exclusion and unequal-practice caveats. Do not present the interaction-model coefficient as an unconditional effect. The separate review records its source checks. |
| Four company blog entries: `roleplayDesign`, `explainFree`, `falstaffResearch`, `videoResearch` | The second agent checked visible H1 titles against the byline dates and authors in original HTML; the bibliography had used search/SEO titles for these entries. | Replace the four titles with visible article titles, retain verified author/date metadata, and synchronise the register. Protect the capital A after the question mark in the Li meta-analysis title for APA rendering. |
| [Ouyang et al. publisher record](https://www.irrodl.org/index.php/irrodl/article/view/7677) and [ACM/Crossref record for Yancey and Settles](https://api.crossref.org/works/10.1145/3394486.3403351) | The second agent verified page ranges of 97–115 and 3008–3016 respectively. Ouyang's 80-person sample comprises two 40-student classes, including a non-Duolingo control. | Add missing page ranges; describe 80 EFL learners rather than 80 app users. These checks refine metadata and sample description without importing new effects. |

The current revision also checked all 45 cited keys against the register and bibliography. That is a coverage check, not fresh full-text verification of all 45 sources.

## Codebook and appraisal decisions

| Field or rule | Operational meaning |
|---|---|
| Unit | A cited document. Documents, cohorts, reports, and independent experiments are not interchangeable counts. |
| RQ relevance | 1 = baseline/product change; 2 = learner effects and comparable research; 3 = capability, production, access, incentives, or interpretation. A source may serve several questions. |
| Specificity | Confirmed feature requires a named generative intervention in inspected text. General Duolingo means feature exposure is unverified or the source concerns the older app. Other AI means a different tool/setting or a broad synthesis. Technical generation research does not establish deployment. |
| Source relationship | Company authorship, company-affiliated research, external study, external commentary, and external reporting of company statements are kept distinct. External hosting does not make company metrics independent. Authorship alone is not a quality score. |
| Access | Whole original text available; selected original passages; abstract/metadata; or indexed original passages. Availability does not mean every passage was appraised. Historical checks are identified by their saved log. |
| Motivation | Reasons for starting or persisting in learning. Activity counts alone do not measure motivation. |
| Self-efficacy | Perceived capability for specified tasks. Record selected items, response transformation, and pre/post timing where inspectable. |
| Willingness to communicate | Readiness or intention to communicate. It is not interchangeable with self-efficacy. |
| Confidence perceptions | A source's confidence self-report; a post-use perception is not a change score. Incomplete instrument/timing details remain explicit. |
| Engagement | Behavioural participation, emotional involvement, cognitive investment; agentic engagement where the source reports it. Spoken-word counts indicate participation and cannot establish learning or deep engagement. |
| Performance | Demonstrated task performance. Record whether tasks concern practised phrases or unrehearsed transfer. |
| Timing and comparison | Keep baseline/post-test, post-only perceptions, aggregate trends, controlled contrasts, and within-group changes separate. Missing allocation or instrument information is unresolved, not inferred. |
| Capability enrichment | Documented additional practice or support. It does not, by definition, establish educational benefit. |
| Demonstrated learner benefit | A measured favourable outcome interpreted within design, comparator, selection, and measurement limits. Positive association need not establish causation. |
| Industrialisation | Reported production/delivery volume, speed, or cost. No automatic judgement about quality follows. |
| Appraisal | Check exposure match, attribution/comparator, construct match, and generalisability. Record the permitted use and limiting inference for every source. No composite quality score is calculated. |
| Ambiguity | Use the narrower inspected claim; preserve unresolved details. Do not replace unavailable primary details with inventory annotations. |
| Overlap | Multiple company summaries may describe the same study; syntheses may share primary studies. Do not count them as independent replications or add participant totals. Review overlap was not exhaustively reconstructed. |
| Null findings | “Not statistically significant” does not establish equivalence or absence of an effect. |

### Worked coding example

`kittredge2025video` is a **confirmed Video Call intervention**, **company-authored**, accessed through **indexed original-report passages**. The report describes stratified random assignment to 30-day conditions, with regular lessons as the comparison. Its entering population is 658, but speaking and survey analyses use 567 and 558 respectively. Figure 2 has separate condition counts; chart percentages divide each analysis count by 329. Those proportions represent analysis inclusion under imposed usage requirements, not natural app retention and not treatment-effect sizes.

The report supports an attributed short-term speaking advantage among analysed learners on the Versant test. Stable willingness to communicate (adapted nine-item pre/post scale) and neutral post-only confidence perceptions are separate outcomes. The latter cannot establish no change in confidence. Differential weekly exclusions limit generalisation to everyone offered the feature; unequal mean total practice time limits format-only attribution. The Table 3 regression includes interactions, so its coefficient is not adopted as an unconditional effect. The source therefore informs RQ2 without demonstrating durable improvement, unbiased population benefit, or internal company priorities.

### How to read the CSV

Each of the 45 rows supplies a citation key and title, original URL/DOI, inventory correspondence, RQ relevance, document type, specificity, source relationship, access scope and verification record, original-source locator, design/measure/timing information, inclusion rationale, and claim limit. “Not inspected,” “unresolved,” and “not applicable” are limitations, not negative study findings. The final bibliography remains the APA citation list; the CSV is the audit instrument.

## Submission and responsibility

Supply the two supplement files together with the paper so that its Method section's source-register reference is usable. The required lecturer approval, assigned student peer review, portfolio feedback, and Teams submission process are separate course requirements; an AI manuscript review does not establish or replace them. The authors remain responsible for source accuracy and final submission.

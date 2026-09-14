# Duolingo & AI — Annotated Source Inventory

Sources connecting Duolingo and AI, 2015–2026, with the emphasis on 2020 onward. Built for an academic literature review: peer-reviewed work is listed first within each section, and every entry is tagged with who wrote it.

**222 sources.** Every URL was checked programmatically. `bot-blocked` means the publisher refuses scripted requests — the link is live in a browser. Nothing is listed without a resolving URL.

> **Read the provenance tag before citing.** A large share of the research on Duolingo's AI is written by Duolingo. That does not make it wrong, but Duolingo-authored and independent evidence should never be pooled without comment.

## At a glance

| | Count |
|---|---|
| Total sources | 222 |
| Peer-reviewed | 102 |
| Direct PDF available | 125 |
| Duolingo-authored | 107 |
| Mixed Duolingo/external authorship | 3 |
| Independent | 80 |
| Press / third-party non-academic | 32 |

## Foundations: the pre-LLM ML stack

*13 sources*

- **[Identifying and Analyzing 'Noisy' Spelling Errors in a Second Language Corpus](https://aclanthology.org/2025.wnut-1.4/)** — B. Naismith, A. Juffs — *W-NUT 2025*, 2025
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://aclanthology.org/2025.wnut-1.4.pdf>
  <br/>Learner-corpus error analysis.
- **[Exploring Neural Entity Representations for Semantic Information](https://research.duolingo.com/papers/runge.blackboxnlp20.pdf)** — A. Runge, E. Hovy — *BlackboxNLP @ EMNLP 2020*, 2020
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Interpretability of entity embeddings.
- **[Ongoing Cognitive Processing Influences Precise Eye-Movement Targets in Reading](https://research.duolingo.com/papers/bicknell.ps20.pdf)** — K. Bicknell, R. Levy, K. Rayner — *Psychological Science*, 2020
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Reading cognition.
- **[A Rational Model of Word Skipping in Reading](https://research.duolingo.com/papers/duan.cogsci19.pdf)** — Y. Duan, K. Bicknell — *CogSci 2019*, 2019
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Eye-movement / reading modelling.
- **[Influence of Speaking Style Adaptations and Semantic Context on the Time Course of Word Recognition](https://research.duolingo.com/papers/vanderfeest.jp19.pdf)** — S.V.H. van der Feest, C.P. Blanco, R. Smiljanic — *Journal of Phonetics*, 2019
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Speech perception; relevant to ASR-graded listening exercises.
- **[Learning from Omission](https://research.duolingo.com/papers/mcdowell.acl19.pdf)** — B. McDowell, N. Goodman — *ACL 2019*, 2019
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Pragmatic inference from what speakers leave out.
- **[Observing the Emergence of Constructional Knowledge](https://research.duolingo.com/papers/romer.ssla19.pdf)** — U. Roemer, C.M. Berger — *Studies in Second Language Acquisition*, 2019
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Construction learning in L2; SLA-side evidence.
- **[Using LSTMs to Assess the Obligatoriness of Phonological Distinctive Features for Phonotactic Learning](https://research.duolingo.com/papers/mirea.acl19.pdf)** — N. Mirea, K. Bicknell — *ACL 2019*, 2019
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://aclanthology.org/P19-1155/>
  <br/>Neural phonotactics; Bicknell (later Head of AI) on core NLP.
- **[A Trainable Spaced Repetition Model for Language Learning](https://research.duolingo.com/papers/settles.acl16.pdf)** — B. Settles, B. Meeder — *ACL 2016*, 2016
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.18653/v1/P16-1174](https://doi.org/10.18653/v1/P16-1174)`
  <br/>Alt: <https://aclanthology.org/P16-1174/>
  <br/>Half-life regression (HLR). The most-cited Duolingo paper and the origin of its personalisation stack.
- **[Difficulty in Learning Similar-Sounding Words](https://research.duolingo.com/papers/pajak.jep16.pdf)** — B. Pajak, S.C. Creel, R. Levy — *J. Experimental Psychology*, 2016
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Phonological confusability; feeds difficulty estimation.
- **[Learning Additional Languages As Hierarchical Probabilistic Inference](https://research.duolingo.com/papers/pajak.ll16.pdf)** — B. Pajak, A.B. Fine, D.F. Kleinschmidt, T.F. Jaeger — *Language Learning*, 2016
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Duolingo's theoretical account of L2 acquisition; the learning-science frame behind curriculum design.
- **[Self-directed Learning Favors Local, Rather Than Global, Uncertainty](https://research.duolingo.com/papers/markant.cogsci16.pdf)** — D.B. Markant, B. Settles, T.M. Gureckis — *Cognitive Science*, 2016
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Active-learning theory behind how the app selects what to show next.
- **[Mixture Modeling of Individual Learning Curves](https://research.duolingo.com/papers/streeter.edm15.pdf)** — M. Streeter — *EDM 2015 (Best Paper)*, 2015
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Early learning-curve modelling; precursor to the adaptive engine.

## Adaptive learning & personalisation (Birdbrain)

*6 sources*

- **[Duolingo Evolution: From Automation to Artificial Intelligence](https://doi.org/10.1109/colcaci63187.2024.10666523)** — J. Vega, M. Rodriguez, E. Check, H.W. Moran, L. Loo — *IEEE ColCACI 2024*, 2024
  <br/>`peer-reviewed · DOI [10.1109/ColCACI63187.2024.10666523](https://doi.org/10.1109/ColCACI63187.2024.10666523)`
  <br/>Alt: <https://doi.org/10.1007/978-3-031-88854-0_5>
  <br/>External engineering-history account of the automation-to-AI shift. Extended version in Springer CCIS 2025.
- **[A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications](https://research.duolingo.com/papers/yancey.kdd20.pdf)** — K.P. Yancey, B. Settles — *KDD 2020*, 2020
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.1145/3394486.3403351](https://doi.org/10.1145/3394486.3403351)`
  <br/>Bandit-optimised push notifications: engagement-optimisation AI rather than learning AI. A useful tension.
- **[AWS AI | Duolingo (customer case studies)](https://aws.amazon.com/machine-learning/customers/innovators/duolingo/)** — Amazon Web Services — *AWS*, 2023
  <br/>`PDF · not peer-reviewed`
  <br/>Alt: <https://d1.awsstatic.com/case-studies/partner-case-studies/Duolingo%20PDF.pdf>
  <br/>AWS's account of the PyTorch/EC2 training stack for non-native ASR and automated scoring. Infrastructure-economics detail in the PDF.
- **[Duolingo's Biggest Technology Innovations](https://blog.duolingo.com/duolingo-technology-innovations/)** — Duolingo — *Duolingo blog*, 2023
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://blog.duolingo.com/unique-engineering-problems/>
  <br/>Overview including Birdbrain personalisation.
- **[How Duolingo's AI Learns What You Need to Learn](https://spectrum.ieee.org/duolingo)** — K. Bicknell, C. Brust, B. Settles — *IEEE Spectrum 60(3)*, 2023
  <br/>`not peer-reviewed · Duolingo-authored · DOI [10.1109/MSPEC.2023.10061631](https://doi.org/10.1109/MSPEC.2023.10061631)`
  <br/>Alt: <https://ieeexplore.ieee.org/abstract/document/10061631>
  <br/>KEY. The ONLY substantive public description of Birdbrain. Not peer-reviewed, never externally audited.
- **[Learning how to help you learn: Introducing Birdbrain!](https://blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain/)** — K. Bicknell, C. Brust — *Duolingo blog*, 2020
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>The original Birdbrain announcement. Primary source for the pre-LLM AI story.

## Generative AI features (Max, Roleplay, Video Call, AI-authored content)

*25 sources*

- **[Evaluating the Impact of AI Tools on Language Proficiency and Intercultural Communication in Second Language Education](https://doi.org/10.33422/ijsfle.v3i1.768)** — M.S. Fountoulakis — *International Journal of Second and Foreign Language Education 3(1)*, 2025
  <br/>`PDF · peer-reviewed · DOI [10.33422/ijsfle.v3i1.768](https://doi.org/10.33422/ijsfle.v3i1.768)`
  <br/>Alt: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5355281>
  <br/>Open access.
- **[Mobile language app learners' self-efficacy increases after using generative AI](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1499497/full)** — A.K. Kittredge, E.W.M. Hopman, B. Reuveni, D. Dionne, C. Freeman, X. Jiang — *Frontiers in Education*, 2025
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.3389/feduc.2025.1499497](https://doi.org/10.3389/feduc.2025.1499497)`
  <br/>CRITICAL. The ONLY peer-reviewed study of Roleplay/Explain My Answer - and it is entirely in-house, self-report, and measures self-efficacy rather than proficiency.
- **[Span Labeling with Large Language Models: Shell vs. Meat](https://aclanthology.org/2025.bea-1.62/)** — P. Mulcaire, N. Madnani — *BEA @ ACL 2025*, 2025
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://aclanthology.org/2025.bea-1.62.pdf>
  <br/>LLMs for span annotation of shell vs content language.
- **[Uncurtaining windows of motivation, enjoyment, critical thinking, and autonomy in AI-integrated education: Duolingo vs. ChatGPT](https://doi.org/10.1016/j.lmot.2025.102100)** — J. Xu, Q. Liu — *Learning and Motivation*, 2025
  <br/>`peer-reviewed · DOI [10.1016/j.lmot.2025.102100](https://doi.org/10.1016/j.lmot.2025.102100)`
  <br/>HIGH-SIGNAL. True experiment, 3 groups (n=81/81/82). No significant difference between Duolingo and raw ChatGPT on critical thinking and autonomy.
- **[From Tarzan to Tolkien: Controlling the Language Proficiency Level of LLMs for Content Generation](https://aclanthology.org/2024.findings-acl.926/)** — A. Malik, S. Mayhew, C. Piech, K. Bicknell — *Findings of ACL 2024*, 2024
  <br/>`peer-reviewed · Duolingo-authored`
  <br/>KEY. CEFR-level-controlled generation - the published method behind AI-authored course content.
- **[Automated Evaluation of Written Discourse Coherence Using GPT-4](https://aclanthology.org/2023.bea-1.32/)** — B. Naismith, P. Mulcaire, J. Burstein — *BEA @ ACL 2023*, 2023
  <br/>`peer-reviewed · Duolingo-authored`
  <br/>GPT-4 as a discourse-coherence rater.
- **[Rating Short L2 Essays on the CEFR Scale with GPT-4](https://aclanthology.org/2023.bea-1.49/)** — K.P. Yancey, G.T. LaFlair, A. Verardi, J. Burstein — *BEA @ ACL 2023*, 2023
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.18653/v1/2023.bea-1.49](https://doi.org/10.18653/v1/2023.bea-1.49)`
  <br/>Alt: <https://aclanthology.org/2023.bea-1.49.pdf>
  <br/>KEY. Duolingo's first published LLM-scoring study. Absent from research.duolingo.com.
- **[Duolingo makes its AI-powered 'Explain My Answer' feature free for all users in 2026](https://gamesbeat.com/duolingo-makes-its-ai-powered-explain-my-answer-feature-free-for-all-users-in-2026/)** — GamesBeat — *GamesBeat*, 2026
  <br/>`not peer-reviewed`
  <br/>Alt: <https://gamesbeat.com/duolingo-launches-ai-powered-adventures-mini-games-and-video-call-feature/>
  <br/>A Max-tier AI feature moves to the free tier as inference costs collapse.
- **[Evaluating LLM-Generated Lessons from the Language Learning Students' Perspective: A Short Case Study on Duolingo](https://arxiv.org/abs/2603.18873)** — C.R. Catalan, P.N. Monderin, L.M. Dizon, G. Estrella, R.J. Sarmiento, M.A. Patalagsa — *arXiv 2603.18873*, 2026
  <br/>`PDF · not peer-reviewed · DOI [10.48550/arXiv.2603.18873](https://doi.org/10.48550/arXiv.2603.18873)`
  <br/>External student-perspective evaluation of Duolingo's LLM-generated lesson content. Directly probes the AI-course pivot.
- **[A Lesson with Your Artificial Language Tutor: Analyzing Conversational AI in Duolingo, Speakology, and ChatGPT](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5691722)** — J. Harrison — *SSRN working paper*, 2025
  <br/>`PDF · not peer-reviewed`
  <br/>HIGH-SIGNAL. The only external evaluation found that directly examines Duolingo VIDEO CALL alongside competitors.
- **[Duolingo Launches 148 New Language Courses](https://investors.duolingo.com/news-releases/news-release-details/duolingo-launches-148-new-language-courses)** — Duolingo, Inc. — *Duolingo IR*, 2025
  <br/>`not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>Alt: <https://techcrunch.com/2025/04/30/duolingo-launches-148-courses-created-with-ai-after-sharing-plans-to-replace-contractors-with-ai/>
  <br/>KEY MILESTONE, 30 Apr 2025. The generative-AI content-scaling claim: 12 years for 100 courses vs ~1 year for 148.
- **[Duolingo Unveils Major Product Updates at Duocon 2025](https://investors.duolingo.com/news-releases/news-release-details/duolingo-unveils-major-product-updates-turn-learning-real-world)** — Duolingo, Inc. — *Duolingo IR*, 2025
  <br/>`not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>Alt: <https://www.axios.com/local/pittsburgh/2025/09/16/duolingo-chess-video-calls-linkedin-update>
  <br/>16 Sep 2025: Duolingo Score to LinkedIn, Video Call in 9 courses, Chess.
- **[Duolingo's AI Revolution](https://drphilippahardman.substack.com/p/duolingos-ai-revolution)** — P. Hardman — *Substack*, 2025
  <br/>`not peer-reviewed`
  <br/>The most rigorous NON-ACADEMIC critique found: a learning designer on the instructional quality of AI-generated courses.
- **[Duolingo's AI-powered Video Call brings Lily to life with Rive](https://rive.app/blog/duolingo-s-ai-powered-video-call-brings-lily-to-life)** — Rive — *Rive (vendor blog)*, 2025
  <br/>`not peer-reviewed`
  <br/>Vendor-side technical detail on the character-animation layer of Video Call.
- **[Gamified and Non-Gamified AI Tools in Enhancing EFL Listening Comprehension: Duolingo and Replika](https://doi.org/10.21203/rs.3.rs-6032009/v1)** — A. Tajik — *Research Square preprint*, 2025
  <br/>`PDF · not peer-reviewed · DOI [10.21203/rs.3.rs-6032009/v1](https://doi.org/10.21203/rs.3.rs-6032009/v1)`
  <br/>Duolingo vs an LLM companion app on listening outcomes.
- **[Get to know the AI behind every Video Call with Lily](https://blog.duolingo.com/ai-and-video-call/)** — Duolingo — *Duolingo blog*, 2025
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Rare first-party account of prompt/system design; Learning Designers write Lily's instructions.
- **[Video Call research report (Duolingo blog summary of three studies)](https://blog.duolingo.com/video-call-research-report)** — Duolingo — *Duolingo blog*, 2025
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>IMPORTANT: the underlying Video Call efficacy PDF (n=567 Japanese learners, Versant pre/post) is indexed by search engines but now returns AccessDenied on S3. Blog summary is the only live first-party source.
- **[Duolingo Introduces AI-Powered Innovations at Duocon 2024](https://investors.duolingo.com/news-releases/news-release-details/duolingo-introduces-ai-powered-innovations-duocon-2024)** — Duolingo, Inc. — *Duolingo IR*, 2024
  <br/>`not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>Alt: <https://www.post-gazette.com/business/tech-news/2024/09/24/duolingo-ai-conversations-lilly-pittsburgh-jon-batiste/stories/202409240084>
  <br/>Primary source for Video Call with Lily and Adventures, 24 Sep 2024.
- **[Duolingo's Klinton Bicknell on AI creating high-quality learning experiences](https://indiaai.gov.in/article/duolingo-s-klinton-bicknell-on-ai-creating-high-quality-learning-experiences)** — IndiaAI — *IndiaAI*, 2024
  <br/>`not peer-reviewed`
  <br/>Alt: <https://lsvp.com/stories/how-duolingo-uses-ai-to-transform-learning/>
  <br/>Substantive Head-of-AI interview on quality control in AI-generated content.
- **[How Duolingo uses AI to create lessons faster](https://blog.duolingo.com/large-language-model-duolingo-lessons/)** — P. Henry — *Duolingo blog*, 2024
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>KEY. The content-generation pipeline described first-hand - the mechanism behind the 148-course push.
- **[Using generative AI to scale DuoRadio 10x faster](https://blog.duolingo.com/scaling-duoradio/)** — Duolingo — *Duolingo blog*, 2024
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>GenAI script generation with naturalness/grammaticality/coherence filtering. Concrete quality-control detail.
- **[Duolingo - Filling crucial language learning gaps (OpenAI customer story)](https://openai.com/index/duolingo/)** — OpenAI — *OpenAI*, 2023
  <br/>`not peer-reviewed`
  <br/>The GPT-4 partnership as stated by the vendor.
- **[Duolingo launches new subscription tier with access to AI tutor powered by GPT-4](https://techcrunch.com/2023/03/14/duolingo-launches-new-subscription-tier-with-access-to-ai-tutor-powered-by-gpt-4/)** — TechCrunch — *TechCrunch*, 2023
  <br/>`not peer-reviewed`
  <br/>Best same-day trade coverage of the Max launch: pricing and limited rollout.
- **[Duolingo Max Shows the Future of AI Education (press release)](https://investors.duolingo.com/news-releases/news-release-details/duolingo-max-shows-future-ai-education)** — Duolingo, Inc. — *Duolingo IR*, 2023
  <br/>`not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>Alt: <https://techcrunch.com/2023/03/14/duolingo-launches-new-subscription-tier-with-access-to-ai-tutor-powered-by-gpt-4/>
  <br/>Canonical primary source for the GPT-4 launch, 14 Mar 2023. TechCrunch same-day coverage in alt_url is accessible.
- **[Introducing Duolingo Max, a learning experience powered by GPT-4](https://blog.duolingo.com/duolingo-max/)** — Duolingo — *Duolingo blog*, 2023
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://openai.com/index/duolingo/>
  <br/>The GPT-4 launch post: Explain My Answer and Roleplay. 14 March 2023.

## AI in assessment: the Duolingo English Test

*35 sources*

- **[Developing an Automatic Pronunciation Scorer: Aligning Speech Evaluation Models and Applied Linguistics Constructs](https://onlinelibrary.wiley.com/doi/full/10.1111/lang.70000)** — D. Cai, B. Naismith, M. Kostromitina, Z. Teng, K.P. Yancey, G.T. LaFlair — *Language Learning 75(S1)*, 2025
  <br/>`peer-reviewed · Duolingo-authored · DOI [10.1111/lang.70000](https://doi.org/10.1111/lang.70000)`
  <br/>Automated pronunciation scoring aligned to applied-linguistics constructs.
- **[Exploring AI-Enabled Test Practice, Affect, and Test Outcomes in Language Assessment](https://aclanthology.org/2025.aimecon-main.7/)** — J. Burstein, R. Cardwell, P.-L. Chuang, A. Michalowski, S. Nydick — *AIME-Con 2025*, 2025
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2508.17108](https://doi.org/10.48550/arXiv.2508.17108)`
  <br/>Alt: <https://arxiv.org/abs/2508.17108>
  <br/>Does AI-enabled practice raise scores, or only confidence? In-house; an open external research target.
- **[Keystroke Analysis in Digital Test Security: AI Approaches for Copy-Typing Detection and Cheating Ring Identification](https://aclanthology.org/2025.aimecon-wip.13/)** — C. Niu, Y.-S. Shih, M. Liao, R. Liu, A.O. Lee — *AIME-Con 2025 (WIP)*, 2025
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://aclanthology.org/2025.aimecon-wip.13.pdf>
  <br/>Behavioural biometrics for DET fraud detection.
- **[Team Perezoso's ASR and SLA System for Speak & Improve Challenge 2025](https://www.isca-archive.org/slate_2025/cai25_slate.pdf)** — D. Cai, K.P. Yancey, N. Madnani — *SLaTE 2025*, 2025
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Whisper + BERT end-to-end spoken language assessment.
- **[A Generative AI-Driven Interactive Listening Assessment Task](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1474019/full)** — A. Runge, Y. Attali, G.T. LaFlair, Y. Park, J. Church — *Frontiers in Artificial Intelligence 7:1474019*, 2024
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.3389/frai.2024.1474019](https://doi.org/10.3389/frai.2024.1474019)`
  <br/>GenAI-driven listening item generation.
- **[BERT-IRT: Accelerating Item Piloting with BERT Embeddings and Explainable IRT Models](https://aclanthology.org/2024.bea-1.35/)** — K.P. Yancey, A. Runge, G.T. LaFlair, P. Mulcaire — *BEA @ ACL 2024*, 2024
  <br/>`peer-reviewed · Duolingo-authored`
  <br/>10x reduction in item-piloting length on the DET. Also absent from the research portal.
- **[Detecting LLM-Assisted Cheating on Open-Ended Writing Tasks on Language Proficiency Tests](https://aclanthology.org/2024.emnlp-industry.70/)** — C. Niu, K.P. Yancey, R. Liu, M.B. Baig, A.K. Horie, J. Sharpnack — *EMNLP 2024 Industry Track*, 2024
  <br/>`peer-reviewed · Duolingo-authored`
  <br/>Detecting GPT-written essays on the DET. AI defending assessment against AI.
- **[Digital-First Learning and Assessment Systems for the 21st Century](https://doi.org/10.3389/feduc.2022.857604)** — T. Langenfeld, J. Burstein, A.A. von Davier — *Frontiers in Education 7*, 2022
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.3389/feduc.2022.857604](https://doi.org/10.3389/feduc.2022.857604)`
  <br/>Duolingo's programmatic vision for AI-native assessment.
- **[Quality Assurance in Digital-First Assessments](https://doi.org/10.1007/978-3-031-04572-1_20)** — M. Liao, Y. Attali, A.A. von Davier, J.R. Lockwood — *Springer PROMS*, 2022
  <br/>`peer-reviewed · Duolingo-authored · DOI [10.1007/978-3-031-04572-1_20](https://doi.org/10.1007/978-3-031-04572-1_20)`
  <br/>QA processes for automated assessment pipelines.
- **[The Interactive Reading Task: Transformer-Based Automatic Item Generation](https://doi.org/10.3389/frai.2022.903077)** — Y. Attali, A. Runge, G.T. LaFlair, K.P. Yancey, S. Goodwin, Y. Park, A.A. von Davier — *Frontiers in Artificial Intelligence 5*, 2022
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.3389/frai.2022.903077](https://doi.org/10.3389/frai.2022.903077)`
  <br/>Alt: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9354894/>
  <br/>KEY. GPT-3-based fully automated passage and question generation in a live high-stakes test.
- **[Jump-Starting Item Parameters for Adaptive Language Tests](https://research.duolingo.com/papers/mccarthy.emnlp21.pdf)** — A.D. McCarthy, K.P. Yancey, G.T. LaFlair, J. Egbert, M. Liao, B. Settles — *EMNLP 2021*, 2021
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.18653/v1/2021.emnlp-main.67](https://doi.org/10.18653/v1/2021.emnlp-main.67)`
  <br/>Alt: <https://aclanthology.org/2021.emnlp-main.67/>
  <br/>Cold-start item calibration via BERT features. The NEWEST item on research.duolingo.com - the portal stops here.
- **[Mining Process Data to Detect Aberrant Test Takers](https://research.duolingo.com/papers/liao.mirp21.pdf)** — M. Liao, J. Patton, R. Yan, H. Jiao — *Measurement: Interdisciplinary Research and Perspectives*, 2021
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Algorithmic cheating detection: the proctoring / test-security side of DET AI.
- **[Machine Learning-Driven Language Assessment](https://research.duolingo.com/papers/settles.tacl20.pdf)** — B. Settles, G.T. LaFlair, M. Hagiwara — *TACL 8*, 2020
  <br/>`PDF · peer-reviewed · Duolingo-authored · DOI [10.1162/tacl_a_00310](https://doi.org/10.1162/tacl_a_00310)`
  <br/>Alt: <https://aclanthology.org/2020.tacl-1.17/>
  <br/>KEY. Foundational DET account: NLP-induced proficiency scales, automatic item generation, adaptive testing.
- **[Analytics for Quality Assurance for Item Pools (AQuAP): Monitoring and Maintaining Item Bank Health](https://arxiv.org/abs/2606.18536)** — A.A. von Davier, X. Zhang, Y. Attali, Y. Park, J. Church, A. Runge, G.T. LaFlair, A. Tsigler — *arXiv 2606.18536*, 2026
  <br/>`PDF · not peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2606.18536](https://doi.org/10.48550/arXiv.2606.18536)`
  <br/>Monitoring the health of an AI-generated item bank at scale.
- **[Duolingo English Test: Technical Manual (2026-07)](https://duolingo-papers.s3.us-east-1.amazonaws.com/other/technical_manual/DET_technical_manual_2026_07.pdf)** — B. Naismith, R. Cardwell, G.T. LaFlair, S. Nydick, M. Kostromitina — *Duolingo technical manual*, 2026
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://go.duolingo.com/dettechnicalmanual>
  <br/>The single most detailed document on DET scoring, item generation and adaptivity. Current edition.
- **[Learning Item Embeddings and Hyperparameters for IRT Calibration via Monte Carlo EM](https://arxiv.org/abs/2607.06905)** — J. Sharpnack, K.-L. Lo — *arXiv 2607.06905*, 2026
  <br/>`PDF · not peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2607.06905](https://doi.org/10.48550/arXiv.2607.06905)`
  <br/>Neural item embeddings for fast calibration of new DET items.
- **[S2A3: Thompson Sampling and Stochastic Exposure Control for High-Stakes CATs](https://arxiv.org/abs/2606.07364)** — J. Sharpnack, A. Tsigler, J.R. Lockwood, S. Nydick, A.A. von Davier — *arXiv 2606.07364*, 2026
  <br/>`PDF · not peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2606.07364](https://doi.org/10.48550/arXiv.2606.07364)`
  <br/>Unified calibration plus administration via Thompson sampling.
- **[Stochastic Constrained Test Assembly for AI-Enabled Assessment Systems](https://arxiv.org/abs/2607.09965)** — A.A. von Davier — *arXiv 2607.09965*, 2026
  <br/>`PDF · not peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2607.09965](https://doi.org/10.48550/arXiv.2607.09965)`
  <br/>Bandit-based test-form assembly.
- **[Duolingo English Test: Technical Manual (2025-07)](https://duolingo-papers.s3.amazonaws.com/other/technical_manual/DET_technical_manual_2025_07.pdf)** — B. Naismith, R. Cardwell, G.T. LaFlair, S. Nydick, M. Kostromitina — *Duolingo technical manual*, 2025
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Prior edition - useful for diffing what changed year on year.
- **[An Overview of Duolingo English Test Administration and Scoring (DRR-24-03)](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_test_scoring_2024_v1.pdf)** — Duolingo English Test — *Duolingo research report*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Administration and automated scoring overview.
- **[AutoIRT: Calibrating Item Response Theory Models with Automated Machine Learning](https://arxiv.org/abs/2409.08823)** — J. Sharpnack, P. Mulcaire, K. Bicknell, G.T. LaFlair, K.P. Yancey — *arXiv 2409.08823*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2409.08823](https://doi.org/10.48550/arXiv.2409.08823)`
  <br/>AutoML for IRT calibration on the DET.
- **[BanditCAT and AutoIRT: Machine Learning Approaches to Computerized Adaptive Testing and Item Calibration](https://arxiv.org/abs/2410.21033)** — J. Sharpnack, K. Hao, P. Mulcaire, K. Bicknell, G.T. LaFlair, K.P. Yancey, A.A. von Davier — *arXiv 2410.21033 (NeurIPS 2024 workshop)*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2410.21033](https://doi.org/10.48550/arXiv.2410.21033)`
  <br/>Adaptive testing framed as a contextual bandit.
- **[Facilitating the Writing Process on the DET: The Interactive Writing Task (DRR-24-02)](https://duolingo-papers.s3.amazonaws.com/other/interactive-writing-whitepaper.pdf)** — Duolingo English Test — *Duolingo research report*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>AI-scaffolded writing task design.
- **[The Duolingo English Test Handbook](https://englishtest-static.duolingo.com/media/resources/GPN%20The%20DET%20Handbook.pdf)** — Duolingo English Test — *Duolingo*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Official handbook covering AI-driven scoring mechanics for a general audience.
- **[Assessing Speaking on the Duolingo English Test (DRR-23-03)](https://englishtest-static.duolingo.com/media/resources/media/resources/whitepapers/speaking-whitepaper.pdf)** — Y. Park, R. Cardwell, S. Goodwin, B. Naismith, G.T. LaFlair, K.-L. Lo, K.P. Yancey — *Duolingo research report*, 2023
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>ASR-based speaking assessment.
- **[Assessing Vocabulary on the Duolingo English Test](https://duolingo-papers.s3.amazonaws.com/other/vocab_whitepaper_final.pdf)** — B. Naismith, Y. Park, R. Cardwell — *Duolingo whitepaper*, 2023
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Vocabulary construct; the yes/no item type is fully machine-generated.
- **[Interactive Listening - The Duolingo English Test (DRR-23-01)](https://duolingo-papers.s3.amazonaws.com/other/Interactive+Listening+%E2%80%93+The+Duolingo+English+Test.pdf)** — Duolingo English Test — *Duolingo research report*, 2023
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Construct and generation pipeline for interactive listening.
- **[A Theoretical Assessment Ecosystem for a Digital-First Assessment - The DET (DRR-22-01)](https://duolingo-papers.s3.amazonaws.com/other/det-assessment-ecosystem.pdf)** — Duolingo English Test — *Duolingo research report*, 2022
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://duolingo-papers.s3.amazonaws.com/other/det-assessment-ecosystem-mpr.pdf>
  <br/>The overarching validity-argument framing.
- **[Assessing Listening on the Duolingo English Test](https://englishtest-static.duolingo.com/media/resources/media/resources/whitepapers/listening-whitepaper.pdf)** — Duolingo English Test — *Duolingo whitepaper*, 2022
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://duolingo-testcenter.s3.amazonaws.com/media/resources/listening-whitepaper.pdf>
  <br/>Listening construct and generation.
- **[Duolingo English Test - Writing Construct (DRR-22-03)](https://duolingo-papers.s3.amazonaws.com/other/writing-whitepaper.pdf)** — S. Goodwin, Y. Attali, G.T. LaFlair, Y. Park, A. Runge, A.A. von Davier — *Duolingo research report*, 2022
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>What the automated writing score claims to measure.
- **[Interactive Reading - The Duolingo English Test (DRR-22-02)](https://duolingo-papers.s3.amazonaws.com/other/The+Interactive+Reading+Task.pdf)** — Y. Park, G.T. LaFlair, Y. Attali, A. Runge, S. Goodwin — *Duolingo research report*, 2022
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://duolingo-papers.s3.amazonaws.com/other/mpr-whitepaper.pdf>
  <br/>Whitepaper companion to the Frontiers AIG paper.
- **[Duolingo English Test: Security, Proctoring, and Accommodations](https://duolingo-papers.s3.amazonaws.com/other/det-security-proctoring-whitepaper.pdf)** — Duolingo English Test — *Duolingo whitepaper*, 2021
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>The AI-assisted remote proctoring pipeline described first-hand.
- **[The Duolingo English Test - Design, Validity, and Value](https://s3.amazonaws.com/duolingo-papers/other/DET_ShortPaper.pdf)** — Duolingo English Test — *Duolingo whitepaper*, 2020
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Short-form validity summary.
- **[The Duolingo English Test: Psychometric Considerations (DRR-20-02)](https://duolingo-papers.s3.amazonaws.com/reports/DRR-20-02.pdf)** — Duolingo English Test — *Duolingo research report*, 2020
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Psychometric foundations of the adaptive test.
- **[The Duolingo English Test and Academic English (DRR-16-01)](https://s3.amazonaws.com/duolingo-papers/reports/DRR-16-01.pdf)** — Duolingo English Test — *Duolingo research report*, 2016
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Earliest DRR; establishes the report numbering scheme for tracking the series.

## Validity, fairness and bias in AI-driven assessment

*13 sources*

- **[Duolingo English Test vs. IELTS in South Asia: Accessibility, Validity, Cost, and Equity](https://www.ijrp.org/paper-detail/9718.pdf)** — S. Rehna, N. Yasmeen — *International Journal of Research Publications*, 2026
  <br/>`PDF · peer-reviewed · DOI [10.47119/IJRP1002031820269718](https://doi.org/10.47119/IJRP1002031820269718)`
  <br/>Recent equity-framed comparison. Open access.
- **[A survey of English language proficiency tests in international student admissions at US research-intensive universities](https://doi.org/10.1177/02655322251348617)** — N. Coney, D.R. Isbell — *Language Testing*, 2025
  <br/>`peer-reviewed · DOI [10.1177/02655322251348617](https://doi.org/10.1177/02655322251348617)`
  <br/>Institutional-uptake evidence: where the DET is and is not accepted.
- **[Evaluating Fairness in AI-Assisted Remote Proctoring](https://proceedings.mlr.press/v273/belzak25a.html)** — W. Belzak, J. Burstein, A.A. von Davier — *PMLR 273*, 2025
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Does proctor or test-taker nationality bias AI flagging decisions? In-house fairness audit.
- **[Test Takers' Attitudes Toward Varieties of Accents in Listening Tasks of the Duolingo English Test](https://doi.org/10.1080/15434303.2024.2448963)** — O. Kang, M. Kostromitina, X. Yan — *Language Assessment Quarterly*, 2025
  <br/>`peer-reviewed · DOI [10.1080/15434303.2024.2448963](https://doi.org/10.1080/15434303.2024.2448963)`
  <br/>Attitudinal companion to Kang et al. 2024.
- **[Construct representation and predictive validity of integrated writing tasks: the writing component of the Duolingo English Test](https://doi.org/10.1016/j.asw.2024.100846)** — Q. Xie — *Assessing Writing*, 2024
  <br/>`peer-reviewed · DOI [10.1016/j.asw.2024.100846](https://doi.org/10.1016/j.asw.2024.100846)`
  <br/>External construct critique of what the automated writing score actually measures.
- **[Exploring the effects of task difficulty and learner variables on performance on picture description writing tasks](https://doi.org/10.1016/j.asw.2024.100827)** — K. Barkaoui — *Assessing Writing*, 2024
  <br/>`peer-reviewed · DOI [10.1016/j.asw.2024.100827](https://doi.org/10.1016/j.asw.2024.100827)`
  <br/>DET-format task analysis.
- **[Fairness of using different English accents: The effect of shared L1s in listening tasks of the Duolingo English Test](https://doi.org/10.1177/02655322231179134)** — O. Kang, X. Yan, M. Kostromitina, R. Thomson, T. Isaacs — *Language Testing 41(2), 263-289*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.1177/02655322231179134](https://doi.org/10.1177/02655322231179134)`
  <br/>Alt: <https://eric.ed.gov/?q=duolingo&id=EJ1419067>
  <br/>HIGH-SIGNAL. The key external accent-bias study on an AI-scored test. Finds a shared-L1 benefit but no penalty for highly intelligible accents.
- **[Predictability of Duolingo English mock test for Chinese college-level EFLs: using assessment use argument](https://doi.org/10.3389/feduc.2023.1275518)** — X. Ma, H. Zhang — *Frontiers in Education 8*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.3389/feduc.2023.1275518](https://doi.org/10.3389/feduc.2023.1275518)`
  <br/>Open access.
- **[Speaking performances, stakeholder perceptions, and test scores: Extrapolating from the Duolingo English Test to the university](https://doi.org/10.1177/02655322231165984)** — D.R. Isbell, D. Crowther, H. Nishizawa — *Language Testing 41(2)*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.1177/02655322231165984](https://doi.org/10.1177/02655322231165984)`
  <br/>Do AI-scored DET speaking scores translate to real academic speech that faculty accept?
- **[Writing assessment literacy and its impact on the learning of writing: A netnography focusing on Duolingo English Test examinees](https://doi.org/10.1186/s40468-024-00297-x)** — C. Yu, W. Xu — *Language Testing in Asia 14*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.1186/s40468-024-00297-x](https://doi.org/10.1186/s40468-024-00297-x)`
  <br/>Alt: <https://languagetestingasia.springeropen.com/counter/pdf/10.1186/s40468-024-00297-x>
  <br/>Washback of AI-scored writing: how examinees reverse-engineer the automated scorer. Excellent angle.
- **[Examining the predictive validity of the Duolingo English Test: Evidence from a major UK university](https://doi.org/10.1177/02655322231158550)** — T. Isaacs, R. Hu, D. Trenkic, J. Varga — *Language Testing 40(3)*, 2023
  <br/>`PDF · peer-reviewed · DOI [10.1177/02655322231158550](https://doi.org/10.1177/02655322231158550)`
  <br/>Alt: <https://discovery.ucl.ac.uk/id/eprint/10164102/7/Isaacs_Examining%20the%20predictive%20validity%20of%20the%20Duolingo%20English%20Test-%20Evidence%20from%20a%20major%20UK%20university_VoR.pdf>
  <br/>ANCHOR. The definitive independent predictive-validity study. Green OA full text via UCL Discovery.
- **[Examining the subjective fairness of at-home and online tests: Taking Duolingo English Test as an example](https://doi.org/10.1371/journal.pone.0291629)** — D. Yao — *PLOS ONE 18(9)*, 2023
  <br/>`PDF · peer-reviewed · DOI [10.1371/journal.pone.0291629](https://doi.org/10.1371/journal.pone.0291629)`
  <br/>Alt: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10508603/>
  <br/>HIGH-SIGNAL. Test-takers perceive the DET as invalid even where objective bias analyses find none. Directly on remote AI proctoring and equity.
- **[Influences of Duolingo English Test: A Qualitative Study on the Tertiary-Level Students of Bangladesh](https://doi.org/10.4236/ojml.2023.133024)** — M. Sadaf — *Open Journal of Modern Linguistics 13(3)*, 2023
  <br/>`PDF · peer-reviewed · DOI [10.4236/ojml.2023.133024](https://doi.org/10.4236/ojml.2023.133024)`
  <br/>Global-South access and equity angle.

## Efficacy and learning outcomes

*28 sources*

- **[Duolingo-Inspired Pretesting with Words and Pictures Improves Vocabulary Learning](https://eric.ed.gov/?q=duolingo&id=EJ1513201)** — T.J.E. Chua, S.C. Pan — *Cognitive Research: Principles and Implications*, 2026
  <br/>`PDF · peer-reviewed`
  <br/>Lab replication testing whether the exercise DESIGN, not the AI, drives gains. Methodologically sharp.
- **[L2 grit and age as predictors of attrition in mobile-assisted language learning](https://doi.org/10.1016/j.lindif.2025.102704)** — E. Sudina, Y. Teimouri, L. Plonsky — *Learning and Individual Differences*, 2025
  <br/>`peer-reviewed · DOI [10.1016/j.lindif.2025.102704](https://doi.org/10.1016/j.lindif.2025.102704)`
  <br/>Who drops out, and why gamified retention is not learning retention.
- **[Online Learning through Duolingo Stories: An Examination of Literacy Development](https://eric.ed.gov/?q=duolingo&id=EJ1473941)** — T. Neuschafer — *Journal of Educators Online*, 2025
  <br/>`PDF · peer-reviewed`
  <br/>Same author also has JEO 2024 (teacher assessment) and JEO 2023 (discussion boards during COVID).
- **[The Effectiveness of App-Based and Classroom-Based Instruction on L2 Learning and Motivation](https://eric.ed.gov/?q=duolingo&id=EJ1486621)** — B. Gonzalez-Fernandez, I. de la Vina — *Language Learning & Technology*, 2025
  <br/>`PDF · peer-reviewed`
  <br/>App vs classroom head-to-head.
- **[Enhancing willingness to communicate in English among Chinese students in the UK: the impact of MALL with Duolingo and HelloTalk](https://doi.org/10.1515/jccall-2023-0027)** — D. Zhao, R.R. Jablonkai, A. Sandoval-Hernandez — *Journal of China Computer-Assisted Language Learning*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.1515/jccall-2023-0027](https://doi.org/10.1515/jccall-2023-0027)`
  <br/>Alt: <https://www.degruyter.com/document/doi/10.1515/jccall-2023-0027/pdf>
  <br/>Open access via De Gruyter.
- **[How Effective Is Duolingo at Promoting Implicit Pronunciation Learning?](https://eric.ed.gov/?q=duolingo&id=EJ1454782)** — C. Taylor, C.-L. Huang — *English Australia Journal*, 2024
  <br/>`PDF · peer-reviewed`
  <br/>Targets the speech-recognition / pronunciation component specifically.
- **[Impacts of digital applications on emergent multilinguals' language learning experiences: the case of Duolingo](https://doi.org/10.1007/s10639-024-13185-x)** — O. Solmaz — *Education and Information Technologies*, 2024
  <br/>`peer-reviewed · DOI [10.1007/s10639-024-13185-x](https://doi.org/10.1007/s10639-024-13185-x)`
  <br/>Multilingual learner experience.
- **[Opening the 'Black Box': How Out-of-Class Use of Duolingo Impacts Chinese Junior High School Students' Intrinsic Motivation for English](https://eric.ed.gov/?q=duolingo&id=EJ1425890)** — C. Zeng, L. Fisher — *ECNU Review of Education*, 2024
  <br/>`peer-reviewed`
  <br/>Self-determination-theory critique of the reward loop.
- **[The Effectiveness of Duolingo English Courses in Developing Reading and Listening Proficiency](https://doi.org/10.1558/cj.26704)** — X. Jiang, R. Peters, L. Plonsky, B. Pajak — *CALICO Journal 41(1)*, 2024
  <br/>`peer-reviewed · Mixed Duolingo/external authorship · DOI [10.1558/cj.26704](https://doi.org/10.1558/cj.26704)`
  <br/>Alt: <https://eric.ed.gov/?q=duolingo&id=EJ1447491>
  <br/>CAUTION: mixed authorship - Jiang and Pajak are Duolingo employees. The most-cited 'does it work' paper; treat as partially in-house.
- **[The effectiveness of Duolingo in developing receptive and productive language knowledge and proficiency](https://scholarspace.manoa.hawaii.edu/bitstreams/ea47a53e-da6e-4419-bd55-e72b458294f4/download)** — Language Learning & Technology 28(1) — *Language Learning & Technology 28(1)*, 2024
  <br/>`PDF · peer-reviewed`
  <br/>~27 hours of study yields significant gains across receptive AND productive measures. Open access.
- **[The Effects of Duolingo, an AI-Integrated Technology, on EFL Learners' Willingness to Communicate and Engagement in Online Classes](https://files.eric.ed.gov/fulltext/EJ1441347.pdf)** — Z. Ouyang, Y. Jiang, H. Liu — *IRRODL 25(3)*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.19173/irrodl.v25i3.7677](https://doi.org/10.19173/irrodl.v25i3.7677)`
  <br/>Alt: <https://www.irrodl.org/index.php/irrodl/article/view/7677>
  <br/>Quasi-experimental (n=40); one of few external studies that explicitly frames Duolingo AS an AI technology.
- **[Mobile-assisted language learning with Babbel and Duolingo: comparing L2 learning gains and user experience](https://doi.org/10.1080/09588221.2023.2215294)** — M. Kessler, S. Loewen, T. Gonulal — *Computer Assisted Language Learning*, 2023
  <br/>`peer-reviewed · DOI [10.1080/09588221.2023.2215294](https://doi.org/10.1080/09588221.2023.2215294)`
  <br/>Alt: <https://eric.ed.gov/?q=duolingo&id=EJ1473885>
  <br/>HIGH-SIGNAL. Rare head-to-head external comparison of two commercial adaptive apps.
- **[Self-directed language learning with Duolingo in an out-of-class context](https://doi.org/10.1080/09588221.2023.2206874)** — Z. Li, C.J. Bonk — *Computer Assisted Language Learning*, 2023
  <br/>`peer-reviewed · DOI [10.1080/09588221.2023.2206874](https://doi.org/10.1080/09588221.2023.2206874)`
  <br/>Alt: <https://eric.ed.gov/?q=duolingo&id=EJ1469292>
  <br/>Interview study on autonomy, motivation and the limits of algorithmic scaffolding.
- **[Supporting learners' self-management for self-directed language learning: a study within Duolingo](https://doi.org/10.1108/itse-05-2023-0093)** — Z. Li, C.J. Bonk, C. Zhou — *Interactive Technology and Smart Education*, 2023
  <br/>`peer-reviewed · DOI [10.1108/ITSE-05-2023-0093](https://doi.org/10.1108/ITSE-05-2023-0093)`
  <br/>Self-management scaffolds inside an adaptive app.
- **[The effects of frequency, duration, and intensity on L2 learning through Duolingo](https://doi.org/10.1075/jsls.00021.plo)** — E. Sudina, L. Plonsky — *Journal of Second Language Studies 6(2)*, 2023
  <br/>`PDF · peer-reviewed · DOI [10.1075/jsls.00021.plo](https://doi.org/10.1075/jsls.00021.plo)`
  <br/>Dose-response analysis; an independent test of the practice-intensity assumption baked into the algorithm.
- **[Methods for Language Learning Assessment at Scale: Duolingo Case Study](https://research.duolingo.com/papers/portnoff.edm21.pdf)** — L. Portnoff, E. Gustafson, J. Rollinson, K. Bicknell — *EDM 2021*, 2021
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://eric.ed.gov/?id=ED615620>
  <br/>How Duolingo measures learning in-app at scale. Defines what 'learning' means in their own metrics.
- **[Duolingo Efficacy Studies hub](https://www.duolingo.com/efficacy/studies)** — Duolingo — *Duolingo*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Index of all in-house efficacy whitepapers.
- **[The Promise of Duolingo](https://www.thedial.world/articles/news/issue-22/duolingo-language-learning-fluency)** — The Dial — *The Dial*, 2025
  <br/>`not peer-reviewed`
  <br/>Longform critique of whether AI-assisted Duolingo actually produces fluency.
- **[Duolingo learners can start a conversation after 4-6 weeks](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_conversation_2024.pdf)** — Duolingo — *Duolingo whitepaper*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>In-house conversational-readiness claim.
- **[Duolingo Path Meets Expectations for Proficiency Outcomes](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_read_listen_write_speak_2024.pdf)** — Duolingo — *Duolingo whitepaper*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>In-house efficacy across four skills.
- **[Educators' perceptions of Duolingo efficacy (DRR-24-07)](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_educator_perception_2024.pdf)** — Duolingo — *Duolingo research report*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Educator perception survey.
- **[Grit and motivation in language learning](https://duolingo-papers.s3.amazonaws.com/reports/Plonsky_etal_whitepaper_language_learning_grit_motivation_2023.pdf)** — L. Plonsky et al. — *Duolingo whitepaper*, 2023
  <br/>`PDF · not peer-reviewed · Mixed Duolingo/external authorship`
  <br/>Academic-industry collaboration published outside peer review.
- **[Seven units of Duolingo courses comparable to 5 university semesters](https://duolingo-papers.s3.amazonaws.com/reports/duolingo-intermediate-efficacy-whitepaper.pdf)** — Duolingo — *Duolingo whitepaper*, 2023
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>The most-quoted in-house efficacy comparison; worth scrutinising methodologically.
- **[The Duolingo Method for App-based Teaching and Learning](https://duolingo-papers.s3.amazonaws.com/reports/duolingo-method-whitepaper.pdf)** — Duolingo — *Duolingo whitepaper*, 2023
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Duolingo's own statement of pedagogical method.
- **[The Duolingo Method: 5 key principles](https://blog.duolingo.com/duolingo-teaching-method/)** — Duolingo — *Duolingo blog*, 2023
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://blog.duolingo.com/results-duolingo-efficacy-studies/>
  <br/>Pedagogical principles as stated by the company.
- **[Reading and Listening Outcomes of Learners in the Duolingo English Course](https://duolingo-papers.s3.amazonaws.com/reports/duolingo-efficacy-english-reading-listening-whitepaper.pdf)** — Duolingo — *Duolingo whitepaper*, 2022
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>In-house receptive-skills outcomes.
- **[How well does Duolingo teach speaking skills? (DRR-21-02)](https://duolingo-papers.s3.amazonaws.com/reports/Duolingo_whitepaper_language_speak_2021.pdf)** — Duolingo — *Duolingo research report*, 2021
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>Pre-GenAI speaking baseline - the comparison point for Video Call claims.
- **[Duolingo efficacy study: Beginning-level courses](https://duolingo-papers.s3.amazonaws.com/reports/duolingo-efficacy-whitepaper.pdf)** — Duolingo — *Duolingo whitepaper*, 2020
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>The original in-house efficacy study.

## Systematic reviews and meta-analyses

*14 sources*

- **[A meta-analysis of generative AI effects on language proficiency and affective-cognitive outcomes in language learning](https://doi.org/10.1007/s10791-026-10015-1)** — Discover Computing — *Discover Computing*, 2026
  <br/>`PDF · peer-reviewed · DOI [10.1007/s10791-026-10015-1](https://doi.org/10.1007/s10791-026-10015-1)`
  <br/>Stronger effects in INFORMAL learning settings and for productive skills - directly relevant to an app like Duolingo.
- **[A PRISMA-based systematic review of artificial intelligence in English as a foreign and second language education (2023-2025)](https://doi.org/10.1007/s44217-026-01504-y)** — Discover Education — *Discover Education*, 2026
  <br/>`PDF · peer-reviewed · DOI [10.1007/s44217-026-01504-y](https://doi.org/10.1007/s44217-026-01504-y)`
  <br/>Most recent PRISMA review in the space.
- **[Artificial Intelligence in Language Learning: A Twenty-Year Scoping Review of Applications, Research Methods, and Outcomes](https://doi.org/10.1080/29984475.2026.2647961)** — Taylor & Francis — *Taylor & Francis*, 2026
  <br/>`peer-reviewed · DOI [10.1080/29984475.2026.2647961](https://doi.org/10.1080/29984475.2026.2647961)`
  <br/>KEY STAT: Duolingo appears in only 1.4% of empirical AI-in-language-learning studies (2005-2024). The dominant app is drastically under-studied.
- **[A systematic review of AI in second language acquisition using the expanded SAMR model (2015-2024)](https://doi.org/10.1007/s10791-025-09833-6)** — Discover Computing — *Discover Computing*, 2025
  <br/>`PDF · peer-reviewed · DOI [10.1007/s10791-025-09833-6](https://doi.org/10.1007/s10791-025-09833-6)`
  <br/>281 studies. Useful for classifying Duolingo's AI as augmentation vs redefinition.
- **[A Systematic Review of Multilingual Applications, Large Language Models, and Language Learning (2015-2024)](https://files.eric.ed.gov/fulltext/EJ1482233.pdf)** — (see ERIC EJ1482233) — *ERIC EJ1482233*, 2025
  <br/>`PDF · peer-reviewed`
  <br/>HIGH-SIGNAL. 161 studies. Sharpest peer-reviewed critique of Duolingo's streak/reward design; cites the ~12% intermediate-fluency figure.
- **[Applying Generative AI to Task-based Language Teaching and Learning: A Systematic Review and Meta-analysis](https://doi.org/10.1007/s11528-025-01140-7)** — TechTrends — *TechTrends*, 2025
  <br/>`peer-reviewed · DOI [10.1007/s11528-025-01140-7](https://doi.org/10.1007/s11528-025-01140-7)`
  <br/>25 studies, 2,431 participants.
- **[Can Generative AI Chatbots Promote Second Language Acquisition? A Meta-Analysis](https://onlinelibrary.wiley.com/doi/10.1111/jcal.70060)** — Li et al. — *Journal of Computer Assisted Learning*, 2025
  <br/>`peer-reviewed · DOI [10.1111/jcal.70060](https://doi.org/10.1111/jcal.70060)`
  <br/>HIGH-SIGNAL. The benchmark against which Roleplay / Video Call-type features should be judged.
- **[Do mobile games improve language learning? A meta-analysis](https://doi.org/10.1080/09588221.2025.2528786)** — Computer Assisted Language Learning — *Computer Assisted Language Learning*, 2025
  <br/>`peer-reviewed · DOI [10.1080/09588221.2025.2528786](https://doi.org/10.1080/09588221.2025.2528786)`
  <br/>38 studies, 4,102 participants, g = 0.962.
- **[Integrating Generative AI in Language Education: A Systematic Review of Pedagogical, Ethical, and Technological Themes](https://www.ijlter.org/index.php/ijlter/article/view/15573)** — Cong et al. — *IJLTER*, 2025
  <br/>`PDF · peer-reviewed`
  <br/>Open access.
- **[Two years of innovation: A systematic review of empirical generative AI research in language learning and teaching (2023-2024)](https://www.sciencedirect.com/science/article/pii/S2666920X25000852)** — Computers and Education: Artificial Intelligence — *Computers and Education: AI*, 2025
  <br/>`PDF · peer-reviewed`
  <br/>PRISMA, 144 articles. Writing dominates (51.3%); speaking badly under-studied - which is exactly where Video Call sits.
- **[Enabling learner independence and self-regulation in language education using AI tools: a systematic review](https://doi.org/10.1080/2331186X.2024.2433814)** — Cogent Education — *Cogent Education*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.1080/2331186X.2024.2433814](https://doi.org/10.1080/2331186X.2024.2433814)`
  <br/>Open access.
- **[The effects of AI-guided individualized language learning: A meta-analysis](https://doi.org/10.64152/10125/73575)** — H.-S. Lee, J.H. Lee — *Language Learning & Technology 28*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.64152/10125/73575](https://doi.org/10.64152/10125/73575)`
  <br/>HIGH-SIGNAL. The closest thing to a quantitative synthesis of adaptive/AI-personalised language learning. Duolingo is a core included platform.
- **[Gamification in mobile-assisted language learning: a systematic review of Duolingo literature from public release of 2012 to early 2020](https://www.tandfonline.com/doi/full/10.1080/09588221.2021.1933540)** — M. Shortt, S. Tilak, I. Kuznetcova, B. Martens, B. Akinkuolie — *Computer Assisted Language Learning 36(3)*, 2023
  <br/>`PDF · peer-reviewed · DOI [10.1080/09588221.2021.1933540](https://doi.org/10.1080/09588221.2021.1933540)`
  <br/>Alt: <https://eric.ed.gov/?q=duolingo&id=EJ1386218>
  <br/>ANCHOR. The canonical external systematic review: 367 records screened, 35 included. Finds the literature is design-focused, non-probability-sampled and US/English-skewed. The natural baseline to extend to 2026.
- **[A Meta-Analysis on Mobile-Assisted Language Learning Applications: Benefits and Risks](https://doi.org/10.5334/pb.1146)** — Psychologica Belgica — *Psychologica Belgica*, 2022
  <br/>`PDF · peer-reviewed · DOI [10.5334/pb.1146](https://doi.org/10.5334/pb.1146)`
  <br/>Alt: <https://psychologicabelgica.com/articles/10.5334/pb.1146>
  <br/>g = 0.88 but flags HIGH risk of bias and low evidence quality across MALL. A good skeptical anchor.

## Public datasets, shared tasks and their reuse

*27 sources*

- **[Adaptive and Personalized Exercise Generation for Online Language Learning](https://arxiv.org/abs/2306.02457)** — P. Cui, M. Sachan — *ACL 2023 / arXiv 2306.02457*, 2023
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.2306.02457](https://doi.org/10.48550/arXiv.2306.02457)`
  <br/>HIGH-SIGNAL. An independent academic re-implementation of the Duolingo Max content-generation idea, built on Duolingo data.
- **[Machine Translation Robustness to Natural Asemantic Variation](https://arxiv.org/abs/2205.12514)** — (arXiv 2205.12514) — *EMNLP 2022*, 2022
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.2205.12514](https://doi.org/10.48550/arXiv.2205.12514)`
  <br/>Uses STAPLE paraphrase sets as an MT robustness testbed - dataset reuse well beyond education.
- **[Question Generation for Adaptive Education](https://arxiv.org/abs/2106.04262)** — (arXiv 2106.04262) — *ACL 2021 / arXiv 2106.04262*, 2021
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.2106.04262](https://doi.org/10.48550/arXiv.2106.04262)`
  <br/>Uses SLAM for difficulty-controlled item generation.
- **[Variational Deep Knowledge Tracing for Language Learning](https://doi.org/10.1145/3448139.3448170)** — LAK 2021 — *LAK '21 (ACM)*, 2021
  <br/>`PDF · peer-reviewed · DOI [10.1145/3448139.3448170](https://doi.org/10.1145/3448139.3448170)`
  <br/>VDKT on Duolingo data.
- **[Growing Together: Modeling Human Language Learning With n-Best Multi-Checkpoint Machine Translation](https://arxiv.org/abs/2006.04050)** — E.M.B. Nagoudi, M. Abdul-Mageed, H. Cavusoglu — *NGT @ ACL 2020 / arXiv 2006.04050*, 2020
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.2006.04050](https://doi.org/10.48550/arXiv.2006.04050)`
  <br/>STAPLE shared task.
- **[Simultaneous paraphrasing and translation by fine-tuning Transformer models](https://arxiv.org/abs/2005.05570)** — (arXiv 2005.05570) — *NGT @ ACL 2020*, 2020
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.2005.05570](https://doi.org/10.48550/arXiv.2005.05570)`
  <br/>STAPLE shared-task submission.
- **[Simultaneous Translation and Paraphrase for Language Education (STAPLE overview)](https://research.duolingo.com/papers/mayhew.staple20.pdf)** — S. Mayhew, K. Bicknell, C. Brust, B. McDowell, W. Monroe, B. Settles — *WNGT @ ACL 2020*, 2020
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://aclanthology.org/2020.ngt-1.28/>
  <br/>Accepting many valid translations; underpins grading of free-response answers.
- **[Training and Inference Methods for High-Coverage Neural Machine Translation](http://sharedtask.duolingo.com/papers/yang.staple20.pdf)** — Yang et al. — *NGT @ ACL 2020*, 2020
  <br/>`PDF · peer-reviewed`
  <br/>STAPLE submission, hosted on Duolingo's own shared-task site.
- **[Enhancing human learning via spaced repetition optimization](https://doi.org/10.1073/pnas.1815156116)** — B. Tabibian, U. Upadhyay, A. De, A. Zarezade, B. Schoelkopf, M. Gomez-Rodriguez — *PNAS 116(10)*, 2019
  <br/>`PDF · peer-reviewed · DOI [10.1073/pnas.1815156116](https://doi.org/10.1073/pnas.1815156116)`
  <br/>Alt: <https://arxiv.org/abs/1712.01856>
  <br/>HIGH-SIGNAL. The major independent theoretical challenger to half-life regression, using Duolingo's own released traces.
- **[Deep Factorization Machines for Knowledge Tracing](https://arxiv.org/abs/1805.00356)** — J.-J. Vie — *BEA 2018 / arXiv 1805.00356*, 2018
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.1805.00356](https://doi.org/10.48550/arXiv.1805.00356)`
  <br/>Alt: <https://github.com/jilljenn/slam2018>
  <br/>Highly cited SLAM-based knowledge tracing, with code.
- **[Deep Reinforcement Learning of Marked Temporal Point Processes](https://arxiv.org/abs/1805.09360)** — U. Upadhyay, A. De, M. Gomez-Rodriguez — *NeurIPS 2018 / arXiv 1805.09360*, 2018
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.1805.09360](https://doi.org/10.48550/arXiv.1805.09360)`
  <br/>Follow-on optimal-review-scheduling work on the same data.
- **[Predicting and Explaining Behavioral Data with Structured Feature Space Decomposition](https://arxiv.org/abs/1810.09841)** — P.G. Fennell, Z. Zuo, K. Lerman — *EPJ Data Science / arXiv 1810.09841*, 2018
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.1810.09841](https://doi.org/10.48550/arXiv.1810.09841)`
  <br/>Uses Duolingo learner behaviour traces.
- **[Second Language Acquisition Modeling (SLAM shared task overview)](https://research.duolingo.com/papers/settles.slam18.pdf)** — B. Settles, C. Brust, E. Gustafson, M. Hagiwara, N. Madnani — *BEA @ NAACL-HLT 2018*, 2018
  <br/>`PDF · peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://aclanthology.org/W18-0506/>
  <br/>Released the dataset that seeded an entire external knowledge-tracing literature.
- **[Using Simpson's Paradox to Discover Interesting Patterns in Behavioral Data](https://arxiv.org/abs/1805.03094)** — N. Alipourfard, P.G. Fennell, K. Lerman — *ICWSM 2018 / arXiv 1805.03094*, 2018
  <br/>`PDF · peer-reviewed · DOI [10.48550/arXiv.1805.03094](https://doi.org/10.48550/arXiv.1805.03094)`
  <br/>Demonstrates aggregation traps in Duolingo-style engagement data. Methodologically useful for critiquing in-house efficacy claims.
- **[Are Large Language Models for Education Reliable Across Languages?](https://arxiv.org/abs/2504.17720)** — (arXiv 2504.17720) — *arXiv 2504.17720*, 2025
  <br/>`PDF · not peer-reviewed · DOI [10.48550/arXiv.2504.17720](https://doi.org/10.48550/arXiv.2504.17720)`
  <br/>Uses Duolingo SLAM as a benchmark for cross-lingual educational-LLM reliability. Good multilingual-equity angle.
- **[Fair Knowledge Tracing in Second Language Acquisition](https://arxiv.org/abs/2412.18048)** — W. Tang, G. Chen, S. Zu, J. Luo — *arXiv 2412.18048*, 2024
  <br/>`PDF · not peer-reviewed · DOI [10.48550/arXiv.2412.18048](https://doi.org/10.48550/arXiv.2412.18048)`
  <br/>HIGH-SIGNAL. Fairness audit of models trained on Duolingo SLAM data across platforms and regions. Sits exactly at datasets x ethics.
- **[Deep Knowledge Tracing is an implicit dynamic multidimensional item response theory model](https://arxiv.org/abs/2309.12334)** — (arXiv 2309.12334) — *arXiv 2309.12334*, 2023
  <br/>`PDF · not peer-reviewed · DOI [10.48550/arXiv.2309.12334](https://doi.org/10.48550/arXiv.2309.12334)`
  <br/>Theoretical unification of DKT and IRT; relevant to reverse-engineering Birdbrain.
- **[Duolingo Shared Task on Second Language Acquisition Modeling (Stanford CS230 project report)](http://cs230.stanford.edu/projects_winter_2021/reports/70768216.pdf)** — Stanford CS230 — *Stanford CS230*, 2021
  <br/>`PDF · not peer-reviewed`
  <br/>Student replication. Evidence of the dataset's teaching and benchmark afterlife.
- **[Replication of Duolingo's Half-Life Regression in PyTorch](https://github.com/phcavelar/duolingo-spaced-repetition)** — P.H.C. Avelar et al. — *GitHub*, 2021
  <br/>`not peer-reviewed`
  <br/>Independent reimplementation of Settles & Meeder 2016.
- **[2020 Notification Bandit Data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/23ZWVI)** — Duolingo — *Harvard Dataverse*, 2020
  <br/>`not peer-reviewed · Duolingo-authored · DOI [10.7910/DVN/23ZWVI](https://doi.org/10.7910/DVN/23ZWVI)`
  <br/>200M push-notification examples. Companion to Yancey & Settles 2020.
- **[Data for the 2020 Duolingo Shared Task (STAPLE)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/38OJR6)** — Duolingo — *Harvard Dataverse*, 2020
  <br/>`not peer-reviewed · Duolingo-authored · DOI [10.7910/DVN/38OJR6](https://doi.org/10.7910/DVN/38OJR6)`
  <br/>Alt: <https://huggingface.co/datasets/SEACrowd/duolingo_staple_2020>
  <br/>3M+ English sentences with weighted multi-translations into 5 languages.
- **[duolingo/duolingo-sharedtask-2020 (STAPLE starter code)](https://github.com/duolingo/duolingo-sharedtask-2020/)** — Duolingo — *GitHub*, 2020
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://github.com/duolingo>
  <br/>Official baselines for the STAPLE task.
- **[Data for the 2018 Duolingo Shared Task on Second Language Acquisition Modeling (SLAM)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/8SWHNO)** — Duolingo — *Harvard Dataverse*, 2018
  <br/>`not peer-reviewed · Duolingo-authored · DOI [10.7910/DVN/8SWHNO](https://doi.org/10.7910/DVN/8SWHNO)`
  <br/>Alt: <https://sharedtask.duolingo.com/2018.html>
  <br/>7M words, 6,000+ learners, 30 days. The most reused Duolingo dataset in external research.
- **[Second Language Acquisition Modeling: An Ensemble Approach](https://arxiv.org/abs/1806.04525)** — A. Osika, S. Nilsson, A. Sydorchuk, F. Sahin, A. Huss — *arXiv 1806.04525*, 2018
  <br/>`PDF · not peer-reviewed · DOI [10.48550/arXiv.1806.04525](https://doi.org/10.48550/arXiv.1806.04525)`
  <br/>The winning SLAM shared-task system.
- **[Analysis of Half-Life Regression Model Made by Duolingo](https://papousek.github.io/analysis-of-half-life-regression-model-made-by-duolingo.html)** — J. Papousek — *Grey literature (personal site)*, 2016
  <br/>`not peer-reviewed`
  <br/>HIGH-SIGNAL grey literature. Argues HLR's reported gains are partly an artifact of the evaluation setup. Frequently cited in the adaptive-learning community.
- **[duolingo/halflife-regression (reference implementation)](https://github.com/duolingo/halflife-regression)** — Duolingo — *GitHub*, 2016
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Official HLR code plus baselines and evaluation.
- **[Replication Data for: A Trainable Spaced Repetition Model for Language Learning](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/N8XJME)** — Duolingo — *Harvard Dataverse*, 2016
  <br/>`not peer-reviewed · Duolingo-authored · DOI [10.7910/DVN/N8XJME](https://doi.org/10.7910/DVN/N8XJME)`
  <br/>Alt: <https://github.com/duolingo/halflife-regression>
  <br/>13M user-word learning traces. The basis for every external HLR replication.

## Ethics, responsible AI and critical scholarship

*15 sources*

- **[Encouraging Repeated App Usage Through Habit-Forming Mechanisms: A Case Study Using the Example of Duolingo](https://doi.org/10.51137/wrp.ijmat.908)** — C. Maass — *International Journal of Mobile Applications and Technologies*, 2026
  <br/>`PDF · peer-reviewed · DOI [10.51137/wrp.ijmat.908](https://doi.org/10.51137/wrp.ijmat.908)`
  <br/>Behavioural-design / compulsion-loop analysis. Open access.
- **[Mobile-assisted language learning with commercial apps: A focused methodological review of quantitative/mixed methods research - and ethics](https://www.sciencedirect.com/science/article/abs/pii/S2772766125000072)** — Research Methods in Applied Linguistics — *Research Methods in Applied Linguistics*, 2025
  <br/>`peer-reviewed`
  <br/>HIGH-SIGNAL. Interrogates the ethics of researching commercial apps, including researcher-company entanglement. Directly relevant to the mixed-authorship problem.
- **[Revisiting Foucault's panopticon: how does AI surveillance transform educational norms?](https://doi.org/10.1080/01425692.2025.2501118)** — British Journal of Sociology of Education — *British Journal of Sociology of Education*, 2025
  <br/>`peer-reviewed · DOI [10.1080/01425692.2025.2501118](https://doi.org/10.1080/01425692.2025.2501118)`
  <br/>Theoretical frame for AI-proctoring and learning-surveillance critique; applies to DET proctoring.
- **[Generative artificial intelligence, co-evolution, and language education](https://doi.org/10.1111/modl.12932)** — S.L. Thorne et al. — *Modern Language Journal 108(S1)*, 2024
  <br/>`PDF · peer-reviewed · DOI [10.1111/modl.12932](https://doi.org/10.1111/modl.12932)`
  <br/>Alt: <https://doi.org/10.1111/modl.12925>
  <br/>Companion piece in the same MLJ special issue (see also Davin, 10.1111/modl.12925).
- **[How Do We Demonstrate AI Responsibility: The Devil Is in the Details](https://doi.org/10.3102/10769986241257963)** — M.S. Johnson — *Journal of Educational and Behavioral Statistics*, 2024
  <br/>`peer-reviewed · DOI [10.3102/10769986241257963](https://doi.org/10.3102/10769986241257963)`
  <br/>HIGH-SIGNAL. External statistician's direct rebuttal to Duolingo's Responsible AI claims. Rare formal scholarly pushback - pair with burstein24rai.
- **[Twenty-first century technologies and language education: Charting a path forward](https://doi.org/10.1111/modl.12924)** — R. Kern — *Modern Language Journal 108(S1)*, 2024
  <br/>`peer-reviewed · DOI [10.1111/modl.12924](https://doi.org/10.1111/modl.12924)`
  <br/>The flagship applied-linguistics disciplinary response to commercial AI language tools.
- **[Gamification, Motivation, and Contradiction: A Critical Analysis of Duolingo](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6846283)** — L. Espinosa Ospina — *SSRN*, 2026
  <br/>`PDF · not peer-reviewed`
  <br/>Reads Duolingo through Self-Determination Theory plus dark patterns.
- **[Not Just Duolingo: Supporting Immigrant Language Preservation Through Family-Based Play](https://arxiv.org/abs/2604.00282)** — A. Ciuba, Z.Y.Y. Li, A. Gautam — *arXiv 2604.00282*, 2026
  <br/>`PDF · not peer-reviewed · DOI [10.48550/arXiv.2604.00282](https://doi.org/10.48550/arXiv.2604.00282)`
  <br/>HIGH-SIGNAL. HCI design critique: Duolingo's individualist, gamified, AI-driven model is inadequate for heritage-language and community needs.
- **[Duolingo's Controversial AI-Driven Course Expansion](https://www.onlineeducation.com/features/duolingo-ai-course-expansion)** — OnlineEducation.com — *OnlineEducation.com*, 2025
  <br/>`not peer-reviewed`
  <br/>Linguists on low-resource languages being underrepresented in training data. Good source for the equity critique.
- **[The Duolingo English Test Responsible AI Standards (DRR-25-03)](https://duolingo-papers.s3.us-east-1.amazonaws.com/other/Duolingo+English+Test+Responsible+AI.pdf)** — Duolingo English Test — *Duolingo research report*, 2025
  <br/>`PDF · not peer-reviewed · Duolingo-authored`
  <br/>KEY. Four principles: validity/reliability, fairness, privacy/security, accountability/transparency. Covers the TEST ONLY, not the consumer app.
- **[Responsible AI for Test Equity and Quality: The Duolingo English Test as a Case Study](https://arxiv.org/abs/2409.07476)** — J. Burstein, G.T. LaFlair, K.P. Yancey, A.A. von Davier, R. Dotan — *arXiv 2409.07476*, 2024
  <br/>`PDF · not peer-reviewed · Mixed Duolingo/external authorship · DOI [10.48550/arXiv.2409.07476](https://doi.org/10.48550/arXiv.2409.07476)`
  <br/>KEY. Co-authored with independent AI ethicist Ravit Dotan. The target of Johnson's 2024 rebuttal.
- **[Where Assessment Validation and Responsible AI Meet](https://arxiv.org/abs/2411.02577)** — J. Burstein, G.T. LaFlair — *arXiv 2411.02577*, 2024
  <br/>`PDF · not peer-reviewed · Duolingo-authored · DOI [10.48550/arXiv.2411.02577](https://doi.org/10.48550/arXiv.2411.02577)`
  <br/>Alt: <https://files.eric.ed.gov/fulltext/EJ1494890.pdf>
  <br/>Argues validity theory and responsible-AI frameworks should be unified.
- **[Why AI in education needs custodianship](https://blog.englishtest.duolingo.com/ai-education-custodianship-responsible-ai/)** — Duolingo English Test — *DET blog*, 2024
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://blog.englishtest.duolingo.com/a-holistic-approach-to-ai-in-education/>
  <br/>First-party AI-ethics argument from the assessment side.
- **[Surveillance Capitalism in Schools: What's the Problem?](https://static1.squarespace.com/static/5cf15af7a259990001706378/t/61f83a89da35695874e24398/1643657868894/Stockman_Nottingham_2022.pdf)** — Stockman & Nottingham — *Working paper*, 2022
  <br/>`PDF · not peer-reviewed`
  <br/>Cites Duolingo topping an edtech-app study for data collection across 19 segments, sharing identifiers with Facebook. The most concrete academic privacy datapoint found.
- **[When Gamification Spoils Your Learning: A Qualitative Case Study of Gamification Misuse in a Language-Learning App](https://arxiv.org/abs/2203.16175)** — R. Hadi Mogavi, B. Guo, Y. Zhang, E.-U. Haq, P. Hui, X. Ma — *arXiv 2203.16175*, 2022
  <br/>`PDF · not peer-reviewed · DOI [10.48550/arXiv.2203.16175](https://doi.org/10.48550/arXiv.2203.16175)`
  <br/>HIGH-SIGNAL. The best-known independent critical HCI study of Duolingo's gamification; documents how streaks and leagues displace learning goals.

## AI and labour: the contractor cuts and the 'AI-first' pivot

*18 sources*

- **[English Teachers' Professional Identity in the Age of AI: A Meta-Ethnographic Synthesis](https://www.ijlter.org/index.php/ijlter/article/view/17636)** — Sumalinog — *IJLTER*, 2026
  <br/>`PDF · peer-reviewed`
  <br/>Deskilling / identity-disruption framework applicable to the replaces-teachers debate.
- **[Professional identity in AI-supported EFL teaching: a comparative qualitative study of pre-service and in-service teachers](https://doi.org/10.3389/feduc.2026.1783566)** — Frontiers in Education — *Frontiers in Education*, 2026
  <br/>`PDF · peer-reviewed · DOI [10.3389/feduc.2026.1783566](https://doi.org/10.3389/feduc.2026.1783566)`
  <br/>Open access.
- **[Human resource management in the age of generative artificial intelligence](https://doi.org/10.1111/1748-8583.12524)** — P. Budhwar, S. Chowdhury, G. Wood et al. — *Human Resource Management Journal 33(3)*, 2023
  <br/>`PDF · peer-reviewed · DOI [10.1111/1748-8583.12524](https://doi.org/10.1111/1748-8583.12524)`
  <br/>800+ citations. The standard scholarly framing for AI-first workforce restructuring. Open access.
- **[Duolingo CEO backs off from evaluating employees on their AI usage](https://fortune.com/2026/04/13/duolingo-ceo-luis-von-ahn-ai-usage-requirement-employee-performance-evaluations/)** — Fortune — *Fortune*, 2026
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.entrepreneur.com/business-news/duolingos-ceo-changing-how-he-measures-employee-performance-backlash>
  <br/>ESSENTIAL BOOKEND, 13 Apr 2026. AI usage dropped from performance reviews one year on.
- **[Duolingo's AI-first (Museum of Failure exhibit)](https://museumoffailure.com/exhibition/duolingo-ai-failure)** — Museum of Failure — *Museum of Failure*, 2026
  <br/>`not peer-reviewed`
  <br/>Alt: <https://businessjournalism.org/2026/05/duolingo/>
  <br/>The episode canonised as a business-failure case study - a cultural-reception datapoint in its own right.
- **[As Duolingo Turns to AI, Some Users Say Language App Has Joined 'The Dark Side'](https://www.the74million.org/article/as-duolingo-turns-to-ai-some-users-say-language-app-has-joined-the-dark-side/)** — The 74 — *The 74*, 2025
  <br/>`not peer-reviewed`
  <br/>Education journalism; strong on user and educator sentiment.
- **[Duolingo CEO says controversial AI memo was misunderstood](https://techcrunch.com/2025/08/17/duolingo-ceo-says-controversial-ai-memo-was-misunderstood/)** — TechCrunch — *TechCrunch*, 2025
  <br/>`not peer-reviewed`
  <br/>Alt: <https://fortune.com/2025/08/18/duolingo-ceo-admits-controversial-ai-memo-did-not-give-enough-context-insists-company-never-laid-off-full-time-employees/>
  <br/>Aug 2025. Note the careful full-time vs contractor distinction in the follow-up.
- **[Duolingo CEO walks back AI-first comments: 'I do not see AI as replacing what our employees do'](https://fortune.com/2025/05/24/duolingo-ai-first-employees-ceo-luis-von-ahn/)** — Fortune — *Fortune*, 2025
  <br/>`not peer-reviewed`
  <br/>Alt: <https://fortune.com/2025/06/09/duolingo-ceo-surprised-backlash-ai-first-company-announcement/>
  <br/>The definitive walk-back story, 24 May 2025.
- **[Duolingo deletes all its TikTok videos after AI backlash - and then returns with a strange message](https://www.fastcompany.com/91338068/duolingo-deletes-tiktok-ai-backlash-returns-with-strange-message)** — Fast Company — *Fast Company*, 2025
  <br/>`not peer-reviewed · bot-blocked, opens in browser`
  <br/>Alt: <https://adage.com/social-media/aa-duolingo-wipes-tiktok-instagram-ai-backlash/>
  <br/>Best single source on the social-account wipe; contains the 'experimenting with silence' quote.
- **[Fact Check: Duolingo said it would become 'AI-first' and that it plans to replace contractors](https://www.snopes.com/fact-check/duolingo-ai-first/)** — Snopes — *Snopes*, 2025
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.entrepreneur.com/business-news/duolingo-ceo-clarifies-ai-stance-after-backlash-read-memo/492141>
  <br/>BEST CITATION for the original memo text. Verifies authenticity and reproduces it in full - the LinkedIn original has no stable permalink.
- **[Inside Duolingo's Controversial 'AI-First' Strategy (WSJ Tech News Briefing)](https://pod.wave.co/podcast/wsj-tech-news-briefing/inside-duolingos-controversial-ai-first-strategy)** — WSJ — *WSJ*, 2025
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.youtube.com/watch?v=lNJBGmtJr_g>
  <br/>23 Sep 2025. CTO on the record about the fallout; alt_url has the internal-culture claims (Fri-AI-Days, ~100% 'bi-coded').
- **[Is Duolingo the face of an AI jobs crisis?](https://techcrunch.com/2025/05/04/is-duolingo-the-face-of-an-ai-jobs-crisis/)** — TechCrunch — *TechCrunch*, 2025
  <br/>`not peer-reviewed`
  <br/>BEST SYNTHESIS of the labour thread: connects the 2023/2024 contractor cuts (incl. the Oct 2024 round) to the 2025 memo.
- **[Duolingo cut 10% of its contractor workforce as the company embraces AI](https://techcrunch.com/2024/01/09/duolingo-cut-10-of-its-contractor-workforce-as-the-company-embraces-ai)** — TechCrunch — *TechCrunch*, 2024
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.cnn.com/2024/01/09/tech/duolingo-layoffs-due-to-ai>
  <br/>9 Jan 2024, following Bloomberg's 8 Jan scoop.
- **[Duolingo lays off 10% of contractors amid AI push (AI incident record)](https://oecd.ai/en/incidents/2024-01-08-13c5)** — OECD AI Incidents Monitor — *OECD.AI*, 2024
  <br/>`not peer-reviewed`
  <br/>HIGH-SIGNAL. The canonical institutionally-catalogued record classifying the contractor cuts as an AI labour incident. Citable in policy/ethics writing.
- **[Duolingo offboards translation contractors; workers allege AI replacement](https://www.campaignasia.com/article/duolingo-offboards-translation-contractors-workers-allege-ai-replacement/493703)** — Campaign Asia — *Campaign Asia*, 2024
  <br/>`not peer-reviewed`
  <br/>LOAD-BEARING CONTRADICTION: CMO's 'not directly related to the use of AI' denial vs the company's simultaneous Bloomberg confirmation.
- **[Duolingo Translator Layoffs Spark AI Debate](https://slator.com/duolingo-translator-layoffs-spark-ai-debate/)** — Slator — *Slator*, 2024
  <br/>`not peer-reviewed`
  <br/>Language-industry trade press; best source for translator-community reaction and the originating Reddit post.
- **[Duolingo turns to AI, laying off some language app translators](https://www.washingtonpost.com/technology/2024/01/10/duolingo-ai-layoffs/)** — The Washington Post — *Washington Post*, 2024
  <br/>`not peer-reviewed · bot-blocked, opens in browser`
  <br/>The highest-profile national framing. Paywalled and script-blocked; needs a browser or library access.
- **[Duolingo, relying more on AI, says it will lay off some contract translators](https://www.post-gazette.com/business/tech-news/2024/01/08/duolingo-lays-off-contract-translators-ai/stories/202401080079)** — Pittsburgh Post-Gazette — *Pittsburgh Post-Gazette*, 2024
  <br/>`not peer-reviewed`
  <br/>Earliest dated local reporting with company statements, 8 Jan 2024.

## Corporate strategy, filings and research infrastructure

*26 sources*

- **[Campaign Critique: The Strategic 'Marriage' of Duolingo and Luckin Coffee (2025)](https://doi.org/10.54097/s5p0e681)** — S. Zhang — *Frontiers in Business, Economics and Management*, 2026
  <br/>`PDF · peer-reviewed · DOI [10.54097/s5p0e681](https://doi.org/10.54097/s5p0e681)`
  <br/>Brand/marketing critique; useful for the Duolingo-as-media-company angle. Open access.
- **[Alina A. von Davier - Google Scholar](https://scholar.google.com/citations?hl=en&user=Eu9DtEsAAAAJ)** — A.A. von Davier — *Google Scholar*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Chief Assessment Scientist; drives the computational-psychometrics agenda.
- **[Ben Naismith - Google Scholar](https://scholar.google.com/citations?user=4ldMyhMAAAAJ&hl=en)** — B. Naismith — *Google Scholar*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Applied-linguistics side of DET research.
- **[Burr Settles - publications](https://burrsettles.com/publications)** — B. Settles — *Personal site*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Former Duolingo research lead; author of HLR and the TACL DET paper.
- **[Duolingo (DUOL) Q1 2026 Earnings Call Transcript](https://www.fool.com/earnings/call-transcripts/2026/05/04/duolingo-duol-q1-2026-earnings-transcript/)** — The Motley Fool — *Motley Fool*, 2026
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.fool.com/earnings/call-transcripts/2026/08/12/duolingo-duol-q2-2026-earnings-call-transcript/>
  <br/>Management in their own words on AI investment trade-offs. Q2 2026 transcript in alt_url.
- **[Duolingo English Test - Research and Innovation](https://englishtest.duolingo.com/research)** — Duolingo English Test — *Duolingo*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://englishtest.duolingo.com/research/publications>
  <br/>The active first-party publishing channel post-2021. Client-rendered, so not machine-enumerable.
- **[Duolingo Form 10-K, FY2025](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm)** — Duolingo, Inc. — *SEC EDGAR*, 2026
  <br/>`not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>KEY. The most citable legally-vetted AI statement Duolingo has made: AI strategy language plus vendor-dependency and compute-cost risk factors.
- **[Duolingo Investor Relations (shareholder letters, filings, events)](https://investors.duolingo.com/)** — Duolingo, Inc. — *Duolingo IR*, 2026
  <br/>`not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>Alt: <https://investors.duolingo.com/press>
  <br/>Root for all primary financial sources. Bot-blocked to scripts; opens fine in a browser.
- **[Duolingo Research portal](https://research.duolingo.com/)** — Duolingo — *Duolingo*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>FINDING: the publication list is frozen at 2021. Do not treat as the current research index.
- **[Duolingo's 2026 Strategy: The Road to 100 Million DAUs](https://www.classcentral.com/report/duolingo-2026-strategy/)** — Class Central Report — *Class Central*, 2026
  <br/>`not peer-reviewed`
  <br/>Independent edtech-analyst breakdown of the 2026 AI roadmap.
- **[Geoffrey T. LaFlair - Google Scholar](https://scholar.google.com/citations?user=QPU66QMAAAAJ&hl=en)** — G.T. LaFlair — *Google Scholar*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Assessment-side research lead.
- **[James Sharpnack - publications](https://jsharpna.github.io/publications/)** — J. Sharpnack — *Personal site*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://dblp.org/pid/77/8159.html>
  <br/>Leads the 2024-2026 CAT/bandit line; incl. NeurIPS 2024 keynote on human-in-the-loop AI testing.
- **[Kevin P. Yancey - Google Scholar](https://scholar.google.com/citations?user=lyA6yCYAAAAJ&hl=en)** — K.P. Yancey — *Google Scholar*, 2026
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>The most complete single list of Duolingo AI work, incl. patents.
- **[Q2 FY2026 Shareholder Letter](https://investors.duolingo.com/static-files/3c8277ee-bc94-4f5d-9b77-0db3e46f88b8)** — Duolingo, Inc. — *Duolingo IR*, 2026
  <br/>`PDF · not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>Alt: <https://investors.duolingo.com/static-files/aab30d54-eb91-422e-b365-c03859fea85c>
  <br/>Documents the AI inference-cost collapse (Video Call ~$0.30 to under $0.01 per call) and the shift to open-weight models.
- **[The World's Top EdTech Companies of 2026](https://time.com/article/2026/07/22/worlds-top-edtech-companies-2026/)** — TIME / Statista — *TIME*, 2026
  <br/>`not peer-reviewed`
  <br/>Alt: <https://time.com/article/2026/07/26/duolingo-ceo-luis-von-ahn-interview/>
  <br/>Duolingo ranked #1 US edtech. Useful for the 'backlash didn't dent the business' argument. alt_url is the Jul 2026 von Ahn interview.
- **[Duolingo CEO: AI makes my employees 'four or five times' as productive - without laying off a single human](https://www.cnbc.com/2025/09/17/duolingo-ceo-how-ai-makes-my-employees-more-productive-without-layoffs.html)** — CNBC — *CNBC*, 2025
  <br/>`not peer-reviewed`
  <br/>The 4-5x productivity claim on the record. An unverified quantitative claim worth flagging.
- **[Duolingo Co-Founder Severin Hacker: How AI Impacts the Future of Work and Education](https://www.youtube.com/watch?v=B9sEJurtZIU)** — The Twenty Minute VC — *20VC*, 2025
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.thetwentyminutevc.com/severin-hacker>
  <br/>Hacker's most substantive AI interview; the '100+ courses this year, would have taken tens of years' claim.
- **[Gaming as the Future of Education with Duolingo CEO Luis von Ahn (No Priors Ep. 114)](https://www.youtube.com/watch?v=st6uE-dlunY)** — No Priors (S. Guo, E. Gil) — *No Priors podcast*, 2025
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.gsb.stanford.edu/events/view-top-luis-von-ahn>
  <br/>8 May 2025. Contains the 'AI will teach better than human teachers; schools survive as childcare' prediction.
- **[Klinton Bicknell - papers and CV](https://www.klintonbicknell.com/papers.html)** — K. Bicknell — *Personal site*, 2025
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://www.klintonbicknell.com/bicknell_cv.pdf>
  <br/>Head of AI. CV (Dec 2025) is the best single record of talks not otherwise indexed.
- **[Q1 FY2025 Shareholder Letter](https://investors.duolingo.com/static-files/01420520-3377-4985-887b-55ed3c1e4fc5)** — Duolingo, Inc. — *Duolingo IR*, 2025
  <br/>`PDF · not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>The quarter covering the AI-first memo and the 148-course launch.
- **[Q2 FY2025 Shareholder Letter](https://investors.duolingo.com/static-files/0b55110c-2eb9-466d-8549-5459e0851290)** — Duolingo, Inc. — *Duolingo IR*, 2025
  <br/>`PDF · not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>The quarter covering the backlash and the DAU-growth debate.
- **[3 ways Duolingo improves education using AI](https://blog.duolingo.com/ai-improves-education/)** — S. Wodzak — *Duolingo blog*, 2024
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://blog.duolingo.com/ai-democratize-education/>
  <br/>Duolingo's own framing of AI as social good.
- **[Duolingo CEO Luis von Ahn wants you addicted to learning (Decoder)](https://podcasts.apple.com/us/podcast/duolingo-ceo-luis-von-ahn-wants-you-addicted-to-learning/id1011668648?i=1000673004475)** — Decoder with Nilay Patel — *The Verge / Decoder*, 2024
  <br/>`not peer-reviewed`
  <br/>14 Oct 2024. Longest-form PRE-memo von Ahn interview on AI and product.
- **[The Duolingo Handbook: 14 Years of Big Learnings](https://www.slideshare.net/slideshow/the-duolingo-handbook-14-years-of-big-learnings-in-one-little-handbook/275534515)** — Duolingo — *Duolingo (SlideShare mirror)*, 2024
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>The public artifact of the operating philosophy the AI-first memo builds on.
- **[2022 Duolingo Research Grant](https://blog.duolingo.com/2022-duolingo-research-grant)** — Duolingo — *Duolingo blog*, 2022
  <br/>`not peer-reviewed · Duolingo-authored`
  <br/>Alt: <https://www.duolingo.com/efficacy/research>
  <br/>External research-grant programme - relevant to researcher-company entanglement questions.
- **[Duolingo Form 10-K, FY2021](https://www.sec.gov/Archives/edgar/data/1562088/000156208822000039/duol-20211231.htm)** — Duolingo, Inc. — *SEC EDGAR*, 2022
  <br/>`not peer-reviewed · Duolingo-authored · bot-blocked, opens in browser`
  <br/>BASELINE. How Duolingo described AI/ML strategy and risk BEFORE generative AI. SEC blocks scripted access; needs a browser.

## Competitor context

*2 sources*

- **[10 Best AI Language Learning Apps for Speaking (2026)](https://www.talkio.ai/blog/best-ai-language-speaking-practice-apps-in-2026)** — Talkio AI — *Talkio AI*, 2026
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.borderset.com/blogs/posts/top-10-ai-language-learning-apps-2026>
  <br/>Feature comparison across Duolingo, Babbel, Speak, ELSA, Praktika, Memrise, Busuu. Vendor-adjacent: read for structure, not verdict.
- **[Try Little Language Lessons, learning experiments using Gemini 2.0](https://blog.google/products-and-platforms/products/education/little-language-lessons/)** — Google — *Google Keyword blog*, 2025
  <br/>`not peer-reviewed`
  <br/>Alt: <https://www.androidpolice.com/google-labs-little-language-lessons/>
  <br/>The platform-incumbent threat to Duolingo's core, built on Gemini/LearnLM.

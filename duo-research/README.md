# Duolingo & AI — research source collection

Source base for a literature review on Duolingo and artificial intelligence.
223 sources, 2015–2026 (emphasis on 2020 onward). Every URL was checked
programmatically; nothing is listed without a resolving link.

| File | What it is |
|---|---|
| [`sources.md`](sources.md) | The annotated inventory, grouped by theme. Start here. |
| [`sources.csv`](sources.csv) | Same records, flat and filterable. Imports into Zotero/Sheets. |
| [`questions.md`](questions.md) | Findings from building the collection, plus nine proposed sub-questions with the sources that bear on each. |
| [`data/sources.json`](data/sources.json) | Source of truth. Edit `data/part*.json`, then rebuild. |
| `index.html` | Browsable filterable page (published as an Artifact). |

## Rebuilding

```
python build.py       # data/part*.json -> sources.json, sources.md, sources.csv
python make_page.py   # sources.json -> index.html
```

## Field notes

- **`provenance`** is the field that matters most: `duolingo` / `mixed` / `independent` /
  `press`. A large share of research on Duolingo's AI is written by Duolingo, including the
  only peer-reviewed study of its GPT-4 features. Never pool in-house and independent
  evidence without saying so.
- **`status: blocked`** means the publisher refuses scripted requests (SEC EDGAR, Duolingo
  investor relations, some paywalled outlets). The link is live in a browser.
- **`peer_reviewed`** reflects the venue, not quality. Whitepapers, preprints and blog posts
  are included where they are the only account of a system — which for Duolingo's consumer
  AI is often the case.

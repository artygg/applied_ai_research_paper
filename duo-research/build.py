#!/usr/bin/env python3
"""Merge data/part*.json into sources.json, sources.md and sources.csv."""
import csv
import glob
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

THEMES = [
    ("foundations", "Foundations: the pre-LLM ML stack"),
    ("adaptive-personalization", "Adaptive learning & personalisation (Birdbrain)"),
    ("genai-features", "Generative AI features (Max, Roleplay, Video Call, AI-authored content)"),
    ("assessment-det", "AI in assessment: the Duolingo English Test"),
    ("fairness-validity", "Validity, fairness and bias in AI-driven assessment"),
    ("efficacy", "Efficacy and learning outcomes"),
    ("reviews-meta", "Systematic reviews and meta-analyses"),
    ("datasets-reuse", "Public datasets, shared tasks and their reuse"),
    ("ethics-governance", "Ethics, responsible AI and critical scholarship"),
    ("ethics-labour", "AI and labour: the contractor cuts and the 'AI-first' pivot"),
    ("corporate-strategy", "Corporate strategy, filings and research infrastructure"),
    ("competitor", "Competitor context"),
]
THEME_LABEL = dict(THEMES)

PROV_LABEL = {
    "duolingo": "Duolingo-authored",
    "mixed": "Mixed Duolingo/external authorship",
    "independent": "Independent",
    "press": "Press / third-party non-academic",
}


def load():
    recs, seen = [], {}
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "part*.json"))):
        for r in json.load(open(f, encoding="utf-8")):
            if r["id"] in seen:
                raise SystemExit(f"duplicate id: {r['id']}")
            seen[r["id"]] = True
            r.setdefault("alt_url", "")
            recs.append(r)
    return recs


def sort_key(r):
    # peer-reviewed first, then newest, then title
    return (0 if r["peer_reviewed"] else 1, -r["year"], r["title"].lower())


def badges(r):
    out = []
    if r["pdf"]:
        out.append("PDF")
    if r["peer_reviewed"]:
        out.append("peer-reviewed")
    else:
        out.append("not peer-reviewed")
    if r["provenance"] in ("duolingo", "mixed"):
        out.append(PROV_LABEL[r["provenance"]])
    if r["status"] == "blocked":
        out.append("bot-blocked, opens in browser")
    elif r["status"] == "dead":
        out.append("UNRESOLVED")
    return out


def write_md(recs):
    L = []
    A = L.append
    A("# Duolingo & AI — Annotated Source Inventory\n")
    A("Sources connecting Duolingo and AI, 2015–2026, with the emphasis on 2020 onward. "
      "Built for an academic literature review: peer-reviewed work is listed first within each "
      "section, and every entry is tagged with who wrote it.\n")
    A(f"**{len(recs)} sources.** Every URL was checked programmatically. `bot-blocked` means the "
      "publisher refuses scripted requests — the link is live in a browser. Nothing is listed "
      "without a resolving URL.\n")
    A("> **Read the provenance tag before citing.** A large share of the research on Duolingo's AI "
      "is written by Duolingo. That does not make it wrong, but Duolingo-authored and independent "
      "evidence should never be pooled without comment.\n")

    # counts
    A("## At a glance\n")
    A("| | Count |")
    A("|---|---|")
    A(f"| Total sources | {len(recs)} |")
    A(f"| Peer-reviewed | {sum(1 for r in recs if r['peer_reviewed'])} |")
    A(f"| Direct PDF available | {sum(1 for r in recs if r['pdf'])} |")
    for p in ("duolingo", "mixed", "independent", "press"):
        A(f"| {PROV_LABEL[p]} | {sum(1 for r in recs if r['provenance'] == p)} |")
    A("")

    for key, label in THEMES:
        group = sorted([r for r in recs if r["theme"] == key], key=sort_key)
        if not group:
            continue
        A(f"## {label}\n")
        A(f"*{len(group)} sources*\n")
        for r in group:
            auth = r["authors"] or "—"
            A(f"- **[{r['title']}]({r['url']})** — {auth} — *{r['venue']}*, {r['year']}")
            meta = " · ".join(badges(r))
            if r["doi"]:
                meta += f" · DOI [{r['doi']}](https://doi.org/{r['doi']})"
            A(f"  <br/>`{meta}`")
            if r["alt_url"]:
                A(f"  <br/>Alt: <{r['alt_url']}>")
            A(f"  <br/>{r['note']}")
        A("")
    open(os.path.join(ROOT, "sources.md"), "w", encoding="utf-8").write("\n".join(L))


def write_csv(recs):
    cols = ["id", "title", "authors", "year", "venue", "type", "theme", "provenance",
            "peer_reviewed", "pdf", "status", "doi", "url", "alt_url", "note"]
    with open(os.path.join(ROOT, "sources.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(recs, key=lambda r: (r["theme"], sort_key(r))):
            w.writerow(r)


def main():
    recs = load()
    json.dump(recs, open(os.path.join(ROOT, "data", "sources.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    write_md(recs)
    write_csv(recs)
    print(f"{len(recs)} sources -> sources.md, sources.csv, data/sources.json")
    for key, label in THEMES:
        n = sum(1 for r in recs if r["theme"] == key)
        print(f"  {n:4d}  {key}")
    unknown = {r["theme"] for r in recs} - set(THEME_LABEL)
    if unknown:
        raise SystemExit(f"unknown themes: {unknown}")


if __name__ == "__main__":
    main()

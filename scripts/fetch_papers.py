#!/usr/bin/env python3
"""
fetch_papers.py — Fetch LLM / AI-Agent papers from OpenReview and Semantic Scholar.

Usage:
    python fetch_papers.py --venue ICLR --year 2024 --output papers/ICLR/2024_fetched.md
    python fetch_papers.py --venue NeurIPS --year 2024 --output papers/NeurIPS/2024_fetched.md

Environment variables (optional, place in .env file):
    SEMANTIC_SCHOLAR_API_KEY=<your-key>   # Increases rate limits

Requirements:
    pip install -r requirements.txt
"""

import argparse
import json
import os
import re
import sys
import time
from typing import Optional

import requests
from tqdm import tqdm
from dotenv import load_dotenv

try:
    import openreview
except ImportError:
    openreview = None

try:
    from semanticscholar import SemanticScholar
except ImportError:
    SemanticScholar = None

load_dotenv()

# ─── Keywords for filtering relevant papers ───────────────────────────────────
KEYWORDS = [
    "language model", "llm", "large language", "gpt", "agent", "reasoning",
    "chain-of-thought", "tool use", "tool-use", "rag", "retrieval",
    "instruction tuning", "rlhf", "reinforcement learning", "alignment",
    "planning", "multi-agent", "autonomous agent", "benchmark",
]

VENUE_INVITATION_MAP = {
    "ICLR": {
        2024: "ICLR.cc/2024/Conference/-/Accepted_Paper",
        2025: "ICLR.cc/2025/Conference/-/Accepted_Paper",
    },
    "NeurIPS": {
        2024: "NeurIPS.cc/2024/Conference/-/Accepted_Paper",
        2025: "NeurIPS.cc/2025/Conference/-/Accepted_Paper",
    },
}


def is_relevant(title: str, abstract: str = "") -> bool:
    text = (title + " " + abstract).lower()
    return any(kw in text for kw in KEYWORDS)


def fetch_openreview(venue: str, year: int) -> list[dict]:
    """Fetch accepted papers from OpenReview API."""
    if openreview is None:
        print("[WARN] openreview-py not installed. Skipping OpenReview fetch.")
        return []

    invitation = VENUE_INVITATION_MAP.get(venue, {}).get(year)
    if not invitation:
        print(f"[WARN] No OpenReview invitation configured for {venue} {year}.")
        return []

    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
    papers = []
    offset = 0
    limit = 100

    print(f"[INFO] Fetching {venue} {year} from OpenReview …")
    while True:
        submissions = client.get_all_notes(invitation=invitation, offset=offset, limit=limit)
        if not submissions:
            break
        for sub in submissions:
            content = sub.content or {}
            title = (content.get("title") or {}).get("value", "")
            abstract = (content.get("abstract") or {}).get("value", "")
            if is_relevant(title, abstract):
                papers.append({
                    "title": title,
                    "abstract": abstract,
                    "authors": [a for a in (content.get("authors") or {}).get("value", [])],
                    "pdf": (content.get("pdf") or {}).get("value", ""),
                    "venue": venue,
                    "year": year,
                    "code": "",
                    "tags": infer_tags(title, abstract),
                })
        offset += limit
        if len(submissions) < limit:
            break
        time.sleep(0.5)

    print(f"[INFO] Found {len(papers)} relevant papers in {venue} {year}.")
    return papers


def enrich_with_semantic_scholar(papers: list[dict]) -> list[dict]:
    """Add arXiv links, citation counts, and code links via Semantic Scholar."""
    if SemanticScholar is None:
        print("[WARN] semanticscholar not installed. Skipping enrichment.")
        return papers

    api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    sch = SemanticScholar(api_key=api_key)

    print("[INFO] Enriching papers via Semantic Scholar …")
    for paper in tqdm(papers, desc="Semantic Scholar"):
        try:
            results = sch.search_paper(paper["title"], limit=1, fields=[
                "externalIds", "citationCount", "openAccessPdf", "publicationTypes",
            ])
            if results and results[0]:
                hit = results[0]
                external = hit.externalIds or {}
                arxiv_id = external.get("ArXiv", "")
                if arxiv_id:
                    paper["arxiv"] = f"https://arxiv.org/abs/{arxiv_id}"
                paper["citations"] = hit.citationCount or 0
        except Exception as exc:
            print(f"[WARN] Semantic Scholar lookup failed for '{paper['title']}': {exc}")
        time.sleep(0.3)

    return papers


def infer_tags(title: str, abstract: str = "") -> list[str]:
    """Heuristically assign topic tags from title and abstract text."""
    text = (title + " " + abstract).lower()
    tag_rules = {
        "reasoning": ["reasoning", "chain-of-thought", "cot"],
        "math": ["math", "mathematical", "arithmetic", "gsm8k", "math500"],
        "agent": ["agent", "agentic"],
        "multi-agent": ["multi-agent", "multiagent", "cooperative agent"],
        "tool-use": ["tool use", "tool-use", "api", "function call"],
        "RAG": ["retrieval", "rag", "augmented generation"],
        "alignment": ["alignment", "rlhf", "dpo", "reward model"],
        "code": ["code generation", "software", "programming", "coding"],
        "planning": ["planning", "plan", "task decomposition"],
        "benchmark": ["benchmark", "evaluation", "leaderboard"],
        "efficiency": ["efficient", "compress", "distil", "quantiz", "prune"],
        "scaling": ["scaling law", "scale", "scaling"],
        "fine-tuning": ["fine-tun", "finetun", "instruction tun"],
        "multimodal": ["multimodal", "vision", "image"],
        "safety": ["safety", "harmful", "jailbreak", "adversarial"],
        "data": ["synthetic data", "data generation", "dataset"],
    }
    tags = []
    for tag, patterns in tag_rules.items():
        if any(p in text for p in patterns):
            tags.append(tag)
    return tags or ["agent"]


def format_markdown_table(papers: list[dict], venue: str, year: int) -> str:
    """Render papers as a Markdown table."""
    lines = [
        f"# {venue} {year} — Fetched LLM / Agent Papers",
        "",
        f"> Auto-generated by `scripts/fetch_papers.py`. Total: {len(papers)} papers.",
        "",
        "| Title | Authors | Tags | Paper | Code |",
        "|-------|---------|------|-------|------|",
    ]
    for p in papers:
        title = p.get("title", "Unknown")
        arxiv = p.get("arxiv", "")
        paper_link = f"[arXiv]({arxiv})" if arxiv else "—"
        title_cell = f"[{title}]({arxiv})" if arxiv else title

        authors = p.get("authors", [])
        author_str = (
            f"{authors[0]} et al." if len(authors) >= 3 else ", ".join(authors) or "—"
        )

        tags = " ".join(f"`{t}`" for t in p.get("tags", []))
        code = p.get("code", "") or "—"
        code_cell = f"[GitHub]({code})" if code.startswith("http") else "—"

        lines.append(f"| {title_cell} | {author_str} | {tags} | {paper_link} | {code_cell} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch LLM papers from OpenReview + Semantic Scholar")
    parser.add_argument("--venue", required=True, choices=["ICLR", "NeurIPS"], help="Conference name")
    parser.add_argument("--year", required=True, type=int, help="Conference year")
    parser.add_argument("--output", required=True, help="Output Markdown file path")
    parser.add_argument("--json", dest="json_out", default="", help="Optional JSON output path")
    parser.add_argument("--skip-semantic-scholar", action="store_true",
                        help="Skip Semantic Scholar enrichment")
    args = parser.parse_args()

    papers = fetch_openreview(args.venue, args.year)

    if not args.skip_semantic_scholar:
        papers = enrich_with_semantic_scholar(papers)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
        print(f"[INFO] JSON written to {args.json_out}")

    md = format_markdown_table(papers, args.venue, args.year)
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"[INFO] Markdown written to {args.output}")


if __name__ == "__main__":
    main()

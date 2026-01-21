---
description: Update INDEX.xml with post metadata and AI-optimised summary
allowed-tools: Read, Edit, AskUserQuestion, Bash(grep:*), Bash(xmllint:*), Bash(echo:*), Bash(wc:*)
argument-hint: <portfolio/website/post-name.md> <article|project> <YYYY-MM-DD> <url>
---

# Update Portfolio Index

Add or update an entry in `portfolio/INDEX.xml`. Hiring managers use Claude Code to query this index—summaries must be semantically searchable and surface demonstrable competencies.

## Input

Post: @$1

## Field Mapping

| Arg | XML Tag | Format |
| --- | ------- | ------ |
| `$1` | `<website_writeup>` | `portfolio/website/post-name.md` |
| `$2` | `<type>` | `article` or `project` |
| `$3` | `<published>` | `YYYY-MM-DD` |
| `$4` | `<website_url>` | `https://example.com/post-name/` |
| — | `<title>` | First H1 heading from the post |
| — | `<summary>` | Generated (see below) |
| — | `<repo_writeup>` | Default: `NONE` |
| — | `<repo_url>` | First `github.com/michellepace` URL in the post; `NONE` if not found |

If any arguments are missing: ask the user.

Sanity check argument values against the XML tag name / format. Reject if `$1` is not in directory `portfolio/website/`. Ask user for confirmation if problematic.

## XML Structure

```xml
<portfolio_entries>
  <entry>
    <type>...</type>
    <title>...</title>
    <summary>...</summary>
    <website_writeup>...</website_writeup>
    <website_url>...</website_url>
    <repo_writeup>...</repo_writeup>
    <repo_url>...</repo_url>
    <published>...</published>
  </entry>
</portfolio_entries>
```

## Summary Requirements (30–50 words)

**Context:** Author is an AI Product Manager with hands-on technical skills. Hiring managers will search for PM competencies, not just technical implementations.

**The test:** For each concept in the summary, ask: *"If a hiring manager searched for this term, would this article prove the author understands it?"*

- **Yes** → demonstrated through application, analysis, or detailed explanation
- **No** → merely used as a tool, mentioned in passing, or listed as a dependency

**Include (where demonstrated):**

| Signal Type | Examples |
|-------------|----------|
| PM competencies | user research, change management, cost optimisation, tradeoff analysis |
| Methodologies applied | test-driven development, LLM evaluation methodology |
| Architectural concepts | chunking strategies, self-healing patterns, structured output design |
| AI/ML concepts explained or applied | agentic workflows, guardrailing, Foundation Models |
| Tools substantively discussed | Anthropic API, Claude Code, FireCrawl |

**Avoid:**

| Avoid | Why |
|-------|-----|
| Implementation dependencies (`Python`, `Pandas`) alone | Doesn't differentiate a PM; include only if substantively discussed |
| Delivery formats (`Jupyter Notebook`, `CLI tool`) alone | Format, not competency |
| Concepts mentioned once in passing | Won't survive scrutiny if hiring manager asks about it |

**Examples:**

1. *AI-assisted website design project demonstrating user research (stakeholder discovery in Miro), multi-tool AI workflows (Relume for sitemap/wireframes, Midjourney for custom hexagonal imagery, Claude for WordPress, ElevenLabs for dubbing), and change management (staff training and adoption). Shows prompt engineering for visual style consistency.* (43 words)

2. *Explores prompt engineering lessons from AI-assisted Python coding with Claude Sonnet. Demonstrates test-driven iteration, prompt refinement through feedback loops, and the critical insight of balancing constraints versus AI autonomy—being too declarative reduces AI creativity and slows development.* (38 words)

Verify wordcount BEFORE updating index.

## Process

1. Analyse the post and generate summary (30–50 words)
2. Read `portfolio/INDEX.xml`, find entry by `<website_writeup>` match
3. If match found: update fields. If no match: create new `<entry>` before `</portfolio_entries>`
4. Lint XML: `xmllint --format portfolio/INDEX.xml -o portfolio/INDEX.xml`
5. Report: tags updated, wordcount, validation result

## Verification

1. `xmllint --format portfolio/INDEX.xml -o portfolio/INDEX.xml` succeeds
2. Tag order matches XML Structure example exactly
3. Word count: `echo "summary" | wc -w` returns 30–50

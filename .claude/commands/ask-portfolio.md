---
description: Ask anything about Michelle's AI portfolio — overview, deep dive, or read between the lines.
argument-hint: <question>
allowed-tools: Read, Glob, Grep, WebFetch
---

# Ask Question About This Portfolio

Answer this question: `$ARGUMENTS`

## Context

This portfolio belongs to an AI/ML Product Manager, Michelle. The content demonstrates technical depth, product thinking, and hands-on AI implementation experience.

**Portfolio structure:**

- Index: `portfolio/INDEX.xml` — read the file, then evaluate which `<summary>` and `<title>` fields relate to this question
- Writeups: `portfolio/website/*.md` — read via `<website_writeup>` path

Example entry:

```xml
<portfolio_entries>
  <entry>
    <type>project</type>
    <title>Claude Code in Data Analysis Action</title>
    <summary>Visual walkthrough of using Claude Code for data analysis and debugging. Demonstrates agentic investigation through hypothesis formation, self-directed code analysis, root cause identification...</summary>
    <website_writeup>portfolio/website/claude-code-data-analysis-action.md</website_writeup>
    <website_url>https://ailearnlog.com/claude-code-data-analysis-action/</website_url>
    <repo_writeup>NONE</repo_writeup>
    <repo_url>https://github.com/michellepace/plot-py-repo</repo_url>
    <published>2025-10-05</published>
  </entry>
  <!-- ... more entries ... -->
</portfolio_entries>
```

## Source

- **Local path**: `portfolio/INDEX.xml`
- **Remote fallback**: `https://raw.githubusercontent.com/michellepace/craft-me-public/refs/heads/main/`

## Your Task

1. **Analyse the question** to understand what the asker wants to discover.

2. **Get the index** (see Source section for paths):
   - Try reading locally first
   - If file doesn't exist, use WebFetch on the remote URL

3. **Identify relevant entries** — don't stop at obvious matches; consider indirect relevance.

4. **Read the writeups** for identified entries (via `<website_writeup>` paths):
   - If local file exists, use Read
   - Otherwise, prepend the remote fallback URL and use WebFetch

5. **Provide a grounded answer** — synthesise insights from the portfolio content. You may infer patterns and innate qualities about the author from the evidence, but don't fabricate specific experiences not present in the files.

6. **If the portfolio doesn't cover the topic**: Say so honestly. Offer to use WebFetch against the linked `<website_url>` or `<repo_url>` for additional context.

## Response Format

Well-structured, use emojis. Adjust format intelligently based on the question — a factual query may need a short answer with a table; a character "read betwen the lines" question may need prose with supporting quotes.

Here is a format you may adapt:

<format>

```
## 🎯 ANSWER

[Direct response grounded in portfolio content]

[Add 2-3 simple supporting sentences if beneficial]

--xx--

[Summary table if helpful, include emojis]

--xx--

## 📜 EVIDENCE

[Quotes supporting your answer]

[Titles linked to `<website_url>`]

## 🙂 EXPLORE FURTHER?

[Offer 2-3 follow-up questions the asker might find valuable]

Would you like me to answer any of these:

`/ask-portfolio  [follow up question]`

[1 short sentence of why its potentially valuable]

`/ask-portfolio  [follow up question]`

[1 short sentence of why its potentially valuable]
```

</format>

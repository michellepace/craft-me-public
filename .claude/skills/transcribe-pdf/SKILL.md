---
name: transcribe-pdf
description: "Transcribe a PDF document into clean markdown including hyperlinks."

argument-hint: [pdf-path]
disable-model-invocation: true
allowed-tools: Read, Write, Grep, Glob, Bash(uv run --with pymupdf *), Bash(npx markdownlint-cli2 *)
---

# Transcribe PDF to Markdown

- PDF to transcribe: `$0`
- OUTPUT_FILE: !`echo "$0" | sed 's/\.pdf$/.md/'`

## Step 1: Visually transcribe

Read the PDF to visually transcribe it into markdown. Use appropriate markdown: headings for sections, tables for tabular data, bold/italic as shown, bullet lists, blockquotes for metadata (location, dates).

## Step 2: Add hyperlinks

Insert the relevant hyperlinks at the correct locations, extract hyperlinks by running:

```bash
uv run --with pymupdf .claude/skills/transcribe-pdf/scripts/extract_links.py "$0"
```

## Step 3: Lint

Run `npx markdownlint-cli2 --fix [OUTPUT_FILE]`.

## Step 4: Verify

Content of each section is complete and intact.

Recommend any spelling or grammar corrections - use British spelling and style. Flag any hyperlinks that don't appear sensical.

Output: Well-structred verification summary and recommendations.

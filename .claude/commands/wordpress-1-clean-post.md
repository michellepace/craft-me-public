---
description: Convert WordPress block markup to clean markdown
allowed-tools: Read, Edit, Bash(npx markdownlint-cli2:*), Bash(curl:*)
argument-hint: <portfolio/website/post-name.md>
---

# Clean WordPress Post

Convert WordPress Gutenberg block markup to clean, readable markdown for improved LLM comprehension.

The author is an AI Product Manager with hands-on technical skills. Potential clients and hiring managers will use AI to analyse the post and draw insights about the author. Consider this when generating alt text for images.

## Input

Post: @$1

## Transformation Rules

1. **Remove all WordPress block comments**: Strip `<!-- wp:* -->`, `<!-- /wp:* -->`, and `<!-- wp:block {"ref":*} /-->` patterns
2. **Remove all HTML wrapper elements**: Strip tags like `<div>`, `<figure>`, `<table>`, `<span>`, `<p>`, etc. — keep only the text content within
3. **Remove presentational elements**: Strip spacers, empty paragraphs, and purely decorative markup
4. **Preserve content**: Keep all text, links, and semantic meaning intact

## Output Format

### Metadata Header

If the post starts with a sidebar/column containing metadata (labels like "Tools", "The Crux", "Solution", etc.), convert to simple bold-label format. Example:

```markdown
**Label:** value

**Another Label:** value
```

For example:

```markdown
**Tools Used:** [value]
**Techniques Used:** [value]
**Solution:** [link if present]
```

### Structure

Preserve all structure, including:

- Headings (h1, h2, h3, etc.)
- Lists (ordered and unordered)
- Paragraph breaks
- Use `---` for horizontal rules

### Links

Preserve all links as `[text](url)`

### Tables

Convert HTML tables to markdown table syntax. Left-align all column headers.

### Code Blocks

Use triple-backtick fenced blocks. Infer language from content before WordPress hints (e.g., `{"language":"bash"}`) or content.

### Embeds (YouTube, etc.)

Convert to a markdown link with the caption as link text:

```markdown
[Caption or "Video"](url)
```

### Images

Convert to markdown image syntax. If a caption exists, add it as italic text below:

```markdown
![alt text](url)

*Caption if present*
```

**Empty alt text handling:** When original images have empty or missing alt text (`alt=""`):

1. Download images to `/tmp/` using `curl -s -o /tmp/filename.ext "url"`
2. Use Read tool to visually analyse each downloaded image
3. Write alt text describing what the image demonstrates, optimised for LLM comprehension and reflecting the author's product and technical expertise
4. Do NOT infer alt text from surrounding text alone — always analyse the actual image

## Process

1. Read the input file
2. Transform content following the rules above
3. Overwrite the original file with clean markdown
4. Run markdownlint with auto-fix `npx markdownlint-cli2 --fix $1`
5. Conduct verifications

## Verification

After clean-up, verify:

1. **Content completeness**: All text from original is preserved
2. **Structure**: Title and all headings preserved
3. **Links**: All hyperlinks preserved
4. **Tables**: Converted to markdown table syntax
5. **Code blocks**: In fenced blocks with language identifier where determinable
6. **Embeds**: YouTube/video embeds converted to markdown links
7. **Images**: Converted to `![alt](url)` format, captions in italics if present.

8. **Markdown lint**: Run `npx markdownlint-cli2 --fix $1` — should pass

Report verification results.

For all images that did not contain alt text, report:

```
---

URL: `[https://example.com/image.png]`
Alt: *[generated alt text]*
Contextual Fit: [why this alt text aids post comprehension]
```

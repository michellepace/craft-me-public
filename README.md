# Chat with My Portfolio

Use AI to chat with my portfolio.

<a href="https://ailearnlog.com/" target="_blank">
  <img src="ailearnlog.jpg" alt="AI Learnlog" width="830">
</a>

Or read it on [ailearnlog.com](https://ailearnlog.com/).

## Use From Claude Code

Copy the [.claude/commands/ask-portfolio.md](.claude/commands/ask-portfolio.md) command into any IDE project.

Then try:

```bash
/ask-portfolio "Provide a portfolio overview, I'm interested in ..."
/ask-portfolio "What's unusual about this product manager?"
/ask-portfolio "What product thinking has she demonstrated?"
/ask-portfolio "Does she think in systems?"
/ask-portfolio "Is she creative"
/ask-portfolio "Can she do data analysis?"
```

Direct: *"Launch parallel agents to deeply analyse this entire portfolio to extract insights about the author. What are her innate skills? `@portfolio/INDEX.xml`"*

## Use From A Normal AI Chat

Copy and paste into claude.ai, Grok, etc:

```markdown
Analyse this portfolio index: `https://raw.githubusercontent.com/michellepace/craft-me-public/refs/heads/main/portfolio/INDEX.xml`

Create overview: "At a Glance", "Thematic Analysis", "3 Standout Pieces", "What stands out about this product manager". Appendix: "Title | Raw GitHub URL | Ask About". Use Tables, Emojis.

Remind me I must provide URLs before you’ll fetch and analyse further!
```

## Repo Structure

An indexed directory of portfolio entries — articles or projects, some with repos.

```text
portfolio/
├──── INDEX.xml       # Ask Claude questions against here
├──── website/        # Write-ups from ailearnlog.com
│     ├── file1.md
│     ├── file2.md
│     └── ...
└──── repos/          # Write-ups about repos (coming later)
```

Example portfolio entry in the [INDEX.xml](portfolio/INDEX.xml):

```xml
<portfolio_entries>
  <entry>
    <type>article | project</type>
    <title>title</title>
    <summary>[semantic summary for AI to search]</summary>
    <website_writeup>[file.md]</website_writeup>
    <website_url>https://ailearnlog.../</website_url>
    <repo_writeup>[coming later]</repo_writeup>
    <repo_url>https://github.com/michellepace/...</repo_url>
    <published>yyyy-mm-dd</published>
  </entry>
</portfolio_entries>
```

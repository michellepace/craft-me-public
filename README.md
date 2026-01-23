<!-- This README is for the public repo (craft-me-public). Synced via /sync-to-craft-me-public -->

# Chat with My Portfolio

Use AI to chat with my portfolio (a collection of articles and projects).

<a href="https://ailearnlog.com/" target="_blank">
  <img src="ailearnlog.jpg" alt="AI Learnlog" width="830">
</a>

Or read it on [ailearnlog.com](https://ailearnlog.com/).

## Use From Claude Code

Step 1: Clone this repo:

```bash
git clone https://github.com/michellepace/craft-me-public.git michelles-articles-projects
```

Step 2: Ask Claude Code anything, for example:

```bash
/ask-portfolio "Provide a portfolio overview, I'm interested in ..."
/ask-portfolio "What's unusual about this product manager?"
/ask-portfolio "What product thinking has she demonstrated?"
/ask-portfolio "Does she think in systems?"
/ask-portfolio "Is she creative?"
/ask-portfolio "Can she do data analysis?"

/ask-portfolio "Launch 6 parallel agents to deeply analyse this entire portfolio to extract insights about Michelle. What are her innate skills? Format: Well-structured, emojis, narrow tables."
```

*🤔 **Prefer not to clone?** Copy the [.claude/commands/ask-portfolio.md](.claude/commands/ask-portfolio.md) command into any VSCode/Cursor project and run (uses webfetch).*

## Use From A "Normal AI Chat"

Copy and paste into claude.ai, grok.com, etc.:

```markdown
Analyse collection of AI articles/projects: `https://raw.githubusercontent.com/michellepace/craft-me-public/refs/heads/main/portfolio/INDEX.xml`

CREATE: "Major Themes", "3 Standout Pieces", "Summary", References "Title | `website_writeup` as full raw URL". Two questions (AI skills, Product skills) to research about this person with 2+ relevant `website_writeup`. 

FORMAT: well-structured, emojis, 2 markdown code blocks for questions.
```

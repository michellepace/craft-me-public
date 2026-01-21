# [Repo Name]

> **Instructions for Claude Code**: Populate this template by exploring the repository. Look in the locations suggested. Be honest about what exists and what's missing. Assess quality, don't just list.

**Purpose:** [One sentence — what problem does this solve?]

**Repository:** [GitHub URL]

## Tech Stack

> Look in: `package.json`, `pyproject.toml`, `Cargo.toml`, or equivalent

- **Language/Runtime:** [e.g., Python 3.13, Node 22, TypeScript 5.x]
- **Framework:** [e.g., Next.js 16, FastAPI, none]
- **Package Manager:** [e.g., UV, npm, pnpm]
- **Key Dependencies:** [Only substantive ones — not utilities]

## Developer Workflow

> Look in: `.pre-commit-config.yaml`, `lefthook.yml`, `.github/workflows/`, `Makefile`, scripts in package.json/pyproject.toml

| Aspect | Setup | Notes |
|--------|-------|-------|
| **Linting** | [Tool + strictness] | [e.g., Ruff with ALL rules, Biome] |
| **Formatting** | [Tool] | [e.g., Ruff, Prettier, Biome] |
| **Type Checking** | [Tool + mode] | [e.g., Pyright strict, TypeScript strict] |
| **Pre-commit Hooks** | [What runs] | [e.g., lint, format, test] |
| **CI/CD** | [What's automated] | [e.g., PR checks, deploy previews] |

**Key Commands:**

```bash
# [List the main dev commands from scripts/Makefile]
```

## Claude Code Setup

> Look in: `.claude/`, `CLAUDE.md`, `.mcp.json`

- **CLAUDE.md:** [Does it exist? What guidance does it provide?]
- **Slash Commands:** [List any in `.claude/commands/`]
- **MCP Servers:** [List any configured in `.mcp.json`]
- **Permissions:** [Notable allows/denies in `.claude/settings.json`]

## Architecture

> Look at: folder structure, entry points, data flow patterns

```
[ASCII representation of key folders/files]
```

**Patterns Used:** [e.g., App Router, frozen dataclasses, layered architecture]

**Data Flow:** [Brief description of how data moves through the system]

## Testing Strategy

> Look in: test folders, pytest markers, playwright config, coverage reports

- **Test Types:** [unit, integration, e2e — what exists?]
- **Coverage:** [If measurable, state it; otherwise note if comprehensive or sparse]
- **Test-to-Code Ratio:** [Rough assessment]
- **What's Well-Tested:** [Specific areas]
- **What's Not Tested:** [Gaps]

## What's Remarkable

> Assess: What would impress a hiring manager reviewing this repo? What shows craft?

1. [Specific thing with evidence]
2. [Specific thing with evidence]
3. [Specific thing with evidence]

## What Could Be Better

> Assess: Be honest. What's incomplete, missing, or could be improved?

1. [Gap or limitation]
2. [Gap or limitation]
3. [Gap or limitation]

## PM-Relevant Signals

> Synthesise: What does this repo demonstrate about the author's product/technical thinking?

- **Trade-off Awareness:** [Evidence of deliberate choices]
- **Quality Mindset:** [Evidence of testing, linting, documentation]
- **Developer Experience:** [Evidence of thinking about future maintainers]
- **Systems Thinking:** [Evidence of understanding how pieces connect]

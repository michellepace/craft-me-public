# Into Claude Code from Replit and Loveable

**Target Audience:** Non-engineers vibing in tools like v0, Replit, etc. and are wondering about Claude Code

**What you need:** A claude.ai pro account, VSCode (free) or Cursor, Patience to start small

**Where to focus:** Your CLAUDE.md file, A good `spec.md` / `prd.md`, Plan mode saved to `plan.md`

---

This quick start lays out the steps and references to get going with Claude Code.

I came from prototyping and building apps in v0 and Replit. Your reasons for wanting to try Claude Code may be similar to mine:

- **Your Apps are growing**: your code base is getting bigger and debugging more frequent
- **One place:** to plan and track your project in full context of the code (`Plan mode`)
- **LLM Knowledge:** your stack is newer; you need more than a custom instruction (`CLAUDE.md`)
- **Chat with GitHub**: you'd love to be able to say "Claude Code, show me the last 5 commits"
- **You want to know**: you can change the way teams work, you want to *feel* it for yourself

You might think Claude Code is too hardcore for you—so did I. Surprisingly I find it easier than Cursor and the simplicity of working in a terminal wonderful. I did not expect either.

Generating code and slot machines are a lot of fun. With Claude Code, you will need a bit of patience to find your workflow and tweak your `CLAUDE.md` file as you go along. So patience to learn to stack the odds heavily into your favour. It works.

**Claude Code is free** with a [claude.ai Pro](https://www.anthropic.com/pricing) account. Otherwise, leave ChatGPT and come over to the excellent Anthropic at $20/month. To increase your usage and access Opus you will need to upgrade. For me it is fine as it is.

## If you don't understand your tech stack

I could make Next.js apps in v0 without knowing much at all. If you want to move faster with Claude Code, slow down first. Learn how the code works and fits together, not so much the syntax. You will learn to instruct Claude Code more effectively.

To do this, I did two Next.js follow-along projects on YouTube in VSCode without AI. Yes, it was painful. Here is a collection of [Next.js projects](https://youtube.com/playlist?list=PLwsjfz99OaPGg2Kh_lwbXrtj8bZe6loPQ&si=OoTEdkkvawqy7E45) [^1] if your stack aligns to mine (see [Appendix](#appendix)). If you haven't used VSCode, you'll learn as you follow along (ask Claude if you get stuck).

A boring investment that pays off greatly.

## Get Going: Claude Code QuickStart

This is what I did, and assuming you are past the above, a simple plan that works:

**Setup:**

- **IDE**: The obvious choices are [VSCode](https://code.visualstudio.com/) (free) or [Cursor](https://cursor.com/) if you have it already
- **Subscribe**: To [claude.ai Pro](https://www.anthropic.com/pricing) for $20/month to get Claude Code for free
- **Prompt Improver**: You get access with your subscription (more on that later)

**Claude Code, it's not difficult - it's wonderful:**

1. **Watch the workflow:** Watch this 77-minute [Claude Code Project](https://youtu.be/FNpQawHnIrI) [^2] (ignore the stack). Ask questions by uploading the [XML transcript](https://drive.google.com/file/d/1nC3pwGauX2ScAF7NhH8hY5BhuQjmUxAz/view?usp=drive_link) to a Claude chat. Ignore any download warnings or copy/paste to Notepad
2. **Install Claude Code:** Follow the [Claude Code Setup](https://docs.anthropic.com/en/docs/claude-code/setup) [^3] docs. Windows users need WSL. If stuck, reference the docs in a Claude chat, then install the [Claude Code IDE Extension](https://docs.anthropic.com/en/docs/claude-code/ide-integrations) [^4]
3. **Read this well**: [Claude Code: Best Practices for Agentic Coding](https://www.anthropic.com/engineering/claude-code-best-practices) [^5] (twice)
4. **Build an App**: Go back to Step 1 and either build what the demo showed (but in your own stack) or create a simple ToDo list app. Use the transcript in chat to ask questions and generate the PRD retrospectively.
5. **Mimick the masters**: Watch this by Anthropic and try in your app [Mastering Claude Code in 30 minutes](https://www.youtube.com/live/6eBSHbLKuN0?si=L1CBucQ96wrEIXBz) [^6]
6. **Try More:** examples of issuing clear instructions for [Common Workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows) [^7]

**Optional:** If you are using VSCode, having an extension like [Continue.dev](https://www.continue.dev/) (or Cline) comes in very handy. Free to use, but you need to create an [Anthropic API key](https://console.anthropic.com/settings/keys). This will also help with better auto-completion. You can also use your API key in Claude Code itself, I've heard it's expensive. When I hit my usage limits, I just think or do something else.

![Claude.ai conversation generating an ASCII workflow diagram from a YouTube transcript, illustrating the iterative Claude Code development process: requirements → CLAUDE.md initialisation → plan mode → development loop (code, review, test, commit) → production deployment](https://ailearnlog.com/wp-content/uploads/2025/07/claudecode-flow.jpg)

*Image 1: Upload the YouTube transcript to a chat to ask questions*

**My CLAUDE.md (lots of effort) and other docs:**

- **Initialise `CLAUDE.md`**: I use just one `CLAUDE.md` file. To bootstrap your first version → open project in your IDE → Ask Claude Code "tell me all about this project" → then run `/init`
- **Start small, incrementally add** (and delete): Every time I add a rule / example / best practice to `CLAUDE.md`, I make myself test it. If I can't think how, I ask Claude Code "what could you do in order to test that my new rule xyz works, and what should we check?" This painful but worth it:

> A common mistake is adding extensive content without iterating on its effectiveness. Take time to experiment and determine what produces the best instruction following from the model. [Anthropic Best Practices]

- **Chat with your stack**: I use [DeepWiki](https://deepwiki.org/) [^8] to find changes in my stack that postdate Claude 4 knowledge cutoff (Dec 2024). I add the needed info / examples into CLAUDE.md (eg Tailwind 4!)
- **Prompt Improver**: If I need stricter compliance, I put the `CLAUDE.md` file into Anthropic's [prompt improver](https://console.anthropic.com/dashboard). It is a powerful tool (I use it for everything). Click the "Generate" button and paste in.
- **Product PRD**: I still make a `docs/prd.md`. I refer to it when Claude Code has implemented a plan and I need to give direction for the next plan.
- **Save the Plan**: Like the workflow video, I get Claude in Plan mode (shift +tab) to write to my `docs/plan.md`.

I have bookmarked these articles to read later:
[Basic Claude Code | Harper Reed](https://harper.blog/2025/05/08/basic-claude-code/) and
[How to Master Claude Code MD Files | Daniel Lynch](https://empathyfirstmedia.com/claude-md-file-claude-code/)

## Claude Code and GitHub

Claude knows how to use the `gh` command line interface (CLI) to interact with GitHub for creating issues, opening pull requests, reading comments, and more. You can also use GitHub actions via `/install-github-app`. With this you can tag Claude from GitHub with "@claude" - see the [GitHub Actions docs](https://docs.anthropic.com/en/docs/claude-code/github-actions). For myself I only use `gh`, creating branches is fancy enough for me. Finally, Claude Code can also use GitHub API or MCP server. I *think* this when you want to do advanced analysis and/or other fancy things.

## What's Next — MCP

I have a constant feeling of being behind "everyone else." I have not used Claude Code with any MCP's yet. Here are the [docs](https://docs.anthropic.com/en/docs/claude-code/mcp) in case you are ahead of me. The first MCP servers I am going to try are:

1. [Context 7: Up-to-date docs for LLMs](https://upstash.com/blog/context7-llmtxt-cursor)
2. [Puppeteer](https://mcp.so/server/puppeteer) - for iterating on mocks as mentioned at this Anthropic presentation, [11:00](https://www.youtube.com/live/6eBSHbLKuN0?si=zn8Xjg49E0AzHM_K&t=660) and [25:15](https://www.youtube.com/live/6eBSHbLKuN0?si=8XztvQVGcHc8A8Tl&t=1515).
3. [Ask-Human](https://masonyarbrough.com/blog/ask-human) - A bit unsure, but looks interesting (mentioned by [O'Reilly Tech Radar July 2025](https://www.oreilly.com/radar/radar-trends-to-watch-july-2025/))

I hope you have found confidence here — Claude Code is wonderful.

## Appendix

### My Next.js Tech Stack

This is the tech stack I focus on. Take a peek in your `packages.json` file of your last v0 or Replit app to get an idea of what you've been using. If the explanations don't make sense below, see this great article [^9]

**THE FOUNDATION: CORE TECHNOLOGIES**

| Technology | Description |
| :-- | :-- |
| [Next.js 15.x](https://nextjs.org/docs/app/getting-started/installation#automatic-installation) | React framework for building full-stack web applications • With: App Router to provide simplified routing with better performance and server-side rendering |
| [TypeScript](https://www.typescriptlang.org/) | Adds type safety to JavaScript for catching errors during development • Provides better code completion and refactoring in your editor |
| [Tailwind CSS 4.x](https://tailwindcss.com/docs/styling-with-utility-classes) | Style your UI with utility classes for typography, spacing, layout, etc. • E.g., `text-lg font-bold` (typography), `p-4` (padding) • v4 simplifies theming and removes `tailwind.config.ts` |
| [Shadcn/ui](https://ui.shadcn.com/docs/components) | Pre-built customisable UI components styled with Tailwind out of the box. • E.g., Button, Alert, Chart, Accordion, Date Picker, Sonner, etc. • Latest version styled with Tailwind 4. |

*Table 1: Next.js installation provides options for App Router, TypeScript, Tailwind CSS, and ESLint*

**PLUS MORE**

| Technology | Description |
| :-- | :-- |
| [Clerk](https://clerk.com/) Authentication | User auth with login, signup, and profile management - includes social auth (Google, etc.). • Now includes complete billing for B2C and B2B subscriptions. |
| [Zustand](https://zustand.docs.pmnd.rs/getting-started/introduction) State Management | Manage application state (user data, UI state, etc.) • Simpler alternative to Redux with better performance • I use as a "pre-step" to store data before using a DB • Think "smart local storage" |
| [Drizzle](https://orm.drizzle.team/) or [Prisma](https://www.prisma.io/) ORM | Maps database tables to TypeScript objects for type-safe data operations • Drizzle: feels like SQL • Prisma: more abstracted with extra features |
| [Supabase](https://supabase.com/) or [Neon](https://neon.com/) SQL Database | Cloud databases for your app's data • Supabase: Full backend (db, auth, file storage, edge functions, auto-generated APIs) • Neon: Focuses on being a database with instant scaling and branching (like Git for your data) |
| [React Hook Form](https://react-hook-form.com/) + [Zod](https://zod.dev/) Forms | Build forms with validation that catches errors as you type • RHF: Handles form state, submission, and error tracking • Zod: Validates data (email format, required fields, etc.) with TypeScript • Work together via `zodResolver`, see [shadcn guide](https://ui.shadcn.com/docs/components/form) |

*Table 2: Additional tech stack items I install in my Next.js apps (not exhaustive: changes from app to app)*

---

#### Main Resources Mentioned

[^1]: [Next.js follow-along projects playlist](https://youtube.com/playlist?list=PLwsjfz99OaPGg2Kh_lwbXrtj8bZe6loPQ&si=OoTEdkkvawqy7E45)
[^2]: [Build Flutter Apps FASTER with Claude Code | YouTube](https://youtu.be/FNpQawHnIrI)
[^3]: [Claude Code Setup | Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/setup)
[^4]: [Claude Code IDE Extension | Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)
[^5]: [Claude Code: Best Practices for Agentic Coding | Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices)
[^6]: [Mastering Claude Code in 30 minutes | Anthropic YouTube](https://www.youtube.com/live/6eBSHbLKuN0?si=L1CBucQ96wrEIXBz)
[^7]: [Common Workflows | Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/common-workflows)
[^8]: [DeepWiki - AI Documentation You Can Talk To](https://deepwiki.org/)
[^9]: See the appendix tables for technology explanations

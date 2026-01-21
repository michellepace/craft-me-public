# Personal Tutor Follow Along: Claude Code and Python

**Target Audience:** Non-technical people wanting to experience Claude Code and Python

**Tools:** Claude Code, VSCode, Python, Jupyter Notebooks, UV, (Anthropic subscription)

**End Result:** VSCode properly setup for Python with Claude Code working in a project.

---

If you want to experience Claude Code but have no programming experience then this article is for you. Each claude.ai conversation is listed for you to replicate so that you can have your own 24/7 coach.

You will start at installing VSCode. Then setup source control, create a Python project with a Jupyter notebook (using UV), automated code quality checks, and finally Claude Code and the imperative CLADUE.md file.

It is not a "just set it up and don't think" article. By replicating each chat and my instructions within it, you'll learn the imperative basics. All you need to be able to do is read, try, fail, think, and ask again.

These steps are written for Mac users. If you're on Windows, you'll need to do a **Step 1.5**. Don't let this discourage you – I tried Claude Code on Windows, and it works better on Linux (via WSL). I had this confirmed one degree away from Anthropic engineers too.

## Create your claude.ai project

Create a [claude.ai Project](https://claude.ai/projects) with a nice name 🐞 and set the project instruction:

![Claude.ai Projects interface with numbered annotations: (1) project titled "Mac VSCode UV + CC" containing six sequential conversations for VSCode and Python setup, from "Install VSCode" through "Claude Code: Install and Simple Usage"; (2) custom system instruction panel configuring Claude as a software engineer coach specialising in VSCode, Git, UV, and Claude Code.](https://ailearnlog.com/wp-content/uploads/2025/08/setup-claudeai-project-with-instruction.webp)

*Claude.ai Project with instruction set and the conversations to recreate for your own 24/7 coach*

Then set this as the project instruction and refine later as desired:

```text
You are a software engineer coach for intelligent adult beginners.

You specialise in:
- VSCode on Mac
- Git and GitHub for source control
- Python with UV Package and Project Manager (never pip or requirements.txt)
- Claude Code AI agent in VSCode terminal

When researching or uncertain, prioritise official sources and recent 2025 documentation.

Example key sources include:
- Claude Code: https://docs.anthropic.com/en/docs/claude-code/overview
- UV: https://docs.astral.sh/uv/
- UV with Jupyter: https://docs.astral.sh/uv/guides/integration/jupyter/
- VSCode: https://code.visualstudio.com/docs

Provide clear, well-formatted explanations with helpful emojis are great!
Use tables when they aid understanding and for "information at a glance" (use emojis).
```

## Recreate Conversations Incrementally

Mimic each conversation incrementally into your own project. Copy the first instruction → paste it into a chat. Follow Claude's response before moving on in case you have questions or problems.

| No | Conversation Name (and summary) | Conversation to Mimic |
| :-- | :-- | :-- |
| 1 | **Step 1: Install VSCode** Install VSCode, a code editor where you'll write Python and use Claude Code to help you program. | <https://claude.ai/share/21c8e6c0-4b16-4222-9645-3d900e13eff5> |
| 2 | **Step 2: Create GitHub account** Create your GitHub account and first repository to store and share your code online. Can be public or private. | <https://claude.ai/share/e4007e88-07d3-48a5-bde5-6b0796dcae7b> |
| 3 | **Step 3: Install Git and configure** Configure Git with your identity and cross-platform settings. This links to your GitHub for source control. | <https://claude.ai/share/803c1196-22a5-4f04-9d3a-fd179be92c49> |
| 4 | **Step 4: Create Projects directory (+oh-my-zsh)** Set up project folders and enhance your terminal with visual features that makes writing commands easier. | <https://claude.ai/chat/85c8765d-c5f6-4c96-b325-e30629d0b531> |
| 5 | **Step 5: UV +Project +GitHub +Notebook** Create a project. Install UV and configure VSCode with extensions and settings for all projects. Create a Jupyter notebook then put it into GitHub. | <https://claude.ai/share/bfe07f09-c0d4-4525-bb4f-8dc2510463ec> |
| 6 | **Step 6: Claude Code: Install and Simple Usage** Install, understand CLAUDE.md, get it to do Git, automate code quality checks, detailed research about Claude Code. A non-coding use case "BMAD" repo. | <https://claude.ai/share/273ecb8e-677e-4a06-a080-49884268ecc6> |
| *1.5* | ***Step 1.5: Windows Users - Required*** *To follow these steps you need to install WSL for Windows. Once done continue to **Step 2** above.* | *<https://claude.ai/share/98fdbd80-11d8-49ec-9bdd-09c529849b27>* |

*Recreate conversations incrementally: copy my first instruction → do what Claude says → continue.*

Notes:

- **Which claude.ai model?** Use Opus 4.1 for responses to align closer to mine (otherwise Sonnet 4)
- **Tip for line breaks**: If you lose the line breaks when pasting: Copy my instruction → paste into VSCode "temp.md" file → copy and paste into claude.ai
- **Why not ask Claude Code?** Many of these instructions could be done with Claude Code. But for easy reference later and a smoother learning journey, start with this well organised project.

You will hit bumps as you complete these steps. Detail what you did, the problem, and ask it to ask you for additional helpful information (like commands to run) to help investigate the problem. The greater significance of this article is learning how to collaborate with Claude on almost anything.

**Ordered Achievements Across All 6 Conversations**

✅ Installed **VSCode** on Mac
✅ Created **GitHub** account
✅ Configured **Git** with name and email
✅ Created **~/projects/** directory structure
✅ Installed **Oh My Zsh**
✅ Customised **zsh** prompt for better readability
✅ Installed **UV** package manager
✅ Created UV project **~/projects/python/my-python-project**
✅ Installed **VSCode extensions** (Microsoft Python, Jupyter, Ruff)
✅ Configured **VSCode settings.json** for UV + formatting
✅ Pushed project to GitHub
✅ Enabled **Jupyter** notebooks with **uv add --dev ipykernel**
✅ Created **demo_notebook.ipynb** → pushed to GitHub
✅ Installed **Node.js 18+** (Claude Code prerequisite)
✅ Installed Claude Code via **npm i -g @anthropic-ai/claude-code**
✅ Initialised Claude Code project with **/init** → created **CLAUDE.md**
✅ Installed **Ruff** with uv **add --dev ruff**
✅ Installed **pre-commit** with **uv add --dev pre-commit**
✅ Created **.pre-commit-config.yaml** with UV sync + Ruff hooks
✅ Installed pre-commit hooks with **uv run pre-commit install**
✅ **Updated CLAUDE.md** with UV-specific workflows & commands
✅ **Tested changes made to CLAUDE.md** with /clear verification

Great progress across all 6 conversations - everything completed! 🎉

## Where to Next?

Wherever you want. But here are some sequenced ideas.

| Sequence | Side Stepping Rabbit Holes with Sequence |
| :-- | :-- |
| A | Build an app with Claude Code (30m) follow along. Here is one using [Flutter](https://youtu.be/wMSIE8SF0xQ) and using [Next.js](https://youtu.be/cYIxhL6pxL4). The first is very good, I went on to build a "to-do app" in Next.js. The tech stack is inconsequential for now; it is finding your workflow and trying it. |
| B | Read this and write notes <https://www.anthropic.com/engineering/claude-code-best-practices> |
| C | Do an Anthropic tutorial in Jupyter notebook <https://github.com/anthropics/courses>. Either create a clone of your "my-python-project" and copy the Notebooks in manually. Or clone. |
| D | Watch "Mastering Claude Code in 30-minutes" by person who invented it and take notes <https://www.youtube.com/live/6eBSHbLKuN0> |
| E | Establish your Claude Code workflow: Build something really simple in Python and then a bit more complex. Here are mine [text-analyser](https://github.com/michellepace/text-analyser) and [youtube-to-xml](https://github.com/michellepace/youtube-to-xml). |
| F | Do an in-depth course on getting up to speed on Claude Code (free) <https://anthropic.skilljar.com/claude-code-in-action> and use Anthropic [learning resources](https://www.anthropic.com/learn/build-with-claude) after. |
| G | Watch "Advanced Claude Code" to understand context <https://youtu.be/JU8BwMe_BWg> and try mentioned tools [claude-code-docs](https://github.com/ericbuess/claude-code-docs) and [claude-code-project-index](https://github.com/ericbuess/claude-code-project-index) |
| H | Build a Next.js app with Claude Code. I [followed a YouTube tutorial](https://www.youtube.com/playlist?list=PLwsjfz99OaPGg2Kh_lwbXrtj8bZe6loPQ) to build a project manually and read [these docs](https://nextjs.org/docs/app/getting-started) once, then rebuilt everything with Claude Code. I used my [youtube-to-xml repo](https://github.com/michellepace/youtube-to-xml) for a claude.ai tutor and had Claude Code reverse engineer the SPEC.md. |
| I | Read how Claude Code works to use it better <https://minusx.ai/blog/decoding-claude-code/> |
| J | Read why not to go MCP bananas (context) <https://ghuntley.com/allocations/> and how to [Manage Your MCPs Nicely](https://github.com/michellepace/youtube-to-xml/blob/main/docs/knowledge/manage-mcps-nicely.md) (in Claude Code) |
| K | Read free chapters 1-3 of [AI Engineering](https://a.co/d/c04wxqU) to understand LLM fundamentals. This foundation dramatically improves your effectiveness with all AI tools. It really is very beneficial. |

*Sequenced ideas for an A-K rail to hold.*

I code to streamline my work, and I like building for fun. I jumped onto Claude Code for the untapped potential of non-coding use cases. Such as the [Anthropic growth marketing team](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code). Having worked across disciplines and industries, the potential is enormous. Getting the basics above, you will start to see it.

## Aside: Be Mad and Try It

The [BMAD repo](https://github.com/bmad-code-org/BMAD-METHOD) has a collection of interactive prompt templates to produce markdown documentation. These ultimately drive AI development. That is, it's a streamlined approach with disparate humans in the loop using any information (e.g., masses of customer feedback). You can alter it to run in Claude Code.

![Structured analysis of the BMAD methodology showing two agent categories: Planning Phase Agents (Analyst, PM, Architect, UX Expert, Product Owner) for web-based documentation, and Development Phase Agents (Scrum Master, Developer, QA) for IDE-based implementation. Each agent maps to specific prompt files (e.g., analyst.md, prd-template.md) that produce defined outputs like Project Briefs and Architecture Documents.](https://ailearnlog.com/wp-content/uploads/2025/08/pic_bmad_repo.webp)

*Analysis of BMAD repo in claude.ai to understand agents and prompts available*

## ♥️ Claude Code — Not Just Code

Claude Code has unbridled possibility beyond coding, in addition to the "BMAD" methodology. For instance, you could get it to scrape websites (e.g. with [FireCrawl](https://www.firecrawl.dev/) MCP), download YouTube transcripts, etc. and synthesise to your research delight. Add in customer data and extract insights. Push it through to your product workflows. It is limited to your imagination. If you want a beautiful experience Claude Code experience but not in an IDE, try <https://bearclaude.specstory.com> (currently free at writing):

![BearClaude application with split-pane layout: left panel shows a markdown document about "mindful making in the age of AI" with rich text formatting toolbar; right panel displays Claude Code Terminal with welcome message, getting started tips, and command prompt. The tool positions itself for "upstream work of planning, reasoning, and structuring" before implementation.](https://ailearnlog.com/wp-content/uploads/2025/08/bearclaudeeditor.webp)

*BearClaude for a clean experience with Claude Code without an IDE.*

Good luck.

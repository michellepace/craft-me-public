# YouTube Transcript to XML • Step 1 of 3

**Tools:** Claude Code, Python, yt-dlp

**Technique:** 100% generated using test-driven development and context management

**Solution:** GitHub [youtube-to-xml](https://github.com/michellepace/youtube-to-xml)

This command-line tool converts transcripts to structured XML with automatic chapter detection, accepting either YouTube URLs or text files. The structured format with organised chapters is hypothesised to improve LLM comprehension - **evaluations pending**.

---

## The Problem

I watch a lot of YouTube educational content, some up to 11 hours long. I try my best to organise these into playlists, but I forget what I've put where, and the commonality across topics. Then I keep dropping these video URLs into Google Notebook LM to ask questions. But I don't like it well enough to pay for it, so I lose these conversations anyway. Neither can I "cross-chat" across multiple videos.

This CLI tool is the foundation for a larger project: a Next.js app for chatting with YouTube playlists and cross-referencing ideas across multiple videos. The development path: build reliable transcript extraction (this CLI), evaluate which format works best for LLM comprehension (plain text vs XML), then wrap this tool as a Python API service (using the optimal format) that the Next.js frontend calls. The clean architecture and exception design already anticipate this evolution to an API.

## What This Tool Does

Imagine working through a 11-hour YouTube tutorial with 40,000 lines of transcript. You would have to scroll on YouTube and manually copy everything just to upload it into claude.ai chat.

Not anymore. For demonstration, I'll convert [this](https://www.youtube.com/watch?v=Q4gsvJvRjCU) 2-minute video:

```bash
$ youtube-to-xml https://youtu.be/Q4gsvJvRjCU   # Run the tool

🚀 Processing: https://www.youtube.com/watch?v=Q4gsvJvRjCU
✅ Created: how-claude-code-hooks-save-me-hours-daily.xml
```

So whilst you would see this on YouTube:

![Hand-annotated YouTube page identifying the raw data extracted by youtube-to-xml: chapter titles ("Intro", "Hooks"), timestamped transcript lines with text, video title, and publication date—each element maps directly to XML output attributes](https://ailearnlog.com/wp-content/uploads/2025/09/youtube-video-terminology-grey.webp)

*Screenshot of YouTube video webpage with common terminology explained*

Now you have the entire transcript in one `.xml` file with chapters:

```xml
<transcript video_title="How Claude Code Hooks Save Me HOURS Daily"
            video_published="2025-07-12" video_duration="2m 43s"
            video_url="https://www.youtube.com/watch?v=Q4gsvJvRjCU">
  <chapters>
    <chapter title="Intro" start_time="0:00">
      0:00
      Hooks are hands down one of the best
      0:02
      features in Claude Code and for some
      <!-- ... more transcript content ... -->
    </chapter>
    <chapter title="Hooks" start_time="0:19">
      0:20
      To create your first hook, use the hooks
      <!-- ... more transcript content ... -->
    </chapter>
    <!-- ... 2 more chapters ... -->
  </chapters>
</transcript>
```

Which means now you could upload [how-claude-code-hooks-save-me-hours-daily.xml](https://github.com/michellepace/youtube-to-xml/blob/main/example_transcripts/how-claude-code-hooks-save-me-hours-daily.xml) to your AI Chat and have a conversation with your YouTube video. Testing whether this truly performs better than plain text is the next step in this greater project.

## Architecting with Grok and Claude Code

I am unsure what "good system design" in engineering really is, but I like simplicity and elegance. Grok voice was instrumental in helping me think the design through:

[Video](https://youtu.be/-ZS9NmYq5To)

The solution is designed like this - and I really like it:

![Hand-drawn architecture diagram with annotations: single CLI entry point auto-detects input type, branches to url_parser.py (yt-dlp API, JSON parsing, metadata) or file_parser.py (pattern matching, chapter rules), both converge at models.py (TranscriptDoc, Chapters, Metadata), then xml_builder.py produces the final XML—demonstrating separation of concerns and API-ready design](https://ailearnlog.com/wp-content/uploads/2025/09/youtube-architecture.webp)

*Architecture designed in collaboration with Grok and Claude Code: dual-input convergence*

This design evolved through test-driven development with high test coverage. I actually have more test code than source code:

![Stacked area chart of youtube-to-xml repository growth over 250 commits: test code (blue) consistently exceeds source code (red) throughout development, reaching approximately 2000 vs 1000 lines respectively by project completion—quantitative evidence of test-first methodology](https://ailearnlog.com/wp-content/uploads/2025/09/repo_evolution_commit.webp)

*Test code (blue) dominates at 60% - disciplined TDD in practice*

Finally, the file-based method: This was the first method I implemented before discovering yt-dlp could download directly from YouTube. It works perfectly, just now more of a fallback when YouTube applies rate limiting.

## Next Steps — Evaluation

Next, I'll build a rudimentary Shiny for Python webapp for blind test exploration, data analysis, and automated evals. I will likely approach it with Six Sigma methods, see [idea-evals.md](https://github.com/michellepace/youtube-to-xml/blob/main/docs/idea-evals.md). Once I have a strong indication of which format is best to use over multiple video durations, I will be ready to move onto building the Next.js app. Possibly try RAG too in order to reduce costs. This should be quite easy as by this stage I'll have an automated evaluation test suite.

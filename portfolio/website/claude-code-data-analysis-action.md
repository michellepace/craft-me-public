# Claude Code in Data Analysis Action

**Target Audience:** Anyone wanting to see Claude Code in action

**Claude Code Key Points:**

- Can analyse data anomalies
- Writes code on its own to investigate
- Self-adjusts direction based on findings

**GitHub:** [plot-py-repo](https://github.com/michellepace/plot-py-repo) to count/classify lines of code and visualise repository growth over time.

---

This article tells a story in pictures of working within Claude Code. The simplicity masks the power you have at hand.

I start off with a chart that showed data in a shape I did not expect. I put Claude Code into planning mode to find the root cause. In the end it, it was found and fixed.

Just imagine how many other things Claude Code could investigate, hypothesise, and test.

In this analysis, I use my [plot-py-repo](https://github.com/michellepace/plot-py-repo) tool to analyse my [youtube-to-xml](https://github.com/michellepace/youtube-to-xml) repository.

## The Problem

All the code that I do is 100% written by Claude Code. I wanted to see my repositories over time and what they are comprised of. So, I created a tool to count and classify lines[^1] and visualised my youtube-to-xml repository[^2].

I write a lot of tests, so when I saw a lot of purple, I was pleased. But three peaks in September? No, I don't remember being extraordinarily efficient. But where to start, the source, the transformations, the code?

![Repository growth stacked area chart with test code (purple), docstrings (orange), and source code (green) from August to September 2025, displaying three unexplained 40k+ line spikes that triggered the debugging investigation.](https://ailearnlog.com/wp-content/uploads/2025/10/00-claude-code-debug-chart.png)

*Apparent repository growth over time with three suspicious peaks in September*

## Claude Code Sherlock Holmes — Finding the Root Cause

All of these screenshots are taken from within my codebase that creates these images. Think of each as a page in a storybook of what it's like to work with Claude Code. And here is the first page where I am instructing Claude Code to make a plan:

![Investigation prompt asking Claude Code to determine root cause of chart anomalies, specifying data source truths including the youtube-to-xml repository path, CSV data file location, and Python file filtering rules with numbered question format requested.](https://ailearnlog.com/wp-content/uploads/2025/10/01-claude-code-debug3.png)

*1 of 8: Setting up the investigation in Claude Code's Plan mode*

On the last line of the image 1, I ask Claude Code to ask me questions first. This is for two reasons: first, what is crystal clear in my head is seldom clear in my writing. Second, there are aspects I miss but Claude Code doesn't. Q&A is a good cheat:

![Four diagnostic questions from Claude Code covering repository selection, CSV vs code logic investigation priority, interpretation of the spike-then-drop pattern, and unusual September activity recall, with user's answers selecting CSV analysis and acknowledging uncertainty about the cause.](https://ailearnlog.com/wp-content/uploads/2025/10/B_cc-debug-questions.png)

*2 of 8: Q&A with Claude Code pre-investigation*

With my answers, Claude Code takes a preliminary look around in the files and then crafted the investigation plan:

![Seven-step investigation plan with three phases: CSV data inspection to identify peak files and commits, Git history cross-reference using date-filtered log commands, and code logic verification of Python file filtering and line counting—awaiting user approval with auto-accept option selected.](https://ailearnlog.com/wp-content/uploads/2025/10/C_cc-debug-plan.png)

*3 of 8: Claude Code's proposed plan of attack — approved*

It started executing the plan at speed, a premature celebration followed by a "Wait, this doesn't make sense":

![Investigation breakthrough showing test_xml_builder.py recorded at 6,362 lines on September 20th but currently only 248 lines—a 96% reduction that Claude Code flags as "doesn't make sense," prompting deeper file history analysis.](https://ailearnlog.com/wp-content/uploads/2025/10/04-claude-code-debug_short.png)

*4 of 8: Found a clue, but something doesn't add up.*

Claude Code adjusts and this is what makes it powerful. A minute later the first glimpse of the bug I missed. One which would have taken me far longer to logically realise:

![Bug confirmation at line 50-51: df.groupby incorrectly sums all commits per date rather than taking latest state, with perfect correlation evidence—September 20th had 15 commits producing 42,762 inflated lines, September 25th had 15 commits at 41,335 lines.](https://ailearnlog.com/wp-content/uploads/2025/10/05-claude-code-debug_short.png)

*5 of 8: Root cause identified—commits erroneously summed per day, not latest state.*

And now the full explanation, supporting data, and proposed fix:

![Complete root cause report identifying the groupby sum bug at chart_evolution.py:50-51, evidence table showing 15x inflation (42,762 displayed vs ~2,850 expected for September 20th), and three-step fix to filter for latest commit per date before grouping—user responds with test-driven implementation request.](https://ailearnlog.com/wp-content/uploads/2025/10/06-claude-code-debug_short.png)

*6 of 8: Complete root cause analysis with proposed fix waiting for me to confirm — YES!*

"Ready to fix the bug?" — "accept edits on" — which means Claude Code just goes and nothing needed from me. YES!

## Fixed

And here it is, about 20 seconds later the fixed chart and a completely different story:

![Before/after comparison with hand-drawn annotations: left chart labelled "Wrong" shows erratic 40k spikes from the summation bug, right chart labelled "Right" reveals steady growth to ~3k lines with consistent test/docstring/source code proportions—same underlying data, completely different narrative.](https://ailearnlog.com/wp-content/uploads/2025/10/07-ccdeb-compare_rev4.png)

*8 of 8: Before and after—same data, completely different story*

**A Sneaky Tweak:**

Looking at the fixed "right" chart, I obviously didn't do much August with a big straight flat. Well, I don't want to tell that story. I'll do a sneaky tweak and ask Claude Code to make a new chart on the same data:

![Concise three-line prompt requesting a commit-indexed chart module, paired with the resulting "Repository Growth by Commit" bar chart showing 240 commits with hand-annotated insights—"Backwards compatibility sounds great!" at commit ~140 and "Get it out!!!" near commit 200 marking development milestones.](https://ailearnlog.com/wp-content/uploads/2025/10/cc_final_chart_by_commit_and_promp_820t.png)

*Instructing Claude Code to make one more chart — index by commit, not date — 240 commits in total.*

With clean patterns to follow it is surprising how simple your instructions can be. The chart was created in one go. I went on to get Claude Code to do a "peak analysis" between commits [140,160]. And there was too, the cost of good old backwards compatibility.

And that is the story of how Claude Code investigated a data problem, fixed it, and then made me a new chart so I could tell a better story.

The End.

---

### Footnotes

[^1]: [plot-py-repo](https://github.com/michellepace/plot-py-repo) — line counting and classification tool
[^2]: [youtube-to-xml](https://github.com/michellepace/youtube-to-xml) — repository visualised in this analysis

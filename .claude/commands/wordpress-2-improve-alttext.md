---
description: Improve alt text in WordPress posts for LLM analysis
allowed-tools: Read, Edit, Bash(curl:*)
argument-hint: <portfolio/website/post-name.md>
---

# Improve WordPress Post Alt Text

The author is an AI Product Manager with hands-on technical skills. Potential clients and hiring managers will use AI to analyse the post and draw insights about the author. Alt text quality shapes how you're perceived through AI analysis. Write for LLM comprehension.

## Input

Post: @$1

## Task

For each image in the post:

1. Use Curl to download the image to a `/tmp/` directory
2. Carefully analyse image visually and read the surrounding post context
3. Improve the alt text to better demonstrate what the image shows and how it relates to the post's concepts
4. Remove UI-centric language ("terminal showing", "screenshot of") — focus on what the image demonstrates and coherance
5. Write concise and clear alt text

## Workflow

1. Create a before/after report for all images with 2-sentence assessment of improvement
2. Present the report and ask for confirmation
3. Ask for confirmation to update the file with improved alt text

## Report Format

For each image, show the original alt text, improved version, and brief explanation of why the improvement works better for LLM comprehension and author positioning.

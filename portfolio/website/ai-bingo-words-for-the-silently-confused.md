# AI Bingo Words For the Silently Confused

**Target Audience:** Non-technical readers.

**Includes:**

- Common AI terms explained
- Value creation: ML vs. Gen AI
- By example: ML, Gen AI

Ever silently wonder about the difference between Data Science, AI, Machine Learning, and where Generative AI fits in? Have "foundation models" got you confused?

This article contains a simple visual explanation, a surprising insight about business value, and anecdotal examples of using machine learning and generative AI.

---

The illustration below starts with the most encompassing term 'data science' and flows through machine learning, generative AI, foundation models, to the increasingly popular AI Agents. Follow the numbers and simple explanations to understand what these words mean and how they fit together.

![Author-created educational infographic demystifying AI terminology through a six-step numbered guide. A black nested circle diagram positions AI, Machine Learning, Deep Learning, and Neural Networks in hierarchy, flowing to Foundation Models (LLMs like GPT-3.5, Vision Models like DALL-E, Multi-Modal like Claude Sonnet). Definitions progress from Data Science through traditional ML, Generative AI, fine-tuning, RAG, to AI Agents. A multi-layer neural network diagram illustrates the architecture powering modern AI, showing input-output flow through two hidden layers.](https://ailearnlog.com/wp-content/uploads/2024/05/ai-bingo-words-explained-900px.png)

*Figure 1: Common AI words explained simply, and how they flow and fit together.*

In Figure 1 traditional ML is shown as one small paragraph whereas Gen AI occupies the entire left column. Like current headlines, Gen AI seems to be everywhere. Let's put these two technologies into perspective before moving onto examples.

## AI Opportunity: According to Andrew Ng

You may be surprised to learn that Gen AI does not currently create the most business value. Traditional ML is still abundant with opportunity.

[Andrew Ng](http://andrewng.org) is a highly respected leader in the field of AI, both in traditional ML and Gen AI. Despite my background in traditional ML, watching his Stanford presentation[^1] I was taken aback by his diagram below.

According to Ng's circles, traditional ML still dominates in business value creation. While he predicts higher growth rates for Gen AI through 2026, traditional ML maintains the lead in actual value generated.

![Business value comparison adapted from Andrew Ng's Stanford 2023 data: a large green circle representing Traditional Machine Learning dominates the visual, roughly 20x larger than the small orange Generative AI circle. Outer rings on both circles indicate projected 2026 growth, with Gen AI showing proportionally higher growth rate. This visualisation challenges the prevailing narrative that Gen AI dominates business value creation.](https://ailearnlog.com/wp-content/uploads/2024/05/andrew-ng-dollar-value-ml-genai-pink.png)

*Figure 2: Andrew Ng, Stanford 2023. Value ($) creation comparison of traditional ML vs Gen AI.*

Traditional ML will quietly continue to power many of the systems we use daily. While the scale of Ng's diagram may not be exact, it is a good reminder that "traditional" remains highly relevant with much opportunity.

With AI words explained and traditional ML and Gen AI put into dollar perspective, let's move on to some examples. I have used some of my own experiences in product to make it as real-world as possible.

## Anecdotal Examples: Machine Learning

**When to use**: For making predictions and finding patterns when you have historical data to learn from. Best for specific, repeated tasks where you need consistent results and data backed decisions. Unlike Gen AI, it can't create content or handle open-ended tasks.

1. **Predicting methane levels** in underground coal mines. The ML model was fed sensor readings from over 80 physical sensors like pressure, airflow, sheerer speed etc. The goal was to reduce the risk of a methane explosion.
2. **Detecting cracks in rotating kilns**. The ML model was fed frames of video footage. The goal was to reduce process downtime by detecting small cracks sooner and not relying on human inspection.
3. **Recommending online content,** to compel people to "click". The goal was to lift advertising revenues. A common example but mentioned to emphasise ML is not new—I headed this product over 10-years ago.

## Anecdotal Examples: Generative AI

**When to use**: For creating or transforming content in human-like ways - whether that's text, images, audio, video. Great for creative and open-ended tasks where you need adaptable, context-aware responses. Be cautious using it for critical decisions that need consistent, verifiable logic.

Example 1 shows talks to building a small powered by AI. The subsequent examples focus on leveraging AI in everyday product management to be faster and more creative.

1. **Correcting large research documents** in formal German whilst preserving writing style and content details. Built with the Anthropic API, [full details](https://ailearnlog.com/correcting-large-documents-better-than-microsoft-word/).
2. **Analysing a person via the articles they wrote** using Grok3 to [design a solution](https://jmp.sh/HDmk219y) and then write the prompts to drive Sonnet to create the code in VSCode (see [workflow](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)). Project still in progress (23 Feb).
3. **Creating a website end-to-end** from generating the design and content, language translation, image generation, code generation, and voice dubbing for demo videos. [Delivered website](https://tsv-delphine.de/).
4. **Using AI as a personal tutor** to understand and use a Python data visualisation library called Seaborn. [Full writeup](https://colab.research.google.com/github/michellepace/seaborn-plot-consistency-guide/blob/main/Seaborn_Consistency_Guide.ipynb).
5. **Writing product requirements documents** faster and with AI creativity added, see [ChatPRD](https://www.chatprd.ai/).

## Conclusion

If you made it this far, thank you. I hope you feel a bit more informed. With any new topic the confusion I find is largely due to the number of new words to learn. Pairing this with a few practical examples is a relieving start to a foundational understanding.

If you would like to gain an even deeper understanding, but still in simple words, see this article: **How They Work: ML and GenAI are cousins not brothers**.

### Footnotes

[^1]: Stanford presentation reference.

# Put Aside the Bench for the Mark: Choosing an LLM

**Target Audience:** Product managers

**Key Areas:**

- LLM selection
- Systematic thinking
- Flexible future proofing

**Source Code:** [Python Notebook on Google Colab](https://colab.research.google.com/github/michellepace/anthropic-model-compare/blob/main/Anthropic_Model_Compare_(simple).ipynb)

---

What if the best-performing LLM on paper is not the best for your product? This article introduces a way of thinking about model selection. Through a simple comparison of five Anthropic models, it shows why to not rely solely on benchmarks. You will understand why testing LLMs against your use case is essential. Not only for choosing a model but staying flexible for the future.

## Benchmarks Are General

When you go to any of the popular benchmark leaderboards, it is like looking at a list of "here are the fastest and most capable athletes." But a general athlete is not what you need; your use case needs a swimmer. They must be capable, but in what exactly: technique, resilience under pressure, or something else? They need to be fast too, but in 100m backstroke or getting to the pool? It turns out your use case is for an open water swimmer capable of swimming the English Channel.

This is the essence of why you cannot simply make your choice by popular benchmarks. They rank in general, but your use case is never general.

Below I will setup a fictitious (and overly simple) example of needing to choose between the five Anthropic models. The purpose is to help you establish a fundamental way of thinking about model selection.

## Choosing An Anthropic Model

Assume that for my fictious use case I need to decide between the following five Anthropic models:

![Anthropic's model positioning matrix with Intelligence on the vertical axis and Cost on the horizontal axis. Three model families occupy distinct quadrants: Haiku ("Light & fast") in the lower-left, Sonnet ("Hard-working") in the centre, and Opus ("Powerful") in the upper-right. The five models under evaluation are listed below: Haiku 3 (Mar 2024), Haiku 3.5 (Oct 2024), Sonnet 3.5 (Jun 2024), Sonnet 3.5 (Oct 2024), and Opus 3 (Feb 2024).](https://ailearnlog.com/wp-content/uploads/2025/02/anthropic-families-and-models.png)

*Figure 1: The Anthropic model families and the models I will be testing (blue).*

Looking at the above Sonnet 3.5 seems to be the easiest choice, and I assume the (Oct 2024) snapshot must be even better. The leaderboards point to this too, but is it?

It depends entirely on your use case. The way to test this is by evaluating or "marking" prompt responses. Not just generic prompts but a set of prompts with representative coverage of your use case. The more coverage you have and the more relevant the prompts, the more confident you will be in choosing a model (or validating a move to the latest version/snapshot).

For this article, I will make evaluating my use case (unrealistically) simple by "marking" model responses on just two prompts:

**Speed Test (prompt 1)**
*Explain photosynthesis in a concise paragraph.* (max_tokens: 400)

**Capability Test (prompt 2)**
*What is the geometric monthly fecal coliform mean of a distribution system with the following FC counts: 24, 15, 7, 16, 31 and 23? The result will be inputted into a NPDES DMR, therefore, round to the nearest whole number.*

As LLMs deal in probabilities, the same prompt can have different responses. Model speed can fluctuate too. To address this, I chose to run each prompt 50 times against each model (5 x 2 x 50 = 500 total runs). While 30 (not 50) runs is typically sufficient for statistical significance, I opted for 50 runs as I was unsure of variability.

The results below were gathered from a full test run done on the 4th of February 2025 at 15:02 UTC. The 500 prompts and their responses finished 16 minutes later.

Now for a step through the results (and surprises) for speed, capability, and cost.

### Speed Test Results

Like measuring typing speed in words per minute, model speed is measured in tokens per second. This measures the total time from sending your prompt request until receiving the response – including both the model's "thinking" time (inference) and the internet journey time. This is the speed your product will experience. See [Appendix II](#appendix-ii) for the code snippet used.

Looking at Figure 1 (above), perhaps you are assuming the same as I did. That the Haiku models will be fastest, and that Haiku 3.5 will be faster than Haiku 3.0. As the results will show below, both assumptions turned out to be wrong.

![Speed test results across 50 sequential runs for five Anthropic models, measured in tokens per second. Three stacked panels separate model families: Opus 3 holds steady around 25 tok/s with minimal variance; Haiku 3 fluctuates between 70-115 tok/s while Haiku 3.5 remains flat around 45 tok/s; both Sonnet 3.5 versions cluster between 50-70 tok/s. The data reveals that the older Haiku 3 substantially outperforms its newer 3.5 successor.](https://ailearnlog.com/wp-content/uploads/2025/02/speed_line_fig.webp)

*Figure 2: Haiku 3 is fastest, but Sonnet 3.5 is faster than Haiku 3.5 which is unexpected.*

Figure 2 above shows "speed over time" for the speed test prompt that was sent 50 times to each model, in sequence. The are clear differences in speed despite the fluctuation between runs. Looking at the same in a more comparable format:

![Dot distribution comparing individual speed measurements across five models. Haiku 3 (Mar 2024) achieves the highest speeds at 70-115 tok/s but with substantial scatter. Opus 3 clusters tightly at 20-28 tok/s, demonstrating the most consistent performance. Critically, Haiku 3.5 (40-50 tok/s) performs slower than both Sonnet 3.5 versions (50-70 tok/s)—contradicting Anthropic's positioning of Haiku as the fastest family.](https://ailearnlog.com/wp-content/uploads/2025/02/speed_strip_fig.webp)

*Figure 3: Same data as Figure 2, Haiku 3.5 should be faster than Sonnet 3.5. This is unexpected.*

What is most surprising is that the newer Haiku 3.5 appears to be slower than Sonnet 3.5 (both snapshots). Also, although Opus is an order of magnitude slower its speed is much more stable (notice the differences in vertical spread).

![Statistical summary of speed test results showing Haiku 3 achieving 97.37 median tok/s (the fastest), followed by Sonnet 3.5 Jun (56.16), Sonnet 3.5 Oct (53.98), Haiku 3.5 (46.22), and Opus 3 (25.51). Standard deviation reveals Opus as most stable (1.71) while Haiku 3 shows highest variability (8.30). The test prompt requested a concise paragraph explaining photosynthesis.](https://ailearnlog.com/wp-content/uploads/2025/02/summary_table_speed2.png)

*Figure 4: Summary of speed results using median speed for quick comparison.*

Figure 4 above is a full summary of the speed test results. I chose the median to compare speed because of outliers and being slightly skewed (mean ≠ median). If this were the real world and speed crucial, ensure observed speed differences are statistically significant.

If we were choosing for your swimmer use case, so far Haiku looks the best although its performance is least dependable (look at the spread of the dots in Figure 3 and the standard deviation in Figure 4). And of course, this is only speed, is it capable of swimming the English Channel?

### Capability Test Results

Capability is easy to measure when a definitive response is expected, like a math solution or classification. Typically, you will need to compare textual responses. In this case, there are several methods, both manual and automated, that can be used to evaluate or "mark" textual responses for comparison. In my opinion, the most promising is using an independent LLM to judge the responses; it can be automated and is more consistent than within and between people[^1].

The capability test prompt used (Figure 5 below) has an exact solution of "18". You can see that even for Opus, "the most intelligent model," is not infallible and got 6% of its answers wrong:

![Capability test results for a geometric mean calculation (correct answer: 18). Opus 3 leads at 94% accuracy, but Haiku 3 follows closely at 88%—outperforming all Sonnet models. Sonnet 3.5 Jun achieved 74%, while Haiku 3.5 dropped to 26% and Sonnet 3.5 Oct collapsed to just 8% accuracy. The response distribution shows models splitting between answers 17, 18, and 19, revealing how newer model versions degraded on this specific mathematical task.](https://ailearnlog.com/wp-content/uploads/2025/02/summary_table_capability.png)

*Figure 5: Summary of Capability results and frequency of answers[^2]. Haiku 3 outperforming all but Opus, this is unexpected.*

Like speed, the results for my "use case" contradict the benchmarks. Sonnet should be outperforming Haiku. And like with speed, both Haiku 3.5 and Sonnet 3.5 (Jun 2024) degraded from their predecessors. What does hold true is that Opus did top as most capable, although surprisingly it is Haiku 3 and not Sonnet 3.5 that comes in as close second.

![Ranked accuracy comparison showing Opus 3 at 94%, Haiku 3 at 88%, Sonnet 3.5 Jun at 74%, Haiku 3.5 at 26%, and Sonnet 3.5 Oct at just 8%. The visualisation makes clear that the older, cheaper Haiku 3 outperformed both Sonnet 3.5 versions on this mathematical reasoning task—directly contradicting benchmark-based expectations.](https://ailearnlog.com/wp-content/uploads/2025/01/cap_bar_fig2.webp)

*Figure 6: The older Haiku 3 outperforms Haiku 3.5 and Sonnet 3.5, this is unexpected.*

You can easily imagine that speed tests are affected by the day of the week you run the test on and where you are getting your model served from (e.g., AWS or Anthropic themselves). But if you think you are in clear with capability, I can tell you absolutely no. Please see [Appendix I](#appendix-i). I may have just caught a rare event, but unexplained variation happened to me with this example.

It is now time to look at what appears at first glance to be the easiest of all: comparing costs.

### Cost Calculations

I used to work in manufacturing where products were sold to mines, shipping companies, etc. Buyers unconnected to ground operations would opt for cheaper suppliers. The cheaper products would fail sooner or require more maintenance. The client would suffer far more costly repercussions, but of course invisible in quarterly budgets. Nobody can blame the buyers — everyone likes the look of a low price.

In the LLM world, most providers price models in "cost per token". However, it is more complex than a simple comparison as a token is not standardised. For example, Anthropic may tokenise a given sentence as "12 anthropic tokens", whereas Open AI may tokenize it as "14 open ai tokens".

The trick is to first delve into deeper cost questions before considering quoted prices. For example, do you get accurate responses efficiently or does it require multiple back and forth (more tokens)? For a hosted model, does it get congested and what will this cost your product? Is the API easy and robust to use so your team can move quickly? Is there documentation on prompt engineering practices for the model? Regarding privacy, how much is that going to cost if things go wrong? Once you have considered these deeper costs, only then standardise and compare the easy token costs.

Anthropic prices their models in dollars per million tokens ($/MTOK), with input tokens costing less than output tokens. You can see where this is going: which price is more important to your use case? Is it possible to cache prompts? And if relevant to your use case, how much could you save?

Current[^3] Anthropic pricing:

![Anthropic API pricing as of February 2025 showing dramatic cost differences. Opus 3 commands premium pricing at $15/$75 per million input/output tokens. Sonnet 3.5 versions cost $3/$15. Haiku 3 offers the lowest rates at $0.25/$1.25, while Haiku 3.5 sits at $0.80/$4.00. Output tokens cost 4-5x more than input tokens across all models.](https://ailearnlog.com/wp-content/uploads/2025/02/summary_table_anthropic_costs.png)

*Figure 7: Anthropic model pricing showing cost differences in input/output tokens.*

It cost $0.93 to run the entire test set of 500 prompt requests. In the detailed breakdown below, the speed tests cost more because a "concise paragraph" was asked for. Whereas the capability prompt instructed "respond only with a number".

![Itemised costs for the 500-prompt experiment totalling $0.93. Opus 3 dominated spending at $0.62 (67% of total), while Haiku 3 cost just $0.01. Speed tests (paragraph responses) cost $0.80 versus $0.12 for capability tests (numeric answers), demonstrating how prompt design directly impacts operational costs. The breakdown shows output tokens driving the majority of expense.](https://ailearnlog.com/wp-content/uploads/2025/02/summary_table_total_costs.png)

*Figure 8: Cost breakdown by test type and model, Opus accounts for 67% of all costs.*

It is obvious now that while developing your product at scale, prompts can be optimised for cost efficiency. But first, you need to ensure the model is fit for your use case. Then, look at the entire cost picture in place of the seemingly easy-to-compare token costs.

### Results Summary

Figure 9 below summarises all the results into one diagram. On the x-axis are the median speed test results (running prompt 1 against each model 50 times). On the y-axis are the capability test results (running prompt 2 against each model 50 times). The size of each circle is the total cost, for both speed and capability tests combined.

![Three-dimensional comparison of all five models: x-axis shows median speed (tok/s), y-axis shows accuracy (%), and circle size represents total test cost. Haiku 3 emerges as the standout performer—achieving 88% accuracy at ~97 tok/s for just $0.01. Opus 3 leads accuracy (94%) but at the slowest speed (~25 tok/s) and highest cost ($0.62). Sonnet 3.5 Oct performs worst overall: 8% accuracy, moderate speed, and $0.13 cost. The experiment totalled 500 API calls across two test prompts.](https://ailearnlog.com/wp-content/uploads/2025/02/speed_cap_cost_fig3.webp)

*Figure 9: All results into one view: The older Haiku 3 almost equals Opus in capability, outperforms all other models, and is the lowest cost. This is VERY unexpected.*

Comparing the benchmarks and Anthropic's model positioning, when measured against my fictitious use case of just two prompts, here are the biggest contradictions and surprises:

**Speed**
"Haiku 3.5 our fastest model" — it was not the fastest, Sonnet 3.5 was faster. Both dwarfed by the older Haiku 3. All newer models and snapshots degraded in speed.

**Capability**
"Sonnet 3.5 our best combination of performance and speed" — it was not, Haiku 3 outperformed Sonnet 3.5 on both. All newer models and snapshots degraded in capability.

**Cost — most surprising of all**
Haiku 3 is the fastest with the closest capability to Opus — yet it is the cheapest!

Again, though, please keep in mind that two little test prompts are not enough to draw a conclusion, but neither are general benchmarks. What these results prove is that you can expect to find surprises: you need to evaluate against your own use case by testing with use case relevant prompts.

## Future Proofing

You certainly will choose the wrong model, if for no other reason that things change rapidly: think of [DeepSeek-V3](https://www.deepseek.com/) that arrived in January. If the popular benchmarks are to be believed, it is comparable to Claude 3.5 Sonnet but at $0.28/MTOK[^4] instead of $3.00. That would make your December decision wrong (ceteris paribus).

The perfect choice does not matter nearly as much as your ability to adjust from a "wrong" decision. To do this you must be able to quickly evaluate new models (or updates) against your use case, then to have the built-in flexibility to switch, confidently.

So deeply consider (A) and (B) below:

### (A) For evaluating new models

As your product grows, you add more prompt evaluations for the prompts used by your product. Now not only do you have the evaluations you started off with in choosing your model, but a growing evaluation set truly representative of your use case. Strive for these tests to be automated. With a little work, you can run this evaluation set against other models for comparison.

At DeepSeek-V3 costing roughly 1/11th of Model 1 (output tokens), it is too difficult to believe that it could possibly be as good. You do not know until you test the model against your own use case. To be able to do this quickly and comprehensively is game-changing.

### (B) Making a model switch easier

From the start, at the very least allow your Engineers to invest in an abstraction layer. Get into a room and explain future proofing, explain the story of DeepSeek-V3 where Sonnet's cost is 1/11th of it. Go beyond price – as a team, what will you do when there's a new breakthrough model that is knocking the lights out on all leaderboards? What will it take to confidently and easily switch? How are we going to easily run our prompt evaluation suite against a new model?

The answer you are likely to get is, at the very least, an abstraction layer that sits between your application's code and LLM APIs. You do not need a perfect interchangeable model solution, but there are things that, if done with discipline from the start, will keep the product adaptable.

### A Zapier Perspective

As a leading automation platform, Zapier has extensively integrated LLMs. In a conversation with me, their VP of Engineering Mojtaba distilled the essence of this article in one breath:

> This space (base LLMs) is moving so fast that choosing the "right LLM" is basically the same as "choosing the right LLM for this week". In other words, the capability to a) quickly evaluate LLMs as they quickly evolve b) quickly adapt/pivot to new models is key (and not so much picking the right one at the moment). This includes ability to evaluate+pivot to LLM based on need. In other words, some LLMs are good at some things and others for another.
>
> [Mojtaba Hosseini](https://www.linkedin.com/in/mojtaba-hosseini-7a6666/), VP of Engineering, Zapier.

---

## Conclusion

In the real world, you cannot use only two prompts to compare models; you must strive for good coverage. I think of my product in major segments of LLM tasks. I emphasise more segments than others, but within each, I strive for coverage by creating relevant test prompts that inject real messy data. When it comes to costs, take the time to research the entire cost picture.

Once the model is chosen, the journey has only started. As your product grows and evolves, so too must your prompt evaluation test suite. Today's decision is likely to be wrong tomorrow.

Benchmarks and marketing are general, your use case is not. Take the time to automate your prompt evaluations. It is an investment that surpasses quarterly budgets. You may need to defend this investment but persist. You are giving the best chance of having your product flourish in a rapidly changing landscape, and to perform well along the way.

And yes, even the product manager must develop a solid understanding of prompting and statistical analysis (beyond just comparing "dots").

---

## Appendix I: Unexpected Variation {#appendix-i}

In a previous life as a Six Sigma consultant, one of the first steps was always to check if the data showed patterns related to time. If there are, the sampling plans and analysis had to be adjusted to draw any useful conclusions. This project here was not a rigorous statistical endeavour, but I did run the tests multiple times over 4-7th of February. For capability, I thought I was in the clear as "Correct %" scores looked very similar over these days.

Then by luck I ran my tests again on the 8th of Feb. This day was extraordinary as all the 3.5 models "jumped" in capability, together:

![Side-by-side capability results from February 4th versus February 8th revealing unexplained performance shifts. On Feb 4th, Haiku 3.5 scored 26% and Sonnet 3.5 Oct scored 8%. By Feb 8th, Haiku 3.5 jumped to 100% and Sonnet 3.5 Oct rose to 26%. Yellow indicators flag the models that shifted dramatically. This variation occurred without any known infrastructure changes, demonstrating why single-day testing can produce misleading conclusions.](https://ailearnlog.com/wp-content/uploads/2025/02/pic_days_capability.png)

*Figure 10: Capability scores were very similar between 4-7th Feb. On the 8th all 3.5 models skyrocketed together, with unknown cause. This is VERY unexpected.*

The lesson learnt is to run your tests more than once. Otherwise, you may be unlucky in that you are drawing your conclusions off of a day like my 8th of Feb. I asked Claude.ai to explain the results to me as an "LLM expert", to guess at what some of the special causes could be of this variation. This is what Claude said:

*Potential Technical Explanations:*

- *Infrastructure Changes*
- *Backend serving infrastructure might have been modified*
- *Load balancing configurations could have changed*
- *Model deployment settings may have been adjusted*
- *Cache clearing or system updates might have occurred*

*The Puzzling Aspect:*

- *The mathematical problem has a single correct answer*
- *Higher temperature might introduce more variance, but not systematic improvement*
- *Feb 4-7 showed consistent results*

Again: Run your tests more than once to be sure you have not caught an 8th of Feb day.

## Appendix II: Code {#appendix-ii}

The code to run and visualise test results is [available on Google Colab](https://colab.research.google.com/github/michellepace/anthropic-model-compare/blob/main/Anthropic_Model_Compare_(simple).ipynb); how speed was measured:

```python
from anthropic import Anthropic
import pandas as pd

# Start the timer
start_time = pd.Timestamp.now('UTC')

# Make API request to Claude and wait for response
response = anthrop_client.messages.create(
    model='claude-3-5-sonnet-20241022',
    max_tokens=400,
    messages=[{'role': 'user', 'content': speed_test_prompt}]
)

# Stop the timer
end_time = pd.Timestamp.now('UTC')

# Calculate speed in tokens per second
execution_seconds = (end_time - start_time).total_seconds()
output_tokens = response.usage.output_tokens
tokens_per_second = output_tokens / execution_seconds
```

---

### Footnotes

[^1]: Using an independent LLM to judge responses can be automated and provides more consistency than human evaluators.

[^2]: Response distribution showing accuracy rates across models.

[^3]: Pricing as of February 2025.

---

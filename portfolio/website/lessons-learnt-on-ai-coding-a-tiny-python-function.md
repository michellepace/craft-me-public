# Lessons Learnt on AI Coding a Tiny Python Function

I'm not a developer. It's just that I've heard so many dismiss AI assisted coding. It made me wonder, what is going on? I took a look for myself and got [Claude Sonnet](https://www.anthropic.com/claude) to generate my code. It went terribly wrong until I learnt these simple but powerful lessons:

1. **Learn to write good prompts** (and leave room for AI creativity).
2. **Get Claude to generate tests** to validate his generated code, iterate immediately.
3. **Set a robust pre-prompt** to generate good code (Appendix).

Your code is likely more complex than mine. But if you have not mastered the simple, there is little hope for the complex. I hope this article will make you curious enough to reconsider "AI Coding".

## The Task

Claude 3.5 Sonnet has a knowledge cut-off date of April 2024. To help Claude understand newer tools, I feed it their documentation files. I prefer using [markdown format](https://www.markdownguide.org/getting-started/) for this as Claude seems to understand it better.

My current Python code combines multiple markdown files into one. Each original file has its own Table of Contents, and I needed to extract these from the combined file — sometimes there's just one, other times up to fifty. Since this requires regular expressions (a type of text pattern matching I struggle with), I asked Claude to write a Python function to handle this task.

## Initial Prompt and Response

Here is the initial prompt I used to instruct Claude to write this function. When I wrote it, I felt like a world-class prompter—structured, detailed, long—what could go wrong?

![Author's initial prompt to Claude organised into three sections: "YOUR GOAL" defining the markdown Table of Contents removal task, "YOUR TASK" requesting a Python function with unit tests, and "YOUR STEPS" prescribing a four-step implementation process that constrained Claude's approach](https://ailearnlog.com/wp-content/uploads/2025/08/intiial_prompt.webp)

*Figure 1: My initial prompt instructing Claude to create the function I needed*

Reading this prompt in retrospect I can see how ambiguous it is. What I have learnt and in contradiction to my belief of being crystal clear, adding "IMPORTANT! Ask me questions to confirm understanding" will save you hours of wrestling with Claude. Nonetheless, here is Claude's response from the prompt above:

![Claude's first code attempt: a five-line Python function using an opaque regex pattern with re.sub—code the author admits they still cannot understand, demonstrating how AI-generated solutions can be functional yet incomprehensible](https://ailearnlog.com/wp-content/uploads/2025/08/initial_response_function.webp)

*Figure 2: Claude's initial attempt at the function (excluding six pytests)*

Claude's function above did not work at all, and I still don't understand the "pattern." However, the six pytests Claude wrote were easy to understand. Since these tests perfectly captured the functionality I needed—and all of them failed when I ran them—I knew that "remove_table_of_contents()" needed fixing.

## Iterating With Claude

It took me 3 rounds with Claude to get the function passing all six tests. Each round, I simply pasted the output of the failing tests to Claude, who would make changes to the function; I would then run the tests again.

- **Round 1:** All 6 tests failed. I gave Claude the failed tests and asked for the function to be fixed.
- **Round 2:** Now 4 tests failed, 2 passed. I gave Claude the failed output again and asked for another fix.
- **Round 3:** All 6 tests passed, and since I had the passing tests as proof, I knew the code worked.

![Final working Python function after three iteration rounds: readable code using list comprehension to filter sections—a cleaner, understandable solution achieved through test-driven iteration rather than the initial regex approach](https://ailearnlog.com/wp-content/uploads/2025/08/correct_function.webp)

*Figure 3: After iterating by providing failed pytest output back to Claude, this code worked perfectly.*

You could have written this little function and 6 tests yourself. Perhaps you would have been faster. But are you faster because you are exceptional, or because I haven't learned to prompt properly?

A small handful of the most exceptional developers I know are entirely on board with AI coding — quite a contrast to the many who dismiss it. After taking three tries to write one little function, I was leaning toward the latter. Clearly I had bumbled, and with nowhere else to look, I turned to examining my prompt.

## Investigating My Prompt

Why did Claude not code this tiny function correctly the first time? I asked Claude to review my initial prompt, which I had thought was crystal clear. Here is what Claude said:

![Claude's self-critique identifying four prompt failures: insufficient context about file structure, over-prescription that discouraged code reuse, ambiguous "ENTIRE section" requirement, and missing edge cases like case sensitivity—demonstrating how AI can diagnose its own input quality when asked](https://ailearnlog.com/wp-content/uploads/2024/08/calude_on_initial_prompt_shortcommings.webp)

*Figure 4: Claude's answer as to why my initial prompt had been ineffective.*

Based on this feedback, I instructed Claude to rewrite my initial prompt. On the first try, Claude presented an enormous prompt of 50 lines with every detail specified. I know what you are thinking: with such a detailed prompt, one might as well write the code directly.

Then I requested a second rewrite and, by pure chance, added—"rewrite the prompt to be effective but ensure it leverages AI creativity." When I ran this prompt, the resulting function worked perfectly the first time! If I had written a prompt like this from the start, I would have been done in 2 minutes (including the 6 tests). I doubt anyone can type that fast.

Claude's explanation of "AI creativity":

![Claude's explanation of "AI creativity": providing minimal but crucial context enables the AI to apply its knowledge of Python and markdown best practices autonomously, producing comprehensive solutions when freed from over-specified instructions](https://ailearnlog.com/wp-content/uploads/2024/08/claude-on-ai-centric.webp)

*Figure 5: Claude's explanation of AI creativity.*

## Conclusion: People and Prompting

I think 90% of people believe they can prompt, probably 99% if they are technical. It is really difficult not to assume this when it feels like you are in a real conversation and not a jungle of vectors in nth-dimensional space. If you have coded for years, you are likely worse at prompting than the rest of us. You have honed yourself for years to be declarative.

Prompting is a mind shift that requires deliberate practice; it does not simply happen. There is no Claude; an LLM is only a football stadium of vectors where the prompt is trying to find a needle. You must become proficient at prompting before dismissing AI-assisted coding.

> **Learn to prompt properly.**
> **It is very likely that Claude's ability vastly**
> **outstrips your prompting ability.**

Wrapping everything I learned from the time I spent with Claude on this function:

- **Learn to prompt:** Master writing better prompts to get faster at coding.
- **Don't be too declarative:** If you are overly specific, you lose the power of AI creativity.
- **Generate tests** from the start; you will iterate faster with greater accuracy.
- **Consider a system prompt:** To generate code how you like it (see Appendix).

## Appendix

As an illustrative example, below is the system prompt I have crafted for use in [VSCode](https://code.visualstudio.com/) whilst using Claude via the [Continue.Dev](https://continue.dev/) extension:

```diff
# You Are:
An expert Python programmer who writes, refactors, and analyses **clean and elegant code**, following **good Python programming practices**.

# For all Python-related tasks (including writing, refactoring, and analysing code):

## Assume Python 3.12

## Process:
1. **Think slowly and plan** the approach before taking action.
2. Execute the task following the guidelines below.
3. **Validate and test** the result for correctness and efficiency.

## Core Design Principles:
1. For **complex functionality**: Create smaller, manageable sub-functions.
2. **Use established libraries** to reduce code written.
   - Prioritize well-maintained, widely-used libraries
   - Explain your reasoning for selecting the library

## Implementation Rules:
1. Use `Path` from `pathlib` for file operations. Functions should accept `Path` objects for file paths.
2. For **function declarations**: Use built-in typing functionality (do NOT import typing library).
3. For **helper functions**: Use a single leading underscore (e.g., `_parse_config_file()`).
4. **Include clear comments** for complex logic.

## When asked to write tests:
Use `pytest`.
   - Write unit tests for individual functions
   - Consider parametrized tests for multiple input scenarios

## Documentation:
Use the following format for function docstrings:
def function_name(file_path: Path, other_param: type) -> return_type:
    """
    Brief description of function.
    :param file_path: Path to the file to be processed
    :param other_param: Description of other parameter
    :return: Description of return value
    """

## After completing the task:
- Briefly explain the changes or analysis made.
- Highlight any best practices or Python-specific features used.
- Summarize the validation process and results.
```

# Swim Club Website with AI Tools

**Project:** Design and build a website.

**Goal:** Elegantly simple for members. Easy to maintain for club staff. Responsive UI.

**Why I Volunteered:** To experience how far I could push AI to create something beautiful.

**Synopsis:** If you're not a web designer or developer, what would happen if you lent on AI to create a website? I found it is entirely possible. It takes finding good AI tools to get you there, and nosiness to learn.

I show the steps and tools used to do this. The distance moved from what was to what is, thanks to AI, is remarkable. Using AI did not take less thinking, ideas and iterations were just faster. Whilst there is wonderful freedom in volunteering, hitting the mark requires just as many conversations.

---

## Before & After

To get from the Before to the After, took choosing and learning a few AI tools. These are summarised in Table 1 below. But first take a quick look at the distance travelled:

Before (the old): [staging5.tsv-delphine.de](https://staging5.tsv-delphine.de)
The After (the new): [https://tsv-delphine.de](https://tsv-delphine.de)

![Before-and-after mobile comparison: the old TSV Delphine website with generic stock photography and dense information layout versus the AI-redesigned version featuring bold "Mach Mit, Tauch Ein" typography, streamlined navigation, and a distinctive hexagonal-mosaic swimmer portrait demonstrating the author's custom Midjourney visual style](https://ailearnlog.com/wp-content/uploads/2024/12/website_before_after_brown.jpg)

*Figure 1: Mobile comparison of the old website vs the new AI built website.*

I used [Perplexity](http://perplexity.ai/) to find, summarise, and compare potential tools. It is more powerful than pages of google results. I still had to trial many tools myself, but with much more focus thanks to Perplexity.

These are the tools I chose:

| Tool | Use |
| :--- | :--- |
| **Relume** [relume.io](https://www.relume.io/) | • Generate sitemap<br>• Generate wireframes |
| **Midjourney** [midjourney.com](http://midjourney.com/) | • Generate images own style<br>• Generate images style reference |
| **Claude.ai** [claude.ai](https://claude.ai/) | • Generate code for styling<br>• 1st pass English to German |
| **Eleven Labs** [elevenlabs.io](https://elevenlabs.io/) | • Dubbing how-to videos<br>• From English to German |
| **My Hours** [myhours.com](https://myhours.com/) | • Streamline logging worked hours<br>• For volunteer staff +payroll<br>• Was Excel before, now mobile |
| **Miro** [miro.com](https://miro.com/) | • Visual conversations |

*Table 1: Summary of tools used to create the website (and streamline staff payroll)*

The rest of this article outlines the broad steps taken. Shown in sequence, but with back-and-forth iterations between.

## Miro: For Talking

This step did not need AI, it was speaking with people who want and will use the website. Understanding their drivers and pain points, mentally linking it all together. Done visually in Miro, because then what you thought you understood can be validated by the people who thought they explained it clearly.

There were many scribbles like these in Miro, here is one of them:

[![User research synthesis on Miro: hand-drawn mind map connecting website visitor personas (parents, adult swimmers, members) to their specific needs—competition schedules, training times, coach information—with annotated screenshots of the existing site and handwritten notes capturing stakeholder feedback from discovery sessions](https://ailearnlog.com/wp-content/uploads/2025/01/miro-brainstorm-example_grey-1024x515.jpg)](https://ailearnlog.com/wp-content/uploads/2025/01/miro-brainstorm-example_grey.jpg)

*Figure 2: Example of good old fashion visual conversations to understand drivers and pain points, one of many.*

## Relume: Sitemap, Wireframes, Words

In Relume you write a prompt to describe the website you want to build (see below). An editable sitemap is generated, then you hit the "create wireframe" button and there you have your prototype. What is magical about Relume is that it generates "place holder" text relevant to the website. The text is good enough to skip grappling with words (for now), and to keep going.

The Relume prompt I wrote to generate a sitemap and then wireframes:

```text
Company description:
TSV Delphine is a community-driven swimming club based in Erding, Germany. We are a club open to both children and adults. We have qualified coaches, we provide everything from beginner swimming courses to competitive training programs in a supportive, family-friendly environment.

Goals:
- Primary: information hub for members on training schedules, competitions, social events.
- Secondary: attract new coaches to come and volunteer out our club. We are a dynamic.

Design Goals:
- Simplicity
- Clean design
- A "wow, what a great community club!" impression
```

Figure 3 below highlights Relume capabilities:

[![Annotated Relume interface demonstrating AI-assisted wireframing workflow: the page section panel for component selection, the "Ask AI" context menu offering actions like Generate copy and Replace component, and the generative features submenu for creating new sitemaps and pages from prompts—illustrating the author's chosen rapid prototyping approach](https://ailearnlog.com/wp-content/uploads/2025/01/Relume.io_.with-dots.jpg)](https://ailearnlog.com/wp-content/uploads/2025/01/Relume.io_.with-dots.jpg)

*Figure 3: A screenshot of Relume showing its major capabilities. A "page" is akin to a wireframe of a particular website page as listed in the generated sitemap.*

I collaborated on the design in Relume with the swim club, in fact we generated it together. I cheated a bit and did prepare in advance — sometimes magic is just preparation.

Here are most of the Relume wireframes:

[![Eight Relume-generated wireframes covering the complete swim club information architecture: Home page with hero and quick links, Club Training with session details, All Events calendar view, FAQ accordion, Contact form, Trainers profile grid, membership Join flow, and Swim Courses overview—demonstrating prompt-to-prototype output from a single AI generation](https://ailearnlog.com/wp-content/uploads/2025/01/Figma.togother.plus-mobile-grey.jpg)](https://ailearnlog.com/wp-content/uploads/2024/12/Figma.togother.plus-mobile-grey-large.jpg)

*Figure 4: In Relume, you write a prompt to generate an editable sitemap, and then editable wireframes are generated complete with relevant placeholder text. These are most of the wireframes I used.*

I exported the Relume wireframes to Figma to try a few font combinations. For me typography screams personality, but you could skip Figma entirely.

## Midjourney: Website Images

Prompting an image model is more difficult than Claude or ChatGPT. After a steep learning curve, I managed to create and maintain my own consistent "*hexagonal patterns slowly dissolving at the edges*" style. I got there by:

- Reading the Midjourney documentation and participating in their prompting community events.
- Creating a [design of experiments (PDF)](https://ailearnlog.com/wp-content/uploads/2025/02/Midjourney-experiment-with-style-stylize-sref-and-colour.pdf) to see the impact of the most significant parameters.
- Painfully documenting and building upon prompts as I went along, in my [Midjourney prompt log](https://docs.google.com/document/d/1rzDphmVj3nk209CY-RA_2BIEYoU0sVUZyD5KNwIj8YA/edit?usp=drive_link).

[![Twenty-plus Midjourney images in the author's custom hexagonal-mosaic style: swimmers mid-stroke, whimsical fish characters with expressive eyes, pool lane perspectives, and underwater scenes—all maintaining consistent blue-teal palette and geometric dissolution effect, shown alongside the final website pages where they appear](https://ailearnlog.com/wp-content/uploads/2024/12/midjourney-collage-collection-1024x578.jpg)](https://ailearnlog.com/wp-content/uploads/2024/12/midjourney-collage-collection.jpg)

*Figure 5: A collage of Midjourney images created in my own style, consistency was very difficult.*

Even more difficult, Midjourney has a "safety" policy that's restrictive on swimming images. The man in Figure 5 (top left) got restricted for "nakedness", and my appeal about male Olympic swimmers being topless failed. Yet I would inadvertently generate topless female swimmers, showing how strongly this persists in the training data despite the guardrails.

Working with swimmers in Midjourney was difficult and full body shots (of swimmers) near impossible; hopefully their guardrails have gotten more logical.

Below is the prompt I wrote to create [this image](https://www.midjourney.com/jobs/3deee2f5-0008-4434-8cbd-f9eba7b0c298?index=0), which served as the "base image" for most images in Figure 5. It helped to hold the hexagonal style, but I still needed the strength of styling words in [subsequent prompts](https://docs.google.com/document/d/1rzDphmVj3nk209CY-RA_2BIEYoU0sVUZyD5KNwIj8YA/edit?usp=drive_link).

```text
A swimmer's form depicted through a series of interconnected hexagonal cells, each containing different shades of blue and white. The figure appears to be emerging from a pixelated water surface, with the hexagons gradually dissolving into abstract patterns at the edges. The entire composition uses only geometric shapes.  --chaos 20 --ar 6:5 --stylize 750 --v 6.1
```

On the website page, [All Events](https://tsv-delphine.de/events/), the images are in a different style. This is because I needed to give a simple way for club staff to create new images for future events. Out of 3 billion "style reference codes" available, I found and loved "--sref 1797160075" on the [Thaeyne YouTube channel](https://www.youtube.com/@thaeyne). Look at the two examples below to see much easier it is to maintain a consistent style:

```text
Colouring book page of three children and a dolphin in a pool. --ar 16:9 --sref 1797160075

Three happy five year old club swimmers. --chaos 30 --ar 16:9 --sref 1797160075
```

Generated "sref" images:

[![Comparison of two Midjourney outputs using style reference code 1797160075: children playing with a dolphin and three young swimmers waving—both in bold-outlined, child-friendly cartoon style that the author selected to enable non-technical club staff to generate consistent event imagery independently](https://ailearnlog.com/wp-content/uploads/2025/01/midjourney-sref-1797160075-wide.png)](https://ailearnlog.com/wp-content/uploads/2025/01/midjourney-sref-1797160075-wide.png)

*Figure 6: Easy consistent styling using "--sref 1797160075"*

Of course, I only discovered the ease of using "sref codes" once everyone had fallen in love with my hexagonal style. So, I persisted.

## Claude: Wordpress & Code Assistant

Wordpress powers about 40% of the world's websites and is a content management system, it was an easy choice. From there however I needed help from Claude on how to build a Wordpress website.

As there is so much Wordpress information on the internet, Claude is very knowledgeable about it (up to April 2024). For all the questions you would usually ask in a forum, I just asked Claude. This really sped me up. For any custom CSS code that I needed to do, Claude did that for me too.

Using Claude as an English to German translator is described in the next section.

## Translation & Dubbing: Into German

I built in English first. I used the Relume generated content for ideas, and then I wrote. I wish I could say Claude was wonderful at translating, and it would have been, had I wanted to write in formal German. I tried several prompting techniques to get Claude to match the writing style I wanted but with little consistent success. I used Claude for a first pass translation, then had bilingual staff members re-write the translations in a warm professional tone.

In Table 1 at the start of this article, I mentioned a non-AI tool called "My Hours." It is disjoint but there is the AI link: Somehow when building this website, I also stumbled into payroll. The before state was 25 staff members filling out an Excel spreadsheet once a year to submit their worked hours. Now they do have the precision of being German, but could you imagine how difficult that is to remember (and to audit and budget)?

I found "My Hours", a mobile app that makes it easy to log hours on the go (or at the pool). I jumped on a sales call and was mightily impressed as it was in fact the product manager. This was a massive divergence from how things had always been done at the club. To ensure adoption I minimised friction. So, I first recorded a "how to" video in English, then I used Eleven Labs to dub me into German. I was not keen to have my voice "captured", but the glee of hearing myself speak fluent German was far too tempting:

- [How to use My Hours (English)](https://youtu.be/ZlvDU6HO2W8?si=sfe5Yvu1nhueYxs1)
- [How to use My Hours (German dubbed)](https://youtu.be/0vRsXKXenfc)

## In Conclusion

I am not sure AI is going to augment you as much as replace you, at least for most of us. If I can build a website single handedly now that I have AI, well to me that says professionals will be faster than ever. Faster means less people are needed to meet demand. For our times, I am convinced it is not so much your current skills that are valuable, but how nosey you are. The future is not one skill but the ability to learn and blend multiple skills. Then change. Again.

Both the website and the tracking of hours is fully adopted and loved. I purposefully pulled the staff through a Wordpress learning curve as I built this. I designed and named things well in the backend so nobody would have to remember. I wrote a good solid help doc for just in case. The sign of a good job done is to be redundant. Happily, I am redundant — they're swimming just fine in the deep end.

[![Live website hero section for TSV Delphine's adult swimming programme: the headline "Auch Erwachsene sind wasserfest!" (Adults Are Waterproof Too!) paired with the author's signature creation—a whimsical fish character wearing swimming goggles, rendered in hexagonal-mosaic style—capturing the club's welcoming, community-focused brand voice](https://ailearnlog.com/wp-content/uploads/2024/12/tsv-fish-picture.jpg)](https://ailearnlog.com/wp-content/uploads/2024/12/tsv-fish-picture.jpg)

*Figure 7: "Adults Are Waterproof Too!" my most favourite image and hero section. It still makes me smile.*

Thanks to Samantha, the Deputy Head of the Swimming Club. Her way of thinking was so different to mine that it made me see differently. Her excitement on every "i" I dotted and "t" I crossed propelled me further. It was all such a freeing creative pleasure. Thank you.

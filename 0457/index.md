---
title: "Module 0457: Tak's thoughts on AI, summer 2025 edition"
---

# What is this?

This is a Summer 2025 update of Tak's thoughts regarding AI within the context of teaching in general at a community college, as well as the specific subject of computer information science.

# AI in CIS

The following are some recent developments relevant to teaching computer information science in a community college.

## AI Researcher Payscale

Meta has recently started a high-profile hiring (mostly poaching) campaign, offering up to $1,000,000,000 (not clear about the method of distribution) to AI researchers already working for competing companies. 

**Thoughts**:

The ripple effect of Meta's action is a general salary increase for AI researchers or engineers working on AI-related products. Except for a few colleges and universities that offer AI as a degree or discipline, most incoming students need first to obtain a general computer science degree to launch their AI careers. As a result, computer science enrollment may continue to spike, although the same technology is also reducing the employment of software engineers (more on this later).

From a psychological and organizational perspective, Meta's action may be detrimental in the long run. What kind of people give up on their current jobs because of Meta's offer? What is the technical skill level of these people being poached by Meta? In short, Meta is attracting highly technically competent individuals who are drawn by substantial financial rewards. These people are also likely to be highly competitive and result-driven. It will be interesting to see how these people work out when they share the same employer.

## The generation gap of Vibe coding

[A study](https://www.reuters.com/business/ai-slows-down-some-experienced-software-developers-study-finds-2025-07-10/) finds that more experienced software developers get slowed down by AI tools. The study finds that more experienced software engineers need to spend time validating AI-generated suggestions. 

**Thoughts**:

The fact that some experienced software engineers *question* the validity of AI-generated suggestions is interesting. In a sense, the "vibe" in Vibe coding is the antithesis of the term "engineering." A more fundamental question is whether these questioning experienced software engineers are wasting their time because the AI-generated suggestions are correct to begin with. We will reexamine this in a later section.

Assuming the human user has no experience in programming nor an educational background in computer science, vibe coding is severely limited by the context window of a GPT. A typical GPT (as of summer 2025) has a context window of about 256k tokens. That loosely translates to a context of about 1 MB combining code, prompt, response, etc. While this capacity can develop some useful programs, it is insufficient for commercial or industrial programs. A GPT does not warn about approaching and exceeding the context window capacity. This can lead to incoherent code or code that makes incorrect assumptions, even if a specification was provided in an earlier prompt.

## More on vibe or AI-assisted coding

[Disasters happen](https://www.zdnet.com/article/bad-vibes-how-an-ai-agent-coded-its-way-to-disaster/). In this case, AI-generated code led to the deletion of tables in a database. 

**Thoughts**:

There are several key issues. The first issue is whether the AI assistant interprets the human's natural language description correctly. Mathematics and its notations predate the invention and use of computers by centuries. Why were mathematical notations even invented? This is not about internationalization because mathematics had been developed in parallel in multiple cultures. Mathematical notations are about conciseness, but most importantly, it is about precision.

# AI in education

## Sam Altman's "Knowing what questions to ask"

Sam Altman [discussed essential skills](https://www.windowscentral.com/software-apps/sam-altman-claims-knowing-what-questions-to-ask-trumps-raw-intelligence-as-ai-advances) for employment in the era of AI.

**Thoughts**:

If solving a problem is navigating from point A to point B, Sam Altman is saying the following:

* Humans should know how to define the waypoints, then let AI find the best routes from one waypoint to the next.
* Point A, point B, and all waypoints should be precisely specified.
* Humans should be able to measure the distance and direction of a location compared to a waypoint.

## Chinese Universities Embrace AI

MIT Technology Review discovered that [Chinese universities are more likely to embrace the student use of AI](https://www.technologyreview.com/2025/07/28/1120747/chinese-universities-ai-use/).

**Thoughts**:

This is the Yin-Yang/duality of Eastern versus Western approaches. The same duality exists in the practice of medicine. Eastern (specifically Chinese) scholars tend to be more comfortable with not fully understanding the exact nature of mechanisms and focus more on associating the action and reaction of black-box mechanisms. Western scholars, after the Greek philosophers, focus more on first understanding the exact mechanisms in the form of a rigid framework of theories before using such mechanisms in practical applications. Of course, this comparison is not absolute and universal.

LLM-based tools are here to stay, and employers expect productivity gains with the proper use of such tools. Consequently, students need to understand the nature of LLMs, their limitations, and how to utilize these tools effectively. This approach extends to more general neural network-based machine learning. 

## It takes skills to use AI effectively

AI (GPT/LLM) has intrinsic limitations. In a broad sense, the same skills in effective written and oral communication are also helpful in interaction with GPT/LLM tools. This is mainly because an LLM (large-language model) is trained based on content that is grammatically correct and effectively structured. The importance of the user's language skills increases with the complexity and length of a conversation with an AI tool.

An awareness of how GPT/LLM works is also important. For example, understanding the purposes and limitations of a context window is crucial to lengthy AI conversations on complex topics. There are techniques to sustain long and complex discussions.

The effective use of AI tools requires critical thinking skills, thought organization, and problem-solving skills. Not surprisingly, good communication skills are also essential in utilizing GPTs. This is because GPTs are (mostly) trained on human-created content that is grammatically correct. 

## AI-amplified Dunning-Kruger Effect

[The Dunning-Kruger Effect](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect) describes the phenomenon of the correlation between actual competency versus self-assessed level of competency. Specifically, people with little competency more often overestimate their competency than people with high competency.

AI (specifically chatbots) amplifies this effect. [According to ChatGPT](https://chatgpt.com/share/6898d6c6-f9a0-8013-b727-95443e3a72e9), an IQ of 85 is sufficient to operate a computer or smartphone sufficiently to ask questions in the web or app interface of ChatGPT. Depending on the version and specific test, ChatGPT demonstrates an IQ of 120 to 155. This means a person with an IQ of 85 may be able to answer questions that require an IQ of 120 (or more). Human self-reflection helps individuals differentiate their abilities from those of the AI tool. However, there is also a correlation between IQ and correct attribution (see the later part of the [linked ChatGPT conversation](https://chatgpt.com/share/6898d6c6-f9a0-8013-b727-95443e3a72e9)).

This presents a unique challenge to educators who encounter students who use GPT tools to shortcut their education. Increasing awareness of the amplified Dunning-Kruger Effect may help, but only to a certain degree, because a person can choose to disbelieve or willfully neglect. This issue is also easier to explain in a career education class, as opposed to a general education class. This is due to career-education classes can often quote from specific job descriptions or invite employers as guest speakers.

This amplified Dunning-Kruger Effect, combined with the inability to detect AI-assisted submissions, can be highly detrimental to students. The amplified Dunning-Kruger Effect increases the gap between the competency expected by employers and the self-assessed competency. The gap may not be discovered until after a student graduates with a degree.

## GPT/LLM as a pedagogy assistant

For people who have an extended chat history with a GPT/LLM, the GPT/LLM can advise customized pedagogy suggestions. Here is an *example*.

Start with a prompt like the following:

> Based on our conversation up to this point, can you estimate my IQ?

> I understand IQ is usually measured by specific, rigorous tests. However, there are also general traits associated with people within particular ranges of IQ. You can potentially use the "delta" between your responses and my follow-up prompts to measure the concept leap distance (extrapolation of patterns and problem-solving abilities).

> Do you think you can estimate my IQ? Note that this estimate is only for curiosity purposes and will not be used in any official manner.

A GPT/LLM is likely to respond with an assessment with a suggestion to provide a "concept-leap distance analysis." This number measures the leap distance/type in response-prompt from GPT/LLM conversations. You can modify the prompt to include only certain types of conversations. For example, instead of general conversations, specify "exploratory, learning, and research-oriented conversations." This may be applicable if you also use a GPT/LLM tool as a glorified search engine for facts.

With this number (along with the estimated IQ), you can then use the following prompt:

> Based on this analysis, suggest some pointers so I can relate to a population centered around an IQ of 100. This is of importance because I teach at a community college with no entry barriers. As a result, the student population is likely to center around an IQ of 100.

> These suggestions can be general strategies in communication styles and/or modality of communication. To provide additional context, I teach only in-person classes. This piece of information can be helpful because I can use gestures and interact in real-time with students.

The response to this prompt is customized to each individual. A GPT/LLM may even offer to summarize the suggestions into a "pocket" version for easier reference in a class or an office hour environment.

# AI in general

## Neural Net AI is a black box

The CEO of Anthropic is one of many to [openly admit](https://www.thealgorithmicbridge.com/p/no-one-knows-how-ai-works) that neural-net-based AI is a black box, and no one knows how it works. 

While the underlying learning and behavior mechanisms of a back-propagation neural network are well understood, what a neural network with many hidden layers can learn is not exactly understood. What a neural network with a high layer count learns can be inferred by tests, but such tests of a complex black box are sparse compared to all practical uses.

**Thoughts**:

Computer scientists understand how a neural network works, much like how electrical engineers comprehend how a transistor works. In the case of transistors, electronic engineers know how to organize transistors to accomplish specific computational tasks. Then, we have computer engineers and software engineers who derive classic computational solutions to solve specific problems.

Not so much in the case of neural networks. The back propagation training of a single-layer neural network is understood. Large language models (LLMs) rely on *huge* neural networks that have billions of neurons on each layer, and more than a hundred layers. At this scale, humans do not fully understand how the model works or how learned concepts are represented and applied.

Much of the research related to neural-network-based AI is based on experimentation, and in some ways, this experimentation is akin to witchcraft. This can be contrasted with two approaches in many STEM-related research studies. The scientific method is based on deriving a model/theory to explain a phenomenon, and then experiments are specifically designed to test the validity of the theory. The engineering method relies on validated models to put together a design that is known to solve a specific problem. Experiments are designed to verify the function of a design and to spot mistakes or oversights.

No scientific theory or engineering design is 100% correct. However, there is *certainty* that is guaranteed by the process of validation and verification.

However, a neural-network-based AI system is such a black art that there is essentially no certainty. While the application of a neural-network-based mechanism does not require it to be probabilistic, the AI-centric application is typically probabilistic. The same input presented to the same system does not guarantee the same output.

## GPTs and thought-forking

If the content in the context window leads to alternative forks for a human, a GPT cannot explore multiple branches like a person. In the case of a fork, the transformer mechanism probabilistically chooses the next token (word). 

In order for a GPT to explore multiple branches, the context window must include such an instruction, such as "generate alternative views." With the explicit instructions, the included forks, and the instruction to explore options, both become parts of the context for the transformer to continue looking for additional forks.

This is another example that illustrates the importance of understanding the general mechanism of a GPT in order to use it effectively.

# *What* do we teach about AI?

## Back-propagation neural network

This applies to most, if not all, LLM (Large Language Model) and other forms of AI tools. Understanding the general nature of a tool helps to determine how it can be used effectively in an application.

* **Probabilistic.** Several aspects are probabilistic. The key point is the lack of exactness or "rigor."
* **Imitative.** The primary function of a neural network (in computer science) is imitation. There is a dependency on **what** it is imitating. The source material that LLM neural networks learn from is human-filtered, human-curated, and human-annotated. In other words, despite the term "artificial", the neural network form of AI in the case of LLMs is very human-based.
* **Surface level.** Language floats on top of thoughts. LLMs are trained on language content. By their very imitative nature, LLMs can imitate on a language level, not on a thought level. The human brain/mind itself is also a black-box. Using a black box to imitate another black box on a surface level is a limiting approach.

## Strong and weak links

At the core of GPT (Generative Pre-trained Transformer) technology, a context that is based on the prompts, the responses, and various internal states of the conversation determines the likelihood of the next concept and token.

In a strong link, the most likely next concept or token significantly outweighs the alternatives. In a weak link, many conflicting concepts or tokens have similar weights and likelihood. Internal to the GPT engine, it can distinguish a strong from a weak link. However, the overall response to a prompt does not show these internal states.

One way to test for weak links is to repeat a prompt several times (each prompt in its own conversation with no memory of the other experiments) and evaluate the differences in the responses. If the responses are divergent, then we know the existence of at least one weak link in the chain.

## Convergence by filtering

Users of chatbots should be aware of the human factor in the creation of such chatbots. Without a consistent policy to filter and select training samples, a neural network cannot converge, and its responses will have many weak links. When presented with conflicting or divergent training samples, the back propagation training of a neural network does not reason, abstract, and learn what is common in such divergent samples.

In STEM subjects, this type of filtering has a small effect on the validity and bias of the responses. However, in many other conversations, this kind of filtering can effectively steer the user in one direction without considering the alternative directions.

## Context window

The context window of a GPT specifies the number of tokens (words and punctuation marks) that form the "attention". As of Summer 2025, this window is usually 256 thousand tokens in a higher-end GPT. 256 thousand tokens is about 1 MB (megabytes) of text, code, etc. While most casual use of GPT can hardly reach this limit, many documents can easily exceed this limit: legal documents, contracts, etc. The code base of commercial or industrial computer programs also often exceeds this limit.

Once a problem is too large to fit in the context window, a GPT does not issue any warnings. References to content that scrolls off the context window trigger the GPT to search beyond the conversation itself. This frequently leads to incorrect assumptions. 

To solve complex problems, a user must have mastery of the domain knowledge and skills of problem-solving, analysis, critical thinking, and communication. This allows a user to utilize a GPT within its capabilities. This is accomplished by breaking a complex problem into smaller problems with clear interfaces to the larger issue. The user also needs to validate the responses from the GPT tool. Knowing how to work within the limitations of a GPT requires skills and competencies that are beyond the domain knowledge and competency of a manual method.

## "Soft" skills

The skills of analysis, problem-solving, critical thinking, and communication are all important in the effective use of GPT/LLM. 

# *How* do we teach in the age of AI?

## Fundamentals

Knowing how to ask a chatbot for an answer is not the same as understanding the answer. More importantly, getting an answer from a chatbot is far from being able to verify and validate the answer! Regardless of the subject, being able to validate and understand an answer is crucial in the long run.

In the age of AI, one challenge is assessing the understanding of fundamentals. The classical method of asking students to derive solutions is no longer an adequate assessment.

Based on the relatively weak logical deduction ability of neural network chatbots, diagnosis-based assessments may be viable. The question is presented in the form of a derivation of a conclusion. Steps of the derivation may include errors. The learner is asked whether the derivation and conclusion are correct, and if not, where the flaws are. The type of question exploits the "agreeableness" of chatbots.

To generate questions of this variety, it is best to rely on an algorithm that can systematically but randomly insert erroneous steps in a chain of reasoning or derivation.

## In-person assessment

Back to the basics. In-person, pen-and-paper quizzes and exams are as effective as they have always been. 

There is an equity concern regarding in-person, on-paper assessments. See this [ChatGPT conversation](https://chatgpt.com/share/688cd2cc-d158-8013-955b-4b8f5a76bb0b) on this topic.

---
title: "Module 0457: Tak's thoughts on AI, summer 2025 edition"
---

# What is this?

This is a Summer 2025 update of Tak's thoughts regarding AI within the context of teaching in general at a community college, as well as the specific subject of computer information science.

# AI in CIS

The following are some recent developments relevant to teaching computer information science in a community college.

## AI Researcher Payscale

Meta has recently started a high-profile hiring (mostly poaching) campaign, offering up to $100,000,000 (not clear about the method of distribution) to AI researchers already working for competing companies. 

**Thoughts**:

The ripple effect of Meta's action is a general salary increase for AI researchers or engineers working on AI-related products. Except for a few colleges and universities that offer AI as a degree or discipline, most incoming students need first to obtain a general computer science degree to launch their AI careers. As a result, computer science enrollment may continue to spike, although the same technology is also reducing the employment of software engineers (more on this later).

From a psychological and organizational perspective, Meta's action may be detrimental in the long run. What kind of people give up on their current jobs because of Meta's offer? What is the technical skill level of these people being poached by Meta? In short, Meta is attracting highly technically competent individuals who are drawn by substantial financial rewards. These people are also likely to be highly competitive and result-driven. It will be interesting to see how these people work out when they share the same employer.

## The generation gap of Vibe coding

[A study](https://www.reuters.com/business/ai-slows-down-some-experienced-software-developers-study-finds-2025-07-10/) finds that more experienced software developers get slowed down by AI tools. The study finds that more experienced software engineers need to spend time validating AI-generated suggestions. 

**Thoughts**:

The fact that some experienced software engineers *question* the validity of AI-generated suggestions is interesting. In a sense, the "vibe" in Vibe coding is the antithesis of the term "engineering." A more fundamental question is whether these questioning experienced software engineers are wasting their time because the AI-generated suggestions are correct to begin with. We will reexamine this in a later section.

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

LLM-based tools are here to stay, and employers expect productivity gain with the proper use of such tools. Consequently, students need to understand the nature of LLMs, their limitations, and how to utilize these tools effectively. This approach extends to more general neural network-based machine learning. 

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

# What *do* we teach about AI?

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

# How do we teach in the age of AI?

## Fundamentals

Knowing how to ask a chatbot for an answer is not the same as understanding the answer. More importantly, getting an answer from a chatbot is far from being able to verify and validate the answer! Regardless of the subject, being able to validate and understand an answer is crucial in the long run.

In the age of AI, one challenge is assessing the understanding of fundamentals. The classical method of asking students to derive solutions is no longer an adequate assessment.

Based on the relatively weak logical deduction ability of neural network chatbots, diagnosis-based assessments may be viable. The question is presented in the form of a derivation of a conclusion. Steps of the derivation may include errors. The learner is asked whether the derivation and conclusion are correct, and if not, where the flaws are. The type of question exploits the "agreeableness" of chatbots.

To generate questions of this variety, it is best to rely on an algorithm that can systematically but randomly insert erroneous steps in a chain of reasoning or derivation.

## In-person assessment

Back to the basics. In-person, pen-and-paper quizzes and exams are as effective as they have always been. 

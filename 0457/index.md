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



# AI in general

## Neural Net AI is a black box

The CEO of Anthropic is one of many to [openly admit](https://www.thealgorithmicbridge.com/p/no-one-knows-how-ai-works) that neural-net-based AI is a black box, and no one knows how it works. 

**Thoughts**:

Computer scientists know how a neural network works, much like how electrical engineers know how a transistor works. In the case of transistors, electronic engineers know how to organize transistors to accommplish specific computational tasks. Then we have computer engineers and software engineers to derive classic computational solutions to solve specific problems.

Not so much in the case of neural networks. The back propagation training of a single-layer neural network is understood. Large language models (LLMs) rely on *huge* neural networks that have billions of neurons on each layer, and more than a hundred layers. At this scale, humans do not fully understand how the model works or how learned concepts are represented and applied.

Much of the research related to neural-network-based AI is based on experimentation, and in some ways, experimentation in a witchcraft way. This can be contrasted to two approaches in many STEM-related research. The scientific method is based on deriving a model/theory to explain a phenomenon, and then experiments are specifically designed to test the validity of the theory. The engineering method relies on validated models to put together a design that is known to solve a specific problem. Experiments are designed to verify the function of a design and to spot mistakes or oversights.

No scientific theory or engineering design is 100% correct. However, there is *certainty* that is guaranteed by the process of validation and verification.

However, a neural-network-based AI system is such a black art that there is essentially no certainty. While the application of a neural-network-based mechanism does not need to be probabilistic, the AI-centric application is mostly probabilistic. The same input presented to the same system does not guarantee the same output.


---
title: "Module 0458: CS in the GPT/LLM era"
---

# What is GPT/LLM?

GPT (Generative Pre-trained Transformer) refers to a category of AI (artificial intelligence) tools that are generally neural-network-based and respond to text prompts with answers. In addition to regular conversations, GPTs can also generate program code.

More specifically, LLMs (Large Language Models) can be used to assist or even originate coding. This poses the question of "what is the role of computer science when AI can write code?"

## Neural networks, in general

A neural network with back propagation learning is, essentially, an imitation engine that is trained by samples in the form of input-output pairs. Assuming there is a pattern to the input-output pairs, an appropriately sized and architected neural network can generalize from the training samples to extrapolate the outputs of non-training inputs of the same pattern.

## GPT

A GPT has an underlying neural network. There are two distinct features of a GPT.

First, a GPT is trained on the *sequencing* of tokens. A token is, essentially, a word or a useful punctuation mark in programming. A GPT answers the question of "given these are the tokens in a sequence that is already produced as a part of the input, what is the most likely next token?" This is an exceptionally simplistic view of a GPT.

The neural network of a GPT is *vast*. It abstracts and learns patterns from the training samples. The training samples include everything that is on the Internet, possibly with the addition of specific proprietary sources of samples.

Another distinct feature of a GPT is an "attention* mechanism. Without an attention mechanism, a GPT can wander off in a conversation or a train of thought. The length of the context window partially characterizes the attention mechanism. A longer context window means a GPT conversation can maintain a coherent discussion longer, and also relate more concepts in a conversation. The length of a context window is measured in the number of tokens. A token is a word or a punctuation mark. 

# Tips to make use of a GPT/LLM

## GPT/LLM is a tool

Like *any* tool, GPT/LLM has limitations. More importantly, the effective use of such a tool relies on the skills and competencies of the user. 

### An LLM is trained on language samples

This point is significant because a practical prompt needs to use language (words) to provide sufficient context.

### An LLM is trained on content written by "average" people

### An LLM is trained on mostly grammatically correct content

For simpler queries, the grammar and punctuation of a prompt may not impact the results. However, for complex conversations, grammatically correct prompts can yield better results. This is because a GPT can better parse and understand a grammatically correct prompt.

## Awareness of context window size

For coding purposes, if the concerned source code has more tokens than the length of the context window, then an LLM cannot be aware of the entire program. In a complex conversation, if the conversation (including prompts and responses) is longer than the context window size, then earlier parts of the discussion no longer inform the continuation of the conversation.

The awareness of context window size is, therefore, vital when GPT/LLM is used to process anything lengthy or complex.

## Handling long and/or complex discussions

A GPT can estimate the length of a conversation in terms of tokens. It can be helpful to check the length of a conversation to make sure the relevant part is within the context window. In the event of a conversation that is close to the context window length, there are methods to help maintain the relevant part of the context.

* Summarize. This performs two tasks at once. It compactifies the information that is still in the context window, and it also refreshes such content to be the latest part of the context window. Most GPT makes use of a mechanism that is similar to first-in-first-out to maintain the context window. As a result, asking a GPT/LLM to summarize refreshes the context.
* Fact extraction. Similar to summarizing, but with a focus on extracting just the factual data to formulate the latest context. 
* External memory. Exports a conversation to be stored. Most GPTs can create a file (usually in Markdown format) for downloading.


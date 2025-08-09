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

## Awareness of context window size

For coding purposes, if the concerned source code has more tokens than the length of the context window, then an LLM cannot be aware of the entire program. In a complex conversation, if the conversation (including prompts and responses) is longer than the context window size, then earlier parts of the discussion no longer inform the continuation of the conversation.

The awareness of context window size is, therefore, vital when GPT/LLM is used to process anything lengthy or complex.

## Handling long and/or complex discussions

* Summarize. This performs two tasks at once. It compactifies the information that is still in the context window, and it also refreshes such content to be the latest part of the context window. Most GPT makes use of a mechanism that is similar to first-in-first-out to maintain the context window. As a result, asking a GPT/LLM to summarize refreshes the context.
* Fact extraction. Similar to summarizing, but with a focus on extracting just the factual data to formulate the latest context. 
* External memory.


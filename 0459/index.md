---
title: "Module 0459: OER as a Custom GPT"
---

# What is a Custom GPT?

A custom GPT is a structures interaction with ChatGPT. There are two main components to a custom GPT:

* An instruction. This is the text that is preloaded into every prompt in a custom GPT chat. The purpose of the instruction is to remind ChatGPT of everything that it should know in the interaction.
* Support files. These files from the knowledge "chunk" from which a custom GPT response may refer to. These files can be large and exceed the context window size of a model.

Together, a custom GPT can serve a specific role, with specific constraints and mode of operation, and specific knowledge to reference.

In the context of OER, a custom GPT can serve as an interactive book, a tutor, or a virtual professor. The key is the collection of support files.

# Why is this important?

The authoring of a book is difficult not because of the author lacking the knowledge, but how the knowledge is presented to the target audience. A custom GPT only needs the knowledge to be correct, complete, and organized. The actual presentation of the material is flexible, and it can be catered to each individual learner based on reading comprehension level, competency of prerequisite knowledge, language preferences, etc.

A custom GPT can also create practice questions and examples on-the-fly. This ability allows a learner to learn in different ways.

# Support files

The support files can be in a variety of formats, but Markdown is one of the best choices.

It is important that the support files be structured. This refers to content (semantic) structure, not format structure. 
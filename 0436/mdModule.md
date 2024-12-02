---
title: "Module 0436: Custom GPT as an educational tool"
---

# _{{ page.title }}_

## An educational tool in more than one way

1. Using a custom GPT as a tutor.
2. Learning about learning in the process of customizing a custom GPT.
3. Find out how teaching material can be improved using GPT as a model.

These ways of utilizing a custom GPT for education purposes are inseparable. 

## Custom GPT background information

### What is a custom GPT?

A custom GPT is a GPT (chatbot) that is specialized for a particular task, possibly having specific knowledge that is not generally available on the internet. It is important to understand that a custom GPT is *not* a GPT pre-trained with specific data. Via the use of the OpenAI API (application programming interface), a GPT can be pre-trained with specific samples. However, pre-training a GPT requires a lot of samples, and it is generally not required.

A custom GPT offers specialization without pre-training. 

### What are the components of a custom GPT?

A custom GPT has a section of "instructions" and up to 20 files as its "knowledge." The instructions can have up to 8000 tokens (words). 

The "knowledge" files can be plain text files. The markdown format also works well. The Markdown format has the advantage of being structured without a lot of overhead. 

The "instructions" text can also be specified in Markdown. This is the core of a custom GPT. The instructions text specifies the purpose of the custom GPT, workflow, restrictions, validations rules, preferences, etc. Interestingly, it can be fine-tuned using ChatGPT itself. This process will be described in a later section.

The "knowledge" files should be specifically named so that they can be referenced from the instructions. This is where specific knowledge can be "offloaded" from the instructions text. 

## Setting up to use a custom GPT

Although a custom GPT does not require any additional resources, a revision control repository like `GitHub` is highly recommended. `GitHub` or a similar revision control repository can help track the changes to the instructions and the knowledge files. 

Because the knowledge files are "static", it may also be helpful to have tools to automate the generation of these files, or at least to describe how to acquire these files manually. 

Last, but not least, having a set of test cases is also important. Being able to consistently test a custom GPT in the fine-tuning process is of paramount importance.

## General strategies

The creation and fine-tuning of a custom GPT is dynamic, but some general strategies apply to most cases.

### Assigning a version or release number

It is important to associate a custom GPT with a specific version or release number. This allows consistent revision control using `GitHub` (or a similar tool) as well as testing. This can be specified in the instructions as follows:

```text
This is release 13 of this custom GPT. A user of this custom GPT can inquire about the release.
```

With this, the associated `GitHub` repository can be tagged with the same release number to track changes. More importantly, however, is that sometimes, somehow, ChatGPT can revert to using an older version of a custom GPT. Being able to check the release or version number is crucial to "debugging" a custom GPT.

### Automatic versus manual update to the instructions

The "preview" side of a custom GPT can instruct ChatGPT to update the instructions. While convenient, an automatic update may not organize instructions correctly. A beginning custom GPT developer can start with automatic revision of the instructions, but gradually transition to manual updates.


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

In the preview window, a custom GPT developer can specifically request to update the instructions for a specific adjustment. For example,

```text
Update the custom GPT instructions so that the custom GPT uses a softer tone when pointing out mistakes of a learner.
```

To learn how to do this manually, a custom GPT developer can use the following prompt:

```text
How can I change the custom GPT instructions to use a softer tone while pointing out the mistakes of a learner?
```

If a custom GPT developer does not want to risk ChatGPT accidentally revising the custom GPT instructions directly, then tests should be performed in the normal ChatGPT interface and not in the "preview window." However, this also requires the restriction of who can access a custom GPT that is being developed. Furthermore, ChatGPT may mistakenly use an earlier release of a custom GPT in this method, hence the importance of specifying the version or release number in the instructions.

### ChatGPT may know *too much*

A custom GPT starts with all the knowledge of ChatGPT, and that is a lot. The problem is that a custom GPT may need to restrict the applicable knowledge to a smaller domain. In this case, a custom GPT developer can specify all the applicable knowledge in the knowledge files, and include specific instructions to only use the knowledge contained in the files.

Due to the probabilistic nature of a GPT, it is still possible for a custom GPT to reference knowledge that it is not supposed to use. It may be necessary to specify validation or verification in the instructions to filter responses that do not pass the test. Verbs like "verify", "cross-check" and "validate" can be combined with adverbs like "strictly". These sentences can also directly reference a knowledge file by name.

### ChatGPT self reflection

In the testing of a custom GPT, if the response is not satisfactory, the custom GPT developer can ask ChatGPT to self-diagnose. For example, if a response is supposed to be `XYZ`, but the custom GPT responds with `ABC`, the developer can inquire something like:

```text
Please explain which parts of the custom GPT instructions or knowledge files lead to the response of ABC.
```

It is important not to disclose the correct answer of `XYZ` initially so that ChatGPT can focus on retracing the steps that led to the response of `ABC`. If the explanation itself is insufficient to lead to revisions to correct, the problem, a follow-up question can be asked:

```text
The correct response is XYZ, not ABC. What revisions to the instructions or knowledge files can help prevent this mistake in the future?
```

### Process specification

The instructions can specify processes. A process can be described as an ordered list, possibly with sub-lists for each step. A process can also be conditional to certain types of prompts. This allows the instructions to specify different processes depending on the properties of the prompts. For example:

```text
If the prompt is about a murder mystery, then use the following process:

1. Identify the characters:
  * Associate the name of each character with his or her participation in the story
  * Indicate the first time the character is mentioned
  * Indicate the last known state of the character
2. Describe the murder
  * What is stated about the murder
  * Where is the murder discovered
  * Who discovered the murder
  * Who is or are the victim(s) of the murder
  * All additional details about the murder
3. Associate character with the identified murder victims
  * How is each character associated with each murder victim?
  * Identify the motives of each character to commit the murder, if any. A motive can be
    * Financial
    * Emotional
4. Analyze the timeline of each character and validate the opportunity of the murder:
  * Identify explicit timeline conflict that rules out a character as the murderer
  * Generate a list of characters who are not cleared by timeline conflicts
5. For each character who does not have a timeline conflict, perform the following analysis:
  * Assuming this character commits the murder, does this lead to any contradiction of details in the story?
  * If the previous step leads to a contradiction, rule out the character
6. List all characters who are not cleared due to any contradiction or timeline conflict.
```

### Emphasize less common conventions or knowledge


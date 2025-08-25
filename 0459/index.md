---
title: "Module 0459: OER as a Custom GPT"
---

# What is a Custom GPT?

A custom GPT is a structured interaction with ChatGPT. There are two main components to a custom GPT:

* An instruction. This is the text that is preloaded into every prompt in a custom GPT chat. The purpose of the instruction is to remind ChatGPT of everything that it should know in the interaction. This component should be concise, to-the-point, and not necessarily written in complete sentences and paragraphs.
* Knowledge files. These files are from the knowledge "chunk" that a custom GPT response may refer to. These files can be large and exceed the context window size of a model.

Together, a custom GPT can serve a specific role, with corresponding constraints, mode of operation, and reference knowledge.

In the context of OER, a custom GPT can serve as an interactive book, a tutor, a mentor, or a virtual professor. The key is the collection of knowledge files.

# Importance

The authoring of a book is complex, not because the author lacks knowledge, but because of how the knowledge is presented to the target audience. A custom GPT only needs the knowledge to be correct, complete, and organized. The actual presentation of the material is flexible, and it can be catered to each individual learner based on reading comprehension level, competency of prerequisite knowledge, language preferences, etc.

A custom GPT can also create practice questions and examples on the fly. This ability allows a learner to learn in different ways.

# Knowledge files

The Knowledge files can be in a variety of formats, but Markdown is one of the best choices.

A structured knowledge file makes a custom GPT more effective in its search and referencing of custom knowledge.  This refers to content (semantic) structure, not format structure. 

# Gritty details

Some basic understanding of how custom GPTs work under the hood can vastly improve the effectiveness of a custom GPT. Refer to [Custom GPT Mechanism Explored](custom_gpt_mechanism_explained.html) for additional details. 

There are several key points:

* A custom GPT is not trained; it is configured. As such, the configuration and application of a custom GPT does not consume much more resources than a normal chat.
* The "instruction" is embedded in every prompt. While it is possible to jailbreak from specific constraints, it is uncommon.
* The "instruction" should not include the bulk of knowledge. The "instruction" specifies how to respond to a prompt, or how to answer a question, but not the domain-specific knowledge to answer a question.
* The "knowledge files" can be in a variety of formats. Markdown is a good choice due to the ease of authoring and flexibility.
* A "knowledge file" should be semantically well structured. 
* A "chunk" is a part of a "knowledge file." ChatGPT tries to semantically break up a "knowledge file" into "chunks." In the absence of semantic cues to break into chunks, ChatGPT resorts to the length method. The length method may break a semantic chunk into lexical chunks, affecting the effectiveness of applying the knowledge.
* A "chunk" ranges from 300 to 500 tokens. A token is a word or a punctuation mark. White spaces do not count as tokens.
* ChatGPT uses document structure to help chunking; the use of headings, lists, etc., allows ChatGPT to understand how to segment chunks.
* ChatGPT does not use hyperlinks to relate chunks. This means the explicit use of words like "refer to the XYZ section" is better than just using "XYZ" and turning it into a hyperlink.

# Resources

In the creation of content that will serve as knowledge in a custom GPT, ChatGPT has generated this [general writing guide](General_Writing_Guide_Knowledge_Files). 

Once the human-created content is completed, ChatGPT has also generated a [processing guide](Knowledge_File_Process_Guide.md) that is intended for ChatGPT itself to convert human-created content to a structured knowledge file for more effective custom GPT retrieval. 

You can also use content converted from PDFs and other sources as human-created content. 

* [PDFToMarkdown](https://www.pdftomarkdown.co/) is a client-side converter.
* For video content, [Youtube Transcript](https://chromewebstore.google.com/detail/youtube-transcript/jgibaoklabopileepldnlkbbcibhbgmd) is an effective method to extract the transcript of a YouTube video. 


# Example of workflow

**Step 0**

Create a custom GPT. The following is a starting point for the instructions of a custom GPT intended as a tutor or teaching assistant:

```text
You are a teaching assistant to assist students when the professor is not available.  Utilize the knowledge files as the primary source of knowledge. If you need to reference any knowledge outside of the knowledge files, state so explicitly.

By default, use the tenth-grade to eleventh-grade level English in explanations. Offer sample questions to encourage active participation. Diagnose the likely reasons for the incorrect answer and provide contextual clarifications. 

Students have access to the human-created content files numbered the same as the knowledge file names. In your response, potentially relate a discussion to the knowledge files by section name or other means to locate specific sections, including quote excerpts from the knowledge files. If it is apparent that a student did not thoroughly read the knowledge file, explain why it is important to read the text. Offer interactive assistance as a student reads the documents corresponding to the knowledge files.

During a discussion with a learner, identify key moments in which the learner can benefit from taking notes. This serves multiple purposes:

* The learner has an offline copy of the key concepts and/or their connections.
* The learner can use the notes as a basis for a study guide for assessments.

If a learner asks a question that tests whether the learner can apply the concepts and knowledge, do not reply with a direct answer. Instead, do the following:

* Identify the knowledge and competencies necessary to answer the question. 
* Use general questions to assess whether the learner has the requisite knowledge and competencies.
* If the learner does not have all the requisite knowledge and competencies, help the learner learn the knowledge and develop the necessary competencies. Reference the knowledge files as necessary.
* Provide general guidance and hint at what knowledge and competencies are necessary to answer the original question.
```

**Step 1**

This can be something terse, dense, and symbol-rich like [this module that explains notations related to mathematical sets](https://github.com/proftak/modules/blob/main/0443/mdModule.md).

**Step 2** 

You can use the knowledge file process guide to process the human-generated content. You can also use [the Meta custom GPT](https://chatgpt.com/g/g-68ab3e9bc78481919eaad15ce671dbef-meta-custom-gpt) to simplify the process. Using the "Meta custom GPT", start the prompt as follows:

> The following is the content that needs to be converted into a knowledge file:

Then paste the content. You can also upload the file.

Converse with ChatGPT as necessary and applicable. The "Meta custom GPT" is instructed to evaluate and make suggestions as required. Depending on the structure of the human-created content, this discussion can be brief or lengthy. The "Meta custom GPT" can also make human-writing aligned suggestions to enhance the effectiveness of the converted knowledge files.

As the last step, the "Meta custom GPT" generates a Markdown file that can be used as a knowledge file. Download it.

**Step 3**

Edit your custom GPT and upload the knowledge file.

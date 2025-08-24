---
title: "Module 0459: OER as a Custom GPT"
---

# What is a Custom GPT?

A custom GPT is a structured interaction with ChatGPT. There are two main components to a custom GPT:

* An instruction. This is the text that is preloaded into every prompt in a custom GPT chat. The purpose of the instruction is to remind ChatGPT of everything that it should know in the interaction. This component should be concise, to-the-point, and not necessarily written in complete sentences and paragraphs.
* Support files. These files are from the knowledge "chunk" that a custom GPT response may refer to. These files can be large and exceed the context window size of a model.

Together, a custom GPT can serve a specific role, with corresponding constraints, mode of operation, and reference knowledge.

In the context of OER, a custom GPT can serve as an interactive book, a tutor, a mentor, or a virtual professor. The key is the collection of support files.

# Importance

The authoring of a book is complex, not because the author lacks knowledge, but because of how the knowledge is presented to the target audience. A custom GPT only needs the knowledge to be correct, complete, and organized. The actual presentation of the material is flexible, and it can be catered to each individual learner based on reading comprehension level, competency of prerequisite knowledge, language preferences, etc.

A custom GPT can also create practice questions and examples on the fly. This ability allows a learner to learn in different ways.

# Support files

The support files can be in a variety of formats, but Markdown is one of the best choices.

A structured support file makes a custom GPT more effective in its search and referencing of custom knowledge.  This refers to content (semantic) structure, not format structure. 

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

Once the human-created content is completed, ChatGPT has also generated a [processing guide](Knowledge_File_Process_Guide) that is intended for ChatGPT itself to convert human-created content to a structured knowledge file for more effective custom GPT retrieval. The following is the raw Markdown version for copy and paste into ChatGPT:

```markdown
{% include_relative Knowledge_File_Process_Guide.md %}
```

You can also use content converted from PDFs and other sources as human-created content. 

* [PDFToMarkdown](https://www.pdftomarkdown.co/) is a client-side converter.
* For video content, [Youtube Transcript](https://chromewebstore.google.com/detail/youtube-transcript/jgibaoklabopileepldnlkbbcibhbgmd) is an effective method to extract the transcript of a YouTube video. 




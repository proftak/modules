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

# A helper

ChatGPT itself, outside of the custom GPT that is being constructed, can help with the organization of ideas, the structuring of a knowledge file, and the proper use of headings to lexically structure the document.

The role of the human is, therefore, to think of what ideas, concepts, facts, and other material to include. Furthermore, the human can also write about how the ideas, concepts, facts, and other material relate to each other. All this material can be messy and unorganized. ChatGPT can be instructed to organize, structure, and turn the messy collection into an effective knowledge file.

First, we start with the template of a knowledge file:

```text
The following is a template for a knowledge file, we will refer to it as "the knowledge file template" in the following prompts.

# {{Project / Domain Title}}
_Aim: A retrieval-friendly knowledge file for Custom GPTs. Keep sections concise (≈300–500 tokens) and self-contained._

<!-- Authoring notes (delete before publishing):
- Prefer short, topical sections; avoid walls of text.
- Repeat parent context in each subsection title or first sentence.
- Use consistent terminology; add synonym “retrieval hooks”.
- Favor headings/paragraphs/lists as natural chunk boundaries.
-->

## Scope & Audience
- **Who:** {{target users}}
- **What:** {{topics covered / excluded}}
- **When to use:** {{situations / workflows}}

## Executive Summary (TL;DR)
- {{3–6 bullets of the most important points}}
- {{key decisions / defaults}}

## Table of Contents
- [1. Core Concepts](#1-core-concepts)
- [2. Procedures & Checklists](#2-procedures--checklists)
- [3. Patterns & Examples](#3-patterns--examples)
- [4. Reference](#4-reference)
- [5. FAQ](#5-faq)
- [6. Glossary](#6-glossary)
- [7. Retrieval Hooks](#7-retrieval-hooks)
- [8. Change Log](#8-change-log)

---

## 1. Core Concepts
_Introduce each concept in its own subsection. Keep each subsection coherent and self-contained._

### 1.1 {{Concept A}} (Part of {{Parent Topic}} → {{Project/Domain}})
**Definition:** {{1–2 sentences}}  
**Why it matters:** {{impact / use cases}}  
**Inputs/Dependencies:** {{prereqs, assumptions}}  
**Outputs:** {{artifacts, decisions}}  
**Common pitfalls:**  
- {{pitfall 1}}  
- {{pitfall 2}}

### 1.2 {{Concept B}} (Part of {{Parent Topic}} → {{Project/Domain}})
**Definition:** {{…}}  
**Contrast with:** {{related concepts and how they differ}}  
**Signals/Heuristics:** {{how to recognize when relevant}}

### 1.3 {{Concept C}} (Part of {{Parent Topic}} → {{Project/Domain}})
**Definition:** {{…}}  
**Metrics/Criteria:** {{how to evaluate / success measures}}

> **Cross-reference (inline, retrieval-friendly):**  
> See **{{Target Section Name}}** for {{key terms repeated here}}.

---

## 2. Procedures & Checklists
_Procedures should be stepwise and testable. Keep each under ~500 tokens._

### 2.1 {{Procedure Name}} (for {{Context}})
**Goal:** {{what success looks like}}  
**Preconditions:** {{required state / inputs}}  
**Steps:**
1. {{step}}
2. {{step}}
3. {{verification / acceptance check}}

**Rollback / Recovery:** {{if things go wrong}}  
**Time/Cost Considerations:** {{optional}}

### 2.2 {{Secondary Procedure}} (for {{Context}})
**Steps:**  
- {{bullet}}  
- {{bullet}}  
**Quality Gates:** {{criteria to proceed}}

---

## 3. Patterns & Examples
_Concrete, minimal examples improve retrieval precision._

### 3.1 Pattern: {{Name}} (Use when {{conditions}})
**Problem:** {{short}}  
**Solution:** {{short}}  
**Trade-offs:** {{list}}  
**Example:**
```{{language}}
# minimal, compilable/run-able if possible
{{code or configuration snippet}}

```

Then we present the instruction to convert a conversation into a knowledge file of the specified template:

```text
You will be given a long, unorganized, and meandering discussion on a specific topic.  
Your task is to **restructure the content into a clean, semantically coherent knowledge file** that can be uploaded into a Custom GPT for retrieval.

## Instructions

1. **Apply the Knowledge File Template**
   - Use the previously defined structure:
     - Title, Scope & Audience, Executive Summary
     - Core Concepts (with subsections and parent context repeated)
     - Procedures & Checklists
     - Patterns & Examples
     - Reference (tables, policies, decision matrices)
     - FAQ
     - Glossary
     - Retrieval Hooks
     - Change Log
   - Format strictly in **Markdown** with `#`, `##`, `###` headings and lists.

2. **Preserve Semantic Content**
   - Keep all *correct* and *complete* information from the discussion.
   - Remove digressions, repetitions, and irrelevant side notes.
   - If multiple phrasings exist for the same idea, consolidate them but add synonyms in the *Retrieval Hooks* section.

3. **Chunking Awareness**
   - Each subsection should be about **300–500 tokens** (short, coherent units).
   - Ensure subsections are self-contained — they must make sense if retrieved alone.
   - Repeat parent context in titles (e.g., `### Linear Regression (Supervised Learning → Machine Learning)`).

4. **Cross-References**
   - Avoid dangling references like “see above.”
   - If cross-reference is needed, repeat the key terms inline.

5. **Clarity**
   - Use plain, direct prose suitable for intelligent readers who may not be specialists.
   - Use lists, tables, and headings liberally to create natural lexical breakpoints.

6. **Final Output**
   - Return the finished **Markdown document only**, provide a link to download the document.
   - Do not include explanation, commentary, or meta-text — just the file.

---
```

And then finally, we present the actual discussion to be converted. Note that ChatGPT can retrieve an entire chat just by referencing the topic. If possible, use the full title of the discussion. Here is an example of a prompt:

```text
Now convert our discussion title "Analogical rebuttal analysis" into a knowledge file using the above knowledge file template and instructions.
```

You may find a browser extension that allows you to copy a ChatGPT discussion/conversation in Markdown to be particularly useful. This allows you to paste the content of a discussion directly into a prompt for processing. The Chrome extension [ExportGPT](https://chatopenai.pro/exportgpt/) works well, even in the free version.

# Resources

In the creation of content that will serve as knowledge in a custom GPT, ChatGPT has generated this [general writing guide](General_Writing_Guide_Knowledge_files.md). 

Once the human-created content is completed, ChatGPT has also generated a [processing guide](Knowledg_File_Process_Guide.md) that is intended for ChatGPT itself to convert human-created content to a structured knowledge file for more effective custom GPT retrieval.

Instead of using a ChatGPT discussion, you can also use content converted from PDFs and other sources. [PDFToMarkdown](https://www.pdftomarkdown.co/) is a client-side converter.




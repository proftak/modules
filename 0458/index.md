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

A GPT/LLM does not reason like a person; it relates and infers based on the tokens (words and punctuation marks) sequencing of content created mainly by humans. "Average humans."

As such, a GPT/LLM may not be trained to connect steps that may seem obvious to people who are accustomed to deep thinking and problem-solving. This does not mean GPT/LLM is not helpful, but guidance and breaking down complex tasks into smaller steps may be necessary. 

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

None of the above techniques solves the problem of a finite-length context window. To utilize GPT/LLM to solve large and complex problems, human needs to partition the larger problem into smaller pieces with well-defined interfaces between the pieces. The process is repeated until each puzzle piece is small enough to fit in the context window of a GPT/LLM tool. In problem-solving, the "interface" can be expressed in the form of an assumption. For example, "assume the air pressure of the inlet is regulated to a range of 120 to 130 PSI." *How* this assumption is guaranteed is the responsibility of another session with a GPT/LLM tool.

# CS/CE/EE in the GPT/LLM era

## Knowing how to use GPT/LLM is essential

Employers expect their employees to be efficient and productive. GPT/LLM tools *can* improve the efficiency and productivity of software development and coding. 

**Important:** Students may equate this to using a homework assignment description as a prompt to get a working program for submission. This misunderstanding can be costly in the long run. This is because the complexity of any homework assignments at a community college level is *well* within the capacity of a GPT/LLM. However, commercial and industrial computer programs are too complex to fit in the context window of a GPT/LLM. As a result, the apparent success of turning in solutions to homework assignments using GPT/LLM tools does not correlate with the actual competency needed in industry.

## Go beyond homework assignments

Due to the relative simplicity of homework assignments and the inability of a transcript to differentiate whether the homework assignments are completed manually or AI-assisted, a student needs additional evidence to show their worth to a potential employer.

### Internship

Internships are beneficial in many ways, especially when they relate to the area of study. 

First, an internship experience allows a student to learn in a more realistic environment. Even if the task of an intern is testing code, the code being tested is commercial/industrial with engineered test cases using a robust test system. 

Second, if an intern performs well, the "employer" can serve as a verifiable reference in job applications. 

Third, some internships are paid. In many cases, the pay of an internship is the least impactful part of the internship experience.

### Personal projects

Internships may not be available to everyone due to scheduling limitations, etc. Personal projects, however, are viable for almost every student.

The main benefit of a personal project that relates to the area of study is that its complexity can easily exceed that of individual homework assignments. While a homework assignment is typically due in one to two weeks, a personal project can span months, quarters, or semesters. Furthermore, unlike homework assignments, the use of GPT/LLM tools is perfectly fine in a personal project. The proper use of GPT/LLM tools can significantly speed up the completion of a personal project.

The key to leveraging a personal project to help with landing a job is documentation in the form of source code commenting, periodic reflection, and summaries of insights. GitHub is an excellent revision control mechanism for tracking documentation because every change is logged. It is essential to check in (commit and push) changes and documentation periodically to prove authenticity. Even draft documents containing thoughts from brainstorming sessions are important. 

### Professors

Some professors may choose to hide from students, but most are approachable. Demonstrating study area competency to a professor beyond course assessments can be beneficial. 

This can be as casual as a weekly visit to an office hour for 15 minutes, discussing fringe/tangential topics related to a course. Regular contact with a professor enables the professor to write recommendations or to serve as a meaningful reference. The effect is compounded if the office hour visits involve discussions of personal projects and other activities that demonstrate competencies that an employer looks for. One competency is the effective use of GPT/LLM tools. 


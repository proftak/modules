# How a Custom GPT Works: A Creator's Guide

This guide explains, in practical terms, how a **Custom GPT** operates inside ChatGPT so you can write effective **instructions** and prepare **supporting files**.

---

## 1. What a Custom GPT Is
A **Custom GPT** is not a different AI model.  
It’s a **configuration layer** on top of the GPT models you already use (like GPT-4o or GPT-5).  

When you create one, you set:
- **Custom instructions** (tone, style, rules, goals)
- **Tool permissions** (e.g., web browsing, code interpreter)
- **Optional knowledge files** (uploaded documents)
- **Example interactions** (to guide behavior)

These settings shape *how* the GPT responds — they don’t change the model itself.

---

## 2. What Happens When You Use a Custom GPT
When you open a Custom GPT and send a message, this sequence happens:

1. **Inject Custom Instructions**  
   - Your custom rules are added to the start of the conversation as hidden “system instructions.”  
   - These guide the model for every response.

2. **Add Your Query**  
   - Whatever you type is appended after the instructions.

3. **Retrieve Relevant File Content (If You Uploaded Files)**  
   - The system breaks your files into small chunks when you upload them.
   - Each chunk is stored with a *semantic fingerprint* (called an embedding) so the GPT can find the right part later.
   - When you ask a question, the system looks for chunks most related to your query and adds them to the prompt.

4. **Include Recent Conversation History**  
   - Previous turns are included until the context limit is reached.
   - If the conversation is too long, oldest turns drop off first — but your instructions stay.

5. **Send Everything to the GPT Model**  
   - The GPT sees:  
     ```
     [Your instructions]
     [Your query]
     [Retrieved file chunks]
     [Recent conversation]
     ```
   - It uses all this to generate a response.

---

## 3. The Role of the Context Window
The **context window** is the model’s “working memory” for the current conversation.  
Everything listed above must fit inside it.

- GPT-5 has a very large window (e.g., ~128k tokens).
- If the combined instructions, query, file content, and conversation exceed this limit:
  - Oldest conversation turns are removed first.
  - File chunks are always re-fetched fresh each time.

---

## 4. Key Points for Creators
To make your Custom GPT work well:
- **Write precise instructions** — these are always included.
- **Structure files for retrieval** — good headings, clear sections (see *Best Practices* guide).
- **Expect retrieval to be semantic, not keyword-only** — use consistent terminology.
- **Avoid over-relying on file cross-references** — the system doesn’t follow links.
- **Test common queries** — ensure the right chunks are being retrieved.

---

## 5. Why This Matters
If you understand this flow, you can:
- Give the model exactly the behavioral framing you want.
- Prepare documents so the right parts show up in answers.
- Avoid surprises when the conversation gets long or when a query misses important file sections.

---

**In short:**  
A Custom GPT is like a **pre-trained assistant** with a fixed personality and toolbox, but it only knows what’s in the current context window. Your job as creator is to make sure instructions and files give it the best possible starting point for any query.

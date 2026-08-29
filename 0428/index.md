---
title: "Module 0428: Exam 2 Question 3 Code Correction"
author: Tak Auyeung
kramdown:
  syntax_highlighter_opts:
    disable: true
---

# What is this document?

This document describes how to answer question 3 of exam 2 in CISP 310. Specifically, what is a correction and how it is scored.

# Types of answers

## Correction

Some instructions or definitions are partially correct. In these cases, the answer is to cross out the wrong part while keeping as much of the original instruction or definition as possible. Here is an example:

> ~~`ldi`~~`ld a,(b) // use ld instead of ldi`

## Insertion

Some instructions or definitions may be missing entirely. In these cases, an answer is in the form of an insertion of instructions or definitions. In this case, use an arrow to point to the insertion point of the additional code. Here is an example:

> `cmp a,b`<br />
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\leftarrow$ `jzi L1 // if (a==b) goto L1; need to branch if a==b`<br />
> `// get here when a != b`

## Deletion

Some instructions or definitions should not be present, at all. In these cases, an answer is a strike-out of the instructions of definitions that should be removed. Here is an example:

> ~~`cpr d,c`~~ `// do not overwrite register d, it is needed later`

# How a correction is scored

## Incorrect code is corrected

If the original incorrect code is corrected and commented on, it receives 4/4 for that particular incorrect code. The lack of comments deducts one point to 3/4.

## Incorrect code is not corrected

Usually, this receives zero point, 0/4. However, if there is commenting that *identifies* the flaw, some partial credit may be earned. The partial credit, if any, is 1/4.

## Correction itself is flawed

If the incorrect code is identified and explained, but the correction itself is also flawed, partial credit will be earned. Depending on the flaw, the partial credit ranges from 1/4 to 3/4.

## Correct code is "corrected"

If the provided code is correct, and a "correction" is made, points will be deducted because the correction indicates a lack of understanding of how the original code works. The deduction is -1/4. This means four "corrections" to correct code counteract the properly commented correction of incorrect code.

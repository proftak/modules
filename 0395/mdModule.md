---
title: "Module 0395: CISP 310 Final Exam Explanations"
author: Tak Auyeung
kramdown:
  syntax_highlighter_opts:
    disable: true
---

# What is this document?

This document describes how to answer questions in the final exam of CISP 310. Specifically, what is an explanation and how it is scored.

# Types of answers

## Correction

Some instructions or definitions are partially correct. In these cases, an answer is in the form of crossing out the part that is wrong, but keeping as much of the original instruction or definition as possible. The answer should also include an [explanation](#how-to-explaincomment).

## Insertion

Some instructions or definitions may be missing entirely. In these cases, an answer is in the form of an insertion of instructions or definitions. The answer should also include an [explanation](#how-to-explaincomment).

## Deletion

Some instructions or definitions should not be present, at all. In these cases, an answer is in the form of a strike-out of the instructions of definitions that should be removed. The answer should also include an [explanation](#how-to-explaincomment).

## Explanation of correct instructions/definitions

Some instructions or definitions are correct, but an [explanation](#how-to-explaincomment) is requested. In these cases, an answer is in the form of an explanation of what each involved register contains, and the effect of the instruction.

# How to explain/comment

## Relating to C/C++ concepts

An explanation should relate to C/C++ concepts. For example, the following explanation does not meet the requirement of relating to C/C++ concepts:

```ttpasm
  add c,d // c=c+d
```

However, assuming `var1` is a local variable, and the correct offset to `var1` from where the stack pointer points to is already loaded into register `c`, then the following explanation for *this* instruction meets the requirement:

```ttpasm
  add c,d // c == &var1
```

In this example, how register `c` gets the offset to `var1` from where the stack pointer points should also be explained in some prior instructions. See [chained explanations](#chained-explanations) for more details.

## Reason of correction

In the cases of correction, insertion or deletion, the reason of the correction should be stated. Again, this explanation should relate to C/C++ concepts. In other words, describe what the code *is supposed to do*, and what the code would have done without the correction. For example, an insertion may look like the following:

$<$ `ld a,(a) // a==var1, a==&var1 without this instruction`

In this example, earlier instructions also need to be [chain-commented](#chained-explanations) to explain how reg `a` already has the address of `var1` before this inserted instruction.

## Chained explanations

Some answers involve the correction, deletion, insertion, or the explanation of instructions that involve the use of one or more registers. In these cases, it is necessary to explain how each involved register gets its value by commenting related earlier instructions.

### Example 1

In the following example, assume `var1` is a global variable in C/C++, and the label `GLOBAL_var1` is defined to bookmark the location of `var1`.

```ttpasm
  ldi a,GLOBAL_var1
  sub b,b
  st  (a),b // describe the effect of the instruction
```

In this example, the first task to use the opcodes table to look up what is `reg x` and `reg y`. However, the following answer will receive no point value because it does not relate to concepts in the C/C++ code:

```ttpasm
  ldi a,GLOBAL_var1
  sub b,b
  st  (a),b // describe the effect of the instruction    answer: *a=b
```

The following answer receives partial credit (2/4) because it does not fully explain *how* reg `a` and reg `b` get their values:

```ttpasm
  ldi a,GLOBAL_var1
  sub b,b
  st  (a),b // describe the effect of the instruction    answer: a==&var1, b==0, effect: var1=0
```

In order to receive full credit (4/4), the chain of instructions that contribute to the values of reg `a` and `b` must also be explained:

```ttpasm
  ldi a,GLOBAL_var1 // a==&var1
  sub b,b // b==0
  st  (a),b // describe the effect of the instruction    answer: var1=0
```

### Example 2

In the following example, assume `var1` is a global variable in C/C++, and the label `GLOBAL_var1` is defined to bookmark the location of `var1`. Furthermore, assume the code fragment is to push the address of `var1` on the stack.

```ttpasm
  ldi a, GLOBAL_var1
  ld  a,(a)
  dec d
  st  (a)
```

The correction is to remove the `ld` instruction. However, the following answer receives 1/4 of the credit because it has no explanations:

```ttpasm
  ldi a, GLOBAL_var1
~ ld  a,(a) // <-- DELETE
  dec d
  st  (a)
```

The following answer receives partial credit (2/4) because it explain partially what happens with the deleted instruction, but not why it is incorrect.

```ttpasm
  ldi a, GLOBAL_var1
~ ld  a,(a) // <-- DELETE, otherwise a==var1
  dec d
  st  (a)
```

The following answer receives full credit (4/4) because it explains what is in reg `a` at the removed instruction, how reg `a` gets its value *prior* to the removed instruction, and what is expected:

```ttpasm
  ldi a, GLOBAL_var1 // a==&var1
~ ld  a,(a) // <-- DELETE, otherwise a==var1
  dec d
  st  (a) // push &var1
```

## Other types of explanations

Not every explanation is about registers. Some explanations may relate to a control structure. For example, the lack of a unconditional branch at the end of a `while` loop to get back to the beginning may require the following explanation:

$<$ `jmpi f_while0_begin // otherwise there is no repetition`

Essentially, the explanation describe what would have happened erroneously if the correction is not in place.

# General strategies

## Always track/comment

A general strategy is to add comments to track the code all the time, and not to wait until an answer is expected. This strategy can end up saving time because a register may not seem important until it is reference much later in the code. Instead of backtracking and trying to figure out and comment register when needed, the "always-on" commenting means a quick look at commented prior line can connect the *reference* of a register from the *overwriting* of the same register that may have occurred many lines before the reference.

## Shorthand notations

While "always-comment" sounds like a major chore, some shorthand can be useful.

For example, if `f_var1` is "the offset of `var1` from where the stack pointer points to", then a shorthand that makes sense is `&f_var1-d`. For example:

```ttpasm
  ldi b,f_var1 // b==&f_var1-d
```

If `X_m1` is the "offset of member `m1` from the beginning of a `struct X`, then a shorthand can be `&m1-&X` or $\mathtt{m1}\Delta \mathtt{X}$. Here is an example:

```ttpasm
  ldi c,X_m1 // c==&m1-&X
```

## Watch the notations

Be careful with the address-of (`&`) and dereference (`*`) operators. The following is a list of examples of notations that can be easily confused:

* `&var1-d`: the offset of a non-static (auto) local variable or parameter `var1` from where the stack pointer points to
* `&var1`: the address of a variable `var1`
* `var1`: the value of `var1`
* `*var1`: what `var1` points to, assuming `var1` is a pointer

Here is another list of more examples of notations that can be confusing:

* `var1.m`: the value of member `m` of `var1`, assuming `var1` is a structure with a member `m`
* `&(var1.m)`: the address of member `m` of `var1`
* `var1->m`: the value of member `m` of a structure (that has a member `m`) that is pointed to by `var1` (assuming `var1` is a pointer to a structure)
* `&(var1->m)`: the address of member `m` of a structure that is pointed to by `var1`

The incorrect use of these notations can result in a deduction of points.

## Parenthesize when in doubt

If you cannot remember the priority of operators, use parentheses to indicate how operations should be nested. For example, `*p++` is really `*(p++)` and not `(*p)++`. However, `&p->m` is the same as `&(p->m)`. 

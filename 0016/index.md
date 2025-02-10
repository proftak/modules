---
title: "Module 0016: Loops"
---

# About this module

-   Prerequisites: [0013](../0013/mdModule.html)
-   Objectives: This module discusses various iterative control
    structures.

# What is a loop, again?

A loop is a control structure that permits certain steps in a program to
be repeated. Without loops, programs cannot perform certain steps again
and again, often without knowing exactly the number of times to repeat.

In real life, we often rely on loops as well. For example, the logic of
eating is iterative. Let's think about eating a relatively large order
of food. The basic step is "eat a spoonful" (or whatever quantum of food
you want to use). Ahead of time, we don't know exactly how many
spoonfuls is necessary. The proper logic to eat a meal is "eat as many
spoonfuls as possible until you feel full".

# Repeat that, again!

Let us explore loops, again. However, this time, we use a special kind
of structure. Let us take a look at the following algorithm that specifies the logic to eat.

```c
do                    // line 1
  take a bite         // line 2
while (one is hungry) // line 3
```

Now, let's take a closer look at this block of code.

-   line 1: this is a "marker" that marks the
    beginning of actions to be repeated.
-   line
    2: this line serves two purposes.
    First, the word "until" is a marker that marks the end of actions to
    be repeated. Second, this line expresses the condition that
    specifies when the action should not be repeated anymore.
-   line 3: this is the action to be repeated. In
    general, there can be exactly one statement between the markers
    "do" and "while".

No explanation is complete without a trace. The following trace able
illustrates the steps taken when someone only needs three bites to
become full.

|line #|comment|
|:-|:-|
|1|this is not necessary since it doesn't do anything|
|2|this is the first bite|
|3|the condition is evaluated, one is still hungry|
|1|this part is important, we get back to this line because the condition is true|
|2|this is the second bite|
|3|the condition is still true|
|1|since one is not full yet, here we go again|
|2|this is the third bite|
|3|this time around, one is full, and this condition is false now; *we don't have to take another bite!*|
|post|the algorithm exits|

There is a problem with the above algorithm. What if someone is already full to begin with? A
special property of a "do-while" loop is that the action is performed *at
least once*. This is because the "while" condition is evaluated after
the action is performed.

## The flowchart of a "do" loop

The logic of the code in the previous section can be represented by the following flowchart:

```mermaid
flowchart TD
start@{shape: stadium, label: "start"}
merge@{shape: diamond, label: " "}
eat@{shape: rect, label: "take a bite"}
decision@{shape: diamond, label: "is one hungry?"}
finish@{shape: stadium, label: "end"}
start --> merge
merge --> eat
eat --> decision
decision -->|true| merge
decision -->|false| finish
```

## The syntax of a "do" loop

A "do" loop (also called a *post-checking* loop) is a kind of *`statement`*, the related BNF rules are as follows:

* *`statement`* ::= *`doStmt`*
* *`doStmt`* ::= **do** *`statement`* **while (** *`condition`* **)**

# Is this all worth while?

Since we concluded that the previous "eating" algorithm is not perfect, there must be a better
way. What we need is a loop construct that evaluates the condition first
to see if an iteration is necessary, then perform the action only if it
is necessary.

This loop structure is as displayed in the following algorithm.

```c
while (one is hungry) // line 1
  take a bite         // line 2
```

This control structure looks like a "do-while" loop reversed. Let's
explain each line in the new algorithm.

-   line 1: this line is analoguous to line 3 of the "do-while" algorithm. It is a marker to mark the beginning of actions to be performed. It also presents a condition to be evaluated. If this condition is "true" then the action is   performed. If the condition is "false" then the loop terminates.
-   line 2: this line is the action to be *possibly* performed repeatedly. Note that after the action is performed, we go back to line 1 so that we can determine whether it is necessary to perform the action again.

The following table is a trace of algorithm if a person is full (not hungry) to begin with.

|line #|comment|
|:-|:-|
|1|because the person is full already, the condition "one is hungry" is false
|post|when the condition of a "while" loop is false, the loop is terminated.

## The flowchart of a "while" loop

The following is a flowchart corresponding to the "while" loop algorithm.

```mermaid
flowchart TD
start@{shape: stadium, label: "start"}
decision@{shape: diamond, label: "is one huntry?"}
eat@{shape: rect, label: "take a bite" }
finish@{shape: stadium, label: "end" }
start --> decision
decision -->|true| eat
decision -->|false| finish
eat --> decision
```

## The syntax of a "while" loop

A "while" loop is also known as a *pre-checking* loop. It is a kind of statement. The BNF rules related to a "while" loop are as follows:

* *`statement`* ::= *`whileStmt`*
* *`whileStmt`* ::= **while (** *`condition`* **)** *`statement`*

# Examples

## Counting

```c
x=0;              // line 1
while  (x < 3) {  // line 2
  x=x+1;          // line 3
}                 // line 4
```

To trace this code, line 4 is not in the table because it is a syntactic construct that does not perform any action. However, line 2 is important because it evaluates the condition `x < 3`. The trace is as follows:

|line #|`x`|comments|
|:-|:-|:-|
|pre|?|We were not told any assumption about `x`|
|1|0| |
|2| |`x` is not changed, but the condition evalutes to `0 < 3` which is true|
|3|1|`x` is incremented|
|2| |`x` is 1, `1 < 3` is true|
|3|2| |
|2| |`x` is 2, `2 < 3` is true|
|3|3| |
|2| |`x` is 3, `3 < 3` is false|
|post| |exit from the loop|

Note that even though line 2 does not change `x`, the comments states whether the condition evaluates to true or false. This is important in a trace so that we can track the logic of a loop. Also, note how at the end of the trace, the trace goes from line 2 to "post".


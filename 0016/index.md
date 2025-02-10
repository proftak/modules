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

# Picture of a "repeat" loop

Let's look at a "trail map" of algorithm
[\[algorithm:repeateat\]](#algorithm:repeateat){reference-type="ref"
reference="algorithm:repeateat"} in figure
[1](#figure:repeateat){reference-type="ref"
reference="figure:repeateat"}.

!["Trail map" of algorithm
[\[algorithm:repeateat\]](#algorithm:repeateat){reference-type="ref"
reference="algorithm:repeateat"}.](repeateat){#figure:repeateat}

In a trail map representation, each path is one-way only. The top
junction is a merge junction, which means the top and right paths merge
into the down path. The bottom junction is a fork, which means the top
path splits into the down path and the right path. The rectangle labeled
"one is full?" is the question to answer. Depending on whether the
answer is "true" or "false", the bottom or right path is chosen,
respectively.

# Is this all worth while?

Since we concluded that algorithm
[\[algorithm:repeateat\]](#algorithm:repeateat){reference-type="ref"
reference="algorithm:repeateat"} is not perfect, there must be a better
way. What we need is a loop construct that evaluates the condition first
to see if an iteration is necessary, then perform the action only if it
is necessary.

This loop structure is as displayed in algorithm
[\[algorithm:whileeat\]](#algorithm:whileeat){reference-type="ref"
reference="algorithm:whileeat"}.

``` {#algorithm:whileeat .numberLines .pseudocode language="pseudocode" numbers="left" caption="Correct eating logic" label="algorithm:whileeat"}
while one is not full %\label{whileeat:while}%
  take a bite %\label{whileeat:eat}%
end while %\label{whileeat:end}%
done! %\label{whileeat:done}%
```

This control structure looks like a "repeat" loop reversed. Let's
explain each line in algorithm
[\[algorithm:whileeat\]](#algorithm:whileeat){reference-type="ref"
reference="algorithm:whileeat"}.

-   line [\[whileeat:while\]](#whileeat:while){reference-type="ref"
    reference="whileeat:while"}: this line is analoguous to line
    [\[repeateat:condition\]](#repeateat:condition){reference-type="ref"
    reference="repeateat:condition"}. It is a marker to mark the
    beginning of actions to be performed. It also presents a condition
    to be evaluated. If this condition is "true" then the action is
    performed. If the condition is "false" then the loop terminates and
    continues on line
    [\[whileeat:end\]](#whileeat:end){reference-type="ref"
    reference="whileeat:end"}.

-   line [\[whileeat:eat\]](#whileeat:eat){reference-type="ref"
    reference="whileeat:eat"}: this line is the action to be *possibly*
    performed repeatedly. Note that after the action is performed, we go
    back to line
    [\[whileeat:while\]](#whileeat:while){reference-type="ref"
    reference="whileeat:while"} so that we can determine whether it is
    necessary to perform the action again.

-   line [\[whileeat:end\]](#whileeat:end){reference-type="ref"
    reference="whileeat:end"}: this is a marker to mark the end of the
    action that may be performed again and again.

-   line [\[whileeat:done\]](#whileeat:done){reference-type="ref"
    reference="whileeat:done"}: this is simply a line after the loop so
    that we can indicate the termination of the loop in a trace.

Table [2](#table:whileeat){reference-type="ref"
reference="table:whileeat"} is a trace of algorithm
[\[algorithm:whileeat\]](#algorithm:whileeat){reference-type="ref"
reference="algorithm:whileeat"}.

::: {#table:whileeat}
  line \#                                                                                  comment
  ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  [\[whileeat:while\]](#whileeat:while){reference-type="ref" reference="whileeat:while"}   because the person is full already, the condition "one is *not* full" is false
  [\[whileeat:done\]](#whileeat:done){reference-type="ref" reference="whileeat:done"}      when the condition of a "while" loop is false, the loop is terminated. Execution moves to the line immediately following the end marker.

  : A trace of algorithm
  [\[algorithm:whileeat\]](#algorithm:whileeat){reference-type="ref"
  reference="algorithm:whileeat"}, assuming a person is already full
  before this algorithm.
:::

No explanation is complete without a picture. Figure
[2](#figure:whileeat){reference-type="ref" reference="figure:whileeat"}
illustrates the logic of algorithm
[\[algorithm:whileeat\]](#algorithm:whileeat){reference-type="ref"
reference="algorithm:whileeat"}. You can tell that it is a loop because
of the loop-back branch on the left hand side. Note that this loop back
goes from bottom to top. Also note the branching fork is *below* (or
after) the merge point. This means that when we loop back after taking a
bite, we always reevaluate the condition "one is not full", then
determine whether to take the "true" path or "false" path.

![Trail path representing the logic of algorithm
[\[algorithm:whileeat\]](#algorithm:whileeat){reference-type="ref"
reference="algorithm:whileeat"}.](whileeat){#figure:whileeat}

# Argh, repeat no more!

Some languages support the concept of "repeat", but C and its derived
languages do not have repeat. Instead, such languages have an "upside
down while". Let us illustrate with an example.

Let us consider algorithm
[\[algorithm:repeatex\]](#algorithm:repeatex){reference-type="ref"
reference="algorithm:repeatex"} as an example.

``` {#algorithm:repeatex .numberLines .pseudocode language="pseudocode" numbers="left" label="algorithm:repeatex" caption="Repeat-until example to illustrate an upside-down while loop."}
repeat
  ask for a ZIP code
until the ZIP code is valid
```

This logic keeps asking for a ZIP code until a valid one is entered.
Note that because this is a repeat-until loop, the action (asking for a
ZIP code) is performed *before* asking the question whether the ZIP code
is valid. This only makes sense.

In C (and its derived languages), this logic is expressed as follows:

    do
    {
      ask for a ZIP code
    } while (ZIP code is not valid);

It doesn't seem very different. Instead of "repeat", we use "while", and
we use "while" to end the construct instead of "until". However, a
closer look reveals a major difference. In the repeat version, the
condition is "the ZIP code is valid". However, in the do-while version,
the condition is "the ZIP code is *not* valid".

In other words, a repeat-until loop specifies an exit condition (when
true, exit). A do-while loop, however, specifies a do-it-again condition
(when true, do it again).

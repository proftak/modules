---
title: "Module 0279: Boolean Operator"
---

# About this module

-   Prerequisites:

-   Objectives: This module reviews the concept of boolean operators,
    already introduced in beginning programming classes.

# Boolean operators, in general

An operator, in general, is an operation that requires at least one
value, and the operation produces its own value.

A *Boolean* operator is one that uses and produces a Boolean value. A
Boolean value is one that is true or false. In C/C++, any scalar value
that is non-zero is considered true in the context of Boolean values,
and any scalar value of zero (including a NULL address) is considered
false (not true).

# Common C/C++ Boolean Operators

Some Boolean operators are supplied in almost all programming languages.
These are also the ones that we tend to use in natural languages.

## Conjunction

Conjunction is known as the English word "and". The mathematical symbol $\wedge$ represents conjunction. This is a Boolean
operator described by the following truth table:

|x|y|$x \wedge y$|
|-|-|------------|
|0|0|       0|
|0|1|       0|
|1|0|       0|
|1|1|       1|

A few explanations is needed here. First, the symbol $0$ (normally known
as zero) means false, and the symbol $1$ (normally known as one) means
true.

In this table, $x$ and $y$ are *independent* variables. This means that
their values do not depend on each other. The rightmost column is the
value of the conjunction $x \wedge y$ *given* that $x$ and $y$ have the
respective values of the corresponding columns on the same row.

In Boolean algebra, especially in the context of computer engineering or
electrical engineering, it is common to use the arithmetic
multiplication operator to represent conjunction. This means the
following C/C++ expression

`x && y`

is officially represented in math as

$x \wedge y$

but it is often simplified to

$x \cdot y$

or even just

$xy$

in engineering documents.

## Disjunction

Disjunction is known as "or" in English (*not* exclusive or, either or).
We will use the concise truth table to define it:

|  x | y | $x \vee y$|
|---|---|------------|
|  0 | 0 |     0|
|  0 | 1 |     1|
|  1 | 0 |     1|
|  1 | 1 |     1|

Disjunction is often represented by the arithmetic addition operator for
ease of entry in engineering applications. This means the following
C/C++ expression

`x || y`

is officially represented in math as

$x \vee y$

but it is often simplified to

$x + y$


in engineering documents.

## Negation

Negation is known as "not" in English. Since it is a unary operator
(unlike the previous two binary operators), it has a simple truth table
as follows:

| x | $\neg x$  |
|---|----------|
| 0 |    1     |
| 1 |    0     |

In engineering documents, negation is often represented by an overbar.
But that is difficult to type. As a result, the forward slash symbol `/`
is often used to mean negation, especially in digital circuit design.

The following C/C++ expression

`!x`

is officially represented in math as

$\neg x$

but it traditionally represented as

$\overline{x}$

in engineering documents, but it is typically represented as follows in
digital circuits

$/x$

Because the slash symbol (`/`) means division in most programming
languages, this can cause a bit of confusion to computer science
students. The overbar representation is not easy to type in a ordinary
editor. This is why the C/C++ method is accepted in this class.

# Other operators

Besides the common operators, there are other Boolean operators that are
useful.

## NAND negated-and

Negated and is just that, negating the result of an and. Note that the
up arrow symbol ($\uparrow$) represents nand. This means
$x \uparrow y = \neg(x \wedge y)$.

Nand is an interesting Boolean operator because it can emulate other
Boolean operators. Let's check this out!

-   $\neg x = x \uparrow x$, this handles negation.

-   $x \wedge y = (x \uparrow y) \uparrow (x \uparrow y)$, this handles
    regular conjunction.

-   $x \vee y= (x \uparrow x) \uparrow (y \uparrow y)$, this handles
    disjunction.

Of course, the big question is how we know all of these alternative
definitions of common Boolean operators using nand are correct. I am
leaving this as an exercise.

## Implies

Implication has its own Boolean operator. $x \Rightarrow y$ means $x$
implies $y$. The implication *itself* can be true or false.

Mechanically, implication can be defined using other Boolean operators,
$x \Rightarrow y = \neg x \vee y$. As such, it is easy to understand its
truth table:

| x | y | $x \Rightarrow y$ |
|---|---|-------------------|
| 0 | 0 |         1 |
| 0 | 1 |         1 |
| 1 | 0 |         0 |
| 1 | 1 |         1 |

Semantically, however, it may be a little confusing. Normally, in just
about any natural language, implication is not considered a Boolean
operator lumped with "and", "or', "not". When we say "studying hard
implies better grades", it is considered an assertion of the
implication!

Now let us take a look at a absurd (it works only because it is absurd!)
implication:

"A blue cat is sick implies tomorrow is Doom's day."

This implication statement itself has a true/false value. Let us
consider all four possibilities.

-   "A blue cat is sick", "tomorrow is Doom's days." This pairing
    confirms the implication, the implication is true.

-   "It is not the case that a blue cat is sick", "tomorrow is not
    Doom's day". The implication is still true because it does not say
    anything about what happens when "a blue cat is sick" is not true!

-   "it is not the case that a blue cat is sick", "tomorrow *is* Doom's
    day". The implication is still true because it does not suggest
    anything when "a blue cat is sick" is false.

-   "A blue cat is sick" and "tomorrow is not Doom's day", in this case,
    the implication itself is false.

Sure, we can always use $\neg x \vee y$ instead of $x \Rightarrow y$ in
terms of correctness. However, because implication has such importance
in proofs, it is often handy to represent implication as its own Boolean
operator.

## Equivalence

Equivalence, as a Boolean operator, means the two sides are the same.
Technically, $x$ is equivalent to $y$ is represented as
$x \Leftrightarrow y$. Semantically, it is defined as
$x \Leftrightarrow y = (x \Rightarrow y) \wedge (y \Rightarrow x)$.

The truth table of equivalence is as follows:

| x | y | $x \Leftrightarrow y$ |
|---|---|-----------------------|
| 0 | 0 |           1 |
| 0 | 1 |           0 |
| 1 | 0 |           0 |
| 1 | 1 |           1 |


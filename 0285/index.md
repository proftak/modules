---
title: "Module 0285: Quantifiers"
---

# About this module

-   Prerequisites: [0279](../0279),[0280](../0280)

-   Objectives: This module explores the basics of quantifiers.

# The basics

Quantifiers implicitly apply to everything (or nothing) in the universe.
To make our discussion more concise, let us use variable $x$ to refer to
a thing that we are examining, and $P(x)$ as some kind of boolean
function applied to $x$. This means that depending on what $x$ is,
$P(x)$ is either true or false.

To say that everything in the universe makes $P(x)$ true, we use the
following expression:

$\forall x(P(x))$

In English, this is literally "for all $x$ in the universe, $P(x)$ (is
true)." I put "is true" in parentheses because $P(x)$ is a boolean
function, and so referring to it is implicitly saying it is true.

To say that at least one thing $x$ in the universe makes $P(x)$ true, we
use the following expression:

$\exists x(P(x))$

This is literally saying "There exists at least one $x$ in the universe
such that $P(x)$ (is true)."

Note the importance of saying "at least." This means that maybe there
is more than one thing that makes $P(x)$ true. In other words, the
symbol $\exists$ does not imply "one and only one" or "exactly one."

# More complex use of quantifiers with negation

Now that we have covered "all" ($\forall$)and "some" ($\exists$), let's
take a look at some other quantifiers that we use in daily life.

What about "none" or "no"? Let's assume $P(x)$ means $x$ lasts forever.
How do we say "nothing lasts forever"?

$\neg \exists x(P(x))$

Literally, this means "it is not the case that there exists something
$x$ such that $x$ lasts forever." Of course, we know this really just
means that "nothing lasts forever." There is a more clumsy way to say
"nothing lasts forever": "Everything does not last forever."
"Everything" is $\forall$, so we can say the same thing as follows:

$\forall x(\neg P(x))$

Now, when we change the quantifier to "for all" and keep the predicate
$P$ not negated, the statement takes on a different meaning. Let us take
a look at the following statement:

$\neg \forall x(P(x))$

This says "It is not the case that everything $x$ lasts forever." This
simplifies to "not everything lasts forever."

Ah, "not everything lasts forever" means that "something does not last
forever." Since "something" is $\exists$, can't we also say this as
follows:

$\exists x(\neg P(x))$

The answer is *yes*! Indeed,
$\neg \forall x (P(x)) \Leftrightarrow \exists x (\neg
  P(x))$.

# Filtering what the predicate applies to

Broad statements like "nothing lasts forever" are not very useful.
Although "does not last forever" may be useful, we may want to limit
what it applies to with a filter. Unfortunately, the quantifiers by
default apply to everything.

What if we want to say no cars last forever? Let's assume a set $X$
contains all the cars manufactured. This means an element $e$ of $X$ is
a car.

Let us consider the following statement:

$\forall e(e \in X \Rightarrow P(e) )$

This statement says "For each thing $e$ in the universe, if $e$ is a
car, it lasts forever." Essentially, this is the same as "all cars last
forever" (but we don't know, from this statement, whether other things
last forever or not).

As a concrete example, $\forall e(e \in \\{1,2,3\\} \Rightarrow (e < 5))$ is functionally the same as $(1 < 5) \wedge (2 < 5) \wedge (3 < 5)$.

"No car lasts forever" is, in a longer way, "each car does not last
forever." We can now reformulate the statement as follows:

$\forall e(e \in X \Rightarrow \neg P(e))$

Literally, this statement says "For each thing $e$ in the universe, if
$e$ is a car, $e$ does not last forever." This is the same as saying
"every car does not last forever", or "no car lasts forever."

Note that this statement is universally true as long as no car
lasts forever. When $e$ is bound to, say, Tak, then the clause is
automatically true whether Tak lasts forever or not. This is because in
the implication, if $e$ is not a car (an element of $X$), then the
entire implication is true.

In other words, in an implication $P \Rightarrow Q$, $P$ is a filter. If
$P$ is not true, we don't care about $Q$ and the whole implication is
true. On the other hand, if $P$ is true, then we need $Q$ to be also
true for the implication itself to be true.

Because membership filtering is so commonly used, the statement

$\forall e(e \in X \Rightarrow \neg P(e))$

is often shortened to

$\forall e \in X (\neg P(e))$

This kind of filtering also applies to the existential quantifier.
However, the way it works is slightly different.

If we want to limit the predicate $P$ to only apply to elements of the
set $X$ existentially, we can use the following expression:

$\exists e((e \in X) \wedge P(e))$

Note how we used implication in the universal quantifier, but now we use
the conjunction operator in the existential quantifier. This is because
the \"default\" of the universal quantifier for something not in $X$ is
true, but the default of the existential quantifier for something not in
$X$ is false. The above expression is often simplified as follows:

$\exists e \in X (P(e))$

As a concrete example, $\exists e \in \\{1,2,3\\}(e \mod 2 = 0)$ is functionally the same as $(1 \mod 2 = 0) \vee (2 \mod 2 = 0) \vee (3 \mod 2 = 0)$.

# Quantifiers Practice Questions

## Question 1
**Statement:** Express the following in symbolic form: "All cars are fast."

<details>
  <summary>Answer</summary>
  $\forall x(x \in \text{Cars} \Rightarrow \text{Fast}(x))$
</details>

## Question 2
**Statement:** Express the following in symbolic form: "Some birds cannot fly."

<details>
  <summary>Answer</summary>
  $\exists x(x \in \text{Birds} \wedge \neg \text{Fly}(x))$
</details>

## Question 3
**Statement:** Convert the following to natural language: $\forall x(\neg P(x))$

<details>
  <summary>Answer</summary>
  "Nothing in the universe satisfies $P(x)$." or "For all $x$, $P(x)$ is false."
</details>

## Question 4
**Statement:** Express the following in symbolic form: "Not every student in the class passed the exam."

<details>
  <summary>Answer</summary>
  $\neg \forall x(x \in \text{Students} \Rightarrow \text{Passed}(x))$ or $\exists x(x \in \text{Students} \wedge \neg \text{Passed}(x))$
</details>

## Question 5
**Statement:** Express the following in symbolic form: "There exists at least one even number in the set \{1,2,3,4,5\}."

<details>
  <summary>Answer</summary>
  $\exists x(x \in \{1,2,3,4,5\} \wedge x \mod 2 = 0)$
</details>

## Question 6
**Statement:** Convert the following to natural language: $\exists x(\neg P(x))$

<details markdown="1">
  <summary>Answer</summary>
  "There exists at least one $x$ in the universe such that $P(x)$ is false." or "There is something that does not satisfy $P(x)$."
</details>

## Question 7
**Statement:** Express the following in symbolic form: "All humans are mortal."

<details>
  <summary>Answer</summary>
  $\forall x(x \in \text{Humans} \Rightarrow \text{Mortal}(x))$
</details>

## Question 8
**Statement:** Convert the following to natural language: $\neg \exists x(P(x))$

<details>
  <summary>Answer</summary>
  "There does not exist any $x$ in the universe such that $P(x)$ is true." or "Nothing satisfies $P(x)$."
</details>

## Question 9
**Statement:** Express the following in symbolic form: "No prime numbers are even except 2."

<details>
  <summary>Answer</summary>
  $\forall x((x \in \text{Primes} \wedge x \neq 2) \Rightarrow \neg (x \mod 2 = 0))$
</details>

## Question 10
**Statement:** Convert the following to natural language: $\forall x(x \in \text{Natural Numbers} \Rightarrow x \geq 0)$

<details>
  <summary>Answer</summary>
  "All natural numbers are greater than or equal to 0."
</details>


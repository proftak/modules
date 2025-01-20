---
title: "Module 0312: Relations"
---

# About this module

-   Prerequisites: [0280](../0280/mdModule.html),[0285/mdModule.html](../0285/mdModule.html)

-   Objectives: This module introduces relations and the types of
    relations in mathematics.

# What is a relation?

A relation is, technically, *whether* two elements of a set are related
or not. Of course, this really doesn't say much, but that is the whole
point. Let us consider a relation $R$ that is defined over a set $X$.

The first thing that we know is the following:

$R \subseteq (X \times X)$

This means that every element in a relation is a two-tuple, where both
items of the tuple come from the set that the relation is defined over.

From the notation perspective, it is conventional to write "x relates to
y via R" as $xRy$. This is the infix notation of relation. Note that
$xRy$ is not an assertion. It is not saying the x does relate to y, it
is a boolean expression that can be true or false.

There can be many relations defined over the same set.

# A concrete example

The familiar comparison operator, less then $<$, is a relation. It can
defined over any set that is fully ordered, but for now we will only
consider the set of integers, otherwise known as $\mathbb{Z}$.

As an example to illustrate that relation is a set, let's consider the
following statements:

-   $1 < 2$ is true.

-   $(1,2) \in <$ is true.

These statements are equivalent! The first statement is familiar to us
because that is how we see comparison "normally." However, the second
statement asserts the same truth, just expressed slightly differently
viewing a relation (less-than in this case) as a set of two-tuples.

# A random example

Let us define $X = \\{a,b,c,d\\}$. Now we define $R$ as follows:

$R = \\{(a,a), (a,b), (b,c), (d,d), (b,a) \\}$

With this, then we can state the following truths:

-   $aRb$ is true.

-   $(b,c) \in R$ is true.

-   $bRb$ is false.

-   $(d,c) \in R$ is false.

As stated earlier, $R$ is not the only relation that can be defined over
$X$. Because $X \times X$ in this case has 16 elements, the number of
relations that can be defined over $X$ is $2^{16}$. Think of the
presence of each element of $X \times X$ as a bit, we can use a 16-bit
number to represent a relation over $X$. The number of values that can
be represented by a 16-bit number is $2^{16}$ because each bit is
independent from all others, and each bit has 2 values to choose from.

# Special properties of relations

## Reflexive

A relation $R$ over a set $X$ is reflexive if and only if the following
is true:

$\forall e \in X((e,e) \in R)$

Note that the condition has to hold true for every element in the set.
At the same time, there can be elements in $R$ other than the ones
necessary for reflexivity.

## Symmetric

A relation $R$ over a set $X$ is symmetric if and only if the following
is true:

$\forall e,f \in X((e,f) \in R \Leftrightarrow (f,e) \in R)$

This definition is tricky because of the use of "if and only if" (aka
iff). An empty relation, according to this definition, is actually
symmetric!

## Transitive

A relation $R$ over a set $X$ is transitive if and only if the following
is true:

$\forall e,f,g \in X(((e,f) \in R \wedge (f,g) \in R) \Rightarrow (e,g) \in R)$

This definition relies on implication, which also makes it slightly
tricky. Again, an empty relation is also transitive!

## Antisymmetric

A relation $R$ over a set $X$ is antisymmetric if and only if the
following is true:

$\forall e,f \in X(((e,f) \in R) \wedge ((f,e) \in R) \Rightarrow (e=f)))$

This definition is also true for any empty relation.

# Partial ordering

A set $X$ is said to be partially ordered by a relation $R$ if and only
if the following is true:

-   $R$ is reflexive over $X$ and

-   $R$ is antisymmetric over $X$ and

-   $R$ is transitive over $X$.

Partial ordering means $R$ may not be defined for certain pairs of
elements in $X$. As a result, sorting is not possible because there may
not be ordering between certain elements, and as such the position of
such elements in an array cannot be determined.

Such an ordering is not uncommon, especially in casual use of
comparison. For example, let's say "smooth" and "rich" are both
desirable qualities. However, let us also say that between the two, we
cannot weigh whether "smooth" carries more weight than "rich". Now we
can define "more desirable."

"Smooth and rich" is more desirable than "smooth but not rich".

"Smooth and rich" is more desirable than "not smooth but rich".

"Smooth and rich" is more desirable than "not smooth and not rich".

"Smooth and not rich" is more desirable than "not smooth and not rich".

"Not smooth and rich" is more desirable than "not smooth and not rich".

Obviously, "more desirable" does not meet the requirements of a
partially ordered relation! It is definitely not reflexive. Instead of
using "more desirable than", we can use "at least as desirable as".
Let's call this new relation "alada".

Now we can claim the following:

"Smooth and rich" is alada "smooth and rich".

"Smooth and rich" is alada "smooth but not rich".

"Smooth and rich" is alada "not smooth but rich".

"Smooth and rich" is alada "not smooth and not rich".

"Smooth and not rich" is alada "smooth and not rich".

"Smooth and not rich" is alada "not smooth and not rich".

"Not smooth and rich" is alada "not smooth and rich".

"Not smooth and rich" is alada "not smooth and not rich".

"Not smooth and not rich" is alada "not smooth and not rich".

Observe how alada is now reflexive! It is also transitive and
antisymmetric. As a result, alada is relation that partially order the
set of smooth versus rich (4 elements in this set).

Also pay attention to the *lack* of alada relation between "smooth and
not rich" and "not smooth and rich".

# Total ordering

A set $X$ is said to be totally ordered by a relation $R$ if and only if
the following is true:

-   $R$ is reflexive over $X$ and

-   $R$ is antisymmetric over $X$ and

-   $R$ is transitive over $X$ and

-   $R$ is comparable over $X$, meaning that
    $\forall e,f \in X(eRf \vee fRe)$, this is also called the
    "trichotomy law."

You can see that the only difference between partial ordering and total
ordering is the last item, known as comparability. Furthermore, any
totally ordering relation is also automatically partial ordering.

Elements in a set $X$ that is totally ordered by a relation $R$ can be
linearly sorted by $R$.

# AI-generated questions

[This](https://chatgpt.com/share/66f43157-0cd8-8013-90e7-3296096806ec) is how these questions are generated.

<details>
  <summary><strong>Question 1:</strong> What is a relation over a set?</summary>
  <p>A relation over a set $X$ is a subset of $X \times X$, meaning that it consists of pairs of elements from $X$. A relation specifies whether two elements from the set are related or not.</p>
</details>

<details>
  <summary><strong>Question 2:</strong> How do we express the relation between two elements $x$ and $y$ in infix notation?</summary>
  <p>The infix notation for expressing a relation $R$ between $x$ and $y$ is written as $xRy$. This indicates that $x$ is related to $y$ via the relation $R$.</p>
</details>

<details>
  <summary><strong>Question 3:</strong> Given the set $X = \{1, 2, 3\}$ and a relation $R = \{(1, 2), (2, 3)\}$, is $R$ reflexive?</summary>
  <p>No, $R$ is not reflexive because the reflexive property requires that $(1,1), (2,2), (3,3) \in R$, which is not the case here.</p>
</details>

<details>
  <summary><strong>Question 4:</strong> For the same set $X = \{1, 2, 3\}$ and relation $R = \{(1, 2), (2, 1)\}$, is $R$ symmetric?</summary>
  <p>Yes, $R$ is symmetric because for every $(x, y) \in R$, the pair $(y, x) \in R$. For example, since $(1, 2) \in R$, we also have $(2, 1) \in R$.</p>
</details>

<details>
  <summary><strong>Question 5:</strong> What does it mean for a relation $R$ to be transitive?</summary>
  <p>A relation $R$ is transitive if for all $e, f, g \in X$, whenever $(e, f) \in R$ and $(f, g) \in R$, it implies that $(e, g) \in R$.</p>
</details>

<details>
  <summary><strong>Question 6:</strong> Is the empty relation reflexive, symmetric, and transitive?</summary>
  <p>The empty relation is symmetric and transitive but not reflexive. Reflexivity requires that $(x, x) \in R$ for every $x \in X$, which cannot be true in an empty relation. However, it is trivially symmetric and transitive because there are no counterexamples.</p>
</details>

<details>
  <summary><strong>Question 7:</strong> What additional condition distinguishes a totally ordered set from a partially ordered set?</summary>
  <p>A totally ordered set requires that for all elements $e$ and $f$ in the set, either $eRf$ or $fRe$ holds. This is called the trichotomy law, ensuring that every pair of elements is comparable.</p>
</details>

<details>
  <summary><strong>Question 8:</strong> Is the relation $<$ (less than) on the set of integers $\mathbb{Z}$ a total order?</summary>
  <p>The AI answers: Yes, the relation $<$ is a total order on $\mathbb{Z}$ because it is reflexive, antisymmetric, transitive, and comparable for all integers. For any $a, b \in \mathbb{Z}$, either $a < b$, $b < a$, or $a = b$.</p>
  <p>But ChatGPT is wrong. $<$ is not reflexive because an integer is not less than itself. As a result, $<$ is not a total order!</p>
</details>

<details>
  <summary><strong>Question 9:</strong> Define antisymmetry in terms of a relation $R$ over a set $X$.</summary>
  <p>A relation $R$ over a set $X$ is antisymmetric if for all $e, f \in X$, whenever $(e, f) \in R$ and $(f, e) \in R$, it implies that $e = f$.</p>
</details>

<details>
  <summary><strong>Question 10:</strong> Consider the set $X = \{a, b\}$ and the relation $R = \{(a, a), (b, b)\}$. Is this relation a partial order?</summary>
  <p>Yes, $R$ is a partial order because it is reflexive (both $(a, a)$ and $(b, b)$ are in $R$), antisymmetric (no $(a, b)$ or $(b, a)$ pairs exist that would violate antisymmetry), and transitive (if there were any pairs $(a, b)$ and $(b, c)$, the condition for transitivity would be satisfied, but no such pairs exist).</p>
</details>


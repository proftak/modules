---
title: "Module 0288: Set notations defined using quantifiers"
---

# About this module

-   Prerequisites: [0280](../0280/mdModule.html), [0285](../0285/mdModule.html)

-   Objectives: Set theory using quantifiers

# Rationale

Although basic set theory was already discussed in module
[0280](../0280/mdModule.html), that was discussed without the use of quantifiers.
Quantifiers are useful tools for a variety of math topics, set theory is
a part of those topics. By reexamining basic set theory, we reinforce
the understanding of both set theory as well as quantifiers.

# Equality

Given two items, $x$ and $y$, how do we know they are the same? In order
words, how do we evaluate $x=y$?

First of all, if one is a set and other is not, then $x=y$ is false.

Given that $x$ and $y$ are not sets, then the "normal" comparison
applies.

Given that $x$ and $y$ are sets, then we can say the following:

$(x=y) \Leftrightarrow ((\forall e \in x(e \in y)) \wedge (\forall e \in y(e \in x)))$

There is a more concise statement that states the same:

<span id="setEquality">$(x=y) \Leftrightarrow (\forall e((e \in x) \Leftrightarrow (e \in y)))$</span>

# Set description

Recall the notation $E=\\{x|P(x)\\}$ describes a set $E$ where all its
elements make the predicate $P$ true. We mentioned how this means
$x \in E \Leftrightarrow
  P(x)$ in module [0280](../0280). The more correct statement is as
follows:

$\forall x(x \in E \Leftrightarrow P(x))$

This makes it clear where we get (how we bind) the value of the variable
to some "thing." $x$ can be anything in the universe! Without the
quantifier $\forall$, one can ask the question where do we get a value
for $x$ to be evaluated.

# The empty set

How do we know that a set $S$ is empty?

$\neg \exists x(x \in S)$

This literally says "there does not exist a thing $x$ such that $x$ is
in $S$."

# Intersection and Union

$\forall x((x \in (A \cap B)) \Leftrightarrow (x \in A \wedge x \in B))$

and

$\forall x((x \in (A \cup B)) \Leftrightarrow (x \in A \vee x \in B))$

# Cartesian product

$\forall x \in A(\forall y \in B((x,y) \in (A \times B))) \wedge \forall (x,y) \in A \times B(x \in A \wedge y \in B)$

# Subset

$A \subseteq B \Leftrightarrow \forall e \in A(e \in B)$

$A \subset B \Leftrightarrow (A \subseteq B \wedge \exists x \in B(\neg x \in A))$

# AI-generated questions

<details>
  <summary><strong>1. What does it mean for two sets $A$ and $B$ to be equal?</strong></summary>
  <p>Two sets $A$ and $B$ are equal if every element of $A$ is an element of $B$ and every element of $B$ is an element of $A$. In formal terms:</p>
  <p>$$A = B \Leftrightarrow \forall e \in A(e \in B) \wedge \forall e \in B(e \in A)$$</p>
</details>

<details>
  <summary><strong>2. How can you express the empty set using quantifiers?</strong></summary>
  <p>The empty set $S$ can be expressed using quantifiers as follows:</p>
  <p>$$\neg \exists x(x \in S)$$</p>
  <p>This means that there does not exist any element $x$ such that $x$ is in $S$.</p>
</details>

<details>
  <summary><strong>3. How do you represent the intersection of two sets $A$ and $B$ using quantifiers?</strong></summary>
  <p>The intersection of two sets $A$ and $B$ can be represented using quantifiers as:</p>
  <p>$$\forall x((x \in (A \cap B)) \Leftrightarrow (x \in A \wedge x \in B))$$</p>
</details>

<details>
  <summary><strong>4. How do you represent the union of two sets $A$ and $B$ using quantifiers?</strong></summary>
  <p>The union of two sets $A$ and $B$ can be represented using quantifiers as:</p>
  <p>$$\forall x((x \in (A \cup B)) \Leftrightarrow (x \in A \vee x \in B))$$</p>
</details>

<details>
  <summary><strong>5. What does $A \subseteq B$ mean in terms of quantifiers?</strong></summary>
  <p>The statement $A \subseteq B$ means that every element of $A$ is also an element of $B$, and can be expressed as:</p>
  <p>$$A \subseteq B \Leftrightarrow \forall e \in A(e \in B)$$</p>
</details>

<details>
  <summary><strong>6. What does $A \subset B$ mean in terms of quantifiers?</strong></summary>
  <p>The statement $A \subset B$ means that $A$ is a subset of $B$ but $A$ is not equal to $B$. It can be expressed as:</p>
  <p>$$A \subset B \Leftrightarrow (A \subseteq B \wedge \exists x \in B(\neg x \in A))$$</p>
</details>

<details>
  <summary><strong>7. How can you describe a set $E$ using quantifiers if the set is defined by a predicate $P(x)$?</strong></summary>
  <p>If a set $E$ is defined by a predicate $P(x)$, you can describe the set using quantifiers as:</p>
  <p>$$\forall x(x \in E \Leftrightarrow P(x))$$</p>
</details>

<details>
  <summary><strong>8. How is the Cartesian product $A \times B$ defined using quantifiers?</strong></summary>
  <p>The Cartesian product of two sets $A$ and $B$ can be defined using quantifiers as:</p>
  <p>$$\forall x \in A(\forall y \in B((x,y) \in (A \times B))) \wedge \forall (x,y) \in A \times B(x \in A \wedge y \in B)$$</p>
</details>

<details>
  <summary><strong>9. What does the statement $x \in E \Leftrightarrow P(x)$ mean in terms of set notation and quantifiers?</strong></summary>
  <p>The statement $x \in E \Leftrightarrow P(x)$ implies that $E$ is the set of all $x$ such that $P(x)$ is true, and can be formally written as:</p>
  <p>$$E = \{x | P(x)\}$$</p>
  <p>In quantifier form: $$\forall x(x \in E \Leftrightarrow P(x))$$</p>
</details>

<details>
  <summary><strong>10. How would you express the equality of two sets $A$ and $B$ using a single quantifier expression?</strong></summary>
  <p>The equality of two sets $A$ and $B$ can be expressed concisely with the following quantifier expression:</p>
  <p>$$A = B \Leftrightarrow \forall e((e \in A) \Leftrightarrow (e \in B))$$</p>
</details>


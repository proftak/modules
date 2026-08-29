---
title: "Module 0280: Basic Set Notations"
---

# About this module

-   Prerequisites: [0279](../0279)

-   Objectives: This module introduces basic set theory based on basic
    Boolean operators.

# A set and its elements

A "set" is a containment of "elements". The most basic concept of set
theory is the concept of a set containing, or not containing, a
particular element. An element can be just about anything that can
establish uniqueness. In other words, given two values that may be
elements, we need to be able to compare and see if they are the same
value or not.

Note that ordering is not needed of values that can be elements. This
means there is no need to determine which value is greater. Just knowing
whether a value is the same as another value is sufficient. This brings
us to another property of a set.

Elements in a set are not ordered. There is no inherent order of
elements in a set.

The last important concept of a set is that elements in a set must be
unique. This means the same value cannot be represented more than once
in a set.

Now let us introduce some symbols. Typically, though not required, a set
is represented by an uppercase letter. Elements in a set are enclosed by
braces and separated by commas. For example, the following is a set of a
few numbers: $T=\\{12,5,2.2,7,-1,10\\}$.

Using this set as an example, we can illustrate the use of the
"element-of" operator. This operator returns a value that is true or
false. For example, $2.2 \in T$ (read "2.2 is in $T$") is true. On the
other hand $23 \in T$ is false.

## Food for thought

How would you implement the concept of a set in C/C++? If you know ahead
of time a set is to only contain integer values, how would you implement
a set? How do you check whether a value is an element of a set? How do
you place elements into a set?

# Equivalence of sets

A set can be compared to another set to see if they are the same. At
this point, we lack the precise mathematical notation for this kind
discussion, but we can still utilize English for the most part.

Let's say we are interested in whether set $S$ and $T$ are the same. The
two sets are considered the same when every element in $S$ is in $T$ and
every element in $T$ is in $S$. If this requirement is satisfied, then
we say $S=T$.

# A set as an element of another set

Recall that to qualify as a potential element, a value must be
comparable to other values to determine whether they are the same or
not. In the previous section, we just established that a set can be
compared to another set to see if they are the same.

In general, given two values $x$ and $y$, knowing that $x$ is a set,
this is how we can determine whether $x=y$ is true or not:

-   if $y$ is not a set, then $x=y$ is false

-   if $y$ is also a set, then we use the set comparison method in
    section [3](#section:setEq){reference-type="ref"
    reference="section:setEq"} to determine whether $x=y$.

Now that we can compare a set with anything for equality, it is not
surprising that a set can be an element of another set! For example,
$X=\\{a,b,\\{1,2,3\\}\\}$ is a set that has one of its elements being a set
itself. As a result, in this case, $\\{1,2,3\\} \in X$ is true.

# Sets with an infinite number of elements

There are many useful sets with infinite elements. For example, the
symbol $\mathbb{Z}$ refers to the set of integers, while the symbol
$\mathbb{R}$ refers to the set of real numbers.

The set of all even integers is also a set of infinite elements. But how
do we express it? Let's say we want to call this set $E$.

First, we can try the "list by example" method:
$E=\\{\dots, -4, -2, 0, 2, 4, \dots\\}$. While most people understand this notation, it is not a very precise way of stating a set of all
even numbers. In this case, someone can easily think that the next
elements to the left and right are $-8$ and $8$.

The following notation can be used as a precise method to describe a set
of even numbers: $E=\\{x|(x \in \mathbb{Z}) \wedge (x \mod 2 = 0)\\}$.
This notation literally says "something $x$ is an element of set $E$ if
and only if $x$ is an element of the set of integers and $x$ divided by
2 has a remainder of 0." The use of "if and only if" instead of "if" or
"only if" is very important here!

In general, if we consider $P(x)$ as a general predicate $P$ on $x$ as a
function that returns true or false based on $x$, then

$$E=\{x|P(x)\}$$

means exactly the same as

$$x\in E \Leftrightarrow P(x)$$

Let us generalize this to the following example: $X=\\{e|P(e)\\}$. In this
notation, $P(e)$ is called a predicate on $e$, it is some kind of
Boolean expression parametrized by $e$. Given that $P$ is a predicate,
this notation says the following: $P(x) \Leftrightarrow x \in X$.

This means that any value that makes $P$ true must be an element of set
$X$. Any value that makes $P$ false must not be an element of set $X$.
You an also interpret this as every element in $X$ must make $P$ true,
and every value that is not an element of $X$ must make $P$ false.

# A set with no elements

A set with no elements is called, no surprisingly, an empty set. While
there are many representations of an empty set, we will use the one that
is the most intuitive: $\\{\\}$.

# Set operators

A set can relate to another set via some operators.

The first operator we will define is the intersection operator. Given
that $A$ and $B$ are both sets, the intersection is $A \cap B$. The
definition of an intersection is as follows:

$$A \cap B = \{e|(e \in A) \wedge (e \in B)\}$$

Recall that this notation means exactly the same as follows:

$$(e \in (A \cap B)) \Leftrightarrow ((e \in A) \wedge (e \in B))$$

Of course, in English, this is rather simple to explain: an element is
in the intersection of two sets if and only if the element is found in
both sets. Note that "if and only if" means the same thing as "is
equivalent to."

The next operator is the union operator. We will go straight to the
definition:

$$A \cup B = \{e | (e \in A) \vee (e \in B)\}$$

In other words, an element is in the union of two sets if it is in at
least one of the two sets. Note that we are simply using "or", but not
"either or"!

A less commonly use but also important operator is difference.

$$A-B = \{e | (e \in A) \wedge \neg(e \in B)\}$$

This means an element is in the difference between two sets if it is in
the first set and not in the second. This operator, unlike union and
intersection, is not commutative.

An apparently not-too-useful operator is the Cartesian product operator.
This operator is defined as follows (assuming $A$ and $B$ are sets):

$$A \times B = \{(x,y)|(x \in A) \wedge (y \in B)\}$$

This is the first time we encounter the notion of a tuple. In the
definition, the term $(x,y)$ is a 2-tuple. A tuple is a container, but
it is ordered and may have duplicate values. As a result, in our
definition of the Cartesian product, each element of the Cartesian
product is a 2-tuple. Furthermore, the first item of each tuple must be
an element of the first set $A$, and the second item of each tuple must
be an element of the second set $B$.

Now we can also define some set operators that return true or false.

We can start with the "subset of" operator, defined as follows:

$$(A \subseteq B) \Leftrightarrow (((A-B) = \{\}) \wedge (A\cap B = A))$$

This means that $A$ is a subset of ($\subseteq$) $B$ if and only if
no elements are in $A$ but not in $B$. That, in return,
is saying that everything in $A$ should be in $B$ as well.

You can see how a set is always its own subset because $A-A=\\{\\}$ for
any set $A$. Sometimes, expressing that a set is a
"proper subset" of another set is important. This is defined as follows:

$$A \subset B \Leftrightarrow (A \subseteq B) \wedge (B-A \neq \{\})$$

This means that in order for $A$ to be a proper subset of ($\subset$) of
$B$, $A$ must be a subset of $B$, and there has to be at least one
element in $B$ that is not in $A$.

Many times, we are interested in the number of elements in a set $X$.
The notation $|X|$ is called the cardinality of $X$, which is
essentially the number of elements in $X$. For example
$|\\{2,4,6,8\\}|=4$.

# Set Notation Questions

<details>
  <summary>1. Basic Concepts of Sets</summary>
  What are the three fundamental properties of a set that distinguish it from other data structures?
  <details>
    <summary>Answer</summary>
    The three fundamental properties of a set are:
    1. Elements are unique: No duplicates are allowed.
    2. No inherent order: The elements do not have a specific sequence.
    3. Membership: The set contains or does not contain a specific element.
  </details>
</details>

<details>
  <summary>2. Element of a Set</summary>
  Given the set $S = \{3.1, 5, -7, 9, 12\}$, determine whether the statement $5 \in S$ is true or false. Explain your reasoning.
  <details>
    <summary>Answer</summary>
    The statement $5 \in S$ is true because the number $5$ is one of the elements in the set $S$.
  </details>
</details>

<details>
  <summary>3. Equivalence of Sets</summary>
  Explain how to determine whether two sets $A$ and $B$ are equal. Provide an example with two small sets.
  <details>
    <summary>Answer</summary>
    Two sets $A$ and $B$ are equal if every element in $A$ is also in $B$, and every element in $B$ is also in $A$. For example, if $A = \{1, 2, 3\}$ and $B = \{3, 1, 2\}$, then $A = B$ because both sets contain exactly the same elements.
  </details>
</details>

<details>
  <summary>4. Set as an Element</summary>
  Consider the set $X = \{a, b, \{1, 2, 3\}\}$. Is the statement $\{1, 2, 3\} \in X$ true or false? Justify your answer.
  <details>
    <summary>Answer</summary>
    The statement $\{1, 2, 3\} \in X$ is true because the set $\{1, 2, 3\}$ is one of the elements in the set $X$.
  </details>
</details>

<details>
  <summary>5. Infinite Sets</summary>
  Express the set of all odd integers using the precise set notation discussed in the material.
  <details>
    <summary>Answer</summary>
    The set of all odd integers can be expressed as $O = \{x \mid x \in \mathbb{Z}, x \mod 2 \neq 0\}$, where $\mathbb{Z}$ represents the set of all integers.
  </details>
</details>

<details>
  <summary>6. Empty Set</summary>
  What is the symbol for an empty set, and what is its significance in set theory?
  <details>
    <summary>Answer</summary>
    The symbol for an empty set is $\{\}$ or sometimes $\emptyset$. It signifies a set that contains no elements.
  </details>
</details>

<details>
  <summary>7. Intersection of Sets</summary>
  Given two sets $A = \{1, 2, 3, 4\}$ and $B = \{3, 4, 5, 6\}$, find $A \cap B$ and explain what the result represents.
  <details>
    <summary>Answer</summary>
    The intersection $A \cap B$ is $\{3, 4\}$. This result represents the elements that are common to both sets $A$ and $B$.
  </details>
</details>

<details>
  <summary>8. Union of Sets</summary>
  Find the union $A \cup B$ of the sets $A = \{x, y\}$ and $B = \{y, z\}$. What does the result signify?
  <details>
    <summary>Answer</summary>
    The union $A \cup B$ is $\{x, y, z\}$. This result signifies all elements that are in either set $A$ or set $B$, or in both.
  </details>
</details>

<details>
  <summary>9. Difference of Sets</summary>
  Calculate the difference $C - D$ for the sets $C = \{10, 20, 30\}$ and $D = \{20, 40\}$. What does the difference operator tell us about these two sets?
  <details>
    <summary>Answer</summary>
    The difference $C - D$ is $\{10, 30\}$. This result tells us the elements that are in set $C$ but not in set $D$.
  </details>
</details>

<details>
  <summary>10. Subset and Proper Subset</summary>
  Explain the difference between a subset and a proper subset. Provide an example of a set $E$ and a subset $F$ where $F$ is a proper subset of $E$.
  <details>
    <summary>Answer</summary>
    A subset $F$ of $E$ means that every element in $F$ is also in $E$. A proper subset $F$ of $E$ means that $F$ is a subset of $E$, and there is at least one element in $E$ that is not in $F$. For example, if $E = \{1, 2, 3\}$ and $F = \{1, 2\}$, then $F$ is a proper subset of $E$.
  </details>
</details>

---
title: "Module 0289: Functions as Sets"
---

# About this module

-   Prerequisites: [0288](../0288/mdModule.html)

-   Objectives: This module explores how a "function" can be seen as a
    set.

# Tuples

In order to describe a function as a set, we need to utilize the concept
of tuples. In module [0280](../0280/mdModule.html), we discussed how each element of
the Cartesian product of two sets is a 2-tuple.

A tuple, in general, is an ordered container where its components are
ordered, and the ordering is significant. Furthermore, a tuple can
contain duplicate items. The tuple $(1,1,2)$ is considered distinct from
the tuple $(1,2,1)$ even though the two tuples share the same
components.

A tuple is represented by a comma-separated list of items, enclosed in
parentheses. For example, $(a,b,c)$ is a 3-tuple. Because the concept of
a tuple is very similar to the concept of an array, we borrow notations
from array operations. Given that $T$ is a tuple, we can use $T[i]$ to
specify the $i$th item of the tuple. Like arrays in programming, this
class will start indices with 0 (not 1).

We will also borrow the cardinality notation of set theory to specify
the size of a tuple. If $T$ is a tuple, then $|T|$ specifies the number
of items in the tuple.

# Functions

We learn functions in other math contexts. In CISP440, functions are an
important concept to facilitate the discussion of many other topics. In
a typical class, we learn that a function $f$ is much like a macro. For
example, we can define a simple function $f(x)=2x$. This way, $f(2)=4$
and etc.

In this class, we look at a function as a "map" that maps elements from
a *domain* set to a *codomain* set. In some other math classes, the word
"range" is used, it means the same as "codomain."

When we describe a function in this class, it is important to identify
the domain and codomain. Let us examine the following declaration:

$f:X \rightarrow Y$

This declaration identifies that $f$ is a function that maps elements
from the domain $X$ to the codomain $Y$.

Unlike many other math classes, we also view a function as a set. A
function is a set of 2-tuples. Let us consider a concrete example and
reuse the example above $f(x)=2x$.

First, we have to identify the domain. Let's say we are only interested
in integers. The set of integers is known as $\mathbb{Z}$. The codomain
is a little tricky, let us assume the codomain is also $\mathbb{Z}$.

In other words, $f:\mathbb{Z} \rightarrow \mathbb{Z}$.

But how do we see this as a set? Let's see whether the following helps
to explain this:

$$f=\{(0,0), (1,2), (2,4), (3,6), \dots\}$$

However in this notation, it is not clear whether negative integers are
included in the domain. Let's try the following:

$$f=\{(x,2x) | x \in \mathbb{Z}\}$$

Recall that this means the following:

$\forall x \in \mathbb{Z}(\forall y \in \mathbb{Z} ((y=2x) \Leftrightarrow ((x,y) \in f)))$

## What makes a function a function?

You probably recognize that given that a function $f: X \rightarrow Y$,
meaning that $f$ is a function mapping elements of domain $X$ to
codomain $Y$, the following must be true:

$f \subseteq X \times Y$

Indeed, $f$, as a set, must be a subset of the Cartesian product of the
domain $X$ and the codomain $Y$.

In addition to this observation, however, there is another important
criterion for a subset of $X \times Y$ to be a function. In English
terms, "each element of the domain must be mapped to one and only one
element in the codomain."

I am certain that most people understand the English version of this
description. It is a good exercise to come up with simple domains and
codomains, then construct subsets that are functions and non-functions.

However, English, like all natural languages, is not exactly precise
when it comes to mathematical concepts. It is best, therefore, to
re-express the criterion in a much more precise (and concise)
mathematical way. We can start with examining whether to use the
*universal* quantifier $\forall$ or the *existential* quantifier
$\exists$.

Because the criterion is to be applied to every element in the domain,
the universal quantifier is needed. If the requirement only needs to
apply to at least one element, then the existential quantifier is used.

So now we know the statement should look something like the following:

$\forall e \in X(P(e))$

Next, we need to figure out how to express the predicate $P$. $P(e)$
needs to express the fact that this element $e$ maps to one and only one
element in the codomain.

This implies some kind of counting is needed. The cardinality operator
is great for this purpose. We can now make our statement a little more
concrete:

$$\forall e \in X(|\dots| = 1)$$

In other words, we are now shifting our attention to constructing a set
where its cardinality counts the number of things that the element $e$
maps to. Since $e$ is "bound" to a particular element in $X$ at this
point, we do not need to worry about choosing which element in the
domain. We focus on what element or elements it maps to in the codomain.

Given that $e$ is an element of $X$, how do we know its mapping into
$Y$? Since $f \subseteq X \times Y$, each element of $f$ is a mapping
from one element in $X$ to an element in $Y$. We now need a way to
constrain to just elements that $e$ maps to.

In other words, the set that we are trying to construct looks like the
following:

$$\{(e,q)|\dots\}$$

This constrains the elements in this "ad hoc" set to be two-tuples, and
each two-tuple starts with the specific element $e$ in $X$. We need a
second constrain because we are only interested in tuples that are in
$f$, so the set is spelled out as follows:

$$\{(e,q)|((e,q) \in f)\}$$

Now that we have the ad hoc set constructed, we can plug it back into
the quantified statement. The final answer is, therefore:

$$\forall e \in X \bigl(\left|\{(e,q)|((e,q) \in f)\} \right| = 1 \bigr)$$

## Why is the concept of a function useful?

We encounter functions in other math classes like sine, cosine,
logarithmic, exponent and etc. Of course, these functions are extremely
useful in science such as physics because they model the relationship of
quantities in real life.

In this class, CISP440, functions are much more "arbitrary" in the sense
that a function may not model the relationship between real-life
quantities. Instead, a function can be used as a tool to express
statements.

Let us consider the following example: how do we express an algorithm is
sorting an array correctly?

First, it is important to remember the values of each element prior to
the execution of a sorting algorithm. We may assume the following
initial condition of the execution of an algorithm:

$$\forall i \in \{0..|a|-1\} (a[i] = k_i)$$

In other words, for element $i$ of array $a$, the initial value is the
constant $k_i$.

A sorting algorithm can change the values of elements of an array. It is
easy to come up with one criterion of a sorted array:

$$\forall i \in \{0..|a|-2\} (a[i] \le a[i+1])$$

But this is not the *only* needed condition! Otherwise, an algorithm can
simply rewrite all elements to 0 to meet this criterion. We need to make
sure that each original value of the array element is found in the sorted
array. This is why the function may come in handy. Let us define a
function $f: \\{0..|a|-1\\} \rightarrow \\{0..|a|-1\\}$. We can then add the
additional criterion:

$$\forall i \in \{0..|a|-1\}(a[i] = k_{f(i)})$$

However, this criterion by itself is not sufficient because the function
can map everything to a single index, like 0! In order for this second
criterion to work, we need to specify the function $f$ to be
"one-to-one". This topic will be discussed in detail in another module.

# AI-generated questions and answers

You can [view the actual ChatGPT prompt](https://chatgpt.com/share/46091f1e-6132-4a2b-88eb-ec23106dd619).


<details>
  <summary><strong>Question 1:</strong> Given the domain X = {1, 2, 3} and codomain Y = {a, b, c}, is the set f = {(1, a), (2, b), (3, c)} a function?</summary>
  <p><strong>Answer:</strong> Yes, this is a function. Each element in the domain X is mapped to exactly one element in the codomain Y, satisfying the condition of a function.</p>
</details>

<details>
  <summary><strong>Question 2:</strong> Given the domain X = {1, 2, 3} and codomain Y = {a, b, c}, is the set f = {(1, a), (2, b), (2, c)} a function?</summary>
  <p><strong>Answer:</strong> No, this is not a function. The element 2 in the domain is mapped to two different elements in the codomain (b and c), which violates the definition of a function.</p>
</details>

<details>
  <summary><strong>Question 3:</strong> If X = {x1, x2} and Y = {y1, y2, y3}, is the set f = {(x1, y1), (x2, y2)} a function?</summary>
  <p><strong>Answer:</strong> Yes, this is a function. Each element in the domain X is associated with exactly one element in the codomain Y.</p>
</details>

<details>
  <summary><strong>Question 4:</strong> Is the set f = {(a, 1), (b, 1), (c, 2)} with domain X = {a, b, c} and codomain Y = {1, 2} a function?</summary>
  <p><strong>Answer:</strong> Yes, this is a function. Each element in the domain X is mapped to one element in the codomain Y. It is acceptable that different elements in X map to the same element in Y (in this case, both a and b map to 1).</p>
</details>

<details>
  <summary><strong>Question 5:</strong> If X = {p, q, r} and Y = {1, 2}, is the set f = {(p, 1), (q, 1), (r, 1), (r, 2)} a function?</summary>
  <p><strong>Answer:</strong> No, this is not a function. The element r in the domain is mapped to both 1 and 2, violating the rule that each element of the domain must map to only one element in the codomain.</p>
</details>

<details>
  <summary><strong>Question 6:</strong> Consider X = {x1, x2, x3} and Y = {y1, y2}. Is the set f = {(x1, y1), (x2, y2)} a valid function if the domain is X and the codomain is Y?</summary>
  <p><strong>Answer:</strong> No, this is not a valid function because not every element of the domain X is mapped to an element in Y. The element x3 in X is not assigned a value.</p>
</details>

<details>
  <summary><strong>Question 7:</strong> Given X = {a, b, c} and Y = {1, 2, 3}, is the set f = {(a, 1), (b, 2), (c, 3), (d, 4)} a function?</summary>
  <p><strong>Answer:</strong> No, this is not a valid function because element d in the tuple (d, 4) is not part of the domain X. All elements in the set of tuples must have their first component in the domain.</p>
</details>

<details>
  <summary><strong>Question 8:</strong> If X = {1, 2, 3} and Y = {a, b}, is the set f = {(1, a), (2, a), (3, a)} a function?</summary>
  <p><strong>Answer:</strong> Yes, this is a function. Each element in the domain X is mapped to exactly one element in the codomain Y, and it's fine for all elements in the domain to map to the same element in the codomain.</p>
</details>

<details>
  <summary><strong>Question 9:</strong> Is the set f = {(1, 2), (2, 3), (3, 4)} with domain X = {1, 2, 3} and codomain Y = {2, 3, 4} a function?</summary>
  <p><strong>Answer:</strong> Yes, this is a function. Each element in the domain X is mapped to exactly one element in the codomain Y.</p>
</details>

<details>
  <summary><strong>Question 10:</strong> Given the domain X = {a, b} and codomain Y = {1, 2, 3}, is the set f = {(a, 1), (b, 2), (b, 3)} a function?</summary>
  <p><strong>Answer:</strong> No, this is not a function because element b in the domain X is mapped to both 2 and 3 in the codomain Y, which violates the requirement of a function.</p>
</details>


---
title: "Module 0290: Injection, Surjection and Bijection"
---

# About this module

-   Prerequisites: [0289](../0289/mdModule.html)

-   Objectives: This module explores categories of functions known as
    injection, surjection, and bijection, as well as the implications of
    these categories.

# Injection

An injective function, aka an injection, has each element of the domain
mapped to a unique element in the codomain. Let us assume the function
of interest is $f: X \rightarrow Y$. Then an injection has the following
additional property (this statement is true):

$\forall p \in X(\forall q \in X((p \ne q) \Rightarrow f(p) \ne f(q)))$

Or it can also be stated as follows counting the number of elements in
the domain that can map to an element in the codomain:

$$\forall q \in Y(|\{(p,q)|(p,q) \in f\}| \le 1)$$

Let's examine some examples where $f: \\{a,b\\} \rightarrow \\{1,2,3\\}$:

-   $f=\\{(a,2), (a,1)\\}$: this set $f$ is not even a function!

-   $f=\\{(a,1), (b,1)\\}$: two things maps to 1, leaving the other
    element in $X$.

-   $f=\\{(a,1), (b,2)\\}$: this is injective despite having an element in
    Y that is not used.

# Surjection

A surjective function, aka a surjection, is a function where every
element in the codomain is mapped to. The following statement is true
for a surjection $f: X \rightarrow  Y$ in addition to the requirement of
being a function:

$\forall q \in Y(\exists p \in X(f(p)=q))$

Or alternatively, by counting:

$$\forall q \in Y(|\{(p,q)|(p,q) \in f\}| \ge 1)$$

Let's re-examine the assumption that $f: \\{a,b\\} \rightarrow \\{1,2,3\\}$.
Well, any function $f$ like this cannot be surjective! This is because
there are more elements in the codomain than there are elements in the
domain. In order for $f$ to be a function, each element in the domain
must map to one and only one element in the codomain!

We can change our domain so that $f: \\{a,b\\} \rightarrow \\{1,2\\}$. Now
we can examine a few examples:

-   $f=\\{(a,1),(b,2)\\}$ is surjective.

-   $f=\\{(a,1),(b,1)\\}$ is not surjective.

# Bijection

A bijective function, aka a bijection, is a function that is both
injective and surjective.

In other words, for a function $f: X \rightarrow Y$, we want

$$\forall q \in Y(|\{(p,q)|(p,q) \in f\}| \le 1)$$

and

$$\forall q \in Y(|\{(p,q)|(p,q) \in f\}| \ge 1)$$

But that means

$$\forall q \in Y(|\{(p,q)|(p,q) \in f\}| = 1)$$

Bijection is important because it implies reversibility. A function that
is bijective has an inverse.

# Inverse

A bijection is reversible. In other words, given a bijection
$f: X \rightarrow Y$, there is another bijection
$f^{-1}: Y \rightarrow X$ such that $\forall e \in X(f^{-1}(f(e)) = e)$
and $\forall e \in Y(f(f^{-1}(e)) = e)$.

But can we prove this?

Let's examine what we know about a bijection $f:X \rightarrow Y$.
Because a bijection is a function, we know the following is true:

$$\forall p \in X(|\{(p,q)|(p,q) \in f\}| = 1)$$

This is a requirement of all functions, that every element in the domain
be mapped to exactly one item in the codomain.

However, since we also assume $f$ to be a bijection, we also know that

$$\forall q \in Y(|\{(p,q)|(p,q) \in f\}| = 1)$$

As a result, if we define $f^{-1}$ so that

$\forall p \in X(\forall q \in Y(((p,q) \in f) \Leftrightarrow ((q,p) \in f^{-1})))$

Then by symmetry,

$$\forall q \in Y(|\{(p,q)|(p,q) \in f\}| = 1)$$

implies

$$\forall q \in Y(|\{(q,p)|(q,p) \in f^{-1}\}| = 1)$$

But this pattern means $f^{-1}$ is a function because all elements in
the domain of $f^{-1}$ are mapped to one thing in the codomain.

Likewise, the function property of $f$

$$\forall p \in X(|\{(p,q)|(p,q) \in f\}| = 1)$$

means

$$\forall p \in X(|\{(q,p)|(q,p) \in f^{-1}\}| = 1)$$

But this pattern means $f^{-1}$ is a bijection.

This concludes the proof that every bijection has a matching inverse
function.

## The sorting example

Recall at the end of module [0289](../0289/mdModule.html), we attempted to express the
correct outcome of a sorting algorithm. The problem that we were having
was due to the function $f$ can potentially map every index to one
single index. Now that we understand the concept of bijection, we can
specify that function $f$ must be a bijection.

This ensures that each initial value of the array elements is found in
one element of the array when the algorithm is finished.

# AI-generated questions (not manually checked as of 9/8/2024)

You can view the [ChatGPT prompt](https://chatgpt.com/share/e6b26f78-0e9b-48ad-aedc-801de62a9cf0) that was used to generate these questions. 

## First batch

<details>
  <summary>Question 1: What does it mean for a function to be injective?</summary>
  <p>An injective function is one where each element in the domain is mapped to a unique element in the codomain. This means no two elements in the domain map to the same element in the codomain.</p>
</details>

<details>
  <summary>Question 2: Is the function f: {a, b} → {1, 2, 3} with f = {(a, 1), (b, 1)} injective? Why or why not?</summary>
  <p>No, this function is not injective because both 'a' and 'b' map to the same element (1) in the codomain, violating the injectivity condition.</p>
</details>

<details>
  <summary>Question 3: What is the formal definition of a surjective function?</summary>
  <p>A surjective function is one where every element in the codomain has at least one element in the domain mapping to it. This ensures that every element of the codomain is "hit" by the function.</p>
</details>

<details>
  <summary>Question 4: Given the function f: {a, b} → {1, 2} with f = {(a, 1), (b, 1)}, is this function surjective? Why or why not?</summary>
  <p>No, this function is not surjective because the element 2 in the codomain is not mapped to by any element in the domain.</p>
</details>

<details>
  <summary>Question 5: Can a function be surjective if the size of the codomain is greater than the size of the domain? Explain why.</summary>
  <p>No, a function cannot be surjective in this case because there are more elements in the codomain than in the domain, so it is impossible for every element in the codomain to be mapped to by the domain.</p>
</details>

<details>
  <summary>Question 6: What does it mean for a function to be bijective?</summary>
  <p>A bijective function is both injective and surjective. This means that every element in the domain maps to a unique element in the codomain, and every element in the codomain is mapped to by some element in the domain. Therefore, the function is both one-to-one and onto.</p>
</details>

<details>
  <summary>Question 7: Given f: {a, b} → {1, 2} with f = {(a, 1), (b, 2)}, is this function bijective? Explain.</summary>
  <p>Yes, this function is bijective because it is both injective (each domain element maps to a unique codomain element) and surjective (every codomain element is mapped to by some element in the domain).</p>
</details>

<details>
  <summary>Question 8: How does the concept of bijection relate to the idea of function inverses?</summary>
  <p>A bijection is important because it implies the existence of an inverse function. If a function is bijective, its inverse will map each element in the codomain back to its corresponding element in the domain, and vice versa.</p>
</details>

<details>
  <summary>Question 9: If f: X → Y is a bijection, what can we say about the inverse f<sup>-1</sup>: Y → X?</summary>
  <p>If f is a bijection, then f<sup>-1</sup> is also a bijection. This is because f<sup>-1</sup> reverses the mapping such that each element in Y maps to exactly one element in X, ensuring both injectivity and surjectivity for f<sup>-1</sup>.</p>
</details>

<details>
  <summary>Question 10: Consider the function f: {a, b, c} → {1, 2, 3} with f = {(a, 1), (b, 2), (c, 3)}. Is this function injective, surjective, or bijective?</summary>
  <p>This function is bijective. It is injective because each element in the domain maps to a unique element in the codomain, and it is surjective because every element in the codomain is mapped to by an element in the domain.</p>
</details>

## More on the use of set notations

<details>
  <summary>Question 1: Given f: {x, y, z} → {1, 2, 3} with f = {(x, 1), (y, 2), (z, 2)}, evaluate the injectivity of f using the set notation ∀p ∈ X(∀q ∈ X((p ≠ q) ⇒ f(p) ≠ f(q))).</summary>
  <p>The function is not injective. Using the set notation, x maps to 1 and both y and z map to 2, violating the condition that no two elements in the domain map to the same codomain element.</p>
</details>

<details>
  <summary>Question 2: For the function f: {a, b} → {1, 2, 3} with f = {(a, 1), (b, 1)}, apply the set notation ∀q ∈ Y(|{(p, q) | (p, q) ∈ f}| ≤ 1) to determine if the function is injective.</summary>
  <p>The function is not injective because both a and b map to 1, which violates the condition that the number of elements in the domain mapping to any element in the codomain should be less than or equal to 1.</p>
</details>

<details>
  <summary>Question 3: Use the set notation ∀q ∈ Y(∃p ∈ X(f(p) = q)) to determine if the function f: {a, b} → {1, 2} with f = {(a, 1), (b, 1)} is surjective.</summary>
  <p>The function is not surjective. According to the set notation, each element in the codomain should be mapped by at least one element in the domain, but 2 in the codomain is not mapped to by any element in the domain.</p>
</details>

<details>
  <summary>Question 4: For the function f: {a, b, c} → {1, 2} with f = {(a, 1), (b, 2)}, apply the set notation ∀q ∈ Y(|{(p, q) | (p, q) ∈ f}| ≥ 1) to evaluate whether it is surjective.</summary>
  <p>The function is surjective because each element in the codomain (1 and 2) has at least one element in the domain mapping to it, satisfying the condition in the set notation.</p>
</details>

<details>
  <summary>Question 5: Using the set notation ∀q ∈ Y(|{(p, q) | (p, q) ∈ f}| = 1), determine if the function f: {x, y} → {1, 2} with f = {(x, 1), (y, 2)} is bijective.</summary>
  <p>The function is bijective because each element in the codomain has exactly one element from the domain mapping to it, satisfying the condition for both injectivity and surjectivity.</p>
</details>

<details>
  <summary>Question 6: Apply the set notation ∀p ∈ X(|{(p, q) | (p, q) ∈ f}| = 1) to verify whether f: {m, n} → {1, 2} with f = {(m, 1), (n, 2)} satisfies the definition of a function.</summary>
  <p>Yes, f satisfies the definition of a function because every element in the domain is mapped to exactly one element in the codomain, as required by the set notation.</p>
</details>

<details>
  <summary>Question 7: Is the function f: {a, b} → {1, 2, 3} with f = {(a, 1), (b, 2)} surjective using the set notation ∀q ∈ Y(∃p ∈ X(f(p) = q))?</summary>
  <p>No, the function is not surjective because 3 in the codomain is not mapped to by any element in the domain, violating the set notation.</p>
</details>

<details>
  <summary>Question 8: For the function f: {p, q} → {1, 2, 3} with f = {(p, 1), (q, 2)}, use the set notation ∀q ∈ Y(|{(p, q) | (p, q) ∈ f}| ≤ 1) to determine if it is injective.</summary>
  <p>Yes, the function is injective because no two domain elements map to the same codomain element, satisfying the injectivity condition in the set notation.</p>
</details>

<details>
  <summary>Question 9: Using the set notation ∀q ∈ Y(|{(p, q) | (p, q) ∈ f}| = 1), evaluate if the function f: {x, y, z} → {1, 2} with f = {(x, 1), (y, 1), (z, 2)} is injective.</summary>
  <p>The function is not injective because both x and y map to the same codomain element (1), which violates the condition that each codomain element should be mapped to by exactly one domain element.</p>
</details>

<details>
  <summary>Question 10: For the function f: {a, b, c} → {1, 2} with f = {(a, 1), (b, 2)}, use the set notation ∀q ∈ Y(∃p ∈ X(f(p) = q)) to verify if it is surjective.</summary>
  <p>The function is surjective because every element in the codomain (1 and 2) is mapped to by some element in the domain, satisfying the surjectivity condition in the set notation.</p>
</details>

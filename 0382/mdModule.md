---
title: "Module 0382: The recursive definition of summation and other \"big-operators\""
---

# Summation

The sigma Greek letter is often used to denote summation. For example, $\sum_{i=2}^{5} i^2=2^2+3^2+4^2+5^2=4+9+16+25=54$. In general, the sigma (summation) notation is $\sum_{i=b}^{e} f(i)$ where $i$ is the index variable, $b$ is the start integer value of $i$, $e$ is the inclusive end value of $i$, and $f(i)$ is a function of $i$ where the value of the function is being added.

In our previous example, we can think of $b=2$, $e=5$, and $f(i)=i^2$.

In general, summation is difficult to define because of the way it expands. Sure, most people get the idea of what it means, but can summation be defined in a *really* clear way?

Let's give it a try.

First, the start value of $i$ should be less than or equal to the $e$ value, we can express this as follows:

$b > e \Rightarrow \sum_{i=b}^{e}f(i)=0$

This takes care of the weird case where the start value of $i$ is greater than the end value. Then, we can think of the special case when $b=e$:

$b = e \Rightarrow \sum_{i=b}^{e}f(i)=f(b)=f(e)$

Ah, that kind of makes sense! Now we have the tricky case when $b < e$. We know that in this case, $f(b)$ has to be part of the sum, but what about the rest? Let's check out the following:

$b < e \Rightarrow \sum_{i=b}^{e}f(i) = f(b)+\sum_{i=b+1}^{e}f(i)$

That's right, we just defined summation in a recursively way! In fact, using the ternary operator, we can clean up the definition into something *very* neat:

$\sum_{i=b}^{e}f(i) = (b > e) ? 0 : \left(f(b)+ \sum_{i=b+1}^{e} f(i) \right)$

The following illustrates how this recursive definition expands in our example:

$\begin{eqnarray} \sum_{i=2}^{5} i^2 & = & 2^2 + \sum_{i=3}^{5} i^2 \\ & = & 2^2 + 3^2 + \sum_{i=4}^{5} i^2 \\ & = & 2^2+3^2+4^2+\sum_{i=5}^{5} i^2 \\ & = & 2^2+3^2+4^2+5^2+\sum_{i=6}^{5} i^2 \\ & = & 2^2+3^2+4^2+5^2+0 \end{eqnarray}$

# The other "big-operators"

Summation (addition) is not the only operator that is used in computer science:

Note that for multiplication, the base-case default value is 1 because 1 is the identity of multiplication.

$\Pi_{i=b}^{e}f(i) = (b > e) ? 1 : \left(f(b) \cdot \Pi_{i=b+1}^{e} f(i) \right)$

For disjunction, the base-case default value is false (0).

$\bigvee_{i=b}^{e}f(i) = (b > e) ? 0 : \left(f(b) \vee \bigvee_{i=b+1}^{e} f(i) \right)$

For conjunction, the base-case default value is true (1).

$\bigwedge_{i=b}^{e}f(i) = (b > e) ? 1 : \left(f(b) \wedge \bigwedge_{i=b+1}^{e} f(i) \right)$

In an interesting twist, the existential quantifier can also be thought of as a "big operator", iterating through elements:

$\left( \exists e \in X\left(f(e)\right) \right) = \bigvee_{e \in X} f(e)$

From here, the issue is that the iterations through members of $X$ are not well stated. Because elements in a set have no inherent ordering, it is not possible to directly *address* an element in a set. To solve this problem, we need to create a new notation $d(X)$ to "deterministically draw an element from a non-empty set $X$". This means that given $X$ does not change, $d(X)$ draws exactly the same element every time the function is called.

With this notation, we can define the following:

$\left(\exists e \in X\left(f(e)\right) \right) = \left( \bigvee_{e \in X} f(e) \right) = (X = \\{\\}) ? 0 : \left( f \left( d(X) \right) \vee \bigvee_{e \in (X-\\{d(X)\\})} f(e) \right)$

The universal quantifier can be seen as a "big operator":

$\left( \forall e \in X\left(f(e)\right) \right) = \bigwedge_{e \in X}f(e)$

Similar to the existential quantifier, we can use the notation $d(X)$ as follows:

$\left(\forall e \in X \left(f(e) \right) \right) = \left( \bigwedge_{e \in X} f(e) \right) = (X = \\{\\}) ? 1 : \left( f \left( d(X) \right) \wedge \bigwedge_{e \in (X-\\{d(X)\\})} f(e) \right)$

Since we have introduced $d(X)$ at this point, we can also define other big operators based on iterating through elements in a set. *In general*, if $\square$ is an operator, and $i(\square)$ is the identity of the operator such that $\forall x(x \square i(\square) = x)$, then we can define the following:

$\square_{e \in X} f(e) = (X=\\{\\}) ? i(\square) : f(d(x)) \square \left( \square_{e \in (X-\\{d(x)\\}} f(e) \right)$

Let us apply this abstract big operator format to the big union. Union ($\cup$) has an identity of an empty set ($\{\}$). This means the following:

$\bigcup_{e \in X}f(e) = (X = \\{\\}) ? \\{\\} : \left(f\left(d(X)\right) \cup \left(\bigcup_{e \in X-\\{d(X)\\}}f(e) \right) \right)$

## Back to Sigma (summation)

$\sum_{i=b}^{e} f(i)$ can be re-expressed using the generalized template as $+_{e \in \{i\|i \in \mathbb{Z} \wedge i \le e \wedge i \ge b\}} f(e)$. In this form, $i(+)$ is the identity of addition, zero.

# But is this really necessary?

Yes, for two reasons.

The first reason is that there is no better way to explain the summation (sigma) notation. The recursive definition only relies on existing operators (addition, etc.) and the very same definition being defined. The key is the base-case where the summation returns the identity of addition, zero. 

In other words, this recursive definition of summation is concise (short, does not take many words), complete (does not depend on something else), and sound (correct).

The second reason is that this is a good example of recursive definitions. The non-recursive definition itself is fairly intuitive, and most people do not use a recursive definition. But this is why it is a good example for teaching the use of recursive definitions.

# AI-generated Q&A

<details>
<summary>
<b>Question 1</b> What is the general form of the summation (sigma) notation?</summary>
<b>Answer</b> The general form of the summation (sigma) notation is $\sum_{i=b}^{e} f(i)$, where $i$ is the index variable, $b$ is the start integer value of $i$, $e$ is the inclusive end value of $i$, and $f(i)$ is a function of $i$ where the value of the function is being added.
</details>

<details>
<summary>
<b>Question 2</b> What happens if the start value $b$ is greater than the end value $e$ in a summation?</summary>
<b>Answer</b> If the start value $b$ is greater than the end value $e$, then the summation is defined as zero: $\sum_{i=b}^{e}f(i) = 0$.
</details>

<details>
<summary>
<b>Question 3</b> How is the summation defined when the start and end values are the same ($b = e$)?</summary>
<b>Answer</b> When $b = e$, the summation is equal to the value of the function at $b$ (or $e$): $\sum_{i=b}^{e}f(i) = f(b) = f(e)$.
</details>

<details>
<summary>
<b>Question 4</b> How is the recursive case of summation defined when $b < e$?</summary>
<b>Answer</b> When $b < e$, the summation is defined recursively as follows: $\sum_{i=b}^{e}f(i) = f(b) + \sum_{i=b+1}^{e}f(i)$.
</details>

<details>
<summary>
<b>Question 5</b> What is the base-case default value for the product operator $\Pi$?</summary>
<b>Answer</b> The base-case default value for the product operator $\Pi$ is 1, because 1 is the identity of multiplication: $\Pi_{i=b}^{e}f(i) = (b > e) ? 1 : \left(f(b) \cdot \Pi_{i=b+1}^{e} f(i)\right)$.
</details>

<details>
<summary>
<b>Question 6</b> What is the base-case default value for the disjunction operator $\bigvee$?</summary>
<b>Answer</b> The base-case default value for the disjunction operator $\bigvee$ is false (or 0), since disjunction is equivalent to logical OR: $\bigvee_{i=b}^{e}f(i) = (b > e) ? 0 : \left(f(b) \vee \bigvee_{i=b+1}^{e} f(i)\right)$.
</details>

<details>
<summary>
<b>Question 7</b> What is the recursive definition of the existential quantifier $\exists$ as a big operator?</summary>
<b>Answer</b> The existential quantifier $\exists$ can be defined as a big operator using disjunction: $\left(\exists e \in X\left(f(e)\right)\right) = \left(\bigvee_{e \in X}f(e)\right)$. Using the $d(X)$ notation, it can be expressed as:
$\left(\exists e \in X\left(f(e)\right)\right) = (X = \{\}) ? 0 : \left(f(d(X)) \vee \bigvee_{e \in (X-\{d(X)\})} f(e)\right)$.
</details>

<details>
<summary><b>Question 8</b> How is the universal quantifier $\forall$ defined as a big operator?</summary>
<b>Answer</b> The universal quantifier $\forall$ can be defined as a big operator using conjunction: $\left(\forall e \in X\left(f(e)\right)\right) = \left(\bigwedge_{e \in X}f(e)\right)$. With the $d(X)$ notation, it can be expressed as:
$\left(\forall e \in X\left(f(e)\right)\right) = (X = \{\}) ? 1 : \left(f(d(X)) \wedge \bigwedge_{e \in (X-\{d(X)\})} f(e)\right)$.
</details>

<details>
<summary>
<b>Question 9</b> What is the identity of the union operator $\bigcup$?
</summary>
<b>Answer</b> The identity of the union operator $\bigcup$ is the empty set $\{\}$. Therefore, the union operator can be defined as:
$\bigcup_{e \in X}f(e) = (X = \{\}) ? \{\} : \left(f\left(d(X)\right) \cup \left(\bigcup_{e \in X-\{d(X)\}}f(e)\right)\right)$.
</details>

<details>
<summary>
<b>Question 10</b> Why is the recursive definition of summation important in computer science?</summary>
<b>Answer</b> The recursive definition of summation is important because it provides a concise, complete, and sound explanation of the summation process. It relies only on existing operators and the recursive definition itself, making it a clear and rigorous way to define summation. Additionally, it serves as a good example of how recursive definitions can be used in computer science.
</details>

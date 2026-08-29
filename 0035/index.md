---
title: "Module 0035: Proof by Induction"
---

# About this module

- Prerequisites: [0032](../0032)

- Objectives: This module introduces proof by induction.

# Strong Induction

Let $P$ be a proposition (predicate) being proven. Let $a \le b$ both be
integers. Then, strong induction states the following:

$(\forall i \in I: (a \le i \le b) \rightarrow P(i)), (\forall k \in I, (\forall i \in I: (a \le i < k \rightarrow P(i))) \rightarrow P(k)) \vdash (\forall n \in I: (n \ge a) \rightarrow P(n))$

Okay, that's pretty cryptic, even for computer scientists. Let us review
step by step.

First of all, induction is a form of inference. It has a general form of
$A, B \vdash C$, which says given that $A$ and $B$ are true, then we can
conclude that $C$ is true. In this case, $A$ and $B$ are somewhat
complicated propositions themselves.

$A$ states that $\forall i \in I: (a \le i \le b) \rightarrow P(i)$.
This means that we have at least one *base* case, but possibly many
bases cases. The base cases must be contiguous. The truth of each base
case is usually either by definition, or proven by techniques other than
induction (such as direct proof or proof by contradiction).

$B$ states that
$\forall k \in I, (\forall i \in I: (a \le i < k \rightarrow P(i))) \rightarrow P(k)$.
This is the induction step. This requires a little bit more explanation.

First of all, $a \le i < k \rightarrow P(i)$ is the condition of a
conditional proposition (although it *is* a conditional proposition by
itself). This proposition states that $P(i)$ is true for all $i$ such
that $a \le i < k$. The truth of this proposition is assumed for the
next step.

The difficult part is to prove that $a \le i < k \rightarrow P(i)$ leads
to $P(k)$. In other words, *assuming* that
$P(a), P(a+1),\cdots P(b), P(b+1),\cdots P(k-1)$, can we prove $P(k)$?

If we can, indeed, prove that
$P(a), P(a+1),\cdots P(b), P(b+1),\cdots P(k-1)$ does lead to $P(k)$,
and that we have base cases $P(a),\cdots P(b)$, then we can conclude
that $P(n)$ is true for all $a \le n$.

No explanation of induction is complete, or even *sane*, without
examples.

# Ordinary (not so strong) induction

This is like strong induction, but you can only assume $P(n-1)$ in order
to prove $P(n)$ in the induction step. In other words,

$(\forall i \in I: (a \le i \le b) \rightarrow P(i)), (\forall k \in I, (b < k) \rightarrow (P(k-1) \rightarrow P(k)) \vdash (\forall n \in I: (n \ge a) \rightarrow P(n))$

# Example 1

This is a somewhat trivial example. Nonetheless, I hope it helps to
illustrate proof by induction. You can find this proof by a search
engine.

The predicate, $P(x)$, states that
$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$.

The base case is $P(1)$. $\sum_{i=1}^{1} i = 1$, but
$\frac{1(1+1)}{2} = 1$. Therefore, the base case is proven.

Note that our $a = b = 1$ in this case. In other words, we only have one
base case.

Next, we need to show that
$\forall k \in I: (\forall i \in I: (1 \le i < k) \rightarrow P(i)) \rightarrow P(k)$.
In other words, for all $n > 1$, if we know that
$P(1), P(2), \cdots P(n-1)$, how can we show that $P(n)$?

Well, $P(n-1)$ means that $\sum_{i=1}^{n-1} i = \frac{(n-1)n}{2}$. Then,
we can add $n$ to both sides so that we have
$\sum_{i=1}^{n} i = n+\frac{n-1)n}{2}$. The right hand side can be
transformed as follows:

$$\begin{eqnarray}
  \frac{(n-1)n}{2} + n & = & \frac{(n-1)n+2n}{2} \\
                       & = & \frac{(n-1+2)n}{2} \\
                       & = & \frac{(n+1)n}{2} \\
                       & = & \frac{n(n+1)}{2}
\end{eqnarray}$$

As a result, $P(n)$ is true.

Note that we only had to make use of the fact that $P(n-1)$ in order to
prove that $P(n)$. In other words, we only made use of ordinary
induction, but not strong induction.

# Example 2

Let's try to prove that
$\forall k \in I: (k > 0) \rightarrow (2^k = 1+\sum_{i = 0}^{k-1} 2^i)$.
In other words, $2^k = 1+(1 + 2 + 4 + 8 + \cdots 2^{k-1})$ for all
$k > 0$.

The base case is simple (when $k = 1$): $2^1 = 2^0+1 = 1+1 = 2$.

The induction step states that
$\forall k \in I: (k > 0 \wedge 2^k = 1+\sum_{i=0}^{k-1} 2^i) \rightarrow (2^{k+1} = 1+\sum_{i=0}^{k} 2^i)$.
We need to assert this proposition:

$$\begin{eqnarray}
    2^{k+1} & = & 2(2^k) \\
            & = & 2(1+\sum_{i=0}^{k-1}2^i) \\
            & = & 2 + 2\sum_{i=0}^{k-1}2^i \\
            & = & 2 + \sum_{i=1}^k 2^i \\
            & = & 1 + (1+\sum_{i=1}^k 2^i) \\
            & = & 1 + \sum_{i=0}^k 2^i
\end{eqnarray}$$

Because we proved the base case and also the induction step, we conclude
that the original proposition is true.

# External resources

- : this is a list of examples. Some of the examples are quite out of
  the scope of this module, but it is a good sampler of proof by
  induction.

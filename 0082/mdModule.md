---
title: "Module 0082: Big and little Omicron, Omega and Theta"
---

# About this module

-   Prerequisites:

-   Objectives: This module discusses asymptotic notations in the
    context of algorithm time complexity.

# Algorithm time complexity

Although the primary objective of this module is not the discussion of
the time complexity of algorithms, it helps to provide a little bit of
context before we start the discussion of something dry and abstract.

The time complexity of an algorithm refers to the amount of time for an
algorithm to complete, usually as a function of the size of the problem.
Let us consider something that is really trivial. The following listing is an algorithm to compute the sum of all
elements in an array with "n" items.

```c
int i;
int sum;
int a[N];
i = 0; 
sum = 0;
while (i < N) 
{
  sum = sum + a[i]; 
  i = i + 1; 
}
```

How much time does it need? Obviously, that depends on the number of
elements in array "a" (N). Lines
`i=0` and
`sum=0` are executed only once (not dependent on
N), let us say that it takes $t_1$ for these two times to complete.

Line `while (i<N)` executes $N+1$ times because variable i
ranges from 0 to $N$ (not $N-1$). Lines
`sum = sum+a[i]` and
`i=i+1` execute $N$ times. Let $t_2$ indicate the
amount of time for each time line
`while (i<N)` executes, while $t_3$ be the amount of time
for lines `sum = sum+a[i]` and
`i=i+1` to execute in each iteration.

Then, the total amount of time for the algorithm to execute is *exactly*
$f(N) = t_1 + t_2 + N(t_2 + t_3)$. It would appear that the discussion
of time complexity should stop here.

## Complicated algorithms

The algorithm in the previous listing
is *really* simple. There are more
complicated algorithms. For example, bubble sort is relative complex.
The time complexity of a bubble sort algorithm boils down to
$f(N) = t_1 + N\cdot t_2 + N^2t_3$ for some constants $t_1$, $t_2$ and
$t_3$ (not related to the constants used in the complexity of the array
sum algorithm).

It is tedious to compute the *exact* amount of time of that an
implementation of an algorithm takes to execute. The effort is usually
not worth it either, as we only worry about complexity when N gets
large. When N is large, then only $t_3$ matters anyway.

In other words, in many cases, we are quite happy with just a simple
term that approximates the actual time complexity when N is large.

## Comparing algorithms

As it turns out bubble sort, selection sort and insertion sort all have
a time complexity of $f(N) = t_1 + N\cdot t_2 + N^2t_3$. Each
implementation of each algorithm has a different set of
$(t_1, t_2, t_3)$ constants. Nonetheless, they are lumped together as
one type of sorting algorithms.

Another type of sorting algorithm, such as merge sort (recursive or
iterative), have a time complexity of
$t_1 + N\cdot t_2 + N \log(N) t_3$. Although each implementation of each
algorithm has its own set of constants $(t_1, t_2, t_3)$.

When we compare algorithms of the same type, the constant for the
quickest growing term, $t_3$, is important. For example, selection sort
has a relatively small $t_3$ compared to insertion sort. However, when
we compare algorithms of different types, then even $t_3$ is not
important.

For example, let us assume that $t_3=10000$ for merge sort, whereas
$t_3=1$ for selection sort. We can always find a value for $N$ so that
it takes less time for merge sort than selection sort. Essentially, we
are trying to solve for $N$ such that $N^2 \ge 10000 N \log(N)$.

Although it is cumbersome to solve for the smallest $N$ that satisfies
the constraint, we can easily find that any $N \ge 120000$ will make the
condition true.

Because the constants are not useful when we compare algorithms of
different types, we would like to ignore the constants altogether when
we analyze the complexity of an algorithm.

## Asymptotic Estimates

In many cases, we only care about the time complexity of an algorithm,
with respect to the input size, as the size of the problem increases. To
make our lives easier, we use approximation functions that are much
simpler than the actual time complexity to characterize the complexity
of algorithms.

For example, with bubble sort, insertion sort and selection sort, we say
the time complexity is "$N^2$", whereas merge sort has a time complexity
of "$N \log(N)$". What does that really mean?

# Asymptotic characteristics

Let $f(N)$ be the actual time complexity of an algorithm, with respect
to the size of the input, $N$. Let $g(N)$ be a (usually simpler)
approximation of the time complexity of an algorithm. We want to find
out how $f(N)$ relates to $g(N)$.

## Supremum

Let set $A$ be a partial order. This means that we can define the $\le$
relation for $A \times A$ such that it is reflexive, antisymmetric and
transitive. The "less than or equal to" relation for numeric values is a
partial order.

Next, let $X \subseteq A$, which means $X$ has some of the values of
$A$. Let us define the predicate $P(y,X) = \forall x \in X( x \le y)$.
The predicate $P(y,X)$ means that $y$ is an upper bound of $X$. Now, let
use define
$s = \sup X \Leftrightarrow (P(s,X) \wedge (\forall s'(P(s',X)\Rightarrow s \le s')))$.
This basically means that $s$ is the minimum upper bound of $X$.

Note that $\sup(X)$ may be different from $\max(X)$. This is because the
supremum needs not be an element of $X$, but the maximum needs to be an
element of $X$.

## Infimum

These definitions are mirrors of those of the supremum. Let us reuse the
notations of $A$ and $X$.

This time let use define a predicate
$Q(y,X) = \forall x \in X(y \le x)$. This predicate means $y$ is a lower
bound of $X$. Now, we define
$i = \inf X \Leftrightarrow (Q(i,X) \wedge (\forall i'(Q(i',X) \Rightarrow i' \le i)))$.
This means that $i$ is the maximum lower bound of $X$.

## Limit of a sequence

What is the limit of a sequence of numbers? In other words, if I have an
infinite sequence $(x_0, x_1, \ldots)$, what does
$\lim_{i\rightarrow \infty}x_i = k$ mean?

It means that $k$ is a unique value that satisfies the requirement that
$\forall \epsilon > 0 \in \mathbb{R}( \exists m \in \mathbb{N}(
    \forall j \ge m \in \mathbb{N}( \left| k - x_j \right| < \epsilon)))$.
In English, it means that "for all real number epsilon greater than 0,
there exist a natural number m such that the difference between $k$ and
$x_m, x_{m+1}, x_{m+2}, \ldots$ are less than $\epsilon$." Or, even more
casually, "once we get to $x_m$, all other values of the $x$ sequence
are within $\epsilon$ of $k$."

Note that such a limit may not exist. Consider the sequence defined as
$x_i =(-1)^{i}$. In this case, $\lim_{i \rightarrow \infty}x_i$ does not
exist.

The limit of a sequence can be infinity. For example, if the sequence is
defined as $x_i = i$, then $\lim_{i \rightarrow \infty}x_i = \infty$. In
this case, the definition of the limit of a sequence is slightly
different because the difference of infinity and any finite number is
infinity. As a result, the definition needs to be modified as follows.

$\lim_{i \rightarrow \infty}x_i = \infty$ means that
$\forall y \in \mathbb{R}( \exists m \in \mathbb{N}( \forall j \ge m
    \in \mathbb{N}( x_j > y)))$. In plain English, it means that for any
real numbers y, we can find a natural number m such that
$x_m, x_{m+1}, x_{m+2}, \ldots$ are all greater than y.

## Limit superior

We can then define "limit superior" ($\limsup$) of a series of numbers,
$x_n$, as follows:

$$\begin{aligned}
      \limsup_{n \rightarrow \infty} (x_n) & = \inf\{\sup\{x_k|k \ge n\} | n \ge 0\} \\
      & = \inf\{\sup\{x_k|k\ge 0\}, \sup\{x_k|k\ge 1\}, \sup\{x_k|k \ge 2\},\dots\}
    
\end{aligned}$$

Alternatively, assuming $N \subseteq \mathbb{N}$, then we can define the following:

$$(w = \limsup_{n \in N}x_n) \Leftrightarrow (w = \inf\{m | m=\sup \{x_k | k \ge m \wedge k \in N\}\})$$

then 

$$\limsup_{n \rightarrow \infty}x_n = \limsup_{n \in \mathbb{N}}x_n$$

Note that even though $\lim_{i \rightarrow \infty}(-1)^{i}$ does not
exist,

$$\limsup_{i \rightarrow \infty}(-1)^{i} = 1$$

This is why limit superior is useful.

This term can be loosely interpreted as the "maximum lower bound of the
minimum upper bound of the tails of an infinite series of numbers".

## Limit inferior

We can then define "limit inferior" ($\liminf$) of a series of numbers,
$x_n$, as follows:

$$\liminf_{n \rightarrow \infty} (x_n)= \sup\{\inf\{x_k|k \ge n\} | n \ge 0\}$$

Just to follow up an example that we have been using,

$$\liminf_{i \rightarrow \infty}(-1)^{i} = -1$$

This term can be loosely interpreted as the "minimum upper bound of the
maximum lower bound of the tails of an infinite series of numbers".

## Upper bound

Let us start with two functions, $f(n)$ and $g(n)$. The definition of
$g(n)$ being an upper bound of $f(n)$is as follows:

$$f(n) \in O(g(n)) \Leftrightarrow \limsup_{n\rightarrow \infty} \left|{\frac{f(n)}{g(n)}}\right| < \infty$$

Note the use of the "element of" (or "in") notation $\in$. This means
$O(g(n))$ is denoting a set of functions to which $g(n)$ is an upper
bound.

The English translation is that $g(n)$ is an upper bound of $f(n)$. It
essentially means that $\forall n: \exists k: k\cdot g(n) \ge f(n)$.

This is, by far, the most important notation used in algorithm
complexity analysis because the estimate is only different from the
actual time complexity, in the worst case, by some constant as the size
of the problem increases.

Note that it is still possible that $g(n)$ is a gross over-estimate of
$f(n)$.

## Negligible

This is denoted by the little-oh notation:

$$f(n) \in o(g(n)) \Leftrightarrow \lim_{n\rightarrow \infty} \frac{f(n)}{g(n)} = 0$$

This means $g(n)$ is confirmed as a "gross" over-estimate of $f(n)$. For
example, if $f(n)$ is the time complexity of the merge sort algorithm,
then $f(n) \in o(n^2)$.

## Lower bound

This is denoted by big-omega:

$$f(n) \in \Omega(g(n)) \Leftrightarrow \liminf_{n\rightarrow \infty} \left|\frac{f(n)}{g(n)}\right| > 0$$

This means that $g(n)$ is not a gross over-estimate of $f(n)$. However,
it is possible that $g(n)$ is a gross under-estimate of $f(n)$. For
example, if $f(n)$ is the time complexity of bubble sort, then we can
say that $f(n) \in o(n)$.

## Dominant

This is denoted by small-omega:

$$f(n) \in \omega(g(n)) \Leftrightarrow \lim_{n\rightarrow \infty} \frac{f(n)}{g(n)} = \infty$$

This means that $g(n)$ is confirmed as a "gross' under-estimate of
$f(n)$. If $f(n)$ is the actual time complexity of bubble sort, then
$f(n) \in \omega(n)$.

## Tight bound

This is denoted by big-theta:

$$f(n) \in \Theta(g(n)) \Leftrightarrow (f(n) \in O(g(n))) \wedge (f(n) \in \Omega(g(n)))$$

Life does not get any better than this (for a computer scientist
reearching algorithm time complexity). This means that we can find two
constants, $k_1$ and $k_2$, such that
$\forall n: (f(n) \ge k_1g(n)) \wedge (f(n) \le k_2g(n))$.

# What have we learned?

If $f(n)$ is the time complexity of an algorithm,

-   If possible, we'd like to proof $f(n) \in \Theta(g(n))$ for some
    simple function $g(n)$.

-   Otherwise, we'd like to find a simple function $g(n)$ such that
    $f(n) \in O(g(n))$. At least we know that $g(n)$ is a "reasonable"
    estimate.

    -   If we can confirm that $f(n) \in o(g(n))$, then we know that "at
        some point", things can only get better.

-   Showing that $f(n) \in \Omega(g(n))$ is not very useful by itself.

-   Showing that $f(n) \in \omega(g(n))$ means that $g(n)$ is somewhat
    useless as an time complexity estimate.

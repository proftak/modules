---
title: "Module 0305: Counting"
---

# About this module

-   Prerequisites:

-   Objectives: This module discusses the matter of counting possible
    outcomes in experiments.

# Terms for counting

## Trial, experiment, outcome

A trial is a single attempt to do something, typically involving
choosing something. A single choice is a trial.

A trial has a set of possible outcomes associated with it. Each outcome
represents a possible result of a trial.

An experiment is a series of trials where subsequent trials may be
affected by earlier ones. An experiment has its own outcomes

In general, the outcome set of an experiment is represented by $\Omega$,
not to be confused with the set of operators in propositional calculus!

# General counting

Generally speaking, we are counting the outcomes of an experiment. For
example, in the case of Lottery, we may be counting the number of unique
Lottery tickets.

Let $T_i$ represent the outcome set of trial $i$, where $i$ is zero
oriented. In the case where $T_i$ does not influence $T_j$ where $j>i$,
the outcome set of an experiment of $m$ trials is as follows:

$T_0 \times T_1 \times T_2 \times \dots T_{m-1}$

Cartesian product is used because for every $e\in T_0$ as the first
actual outcome from the first trial, every $f \in T_1$ can be the
outcome of the second trial, and so on.

For counting purposes, the outcome space has the cardinality of
${ \displaystyle \prod_{i=0}^{m-1} |T_i|}$

In some cases, the set of outcomes are the same for all trials, meaning
$T_0=T_1=\dots T_{m-1}=T$. Let $n=|T|$. In this case, the cardinality of
the entire experiment of $m$ trials simplifies to

$n^m$

# Without replacement

A common restriction to trials in one experiment is that whatever is
chosen earlier cannot be a choice in later trials (of the same
experiment). Let us assume we start with a set $T$ where $n=|T|$ as the
set of outcomes of the first trial of an experiment with $m$ trials.

If $e_0 \in T$ is the actual outcome of trial 0, then $e_0$ is no longer
available for trial 1. Trial 1, therefore, has an outcome set of
$T-\\{e_0\\}$, and there are now $|T-\\{e_0\\}|=n-1$ choices in trial 1.

Using $e_i$ to represent the actual outcome of trial $i$, it is easy to
see that for trial $i$, the outcome set is

$T-(\bigcup_{j=0}^{i-1}\\{e_j\\})$

And as a result, the number of choices is

$\|T-(\bigcup_{j=0}^{i-1}\\{e_j\\})\| = n-i$

For counting purposes, an experiment of $m$ trials has the following
possible outcomes:

$$\begin{aligned}
    \prod_{i=0}^{m-1}(n-i) & = \prod_{i=0}^{m-1}(n-i)\frac{\prod_{i=m}^{n-1}(n-i)}{\prod_{i=m}^{n-1}(n-i)} \\
      & = \frac{\prod_{i=0}^{n-1}(n-i)}{\prod_{i=m}^{n-1}(n-i)} \\
      & = \frac{\prod_{i=1}^{n}(i)}{\prod_{i=1}^{n-m}(i)} \\
      & = \frac{n!}{(n-m)!} \\
      & = \mathrm{P}_{m}^{n}
  
\end{aligned}$$

Note that $\frac{n!}{(n-m)!}$ is also known as $\mathrm{P}_{m}^{n}$ or
$\mathrm{P}(n,m)$, it is the number of permutations to choose $m$ items
from $n$ items.

# Ordering

In some cases, the ordering of trials in an experiment is not important. For
example, in the case of Lottery, choosing 1,2,3,4,5 is the same as
choosing 5,4,3,2,1.

In this case, $\\{1,2,3,4,5\\}$ (note the use set notation) is known as a
*combination*, as opposed to $(1,2,3,4,5)$, which is known as a
permutation of the combination. There are many other permutations from
the same combination, such as (but not limited to) $(5,4,3,2,1)$,
$(1,2,3,5,4)$ and etc.

Knowing the number of permutations (order significant) of an experiment,
how do we get the number of combinations? In other words, how many
permutations are there to a single combination?

If a combination has $m$ elements, then there are $m$ ways to choose the
first outcome from the permutation perspective. There are $m-1$ ways to
choose the second outcome, and so on. For the last item, there is
exactly one 1 choice left because all other $m-1$ choices are used in
earlier trials already.

But hey, isn't this the same as choosing $m$ items from $m$ items?
Indeed! We already know the number of permutations of choosing $m$ items
from $m$ items is

$$\begin{aligned}
    \mathrm{P}(m,m) & = \frac{m!}{(m-m)!} \\
                    & = \frac{m!}{1} \\
		    & = m!
  
\end{aligned}$$

This means that the number of *combinations* of choosing $m$ items from
$n$ items (also known as $n$ choose $m$) is as follows:

$$\begin{aligned}
    \mathrm{C}(n,m) & = {n \choose m} \\
                    & =  \frac{\mathrm{P}(n,m)}{m!} \\
		    & = \frac{\frac{n!}{(n-m)!}}{m!} \\
		    & = \frac{n!}{m!(n-m)!}
  
\end{aligned}$$

## Choosing between permutations and combinations

In discrete probability, the number of permutations or combinations is used to compute a *ratio*. This ratio is expressed as $\frac{\|E\|}{\|\Omega\|}$ where $E \subseteq \Omega$ is called an event set, consisting of elements of $\Omega$ that are of interest.

If $\Omega$ is a set of tuples where ordering is important, then $E$ should also be a set of permutations. This suggests that $\|E\|$ can be computed as the number of permutations. This is the case for the Birthday Problem.

Likewise when elements of $\Omega$ are sets, then $E$ also needs to be a set of sets, and it suggests the counting of combinations. This is *sort of* the case for the counting of Lotto tickets. "*Sort of*" because the PowerBall Lotto problem also has a PowerBall number that is not a part of the combination of the 5 winning numbers.

# Permutation outcome set of experiments without replacement

In the cases where the outcome sets of each trial $T_i$ is independent
to other trials, the outcome set $\Omega$ of an experiment of $m$ trials
is just the Cartesian product of the outcome set $T_i$ where
$i \in \\{0..m-1\\}$.

However, with the concept of "without replacement", the outcome set of
an experiment gets a little more difficult to express. The cardinality
of the outcome set is already discussed and it is relatively easy to
derive.

Let $T$ represent the pool of choices originally presented. Furthermore,
let $\Omega_i(T)$ represent the outcome set of an experiment involving
$i$ trials starting with $T$ as the set of trial outcomes. It is easy to
see how $\Omega_0(T) = \\{ () \\}$.

However, $\Omega_2$ becomes a little more difficult to express. This is
because it depends on the actual outcome of the first trial. We can
still express it as follows:

$$\begin{aligned}
    \Omega_2(T) & = \bigcup_{e \in T}(\{e\} \times (T-\{e\})) \\
                & = \bigcup_{e \in T}(\{e\} \times \Omega_1(T-\{e\}))
  
\end{aligned}$$

Here, we can a recursive relationship that can be generalized as
follows:

$$\begin{aligned}
    \Omega_i(T) = \bigcup_{e \in T}(\{e\} \times \Omega_{i-1}(T-\{e\}))
  
\end{aligned}$$

The recursive definition ends with $i=0$ where $\Omega_0(T) = \\{ () \\}$.

# Combination outcome set of experiments without replacement

Occasionally, ordering is not important when the outcomes of an
experiment is considered. In this case, an outcome (of the experiment)
can be considered a set.

Let $U_i(X)$ represent the set of all possible combination outcomes of
an experiment with $i$ trials and the set $X$ represents the set of
choices available to the first trial.

As a result, we can see how the following is defined:

$U_0(X) = \\{ \\{ \\} \\}$

In other words, $U$ is a set of sets!

For all $i$ greater than 1, the following recursive definition applies.

$U_{i}(X) = \bigcup_{e \in X} (\bigcup_{S \in U_{i-1}(X-\\{e\\})} \\{\\{e\\} \cup S\\})$

Note that despite the similarity to $\Omega_i(X)$, the cardinality of
$U_i(X)$ is usually much smaller. This is because one set of $n$
elements has $n!$ permutations.

# Significance

Counting (the cardinality of an outcomes set) is important because it is
the denominator of discrete probabilities. In other words, we cannot
study the chances of certain specific outcomes unless we know the total
number of possible outcomes.

# AI-generated questions and answers

You can see the original prompt [here](https://chatgpt.com/share/672001f4-b2a0-8013-abf4-348f0b04f7b6).

<details>
  <summary>1. What is the difference between a trial and an experiment?</summary>
  <p>A <strong>trial</strong> is a single attempt or choice within an experiment, with a set of possible outcomes. An <strong>experiment</strong> is a series of trials where the outcome of one trial may influence subsequent ones.</p>
</details>

<details>
  <summary>2. If an experiment consists of three trials where each trial has 5 possible outcomes, what is the total number of possible outcomes if the trials are independent?</summary>
  <p>The total number of possible outcomes is the product of outcomes from each trial: $5 \times 5 \times 5 = 5^3 = 125$.</p>
</details>

<details>
  <summary>3. How does "without replacement" affect the counting of outcomes in an experiment?</summary>
  <p>"Without replacement" means that each outcome chosen in a trial is not available for subsequent trials, reducing the outcome set by one each time. For example, if there are initially 5 choices, the choices for the next trials would be 4, 3, and so on.</p>
</details>

<details>
  <summary>4. Calculate the number of ways to choose 3 items from 5 items, assuming order matters (permutations).</summary>
  <p>The number of permutations is $P(5,3) = \frac{5!}{(5-3)!} = \frac{5!}{2!} = \frac{120}{2} = 60$.</p>
</details>

<details>
  <summary>5. How many combinations of 3 items can be chosen from a set of 5 items?</summary>
  <p>The number of combinations is $C(5,3) = {5 \choose 3} = \frac{5!}{3!(5-3)!} = \frac{5!}{3! \cdot 2!} = \frac{120}{6 \times 2} = 10$.</p>
</details>

<details>
  <summary>6. Why is the formula for combinations divided by $m!$ when calculating the number of ways to choose $m$ items from $n$ items?</summary>
  <p>The division by $m!$ accounts for all the possible arrangements (or permutations) within each combination, as order does not matter in combinations. Thus, we divide by $m!$ to avoid counting duplicate arrangements as separate combinations.</p>
</details>

<details>
  <summary>7. Given a set of 6 items, calculate the number of permutations and the number of combinations when choosing 2 items.</summary>
  <p>Permutations: $P(6,2) = \frac{6!}{(6-2)!} = \frac{6!}{4!} = \frac{720}{24} = 30$<br>
  Combinations: $C(6,2) = {6 \choose 2} = \frac{6!}{2!(6-2)!} = \frac{6!}{2! \cdot 4!} = \frac{720}{2 \cdot 24} = 15$.</p>
</details>

<details>
  <summary>8. How does the recursive definition for combinations, $U_{i}(X)$, differ conceptually from the permutation outcome set $\Omega_i(T)$?</summary>
  <p>The recursive definition for combinations, $U_{i}(X)$, creates a set of sets, where ordering within each subset doesn’t matter, resulting in fewer total outcomes. The permutation outcome set, $\Omega_i(T)$, considers ordering, making it significantly larger when more outcomes are involved.</p>
</details>

<details>
  <summary>9. Why is counting outcomes important for determining probabilities in discrete math?</summary>
  <p>Counting outcomes provides the cardinality of the sample space, which is the denominator in probability calculations. Knowing the total possible outcomes is essential to determine the likelihood of specific events.</p>
</details>

<details>
  <summary>10. What is the formula for calculating the number of possible outcomes in an experiment of $m$ independent trials with $n$ choices in each trial, and how would you apply it to 4 trials with 6 choices each?</summary>
  <p>The formula for $m$ independent trials with $n$ choices each is $n^m$. For 4 trials with 6 choices each, the total number of possible outcomes is $6^4 = 1296$.</p>
</details>


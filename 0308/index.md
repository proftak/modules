---
title: "Module 0308: Discrete Probability"
---

# About this module

-   Prerequisites: [0305](../0305)

-   Objectives: This module explores discrete probabilities.

# Outcomes and Events

As explored in module [0305](../0305), the set of outcomes is a set of
all possibilities of an experiment. An experiment, in return, is a
series of trials.

The set of all possible outcomes is often denoted as $\Omega$.

An event, on the other hand, is a subset of $\Omega$. How events (as
sets) are constructed depends on the application or probabilities. For
example, in a Powerball Lottery, a particular event may include all
tickets that win a particular prize.

Probability is, in general, expressed as $\frac{|E|}{|\Omega|}$ given
that the set $E$ is an event. Of course, this also assumes the chances
of each element in $E$ are identical.

# Example 1: birthday problem

What are the chances that at least two people in a class share the same
birthday? It helps to make this more specific. Let the number of
students in a class be $n$.

First, we need to define $E$, which depends on how we define an
"experiment", and therefore, what a 'trial' represents.

A trial in this case is the birthday of a specific student. Imagine all
students in a class lined up to mark on a calendar his/her birthday.
Each marking of the calendar is a single trial.

The experiment is then defined as $n$ trials. The outcome of a *single*
instance of an experiment of a class of 3 students may look like the
following: $(2,361,4)$, each number in the tuple represents a day in a
year.

What will $E$ look like for a class of 3 students? This includes all the
ways to have birthdays where at least two students share the same
birthday:

$E=\{(1,1,1), (1,1,2), (1,2,1), (2,1,1), (1,1,3), \dots\}$

This is actually quite tedious to enumerate, especially when $n$ is
large. One of the reasons is that it accounts for how people may have
the same birthdays.

An alternative is to find the complement of $E$ such that
$F=\Omega - E$. Fortunately, in this case, $F$ is quite easy to define:
It is a set of experiment outcomes where no one in a class shares a
birthday. If we can figure out $|F|$, then $|E|=|\Omega|-|F|$.

The focus is now shifted to finding $F$.

If $n$ people are to have different birthdays, we need to pick $n$
birthdays from a year, then assign one day to a student in class.

To choose $n$ days from 365 is counting combination, not permutation.
The ordering of how these $n$ days are picked is not important. As a
result, the number of ways to choose $n$ days is $x={365 \choose n}$.

Imagine that I now have $n$ cards on hand, each card containing a unique
day in a year. My next task is to figure out how many ways I can hand
out these cards to $n$ students in this class. Let's say I have the
cards corresponding to April Fool's Day, New Year's Day and Pi Day, and
we have three students, Homer, Neo and Data. Obviously, the "ordering"
It is important because it determines who is getting which birthday. As a
result, we are counting permutations, or $y=\mathrm{P}(n,n)$.

Once we have the number of combinations of choosing $n$ days from 365,
and the number of permutations of assigning $n$ unique days to $n$
students, it is a simple matter of multiplying the two to get the total
ways of a class of $n$ in which all students have unique birthdays. This
means that:

$$\begin{aligned}
    |F| & =xy \\
	& ={365 \choose n}\mathrm{P}(n,n) \\
	& ={365 \choose n}n! \\
	& =\mathrm{P}(365,n)
  
\end{aligned}$$

We are now almost done!

What is left is to figure out $|\Omega|$. This is asking that, without
restrictions, how many ways can students have birthdays in a class of
$n$. In this case, the birthdate of a student does not affect the
birthdate of any other student. In other words, *each* student can
choose one day out of 365. As a result,

$\|\Omega\| = 365^{n}$

We have the answer now:

$$\begin{aligned}
    \mathrm{Pr}(E,\Omega) & = \frac{\|E\|}{\|\Omega\|} \\
                          & = \frac{\|\Omega\|-\|F\|}{\Omega} \\
			  & = 1-\frac{\mathrm{P}(365,n)}{365 ^ n}
  
\end{aligned}$$

Exercise: find out the chances of at least two students have the same
birthday in a class of 10, 20, 30 and 40 students. What do you observe?

# Example 2: coin toss

This is an even more interesting example. Oh, yeah!

If I toss a coin 5 times, what are the chances that there are 3 heads
and 2 tails?

First, let us assume the coin is not loaded. As a result, the
independent probabilities of landing on a head and landing on a tail are
0.5 exactly, each.

Each trial in this example is a single coin toss, resulting in either a
head or a tail.

An experiment in this example is the sequence of 5 trials.

$\Omega$ is, essentially all the ways that we can end up with the 5 coin
tosses. Because the result of each trial is independent from that of any
other trial, $|\Omega|=2^5$.

$E$, the event set, consists of all the ways we can end up with 3 heads
out of 5 tosses. $E$ include elements like $(H,H,H,T,T)$, $(H,T,H,T,H)$
and etc. The question is, what is $|E|$?

We can cast this into a different problem. Let's say we use a 3-tuple to
indicate the first, second and third heads of a toss. This means the
trial $(H,H,T,T,H)$ is represented as $\{0,1,4\}$ (we are using
zero-oriented indexing). Note that the set notation is used to indicate
that order is not important. This is because each number in a 3-tuple is
already indicating which toss in a series of 5 lands on a head.

In this case, we are counting combinations because the trials are
without replacement, and order is insignificant (when represented as
3-tuples). To be exact, we are counting the number of combinations of
selecting 3 out of 5, or $5 \choose 3$

The answer is, then,

$$\begin{aligned}
    \mathrm{Pr}(E,\Omega)=\frac{{5 \choose 3}}{2^5}
  
\end{aligned}$$

However, this is only one way of looking at this problem. Note that this
method requires that the chances of landing on a head or a tail be the
same.

The other way to look at this problem is as a binomial. This other way
can also handle the cases when a coin is "loaded" where the chances of
landing on a head is not the same as the chances of landing on a tail.

Assume that $p$ is the probability of landing on a head, and $q=1-p$ is
the probability of landing on a tail. Then the probabilities of an
experiment of 5 trials can be see as follows:

$$\begin{aligned}
    (p+q)^5 & = \sum_{i=0}^{i=5}(k_ip^iq^{5-i})
  
\end{aligned}$$

After all, this is just like a binomial! What are the value of the
constants $k_0$ to $k_5$?

## Pascal's Identity

To answer this question, we start with Pascal's identify, state and
proven as follows:

$$\begin{aligned}
 \binom{n}{k}+\binom{n}{k-1} & = \frac{n!}{k!(n-k)!} + \frac{n!}{(k-1)!(n-(k-1))!} \\ & = \frac{n!}{k!(n-k)!} + \frac{n!}{(k-1)!((n-k)+1)!} \\ & = \frac{n!}{k!(n-k)!} + \frac{n!k}{k!((n-k)+1)!} \\ & = \frac{n!}{k!(n-k)!} + \frac{\frac{n!k}{(n-k)+1}}{k!(n-k)!} \\ & = \frac{\frac{n!((n-k)+1)}{(n-k)+1}}{k!(n-k)!} + \frac{\frac{n!k}{(n-k)+1}}{k!(n-k)!}  \\ & = \frac{\frac{n!((n+1)-k) + n!k}{(n-k)+1}}{k!(n-k)!} \\ & = \frac{(n+1)!-n!k+n!k}{k!(n-k)!(n-k+1)} \\ & = \frac{(n+1)!}{k!(n-k+1)!} \\ & = \frac{(n+1)!}{k!((n+1)-k)!} \\ & = \binom{n+1}{k}
\end{aligned}$$

Next, we prove the binomial theorem, stated as follows:

$\forall n \in \mathbb{N}\left ((p+q)^n = \sum_{i=0}^n \binom{n}{i}p^iq^{n-i} \right )$

## Binomial Theorem: Proof by induction

To prove this theorem, we use proof by induction. In proof by induction,
the first step is to establish a base case. In this case, the base case
is when $n=0$:

$$\begin{aligned}
    (p+q)^0 & = 1 \\
            & = p^0q^0 \\
            & = {0 \choose 0}p^0q^0 \\
	    & = \sum_{i=0}^{0}({0 \choose i}p^iq^{0-i})
  
\end{aligned}$$

The next step is the interesting one: the induction step. In this step,
we make an assumption that the theorem holds true for some arbitrary
$n=k$, and we need to prove the theorem also holds true for the case of
$n=k+1$.

In this theorem, this means we assume the following is true

$(p+q)^k = \sum_{i=0}^{k}({k \choose i}p^iq^{k-i})$

Now we work on the case when $n=k+1$:

$$\begin{aligned}
    (p+q)^{k+1} & = (p+q)(p+q)^k  \\
                 & = (p+q)\sum_{i=0}^{k}({k \choose i}p^iq^{k-i})  \\
                 & = \sum_{i=0}^{k}({k \choose i}p^iq^{k-i}(p+q))  \\
                 & = \sum_{i=0}^{k}({k \choose i}p^{i+1}q^{k-i}) +\sum_{i=0}^{k}({k \choose i}p^iq^{k-i+1})  \\
                 & = {k+1 \choose 0}p^0q^{k+1} + \sum_{i=0}^{k-1}({k \choose i}p^{i+1}q^{k-i}) +\sum_{i=1}^{k}({k \choose i}p^iq^{k-i+1})  + {k+1 \choose k+1}p^{k+1}q^0 \\
                 & = {k+1 \choose 0}p^0q^{k+1} + \sum_{i=1}^{k}({k \choose {i-1}}p^{i}q^{k-i+1}) +\sum_{i=1}^{k}({k \choose i}p^iq^{k-i+1})  + {k+1 \choose k+1}p^{k+1}q^0  \\
                 & = {k+1 \choose 0}p^0q^{k+1} + \sum_{i=1}^{k}(({k \choose {i-1}}+{k \choose i})p^{i}q^{k+1-i})  + {k+1 \choose k+1}p^{k+1}q^0  \\
                 & = {k+1 \choose 0}p^0q^{k+1} + \sum_{i=1}^{k}({k+1 \choose i}p^{i}q^{k+1-i})  + {k+1 \choose k+1}p^{k+1}q^0  \\
                 & = \sum_{i=0}^{k+1}({k+1 \choose i}p^{i}q^{k+1-i})
  
\end{aligned}$$

This concludes the proof by induction. This theorem is called the
binomial theorem. You can see how Pascal's identity is used in this
proof, along with "summation" sliding. Of course, don't forget the trick
of ${k+1 \choose 0} = {k+1 \choose k+1} = 1$.

## Binomial distribution

But how is this theorem useful? It can be used to model experiments
involving binary trials with replacement, such as coin toss. Given that
$p$ is the chances of a coin landing on the head, and $q=1-p$, we can
now predict the chances of $m$ heads in $n$ tosses:

${n \choose m}p^mq^{n-m}$

## Exercise

Utilize a spreadsheet to experiment with different distributions with
different $n$ (number of trials) and different $p$ (chances of landing
on a head).

# Observed/empirical probabilities

In some situations, the probability $\mathrm{Pr}(E,\Omega)$ is not
computed but rather observed. For example, when a bit is transmitted, it
has chances of being received correct and incorrectly. In this case, we
can see $\Omega(x) = \{x\} \times \{0,1\}$, where the first item of a
tuple $x$ is what is transmitted, and the second item of a tuple is what
is received. This means that $(1,0) \in \Omega(1)$ represents the
outcome that a 1 is transmitted, but erroneously received as a 0.

In this case, the probability is not based on the ratio of cardinality
because the actual chances of $\mathrm{Pr}((1,0), \Omega(1))$ is based
on either physical modeling or actual empirical observations.

Assuming each trial is independent from other trials, the probability of
a specific experiment outcome is the product of the probability of each
individual trial. For example, assume that 1011 is transmitted, but 1001
is received. Then the chances of this happening is as follows:

$\mathrm{Pr}(((1,1), (0,0), (1,0), (1,1)), \Omega(1)\times \Omega(0)\times \Omega(1) \times \Omega(1)) = 
  \mathrm{Pr}((1,1),\Omega(1)) \cdot
  \mathrm{Pr}((0,0),\Omega(0)) \cdot
  \mathrm{Pr}((1,0),\Omega(1)) \cdot
  \mathrm{Pr}((1,1),\Omega(1))$

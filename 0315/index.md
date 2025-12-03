---
title: "Module 0315: Predicate Calculus via Prolog"
---

# About this module

-   Prerequisites:

-   Objectives: This module introduces predicate calulus by using
    examples of using Prolog.

# Introducing Prolog

Prolog was an AI programming language for "reasoning", and it was widely
used by non-US countries in the 80s in research of AI topics, usually
revolving around how humans reason in a logical way. The basis of
Prolog, however, dates back to the origin of predicate calculus, also
known as first-order logic. Predicate calculus itself dates back to the
mid 1800s.

# Syntax of Prolog

Unlike most other programming languages, the case of the first letter of
words actually carries meanings. If a word starts with a lower-case
letter, it can be the name of the predicate (explained later) or the
name of an "atom" (also explained later). If a word starts with an upper
case letter, it is known as a variable.

A predicate calculus system logically represent truth of a "universe",
the set of all things in this "universe" is known as the domain of
discourse, or simply "universe". For the rest of this document, let us
use $U$ to represent this set.

A predicate $p$ is conceptually a function that maps a tuple of elements
of $U$ to true or false, that is, $p:\prod_{i=0}^{k}U \rightarrow
  \{0,1\}$. In this notation, $k$ represents the length of the tuple.

A predicate is expressed by one or more rules in Prolog. A rule in
Prolog is an implicate that has the general form of "predicate is
implied by an expression". Let us examine a few rules.

```prolog
isAJedi(lukeSkywalker).
```

In this rule, "isAJedi" is the name of the predicate, while
"lukeSkywalker" is an element of $U$. This is actually a shorthand
version of the following rule:

```prolog
isAJedi(lukeSkywalker) :- true.
```

This spelled out rule literally says "lukeSkywalker isAJedi is implied
by true". However, we already know that in order for an implication (a
Prolog rule) to be true, and the antecedent is already true, the
consequent must be true as well. In other words, this rule says
"lukeSkywalker isAJedi" in short.

Rules like this form the "basis" of all truth to be derived, except for
computation truths that do not need to link to specific atoms $U$.

We can now define more interesting rules, such as the following:

```prolog
isAProperJedi(X) :- isAJedi(X), owns(X,Y), isALightSaber(Y).
```

This is where things get more interesting. This rule literally says "X
isAProperJedi is implied by X isAJedi and X owns Y and Y isALightSaber".
That makes sense in the Star Wars (TM) universe. But how does this work
in Prolog?

First of all, we need to a few rules to make Luke a proper Jedi:

```prolog
isALightSaber(anakinBlue).

  owns(lukeSkywalker, anakinBlue).
```

# Substitution

But how does Prolog work? How does it connect to predicate calculus?

First, let us examine what a rule in Prolog means. Let us revisit the
"isAProperJedi" rule. In terms of quantifiers, it means the following:

$\forall X \in U(\exists Y \in U(\mathtt{isAJedi}(X) \wedge \mathtt{owns}(X,Y)
      \wedge \mathtt{isALightSaber}(Y) \Rightarrow \mathtt{isAProperJedi}(X)))$

Note how $X$ uses a universal quantifier and $Y$ uses an existential
quantifier. This is because $X$ appears in the consequent of the
implication, but $Y$ only appears in the antecedent of the implication.

We can single out the actual statement as follows:

$\phi = \mathtt{isAJedi}(X) \wedge \mathtt{owns}(X,Y)
      \wedge \mathtt{isALightSaber}(Y) \Rightarrow \mathtt{isAProperJedi}(X)$

This is not too bad, as it is just a syntactic transformation from
Prolog syntax to quantifier syntax. But how does Prolog finds the answer
when asked whether lukeSkywalker isAProperJedi?

One of the most important underlying mechanism of Prolog is
substitution. For example, the following substitution makes the
"isAProperJedi" predicate true:

$s=\{X/\mathtt{lukeSkywalker}, Y/\mathtt{anakinBlue}\}$

As you can see, a substitution is a set where each element maps a
variable (upper case word) to either another variable or an element of
$U$.

The application of substitution looks like this: $\phi s$. The result of
this substitution is then as follows:

$\phi s = \mathtt{isAJedi}(\mathtt{lukeSkywalker}) \wedge \mathtt{owns}(\mathtt{lukeSkywalker},\mathtt{anakinBlue})
      \wedge \mathtt{isALightSaber}(\mathtt{anakinBlue}) \Rightarrow \mathtt{isAProperJedi}(\mathtt{lukeSkywalker})$

However, we also know that the individual components of the conjunction
in the antecedent of the implication is true, so we can conclude the
following:

$\phi s = 1 \wedge 1
      \wedge 1 = 1 \Rightarrow \mathtt{isAProperJedi}(\mathtt{lukeSkywalker})$

That essentially proves that
$\mathtt{isAProperJedi}(\mathtt{lukeSkywalker})$ is true.

# Disjunctions

As seen in the previous section, a comma means conjunction. Disjunction
can also be expressed, and there are two ways to do it.

A semi-colon means disjunction. The operator priority of disjunction is
lower than conjunction. This means conjunction is like multiplication
and disjunction is like addition in algebra.

A rule can also have alternative definitions. All alternative
definitions are matched in the order as listed in the source code.

# Negation

Negation is a bit tricky in Prolog. Although there is a "not" operator,
it only means that something cannot be proven. The operator "not" is
written as `\+` (backslash plus).

Let us example the use of negation in the following Prolog example:

```prolog
sithTolerant(X):- isASith(Y), \+(disagreeWith(X,Y)).
```

This rules says that "for all X, there exists Y isASith and X cannot be
proven disagreeWith Y implies X is sithTolerant."

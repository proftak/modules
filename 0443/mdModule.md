---
title: "Module 0443: A more hair-splitting way to define set notations"
---

# Prerequisites

* [Module 0279: boolean operators](https://proftak.github.io/modules/0279/mdModule.html)
* A general understanding of and the ability to differentiate the following words/phrases: "all", "every", "at least one."

# Operators and notations

* $a \in X$ means $a$, as a value, is an element of set $X$.
* $a = b$ means that the value of $a$ and the value of $b$ are the same, hence interchangeable.
* As a predicate, $P(a)$ is a function that returns a boolean (true/false) value, $a$ is the parameter, and $P$ is the name of the predicate. This is a useful notation that takes the place of an expression that is a placeholder.
* $\forall e(P(e))$ means "for every value $e$, $P(e)$ is true.
* $\exists e(P(e))$ means there is at least one value $e$ such that $P(e)$ is true.
* $(e \in (X \cap Y)) \Leftrightarrow (\forall e((e \in X) \wedge (e \in Y)))$, $X \cap Y$ is the *intersection* of the sets $X$ and $Y$.
* $(e \in (X \cup Y)) \Leftrightarrow (\forall e((e \in X) \vee (e \in Y)))$. $X \cup Y$ is the *union* of the sets $X$ and $Y$.
* $(e \in (X - Y)) \Leftrightarrow (\forall e((e \in X) \wedge \neg(e \in Y)))$. $X \cap Y$ is the *difference* of the sets $X$ and $Y$.

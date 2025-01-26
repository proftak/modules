---
title: "Module 0443: A more hair-splitting way to define set notations"
---

# Prerequisites

* [Module 0279: boolean operators](https://proftak.github.io/modules/0279/mdModule.html)
* [Module 0440: the syntax to describe syntax](https://proftak.github.io/0440/mdModule.html)
* A general understanding of and the ability to differentiate the following words/phrases: "all", "every", and "at least one."

# Operators and notations

* $\boxed{a \in X}$ means $a$, as a value, is an element of set $X$. This is a boolean operator that can be evaluated to be true or false.
* $a = b$ means that the value of $a$ and the value of $b$ are the same, hence interchangeable.
* As a predicate, $P(a)$ is a function that returns a boolean (true/false) value, $a$ is the parameter, and $P$ is the name of the predicate. This is a useful notation that takes the place of an expression that is a placeholder.
* $\boxed{\forall e}(P(e))$ means "for every value $e$, $P(e)$ is true." This universally-quantified expression returns a boolean value.
* $\boxed{\exists e}(P(e))$ means "there is at least one value $e$ such that $P(e)$ is true." This existentially-quantified expression returns a boolean value.
* $\forall e((e \in (X \cap Y)) \Leftrightarrow ((e \in X) \wedge (e \in Y)))$, $X \cap Y$ is the *intersection* of the sets $X$ and $Y$.
* $\forall e((e \in (X \cup Y)) \Leftrightarrow ((e \in X) \vee (e \in Y)))$. $X \cup Y$ is the *union* of the sets $X$ and $Y$.
* $(e \in (X - Y)) \Leftrightarrow (\forall e((e \in X) \wedge \neg(e \in Y)))$. $X - Y$ is the *difference* of the sets $X$ and $Y$.
* $(X \subseteq Y) \Leftrightarrow (\forall e((e \in X) \Rightarrow (e \in Y)))$. $X \subset Y$ evaluates whether $X$ is a subset of $Y$, it says "every element $e$ in set $X$ is also in set $Y$."
* $(X \subset Y) \Leftrightarrow ((\forall e((e \in X) \Rightarrow (e \in Y))) \wedge (\exists e((e \in Y) \wedge \neg(e \in X))))$. $X \subset Y$ evaluates whether $X$ is a *proper* subset of $Y$. There needs to be one element that is in $Y$ but not in $X$.
* $(X=\\{e\|P(e)\\}) \Leftrightarrow (\forall e((e \in X) \Leftrightarrow (P(e))))$. This is a notation to describe the membership of a set with an infinite number of elements where $P$ is a predicate.
* To describe all the members of a set that has a finite number of elements:
  * The general BNF syntax is as follows: **\{** [ *`element`* \{ **,** *`element`* \}*] **\}**
    * Anything that is **bold** is a terminal, it should be a part of the expression verbatim.
    * Anything that is *`italic`* is a token, it is a placeholder of something else.
    * Anything that is between brackets [] is optional, there may be zero or one occurrence.
    * Anything that is between braces \{\} is a group.
    * Anything that is followed immediately by an asterisk * can occur any number of times, including zero.
  * Given the syntax described, the ordering of elements in this notation is not important. As an example, $\\{a,b,c\\} = \\{a,c,b\\} = \\{b,a,c\\} = \\{b,c,a\\} = \\{c,a,b\\} = \\{c,b,a\\}$.
  * $\\{\\}$ is known as the empty set.
* $\|X\|$ is the cardinality of the set $X$, the cardinality of a set is *similar* to the number of elements in the set.
* $\forall e \in X(P(e))$ is an abbreviation of $\forall e((e \in X) \Rightarrow (P(e)))$, it says "for every element $e$ in set $X$, $P(e)$ is true."
* $\exists e \in X(P(e))$ is an abbreviation of $\exists e((e \in X) \wedge (P(e)))$, it says "there is at least one element $e$ in set $X$ such that $P(e)$ is true."

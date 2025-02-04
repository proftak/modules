---
title: "Module 0443: A more hair-splitting way to define set notations"
---

# Prerequisites

* [Module 0279: boolean operators](https://proftak.github.io/modules/0279/mdModule.html)
* [Module 0440: the syntax to describe syntax](https://proftak.github.io/0440/mdModule.html)
* A general understanding of and the ability to differentiate the following words/phrases: "all," "every," and "at least one."

# Operators and notations

* $\boxed{a \in X}$ means $a$, as a value, is an element of set $X$. This is a boolean operator that can be evaluated to be true or false.
* $a = b$ means that the value of $a$ and the value of $b$ are the same, hence interchangeable.
* As a predicate, $P(a)$ is a function that returns a boolean (true/false) value, $a$ is the parameter, and $P$ is the name of the predicate. This is a useful notation that takes the place of a potentially complicated expression. The actual definition of $P(a)$ depends on the context. 
* $\boxed{\forall e}(P(e))$ means "for every value $e$, $P(e)$ is true." This universally-quantified expression returns a boolean value.
* $\boxed{\exists e}(P(e))$ means "there is at least one value $e$ such that $P(e)$ is true." This existentially-quantified expression returns a boolean value.
* $\forall e((e \in (\boxed{X \cap Y)}) \Leftrightarrow ((e \in X) \wedge (e \in Y)))$ is *definitive*, $X \cap Y$ is the *intersection* of the sets $X$ and $Y$. The term "definitive" means an expression true by definition.
* $\forall e((e \in (\boxed{X \cup Y)}) \Leftrightarrow ((e \in X) \vee (e \in Y)))$ is *definitive*. $X \cup Y$ is the *union* of the sets $X$ and $Y$.
* $\forall e((e \in (\boxed{X - Y})) \Leftrightarrow ((e \in X) \wedge \neg(e \in Y)))$ is *definitive*. $X - Y$ is the *difference* of the sets $X$ and $Y$.
* $\boxed{X \subseteq Y} \Leftrightarrow \forall e(((e \in X) \Rightarrow (e \in Y)))$ is *definitive*. $X \subseteq Y$ evaluates whether $X$ is a subset of $Y$, it says "every element $e$ in set $X$ is also in set $Y$."
* $\boxed{X \subset Y} \Leftrightarrow ((X \subseteq Y) \wedge (\exists e((e \in Y) \wedge \neg(e \in X))))$ is definitive. $X \subset Y$ evaluates whether $X$ is a *proper* subset of $Y$. There needs to be one element in $Y$ but not in $X$.
* $\forall e((e \in \boxed{\\{e\|P(e)\\}}) \Leftrightarrow (P(e)))$ is *definitive*. This is a notation to describe the membership of a set with an infinite number of elements where $P$ is a predicate.
* To describe all the members of a set that has a finite number of elements:
  * The general BNF syntax is as follows: **\{** [ *`element`* \{ **,** *`element`* \}*] **\}**
    * Anything that is **bold** is a terminal; it should be a part of the expression verbatim.
    * Anything that is *`italic`* is a token; it is a placeholder of something else.
    * Anything that is between brackets [] is optional; there may be zero or one occurrence.
    * Anything that is between braces \{\} is a group.
    * Anything that is followed immediately by an asterisk * can occur any number of times, including zero.
  * Given the syntax described, the ordering of elements in this notation is not important. As an example, $\\{a,b,c\\} = \\{a,c,b\\} = \\{b,a,c\\} = \\{b,c,a\\} = \\{c,a,b\\} = \\{c,b,a\\}$.
  * $\boxed{\\{\\}}$ is known as the empty set.
* $\boxed{\|X\|}$ is the cardinality of the set $X$, the cardinality of a set is *similar* to the number of elements in the set.
* $\boxed{\forall e \in X(P(e))}$ is an abbreviation of $\forall e((e \in X) \Rightarrow (P(e)))$, it says "for every element $e$ in set $X$, $P(e)$ is true."
* $\boxed{\exists e \in X(P(e))}$ is an abbreviation of $\exists e((e \in X) \wedge (P(e)))$, it says "there is at least one element $e$ in set $X$ such that $P(e)$ is true."
* The general BNF of a tuple is as follows: **(** [ *`element`* \{ **,** *`element`* \}*] **)**. The ordering of values in a tuple is significant.
* $\forall e(\forall f(((e,f) \in \boxed{X \times Y}) \Leftrightarrow ((e \in X) \wedge (f \in Y))))$ is definitive. $X \times Y$ is called the cartesian product of the sets $X$ and $Y$, each element in $X \times Y$ is a two-tuple (tuple with two items), where the first item in the 2-tuple is an element from $X$ and the second item is an element from $Y$.
* Given $X$ and $Y$ are sets, then $(\boxed{X=Y}) \Leftrightarrow ((X \subseteq Y) \wedge (Y \subseteq X))$, this defines the equality of two sets, and it lays the foundation of understanding nested sets.

# Examples

* $\\{a,b,c\\} \cap \\{d,a,c\\}=\\{c,a\\}$
* $\\{a,b,c\\} \cup \\{d,a,c\\}=\\{b,d,c,a\\}$
* $\\{a,b,c\\} - \\{d,a,c\\}=\\{b\\}$
* $\\{a,b,c\\} \cap \\{\\}=\\{\\}$
* $\\{a,b,c\\} \cup \\{\\}=\\{b,c,a\\}$
* $\\{a,b,c\\} - \\{\\}=\\{a,b,c\\}$
* $\\{a,b\\} \cap \\{d,c\\}=\\{\\}$
* $\\{a,b\\} \cup \\{d,c\\}=\\{c,a,b,d\\}$
* $\\{\\} - \\{a,b\\} = \\{\\}$
* for any set $A$, $A \cup \\{\\} = A$
* $\forall e(e \in A \Leftrightarrow (e \in (A \cup \\{\\}))$
* $X=\\{a,b\\}, Y=\\{a,b,c\\}$
	* $e=a, (e\in X \Rightarrow e \in Y)=1$
	* $e=b, (e\in X \Rightarrow e \in Y)=1$
	* $e=\mathrm{Tak}, (e\in X \Rightarrow e \in Y)=1$
	* $e=23, (e\in X \Rightarrow e \in Y)=1$
* $X \subseteq X$ is always true assuming $X$ is a set.
* $(X \subset Y) \Leftrightarrow ((X \subseteq Y) \wedge (Y-X \ne \\{\\}))$
* $(X \subset Y) \Leftrightarrow ((X \subseteq Y) \wedge (Y \cup X \ne X))$
* $X \subset X$ is always false assuming $X$ is a set.
* $E=\\{n\|(n\in \mathbb{Z}) \wedge (n \mod 2 = 0)\\}$ is the same as $\forall n((n \in E) \Leftrightarrow ((n \in \mathbb{Z}) \wedge (n \mod 2 = 0)))$
* $\|\mathbb{Z}\|=\|\mathbb{N}\|$
* $\forall e \in \\{\\}(0)$ is true or false? True
* $\forall e((e \in \\{\\}) \Rightarrow 0)$ is true or false? True
* $\\{a,b\\} \subseteq \\{a,b\\}$ is true
* $\\{a,b\\} \subset \\{a,b\\}$ is false
* $\\{a,b\\} \subseteq \\{a,b,c\\}$ is true
* $\\{a,b\\} \subset \\{a,b,c\\}$ is true
* $\boxed{X \subseteq Y} \Leftrightarrow \forall e(((e \in X) \Rightarrow (e \in Y)))$
* $\\{a,b,c,d\\} \subseteq \\{a,b,c\\}$
* "Is {a,b,c,d} a subset of {a,b,c}?"
* $X \subseteq Y$ is asking "is it true or false that X is a subset of Y?"
* The following is a list of all the subsets of $\\{a,b,c\\}$:
	* $\\{\\}$
	* $\\{a\\}$
	* $\\{b\\}$
	* $\\{c\\}$
	* $\\{a,b\\}$
	* $\\{a,c\\}$
	* $\\{b,c\\}$
	* $\\{a,b,c\\}$
* $\mathbb{P}(S)$ is called the "power set of the set $S$", it consists all subsets of $S$.
* $|\mathbb{P}(S)| = 2^{|S|}$
* TODO: add section on nested containment
* $\\{a,b\\} \times \\{1,2,3\\} = \\{ (a,1), (a,2), (a,3), (b,1), (b,2), (b,3)  \\}$
	* $(Tak, Iraj) \in \\{a,b\\} \times \\{1,2,3\\}$ is false

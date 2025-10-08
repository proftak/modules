---
title: "Module 0297: Propositional Logic"
---

# About this module

-   Prerequisites: [0280](../0280/mdModule.html), [0285](../0285/mdModule.html), [0288](../0288/mdModule.html),
    [0289](../0289/mdModule.html)

-   Objectives: This module explores propositional logic, specifically
    its connection and application in Computer Science.

# Overview

Propositional logic is, not surprisingly, based on propositions. A
proposition is, essentially, a condition that may be true or false
(hence the name "proposition"). Propositional logic is a logic system
that can prove whether a particular proposition is true or not using a
somewhat mechanical method.

While propositional logic is not sufficient for automatic program
verification, it is still educational and serves as an introduction to
automated proving.

# General propositional logic

This section describes general propositional logic. A propositional
logic system (calculus) is a 4-tuple: $\mathcal{L}(A, \Omega,
  Z, I)$.

-   $A$: this is a set of symbols to be used. Symbols have no inherent
    meanings.

-   $\Omega$: this is a set of operators, also known as connectives.
    Connectives connect symbols and the result of connectives. $\Omega$
    can be broken into subsets $\Omega_i$ where $i$ determines the
    number of items connected by a connective. For example, $\Omega_2$
    is a set of connectives that connect exactly two items.

-   $Z$: this is a set of transformation rules. More on this later.
    Essentially, a transformation rule specifies the presence of a set
    of specific patterns produces a particular result pattern.

-   $I$: this is a set of well-formed formulae (explanation following)
    that are known to be true (axioms).

One of the key concepts is a well-formed formula (WFF). A WFF is defined
as follows:

-   $\forall e \in A(\mathrm{isAWFF}(e))$: this means all symbols
    defined in $A$ are by themselves WFFs.

-   $\forall i \in \\{1..n\\}(\mathrm{isAWFF}(\phi_i)) \wedge 
              (c \in \Omega_n) \Rightarrow \mathrm{isAWFF}(c(\phi_1, \phi_2, \dots \phi_n))$:
    this means that given $n$ WFFs $\phi_i$, and $c$ is a connective
    that has $n$ arguments, $c(\phi_1,\dots \phi_n)$ is also a WFF. This
    is the recursive rule that can make really big WFFs.

Given $A$ and $\Omega$, potentially an infinite number of WFFs can be
generated. However, each of these WFFs is merely a syntactic construct
that is "possible" based on $A$ and $\Omega$, but there is no meaning or
truthfulness associated with any of these WFFs. These WFFs also do not
relate to each other.

With just $A$ and $\Omega$, you can imagine that we can span a space of
WFFs where the WFFs are not connected in any way.

$I$ is a set of WFFs that are known to be true. Imagine that in the
space of WFFs spanned by $A$ and $\Omega$, some of the WFFs are labeled
"true".

Finally, $Z$ consists of rules that connect individual WFFs in the WFF
space. A rule (element) in $Z$ has the form of
$\\{\psi_1,\dots \psi_m\\} \vdash \phi$. The *antecedents* $\psi_i$
specify patterns to be matched. If all $m$ of them are matched, then the
consequent $\phi$ is "inferred ($\vdash$)" in the WFF space (produced).

Added 2022/03/02: A more formal way to look at transformation/inference
rules in $Z$ is as follows.

Consider $W=\\{\beta | \mathtt{isAWFF}(\beta) \\}$ assuming we are using
the $A$, $\Omega$ of some propositional system. In other words, $W$ is
the set of all WFFs with respect to the $A$ and $\Omega$ in
consideration. $I \subseteq W$ because $I$ is the set of all WFFs that
are given to be true (each one is an axiom).

Then we define $D\subseteq W$ so that $D$ is a set of WFFs that are
derivable from WFFs in $I$. This means that $I \subseteq D$ because WFFs
in $I$ are the starting points.

Assuming $\theta, \phi, \psi$ are elements of $A$, each element
$e \in Z$ has the following format:
$M \vdash \mathtt{WFF}_q(\theta, \phi, \psi)$. $M$ itself is a set of
WFFs that refer to $\theta, \phi, \psi$. For example, an element of $Z$
may look like this
$\\{\theta \Rightarrow \phi, \phi \Rightarrow \psi\\} \vdash \theta \Rightarrow \psi$.
[The list of human friendly inference
rules](https://en.wikipedia.org/wiki/List_of_rules_of_inference) is a
little long.

Now we have the vocabulary to describe membership of $D$. First of all,
by definition, $I \subseteq D$. Then we can utilize inference rules as
follows.

-   If

    -   $\exists a,b,c \in W$ (each of $a$, $b$, $c$ is well formed, but
        not necessarily derviable), and

    -   $\exists t \in Z$ (there is a transformation rule $t$) such that

    -   $t=M \vdash \mathtt{WFF_q}(\theta, \phi, \psi)$ (to define where
        $M$ and $\mathtt{WFF}_q$ come from), and

    -   $\forall \mathtt{WFF}(\theta, \phi, \psi) \in M(\mathtt{WFF}(a,b,c) \in D)$
        (using instantiations $\theta=a$, $\phi=b$, $\psi=c$, all
        templates of the constraint $M$ of the rule $t$ are derivable),

-   *then* \"fire the rule\", and establish membership
    $\mathtt{WFF}_q(a,b,c) \in D$ (label the \"new\" WFF as derivable).

The specification of the transformation rules (also called productions)
in $Z$ requires different matching mechanisms. This is why there are
three main categories of symbols in $A$.

-   Constants. A constant symbol is one where it is used in $I$ so that
    its truthfulness and the truthfulnesses of connectives using it are
    defined.

-   Variables. A variable symbol represents something that can be true
    or false, in other words, a proposition. The $I$ set may contain
    some variables that are known to be true.

-   Schmata. A schmata is a symbol that serves as a "wildcard" to match
    any WFF. As such, schemata symbols do not appear in WFFs in the WFF
    space, but they are used extensively in rules in $Z$.

# An (useful) example

Let us examine a concrete example, our "normal" Boolean algebra system.
In this system, the constants are $\\{0,1\\}$ where $0$ is false and $1$
is true. $\Omega_1 = \\{\neg\\}$ because negation is the only unary
operator. $\Omega_2 = \\{\wedge, \vee\\}$.

Variables are typically lower case English letters, conventionally
$\\{p,q,r,s,t\\}$.

Schemata symbols are typically lower case Greek letters, such as
$\\{\psi, \phi, \rho\\}$.

To express $0$ is false, we include $\neg 0$ in $I$. We also spell out
the operators and include the following WFFs in $I$:

-   $1 \wedge 1$

-   $1 \vee 1$

-   $1 \vee 0$

-   $0 \vee 1$

The transformation rules are syntactic patterns of Boolean algebra
rules. For example, we may have a rule like the following:

$\\{\psi, \phi\\} \vdash \psi \wedge \phi$

This rule is almost trivial, but it is important. This rule specifies
that if we can find two WFFs that are labeled true, then we can also
label the conjunction of those two WFFs (as a bigger WFF) true.

If you want to examine odd transformation rules, here is one:

$\\{\\} \vdash \phi \vee \neg \phi$

This means that without knowing anything to be true, we can label the
disjunction of any WFF and the negation of the WFF true.

Other transformations may include the more mundane ones to express rules
in Boolean algebra, for example, one half of DeMorgan's law looks like
the following:

$\\{\neg(\phi \vee \psi)\\} \vdash (\neg \phi) \wedge (\neg \psi)$

However, the transformation works in the opposite direction as well, we
have

$\\{\neg \phi, \neg \psi\\} \vdash \neg(\phi \vee \psi)$

You can imagine that $Z$ has quite a few rules. For a complete list of
rules in $Z$, you can visit
<https://en.wikipedia.org/wiki/Propositional_calculus#Example_2._Natural_deduction_system>.

Last, but not least, the variables and possibly WFF involving the
variables are included in $I$. This provides the semantics (meaning) to
the logic system.

Imagine that $p$ is "Tak is boring", $q$ is "half the class falls asleep
in CISP440". At this point, these are variables. We can also make $r$
mean "many students feel rejuvenated after CISP440".

Now we attach meanings to the otherwise syntactic system by including
the following WFFs in $I$:

-   $\neg p \vee q$: this is another way to say $p \Rightarrow q$, which
    literally means "Tak is boring implies half the class falls asleep
    in CISP440."

-   $\neg q \vee r$: this is another way to say $q \Rightarrow r$, which
    literally means "half the class falls asleep in CISP440 implies many
    students feel rejuvenated after CISP440."

The propositional system now has enough WFFs known to be true to apply
the transformation rules to eventually reach the conclusion that
$\neg p \vee r$ is a also a true WFF. Note that the conclusion is *not*
that "many students feel rejuvenated after CISP440", but the implication
"Tak is boring implies many students feel rejuvenated after CISP440."

By including different WFFs only involving variables, the propositional
system can come to different conclusions (which WFFs in the WFF space
are true).

## Another example

* $A=\\{0,1,p,q,r,s,t,\rho,\phi,\psi\\}$
* $\Omega=\\{\wedge, \vee, \Rightarrow, \neg \\}$
* $I=\\{1, \neg 0, (s \vee t) \Rightarrow q, \neg q\\}$, can we deduce anything about $s$ and $t$?
* $Z=\\{\\{\\} \vdash \psi \vee \neg \psi, \\{\phi \Rightarrow \psi, \neg \psi \\} \vdash \neg \phi, \\{\neg (\phi \vee \psi)\\} \vdash (\neg \phi) \wedge (\neg \psi), \\{\phi \wedge \psi\\} \vdash \phi, \\{\phi \wedge \psi\\} \vdash \psi \wedge \phi\\}$
	* $\phi = (s \vee t), \psi = q$,
		* fire $\\{\phi \Rightarrow \psi, \neg \psi \\} \vdash \neg \phi$,
		* label $\neg (s \vee t)$ as true
	* $\phi = s$, $\psi = t$,
		* fire $\\{\neg (\phi \vee \psi)\\} \vdash (\neg \phi) \wedge (\neg \psi)$,
		* label $(\neg s) \wedge (\neg t)$ as true
	* $\phi = (\neg s), \psi = (\neg t)$,
		* fire $\\{\phi \wedge \psi\\} \vdash \psi \wedge \phi$,
		* label $(\neg t) \wedge (\neg s)$ as true
	* $\phi = (\neg s), \psi = (\neg t)$,
		* fire $\\{\phi \wedge \psi\\} \vdash \phi$,
		* label $\neg s$ as true
	* $\phi = (\neg t), \psi = (\neg s)$,
		* fire $\\{\phi \wedge \psi\\} \vdash \phi$,
		* label $\neg t$ as true
* Conclusion: $s$ is false, $t$ is false

## An example using substitution to explain rule matching and firing

$A=\\{0,1,p,q,r,s,t,\phi,\rho,\psi\\}$
$\Omega=\\{\neg, \wedge, \vee, \Rightarrow\\}$
$I=\\{\neg 0,1,p \wedge q, q \Rightarrow r, \neg s \Rightarrow \neg r\\}$
* $p \in W$
* $p \wedge p \in W$
* $p \vee \neg p \in W$
* $\neg (u \in W)$

$Z=\\{\\{\\} \vdash \phi \vee \neg \phi,\\{\rho \wedge \phi\\} \vdash \rho, \\{\rho \wedge \phi\\} \vdash \phi, \\{\rho, \rho \Rightarrow \phi\\} \vdash \phi, \\{\neg \phi \Rightarrow \neg \rho, \rho\\} \vdash \phi\\}$
Each rule is like $T \vdash WFF(\phi, \rho, \psi)$
$I \subseteq D$, but what else are in $D$?

1. $\\{\rho \wedge \phi\\} \vdash \rho \in Z$, substitute: $\rho / p, \phi / q$, the RHS set matches $p \wedge q \in D$, now we can also claim $p \in D$
1. $\\{\rho \wedge \phi\\} \vdash \phi \in Z$, substitute: $\rho / p, \phi / q$, the RHS set matches $p \wedge q \in D$, now we can also claim $q \in D$
2. $\\{\rho, \rho \Rightarrow \phi\\} \vdash \phi \in Z$, substitute: $\rho/q, \phi/r$, confirm that $q \in D$, $q \Rightarrow r \in D$, fire the rule, confirm $r \in D$
3. $\\{\neg \phi \Rightarrow \neg \rho, \rho\\} \vdash \phi \in Z$, substitute: $\phi/s,\rho/r$, fire the rule, confirm $s \in D$
4. $\\{\\} \vdash \rho \vee \neg \rho$, $\rho/t$, fire the rule, confirm $t \vee \neg t \in D$

## Completeness and soundness

It is important to differentiate a transformation inference from a
logical implication. A transformation inference is a syntactic operation
that a computer can perform with great efficiency, it is expressed
simply in the form as follows:

$\\{\phi_1,\dots \phi_n\\} \vdash \psi$

This is also known as $\\{\phi_i,\dots \phi_n\\}$ syntactically entails
$\psi$.

*Semantic* entailment, on the other hand, is expressed as

$\\{\phi_1,\dots \phi_n\\} \models \psi$

It means that using conventional Boolean algebra, it can be proven that

$(\bigwedge_{i=1}^{n} \phi_i) \Rightarrow \psi$

Soundness means for each transformation in $Z$,
$(\\{\phi_1, \dots \phi_n\\} \vdash \psi) \Rightarrow (\\{\phi_1, \dots \phi_n\\} \models \psi)$.
This is essentially saying everything that the computer models is
correct in real life (Boolean algebra).

Completeness means that for each possible logical derivation using
Boolean algebra,
$(\\{\phi_1, \dots \phi_n\\} \models \psi) \Rightarrow (\\{\phi_1, \dots \phi_n\\} \vdash \psi)$.
Contrasting soundness, this means that everything that is doable using
Boolean algebra can also be accomplished by a computer using only
syntactic operations.

Of course, we want a propositional logic system to be both sound and
complete.

# Resolution

One issue with propositional logic in the context of automated reasoning
is that at any time, there is a large number of applicable
transformations. Furthermore, many transformations produce results that
do not get closer to the theorem to be proven.

As such, there are two specific issues. The first one is there is no
telling whether the automated theorem proving mechanism will stop. A
bigger problem is that it is difficult to show that a theorem is not
true because for all we know, the proving algorithm is still searching
for the theorem.

Resolution is a special production and mechanism that guarantees
algorithm termination within a reasonable amount of time.

## Resolution logic

Resolution works because of the following proof

$$\begin{aligned}
 (\phi \vee \psi) \wedge (\neg \psi \vee \rho) \Rightarrow (\phi \vee \rho) & =   \neg ((\phi \vee \psi) \wedge (\neg \psi \vee \rho)) \vee ((\phi \vee \rho)) \\ 
& =  \neg((\phi \vee \psi)) \vee \neg((\neg \psi \vee \rho)) \vee \phi \vee \rho \\ 
& =  (\neg \phi \wedge \neg \psi) \vee (\psi \wedge \neg \rho) \vee \phi \vee \rho \\ 
& =  (\neg \phi \wedge \neg \psi) \vee (\psi \wedge \neg \rho) \vee (\phi \wedge 1) \vee (\rho \wedge 1) \\ 
& =  (\neg \phi \wedge \neg \psi) \vee (\psi \wedge \neg \rho) \vee (\phi \wedge (\psi \vee \neg \psi)) \vee (\rho \wedge (\psi \vee \neg \psi)) \\ 
& =  (\neg \phi \wedge \neg \psi) \vee (\psi \wedge \neg \rho) \vee (\phi \wedge \neg \psi) \vee (\phi \wedge \psi) \vee (\rho \wedge \neg \psi)\vee (\rho \wedge \psi) \\ 
& =  ((\neg \phi \vee \phi) \wedge \neg \psi) \vee (\psi \wedge (\rho \vee \neg \rho)) \vee (\phi \wedge \psi) \vee (\rho \wedge \neg \psi) \\ 
& =  (1 \wedge \neg \psi) \vee (\psi \wedge 1) \vee (\phi \wedge \psi) \vee (\rho \wedge \neg \psi) \\ 
& =  \neg \psi \vee \psi \vee (\phi \wedge \psi) \vee (\rho \wedge \neg \psi) \\ 
& =  1 \vee (\phi \wedge \psi) \vee (\rho \wedge \neg \psi) \\ 
& =  1 
\end{aligned}$$

While this theorem is true for any WFF $\phi$, $\psi$ and $\rho$, it is
particularly helpful when we place the following restrictions:

-   $\psi$ is a single variable

-   $\phi$ is a disjunction of constants, variables or negation of
    variables

-   $\rho$ is a disjunction of constants, variables or negation of
    variables

Because the logic is sound, we can now introduce the following
transformation rule/production:

$\\{(\phi \vee \psi), (\neg \psi \vee \rho)\\} \vdash (\phi \vee \rho)$

With this, we only need the transformation rules corresponding to
commutative properties to arrange the ordering of items.

Furthermore, we also need to refine the qualification of a WFF:

-   $\Omega_1 = \\{\neg\\}$: Only negation is an element.

-   $\Omega_2 = \\{\vee\\}$: Only disjunction is an element. Conjunction
    is implied.

-   $\forall e \in A(\mathrm{isADE}(e))$: $\mathrm{isADE}$ means "is a
    disjunction element", meaning that any element of alpha can be a
    part of a disjunction.

-   $\forall e \in A(\mathrm{isADE}(\neg e))$: the negation of any
    element of $A$ can be a part of a disjunction.

-   $\forall i \in \\{1..n\\}(\mathrm{isADE}(\phi_i)) \Rightarrow
                \mathrm{isAWFF}(\bigvee\limits_{i=1}^{n} \phi_i)$: this
    is the most important part, a WFF is a disjunction of disjunction
    elements. There is no conjunction, and negation cannot be on the
    outside of a disjunction.

Note that all produced/inferred WFFs and every elements in $I$ are
implicitly connected by a conjunction. As a result, what is known to be
true is essentially a CNF (conjunctive normal form) where the overall
operator is a conjunction (but it is implied), and all components are
disjunctions. Each disjunction can only consist of elements in $A$ or
negations of elements in $A$.

## Completeness of CNF

Can any logic expression be converted into CNF? Resolution requires that
everything be represented in CNF to work.

Conceptually, CNF *has* to be complete. This is because any boolean
expression involving $n$ variables can be represented by a truth table
that has $2^n$ rows. There are $n+1$ columns, $n$ of them corresponding
to the $n$ variables, and the extra one corresponding to the value of
the expression based on the values of variables on that row.

Any additional term to a conjunction further restricts the value of the
original conjunction. The most concise way to expression this is that
for any boolean expressions $p$ and $q$, $(p \wedge q) \Rightarrow p$
and likewise, $(p \wedge q) \Rightarrow q$. All this is saying is that
it is not possible for $p \wedge q$ to be true but $p$ is false, and it
is impossible for $p \wedge q$ to be true but $q$ is false.

This means that each DE (disjunction element) in a CNF turns more rows
of the truth table corresponding to the value false ($0$). Once a row is
false, an even longer conjunction cannot make it true anymore.

Let $i$ be an integer from 1 to $n$, there are $n$ variables, and each
variable is represented by $v_i$. Furthermore, let $t_i$ be a term that
is based on variable $v_i$. $t_i$ can be $v_i$ or $\neg v_i$.

For each row of a truth table, we can create a DE as follows. Assume
$v_i$ corresponds to a boolean variable on a row in the truth table. If
and only if $v_i=1$ on this row, then the corresponding $t_i=\neg v_i$,
otherwise $t_i = v_i$. Using this method to define $t_i$ based on the
values of $v_i$ on a row of the truth table ensures that
$\bigvee_{i=1}^{n} t_i=0$ for this row.

For example, if a row corresponds to $p=0, q=1, r=1$, and the value of
the expression of the truth table of this row is $0$, then the
corresponding DE is $p \vee \neg q \vee \neg r$ because
$0 \vee \neg (1) \vee \neg (1)=0$. This method is repeated for every row
that evaluates to $0$, then all the DEs are joined by a conjunction to
make a CNF expression.

This mechanical method works, but it has a time complexity of $O(2^n)$
where $n$ is the number of variables.

Practically, using boolean algebra to turn a boolean expression into a
CNF is a little more messy, but this process can be faster when
completed by a competent practitioner. Generally speaking, a person can
use the following guide to turn an expression involving $\phi$ and
$\psi$ into its DEs:

-   $\phi \Rightarrow \psi$ becomes $(\neg \phi) \vee \psi$

-   $\phi \vee \psi$,
    $\mathrm{isAWFF}(\phi) \wedge \mathrm{isAWFF}(\psi) = 1$. We are
    done with this expression.

-   $\phi \vee \psi$,
    $\mathrm{isAWFF}(\phi) \wedge \mathrm{isAWFF}(\psi) = 0$. Apply the
    other rules.

-   $\phi \wedge \psi$, if the conjunction at the top level, separate
    $\phi$ and $\psi$ into two expressions and recursively work on those
    two expressions

-   $(\phi \wedge \psi) \vee \rho$: apply distribution so that we have
    $(\phi \vee \rho) \wedge (\psi \vee \rho)$.

-   $\neg(\phi \vee \psi)$: apply DeMorgan's law.

-   $\neg(\phi \wedge \psi)$: apply DeMorgan's law.

The conclusion is that every Boolean expression can be converted into
CNF. This conversion into CNF must be done to initialize $I$ so that the
propositional logic system start with the correct WFFs.

Another way to look at this is think of a "normal" Boolean WFF using the
usual operators. Then we think of a way to confirm or convert the WFF
$\phi$ into a CNF component:

-   top level operator is $\vee$:

    -   $\phi = \bigvee_{i=1}^{n}\psi_i$

    -   $\forall i\in \\{1..n\\} \mathrm{isADE}(\psi_i) \Rightarrow \mathrm{isAWFF}(\phi)$

    -   $\exists i\in \\{1..n\\} \neg\mathrm{isADE}(\psi_i)$:

        -   $\psi_i$ is a negation of a conjunction or disjunction:
            apply DeMorgan's law.

        -   $\psi_i$ is a conjunction: apply distribution law.

-   top level operator is $\wedge$: $\phi = \bigwedge_{i=1}^n\psi_i$, in
    this case, break them up so we evaluate each $psi_i$. In other
    words, $\forall i \in \\{1,\dots n\\}(psi_i \in I)$

-   top level operator is $\neg$: $\phi = \neg \psi$ there are three
    possibilities.

    -   $\psi \in A$: this means $\mathrm{isAWFF}(\phi)$.

    -   $\psi = \bigwedge_{i=1}^{n}\rho_i$: apply DeMorgan's law so that
        $\phi = \bigvee_{i=1}^{n}(\neg \rho_i)$, apply the steps again

    -   $\psi = \bigvee_{i=1}^{n}\rho_i$: apply DeMorgan's law so that
        $\phi = \bigwedge_{i=1}^{n}(\neg \rho_i)$, apply the steps again

For a list of Boolean algebra rules, you can refer to this rather
interesting page [Laws of Boolean Algebra and Boolean Algebra
Rules](https://www.electronics-tutorials.ws/boolean/bool_6.html).

In the process to convert from a general boolean expression into a CNF,
it is important to simplify as much as possible along the way.

### Example

Let us assume we have the following general Boolean WFF:

$\neg p \vee (\neg (r \Rightarrow q) \wedge (p \vee t))$

Here is how to convert it to components of a CNF:

$$\begin{aligned}
      & \neg p \vee (\neg (r \Rightarrow q) \wedge (p \vee t)) \\
    = & \neg p \vee (\neg (\neg r \vee q) \wedge (p \vee t))  \\
    = & \neg p \vee ((\neg \neg r \wedge \neg q) \wedge (p \vee t))  \\
    = & \neg p \vee ((r \wedge \neg q) \wedge (p \vee t)) \\
    = & \neg p \vee ((r \wedge \neg q \wedge p) \vee (r \wedge \neg q \wedge t))  \\
    = & \neg p \vee ((r \vee r) \wedge (r \vee \neg q) \wedge (r \vee t) \wedge
	             (\neg q \vee r) \wedge (\neg q \vee \neg q) \wedge (\neg q \vee t) \wedge 
		     (p \vee r) \wedge (p \vee \neg q) \wedge (p \vee t) ) \\
    = & (\neg p \vee r \vee r) \wedge (\neg p \vee r \vee \neg q) \wedge (\neg p \vee r \vee t) \wedge
	             (\neg p \vee \neg q \vee r) \wedge (\neg p \vee \neg q \vee \neg q) \wedge (\neg p \vee \neg q \vee t) \wedge
		     (\neg p \vee p \vee r) \wedge (\neg p \vee p \vee \neg q) \wedge (\neg p \vee p \vee t)  \\
    = & (\neg p \vee r) \wedge (\neg p \vee r \vee \neg q) \wedge (\neg p \vee r \vee t) \wedge
	             (\neg p \vee \neg q \vee r) \wedge (\neg p \vee \neg q) \wedge
		     (1) \wedge (1) \wedge (1)  \\
    = & (\neg p \vee r) \wedge (\neg p \vee r \vee \neg q) \wedge (\neg p \vee r \vee t) \wedge
	             (\neg p \vee \neg q \vee r) \wedge (\neg p \vee \neg q) \\
    = & (\neg p \vee r) \wedge (\neg p \vee \neg q)
      
\end{aligned}$$


### Observation

The most profound observation from this section is that *any* normal
Boolean WFF can be transformed into a CNF WFF. While the CNF version of
a WFF may not be as concise, it is, nonetheless, equivalent to the more
human-readable version. As we will see a little later, the CNF version
is far more easily processed by a machine that is only capable of
pattern matching.

## Exercise

Convert the following normal Boolean WFF into a CNF WFF:

$(\neg(p \vee q) \Rightarrow r) \vee (\neg q \Rightarrow (p \wedge t))$

## Proof by contradiction

Resolution is just a syntactic mechanism. It can be used to prove
theorems only because of the concept of proof by contradiction.

Proof by contradiction itself relies on a corollary shown and proven as
follows:

$$\begin{aligned}
  & (p \Rightarrow q) \Rightarrow ((p \wedge r) \Rightarrow (q \wedge r)) \\ & =  (\neg p \vee q) \Rightarrow (\neg (p \wedge r) \vee (q \wedge r)) \\ & =  \neg(\neg p \vee q) \vee ((\neg p \vee \neg r) \vee (q \wedge r)) \\ & =  (p \wedge \neg q) \vee (\neg p \vee \neg r \vee (q \wedge r)) \\ & =  (p \wedge \neg q) \vee (\neg p) \vee (\neg r) \vee (q \wedge r) \\ & =  (p \wedge \neg q) \vee (\neg p \wedge 1) \vee (\neg r \wedge 1) \vee (q \wedge r)  \\ & = (p \wedge \neg q) \vee (\neg p \wedge (q \vee \neg q)) \vee (\neg r \wedge (q \vee \neg q)) \vee (q \wedge r) \\ & =  (p \wedge \neg q) \vee (\neg p \wedge q) \vee (\neg p \wedge \neg q) \vee (\neg r \wedge q) \vee (\neg r \wedge \neg q) \vee (q \wedge r) \\ & =  (p \wedge \neg q) \vee (\neg p \wedge \neg q) \vee (\neg p \wedge q) \vee (q \wedge \neg r) \vee (q \wedge r) \vee (\neg q \wedge \neg r) \\ & =  (1 \wedge \neg q) \vee (\neg p \wedge q) \vee (q \wedge 1) \vee (\neg q \wedge \neg r) \\ & =  1 
\end{aligned}$$

All this shows is that we can perform the implication
$(p \Rightarrow q) \Rightarrow ((p \wedge r) \Rightarrow (q \wedge r))$

Now let us make a conjunction of all the known-to-be-true WFFs
$\psi = \bigwedge_{e \in I}^{}e$. Let $\phi$ be the theorem that we are
attempting to prove.

If $\psi \Rightarrow \phi$, then $\phi$ is a theorem. Using the
corollary shown above:

$$\begin{aligned}
      (\psi \Rightarrow \phi)  \Rightarrow \\
      ((\psi \wedge \neg \phi) \Rightarrow (\phi \wedge \neg \phi))  \Rightarrow \\
      ((\psi \wedge \neg \phi) \Rightarrow 0)
    
\end{aligned}$$

This means the conjunction of all elements of $I$ and the negation of
the theorem to be proven leads to a contradiction! This is a powerful
proof technique in general.

The converse is also important. If
$(\psi \wedge \neg \phi) \Rightarrow 0$, can we conclude that
$\psi \Rightarrow \phi$?

$$\begin{aligned}
      ((\psi \wedge \neg \phi) \Rightarrow 0) \Rightarrow \\
      (\neg (\psi \wedge \neg \phi) \vee 0) \Rightarrow \\
      ((\neg \psi) \vee (\neg \neg \phi)) \Rightarrow \\
      (\psi \Rightarrow \phi)
    
\end{aligned}$$

There we have it!

### Observation

Proof by contradiction is a powerful proof technique compared to direct
proofs. Let us take a look at an intuitive theorem that is rather
difficult to proof directly: [the pigeon hole
principle](https://en.wikipedia.org/wiki/Pigeonhole_principle).

### Exercise

In essence, the pigeon hole principle states that given $n$ pigeons and
$m$ holes and that $n>m$, then at least one hole has more than one
pigeons.

Sounds pretty intuitive, right? Well, prove it!

Hint: negate the theorem first. This means you need to first express the
theorem in a mathematical way. Since we have already discussed
functions, this is a great opportunity to apply what we have learned.

Let $N$ be a set of pigeons and $M$ be a set of holes. We are given that
$|N|>|M|$. Let $f:N \rightarrow M$ be an assignment function to assign a
pigeon to a hole. Prove that function $f$ cannot be injective.

Start with digging up the definition of a function and the property of
being injective. Then, assume $f$ is an injective function but maintain
the assumption that $|N|>|M|$. See if this combination implies false.

## Overall strategy

To use resolution and proof by contradiction, here is the roadmap:

-   convert all Boolean expressions in $I$ so that the overall system is
    a CNF (each expression is a disjunction of elements of $A$ or
    negations of elements of $A$).

-   negate the theorem to be proven, and turn that negated theorem into
    a CNF.

-   add the CNF of the negated theorem to $I$.

-   apply resolution (transformation) until no further transformation is
    possible or 0 (false) is produced.

### Example

Let's say we continue with our example above. The given is expressed as
follows:

$\psi = \neg p \vee (\neg (r \Rightarrow q) \wedge (p \vee t))$

But this is expressed as a CNF as follows:

$\psi = (\neg p \vee r) \wedge (\neg p \vee \neg q)$

The theorem that we want to prove is as follows:

$\phi = \neg t \Rightarrow p$

First, we need to express the *negation* of the theorem as a CNF:

$$\begin{aligned}
         & \neg \phi \\
       =  & \neg(\neg t \Rightarrow p) \\
       = & \neg((\neg \neg t) \vee p) \\
       = & (\neg \neg \neg t) \wedge \neg p \\
       = & \neg t \wedge \neg p
      
\end{aligned}$$

Then we form a "super CNF":

$$\begin{aligned}
        & \psi \wedge \neg \phi \\
      = & (\neg p \vee r) \wedge (\neg p \vee \neg q) \wedge (\neg t) \wedge (\neg p)
      
\end{aligned}$$

Now we apply resolution until there is nothing new to resolve to, or
when contradiction is concluded. However, resolution cannot even be
applied once because neither $t$ nor $p$ is in any disjunction (as a
component of the super CNF).

Because a contradiction cannot be reached, the proposed theorem is
invalidated.

Disappointed? Let's try another proposed theorem:
$\phi' = p \Rightarrow \neg q$.

First, we need to figure out the CNF of the negated theorem:

$$\begin{aligned}
        \neg \phi' & = \neg (p \Rightarrow \neg q) \\
	           & = \neg (\neg p \vee \neg q) \\
		   & = (\neg \neg p) \wedge (\neg \neg q) \\
		   & = p \wedge q
      
\end{aligned}$$

Again, we mix the CNF of $\neg \phi'$ with the given CNF:

$$\begin{aligned}
        \psi \wedge \neg \phi'  
	& =  (\neg p \vee r) \wedge (\neg p \vee \neg q) \wedge p \wedge q \\
	& =  (\neg p \vee r) \wedge (\underline{\neg p} \vee \neg q) \wedge \underline{p} \wedge q \wedge (\neg q) \\
	& =  (\neg p \vee r) \wedge (\neg p \vee \neg q) \wedge p \wedge \underline{q} \wedge (\underline{\neg q}) \wedge 0 \\
	& = 0
      
\end{aligned}$$

Ah, ha! This time we reach a contradiction. According to proof by
contradiction, this means the proposed theorem is actually implied by
the given facts.

# AI-generated questions

[This](https://chatgpt.com/share/670442d0-3034-8013-80b4-bd227f860774) is the prompt that generated these questions.

<details>
  <summary>1. What is a well-formed formula (WFF)?</summary>
  <p>A well-formed formula (WFF) is a syntactically correct expression in a logic system. It is constructed using symbols from a set $A$ and operators from a set $\Omega$, following specific rules.</p>
</details>

<details>
  <summary>2. How is a WFF recursively defined?</summary>
  <p>A WFF is recursively defined as follows: 
  - Any symbol from the set $A$ is a WFF.
  - If $c \in \Omega_n$ is an operator with $n$ arguments, and $\phi_1, \phi_2, \dots, \phi_n$ are WFFs, then $c(\phi_1, \dots, \phi_n)$ is also a WFF.</p>
</details>

<details>
  <summary>3. What does the transformation rule $\\{\psi_1, \dots, \psi_m\\} \vdash \phi$ mean?</summary>
  <p>This transformation rule means that if all the antecedents $\psi_1, \dots, \psi_m$ are true, then the consequent $\phi$ can be inferred as true.</p>
</details>

<details>
  <summary>4. What is the significance of the set $I$ in a propositional logic system?</summary>
  <p>The set $I$ contains all the WFFs that are known to be true (axioms). These WFFs provide meaning to the otherwise syntactic WFFs.</p>
</details>

<details>
  <summary>5. What are the three main types of symbols used in propositional logic?</summary>
  <p>The three main types of symbols are:
  - Constants: Fixed values, such as true (1) and false (0).
  - Variables: Propositions that can be true or false.
  - Schemata: Wildcards that match any WFF but do not appear in the WFF space.</p>
</details>

<details>
  <summary>6. How would you express the implication $p \Rightarrow q$ using a disjunction?</summary>
  <p>The implication $p \Rightarrow q$ can be expressed as a disjunction: $ \neg p \vee q $.</p>
</details>

<details>
  <summary>7. What is conjunctive normal form (CNF)?</summary>
  <p>Conjunctive normal form (CNF) is a way of expressing a Boolean formula where the formula is a conjunction of disjunctions of literals. Each clause in CNF is a disjunction, and the entire formula is a conjunction of those clauses.</p>
</details>

<details>
  <summary>8. Can any Boolean expression be converted into CNF? How?</summary>
  <p>Yes, any Boolean expression can be converted into CNF. This is done by using Boolean algebra rules, such as DeMorgan's laws and distribution, to simplify and transform the expression into a conjunction of disjunctions.</p>
</details>

<details>
  <summary>9. How does resolution work in propositional logic?</summary>
  <p>Resolution is a rule of inference that operates on clauses in CNF. It allows us to infer new clauses by eliminating a literal that appears positively in one clause and negatively in another. For example, from $(\phi \vee \psi)$ and $(\neg \psi \vee \rho)$, we can infer $(\phi \vee \rho)$.</p>
</details>

<details>
  <summary>10. What does it mean for a propositional logic system to be sound?</summary>
  <p>A propositional logic system is sound if every syntactic inference made by the system is semantically valid, meaning that if $ \\{\phi_1, \dots, \phi_n\\} \vdash \psi $, then $ \\{\phi_1, \dots, \phi_n\\} \models \psi $.</p>
</details>

<details>
  <summary>11. What does it mean for a propositional logic system to be complete?</summary>
  <p>A propositional logic system is complete if every semantically valid inference can also be derived syntactically. In other words, if $ \\{\phi_1, \dots, \phi_n\\} \models \psi $, then $ \\{\phi_1, \dots, \phi_n\\} \vdash \psi $.</p>
</details>

<details>
  <summary>12. What is the role of proof by contradiction in propositional logic?</summary>
  <p>Proof by contradiction involves assuming the negation of the theorem to be proven. If this assumption leads to a contradiction, then the original theorem must be true.</p>
</details>

<details>
  <summary>13. How would you negate the expression $p \vee q$?</summary>
  <p>Using DeMorgan's law, the negation of $p \vee q$ is $ \neg p \wedge \neg q $.</p>
</details>

<details>
  <summary>14. How would you negate the expression $p \wedge q$?</summary>
  <p>Using DeMorgan's law, the negation of $p \wedge q$ is $ \neg p \vee \neg q $.</p>
</details>

<details>
  <summary>15. Convert the Boolean expression $ \neg(p \vee q) \Rightarrow r $ into CNF.</summary>
  <p>First, express the implication as a disjunction: 
  $ \neg(\neg(p \vee q)) \vee r $. 
  Using DeMorgan's law: 
  $ (p \wedge q) \vee r $. 
  This is already in CNF form: $ (p \vee r) \wedge (q \vee r) $.</p>
</details>

<details>
  <summary>16. Convert the Boolean expression $ \neg(p \wedge q) \Rightarrow r $ into CNF.</summary>
  <p>First, express the implication as a disjunction: 
  $ \neg(\neg(p \wedge q)) \vee r $. 
  Using DeMorgan's law: 
  $ (p \vee q) \vee r $. 
  This simplifies to $ (p \vee r) \vee (q \vee r) $, which is in CNF.</p>
</details>

<details>
  <summary>17. What is a transformation rule in a propositional logic system?</summary>
  <p>A transformation rule in a propositional logic system is a syntactic rule that allows us to infer new WFFs based on a set of existing WFFs. The general form is $ \\{\psi_1, \dots, \psi_n\\} \vdash \phi $, where the antecedents imply the consequent.</p>
</details>

<details>
  <summary>18. What is the significance of resolution in automated theorem proving?</summary>
  <p>Resolution is important in automated theorem proving because it is a mechanical process that can be applied to clauses in CNF to infer new clauses. It guarantees that if a contradiction exists, it will be found, ensuring termination.</p>
</details>

<details>
  <summary>19. What is the time complexity of converting a Boolean expression to CNF using a truth table?</summary>
  <p>The time complexity of converting a Boolean expression to CNF using a truth table is $O(2^n)$, where $n$ is the number of variables in the expression.</p>
</details>

<details>
  <summary>20. How would you apply proof by contradiction to prove a theorem?</summary>
  <p>To apply proof by contradiction, you negate the theorem and add it to the set of known facts (in CNF form). Then, apply resolution to derive a contradiction. If a contradiction is found, the original theorem is proven to be true.</p>
</details>

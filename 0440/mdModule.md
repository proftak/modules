---
title: "Module 0440: Syntax and the Syntax to Describe Syntax"
---

# Context

* What is this?
  * This module describes what syntax means, and the syntax used to describe syntax.
* Why is this important?
  * On the path to learning how to program, understanding and applying the syntax of a programming language is important. Instead of using a "loose" pseudocode syntax, it is more efficient to "learn the real thing" from the get-go!
* How is this done?
  * This is accomplished by using a *meta* syntax language.
 
# Meta syntax

The syntax of a programming language is like the grammatical rules of the programming language. These rules are often specified by some form of meta syntax. One commonly used meta syntax is called [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) (Backus-Naur form). 

The syntax of C++ is intermediate compared to other programming languages. A plain BNF description of C++ can be difficult to follow. However, a BNF description that makes use of hyperlinks is considerably easier to follow. Fortunately, Alessio Marchetti has already created a [hyperlinked BNF description of the syntax of C++](https://alx71hub.github.io/hcb/).

## How to read the BNF notation

Each syntactic rule (also called a "production") consists of two parts:

* the token being defined
* what the token can be expanded to

Let us consider the following example. An [iteration-statement](https://alx71hub.github.io/hcb/#iteration-statement) is describe as follows:

|token|expansion|
|-|-|
|iteration-statment|**while (** condition **)** statement<br />**do** statement **while (** expression **);**<br /> **for (** for-init-statmentcondition<sub>opt</sub> **;** expression<sub>opt</sub> **)** statement<br />**for (** for-range-declaration **:** for-range-initializer **)** statement


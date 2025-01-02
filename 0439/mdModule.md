---
title: "Module 0439: OpenSCAD programming"
---

# _{{ page.title }}_

## What is this document?

This document describes how to use OpenSCAD from the perspective of a typical programmer.

## Syntax

### Action statement

While not the lowest level of language constructs, the action statement is a logical place to start the description of the syntax of OpenSCAD. Generally speaking, an action statement is similar to a C statement where it ends with a semi-colon (`;`), or it is a compound statement using braces (`{}`). However, unlike a C statement, an OpenSCAD action statement may have optional "operators." In certain OpenSCAD documentation, an "operator" is also called a "transformation." The term "transformation" describes the language construct better.

* The beginning of an action statement can have any number (including 0) of operators (transformations) using at least one space as a separator.
* `transformations ::= [ transformation " "... ]`
* After the transformations:
  *  A 2D or 3D object, terminated by a semi-colon (`;`) or
  *  A control structure

A control structure can be one of the following:

* `control-stmt ::=`
  * `"{" stmt* "}"`: a compound statement block
  * `"for" "(" var "=" "[" start ":" end "]" ")" stmt`
  * `"for" "(" var "=" "[" start ":" step ":" end  "]" ")" stmt`
  * `"for" "(" var "=" "[" value "," ... "]" ")" stmt`
  * `"if" "(" cond ")" stmt`
  * `"let" "(" var-decl "," ...")" stmt`
  * `atom ";"`

An action statement is, therefore:

* `stmt ::= transformations control-stmt`

### Variables

The term "variable" has a different meaning in OpenSCAD. The value of a variable is constant in the same scope, determined by the last update of the variable within said scope. This is because OpenSCAD is a *functional* programming language, as opposed to an *imperative* programming language. Specifically, OpenSCAD has referential transparency.

As a result, stepping that involves self-referencing a variable is not allowed in OpenSCAD. This includes increment operators, compound assignments, and any assignment in which the right-hand side explicitly or implicitly references the right-hand side.

For convenience, one can view the term "variable" in OpenSCAD as "constant" in C. 

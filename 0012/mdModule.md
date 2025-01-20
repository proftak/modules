---
title: "Module 0012: Variables, assignment statements and sequences"
---

# About this module

-   Prerequisites:

-   Objectives: This module introduces the most basic elements of
    programming.

# Example

Let's start with an example of a mundane task that you want a computer
to perform for you. Here is the task:

-   Read credit card bill, assume the balance is $x$ dollars.

-   Write a check of $x$ dollars to the credit card company.

-   Deduct $x$ amount from available funds.

-   Add $x$ to the annual total expense for the credit card.

This is a simple example, yet it illustrates some algorithm concepts.
Let's see what kind of concepts are illustrated.

# Variable

A "variable", as the name implies, is an object that can hold a value,
and the value can change over time (hence variable). More formally, a
variable has the following attributes:

-   Name. The name of a variable has to be unique so that we can refer
    to each variable without any ambiguity.

-   Type. The type of a variable specifies what the variable can store.
    Note that some programming languages are "typed" and others are
    "typeless". C/C++ and Java are typed programming languages, while
    most scripting languages are not typed.

-   Value (state). The value of a variable is its content.

You can look at a variable as a miniature whiteboard that has a name.
The name of the whiteboard distinguishes a whiteboard from other
whiteboards. The content of a whiteboard is the value. The type of a
whiteboard is a constraints of what kind of data a whiteboard may
contain, such as "numbers", "names" and etc.

How many variables do we have?

$x$ is an obvious one. Although $x$ is a variable, its value does not
change as we perform the steps. Nonetheless, that's fine. $x$ is the
name, the type is "money", and the value is the amount shown on the
credit card bill.

We have other variables, too. For example, we need one variable to keep
track of the available funds. At this point, we can use any name we wish
for variables. "availableFunds" is the name of this variable, the type
is "money", and the value is the amount of available funds.

This is a good time to mention "camel case". Most programming languages
have restrictions of what characters can be used as a part of a variable
name. The space character is often not allowed because it is used to
separate lexicons (words) from each other. In order to combine words
into a variable name, "camel case" capitalize the first letter of each
word and concatenate (join) all the words together. Note that the first
word is usually not capitalized for variable names.

Yet another variable is the total expense for this credit card. We can
call the variable "aETotalExpense" (assuming the credit card is an
American Express card). The type is "money", and the value is the total
amount spent through the card from the beginning of the year.

# Expressions and assignment

The English description of the steps is not too bad, but we can use
expressions to make it better. Particularly, we can specify how to
change "availableFunds" and "aETotalExpense" as follows:

``` {.numberLines .algorithm language="algorithm" numbers="left"}
@ $\mathrm{availableFunds} \leftarrow \mathrm{availableFunds} - x$ @ 
@ $\mathrm{aETotalExpense} \leftarrow \mathrm{aETotalExpense} + x$ @
```

Does this look confusing? Let us look into this more closely.

## Assignment

An assignment (statement) is a step that updates the value of a
variable. It is usually expressed as follows:

$lhs \leftarrow rhs$

$lhs$ (left-hand-side) specifies which variable to update, whereas $rhs$
(right-hand-side) specifies the new value. The symbol $\leftarrow$ (left
arrow) indicates the direction of information flow (from the right hand
side to the left).

Note that the symbol $\leftarrow$ is replaced by `=` (the equal sign) in
most programming languages, including C, C++, Java, Perl, PHP, and
Visual Basic. The left arrow is used in this module because it avoid the
confusion with equality check.

In an assignment, the right hand side is always evaluated first, then
the value of the expression is used to update the variable specified on
the left hand side.

## Constant assignment

Let us take a step back and look at a simple assignment:

$\mathrm{aETotalExpense} \leftarrow 0$

This is probably something that needs to be done on January 1 every year
to reset the annual expense. The right hand side is a simple expressions
of 0, which is a constant. This value is used to update the variable
"aETotalExpense".

This means no matter what the value of the variable is before the
assignment, it *always* become 0 after the assignment executes.

## Self referencing assignment

Let us take a look at something more confusing:

$\mathrm{aETotalExpense} \leftarrow \mathrm{aETotalExpense} + x$

This is where things get a little bit confusing. If we had used the `=`
symbol for assignment, it would have been even more confusing! For this
example, let us assume "aE total expense" is \$263, and $x$ is \$71
before the assignment.

Remember, we always evaluate the right hand side first for assignment
statements. In this particular case, we need to evaluate
$\mathrm{aETotalExpense} + x$. Since we already know the values of these
two variables are \$263 and \$71, the answer is quite simple: \$334.

Next, we take the value from the right hand side, and use it to update
the variable specified by the left hand side. *It just so happens* that
the variable on the left hand side is "aETotalExpense". After the
assignment statement, the value of "aETotalExpense" becomes \$334.

In summary, the assignment statement updates the value of
"aETotalExpense" from \$261 to \$334.

# Visualizing Variables

One way to visualize the changes to variables is to use a "trace table".
A "trace table" is a table such that each column represents a variable,
and each row represents a step in the execution of an algorithm. Each
cell (the intersection of a row and a column) represents the value of a
variable *after* the statement executes.

To facilitate better tracing, we can add line numbers to algorithms,
such as the following:

``` {.numberLines .algorithm language="algorithm" numbers="left"}
@ $\mathrm{availableFunds} \leftarrow \mathrm{availableFunds} - x$ \label{algor:updateAvail} @
@ $\mathrm{aETotalExpense} \leftarrow \mathrm{aETotalExpense} + x$ \label{algor:updateTotal} @
```

This way, we can use a column in a trace table to identify statements.
In our example, the trace table should look like the following:

  line \#                                                                                           availableFunds   aETotalExpense
  ------------------------------------------------------------------------------------------------- ---------------- ----------------
  pre                                                                                               261              0
  [\[algor:updateAvail\]](#algor:updateAvail){reference-type="ref" reference="algor:updateAvail"}   190              0
  [\[algor:updateTotal\]](#algor:updateTotal){reference-type="ref" reference="algor:updateTotal"}   190              71

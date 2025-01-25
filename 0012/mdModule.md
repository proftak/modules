---
title: "Module 0012: Variables, assignment statements and sequences"
---

# About this module

-   Prerequisites: [Module 0440: BNF](../0440/mdModule.html)

-   Objectives: This module introduces the most basic elements of
    programming.

# Example

Let's start with an example of a mundane task that you want a computer
to perform for you. Here is the task:

-   Read the credit card bill, assuming the balance is `x` dollars.
-   Write a check of `x` dollars to the credit card company.
-   Deduct `x` amount from available funds.
-   Add `x` to the annual total expense for the credit card.

This is a simple example, yet it illustrates some algorithm concepts.
Let's see what kind of concepts are illustrated.

# Variable

A "variable", as the name implies, is an object that can hold a value,
and the value can change over time (hence variable). More formally, a
variable has the following attributes:

-   Name (also known as an "identifier"). The name of a variable has to be unique so that we can refer
    to each variable without any ambiguity.
-   Type. The type of a variable specifies what the variable can store.
    Note that some programming languages are "typed" and others are
    "typeless". C/C++ and Java are typed programming languages, while
    most scripting languages are not typed.
-   Value (also known as state). The value of a variable is its content.

You can look at a variable as a miniature whiteboard that has a name.
The name of the whiteboard distinguishes a whiteboard from other
whiteboards. The content of a whiteboard is the value. The type of a
whiteboard is a constraint of what kind of data a whiteboard may
contain, such as "numbers", "names" etc.

How many variables do we have?

`x` is an obvious one. Although `x` is a variable, its value does not
change as we perform the steps. Nonetheless, that's fine. `x` is the
name, the type is "money", and the value is the amount shown on the
credit card bill.

We have other variables, too. For example, we need one variable to keep
track of the available funds. At this point, we can use any name we wish
for variables. `availableFunds` is the name of this variable, the type
is "money", and the value is the amount of available funds.

This is a good time to mention the "camel case". Most programming languages
have restrictions on what characters can be used as a part of a variable
name. The space character is often not allowed because it is used to
separate lexicons (words) from each other. In order to combine words
into a variable name, "camel case" capitalizes the first letter of each
word and concatenates (joins) all the words together. Note that the first
word is usually not capitalized for variable names.

Yet another variable is the total expense for this credit card. We can
call the variable `aeTotalExpense` (assuming the credit card is an
American Express card). The type is "money", and the value is the total
amount spent through the card from the beginning of the year.

# Expressions and assignment

The English description of the steps is not too bad, but we can use
expressions to make it better. Particularly, we can specify how to
change "availableFunds" and "aeTotalExpense" as follows:

```c
availableFunds = availableFunds - x;
aeTotalExpense = aeTotalExpense + x;
```

Does this look confusing? Let us look into this more closely.

## Assignment

An assignment is a step that updates the value of a
variable. It is usually expressed as follows in BNF:

* *`assignment`* ::= *`lhs`* **=** *`rhs`*

*`lhs`* (left-hand-side) specifies which variable to update, whereas *`rhs`*
(right-hand-side) specifies the new value. The terminal **=** is called the
"assignment operator". The operation is to first evaluate *`rhs`*, get the value, then update *`lhs`* using this value.

The use of **=** to represent "copy *`rhs`* to *`rhs`*" can be confusing because, in mathematics, the equality symbol $=$ does not change a value, but rather it *compares* two values and reports whether the two values are the same. 

The actual BNF of the assignment operator in C++ is quite complex. For now, we assume the following:

* *`lhs`* ::= *`varName`*
* *`rhs`* ::= *`expression`*

*`varName`* is a token to represent a "variable name." A variable name can start with a lowercase or uppercase letter or the underscore symbol, followed by any number of lowercase or uppercase letters, the underscore symbol, and any digit. As such, technically, we can define the following:

* *`varName`* ::= *`identifier`*
* *`digit`* ::= **0** \| **1** \| **2** \| **3** \| **4** \| **5** \| **6** \| **7** \| **8** \| **9**
* *`lcase`* ::= **a** \| **b** \| ... **z**
* *`ucase`* ::= **A** \| **B** \| ... **Z**
* *`idFirstChar`* ::= *`lcase`* \| *`ucase`* \| **_**
* *`idRestChar`* ::= *`idFirstChar`* \| *`digit`*
* *`identifier`* ::= *`idFirstChar`* *`idRestPortion`*<sub>opt</sub>
* *`idRestPortion`* ::= *`idRestChar`*
* *`idRestPortion`* ::= *`idRestPortion`* *`idRestChar`*

If this is cumbersome, the BNF of *`expression`* is much worse! For now, we will simply assume that *`expression`* can be any "common mathematical expression."

But what about the semi-colon? In C/C++ and all derived languages, assignment is an *expression*, not a *statement*. In order to turn an expression into a statement, a semi-color is needed. In other words:

* *`assignmentStmt`* ::= *`assignment`* **;**

## Constant assignment

Let us take a step back and look at a simple assignment:

```c
aeTotalExpense = 0;
```

This is probably something that needs to be done on January 1 every year
to reset the annual expense. The right-hand side is a simple expression
of 0, which is a constant. This value is used to update the variable
"aeTotalExpense".

This means no matter what the value of the variable is before the
assignment, it *always* becomes 0 after the assignment executes.

## Self-referencing assignment

Let us take a look at something more confusing:

```c
aeTotalExpense} = aeTotalExpense + x;
```

This is where things seem confusing. For this
example, let us assume `aeTotalExpense` is \$263, and `x` (the balance of this month) is \$71
before the assignment.

Remember, we always evaluate the right-hand side first for assignment
statements. In this particular case, we need to evaluate
`aeTotalExpense + x`. Since we already know the values of these
two variables are \$263 and \$71, the answer is quite simple: \$334.

Next, we take the value from the right-hand side and use it to update
the variable specified by the left-hand side. *It just so happens* that
the variable on the left-hand side is `aeTotalExpense`. After the
assignment statement, the value of `aeTotalExpense` becomes \$334.

In summary, the assignment statement updates the value of
`aeTotalExpense` from \$261 to \$334.

# Visualizing Variables

One way to visualize the changes to variables is to use a "trace table".
A "trace table" is a table such that each column represents a variable,
and each row represents a step in the execution of an algorithm. Each
cell (the intersection of a row and a column) represents the value of a
variable *after* the statement executes.

To facilitate better tracing, we can add line numbers to algorithms,
such as the following:

```c
availableFunds = availableFunds - x;  // line 1
aeTotalExpense = aeTotalExpense} + x; // line 2
```

In C/C++ and most derived languages, two slashes `//` begins comments. Comments are content in a program that is not interpreted by the machine but rather only serve as annotations to a human reader. In this case, we are only using the comments to indicate the line number so that the trace table can reference the line.

This code is also a *sequence* (of statements). A sequence means that there may be multiple steps, and the order of the steps is important. 

This way, we can use a column in a trace table to identify statements.
In our example, the trace table should look like the following:

|line#|`availableFunds`|`aeTotalExpense`|
|:-|:-|:-|
|pre|261|0|
|1|190|0|
|2|190|71|
|post|190|71|

The word "pre" represents "pre-condition", this row represents the state of the variables before the code runs. Likewise, the word "post" represents "post-condition", this row represents the state of the variables after the entire code runs. The row that corresponds to line 1 reports the states of the variables *after* the execution of line 1.

In essence, this "trace table" is like a reel of film, where each row is a frame. The trace table records all the changes to the variables throughout the execution of the code.

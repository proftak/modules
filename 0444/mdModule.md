---
title: "Module 0444: The Block Statement"
---

# Prerequisite

[Module 0013](../0013/mdModule.html)

# Rationale

In [Module 0013](../0013/mdModule.html), the conditional statement was introduced. One limitation of the conditional statement is that it only permits the specification of one statement to execute when the condition is true and, optionally, another one to execute when the condition is false.

In the examples, only one assignment statement was needed for each then-statement and each else-statement. But What if multiple statements are needed? This module introduces the "block statement" that acts as a container (think of it like a folder).

# The Syntax

The syntax related to a block statement *`blkStmt`* is as follows:

* *`statement`* ::= *`blkStmt`*
* *`blkStmt`* ::= **{** *`statements`*<sub>opt</sub> **}**
* *`statements`* ::= *`statement`* | *`statements`* *`statement`*

# An example

In this example, assume the condition is `x != y`, and the statements to execute if-and-only-if the condition is true are as follows:

* `x = x * 2;`
* `y = y - 1;`

It is not uncommon for a beginner to write the code as follows:

```c
if (x != y)   // line 1
  x = x * 2;  // line 2
  y = y - 1;  // line 3
```

The indentation of this code *suggests* that lines 2 and 3 both execute if-and-only-if `x != y`. However, because only one statement is expected after the condition of a conditional statement, only line 2 is the then-statement of the conditional statement. This leaves line 3 to be *independent* of the conditional statement. In other words, line 3 *always* executes after the conditional statement concludes. To better visualize this situation, the above code should be properly rewritten as follows so that the indentations reflect the nesting of the code:

```c
if (x != y)   // line 1
  x = x * 2;  // line 2
y = y - 1;  /  / line 3
```

In order to execute both lines 2 and 3, if-and-only-if `x != y, we can use a block statement to contain those two lines. The following code illustrates how to use a block statement.

```c
if (x != y)   // line 1
{             // line 1.5
  x = x * 2;  // line 2
  y = y - 1;  // line 3
}             // line 3.5
```

Note how the braces (`{}`) were introduced on lines 1.5 and 3.5 to enclose and contain the two lines of code that belong in the then-statement.

Aesthetically speaking, most people put the open brace on the same line as the beginning of the conditional statement, therefore the code is often formatted as follows:

```c
if (x != y) { // line 1
  x = x * 2;  // line 2
  y = y - 1;  // line 3
}             // line 3.5
```

# Best practice

The best practice is always to use a block statement where there *may* be a need to specify multiple statements. Using a block statement when the block only contains one, or even no, statement does not waste execution time. However, this approach makes it much easier to insert additional code without worrying about the "one-statement" limitation. 

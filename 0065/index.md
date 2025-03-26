---
title: "Module 0065: Subroutines (functions) control flow"
---

# About this module

-   Prerequisites:
-   Objectives: This module explores the concept of subroutine (aka functions in C/C++). It
    focuses only on the control flow portion. Another module will
    introduce the concept of parameters.

# Why?

In programming, copy-and-paste is not a good approach to "reusing" code. This is because of several reasons:

* It is not space-efficient. Each copy of copy-and-paste uses up code space. However, modern computing hardware has less space concern due to the availability of resources.
* The code that is copied and pasted may be flawed. If this code is duplicated many times, then all the copies also need to be fixed once the flaws of the original are discovered. This leads to maintenance issues.

# The `main` function

Up to this point, we have been writing C++ code without any functions. In C/C++, code cannot exist outside of a function! A function of the name `main` is the entry point of code execution of an entire program. The following is the shell of a minimalist `main` function:

```c
int main() {  // line 1
  return 0;   // line 2
}             // line 3
```

Here is an explanation of this minimalist shell:

* Line 1 is the beginning of the definition of the `main` function.
  * The word `int` signifies that the `main` function returns an integer value. More on the return value later.
  * The word `main` is the name of the function.
  * The parentheses `()` are needed to specify there are no *parameters* for this function. The concept of parameters will be explained in a different module.
  * The open brace `{` marks the block statement that becomes the body of the `main` function definition.
* Line 2 specifies a return value of 0:
  * A return value is a rather complex concept; it will be discussed in different modules.
  * A return value of 0 (zero) means there is nothing wrong. This value is called the *exit code* of a program. An exit code of 0 tells the operating system that this program completes "normally."
* Line 3 is the close brace `}` that marks the end of the definition of the `main` function.

# An example of function invocation

Consider the following code:

```c
void f() {    // line 1
}             // line 2

int main() {  // line 3
  f();        // line 4
  f();        // line 5
  return 0;   // line 6
}
```

There are two functions defined in this program: `f` and `main`. Function `f` has a return type of `void`, meaning it does not have a return value. Also, note the empty block statement spanning from line 1 to line 2. 

The function `main` is no longer just a shell. Lines 3 and 4 are *calls* to the function `f`. The verb "call" is also interchangeable with "invoke". It is best to take a look at the trace of this code to understand what "calling" or "invoking" means.

|line #|Comments|
|-|-|
|3|`main` is the entry point of an entire program|
|4|Invoke the function `f`|
|1|Execution continues at the entry point of the invoked function|
|2|The invoked function completes|
|5|When an invoked function completes, execution continues immediately after the invocation ("returning to the caller"). In this case, there is a second invocation of function `f`.|
|1|Execution continues at the entry point of the invoked function|
|2|The invoked function `f` completes|
|6|When an invoked function completes, execution continues immediately after the invocation.|
|post|When `main` returns, the program execution completes|

But how does the computer know where to return to from the function? In other words, in the first invocation, line 2 leads to line 5. However, in the second invocation, line 2 leads to line 6.

# Dynamically allocated columns in a trace

We need to modify how code is traced to explain how a called function knows where to return. First, we move the "comments" column to the left. This allows the right side to expand and contract as necessary. Second, we introduce a way to document how columns can be dynamically allocated and deallocated.

The following is a trace that corresponds to the C++ code introduced earlier:

|comments             |line&nbsp;#|<span style="color: transparent;">ret_line_#</span>|
| ------------------- | ----- | --------------- |
| |3| |
|invoke `f`, remember where to return to|4|**ret line #**|
|remember to return to line 5 when function `f` completes| |5|
|continue execute in function `f`|1| |
|function `f` completes, use the right-most column to indicate where to return to, and deallocate it|2|~~ret line #~~|
|now execution returns to the caller, but line 5 is another invocation, so the previously deallocated column is reallocated|5|**ret line #**|
|after the second invocation of `f`, remember to return to line 6| |6|
|continue execution in function `f`|1| |
|function `f` completes, use the right-most column to indicate where to return to, and deallocate it|2|~~ret line $~~|
|now execution returns to the caller|6| |
|all done|post| |

## To invoke a function

1. Dynamically allocate the next available column on the right-hand side and label it "ret line #" (return line number).
2. On the following row, remember the line number to return to on the newly allocated column
3. Continue execution on the first line of the invoked function

## To return when a function completes

1. Locate the right-most column that is labeled "ret line #".
2. Copy-and-paste the return line number to the "line #" column **of the next row**
3. Use strike-out style to indicate the "ret line #" column is now deallocated, like "~~ret line #~~"
4. Once a column is deallocated, it becomes available again.

# How are functions useful?

As illustrated [in the example](#an-example-of-function-invocation), functions provide a mechanism to execute the same block of code (in the example, the code contained in function `f`) at multiple points of invocation. This ability reduces, and in many cases eliminates, the copy-and-paste method.

At the same time, the ability to name a block of code and separate it from the context in which this block of code is used helps to reduce the apparent complexity of algorithms. This is similar to the outlining approach when writing an essay. A function serves as a "main point to be expanded" so that the writer (developer) can focus on a few items and how they relate to each other at any time.

# What about the variables?

The introduction of functions also adds a new dimension to the concept of variables that will be discussed in a different module.



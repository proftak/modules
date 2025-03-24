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


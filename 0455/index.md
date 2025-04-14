---
title: "Module 0455: Parameters"
---

Prerequisite: [0454](../0454)

# What is a parameter?

A parameter is similar to a local variable. However, unlike a local variable, the value of a parameter is specified by the caller. This allows caller-to-function communication.

# An example

Observe the following code:

```c
int add(int x, int y) {  // line 1
  return x+y;            // line 2
}                        // line 3
int main() {             // line 4
  int x;                 // line 5
  x = add(23,56);        // line 6
  return 0;              // line 7
}                        // line 8
```

The function definition starting on line 1 includes two parameters, `x` and `y`. Parameters are specified in the parentheses of a function definition, comma-separated. Each parameter has its own type specifier. In this case, `x` and `y` are both integers. Line 2 references the parameters, computes the sum, and returns the sum as the return value.

The trace is as follows:

|comments|line#|<span style="color:transparent" markdown=1>`x`</span>|<span style="color:transparent" markdown=1>`x`</span>|<span style="color:transparent" markdown=1>`y`</span>|<span style="color: transparent;" markdown=1>return</span>|
|-|-|-|-|-|-|
| |5|`x`|
| | |?|
|each parameter is a column, and the values in the invocation are used to initialize the parameters based on their positions|6| |`x`|`y`|return|
| | | |23|56|6: `x=?;`|
| |16| |  |  |         |
| |17| |  |  |6: `x=79;`|
|parameters are deallocated upon returning|  | |~~`x`~~|~~`y`~~|~~return~~|
| |6: `x=79;`|79|
| |7|~~`x`~~|
| |post|

# General rules related to parameters

Invoking a function with parameters requires the caller to specify the values of the parameters (each value is called an argument). The parameters are allocated in a trace before `return` or `ret line #`. When the function is executed, the parameters are accessed like local variables.

Parameters are deallocated when a function returns.



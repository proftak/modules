---
title: "Module 0451: Local variables"
---

Prerequisite: [module 0065](../0065)

# The meaning of "local"

A local variable is "local" because of the "scope" of visibility. A local variable has the scope of the block statement in which the variable is defined. Because the definition of a function is a block statement, the local variables of one function are out of scope from another function.

Though not always the case, a local variable is also local in lifespan.

These descriptions of local variables can sound abstract. It is best to illustrate these concepts using an example. Let us observe the following algorithm:

```c
void f() {    // line 1
  int x;      // line 2
  x = 2;      // line 3
}             // line 4
              // line 5
int main() {  // line 6
  int x;      // line 7
  f();        // line 8
  x = 5;      // line 9
  f();        // line 10
  return 0;   // line 11
}             // line 12
```

Lines 2 and 7 are definitions of variables. Let's take a closer look at one of these lines (they are identical):

* `int`: this is the abbreviation of "integer", this is the *type* of the variable being defined.
* `x`: this is the name (identifier) of the variable being defined.
* `;`: this is required by the syntax to end the definition of a variable

Like the "ret line #" (return line number), local variables are allocated and deallocated dynamically. This is best illustrated in the following trace of the above algorithm:

|comments|line&nbsp;#| | | |
|-|-|-|-|-|
|`main` is the entry point of execution|6|
|`x` is allocated| |**`x`**|
|the value of `x` is unknown initially| |?|
|invoke `f`| | |**ret&nbsp;line&nbsp;#**|
|remember to return to line 9 in the first invocation of `f`| | |9|
|`f` starts to execute|1| |
|`x` is allocated for `f`|2| | |**`x`**|
| | | | |?|
|assignment|3| | |2|
|`f` completes, deallocate both `x` and `ret line #`|4| |~~ret&nbsp;line&nbsp;#~~|~~x~~|
|`f` returns to line 9|9|5|
|invoke `f`| | |**ret&nbsp;line&nbsp;#**|
|remember to return to line 11 in the second invocation of `f`| | |11|
|`f` starts to execute|1| |
|`x` is allocated for `f`|2| | |**`x`**|
| | | | |?|
|assignment|3| | |2|
|`f` completes, deallocate both `x` and `ret line #`|4| |~~ret&nbsp;line&nbsp;#~~|~~x~~|
|the algorithm completes|11|
| |post|

# How to look up a local variable

When a local variable is referenced, such as lines 3 and 9 of the previous example, the following mechanism is used to find the column associated with the referenced local variable:

1. Locate the rightmost `ret line #` column.
2. Search for the column labeled with the variable's name.

These steps allow you to resolve which `x` to use on line 3. When line 3 executes, there are two columns labeled `x`. Following the above instructions, only the most recently allocated column labeled `x` is updated.

*Generally speaking* when a variable is referenced, it refers to the rightmost column (that is not deallocated) labeled with the variable's name.

# The allocation and deallocation of local variables

A function allocates local variables *after* it starts execution. The following are the steps to allocate a local variable `x`:

1. Find the leftmost available column.
2. Label the column with the name of the variable `x`.
3. In the next row, put a question mark `?` in the column to indicate the variable starts with an unknown value.

A function deallocates local variables when it completes and is ready to return to the caller. Technically, local variables are deallocated before the `ret line #` column. However, for all practical considerations, we can consider local variables and the `ret line #` column are deallocated at the same time.

# Global variables

If there are *local* variables, there must be *global* variables.

While C++ does support global variables, developers generally avoid using them. There are many reasons to avoid using global variables, but these reasons are difficult to understand in a beginning class.

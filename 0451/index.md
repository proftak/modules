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

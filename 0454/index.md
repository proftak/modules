---
title: "Module 0454: Functions that return a value"
---

Prerequisite: [0065](../0065) and [0451](../0451)

# Rationale

A function is a block of code that performs a specific operation. As a result, a function has some information to return to the caller. There are different mechanisms for a function to return information to the caller; the simplest and most commonly used mechanism is via a "return value."

# An example

Let us consider the following code:

```c
int chuht() {               // line 1
  return 7;                 // line 2
}                           // line 3

int m_ng() {                // line 4
  return 5;                 // line 5
}                           // line 6

int main() {                // line 7
  int x;                    // line 8
  x = chuht() + m_ng();     // line 9
  return 0;                 // line 10
}                           // line 11
```

The idea of a function that returns a value is that the value returned by the function can take the place of any value of return value type. The return value type of a function is the first word in the definition of a function. In the sample program, __`int`__ of line 1 indicates the return value type of function "chuht". 

Because integers can be used on both sides of addition, the invocation of function "chuht" is on the left-hand side of the addition. Likewise, the return type of function `m_ng` is also __`int`__, and as a result, the invocation of `m_ng` can be on the right-hand side of the addition of line 9.

# Tracing function calls to keep track of return values

The trace of the previous sample program is as follows:

|comments|line#|<span style="color:transparent;" markdown=1>**`x`**</span>|<span style="color:transparent;" markdown=1>return</span>|
|-|-|-|-|
| |7|**`x`**|
| | |?      |
| |9|       |return|
|use '?' as a placeholder of where the returned value goes| |       |9: `x=?+m_mg();`|
| |1|       |      |
|the return statement replaces the return value place holder with the actual return value|2|       |9: `x=7+m_ng();`|
|the return statement *also* returns to the caller, copy-and-paste the filled return information to the "line #" column of the following row before deallocating the "return" column| |       |~~return~~|
|now continue the execution of line 9 as if the invocation of `chuht()` is a constant value of 7|9: `x=7+m_mg();`|       |**return**|
| | |       |9: `x=7+?;`|
| |4|       |           |
|the return statement replaces the return value place holder with the actual return value|5|       |9: `x=7+5;`|
|copy-and-paste the filled return information to the following line # column, then deallocate the "return" column| |       |~~return~~|
|the third time we get back to line 9 has no additional function invocations, proceed as usual|9: `x=7+5;`|12         |
| |10|
| |post|





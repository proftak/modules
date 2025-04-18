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

# Trace formatting

Up to now, there has been no need to reference columns in a trace. However, the following topic requires certain columns to be identified. As a result, it becomes necessary to name columns like in a spreadsheet. It is also helpful to be able to reference rows in some cases.

As a result, the format of the tracing of code is adjusted accordingly. For easier reference to line numbers, the algorithms will be represented in a spreadsheet as follows.

<div style="font-family: monospace;" markdown=1>

| |A|
|-|-|
|**1**|int&nbsp;f(int&nbsp;n)&nbsp;{|
|**2**|&nbsp;&nbsp;if&nbsp;(n<2)&nbsp;{|
|**3**|&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;1;|
|**4**|&nbsp;&nbsp;}&nbsp;else&nbsp;{|
|**5**|&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;n*f(n-1);|
|**6**|&nbsp;&nbsp;}|
|**7**|}|
|**8**|int&nbsp;main()&nbsp;{|
|**9**|&nbsp;&nbsp;int&nbsp;x;|
|**10**|&nbsp;&nbsp;x&nbsp;=&nbsp;f(3);|
|**11**|&nbsp;&nbsp;return&nbsp;0;|
|**12**|}|

</div>

The corresponding trace is as follows:

| |A|B|C|D|E|F|G|H|I|
|-|-|-|-|-|-|-|-|-|-|
|**1**||pre||||||||
|**2**||8|x|||||||
|**3**|||?|||||||
|**4**||10||n|return|||||
|**5**||||3|10: x=?;|||||
|**6**||1||||||||
|**7**|n<=1 is F|2||||||||
|**8**||5||||n|return|||
|**9**||||||2|5: return n*?;|||
|**10**||1||||||||
|**11**|n<=1 is F|2||||||||
|**12**||5||||||n|return|
|**13**||||||||1|5: return n*?;|
|**14**||1||||||||
|**15**|n<=1 is T|2||||||||
|**16**||3|||||||5: return n*1;|
|**17**||||||||n|return|
|**18**||5: return n*1;|||||5: return n*2;|||
|**19**||||||n|return|||
|**20**||5: return n*2;|||10: x=6;|||||
|**21**||||n|return|||||
|**22**||10: x=6;|6|||||||
|**23**||11||||||||
|**24**||post||||||||

# Another kind of parameter

The type of parameter discussed up to this point is "passed by value". The column representing the parameter has the *value* of the parameter. As such, this kind of parameter acts much like a local variable.

Although the return value of a function can be used to return the result of a function, many functions have more effects than can be reflected by a single return value. Other times, a function also needs to modify items that do not "belong" to it. Most programming languages, like C++, support a second type of parameter called "passed by reference".

A pass-by-reference parameter is a *reference* to something else. A change to a pass-by-reference parameter does not modify the column that represents the parameter but the column that the parameter references. Here is an example:

<div style="font-family: monospace;" markdown=1>

| |A|
|-|-|
|**1**|void&nbsp;f(int&nbsp;&n)&nbsp;{|
|**2**|&nbsp;&nbsp;n&nbsp;=&nbsp;n&nbsp;+&nbsp;1;|
|**3**|}|
|**4**|int&nbsp;main()&nbsp;{|
|**5**|&nbsp;&nbsp;int&nbsp;x;|
|**6**|&nbsp;&nbsp;x&nbsp;=&nbsp;5;|
|**7**|&nbsp;&nbsp;f(x);|
|**8**|&nbsp;&nbsp;return&nbsp;0;|
|**9**|}|

</div>

The corresponding trace is as follows:

| |A|B|*C*{: style="color: red;"}|D|E|
|-|-|-|-|-|-|
|**1**|Comments|line#||||
|**2**||pre||||
|**3**||4|x|||
|**4**|||?|||
|**5**||6|5|||
|**6**|parameter n is allocated like any other parameter|7||n|ret line #|
|**7**|note how column D is a reference to column C|||ref col *C*{: style="color: red;"}|8|
|**8**||1||||
|**9**|any reference to parameter n is deferred to column C|2|6|||
|**10**|parameter n is deallocated like any other parameter|3||n|ret line #|
|**11**||8||||
|**12**||post||||

## Exercise

Trace the following code:

```c
void f(int &x, int &y) {
  int t;
  t = x;
  x = y;
  y = t;
}
int main() {
  int j,k;
  j = 2;
  k = 5;
  f(j,k);
  return 0;
}
```

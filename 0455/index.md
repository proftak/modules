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

| |A|
|-|-|
|**1**|<span style=""font-family: monospace"" markdown=1>int&nbsp;f(int n) {</span>|
|**2**|<span style=""font-family: monospace"" markdown=1>&nbsp; if (n<2) {</span>|
|**3**|<span style=""font-family: monospace"" markdown=1>&nbsp;   return 1;</span>|
|**4**|<span style=""font-family: monospace"" markdown=1>&nbsp; } else {</span>|
|**5**|<span style=""font-family: monospace"" markdown=1>&nbsp;   return n*f(n-1);</span>|
|**6**|<span style=""font-family: monospace"" markdown=1>&nbsp; }</span>|
|**7**|<span style=""font-family: monospace"" markdown=1>}</span>|
|**8**|<span style=""font-family: monospace"" markdown=1>int&nbsp;main() {</span>|
|**9**|<span style=""font-family: monospace"" markdown=1>&nbsp; int x;</span>|
|**10**|<span style=""font-family: monospace"" markdown=1>&nbsp; x = f(3);</span>|
|**11**|<span style=""font-family: monospace"" markdown=1>&nbsp; return 0;</span>|
|**12**|<span style=""font-family: monospace"" markdown=1>}</span>|

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


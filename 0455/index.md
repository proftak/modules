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
|**17**||||||||~~n~~|~~return~~|
|**18**||5: return n*1;|||||5: return n*2;|||
|**19**||||||~~n~~|~~return~~|||
|**20**||5: return n*2;|||10: x=6;|||||
|**21**||||~~n~~|~~return~~|||||
|**22**||10: x=6;|6|||||||
|**23**||11|~~x~~|||||||
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
|**10**|parameter n is deallocated like any other parameter|3||~~n~~|~~ret line #~~|
|**11**||8|~~x~~|||
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

# General rules related to parameters

## Terminology

In a function definition, *parameters* are specified. `x` and `y` are parameters in the following function definition:

```c
int f(int x, int y) {
  return x+y;
}
```

In a function invocation, *arguments* are specified. `23` and `65` are arguments in the following function invocation:

```c
x = f(23,65);
```

## In an invocation

Both pass-by-value and pass-by-reference parameters require columns to be allocated, one for each parameter. The allocation of columns is the leftmost available column. After a column is allocated, it is labeled with the name of the parameter.

If a parameter of the called function is passed by value, then the argument in the function call is evaluated as a general expression. The value of the expression becomes the initial value of the column of the parameter.

If a parameter of the called function is passed by reference, then the argument in the function call should be something that can be on the left-hand side of an assignment. This means the argument should have a column associated with it. The column corresponding to the parameter should be documented as a reference to the column specified by the argument.

## When referenced

When a pass-by-value parameter is referenced, the value of the parameter is retrieved in the right-most column that is labeled by the name of the parameter.

When a pass-by-reference parameter is referenced, the value of the column that is referenced by the parameter is retrieved.

## When an invocation completes

When a function returns, all parameters are deallocated along with the `return` or `ret line #` columns.

# Arrays as parameters

In C/C++, arrays can *only* be passed by reference. Furthermore, an array passed as a parameter only knows where to find the first column corresponding to the array. Observe the following example:

<div style=""font-family: monospace;"" markdown=1>

| |A|
|-|-|
|**1**|int&nbsp;sumArray(int&nbsp;a[],&nbsp;int&nbsp;n)&nbsp;{|
|**2**|&nbsp;&nbsp;int&nbsp;sum;|
|**3**|&nbsp;&nbsp;int&nbsp;i;|
|**4**|&nbsp;&nbsp;i=0;|
|**5**|&nbsp;&nbsp;sum=0;|
|**6**|&nbsp;&nbsp;while&nbsp;(i<n)&nbsp;{|
|**7**|&nbsp;&nbsp;&nbsp;&nbsp;sum=sum+a[i];|
|**8**|&nbsp;&nbsp;&nbsp;&nbsp;i=i+1;|
|**9**|&nbsp;&nbsp;}|
|**10**|&nbsp;&nbsp;return&nbsp;sum;|
|**11**|}|
|**12**|int&nbsp;main()&nbsp;{|
|**13**|&nbsp;&nbsp;int&nbsp;x;|
|**14**|&nbsp;&nbsp;int&nbsp;b[5];|
|**15**|&nbsp;&nbsp;b[0]=4;|
|**16**|&nbsp;&nbsp;b[1]=2;|
|**17**|&nbsp;&nbsp;b[2]=6;|
|**18**|&nbsp;&nbsp;b[3]=1;|
|**19**|&nbsp;&nbsp;b[4]=8;|
|**20**|&nbsp;&nbsp;x=sumArray(b,3);|
|**21**|&nbsp;&nbsp;return&nbsp;0;|
|**22**|}|

A few lines are worth noting:

* line 14: this is how an array of integers is declared in C/C++.
* line 1: this is how to specify that the type of a parameter is an array of integers
* line 20: parameter `n` does not match the actual number of elements in array `b`


The trace corresponding to the above code is as follows:

| |A|B|C|D|E|F|G|H|I|J|K|L|M|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|**1**|Comments|line#||||||||||||
|**2**||pre||||||||||||
|**3**||12|x|b[0]|b[1]|b[2]|b[3]|b[4]||||||
|**4**|||?|?|?|?|?|?||||||
|**5**||15||4||||||||||
|**6**||16|||2|||||||||
|**7**||17||||6||||||||
|**8**||18|||||1|||||||
|**9**||19||||||8||||||
|**10**||20|||||||a|n|return|||
|**11**|||||||||ref col D|3|20: x=?;|||
|**12**||1||||||||||sum|i|
|**13**||||||||||||?|?|
|**14**||4|||||||||||0|
|**15**||5||||||||||0||
|**16**|i<n is T|6||||||||||||
|**17**||7||||||||||4||
|**18**||8|||||||||||1|
|**19**|i<n is T|6||||||||||||
|**20**||7||||||||||6||
|**21**||8|||||||||||2|
|**22**|i<n is T|6||||||||||||
|**23**||7||||||||||12||
|**24**||8|||||||||||3|
|**25**|i<n is F|6||||||||||||
|**26**||10|||||||||20: x=12;|||
|**27**|||||||||~~a~~|~~n~~|~~return~~|~~sum~~|~~i~~|
|**28**||20: x=12;|12|||||||||||
|**29**||21|~~x~~|~~b[0]~~|~~b[1]~~|~~b[2]~~|~~b[3]~~|~~b[4]~~||||||
|**30**||post||||||||||||

</div>



---
title: "Module 0054: Introduction to Arrays"
---

# About this module

-   Prerequisites: [0012](../0012), [0013](../0013), [0016](../0016)

-   Objectives: This module introduces the concept of arrays, as well as
    some simple algorithms that work on arrays.

# Why?

Let us first explore why arrays are useful. This can be illustrated
using an example.

The code that we need to find the maximum $m$ of two variables $a$ and
$b$ is simple. It is represented in the following algorithm.

```c
// an algorithm to find the maximum of 2 variables
if (a >= b)
  m=a;
else
  m=b;
```

If we add one more variable, $c$, then the algorithm gets more
complicated, as described in the following algorithm.

```c
// algorithm to find the maximum of three variables
if ((a >= b) && (a >= c))
  m=a;
else
  if ((b >= a) && (b >= c))
    m=b;
  else
    m=c;
```

What if we have given 20 values? 200 values? 2000 values?

As you can see, this approach does not "scale". In other words, the
algorithm becomes more and more complicated as the number of values
increases. However, if we use an array of numbers, then the algorithm is
much simple, as described in the following algorithm.

```c
// algorithm to find the maximum in an array of values
// assume there are "n" values in array "a"
i=0;
while (i < n) {
  if (a[i] > m)
    m=a[i];
  i=i+1;
}
```

Of course, the complexity of the algorithm that finds the maximum in an array of values doesn't appear to be much simpler than the
algorithm that finds the maximum of 3 variables. However, the array-based algorithm
works for 3 values, 30 values, 3000
values, and etc. *The same algorithm works for any number of values!*

# What is an array?

An array can be seen as one variable. However, it is actually the
composite of many elements. An C/C++ array has several attributes:

-   all elements in an array have the same type
-   each element has an index (number) to identify it from all other values in the same array
-   the index of the first element is 0
-   indices of elements must be contiguous (0, 1, 2, ...)
-   the number of elements in an array in C++ must be "given"
-   the last element in an array `a` has an index of "the number of elements in the array minus 1"
-   an element with index `i` in array `a` is represented as `a[i]`

Note that each element of an array can behave like a variable on its
own. You can use it on either side of an assignment, you can perform
mathematical operations, you can compare, etc.

# Initialization algorithm

Let us consider an algorithm that initializes an array so that all
elements become 0. This algorithm is illustrated in the following algorithm.

```c
// Algorithm to initialize all elements in an array to 0.
// Assume "n" is the number of elements in array "a"
i = 0;          // line 1
while (i<n) {   // line 2
  a[i] = 0;     // line 3
  i = i + 1;    // line 4
}
```

Let us analyze each line of code here.

-   line 1: this is the initialization of variable
    $i$. Variable $i$ is really just an integer variable. However, *the
    role* that it serves in this algorithm is the changing index. It
    tells us which element in the array should be initialized for each
    iteration fo the loop.
-   line 2 marks the beginning of a prechecking loop.
    The stay-in condition is `i<n`. This means that as soon as
    `i == n` is true, we exit the loop. This makes sense because the last
    element is `a[n-1]`, so when `i = n`, we are done.
-   line 3 changes one element in array `a` to 0. The
    most important part of this assignment is the use of the expression
    `i` to specify the index of the element. Because `i` changes
    (increments for each iteration), we can access a different element
    for each iteration of the loop.
-   line 4 increments `i`. This moves the index forward so we will be ready for the "next" element in the next     iteration. If we don't have this line, then `i` stays 0, and the
    loop won't exit! 
-   line 5 marks the end of the prechecking loop.

When we trace an algorithm involving an array, each element in the array
has its own column. This is hardly surprising because each element in an
array *is* an independent variable! This fact makes tracing an
algorithm involving an array rather tedious. A table/spreadsheet should
be used because the gridlines help significantly.

As an exercise, trace algorithm
[\[algorithm:init0\]](#algorithm:init0){reference-type="ref"
reference="algorithm:init0"}, assuming array $a$ has 3 elements.

# Searching for a value in an array

## Unsorted array

Given an unsorted array $a$ and a value $v$ to find, how do we know
whether the array has an element that matches the value $v$ or not?

Algorithm
[\[algorithm:inflinsearch\]](#algorithm:inflinsearch){reference-type="ref"
reference="algorithm:inflinsearch"} is the not-so-formal version.

``` {#algorithm:inflinsearch .numberLines .pseudocode language="pseudocode" numbers="left" label="algorithm:inflinsearch" caption="An informal algorithm to search for a value in an unsorted array."}
start with the first element
while there are more elements, and the current one does not match %$v$% do
    move on to the next element
end while
if we have exhausted all elements then
  conclude no element has a value of %$v$%
else
  conclude at least one element has a value of %$v$%
end if
```

Recall our technique of using an integer variable to control which
element we want to access. We an reapply that technique here. In fact,
we'll use the same variable $i$ for this purpose.

To start with the first element means $i$ should be initialized to 0.
Hence, we have $i \leftarrow 0$ as our first statement.

Next, let us consider the phrase "there are more elements." Since we
start with the first element, then as long as the index remains within
the range of 0 to $|a|-1$, there is at least one more element to
consider. Consequently, "there are more elements" translates to the
condition $i < |a|$. Note that we *cannot* use $i \le |a|$ because when
$i = |a|$, $a[i]$ is not defined anymore.

The next phrase to consider is "the current one does not match $v$". The
"current one" is an element controled by the indexing variable $i$. In
other words, the "current one" is simply $a[i]$. To say that $a[i]$ does
not match $v$ is to say $a[i] \ne v$.

As a result, the condition of the prechecking loop can be more formally
written as $(i < |a|) \wedge (a[i] \ne v)$.

The only thing to do in the loop is to move on the next element. Because
the current element is controled by the indexing variable $i$, to move
on to the next element is to bump $i$ up by 1. This means the action
"move on to the next element" is really just $i \leftarrow
    i + 1$.

In the conditional (if-then-else) statement, how do we know we have
exhausted all the elements in the array? If we have searched through the
array and no element matches, $i = |a|$, and that is the reason to exit
the prechecking loop. As a result, "we have exhausted all elements"
should be replaced by $i = |a|$.

Algorithm
[\[algorithm:linsearch\]](#algorithm:linsearch){reference-type="ref"
reference="algorithm:linsearch"} is the result of replacing all the
not-so-formal description with formal pseudocode.

``` {#algorithm:linsearch .numberLines .pseudocode language="pseudocode" numbers="left" label="algorithm:linsearch" caption="The formalized version of algorithm \\ref{algorithm:inflinsearch}."}
while %$(i < |a|) \wedge (a[i] \ne v)$% do
  %$i \leftarrow i + 1$%
end while
if %$i = |a|$% then
  // conclude no element in %$a$% has a value of %$v$%
else
  // conclude %$a[i]$% is the first element in %$a$% that has a value of %$v$%
end if
```

Again, it really helps to trace an algorithm. In this case, try to
consider $a$ as an array of 4 elements. Let's assume $a[0] = 2$,
$a[1] = 0$, $a[2] = 10$ and $a[3] = 1$.

Perform two traces. First, assume $v = 7$, trace. Then, assume $v = 0$,
trace.

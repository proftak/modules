---
title: "Module 0068: Recursive definitions and algorithms"
full-width: true
---

# About this module

- Prerequisites: [0035](../0035}

- Objectives: This module introduces the concept of recursive
  definitions and algorithms. It also discusses how we can prove the
  correctness of recursive algorithms by induction.

# What is recursion?

A recursive definition is one that involves the very definition that is
being defined. There are some well known ones.

Factorial can be recursively defined.
$\forall n \in \mathbb{Z^+}: (n \ge 1) \Rightarrow (n! = n(n-1)!)$ and
$0! = 1$. Using this recursive definition, we can compute the value of
$4!$ as follows:

$$\begin{eqnarray}
  4! & = & 4\cdot (3!) \\
     & = & 4\cdot (3\cdot(2!)) \\
     & = & 4 \cdot (3 \cdot (2 \cdot (1!))) \\
     & = & 4 \cdot (3 \cdot (2 \cdot (1 \cdot (0!)))) \\
     & = & 4 \cdot (3 \cdot (2 \cdot 1 \cdot 1)) \\
     & = & 4 \cdot (3 \cdot (2 \cdot 1)) \\
     & = & 4 \cdot (3 \cdot 2) \\
     & = & 4 \cdot 6 \\
     & = & 24
\end{eqnarray}$$

The name GNU is also recursively defined. However, in this case, it is
merely just for the sake of making it confusing. The definition of GNU
is "GNU is not Unix". Thus, expanding GNU twice gets "(GNU is not Unix)
is not Unix", expanding it three times get "((GNU is not Unix) is not
Unix) is not Unix", and so on. Obviously, there is no end to this. As a
result, we really don't know what GNU is.

# Recursive algorithms

## Factorial

The C version of the factorial function is as follows:

``` {.c language="c"}
unsigned f(unsigned n)
{
  int res;
  if (n > 0)
  {
    res = n * f(n-1);
  }
  else
  {
    res = 1;
  }
  return res;
}
```

## Pascal's triangle

The C version of finding the value of an element in Pascal's triangle is
as follows:

``` {.c language="c"}
unsigned pascal(unsigned r, unsigned c)
{
  unsigned res;
  if ((c == 0) || (c == r))
  {
    res = 1;
  }
  else
  {
    res = pascal(r-1,c-1) + pascal(r-1,c);
  }
  return res;
}
```

## Tower of Hanoi

Tower of Hanoi involves three poles. We can label these poles 1, 2 and
3. We start with a sorted stack of disks on pole 1, with the largest
disk at the bottom, and the smallest disk at the top. We can move one
disk from one pole to another pole in one move, but one restriction is
that we can only move the top disk from one pole so it becomes the top
disk of another pole. Another restriction is that only a smaller disk
can be on top of a larger disk.

How do we move all the disks from pole 1 to pole 3?

Let us try to figure out the algorithm. First, let us define the
following prototype:

    void hanoi(int n, int from, int to, int via);

It is the prototype of a function that moves `n` disks from pole `from`
to pole `to` through pole `via`. Is there a easy case? Sure! When `n` is
one, we can just move it without using the `via` pole:

``` {.c language="c"}
void hanoi(int n, int from, int to, int via)
{
  if (n == 1)
  {
    printf("move from pole %d to pole %d\n",from,to);
  }
}
```

What if `n > 1`? In other words, what if we need to move a whole bunch
of (`n`) disks from a source pole to a destination pole, given that we
can use an intermediate pole? It'd be easy if we can move `n-1` disks
from the source pole to the intermediate pole, then move the last disk
from the source pole to the destination pole, then move the `n-1` disks
from the intermediate pole to the destination pole.

This sounds easy, but how exactly are we going to move `n-1` poles from
the source pole to the intermediate pole? We can use the destination
pole as the intermediate pole! Using the same reasoning, we can move
`n-1` poles from the intermediate pole to the destination pole using the
source pole as an intermediate pole.

This means we can use `hanoi` to solve the two subproblems, but we need
to change the parameters a little in each case:

``` {.c language="c"}
void hanoi(int n, int from, int to, int via)
{
  if (n == 1)
  {
    printf("move from pole %d to pole %d\n",from,to);
  }
  else
  {
    hanoi(n-1, from, via, to); // note the change of params!
    hanoi(1, from, to, via); // recursion to use the base case
    hanoi(n-1, via, to, from); // note the change of params again!
  }
}
```

## Delete directory

Many operating systems do not allow the deletion of a directory that
still has files or other directories inside it. As a result, if we are
really sure that we want to delete a directory, we need to delete all
its files and subdirectories first. The problem is that the
subdirectories may contain subsubdirectories, and so on.

How can we do this as an algorithm? When we encounter a subdirectory, we
simply invoke the same function that is being used to delete the parent
directory!

``` {.c language="c"}
void nukedir(const char *name)
{
  DIR *pDir = opendir(name);
  if ((pDir == NULL) && (errno == ENOTDIR)) 
  {
    unlink(name);
  }
  else if (pDir != NULL)
  {
    struct dirent *entry;
    
    chdir(name);
    while ((entry = readdir(pDir) != NULL))
    {
      nukedir(entry->d_name);
    }
    closedir(*dir);
    chdir("..");
    rmdir(name);
  }
}
```

# When to consider recursion?

A recursive algorithm can be converted to an iterative one, and vice
versa. This is illustrated by the implementation of recursive algorithm
using languages that do not support recursion. On the other hand, Lisp
is a language that has no iterations (loops), but yet it can be used to
implement any algorithm that contains loops.

Consequently, technically speaking, there is no difference between a
recursive algorithm and its iterative counterpart.

However, to a computer scientist or a programmer, some algorithms are
more simple in their recursive form. This section explores what kinds of
problem lend themselves to recurisve solutions.

## Recursive definitions

Any algorithm to implement a recursive definition can be done
recursively. This is quite obvious! Recursion, Fibonacci, Pascal's
triangle are just a few examples.

## Self similar structure

Some data structures are self similar. This means the parent
(containing) structure is structurally similar to its children
(contained) structures. One example is a tree structure. Each branch is
a tree by itself.

A lesser known structure is a list. A non-empty list consists of a value
and "the rest of the list". "The rest of the list" is considered a list
by itself.

## Self similar action

A self similar action is an action that can be broken down to operations
that involve the same kind of action, but with different parameters. We
have already seen an example: tower of Hanoi. There are other algorithms
that fit in this category.

One algorithm is called depth-first-search. It is a search algorithm
that can work on any graph and state spaces.

# Practical issues with recursion

Although recursion may be the best form of solution, it is not always
practical. This section explains the limitations of recursion, and when
*not* to use recursion.

## Implementation

Recursion is possible because most languages maintain a context per
*invocation* of a subroutine, and not per subroutine. The "context" of
an invocation includes all parameters, all `auto` local variables, and
the return address. The entire context is saved on the stack.

Let us consider one of our examples, the Pascal's triangle code:

``` {name="pascal"}
int pascal(int r, int c)
{
  int res;
  if ((c == 1) || (c == r))
  {
    res = 1;             // pascal:basecase
  }
  else
  {
    res =                // pascal:assignres
      pascal(r-1,c-1) +  // pascal:recurcall1
      pascal(r-1,c);     // pascal:recurcall2
  }
  return res; // pascal:return
}
```

In this example, each invocation (call) of `pascal` saves at least this
much information on the stack:

- `r`: the row number of this invocation

- `c`: the column number of this invocation

- `res`: the result of this invocation

- `return address`: the return address to the caller

Let us consider the following code:

``` {name="pascal"}
void test(void)
{
  int i;

  i =            // pascal:assigni
    pascal(3,2); // pascal:testcall
}
```

When `pascal` is called the first time from line
`pascal:testcall`, the following context is constructed (we
omit the context of invoking `test` and all earlier contexts):

- `r = 3`

- `c = 2`

- `res = ?`

- return to line
 `pascal:assigni`

Then, the program executes the code in `pascal`. When `pascal` is
invoked again on line
`pascal:recurcall1`, a *new* context is constructed. At this
point, there are two contexts (the first one is the first one created):

- first context (bottom of stack):

  - `r = 3`

  - `c = 2`

  - `res = ?`

  - return to line
    `pascal:assigni`

- second context (top of stack):

  - `r = 2`

  - `c = 1`

  - `res = ?`

  - return to line
    `pascal:recurcall2`

Transfer is, once again, transferred to *the beginning* of `pascal`.
This time, because `c = 1`, we execute line
`pascal:basecase`. Immediately before we return on line
`pascal:return`, the stack looks like the following:

- first context (bottom of stack):

  - `r = 3`

  - `c = 2`

  - `res = ?`

  - return to line
    `pascal:assigni`

- second context (top of stack):

  - `r = 2`

  - `c = 1`

  - `res = 1`

  - return to line
    `pascal:recurcall2`

As we return, we naturally return to line
`pascal:recurcall2` to continue execution based on the return
address. Note that as soon as a subroutine returns, the invocation
context is removed from the stack. Thus, the intermediate state of the
stack is as follows (with only one context):

- first context (bottom of stack):

  - `r = 3`

  - `c = 2`

  - `res = ?`

  - return to line
    `pascal:assigni`
At this point, we have evaluated the left hand side of the additional
operator. We are now ready to evaluate the right hand side of the
addition operator.

Line `pascal:recurcall2` invokes `pascal` again, but this time the
parameters are different. We end up with the following contexts
immediately after the invocation on line
`pascal:recurcall2`:

- first context (bottom of stack):

  - `r = 3`

  - `c = 2`

  - `res = ?`

  - return to line
    `pascal:assigni`

- second context (top of stack):

  - `r = 2`

  - `c = 2`

  - `res = ?`

  - return to line
    `pascal:assignres`

Control now starts from the beginning of `pascal`. Because `c == r`, we
execute line
`pascal:basecase`, which changes the stack to the following
state:

- first context (bottom of stack):

  - `r = 3`

  - `c = 2`

  - `res = ?`

  - return to line
    `pascal:assigni`

- second context (top of stack):

  - `r = 2`

  - `c = 2`

  - `res = 1`

  - return to line
    `pascal:assignres`

When we reach line
`pascal:return`, we return to line
`pascal:assignres`. At this point, we are ready to compute
the addition of the assignment expression. Because both recursive calls
to `pascal` returned 1s, the sum is 2. As a result, we update `res` so
that the context is as follows:

- first context (bottom of stack):

  - `r = 3`

  - `c = 2`

  - `res = 2`

  - return to line
    `pascal:assigni`

After this, execution reaches line
`pascal:return`. As a result, we return a value of 2, and
execution continues on line
`pascal:assigni`. Subroutine `test` proceeds to store the
value of 2 in `i`.

## Implementation overhead

The context of an invocation is not limited only to the parameters and
local variables. It also includes the return address, as well as the
saved values of hardware registers. Compared to an iterative approach, a
recursive solution always has more storage overhead.

In terms of performance, however, a recursive implementation can be very
competitive with respect to a equivalent iterative implementation. This
is especially the case for a multi-point recursive solution (such as the
tower of Hanoi, as opposed to factorial).

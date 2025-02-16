---
title: "Module 0046: Pre and post conditions"
---

# About this module

-   Prerequisites: [0011](../0011/mdModule.html), [0012](../0012/mdModule.html), [0013](../0013)

-   Objectives: This module introduces the concepts of pre and post
    conditions for various types of statements.

# What is this crazy math?

So you thought it'd be easy to become a programmer.

There are two schools of thought regarding the role of mathematics in
programming. One school, led by Edsger Dijkstra, suggests that a
programmer should be a mathematician first. At the very least, every
programmer should have a solid foundation of mathematics. Furthermore,
computer science should be a branch of mathematics. For a more detailed
discussion of this topic, visit, and search for "cruelty computer
science".

Another school, including Donald Knuth (another giant and pioneer of
computer science), claims that with sufficient advances in tools,
everyone can program computers. This is at least partially true. In the
"good old days," programs are only written in machine language,
consisting of long strings of 0's and 1's. Later on, with symbolic
assemblers, writing programs became easier. These days, with Visual
Studio and other development environments, the tools actually help to
fix problems not only in syntax but also sometimes in the logic of
programs.

Nonetheless, it is still important for programmers to understand 
logic and mathematics. Programming by intuition is possible, but it only
enables a programmer to a certain level. If not for anything else, a
solid background in logic and mathematics enables a programmer to troubleshoot faulty programs with great efficiency. Most programmers who are
well-trained in mathematics also tend to design more elegant programs
that minimize the chances of errors to begin with.

# Pre and post conditions

A pre-condition is simply "what we know before the execution of a
statement in a program." A post-condition is "what we know after executing a statement in a program." The analysis of the pre and post-conditions of a program is essential, because we can prove the
correctness of a program (or an algorithm) rigorously.

If you consider an algorithm, the pre-condition of the entire algorithm
is what is given to the program. The post-condition of an entire
algorithm is the outcome of a program. Being able to mathematically
derive the post-condition of an algorithm based on its pre-condition
means we can prove whether an algorithm does what it is supposed to.
There is no need to use test cases because proof of
correctness covers *all* cases that can be thrown at the algorithm.

## Constant assignment

Let's start with something relatively simple to deal with.
Algorithm
`constant assignment` is just a sequence of assignment
statements.

```c
// algorithm constant assignment
x = 0; // line 1 constassign1:x0
y = 2; // line 2 constassign1:y2
x = 5; // line 3 constassign1:x5
y = 1; // line 4 constassign1:y1
```

Assuming this algorithm stands alone, there is no pre-condition to it.
In our notation, $\rm{pre(1)}$ represents the pre-condition of the
statement on line 1. Because line 1 is the first line of code,
$\rm{pre(1)}$ also represents the pre-condition of the entire algorithm.

Note that a pre-condition is a condition. It expresses something that is
true. How do we express truth when we don't know anything is true? Well,
we know something is always true, it is "true" itself!

Consequently, we can simply say that $\rm{pre(1)} = \rm{true}$.

What is the post-condition of line 1? Since this is a constant assignment
statement, we know that variable $x$ must end up with a value of 0. In
other words, we know that $x = 0$ after this statement. Consequently, we
"add" the fact to $\rm{pre(1)}$ so that
$\rm{post(1)} = \rm{pre(1)} \wedge (x = 0)$
If you look up the conjunction definition, $x \wedge true$ is simply
$x$. We can simplify our post condition so that
$\rm{post(1)} = (x = 0)$.

The same argument applies to line 1. Note that
$\rm{pre(2)} = \rm{post(1)}$
because there is nothing that can change what we know about the program
between the lines. What is $\rm{post(2)}$?

Line 2 changes variable $y$ to a constant of $2$.
We know that after line
2, $y = 2$. However, this is *not* the only
thing that we know. What we knew earlier that $x = 0$ is still true. As
a result, $\rm{post(2)} = (x = 0) \wedge (y = 2)$.

Here comes the tricky part. What is $\rm{post(3)}$?
If we simply add the fact that $x = 5$, then we end up with
$\rm{post(3)} = (x = 0) \wedge (y = 2) \wedge (x = 5)$.
However, this is impossible because $x = 0$ contradicts $x = 5$. What do
we need to do?

What we need is a way to "forget" some facts because a new fact is in,
and the new fact may contradict some old facts. This is accomplished by
a "forget" operation. let us define $\rm{forget(c,v)}$ to mean
forgetting all components in condition $c$ that refers to variable $v$.

In our example, we can now derive
$\rm{post(3)} = \rm{forget(\rm{post(2)},x)} \wedge (x = 5)$.
Literally, this means "the post-condition of line 3 is essentially the same as the post-condition of line 2, except that all components referring to
$x$ should be forgotten. Then, we add the fact that $x = 5$."

This results in the following derivation:

$\begin{aligned}
      \rm{post(3)} & = & \rm{forget(\rm{post(2)},x)} \wedge (x = 5) \\
                                   & = & \rm{forget((x = 0) \wedge (y = 2),x)} \wedge (x = 5) \\
                                   & = & (y = 2) \wedge (x = 5)
    
\end{aligned}$

Now, onto the last statement. We only have to reapply what we learned in
the previous step:

$\begin{aligned}
      \rm{post(4)} & = & \rm{forget(\rm{post(3)},y)} \wedge (y = 1) \\
                                   & = & \rm{forget((y = 2) \wedge (x = 5),y)} \wedge (y = 1) \\
                                   & = & (x = 5) \wedge (y = 1)
    
\end{aligned}$

Are you surprised at the result?

Let us consider the general case (`x`, `e` and `n` are all placeholders):

```c
x=e; // line n
```

Assuming $e$ does not refer to variable $x$ itself, then
$\rm{post(n)} = \rm{forget(\rm{pre(n)},x)} \wedge (x = e)$.

## Resolving references to variables to constants

If there are any "chainable" equalities, you should try to get
everything resolved to constants whenever possible. For example, let us
consider the following post-condition:

$\rm{post(1)} = (x < y) \wedge (y = 10)$

Here, we already know for sure that $y$ has a value of 10. This means
that the inequality $(x < y)$ can now be resolved as $(x < 10)$. The
main purpose of doing this is to decouple variables from each other. In
other words, we want to lessen the impact of a change to one variable on
conditions that involve other variables.

In this example, a later assignment can change the value of $y$.
However, that will not impact the fact that we already know that
$(x < 10)$.

## Simple self-referencing assignments

Now that we can handle constant assignments and a sequence, let's move
on to something *slightly* more interesting.

Let us consider algorithm `self-assignment 1`.

```c
// algorithm self-assignment 1
y = 2;   // line 1
x = x+3; // line 2 selfassign1:xp3
y = y-1; // line 3 selfassign1:ym1
```

Note that the first two statements of algorithm `self-assignment 1`
are the same as the first two
statements of algorithm `constant assignment`. Let's start with the first
statement that is different. We know that
$\rm{pre(2)} = (x = 0) \wedge (y = 2)$. What is the
$\rm{post(2)}$?

Let us examine what we are doing on line 2. In this assignment statement, we first
evaluate the right-hand side. $x = 0$ at this point, so $x + 3 = 3$.
Then, we take the value of 3 and use that to update $x$. In other
words, $x = 3$ after the statement.

In the analysis of post-conditions, we have a more obscure way to come to
the same conclusion.

First, let us define a "function" $f(x) = x + 3$. This is really just a
notation so that $f(3) = 6$, $f(-2) = 1$ and etc. When some functions,
we can also define an "inverse function". In this case, the inverse
function is $f^{-1}(x) = x - 3$. What this really means is simply that
$f^{-1}(f(x)) = x$. In other words, $f^{-1}$ undoes whatever $f$ does.

Next, let us define a substitution operation. $\rm{sub(c,x,y)}$ means
that in condition $c$, replace all occurances of $x$ with $y$. For
example, $\rm{sub(x + y = z,y,y-1)} = x + (y-1) = z$.

With these new tools, we can get back to work. Let us keep the
definition that $f(x) = x + 3$ and $f^{-1}(x) = x - 3$. Then, we have the
following derivation:

$\begin{aligned}
      \rm{post(2)} & = & \rm{sub(\rm{pre(2)},x,f^{-1}(x))} \\
                                   & = & \rm{sub((x = 0) \wedge (y = 2),x,x - 3)} \\
                                   & = & ((x - 3) = 0) \wedge (y = 2) \\
                                   & = & (x = 3) \wedge (y = 2)
    
\end{aligned}$

Of course, this doesn't really come as a surprise. However, we now know
*why* it is the case!

On to the last statement, we define $g(y) = y - 1$. The inverse function
is $g^{-1}(y) = y + 1$ so that $g^{-1}(g(y)) = y$. Given this, we can
finish the derivation:

$\begin{aligned}
      \rm{post(3)} & = & \rm{sub(\rm{post(2)},y,g^{-1}(y))} \\
                                   & = & \rm{sub((x = 3) \wedge (y = 2),y,y + 1)} \\
                                   & = & (x = 3) \wedge ((y+1) = 2) \\
                                   & = & (x = 3) \wedge (y = 1)
    
\end{aligned}$

This is yet another earth-breaking discovery (not!). Although it may
seem that we could have used intuition (sometimes called "eyeball
proof") to come to the same conclusion, the tools that we have used in
this section is very general and can be applied to much more difficult
problems.

We can now derive the general case as follows (`x`, `f`, and `n` are all placeholders):

```c
x=f(x); // line n
```

Assume that $f(x)$ is a function of $x$ that has an inverse function
$f^{-1}(x)$, then $\rm{post(n)} = \rm{sub(\rm{pre(n)},x,f^{-1}(x))}$.

## Revisiting the Forget operation

The forget operation is applicable for assignment statements whenever
the substitution operation cannot be performed. This means that the
following statement should use the "forget" operation:

``` {.numberLines .pseudocode language="pseudocode" numbers="left"}
```

This is because the RHS of the assignment does not refer to the LHS.
There is no inverse function to reverse the new value of $x$ back to its
previous value before the assignment statement.

As a result, you can use the substitution rule if and only if the
following conditions are all true for an assignment statement
$x \leftarrow e$ ($e$ is an expression):

-   The RHS ($e$) refers to the LHS. If so, let us define $f(x)=e$

-   There is an inverse function $f'(x)$ such that $f'(f(x))=x$

For *all* other assignment statements, the forget rule should be used.
This includes the following statement:

```c
x=x-x;
```

This is because even though the RHS refers to the LHS in this case, it
is not reversible. Once variable $x$ becomes zero after this statement,
there is no way to "recover" its previous value before the assignment
statement.

## Conditional statements

Let's consider algorithm
[\[algorithm:findmax\]](#algorithm:findmax){reference-type="ref"
reference="algorithm:findmax"} that makes $z$ the maximum of $x$ and
$y$.

``` {#algorithm:findmax .numberLines .pseudocode language="pseudocode" numbers="left" label="algorithm:findmax"}
if %$x>y$% then %\label{findmax:if}%
  %$z \leftarrow x$ \label{findmax:zgx}%
else
  %$z \leftarrow y$ \label{findmax:zgy}%
end if %\label{findmax:endif}%
```

Let us express the pre and post conditions of each statement. In this
case, let us not to assume any values in the variables. In other words,
$\rm{pre(\ref{findmax:if})} = \rm{true}$

The pre condition of line
[\[findmax:zgx\]](#findmax:zgx){reference-type="ref"
reference="findmax:zgx"} is not just $\rm{true}$. This is because the
only way that we get to line
[\[findmax:zgx\]](#findmax:zgx){reference-type="ref"
reference="findmax:zgx"} is that the condition $x > y$ must be true.
Consequently, $\rm{pre(\ref{findmax:zgx})} = (x > y)$. Using the same
argument, the only way we get to line
[\[findmax:zgy\]](#findmax:zgy){reference-type="ref"
reference="findmax:zgy"} is that $\neg(x > y)$, which is equivalent to
saying $x \le y$. As a result,
$\rm{pre(\ref{findmax:zgy})} = (x \le y)$.

The post condition of line
[\[findmax:zgx\]](#findmax:zgx){reference-type="ref"
reference="findmax:zgx"} is simply
$\rm{post(\ref{findmax:zgx})} = \rm{pre(\ref{findmax:zgx})} \wedge (z = x) = (x > y) \wedge (z = x)$.
Similarly, the post condition of line
[\[findmax:zgy\]](#findmax:zgy){reference-type="ref"
reference="findmax:zgy"} is
$\rm{post(\ref{findmax:zgy})} = \rm{pre(\ref{findmax:zgy})} \wedge (z = y) = (x \le y) \wedge (z = y)$.

Here comes the tricky part: what is $\rm{post(\ref{findmax:endif})}$? In
other words, after the entire conditional statement, what can we
conclude?

There are two ways to get to line
[\[findmax:endif\]](#findmax:endif){reference-type="ref"
reference="findmax:endif"}. We can get there from line
[\[findmax:zgx\]](#findmax:zgx){reference-type="ref"
reference="findmax:zgx"}, or from line
[\[findmax:zgy\]](#findmax:zgy){reference-type="ref"
reference="findmax:zgy"}. Consequently, the post condition of line
[\[findmax:endif\]](#findmax:endif){reference-type="ref"
reference="findmax:endif"} is the post condition of line
[\[findmax:zgx\]](#findmax:zgx){reference-type="ref"
reference="findmax:zgx"} or the post condition of line
[\[findmax:zgy\]](#findmax:zgy){reference-type="ref"
reference="findmax:zgy"}. In other words,

$\begin{aligned}
      \rm{post(\ref{findmax:endif})} & = & \rm{post(\ref{findmax:zgx})} \vee \rm{post(\ref{findmax:zgy})} \\
                                 & = & ((x > y) \wedge (z = x)) \vee ((x \le y) \wedge (z = y)) 
    
\end{aligned}$

Does this make sense?

Here is the general conditional statement:

``` {.numberLines .pseudocode language="pseudocode" numbers="left"}
if c then %\label{genif:if}%
    then-block %\label{genif:then}%
else
    else-block %\label{genif:else}%
end if %\label{genif:endif}%
```

-   $\rm{pre(\ref{genif:then})} = \rm{pre(\ref{genif:if})} \wedge c$

-   $\rm{pre(\ref{genif:else})} = \rm{pre(\ref{genif:if})} \wedge \neg c$

-   $\rm{post(\ref{genif:then})}$ has no general form, it depends on the
    actual code of "then-block". Note that even $c$ may not true after
    the code of "then-block".

-   $\rm{post(\ref{genif:else})}$ has no general form, it depends on the
    actual code of "else-block". Note that $c$ may actually be true
    after the code of "else-block".

-   $\rm{post(\ref{genif:endif})} = \rm{post(\ref{genif:then})} \vee \rm{post(\ref{genif:else})}$

## Loops

We are now on our final stretch!

Let us consider algorithm
[\[algorithm:while1\]](#algorithm:while1){reference-type="ref"
reference="algorithm:while1"}.

``` {#algorithm:while1 .numberLines .pseudocode language="pseudocode" numbers="left" label="algorithm:while1"}
while %$x<3$% do %\label{while1:while}%
  %$x \leftarrow x + 1$ \label{while1:step}%
end while %\label{while1:endwhile}%
```

Let's begin with $\rm{pre(\ref{while1:while})}$. After the
initialization of $x$, we know that
$\rm{pre(\ref{while1:while})} = (x = 0)$. However, the post condition of
line [\[while1:while\]](#while1:while){reference-type="ref"
reference="while1:while"} is not as simple. This is because there are
actually *two* ways to get to line
[\[while1:while\]](#while1:while){reference-type="ref"
reference="while1:while"}. In the first iteration, we enter from line
[\[while1:init\]](#while1:init){reference-type="ref"
reference="while1:init"}. However, in subsequent iterations, we enter
from line [\[while1:step\]](#while1:step){reference-type="ref"
reference="while1:step"}. On the other hand, no matter which way we come
from, we know that the condition $(x < 3)$ must be true if we enter the
loop.

As a result, all we say at this time is that
$\rm{post(\ref{while1:while})} =
    (x < 3) \wedge ((x = 0) \vee \rm{post(\ref{while1:step})})$. Note
that $\rm{pre(\ref{while1:step})} = \rm{post(\ref{while1:while})}$.

The statement on line
[\[while1:step\]](#while1:step){reference-type="ref"
reference="while1:step"} looks familiar. It involves a function of $x$.
In this case, the inverse function is $x-1$. We can then derive the
following:

$\begin{aligned}
      \rm{post(\ref{while1:step})} & = & \rm{sub(\rm{pre(\ref{while1:step})},x,x - 1)} \\
                               & = & ((x-1) < 3) \wedge (((x-1) = 0) \vee \rm{post(\ref{while1:step})}) \\
                               & = & (x \le 3) \wedge ((x = 1) \vee \rm{post(\ref{while1:step})})
    
\end{aligned}$

This is interesting because the same notation appears on the left and
the right hand side of the equation. The solution is to find a
definition that works in this equation. Choosing
$\rm{post(\ref{while1:step})} = (x \le 3)$ works. This is because
$(x = 1) \vee (x \le 3)$ simplifies to $x \le 3$ because it includes the
case of $x=1$. Furthermore, $(x \le 3) \wedge (x \le 3)$ can also
simplify to just $x \le 3$. In conclusion, we can define
$\rm{post(\ref{while1:step})} = (x \le 3)$.

How about $\rm{post(\ref{while1:endwhile})}$? In theory, we can get
there using two means. First, it is possible not to enter the loop at
all. Second, we can go through the loop at least once, then exit the
loop. Regardless of whether we get into the loop or not, one thing is
for sure: $x < 3$ must be false. As a result,

$\begin{aligned}
      \rm{post(\ref{while1:endwhile})} & = & \neg(x < 3) \wedge (\rm{pre(\ref{while1:while})} \vee \rm{post(\ref{while1:step})}) \\
                                   & = & (x \ge 3) \wedge ((x = 3) \vee (x \le 3)) \\
                                   & = & (x \ge 3) \wedge (x \le 3) \\
                                   & = & (x = 3)
    
\end{aligned}$

In other words, when we exit the loop, we know that $x = 3$.

In its general form, a prechecking loop is as follows:

``` {.numberLines .pseudocode language="pseudocode" numbers="left"}
while c do %\label{while:while}%
    block %\label{while:in}%
end while %\label{while:endwhile}%
```

-   $\rm{post(\ref{while:while})} = \rm{pre(\ref{while:in})} = c \wedge (\rm{pre(\ref{while:while})} \vee \rm{post(\ref{while:in})})$

-   $\rm{post(\ref{while:endwhile})} = \neg c \wedge (\rm{pre(\ref{while:while})} \vee \rm{post(\ref{while:in})})$

-   The trick is to find a good definition of
    $\rm{post(\ref{while:in})}$! $\rm{post(\ref{while:in})}$ is also
    called the "loop invariant".

The general form of a postchecking loop is as follows:

``` {.numberLines .pseudocode language="pseudocode" numbers="left"}
repeat %\label{repeat:repeat}%
    block %\label{repeat:step}%
until c %\label{repeat:until}
```

-   $\rm{pre(\ref{repeat:step})} = \rm{pre(\ref{repeat:repeat})} \vee \rm{post(\ref{repeat:step})}$

-   $\rm{post(\ref{repeat:until})} = c \wedge \rm{post(\ref{repeat:step})}$

-   Again, the trick is to find a good definition for
    $\rm{post(\ref{repeat:step})}$, it is also called the "loop
    invariant".

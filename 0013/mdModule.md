---
title: "Module 0013: Conditions and conditional statements"
---

# About this module

-   Prerequisites: [0012](../0012/mdModule.html)

-   Objectives: This module explores conditions and conditional
    statements in programming.

# Why?

Conditional statements are important because they permit a program to
follow different paths based on the outcome of conditions. In other
words, conditional statements give programs the ability to "choose".

# Conditions

A condition is essentially a question that can only have one of two
answers: "true" or "false". I choose to use "true" and "false" instead
of "yes" and "no" for a reason. Let us examine this question:

Is variable `x` greater than variable `y`?

Obviously, the answer is either "yes" or "no". However, let me change
the question just a little, as follows:

Is variable `x` not greater than variable `y`?

Although the proper answer is still either "yes" or "no", it depends
greatly on the (natural) language. In English, for example, if `x > y`,
then the proper answer to "Is variable `x` not greater than `y`?" is "yes". However, in some other languages, the proper
answer is "no". This is why "yes" and "no" are not really good answers.

As a result, it is better to pose questions as follows:

Is it true or false that $x > y$?

We can now flip the question as follows: Is it true or false that `x` is
not greater than `y`?

It is important to remember that in programming, `x > y` is not an assertion, it is a question. That is, `x > y` is not saying that
`x` is actually greater than `y`, but rather asking the question "is it
true that `x` is greater than `y`". This means that $` > y` in
programming should have been `x ?>? y`, just to make it
clear.

## Comparisons

The first and more primitive kind of conditions is the comparison
operators. This is a list of comparison operators that exist in all
programming languages:

-   `>`: greater than.
-   `<`: less than.
-   `>=`: greater than or equal to. 
-   `<=`: less than or equal to.
-   `!=`: not equal to. In Visual Basic, SQL and Pascal, it is represented by `<>` (less than or greater than).
-   `==`: equal to.

It is important to distinguish `=` from `==` in a C-derived language.
This topic is out of scope in this module. However, it suffices to say
that this is a source of many defects in programming.

These comparison operators take two values, one on each side of the
operators.

## Logical operators

Although comparison operators are useful, they cannot express all the
conditions that a program requires. However, we'll get back to this
topic later.

# Conditional statements

Let's try to express the logic to compute the maximum of two variables,
`x` and `y`, and put that maximum value in variable `z`. This kind of
logic cannot be expressed by sequential statements because whether `z`
should receive the value of `x` or the value of `y` *depends* on the
relationship of `x` and `y`.

I think we have enough suspense already. The proper code for this logic
is as follows:

```c
if (x > y) // line 1
  z = x;   // line 2
else       // line 3
  z = y;   // line 4
```

Line 1 expresses the question of whether `x` is
greater than `y`. Line
2 is the statement that executes if and
only if `x` is actually greater than `y` (`X > y` is true). Line
4 is the statement that executes if and
only if `x` is *not* actually greater than `y` (`x > y` is false). Line
3 is merely a separator marker to separate the
statement groups. Line

Also, note that the statements on line
2 and line
4 are "indented". This means that they are
shifted a little to the right-hand side. The purpose of indentation is
to indicate how a statement "embeds" another one. This will become more
important later.

A conditional statement is also graphically presented as follows:

![If-then-else template](ifthenelse_template.png) 

Note that this is not a
flow-chart, but rather a "trail-map". There is no special symbol to
remember! In this picture, the condition is a question of a post before
entering the fork. One path of the fork is chosen based on the answer to
the question (on the post). If the answer is "true", then the left path
is chosen. If the answer is "false", then the right path is chosen. The
bubble on the left hand side is labeled "then", it represents whatever
needs to be done if the answer is "true". Likewise, the bubble on the
right hand side is labeled "else", it represents whatever needs to be
done if the answer is "false".

![The pictorial template of a basic conditional (if-then-else)
statement.](ifthenelse_template.png){#figure:ifthenelse_template}

Given this template, we can substitute the proper condition and actions
for algorithm [\[algorithm:max2\]](#algorithm:max2){reference-type="ref"
reference="algorithm:max2"}. The resulting trail map is presented in
figure [2](#figure:max2){reference-type="ref" reference="figure:max2"}.

![The pictorial representation of algorithm
[\[algorithm:max2\]](#algorithm:max2){reference-type="ref"
reference="algorithm:max2"}.](ifthenelse_max2.png){#figure:max2}

# Logical operators

Although comparison operators are important and useful, they are not
sufficient to express all the different kinds of conditions needed in
programming. Let us think about the logic to figure out the maximum $z$
of three variables $w$, $x$ and $y$.

We know that we need to rely on a conditional statement. In fact, we can
guess the overall form of the statement (in listing
[\[algorithm:max3t\]](#algorithm:max3t){reference-type="ref"
reference="algorithm:max3t"}:

``` {#algorithm:max3t .numberLines .pseudocode language="pseudocode" numbers="left" escapechar="\\%" label="algorithm:max3t" caption="Template to find max of 3 variables"}
if %$c_1$% then
  %$z \leftarrow w$% %\label{max3:w}%
else if %$c_2$% then
  %$z \leftarrow x$% %\label{max3:x}%
else
  %$z \leftarrow y$% %\label{max3:y}%
end if
```

Line [\[max3:w\]](#max3:w){reference-type="ref" reference="max3:w"}
should execute if and only if $w$ is, indeed, the maximum. Similar logic
applies to lines [\[max3:x\]](#max3:x){reference-type="ref"
reference="max3:x"} and [\[max3:y\]](#max3:y){reference-type="ref"
reference="max3:y"}. Let us focus on line
[\[max3:w\]](#max3:w){reference-type="ref" reference="max3:w"} for now.

How can we confirm that $w$ is the maximum? If $w \ge x$ and $w \ge y$,
then by definition, $w$ is the maximum. But how do we express this as
$c_1$?

How about just "$w \ge x$ and $w \ge y$"?

Bingo! That's the answer! The word "and" *is* a logical operator! It is
called a "conjunction". A conjunction means the whole expression is true
if and only if both sides of the operator are true. Let us explore all
the logical operators.

## Conjunction

As stated, conjunction is an operator that has two sides. The entire
expression is true if and only if both sides are true. In English, a
conjunction is "and". The mathematical symbol of conjunction is $\wedge$
(like an inverted "V"). In C and other C-derived languages, the
conjunction operator is `&&`. In Pascal, SQL and Visual Basic, the
operator is simply spelled as `AND`.

The four possible combinations are as follows:

-   $({\rm true} \wedge {\rm true})$ is true

-   $({\rm false} \wedge {\rm true})$ is false

-   $({\rm true} \wedge {\rm false})$ is false

-   $({\rm false} \wedge {\rm false})$ is false

## Disjunction

Disjunction is the English word "or". This operator also requires two
sides. The entire disjunction expression is true if and only if at least
one side is true. The mathematical symbol of disjunction is $\vee$ (like
a "V"). In C and other C-drived languages, the disjunction operator is
`||`. In Pascal, SQL and Visual Basic, the operator is simply spelled as
`OR`.

The four possible combinations are as follows:

-   $({\rm true} \vee {\rm true})$ is true

-   $({\rm false} \vee {\rm true})$ is true

-   $({\rm true} \vee {\rm false})$ is true

-   $({\rm false} \vee {\rm false})$ is false

## Negation

Negation is the English word "not". This operator only has one side (on
the right hand side). A negation expression is true if and only if the
value of the right hand side is false. The mathematical symbol is $\neg$
(like a cliff). In C and other C-derived languages, the operator is `!`
(exclamation point). In Pascal, SQL and Visual Basic, the operator is
spelled out as `NOT`.

The two possible combinations are as follows:

-   $(\neg {\rm true})$ is false

-   $(\neg {\rm false})$ is true

# Back to the example

Getting back to the example to compute the maximum of three variables,
we can now utilize the conjunction operator as in listing
[\[algorithm:max3\]](#algorithm:max3){reference-type="ref"
reference="algorithm:max3"}.

``` {#algorithm:max3 .numberLines .pseudocode language="pseudocode" label="algorithm:max3" numbers="left" escapechar="\\%" caption="Find max of 3 variables"}
if %$(w \ge x) \wedge (w \ge y)$% then %\label{max3a:if}%
  %$z \leftarrow w$% %\label{max3a:w}%
else if %$(x \ge w) \wedge (x \ge y)$% then
  %$z \leftarrow x$% %\label{max3a:x}%
else
  %$z \leftarrow y$% %\label{max3a:y}%
end if %\label{max3a:endif}%
```

Now that the algorithm is finished, let us try to trace it. In our first
example, let us assume $w=2$, $x=2$ and $y=2$. Although this is a
trivial case, a trace of the algorithm illustrates a conditional
statement with multiple conditions.

  line \#                                                                         w   x   y   z   comments
  ------------------------------------------------------------------------------- --- --- --- --- ----------------------------------------------------
  pre                                                                             2   2   2   ?   we don't know the value of $z$
  [\[max3a:if\]](#max3a:if){reference-type="ref" reference="max3a:if"}            2   2   2   ?   $2 \ge 2$ is true, the conjunction is true as well
  [\[max3a:w\]](#max3a:w){reference-type="ref" reference="max3a:w"}               2   2   2   2   $z$ gets its value from $w$
  [\[max3a:endif\]](#max3a:endif){reference-type="ref" reference="max3a:endif"}   2   2   2   2   we only executes one case

This example illustrates one very important point. In a complex
conditional statement, even though multiple conditions may be true, only
the statement matching the first (in top-to-bottom order) true condition
executes.

Now, it is your turn to work out the next example. Assume $w=2$, $x=3$
and $y=3$. Create a trace table that shows exactly which lines get
executed.

## Else if?

In algorithm [\[algorithm:max3\]](#algorithm:max3){reference-type="ref"
reference="algorithm:max3"}, we use a construct that was not present in
algorithm [\[algorithm:max2\]](#algorithm:max2){reference-type="ref"
reference="algorithm:max2"}. What exactly is "else if"? It is best to
first take a look of the template of a conditional statement with an
"else if" in figure
[3](#figure:ifthenelseifelse_template){reference-type="ref"
reference="figure:ifthenelseifelse_template"}.

![The template of a if-then-else-if-else conditional
statement](ifthenelseifelse_template.png){#figure:ifthenelseifelse_template}

Note that "condition2" is evaluated if-and-only-if "condition1"
evaluates to false. If "condition1" is true, we simply executes the
"then" action, and then bypass everything else and exit the statement.
This also means that if we execute the action "else then" or "else
else", we know, for sure, that "condition1" is false.

Once we fill in the details of algorithm
[\[algorithm:max3\]](#algorithm:max3){reference-type="ref"
reference="algorithm:max3"}, the picture becomes the one in figure
[4](#figure:max3){reference-type="ref" reference="figure:max3"}.

![The pictorial representation of algorithm
[\[algorithm:max3\]](#algorithm:max3){reference-type="ref"
reference="algorithm:max3"}.](ifthenelseifelse_max3.png){#figure:max3}

# Language issues

## Markers

In pseudocode, we can use any marker keywords. However, in a real
programming language, many of these marker keywords are not present.
This is especially the case in a "concise" programming language, such as
C and its derived languages.

Let us consider the following pseudocode example:

``` {.numberLines .pseudocode language="pseudocode" numbers="left"}
if %$x \ne y$% then
  %$z \leftarrow x + y$%
else
  %$z \leftarrow x - y$%
end if
```

Don't mind the meaning of this code. Rather, focus on the translation
into C language:

    if (x != y)
      z = x + y;
    else
      z = x - y;

Note that the marker words "then" and "end if" are missing.

Now, let us consider a slightly more complex example:

``` {.numberLines .pseudocode language="pseudocode" numbers="left"}
if %$c > l$% then
  %$c \leftarrow c - l$%
  %$x \leftarrow x + 1$%
else
  %$y \leftarrow y + 1$%
end if
```

The corresponding C code is as follows:

    if (c > l)
    {
      c = c - l;
      x = x + 1;
    }
    else
      y = y + 1;

Curly braces (`{}`) are used to group the two lines for the "then" case.
This is because C can only specify one statement for the "then" case,
and another one for the "else" case. In order to perform multiple steps
in either case, the curly braces are used to group multiple steps into a
"compound statement".

As a personal preference, I always use curly braces, even if there is
only one statement. The following is the C code that I would have used:

    if (c > l)
    {
      c = c - l;
      x = x + 1;
    }
    else
    {
      y = y + 1;
    }

The advantage of this approach is that I can add lines to the "else"
case without worrying that I need to add curly braces.

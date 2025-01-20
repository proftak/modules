---
title: "Module 0296: Floating point numbers"
---

# About this module

-   Prerequisites:

-   Objectives: This modules looks into the IEEE floating point number
    representation, the parsing and conversion there of.

# The IEEE floating point number representation

For the discussion, this module focuses on the [double precision
floating-point
number](https://en.wikipedia.org/wiki/Double-precision_floating-point_format).
The full name is abbreviated to "double" henceforth.

A double has 64 bits (8 bytes). For the discussion of the format, let us
use $f_i$ to refer to bit $i$ of a double. The bit fields are arranged
as follows:

-   bit 63 (most significant): sign bit. Unlike a signed integer,
    however, the sign bit of a double is independent and only serves to
    indicate whether a value is negative (when this bit is a 1) or not
    (when this bit is a 0). We will call this bit $s=f_{63}$.

-   bit 52 to 62: these 11 bits are the 2's exponent. Let us define
    $e = \sum_{i=0}^{10} (f_{52+i}2^i)$. $e$ is not the actual exponent
    of 2, however, as it is an offset/biased amount. The offset amount/bias is 1023.
    As a result, the actual exponent of 2 is $e_2 = e-1023$. $e_2$
    denotes the exponent of 2. Note how this calculation is similar to the definition of the $v_u$ function in [module 0351](../0351/mdModule.html). 

-   bit 0 to 51: these 52 bits are the fractional base-2 mantissa. The
    actual mantissa is $c_2 = 1+\sum_{i=-52}^{-1}(f_{i+52}2^i)$. Note
    that the mantissa is a special case of a coefficient where the value
    of the coefficient is $\ge 1$ and less than the base. $c_2$ denotes
    the mantissa in base-2. Note how this calculation is related to, but not exactly the same as the computation of $v$ in [module 0282](../0282/mdModule.html#common-base-multiple-digit-numbers).

With these definitions, the value of a double $v_d(f)$ is:

$$v_d(f) = (s?-1:1) c_2 2^{e_2} = (-1)^{f_{63}}\cdot (1+\sum_{i=-52}^{-1}f_{52+i}2^{i}) \cdot 2^{(\sum_{i=0}^{10}f_{i+52}2^{i})-1023}$$

# Value range of a double

The value that can be represented by a double is quite wide. This is
mostly due to the use of an explicit exponent of 2 ($e_2$. The value of
$e_2$ itself is from -1023 (when $e = 0$) to 1024 (when $e=2047$). This
means the magnitude is from $2^{-1023}$ to $2^{1024}$. A double can
represent very *fine* to very large values on both sides of the number
line.

The precision of a double has 52 bits as it is determined by the number
of bits allocated to the mantissa. This means the smallest quantity a
double can discern is about $\frac{1}{2^{52}}$ of the magnitude
determined by the exponent. Any quantity smaller than this is "lost."

# Base-10 scientific notation

You may notice that a double is, essentially, an awkward base-2
scientific notation. Indeed, it is!

The problem is that people do not use base-2 scientific notation. People
use base-10 scientific notation. The syntax of a base-10 scientific
notation can be summarized in the following regular expression:

```perl
[+-]\=[1-9]\(\.\d*\)\=\(e[+-]\=\d\+\)\=
```

Of course, this needs .

-   `[+-]`: Characters enclosed in brackets are alternative
    accepted characters. In this case, the "+" and "-" symbols are
    accepted as alternatives.

-   `\=`: this escaped sequence means we can have 0 or 1 of
    whatever is specified earlier. In this context, the explicit sign of
    a number is optional. If it is missing, the default sign is
    non-negative $s=0$.

-   `[1-9]`: this escaped sequence means a character from the
    character of 1 to the character of 9.

-   `\( \)`: this pair of escaped sequence is a grouping.
    Whatever is enclosed is considered a single unit by the quantifier
    after it

-   `\.`: this escaped sequence means the decimal point. The
    decimal point is escaped because it means match any character when
    unescaped by the backslash character.

-   `\d`: this specifies base-10 digits following the decimal
    point.

-   `*`: this means any number of the thing before. Since this
    quantifier applies to the decimal digit, it means we can have any
    number of base-10 digits (including zero) after the decimal point.

-   `\=`: again, this means optional (0 or 1 occurrence). Since
    this quantifier is right after the grouping of the decimal point and
    any number of digits, it means the decimal point followed by any
    number of digits is optional.

-   `\( \)`: we have another grouping, this it is for the
    exponent (in base-10).

-   `e`: this means the exponent portion must start with the
    letter "e", in lower case.

-   `[+-]`: the exponent can have an explicit sign. If this sign
    is missing, the implicit sign is non-negative.

-   `\=`: this means the sign of the exponent is optional.

-   `\d\+`: we know the first escape sequence means any one
    base-10 digit. The second escape sequence means at least one of
    whatever is before it. Together, this means the base-10 number that
    specifies the exponent must have at least one base-10 digit.

-   `\=`: this applies to the exponent grouping, meaning the
    exponent in base-10 is optional. If the exponent is missing, the
    implicit exponent is 0.

Let us consider the example of

    -2.67e-6

:

-   the sign is negative, $s=1$.

-   the base-10 mantissa $c_{10} = 2.67$. Note that sign is not
    associated with the mantissa.

-   the base-10 exponent $e_{10} = -6$. Note that this sign *is*
    associated with the exponent.

The represented quantity is $(s?-1:1)c_{10}10^{e_{10}}$, which in this
case is $(-1)2.67\cdot 10^{-6}$.

## Exercise

Think about how to parse a base-10 scientific notation assuming it is as
described in this section. Because the syntax of a scientific notation
is a regular expression, it can be recognized by a finite-state
automata. More importantly, it can be parsed without using nested
recursive function calls!

The key is to break it up to all the possible sections and have a
dedicated parser for each section.

Assuming the notation is already stored in a string is helpful because
then it is easy to look at the same character multiple times for
optional sections. Reading and parsing directly from a stream can get
tricky because once a character is read from a stream, it has to be
"consumed" and understood right away, complicating the logic handling
optional parts.

# Conversion from base-10 scientific notation to double

The key is to preserve the represented value $v$ as much as possible so
that

$v = (s?-1:1)c_{10}\cdot 10^{e_{10}} = (s?-1:1)c_2\cdot 2^{e_2}$

The values of $s$, $c_{10}$ and $e_{10}$ can be parsed fairly easily.
The big question is how to come up with $c_2$ and $e_2$ to preserve the
represented $v$. The last part of the conversion is to extract just the
fractional part of $c_2$ to become $f_{51..0}$ and figure out
$e = e_2 + 1023$.

## Getting rid of the decimal point

The first step is to change the base-10 mantissa to a natural number
coefficient and adjust the base-10 exponent accordingly. In other words,
we express $2.67 = 267 \cdot 10^{-2}$, therefore decreasing $e_{10}$ by
2.

Note that $267$ is a coefficient, but it is not a mantissa anymore. This
is because a mantissa is a coefficient that is normalized. A coefficient
$m$ that is normalized should satisfy the condition of $1 \le |m| < 10$
for base-10 scientific notation.

In our example, $c_{10}=267$ and $e_{10} = -2$ after the adjustment.

This step ensures that we end up with just integers to perform further
calculations.

In this step, we need to apply a constraint that the ending $c_{10}$ can
be represented by a 64-bit integer. If the original $c_{10}$ contains
too many digit after the decimal point, then the algorithm rounds off at
a certain point. This rounding must be performed in base-10, which is
rather tedious. Truncating also works and it is much more efficient, but
in the long run, truncation has a bias to make values smaller.

We have 64 bits of precision in a 64-bit integer, that is
$16 \cdot (2^{60}) = 16 \cdot (2^{10})^{6}$. Because $2^{10}$ is
approximately 1000, we need to truncate or round $c_{10}$ to 19 decimal
digits.

In most cases, the base-10 coefficient does not come close to the
19-digit limit if the value is an observed or measured quantity (it is
then quantized by the instrument). However, the expression of irrational
numbers use up all 19 digits.

## Getting rid of the exponent of 10

Once we have a coefficient that is a natural number, the rest is to
change $c_{10}10^{e_{10}}$ to $c_2 2^{e_2}$. There are two distinct
processes to do this depending on the sign of $e_{10}$. For the rest of
this section, we start with $m \leftarrow c_{10}$. The algorithms
changes $m$, $e_2$ and $e_{10}$ so that the represented value (not
considering the sign) is

$v = c \cdot 2^{e_2} 10^{e_{10}}$

The idea is to gradually make $e_{10}=0$ by adjusting both $c$ and
$e_2$.

The key point of this phase is that we want to maximize precision and
ensure there is no "bias".

Consider an integer division $\frac{n}{d}$. Because it is an integer
division, the quotient is only the integer part of the actual result.
What is truncated is an error.

Let us consider the case where $n=dq+r$ where all terms are natural
numbers. As a result, $\frac{n}{d}=\frac{dq+r}{d} = q+\frac{r}{d}$. When
the fractional part is truncated, the ratio of the error is
$\frac{r}{n}$, and we want to keep this down. The key is, then, to
maximize the dividend (the number being divided) when a division.

The other problem of truncating is that the errors are all making the
represented result (as opposed to the true result) smaller. A sequence
of calculations involving these truncations will cumulatively make the
result err on the side of less than the true answer. This is a "bias" in
calculations.

The solution to handle a bias is to round instead of truncate. For
non-negative values, truncating is the same as the floor function.
Rounding, on the other hand, is adding 0.5 before truncating. This means
that we are using the following method to round:

$$\begin{aligned}
      \mathrm{round}(\frac{n}{d}) & = \lfloor \frac{n}{d} + 0.5 \rfloor \\
                                  & = \lfloor \frac{n+0.5d}{d} \rfloor
    
\end{aligned}$$

Fortunately, the divisor that we need to deal with is either 2 or 10,
and both are divisible by 2.

With the issues of precision and bias in mind, let us explore what to do
for the two cases to convert the number representation from base-10
scientific notation to base-2 double representation.

### Exponent of 10 is less than 0

We need to increase $e_{10}$ to 0 when decreasing $e_2$. The general
strategy is to divide $c$ by 10, then increase $e_{10}$ by 1, until
$e_{10}$ is 0. However, since we also want to maximize precision, we
also want to keep $c$ as large as possible in each step.

As a result, each step is divided into two steps. The first step is to
maximize $c$ by multiplying by 2 and decreasing $e_2$:

-   as long as $c$ is less than or equal to the largest possible
    coefficient value minus 5 then divided by 2

    -   $c \leftarrow 2c$

    -   $e_2 \leftarrow e_2 - 1$

The next step is rather easy:

-   $c \leftarrow \lfloor \frac{c+5}{10} \rfloor$

-   $e_{10} \leftarrow e_{10} + 1$

There is an overall loop on top to perform these two steps as long as
$e_{10} < 0$.

### Exponent of 10 is more than 0

We need to decrease $e_{10}$ to 0 when increasing $e_2$. In this case,
the general strategy is to multiply $m$ by 10 and decrement $e_{10}$
by 1. Keep doing until $e_{10} = 0$.

This process is complicated by the fact that $m$ can exceed the largest
value that can be represented by an integer. In that case, $m$ needs to
be divided by 2 and have $e_2$ increment.

In fact, we need to *first* make sure there is room to multiply by 10:

-   as long as $c$ is not less than the largest integer value divided by
    10

    -   $c \leftarrow \lfloor \frac{c+1}{2} \rfloor$

    -   $e_2 \leftarrow e_2 + 1$

Once we know there is enough room, then the next step is straight
forward:

-   $c \leftarrow 10c$

-   $e_{10} \leftarrow e_{10}-1$

All these steps need to in a loop that repeats as long as $e_{10} > 0$.

## Normalize the coefficient

At this point, because $e_{10}=0$, $c_2 = c$. However, this coefficient
is not normalized because it does not satisfy the requirement that
$1 \le c_2 < 2$. Normalizing is easy to do:

-   as long as $c_2 \ge 2$

    -   $c_2 \leftarrow \frac{c_2}{2}$

    -   $e_2 \leftarrow e_2 + 1$

However, this is *not* what we need to do! What we want to do is to make
sure $c_2$ is represented by exactly 53 (not 52!) bits. We use 53 bits
because the leading one will be implicit in the actual double
representation. Depending on $c_2$, one of the following two loops may
apply:

-   as long as $c_2 < 2^{52}$

    -   $c_2 \leftarrow 2c_2$

    -   $e_2 \leftarrow e_2 - 1$

```{=html}
<!-- -->
```
-   as long as $c_2 \ge 2^{53}$

    -   $c_2 \leftarrow \lfloor \frac{c_2 + 1}{2} \rfloor$

    -   $e_2 \leftarrow e_2 + 1$

When this is all done, we are guaranteed that $2^{52} \le c_2 < 2^{53}$.
Then it is a matter of adjusting $e_2$ and masking bit 52 to get the
fractional part of the coefficient:

-   $c_2 \leftarrow c_2 \mod 2^{52}$ to turn bit 52 to 0

-   $e_2 \leftarrow e_2 + 52$ to compensate for virtually shifting the
    binary point 52 times from the right of bit 0 to the left of bit 51

At this point, $c_2$ is a 52-bit number that represents the fractional
part of a normalized base-2 coefficient. $e_2$ is the correct scaling
exponent of 2.

## Computing the "e" component

Because $e_2 = e - 1023$, we know that $e = e_2 + 1023$. Convert the
resulting $e$ to the binary representation and we have bit 52 to bit 62
of the double representation.

## Putting the whole thing together

In terms of bits, at this point we have all of them:

-   bit 63: this is the sign bit, this bit is a 1 if the overall value
    is negative, 0 if the overall value is non-negative

-   bit 62 to 52: this is $e$

-   bit 51 to 0: this is $c_2$

Bitwise-or and bit shifting can be very useful to combine all the
elements together.


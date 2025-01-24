---
title: "Module 0282: Values, Numbers and Bases"
---

# About this module

-   Prerequisites:

-   Objectives: This modules explores something that we seem to be
    familiar with: numbers.

# What is a number?

A number is the name of a value. Just like a person has a name so that
others can refer to this person and distinguish this person from others,
values have names so that they can be referred to. What this also
implies is that the same value may have different names. This is not
surprising considering most people have formal names, friendly names and
names that only close friends use.

# Let's count!

Numbers are useful for counting. In the early days, people count by
fingers. Since we have ten fingers (digits), counting from 1 to 10 is
pretty simple. I am sure someone said "who would need to count to more
than ten!"

Of course, in time, we needed to count beyond ten. This was when people
realized that counting beyond 10 needed more than just fingers. The
representation of a value that is more than 10 requires some form of
abstraction.

Instead of using fingers, people used other objects for counting.
Pebbles, shells, sticks, and etc. Eventually, someone got tired of
bringing 200 pebbles to represent his/her worth. This was when
multi-digit numbers was invented.

To put simply, a multiple digit number uses different things to
represent quantities of different units. For example, a shell may mean a
singleton. A pebble may mean four shells, and a stick may mean five
pebbles. Multiple digit numbers makes it easier to represent larger
quantities.

# Common-base multiple digit numbers

Unlike the previous example or US currency, some people learn that using
a common *base* has many benefits. A "base" is essentially the quantity
that a single digit can count up to but excluding it. For example, in
our familiar base-10, it means that we can count to nine using a single
digit, but ten itself needs two digits.

To facilitate our discussion in a more abstract and convenient way, let
us look at a number as an array of digits. For example, consider the
decimal number 724. The "4" represents there are four units, we will
make that index 0. The "2" indicates we have two tens, make that index
1, and the "7" is index 2. Note that this notation works for decimal
places, as well. In 0.25, the digit "2" has an index of -1, while the
digit "5" has an index of -2.

Now let us take a look at a number and figure out its components. Let's
consider 16.375.

$$\begin{aligned}
    16.375 & = 10 + 6 + 0.3 + 0.07 + 0.005 \\
    & = 1\cdot 10^1 + 6 \cdot 10^0 + 3 \cdot 10^{-1} + 7 \cdot 10^{-2} + 5 \cdot 10^{-3}
  
\end{aligned}$$

This is hardly exciting. But then we see a pattern. In computer
programming, when we see a pattern, it means the concept can be
represented in a concise abstract way. First, we need a method to
designate each digit in a number. We use the notation $d_i$ to represent
the digit that indicates the quantity of 10 raised to the power of $i$.
In this example, $d_1=1, d_0=6, d_{-1}=3$, etc. With this notation, the
value $v$ represented by a base-10 number with digits $d_i$ is as
follows:

$$\begin{aligned}v & = d_0 \cdot 10^{0} + d_1 \cdot 10^{1} + d_{-1}\cdot 10^{-1} + ... \\ 
& = \sum\limits_{i=-\infty}^{\infty} d_i \cdot 10^{i}\end{aligned}$$

Obviously $i$ should be an integer. You can imagine an infinite amount
of leading zeroes to the left, and the infinite amount of trailing zeros
to the right.

It is always a good thing to challenge our believes. In this case, let
us challenge the only one constant used in the previous equation: 10. As
it turns out this is only because we implicitly use base-10 usually.
This means that if we choose to use an arbitrary base $b$ for a number
representing a value $v$, then the following is true:

$v = \sum\limits_{i=-\infty}^{\infty} d_i \cdot b^{i}$

# Converting v to a number in some base b

Now that we know how to figure the value $v$ represented by a number
using digits $d_i$ and a base of $b$, how do we figure out the
representation of a value $v$? In other words, how do we go backward?

The main restriction is that each digit can only be from 0 to $b-1$.
This is where the modulus (mod) operator comes in handy.

Let's say we are only dealing with non-negative values. Dealing with a
sign is easy, after all. Let us also think about just the digit with
index $i$.

What we know is that the quantities of $b^{i+1}$ is of no concern. $d_i$
is only responsible to indicate the quantity of $b^i$. Also, the
quantities of $b^{i-1}$ is also of concern here.

To get rid of anything less than the unit that we are interested, let us
define a new term $x=\left \lfloor \frac{v}{b^{i}} \right \rfloor$.

This step also converts the units to the number of $b^i$. To single out
the digit that we are concerned with, then we get $d_i=x \mod b$. The
use of $x$ is only to help clarify the concepts. To get to $d_i$
directly, we have the following

$d_i = \left \lfloor \frac{v}{b^{i}} \right \rfloor \mod b$

Note that this technique works even if $i<0$!

# Binary numbers

Easy: $b=2$!

The interesting part of binary numbers is that each digit can only be 0
or 1. This is because a single digit can only represent values from 0 to
$b-1$ where $b$ is the base. Binary numbers are important because we
have another system that only deals with two value: Boolean operations.
In module [0281](../0281), we already explored the implementation of
logic operations using transistors. At some point, we will also explore
how to use logic operations to perform arithmetic operations.

For now, let us check out binary numbers. Let us consider an example,
$01101_2$. The 2 in subscript signifies this is a binary numbers.

The least significant digit is a 1, meaning there is one of one. The
next digit (to the left) is a zero, meaning there is none of two. The
next one is a 1, there is one of four. The next one is also a one, there
is one of eight. The last (left most) one is a zero, there are zero
sixteens.

When you add up the values represented by individual digits, we have
$8+4+1=13$.

This is how we get the value of a base-2 number, usually representing
the value in base-10 as the final answer because that is a base that we
are familiar with.

# How are values represented in a computer?

Because a computer, after all, computes, it needs to store values before
and after computation. Almost all modern computers are digital binary
computers. This means that internally, all values are represented as
binary numbers. When we write a program that outputs values, what we see
as the output may be in base 10 (the default base of C++ streams), but
that is *after* a conversion process. Likewise, when we type numbers as
input to a program, we typically use base-10. The ASCII characters of a
base-10 number needs to go through a conversion process to be stored in
binary internally.

# Exercise: conversion

Write a general purpose program to do base conversion. For flexibility,
make the base a part of the input. This program should get the base of
the input, the base of the output, the actual input number, and prints
out the converted number.

# Gen-AI generated questions

### Easy:
1. **What is a number?**  
   <details>
   <summary>Answer</summary>
   A number is the name of a value.
   </details>

2. **In the base-10 system, what is the highest single-digit number?**  
   <details>
   <summary>Answer</summary>
   9.
   </details>

3. **What does the subscript "2" signify in the binary number $01101_2$?**  
   <details>
   <summary>Answer</summary>
   It signifies that the number is in base-2 (binary).
   </details>

4. **Why are binary numbers important in computing?**  
   <details>
   <summary>Answer</summary>
   Binary numbers are important because computers are digital binary systems, meaning they represent and process all values in binary.
   </details>

### Medium:
5. **Convert the binary number $1011_2$ to its decimal equivalent.**  
   <details>
   <summary>Answer</summary>
   $1011_2 = 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0 = 8 + 0 + 2 + 1 = 11$.
   </details>

6. **Explain the role of the modulus operator in converting a value $v$ to a number in some base $b$.**  
   <details>
   <summary>Answer</summary>
   The modulus operator helps in determining the digit at a specific position by isolating the value after dividing $v$ by the base raised to the power of the digit's position.
   </details>

7. **What does the equation $v = \sum\limits_{i=-\infty}^{\infty} d_i \cdot b^{i}$ represent?**  
   <details>
   <summary>Answer</summary>
   It represents the value $v$ as a sum of digits $d_i$ multiplied by the base $b$ raised to the power of their respective positions.
   </details>

### Hard:
8. **Convert the decimal number 45.75 to its binary equivalent.**  
   <details>
   <summary>Answer</summary>
   45 in binary is $101101_2$. For 0.75, the binary equivalent is 0.11. So, 45.75 in binary is $101101.11_2$.
   </details>

9. **Why is it important to use a common base, such as base-10, in numbering systems?**  
   <details>
   <summary>Answer</summary>
   Using a common base simplifies the representation and manipulation of numbers, allows for consistent arithmetic operations, and facilitates easier communication and understanding across different systems.
   </details>

10. **Describe the process of converting a base-10 number to a base-$b$ number.**  
   <details>
   <summary>Answer</summary>
   To convert a base-10 number to base-$b$, you repeatedly divide the number by $b$, keeping track of the remainders. These remainders form the digits of the new base-$b$ number when read in reverse order from the last remainder to the first.
   </details>

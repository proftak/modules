---
title: "Module 0352: Binary comparison"
author: Tak Auyeung
---

# About this module

-   Prerequisites: [0351](../0351)

-   Objectives: This module shows how the borrow, sign and overflow flags
    produced by a binary subtraction determine whether one value is less
    than another, for both the signed and the unsigned interpretation.

# Only "less-than" is needed

Because all other comparisons can be translated to less-than, possibly with the use of some logical operators, we are only concerned with less than in this module.

# Interpreted value

Given a bit pattern $x$ with $m$ bits, a C++ program can interpret the value as `int` (signed) or `unsigned`. The `unsigned` interpretation is simple because it is the default method of interpreting the value of a number (of any base):

<div style="border: 2px solid green" markdown="1">
$$v_u(x,m) = \sum_{i=0}^{m-1} x_i2^i$$
</div>

However, the `int` interpretation is a little more tricky. Congruent modulo $2^m$ helps to understand how a bit pattern can represent different values. However, it does not help determine exactly what value a bit pattern represents.

Two's complement is an operator that performs the same operation as arithmatic negation. However, it is not helpful to indicate the value represented by a bit pattern.

It is the decision that the range of values using the signed interpretation of a bit pattern is helpful. An $m$-bit pattern represents values from $-2^{m-1}$ to $2^{m-1}-1$. This range, combined with congruent modulo $2^m$, helps to determine that the signed (`int`) interpreted value of an $m$-bit pattern $x$ is as follows:

<div style="border: 2px solid green" markdown="1">
$v_s(x,m) = (\sum_{i=0}^{m-2} x_i 2^i) - x_{m-1}2^{m-1}$
</div>

As an example consider the 4-bit pattern $1011_2$. $v_u(1011_2,4)=1+2+0+8=11$, whereas $v_s(1011_2,4)=1+2-8=-5$.

# `unsigned` less-than

<div style="border: 2px solid green" markdown="1">
In a binary subtraction of two $m$-bit patterns $x-y$, $t_m=1$ if and only if $v_u(x,m) < v_u(y,m)$ assuming $t_0=0$.
</div>
  
## The proof (by induction)

This can be proven as follows using proof by induction.

The base case is when $m=1$. By definition $t_1 = b(x_0,y_0)+b(q_0,t_0)$. Since $t_0$ is part of the assumption, $b(q_0,t_0)$ has to be 0. This means $t_1 = b(x_0,y_0) = !x_0y_0$. This means $t_1 = 1$ if and only if $x_0=0 \wedge y_0=1$. This proves the base case.

The induction step assumes the theorem is true up to $m=k$. In other words, the assumption is $t_k=1$ if and only if $v_u(x,k) < v_u(y,k)$.

By the definition of $v_u$, $v_u(x,k+1) = x_{k}2^{k} + v_u(x,k)$, and likewise for $y$. In a $k+1$ bit subtraction of $v_u(x,k+1)-v_u(y,k+1)=x_{k}2^k + v_u(x,k) - y_k2^k - v_u(y,k)$.

If $x_k=y_k$, then $t_{k+1}=b(x_k,y_k)+b(x_k \oplus y_k,t_k)=b(0,t_k)=!0t_k=t_k$. This means that in this case, $t_{k+1}=1$ iff $t_k=1$, but it makes sense because the difference between $v_u(x,k+1)$ and $v_u(y,k+1)$ is $v_u(x,k)-v_u(y,k)$.

If $x_k=1 \wedge y_k=0$, then $v_u(x,k+1)>v_u(y,k+1)$, but $t_{k+1}=0$ in this case.

If $x_k=0 \wedge y_k=1$, then $t_{k+1}=b(0,1)+b(1,t_k)=1$, this also means that $v_u(x,k+1) < v_u(y,k+1) \Rightarrow t_{k+1}=1$.

Conversely, 

$$\begin{aligned}t_{k+1} =1 \Leftrightarrow (b(x_k,y_k)=1 \vee b(x_k \oplus y_k, t_k))=1\end{aligned}$$

$b(x_k,y_k)=!x_ky_k=1$ if and only if $(x_k=0 \wedge y_k=1)$. This means $v_u(x,k+1) < v_u(y,k+1)$. 

On the other hand, $b(x_k \oplus y_k, t_k)=1$ if and only if $(!(x_k \oplus y_k)t_k = 1) \Leftrightarrow ((x_k=y_k) \wedge t_k)=1$. 

In order for $!(x_k \oplus y_k)$ to be true, $x_k=y_k$. This means $(v_u(x,k+1)-v_u(y,k+1) = v_u(x,k)-v_u(y,k)) \wedge t_k=1$. Using the induction assumption of $t_k=1 \Leftrightarrow v_u(x,k) < v_u(y,k)$, we can conclude that $v_u(x,k+1) < v_u(y,k+1)$.

This concludes the induction step of the proof by induction.

# (Signed) `int` less-than

Unlike `unsigned` where the actual difference of $x-y$ cannot be its own value when $v_u(x,m)<v_u(y,m)$, signed `int` can represent the actual difference of $x-y$ because of the ability to represent negative values. This means $x < y \Leftrightarrow (x-y) < 0$. In a $m$-bit pattern interpreted signed, bit $m-1$ is the sign bit. This means $d=x-y$, $d_{m-1}=1 \Leftrightarrow v_s(x,m) < v_s(y,m)$.

This works fine as long as the actual difference is within the range of an $m$-bit pattern interpreted signed. Assume $m=4$, $x=1100_2$ and $y=0101_2$. In this case, $v_s(x,4)=4-8=-4$, $v_s(y,4)=1+4=5$. As a result, the *actual* value of $v_s(x,4)-v_s(y,4)$ is $-5-4=-9$. However, -9 is out of the range of signed values that can be represented. 

Instead, $-9 \equiv_{2^4} -9+16=7$. $7$ has a binary representation of $0111_2$.

This "out of range" problem can also happen in the opposite direction. Consider $x=0111\_{2}$, 
$y=1110\_{2}$. 
In this example, $v_s(x,4)=1+2+4=7$, whereas $v_s(y,4)=2+4-8=-2$. The actual difference of $v_s(x)-v_s(y)$ is $7-(-2)=9$. However, 9 is out of the range of a 4-bit pattern interpreted signed. However, we know that $9 \equiv_{2^4} 9-16 = -7$. $-7 = -8+1$, and as a result, $v_s(1001_2,4)=1-8=-7$, meaning that $-7$ is represented as $1001_2$.

How "over the range" can the difference be? If we use the $m=4$ example, then in one direction, the most negative value of a difference is $-8-7=-15 \equiv_{2^4} -15+16 = 1$, and in the other direction, $7-(-8)=15 \equiv_{2^4} 15-16 = -1$. 

Whenever the difference of the signed interpreted values $v_s(x,m)-v_s(y,m)$ is out of range, the sign of the difference, $d_{m-1}$, is opposite of what it should be. Furthermore, to determine whether the difference of the signed interpreted values is out of range, we only need to check whether the sign of the minuend is opposite to *both* the signs of the subtrahend and the difference.

<div style="border: 2px solid green" markdown="true">
This is why the overflow flag is defined as $O=x_{m-1}!y_{m-1}!d_{m-1}+!x_{m-1}y_{m-1}d_{m-1}$. The overflow flag is 1 iff $v_s(x,m)-v_s(y,m)$ is out of range.
</div>

The overflow flag is really indicating whether the actual sign of the difference should be opposite to the one computed using binary subtraction. <span style="border: 2px solid green" markdown="1">If we define $S=d_{m-1}$ (as a shorthand), then $S \oplus O$ is the correct sign of $v_s(x,m)-v_s(y,m)$</span>.

## The L-flag

<div style="border: 2px solid green" markdown="true">
If we define $L=S \oplus O$, then $L=1$ iff $v_s(x,m) < v_s(y,m)$.
</div>

# Exercise

Perform the following in binary subtraction using a bit-width of 3. Figure out all the rows, $x,y,q,t,d$, as well as the flags `B` (same as $t_3$) `S` (same as $d_2$), `O` (overflow), and `L` (less-than).

Note that the range of signed values given a width of 3 bits is from -4 to 3,and the unsigned values is from 0 to 7.

* 2-3
* -2-(-3)
* 3-2
* -2-3
* 2-(-3)

# AI-generated questions and answers

## Overall concepts

<details>
  <summary>1. How is an unsigned value interpreted from an m-bit binary pattern?</summary>
  <p>The unsigned interpretation of an m-bit binary pattern $x$ is calculated as:</p>
  <p>$v_u(x, m) = \sum_{i=0}^{m-1} x_i 2^i$</p>
</details>

<details>
  <summary>2. How is a signed value interpreted using two's complement in an m-bit binary pattern?</summary>
  <p>The signed interpretation of an m-bit binary pattern $x$ is given by:</p>
  <p>$v_s(x, m) = \left( \sum_{i=0}^{m-2} x_i 2^i \right) - x_{m-1} 2^{m-1}$, where the most significant bit ($x_{m-1}$) is treated as the sign bit.</p>
</details>

<details>
  <summary>3. What is the difference between signed and unsigned binary subtraction?</summary>
  <p>In unsigned subtraction, the result cannot represent a negative value, while in signed subtraction, the result can represent a negative value because of two's complement. Signed binary subtraction uses the sign bit (the most significant bit) to determine if the result is negative.</p>
</details>

<details>
  <summary>4. How can the less-than comparison for unsigned values be derived?</summary>
  <p>The less-than comparison for unsigned values can be derived by binary subtraction. Specifically, $t_m = 1$ if and only if $v_u(x, m) < v_u(y, m)$ for an m-bit binary subtraction.</p>
</details>

<details>
  <summary>5. What does the overflow flag indicate in signed binary subtraction?</summary>
  <p>The overflow flag indicates whether the difference between two signed numbers is out of range, meaning that the sign of the result is opposite to what it should be. The overflow flag is calculated as:</p>
  <p>$O = x_{m-1} \neg y_{m-1} \neg d_{m-1} + \neg x_{m-1} y_{m-1} d_{m-1}$</p>
</details>

<details>
  <summary>6. What is the relationship between the overflow flag and the correct sign of a signed subtraction result?</summary>
  <p>The correct sign of a signed subtraction result can be determined by the expression $S \oplus O$, where $S$ is the sign bit of the difference, and $O$ is the overflow flag. This expression provides the correct sign of the result.</p>
</details>

<details>
  <summary>7. What are the possible ranges for m-bit signed and unsigned values?</summary>
  <p>For an m-bit signed value, the range is from $-2^{m-1}$ to $2^{m-1} - 1$. For an m-bit unsigned value, the range is from 0 to $2^m - 1$.</p>
</details>

<details>
  <summary>8. How does the two's complement operation help in representing negative numbers?</summary>
  <p>The two's complement operation effectively negates a binary number by flipping all the bits and adding 1. It allows negative numbers to be represented in binary, and in the context of signed numbers, it ensures that arithmetic operations like addition and subtraction work as expected.</p>
</details>

<details>
  <summary>9. What is the significance of the most significant bit (MSB) in signed numbers?</summary>
  <p>The most significant bit (MSB) in signed numbers is used as the sign bit. If the MSB is 1, the number is negative; if it is 0, the number is positive. This bit plays a crucial role in determining the value of the number in two's complement representation.</p>
</details>

<details>
  <summary>10. How is the less-than condition represented in signed binary comparison?</summary>
  <p>The less-than condition in signed binary comparison is determined by the expression $L = S \oplus O$, where $L = 1$ if $v_s(x, m) < v_s(y, m)$. This condition checks whether the signed difference between two numbers is negative.</p>
</details>

## Practice questions with concrete values

Note that the AI-generated answers are quite wrong for these questions. The answers are corrected by hand.

<details>
  <summary>1. Subtract 011 from 010 in 3-bit unsigned binary. What are the borrow, sign, overflow, and L flags?</summary>
  <p>
    <strong>Subtraction:</strong> <code>010 - 011</code> = <code>111</code> (unsigned: 7, signed: -1) <br>
    <strong>Borrow Bit (B):</strong> 1 <br>
    <strong>Sign Bit (S):</strong> 1 <br>
    <strong>Overflow Bit (O):</strong> 0 <br>
    <strong>L Flag (Less-than):</strong> 1 <br>
    Result: Since <code>010 < 011</code>, the less-than condition holds in both signed and unsigned comparisons.
  </p>
</details>

<details>
  <summary>2. Subtract 110 from 001 in 3-bit signed binary. What are the borrow, sign, overflow, and L flags?</summary>
  <p>
    <strong>Subtraction:</strong> <code>001 - 110</code> = <code>011</code> (unsigned: 3, signed: 3) <br>
    <strong>Borrow Bit (B):</strong> 1 <br>
    <strong>Sign Bit (S):</strong> 0 <br>
    <strong>Overflow Bit (O):</strong> 0 <br>
    <strong>L Flag (Less-than):</strong> 0 <br>
    Result: <code>001</code> is not less than <code>110</code> in signed interpretation, but <code>001</code> is less than <code>110</code> in unsigned interpretation.
  </p>
</details>

<details>
  <summary>3. Subtract 011 from 011 in 3-bit unsigned binary. What are the borrow, sign, overflow, and L flags?</summary>
  <p>
    <strong>Subtraction:</strong> <code>011 - 011</code> = <code>000</code> (unsigned: 0) <br>
    <strong>Borrow Bit (B):</strong> 0 <br>
    <strong>Sign Bit (S):</strong> 0 <br>
    <strong>Overflow Bit (O):</strong> 0 <br>
    <strong>L Flag (Less-than):</strong> 0 <br>
    Result: The numbers are equal, so less-than is not true.
  </p>
</details>

<details>
  <summary>4. Subtract 001 from 100 in 3-bit signed binary. What are the borrow, sign, overflow, and L flags?</summary>
  <p>
    <strong>Subtraction:</strong> <code>100 - 001</code> = <code>011</code> (signed and unsigned: 3) <br>
    <strong>Borrow Bit (B):</strong> 0 <br>
    <strong>Sign Bit (S):</strong> 0 <br>
    <strong>Overflow Bit (O):</strong> 1 <br>
    <strong>L Flag (Less-than):</strong> 1 <br>
    Result: <code>100</code> is less than <code>001</code> in signed form, <code>100</code> is not less than <code>001</code> in unsigned form.
  </p>
</details>



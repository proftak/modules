---
title: "Module 0283: Binary Adition and Subtraction"
---

# Addition

## Base-10 Addition

### Example

     3 2 1 0 digit
       7 5 2 x
    +  2 4 9 y
    --------
       9 9 1 q
    +1 1 1 0 k
    --------
       0 0 1 s

Note that the rows $x$, $y$, and $s$ have the same number of digits because these rows correspond to fixed-width storage in a computer. Does $752+249=1$ make sense? The answer is yes once we take into consideration that $k_3=1$. $k_3=1$ means there is a carry to the digit that represents the quantity of 1000. The *actual* sum is, therefore, $1000+1=1001$.

### Pattern extraction and Generalization

$x$ and $y$ are the numbers being added. $s$ is the sum. $q$ is an intermediate row, we call it the "single-digit sum of $x$ and $y$". $k$ is also an intermediate row, it is the *k*arry to a specific digit. $s$ turns out to be the single-digit sum of $q$ and $k$.

The concept of a single-digit sum is important when we need to computer multi-digit addition. This is because instead of viewing $5+7$ as $12$, we say that the single-digit sum is $2$ with a carry of $1$ to the digit to the right. This is because $5+7$ results in a value that cannot be represented by a single digit in base 10. This causes a carry of 1 to the next digit (which specifies a power of 10 that is 10 times of current column). Once the $10$ is taken care of using a carry, the "leftover" amount is $2$.

We define two functions. Assuming $u$ and $v$ are single base-10 digits, then $r(u,v)$ computes the single-digit sum, while $c(u,v)$ computes the carry. Following the logic of the previous paragraph, we can conclude that $r(u,v)=(u+v) \mod 10$, and $c(u,v)=(u+v \ge 10)?1:0$. Or, in C:

```c
unsigned r(unsigned u, unsigned v)
{
  return (u+v)%10;
}

unsigned c(unsigned u, unsigned v)
{
  return (u+v>=10) ? 1 : 0;
}
```

Based on these functions, we can now relate the digits based on their rows and columns. $q_i = r(x_i,y_i)$, $s_i = r(q_i, k_i)$, and $k_{i+1}=c(x_i,y_i)+c(q_i,k_i)$. $k_0$ is assumed zero in a standalone addition. In a stacked addition (breaking the addition of long numbers into parts, from least significant to most significant chunks), $k_0$ has the value of the overall carry from a prior addition.

## Base-2 Addition

### r and c, redefined

Based on [a previous section](#pattern-extraction-and-generalization), the functions $r$ and $c$ can easily be redefined for any base $b$. This is because the concept of a single-digit sum and carry is not base-dependent. Given that $b$ is the base, $r(u,v)=(u+v) \mod b$, and $c(u,v)=(u+v \ge b)?1:0$.

To work in base-2, $b=2$, this means $r(u,v)=(u+v) \mod 2$ and $c(u,v)=(u+v \ge 2)?1:0$. The relationship between the digits remains the same.

Let us first example all the possibilities of $c(u,v)$ in base-2:

|u|v|c(u,v)|
|-|-|-|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

Does this look familiar? Indeed, in base-2, $c(u,v) = u \wedge v$, or in C, 

```c
unsigned c(unsigned u, unsigned v)
{
  return (u && v) ? 1 : 0;
}
```

This is convenient because we know that conjunction can be implemented by nand, and nand can, in return, be implemented in transistors. In other words, we can use transistors to implement $c(u,v)$ in base-2.

$r(u,v)$ is a little more tricky:

|u|v|r(u,v)|
|-|-|-|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

There is no single logical operator in C to perform this operation. However, in mathematics, exclusive-or is an exact match. In other words, $r(u,v) = u \oplus v$ in base-2. If insisted, it is also possible to use the "regular" C logical operators to implement $r(u,v)$:

```c
unsigned r(unsigned u, unsigned v)
{
  return ((u && !v) || (!u && v)) ? 1 : 0;
}
```

This is because $u \oplus v = (u \wedge \neg v) \vee (\neg u \wedge v)$. Try to prove this using a truth table as an exercise.

Despite being a little more complex, $r(u,v)$ can also be expressed using logical negation, conjunction, and disjunction. Since all three logical operators can be implemented using nand, and nand can be implemented using transistors, $r(u,v)$ can be implemented using transistors.

The last bit of trouble is how $k_{i+1}=c(x_i,y_i)+c(q_i,k_i)$ is computed using a sum. Can we use disjunction instead of addition here? Let's take a look at the operators in a table:

|$u$|$v$|$u \vee v$|$u + v$|
|-|-|-|-|
|0|0|0|0|
|0|1|1|1|
|1|0|1|1|
|1|1|1|2|

The only row that makes a difference is when $u=v=1$. *In general*, disjunction and addition are not the same!

However, in this case, we need to ask whether $c(x_i,y_i)$ and $c(q_i,k_i)$ can both be ones. The short answer is "no". If anyone is interested in proving this, here is a clue: $q_i$ is not an independent bit because $q_i = r(x_i,y_i) = x_i \oplus y_i$. As a result, $c(x_i,y_i)=1$ implies $x_i=1$ and $y_i=1$, but then $q_i=0$, ensuring $c(q_i,k_i)=0$. Likewise, $c(q_i,k_i)=1$ implies $q_i=1$, then of $x_i \ne y_i$, ensuring $c(x_i,y_i)=0$. This is the rather informal proof.

As a result, disjunction can be used instead of addition, $k_{i+1}=c(x_i,y_i) \vee c(q_i,k_i)=(x_i \wedge y_i) \vee (q_i \wedge k_i)$.

This concludes that binary addition can be implemented using transistors!

# Subtraction

## Base-10 Subtraction

### Example

     3 2 1 0 digit
       5 0 1 x
    -  5 0 4 y
    --------
       0 0 7 q
    -1 1 1 0 t
    --------
       9 9 7 d

Note that the rows $x$, $y$, and $d$ have the same number of digits because these rows correspond to fixed-width storage in a computer. Does $501-504=997$ make sense? The answer is yes once we take into consideration that $t_3=1$. $t_3=1$ means there is a borrow from the digit that represents the quantity of 1000. The *actual* difference is, therefore, $997-1000=-3$.

### r and b for base-10

$x$ is the minuend, and $y$ is the subtrahend.  $d$ is the difference. $q$ is an intermediate row, we call it the "single-digit difference of $x$ and $y$". $t$ is also an intermediate row, it is the *t*ake-away from a specific digit. $d$ turns out to be the single-digit difference of $q$ and $t$.

The concept of a single-digit difference is important when we need to compute multi-digit subtraction. This is because instead of viewing $5-7$ as $-2$, we say that the single-digit difference is $8$ with a borrow of $1$ from the digit to the right. This is because $5-7$ results in a value that cannot be represented by a single non-negative digit in base 10. This causes a borrow of 1 from the next digit (which specifies a power of 10 that is 10 times of current column). Once the $10$ is borrowed, the "difference" amount is $10+5-7=8$.

We define two functions. Assuming $u$ and $v$ are single base-10 digits, then $r(u,v)$ computes the single-digit difference, while $b(u,v)$ computes the borrow. Following the logic of the previous paragraph, we can conclude that $r(u,v)=(10+u-v) \mod 10$, and $b(u,v)=(u<v)?1:0$. Or, in C:

```c
unsigned r(unsigned u, unsigned v)
{
  return ((10+u)-v)%10;
}

unsigned b(unsigned u, unsigned v)
{
  return (u<v) ? 1 : 0;
}
```

Based on these functions, we can now relate the digits based on their rows and columns. $q_i = r(x_i,y_i)$, $d_i = r(q_i, t_i)$, and $t_{i+1}=b(x_i,y_i)+b(q_i,t_i)$. $t_0$ is assumed zero in a standalone subtraction. In a stacked subtraction (breaking the subtraction of long numbers into parts, from least significant to most significant chunks), $t_0$ has the value of the overall borrow from a prior addition.

Why are we using $r(u,v)$ both for the single-digit sum and single-digit difference? Read on!


## Base-2 Subtraction

### r and b, redefined 

Based on [a previous section](#r-and-b-for-base-10), the functions $r$ and $b$ can easily be redefined for any base $b$. This is because the concept of a single-digit difference and borrow is not base-dependent. Given that $e$ is the base, $r(u,v)=((e+u)-v) \mod e$, and $b(u,v)=(u<v)?1:0$.

To work in base-2, $e=2$, this means $r(u,v)=((2+u)-v) \mod 2$ and $b(u,v)=(u<v)?1:0$. The relationship between the digits remain the same.

Let us first example all the possibilities of $b(u,v)$ in base-2:

|u|v|b(u,v)|
|-|-|-|
|0|0|0|
|0|1|1|
|1|0|0|
|1|1|0|

Unlike $c(u,v)$ in base-2, this table does not look very familiar. However, we can still manage to use a boolean expression to perform the operation. In base-2, $b(u,v) = (\neg u) \wedge v$, or in C, 

```c
unsigned b(unsigned u, unsigned v)
{
  return (!u && v) ? 1 : 0;
}
```

This is convenient because we know that conjunction can be implemented by nand, and nand can, in return, be implemented in transistors. In other words, we can use transistors to implement $b(u,v)$ in base-2.

$r(u,v)$ is a little more tricky but familiar:

|u|v|r(u,v)|
|-|-|-|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

Hey, that is the same as $r(u,v)$ for binary addition! In a boring fashion, $r(u,v) = u \oplus v$ in base-2 subtraction (the same as addition). If insisted, it is also possible to use the "regular" C logical operators to implement $r(u,v)$:

```c
unsigned r(unsigned u, unsigned v)
{
  return ((u && !v) || (!u && v)) ? 1 : 0;
}
```

This is because $u \oplus v = (u \wedge \neg v) \vee (\neg u \wedge v)$. Try to prove this using a truth table as an exercise.

Despite being a little more complex, $r(u,v)$ can also be expressed using logical negation, conjunction, and disjunction. Since all three logical operators can be implemented using nand, and nand can be implemented using transistors, $r(u,v)$ can be implemented using transistors.

The last bit of trouble is how $t_{i+1}=b(x_i,y_i)+b(q_i,t_i)$ is computed using a sum. Can we use disjunction instead of addition here? Using a similar argument as in [an earlier section](#r-and-c-redefined), we need to ask whether $b(x_i,y_i)$ and $b(q_i,t_i)$ can both be ones. The short answer is "no". $q_i$ is not an independent bit because $q_i = r(x_i,y_i) = x_i \oplus y_i$. As a result, when $x_i=0$ and $y_i=1$ so that $b(x_i,y_i)=1$, $q_i=1$ and guarantees $b(q_i,t_i)=0$. Likewise, $b(q_i,t_i)=1$ implies $q_0=0$, then of $x_i=y_i$, ensuring $b(x_i,y_i)=0$. This is the rather informal proof.

As a result, disjunction can be used instead of addition, $t_{i+1}=b(x_i,y_i) \vee b(q_i,t_i)=(\neg x_i \wedge y_i) \vee (\neg q_i \wedge t_i)$.

This concludes that binary subtraction can also be implemented using transistors!

# Optimized adder and subtractor

In order to save enough time for other topics, this module does not discuss the optimization and actual circuit design of adders and subtractors. The equations in this module naturally lead to carry-ripple and borrow-ripple adders and subtractors. While these circuits are simple and they work, they are also inefficient. The more efficient ones utilize carry lookahead and borrow lookahead, respectively. The boolean algebra and actual circuit structure are complex and out of the scope of this module.

# AI-generated (but fixed by a human!) exercises


<h2>Binary Addition Questions</h2>
    
<details>
<summary>Question 1: Add 1011 and 0110.</summary>
        <pre>
     3 2 1 0 digit
       1 0 1 1 x
    +  0 1 1 0 y
    ----------
       1 1 0 1 q
    +1 1 1 0 0 k
    ----------
       0 0 0 1 s
        </pre>
</details>

<details>
        <summary>Question 2: Add 1101 and 1010.</summary>
        <pre>
     3 2 1 0 digit
       1 1 0 1 x
    +  1 0 1 0 y
    ----------
       0 1 1 1 q
    +1 0 0 0 0 k
    ----------
       0 1 1 1 s
        </pre>
</details>

<details>
        <summary>Question 3: Add 1111 and 0001.</summary>
        <pre>
     3 2 1 0 digit
       1 1 1 1 x
    +  0 0 0 1 y
    ----------
       1 1 1 0 q
    +1 1 1 1 0 k
    ----------
       0 0 0 0 s
        </pre>
</details>

<details>
        <summary>Question 4: Add 1001 and 0111.</summary>
        <pre>
     3 2 1 0 digit
       1 0 0 1 x
    +  0 1 1 1 y
    ----------
       1 1 1 0 q
    +1 1 1 1 0 k
    ----------
       0 0 0 0 s
        </pre>
</details>

<details>
        <summary>Question 5: Add 0011 and 1100.</summary>
        <pre>
     3 2 1 0 digit
       0 0 1 1 x
    +  1 1 0 0 y
    ----------
       1 1 1 1 q
    +0 0 0 0 0 k
    ----------
       1 1 1 1 s
        </pre>
</details>

<h2>Binary Subtraction Questions</h2>
    
<details>
        <summary>Question 1: Subtract 0110 from 1011.</summary>
        <pre>
     3 2 1 0 digit
       1 0 1 1 x
    -  0 1 1 0 y
    ----------
       1 1 0 1 q
    -0 1 0 0 0 t
    ----------
       0 1 0 1 d
        </pre>
</details>

<details>
        <summary>Question 2: Subtract 1010 from 1101.</summary>
        <pre>
     3 2 1 0 digit
       1 1 0 1 x
    -  1 0 1 0 y
    ----------
       0 1 1 1 q
    -0 0 1 0 0 t
    ----------
       0 0 1 1 d
        </pre>
</details>

<details>
        <summary>Question 3: Subtract 0001 from 1111.</summary>
        <pre>
     3 2 1 0 digit
       1 1 1 1 x
    -  0 0 0 1 y
    --------
       1 1 1 0 q
    -0 0 0 0 0 t
    ----------
       1 1 1 0 d
        </pre>
</details>

<details>
        <summary>Question 4: Subtract 0111 from 1001.</summary>
        <pre>
     3 2 1 0 digit
       1 0 0 1 x
    -  0 1 1 1 y
    ----------
       1 1 1 0 q
    -0 1 1 0 0 t
    ----------
       0 0 1 0 d
        </pre>
</details>

<details>
        <summary>Question 5: Subtract 1100 from 0011.</summary>
        <pre>
     3 2 1 0 digit
       0 0 1 1 x
    -  1 1 0 0 y
    ----------
       1 1 1 1 q
    -1 1 0 0 0 t
    ----------
       0 1 1 1 d
        </pre>
</details>




---
title: "Module 0374: Structures and arrays in TTPASM"
author: Tak Auyeung
---

# Arrays

Most compilers allocate space for arrays in a straightforward way.  Let us consider the following declaration where `TYPEX` is the name of a type, and `BUFLEN` is a natural number.

```c
TYPEX buffer[BUFLEN];
```

The total number number of bytes used by variable `buffer` is `sizeof(TYPEX)*BUFLEN`. 

In terms of address (for byte-addressable architectures), `&buffer[i]` has an address of `&buffer + sizeof(TYPEX) * i`.

General indexing is difficult in TTPASM because of the lack of a multiplication instruction. However, indexing into an array of byte-size elements is easy. The following is an example:

```ttpasm
// assume the address of an array is in register c
// assume the index is in register b
// assume an element is one byte wide
add b,c // b is now the address of the element at the index
```

If the size of an element is a power of 2, the code is still relatively simple:

```ttpasm
// assume the address of an array is in register c
// assume the index is in register b
// assume an element is four-byte wide
add b,b // b=2*b
add b,b // b=2*b, now it is 4x the initial value
add b,c // b is now the address of the element at the index
```

However, there is no easy way to generate a template of code given the size of each array element. 

Pointer arithmetic is generally as difficult. However, pointer increment can be done easily. Consider the following C code:

```c
TYPEX *ptr;
//...
ptr+1 // compute the value of this expression
```

The equivalent TTPASM code is as follows:

```ttpasm
// assume the value of ptr is in register a
// assume the size of TYPEX is defined by the label TYPEX_size
ldi b,TYPEX_size
add a,b // a is now the value of ptr+1
```

Many algorithms related to arrays only need to access elements sequentially. As a result, the code can be converted to use pointer-arithmetic operations. For example, the following C code computes the sum of an array:

```c
for (i = 0, sum = 0; i < N; ++i)
{
  sum += a[I];
}
```

It can be changed to use pointer arithmetic as follows:

```c
for (i=0, sum=0, ptr=a; i<N; ++i)
{
  sum += *(ptr++);
}
```

Note that the expression `sum += *(ptr++)` is the same as first performing `sum += *ptr`, then performing `ptr++`.

# Structures

A general structure definition in C/C++ looks like this:

```c
struct STRUCTX
{
  TYPE1 m1; // first member
  TYPE2 m2;
  // ...
  TYPEn mn; // last member
};
```

The word width of an architecture is the width of the data bus in the processor core. Currently, most production processors have a word-width of 64 bits, also known as 8 bytes. If a member is of a scalar type, then a compiler attempts to make sure the entire member can be accessed in a single memory operation based on the word width of the processor.

Unless otherwise instructed using a `pragma`, a compiler sequentially allocates storage for members within a structure. The offset of a member from the beginning of a structure is based on the offset of a previous member, but aligned to ensure each elemental type can be accessed in a single memory cycle.

The offset to the first member is easy to compute because it is at the beginning of the entire structure, the offset is 0 (zero).

The offsets to the rest of the members are a little more complicated. Let `offset(m)` refer to the byte offset to member `m` in a structure, and `alignment(m)` refers to the alignment width of member `m` (to be defined). Then $\mathtt{offset}(\mathtt{m}_{i+1}) = \lceil \frac{\mathtt{offset}(m_i)+\mathtt{sizeof}(\mathtt{m}\_i)}{\mathtt{alignment}(\mathtt{m}\_{i+1})} \rceil \times \mathtt{alignment}(\mathtt{m}\_{i+1})$. The symbol $\lceil x \rceil$ is the ceiling function that returns the smallest integer greater than or equal to $x$.

The alignment width of a structure is the maximum of the alignments of its members but is also restricted by the architecture's word width (in bytes). In this example, `alignment(STRUCTX) = min(wordWidth, max(alignment(m1), alignment(m2),... alignment(mn)))`. For a 64-bit architecture, `wordWidth` is 8.

The alignment width of an elemental (scalar) type `t` is defined as `alignment(t)=min(wordWidth, sizeof(t))`.

## TTP implementation

### Structure definition

TTP has a `wordWidth` of 1. As a result, there are no alignment issues!

The concept of a `struct` is merely a matter of tracking the offset from the beginning of a structure to the members, please an overall size of a `struct`.

For example, let us consider the following C `struct` definition:

```c
struct X
{
  uint8_t x;
  struct X *ptr;
  uint8_t y;
};
```

This translates to the following labels in TTPASM:

```ttpasm
X_x: 0
X_ptr: X_x 1 +
X_y: X_ptr 1 +
X_size: X_y 1 +
```

### Accessing members of a structure

Because labels are used to track the offset of a member from the beginning of a structure, given the address of a structure is in a register already, the address of a member is the sum of the address of the structure and the offset to the member. Using the example from the previous section, the following is an example:

```ttpasm
// assume the address of a struct X is in register b
ldi a,X_y
add b,a // b is now the address of member y of the struct X
```


---
title: "Module 0304: Calling and returning from functions"
---

# About this module

-   Prerequisites:

-   Objectives: This module explains how to call and return from a
    subroutine using C and TTP assembly language.

# C program example

Let us example the code from the following program:

```c
void f()
{
}

int main()
{
  f();
  f();
  return 0;
}
```

Calling a subroutine does not seem difficult at all, as we can use an
unconditional branch to continue execution from the caller to the called
subroutine (callee). The difficult part is how we return to the caller
at the end of the execution of a callee.

At the end of executing a called subroutine, the processor needs to
figure out where to continue execution in the caller. Given the
instruction set of TTP, this means that location must be remembered
somewhere in memory.

# A quick digression to stack

A "stack" is a data structure that enforces the LIFO (last-in-first-out)
order. In the abstract sense, a stack starts empty, let's denote that with `[]`. If there are items in the stack, **the leftmost item is the "top" of the stack**.

A "push" operation adds an item to a stack from the "top" of the stack. The following illustrates what happens to a stack after 3 pushes:

1.  push "24": `[24]`
2.  push "61": `[61 24]`
3.  push "11": `[11 61 24]`

A "pop" operation retrieves and removes an item from the top of the stack. The following illustrates what happens to the same stack used in the previous example after 2 pops:

1.  pop: `[61 24]` retrieves 11
2.  pop: `[24]` retrieves 61

Push and pop operations can interleave. The following continues with the stack used in previous examples:

1.  push "5": `[5 24]`
2.  push "78": `[78 5 24]`
3.  pop: `[5 24]` retrieves 78
4.  push "100": `[100 5 24]`
5.  pop: `[5 24]` retrieves 100

As a data structure in C++, a stack is often implemented as a
linked list of nodes. However, this is rather inefficient from the
perspective of low-level code that is written in assembly.

In assembly language, a stack is implemented by a stack pointer (SP) and
an area reserved for the stack. The stack pointer always points to "the
last item stored on stack". This automatically makes the location
pointed by the SP also the first item to retrieve due to the LIFO nature
of a stack.

Let us assume the stack area is reserved as a static global array called
"stack" as follows:

```c
#define STACKSIZE 32
uint8_t stack[STACKSIZE];
uint8_t *SP;
```

Note how the stack point is declared as a pointer to an element in the
stack array.

In TTP, we assume the stack is from location 255 to the last byte
available after the program takes up space. We also have to designate a
register to be the stack pointer. For the rest of this discussion, we
assume register D is the stack pointer.

To facilitate efficient use of instructions, a stack grows "down"
instead of up. This means that as more items are added to the stack, the
stack pointer moves down instead of up.

Because the SP is assumed to be pointing to the last item stored (also
called pushed), the code to store something new is as follows:

```c
  SP--; // reserve space on stack
  *(SP)=x; // now store x to the newly reserved location
```

The above block of code can also be condensed into one expression: `*(--SP)=x`.

To retrieve (also referred to as pop) the most recently stored item that
is still on the stack and "remove" it at the same time, we can use the
following code:

```c
  x=*(SP); // retrieve the most recently stored item
  SP++;    // deallocate (free) the space
```

The above block of code can also be condensed into one expression: `x=*(SP++)`.

Due to this method, the proper way to initialize the SP is to make
point to the byte that is just one past the end of the stack area:

```c
  SP=stack+STACKSIZE;
```

This seems to cause a problem because it points past the allocated
area. However, remember that when we push items on a stack, we *first*
decrement the SP, and as a result, the initial value of SP is never used
for dereferencing.

For a demonstration of how a stack works in C, take a look at [this sample program](https://onlinegdb.com/qXosH1QmN).

# Calling and returning

The code to a subroutine has two distinct parts. The first part is to
set for the return address. This allows the called subroutine to
continue execution in the caller. The second part is to continue
execution in the subroutine.

Let us examine the TTP assembly code to do this:

```
  dec  d      // allocate a byte on stack
  ldi  c,L1   // this is the return address
  st   (d),c  // now store it on stack
  jmpi f      // continue execution in subroutine
L1: // continuation point of caller
```

Assuming the return address is stored on the stack, at the end of a
subroutine, the following code can be used to return to the caller:

```
  ld   a,(d)  // retrieve return address
  inc  d      // deallocate location from stack
  jmp  a      // continue execution in caller
```

# Will this work with recursion?

Yes, it will.

The important part is that there is a return address stored on the stack for
each *invocation* of a subroutine.

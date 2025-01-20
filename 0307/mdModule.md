---
title: "Module 0307: Parameters and local variables"
---

# About this module

-   Prerequisites: [0304](../0304/mdModule.html), [0306](../0306/mdModule.md)

-   Objectives: This module discusses how parameters are passed in
    assembly language code in a way that is compatible with C code.
    Local variables are also discussed in this module

# Parameters on the stack

Because there can many parameters, and recursion is to be supported
(along with multi-threading), it is necessary to store parameters in a
per-invocation basis, much like the return address.

Let us examine the following caller code in C:

```c
  subtract(3,5);
```

The equivalent code in TTP assembly is as follows:

```ttpasm
  ldi a,5
  dec d
  st  (d),a // push 5
  ldi a,3
  dec d
  st  (d),a // push 3
  ldi a,retAddr
  dec d
  st  (d),a // push return address
  jmpi subtract
retAddr:
  inc  d
  inc  d    // deallocate parameters
  // now the stack should be balanced
```

Note how the parameters are pushed in reverse order. This means the
second parameter is pushed first, and then the first parameter. Another
implication is that the first parameter has a lower address on the stack
than the second parameter.

Furthermore, also note how the return address is pushed last.

Here is the subroutine code in C:

```c
int subtract(int x, int y)
{
  return x-y;
}
```

The matching code in TTP assembly is as follows:

```ttpasm
subtract: // entry point of subroutine
  cpr c,d  // c is a copy of the stack pointer
  ldi a,1  // offset to find parameter x
  add c,a  // now c is the address to x
  ld  a,(c) // now a is parameter x
  inc c     // now c is the address to y
  ld  b,(c) // now b is parameter y
  sub a,b   // perform the subtraction
  // a already has the right result to return
  ld  b,(d) // d is never changed, still pointer
            // to the return address
  inc d     // callee only deallocates the retAddr
            // NOT the parameters!
  jmp b     // now return and continue in caller
```

It is important to leave register D alone and not to use it directly to
compute the address of parameters.

# Local variables

Local variables of a subroutine are allocated on a per invocation basis
on the stack, much like parameters. However, parameters are allocated
and initialized by the caller, while local variables are allocated by
the called subroutine.

As a result, local variables have addresses that are below that of the
return address. The method to access local variables is the same as
accessing parameters.

The main difficulty of accessing local variables is tracking the stack
pointer as items are pushed and popped. In many real architectures,
there is a "frame point" that points to a fixed place relative to items
used by a subroutine. TTP is too primitive to dedicate yet another
register for this purpose.

# A more mechanical way to access frame items

The parameters, return address, and local variables collectively make up the *call frame* of an invocation of a function. From the perspective of the callee, the parameters, and return address are already pushed on the stack at the entry point. However, a callee is responsible to allocate stack space for its own local variables.

It is best to use symbolic names to reference the *offset* to items in a frame from where the stack pointer points to after the entire frame is allocated. For example, consider the following C code:

```c
void someFunc(uint8_t x, uint8_t y, uint8_t z)
{
   uint8_t a,b,c;
}
```

The corresponding frame looks like the following:

|offset from where SP points to|what|
|-|-|
|6|z|
|5|y|
|4|x|
|3|return address|
|2|c|
|1|b|
|0|a|

From the callee's perspective, some label definitions can be used to first compute the offsets to local variables:

```ttpasm
someFunc_a: 0 // offset from where D points to to find local var a
someFunc_b: someFunc_a 1 + // offset to local var b
someFunc_c: someFunc_b 1 + // offset to local var c
someFunc_localVarSize: someFunc_c 1 + // # bytes used for local vars
```

Parameters are also in a call frame, they can also have their offsets defined by labels. In this example, the following label definitions can apply:

```ttpasm
someFunc_x: someFunc_localVarSize 1 + // add 1 to skip over the return address
someFunc_y: someFunc_x 1 +
someFunc_z: someFunc_y 1 +
```

The "shell" of this callee consists of the code to allocate and deallocate the local variables, as well as the code to return to the caller:

```ttpasm
someFunc: // entry point of the callee
  ldi a,someFunc_localVarSize
  sub d,a // allocate stack space for local variables

  // ... code for the body of someFunc

  ldi b,someFunc_localVarSize
  add d,b // deallocate stack space for local variables
  // the SP should now point to the return address
  ld  b,(d)
  inc d    // pop the return address to reg b
  jmp b    // continue execution at the caller
```

In the body of `someFunc`, accessing a local variable or parameter can be very mechanical. Generally, the following *pattern* works:

```ttpasm
  ldi a,someFunc_b // a=&b-SP load offset to a register
  add a,d // a=&b the address of the item on the frame
```

Whether the address of a frame item should be dereferenced depends on the context.

It is important to keep track of the stack pointer using this approach! If the stack pointer is not pointing to the local variable of the lower address, then adjustments need to be made. This usually happens in a function call. Let's reexamine `someFunc` with a call to `someOtherFunc`:

```c
void someFunc(uint8_t x, uint8_t y, uint8_t z)
{
   uint8_t a,b,c;
   // ...
   someOtherFunc(&a,z);
   // ...
}
```

The code to call `someOtherFunc` is then as follows

```ttpasm
  ldi a,someFunc_z // a=&z-SP
  add a,d // a=&z
  ld  a,(a) // a=z
  dec d
// at this point, the SP points to one byte below local var a!
  st  (d),a // push z
  ldi a,someFunc_a 1 + // reg a=&(local var a)-SP, add 1 to compensate for the second argument already pushed
  add a,d // reg a=&(local var a)
  dec d
  st  (d),a // push &(local var a)
  ldi a,. 6 +
  dec d
  st  (d),a // push return address
  inc d // deallocate the first argument
  inc d // deallocate the second argument
  
```

# Exercise 1

Implement the following program in TTP assembly language:

```c
#include <stdint,h>

void swap(uint8_t *pX, uint8_t *pY);

int main()
{
  uint8_t x,y;
  x=2;
  y=5;
  swap(&x,&y);
  return 0;
}

void swap(uint8_t *pX, uint8_t *pY)
{
  uint8_t t;
  t=*pX;
  *pX=*pY;
  *pY=t;
}
```

In addition to the use of local variables, this program also involves
passing the address of a variable (instead of the value of a variable)
on the stack.

# Exercise 2

Implement the following program in TTP assembly language:

```c
#include <stdint.h>

uint8_t power(uint8_t n);

int main()
{
  uint8_t x;

  x = power(3);
  return 0;
}
 
uint8_t power(uint8_t n)
{
  if (!n)
  {
    return 1;
  }
  else
  {
    return 2*power(n-1);
  }
}
```

The function in this program is recursive!

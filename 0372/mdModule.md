---
title: "Module 0372: Caller-callee agreement"
author: Tak Auyeung
---

# Stack operation specification

Register D is the designated stack point. Although register D is a general-purpose register, it is designated by *convention* in order to specify the agreement between the caller and the callee.

To push the value already loaded into register X (X can be A, B, C, or D), the following C code is used

```c
// to push the value of register X
*(--D) = X;
```

The stack pointer is decremented first to reserve the space, then the content of register X is copied to the location pointed to by register D. The equivalent TTPASM code is as follows:

```ttpasm
dec d
st  (d),x // x is a placeholder for register a,b,c, or d
```

In both the C and TTPASM implementations, it is clear that the stack pointer always points to the last item pushed on the stack. This is because the stack pointer is adjusted *prior* to overwriting the location that the stack pointer points to. In terms of notation, we can use `D+0` to refer to the address that is currently pointed to by the stack pointer.

To pop the "top" of the stack to register X, the operation is reversed. The following is the C code implementation:

```c
X = *(D++);
```

The content pointed to by the stack pointer is copied to the register specified by X, then the stack pointer is incremented to deallocate the location where the content was retrieved from. The following is the TTPASM code:

```ttpasm
ld  x,(d) // x is a placeholder for register a,b,c, or d
inc d
```

Because of this stack convention, items that are pushed earlier occupy memory locations that are higher in addresses. For example, the result of push 2 can be describe by the following:

|location|content|
|-|-|
|D+0|2|

In this notation `D+0` refers to the location that is pointed to by the stack pointer, `D`. The `+0` indicates an offset of zero. 

However, if push 13 follows immediately, then stack becomes as follows:

|Offset from where D points to|content|
|-|-|
|+1|2|
|+0|13|

In this table, the notation `D+1` references the address that is one byte higher than where the stack pointer (D) points to. Not that at this point, the stack pointer is decremented in the process to push 13. As a result, the location that stores the value of 2 has not changed, but its offset from where the stack pointer points to is changed because the stack pointer has changed.


# Mutual agreement

The mutual agreement between the caller and callee starts with how the stack operates, as describe in the previous section. 

## Caller side

* if there are arguments:
  * arguments are pushed in reverse order, the last argument is pushed first
  * on TTP, arguments are pushed contiguously (no gaps between them)
  * this implies the last argument has the highest address in a call frame
* the return address (the address of the instruction right after the jump to the callee) is pushed after all the arguments (if any)  
  * as a result, the return address has an address that is lower than all the arguments
  * the stack pointer points to the return address at the entry point of the function being called
* jump to the entry point of the callee

Assuming $\mathtt{arg}\_1$ to $\mathtt{arg}\_n$ refer to $n$ arguments (each with a width of one byte) in a call to function `func`, the frame is partially constructed by the caller at this point:

|Offset from where D points to|content|
|-|-|
|+n|$\mathtt{arg}\_n$|
|+n-1|$\mathtt{arg}\_{n-1}$|
|+1|$\mathtt{arg}\_{1}$|
|+0|return address to the instruction immediately after `jmpi func|

* the callee should return to the instruction right after the jump instruction with the return address popped

In our example, the stack should like the following at the instruction right after the `jmpi func` instruction:

|Offset from where D points to|content|
|-|-|
|+n-1|$\mathtt{arg}\_n$|
|+n-2|$\mathtt{arg}\_{n-1}$|
|...|...|
|+0|$\mathtt{arg}\_{1}$|

* if the callee returns a scalar value:
  * the return value is assumed to be in register A
* the value of registers A, B and C are not assumed preserved
* if there are arguments:
  * the caller has the responsibility to clean up the stack space used by arguments, if any

## Callee side

* at the entry point of the callee:
  * the stack pointer points to the return address
  * if there are parameters:
    * the first parameter starts at the address immediately after (higher than) that of the return address
    * the last parameter has the highest address
    * parameters are contiguous in TTP
* in the callee's code:
  * additional stack space may be utilized for local variables
  * the callee is responsible for moving the stack pointer lower to reserve space for the local variables

In the ongoing example, if we assume function `func` has local variables $\mathtt{var}\_1$ to $\mathtt{var}\_m$, each being one byte wide, then the stack looks like the following after the entry code of the callee moves the stack pointer and allocate space for the local variables:

|Offset from where D points to|content|
|-|-|
|+n+m+1|$\mathtt{arg}\_n$|
|+n+m|$\mathtt{arg}\_{n-1}$|
|...|...|
|+1+m|$\mathtt{arg}\_{1}$|
|+m|return address|
|+m-1|$\mathtt{var}\_m$|
|...|...|
|+0|$\mathtt{var}\_1$|

Note that local variables are not restricted to one byte wide. Arrays and structures, for example, will be more than one byte wide.

To continue with additional agreements between the caller and callee:

* there is no need to preserve the values of registers A, B, or C
* at the exit point of the callee:
  * if the callee has a scalar return value:
    * use register A to store the return value
  * the callee is responsible for popping the return address
  * the callee uses the popped return address to return to the caller
 
## The call frame

### When there are local variables

The call frame (or just "frame") refers to a region of stack space that provides the data context for a function to operate. This includes the space of local variables, the return address, and the parameters. The call frame is not allocated by the callee. Instead, it is partially constructed by the caller, including the parameters and the return address, and partially constructed by the callee, allocating the additional space for local variables.

After a frame is fully allocated, the stack pointer points to the base of the frame. Let us consider the following example:

```c
void f(uint8_t x, uint8_t y)
{
  uint8_t a,b;

}
```

In this case, the caller is responsible to push the arguments and the return address. As a result, the following table describes the *partially constructed* frame at the entry point of function `f`:

|Offset from where D points to|item description|
|-|-|
|+2|parameter `y`|
|+1|parameter `x`|
|+0|return address|

Note how local variables `a` and `b` are not yet allocated. Function `f` is responsible for allocating the space needed for the local variables. Because `a` and `b` are both 1-byte wide, they need a total of 2 bytes in the frame. These two bytes are allocated at the entry point of function `f`. As a result, the local variables are located lower (in terms of addresses) than the return address. The following table show the content of the frame after local variables are explicitly allocated by the entry code of function `f`:

|Offset from where D points to|item description|
|-|-|
|+4|parameter `y`|
|+3|parameter `x`|
|+2|return address|
|+1|local variable `b`|
|+0|local variable `a`|

The offset to items of the frame may be defined as follows:

```ttpasm
f_a: 0       // offset to local variable a, it is at the base of the entire frame
f_b: f_a 1 + // offset to local variable b
f_lvs: f_b 1 + // the total number of bytes needed for local variables
f_x: f_lvs 1 + // the offset to parameter x, the 1 + is needed to skip the return address
f_y: f_x 1 + // the offset to parameter y
```

The function `f` is responsible to allocate and deallocate the space needed for local variables. As a result, the shell of function `f` is as follows:

```ttpasm
f:
  ldi b,f_lvs
  sub d,b // allocate space for local variables, this completes the construction of the call frame
  // ... actual code of function f
  ldi b,f_lvs
  add d,b // deallocate space for local variables

  ld b,(d) // retrieve the return address
  inc d    // deallocate the return address from the stack
  jmp b    // continue execution at the caller
```

Because the callee is responsible for popping the return address, the stack looks like the following immediately after it returns to the caller:

|Offset from where D points to|item description|
|-|-|
|+1|parameter `y`|
|+0|parameter `x`|

Note how the return address is not on the stack. However, parameters `x` and `y` (known as arguments from the caller's perspective) are still on the stack. As per the agreement, the caller needs to deallocate these two bytes on the stack. For this example, the following TTPASM code that immediately follows `jmpi f` in the call deallocates the arguments:

```ttpasm
  inc d // deallocate parameter x
  inc d // deallocate parameter y
```
### When there are no local variables

A function may have zero (no) local variables. In this scenario, the approach to use `func_lvs` as a label to represent the number of bytes used by local variables is still correct, but the label should be defined as zero. It is important to note that the return address is pointed to by the stack pointer in this case.

For example, let us consider the following C function definition:

```c
void g(uint8_t *x, uint_8 y)
{
  *x = y
}
```

There are no local variables, the call frame consists only of the return address and the two parameters as follows at the entry point of function `g`:

|Offset from where D points to|description of item|
|-|-|
|+2|parameter `y`|
|+1|parameter `x`|
|+0|return address|

The corresponding TTPASM code can be as follows:

```ttpasm
g:
  g_lvs: 0
  g_x: g_lvs 1 + // add 1 to skip over the return address
  g_y: g_x 1 +
  ldi b,g_lvs
  sub d,b // "allocate" local variables even though there is none

  ldi b,g_y
  add b,d
  ld  b,(b)

  ldi a,g_x
  add a,d
  ld  a,(a)

  st  (a),b

  ldi b,g_lvs
  add d,b // "deallocate" local variables even though there is none

  ld  b,(d)
  inc d
  jmp b
```

## Non-caller-callee specific

* Any content below where the stack pointer points can be modified asynchronously.

In an architecture that supports interrupts, hardware interrupt can occur between the execution of any two instructions. A hardware interrupt invokes (calls) the corresponding ISR (interrupt service routine). This causes the return address to the interrupted code to be pushed on the stack. Imagine the stack as follows prior to an interrupt:

|Offset from where D points to|item description|
|-|-|
|+0|last item pushed|
|-1|remnant X|

When an interrupt occurs, the processor pushes the return address from the ISR to the interrupted code on the stack, resulting in the following state:

|Offset from where D points to|item description|
|-|-|
|+1|last item pushed|
|+0|~~remnant X~~ return address to interrupted code|

Note how "last item pushed" is not affected because it was where the stack pointer points to when the interrupt occurs. However, "remnant X" is now overwritten by the return address to resume the execution of code prior to the interrupt.

After the ISR returns, the stack can be described as follows:

|Offset from where D points to|item description|
|-|-|
|+0|last item pushed|
|-1|~~remnant X~~ return address to interrupted code|

From the perspective of the code that was interrupted, the state of the stack has not changed, as long as there is no reference to locations below where the stack pointer points! Note that during the execution of an ISR, more locations on the stack may be overwritten. In other words, the overwriting of the location immediately below where the stack pointer points to at the moment of the interrupt is the *minimum* part of the stack to be used during the execution of an ISR.

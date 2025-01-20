---
title: "Module 0432: A general description of TTP"
---

# The general architecture

This is a general description of TTP (Tak's Toy Processor). There are four instruction-addressable registers: A, B, C, and D. The registers are general-purpose registers, meaning that there are no restrictions on which instruction applies to which register. The program counter, PC, is not directly addressable in instructions.

The processor is an 8-bit processor, which means that all the registers are 8-bit wide. The RAM component has an 8-bit address port, which allows the addressing of 256 locations. Each location in RAM is 8-bit wide.

The ALU (arithmetic and logic unit) is capable of addition, subtraction, bit-wise and, bit-wise or, right-shift, and bit-wise not. There are 5 flags in the flags register:

* C: the C flag is the overall borrow after a subtraction and the overall carry after an addition
* Z: the Z flag is true if and only if the result of the previous operation is zero.
* S: the S flag is the sign flag (bit 7) of the result of the previous operation.
* O: the O flag is the overflow flag of the previous add or subtract operation. Overflow means the result of the operation is out of the range of a signed 8-bit integer.
* L: the L flag is the exclusive-or of the S and and O flags. The L flag is true if and only if the minuend is less than the subtrahend in the previous subtraction.

The flags are not directly accessible, but they are utilized in the conditional branch instructions jci, jzi, jsi, joi and jli. These conditional branches branch based on the value of a flag. For example, jci branches if and only if the C flag is true. If a conditional branch instruction does not branch, the processor continues with the instruction that immediately follow the conditional branch instruction.

# The instructions

The following table uses `x` and `y` as placeholders of one of the four registers, A, B, C, and D. `i` is a placeholder for an immediate value, which must be specified by a postfix expression that is resolvable at assemble time. The register transfer language description explains what happens when the instruction executes. Note that the program counter (`PC`) points to where the next opcode is in memory, but it is not directly addressable in an instruction. Any dereference is getting the content of a memory location. Also, note that `PC` is already pointing to one byte past the opcode being executed due to an autoincrement in the fetch phase of instruction execution.

|mnemonics|RTL|flags affected|number of bytes of the instruction|common name|
|-|-|-|-|-|
|cpr x,y|x=y||1|compare x to y|
|ld x,(y)|x = *y||1|load x from where y points to |
|st (y),x|*y = x||1|store x to where y points to|
|ldi x,i|x=i||2|load immediate to x|
|jmpi i|PC=i||2|jump to location i|
|jci i|PC=c?i:PC+1||2|jump to location i if and only if c is true|
|jzi i|PC=z?i:PC+1||2|jump to location i if and only if z is true|
|jsi i|PC=s?i:PC+1||2|jump to location i if and only if s is true|
|joi i|PC=o?i:PC+1||2|jump to location i if and only if o is true|
|jli i|PC=l?i:PC+1||2|jump to location i if and only if l is true|
|jmp x|PC=x||1|jump to where x points to|
|cmp x,y|x-y|C,Z,S,O,L|1|compare x to y|
|add x,y|x=x+y|C,Z,S,O,L|1|add y to x|
|sub x,y|x=x-y|C,Z,S,O,L|1|subtract y from x|
|and x,y|x=x&y|Z,S,L|1|store the bitwise-and of x and y to x|
|or x,y|x=x\|y|Z,S,L|1|store the bitwise-or of x and y to x|
|not x|x=~x|Z,S,L|1|store the bitwise-not of x to x|
|rsh x,y|x=x << y|Z,S,L|1|store x right-shifted by y to x|
|inc x|x=x+1||1|increment x|
|dec x|x=x-1||1|increment y|

These are the *only* instructions supported by TTP. The syntax requires the parentheses where they are indicated in the mnemonic column. The conditional branches continue execution immediately following instruction if and only if the respective flag they check for is false.

# Label definition

A label definition starts at the beginning of a line, optionally with white spaces before. The syntax of a label definition is a C identifier followed immediately by, without any white space character, a colon. No instruction can be specified on the same line as a label definition.

Using this simple syntax, a label is defined to the current location in the assembly process. 

However, a label can be followed by a postfix expression. If a label definition has a postfix expression, then the value of the label is defined to the value of the postfix expression. The value of the postfix expression must be resolved at assemble time.

A postfix expression may include literal numerical constants, references to labels, or the single dot `.`. The single dot, `.`, represents the start address of the line containing the expression that references the dot.

In other words, 

```
L1:
```

is a simplification of 

```
L1: .
```

# Conventions related to C

## The stack

There is no dedicated stack pointer. Register D is the designated stack pointer. The region of space available for the stack ranges from the location immediately following the assembled program, all the way to the end of the RAM memory space. Because the RAM component has an 8-bit address port, the end address of the stack is location 255.

By convention, the stack pointer points to the last byte pushed or allocated. As a result, the stack pointer should be initialized to location 256 when it is empty. This is because the stack grows to lower memory addresses. To push a value already stored in a register, the following code can be used:

```
dec d
st (d),a // assume the value to be pushed is in register A
```

Likewise, to pop the most recently stored value (the top) of the stack into a register, the following code can be used:

```
ld a,(d)
inc d
```

Like most architectures, assume interrupts can occur asynchronously. As a result, any memory location below where the stack pointer points to can be overwritten asynchronously. This means that unless the content of where the stack pointer points to is no longer needed, do not increment the stack pointer. 

## Caller's responsibility

In a function call, the caller is responsible to push arguments (if any) in a reversed order. This means the last argument is pushed first. This results in the first argument occupying a memory location that is the lowest (least) compared to the other arguments.

After push the arguments, the caller is also responsible to push the return address. 

After the return address is pushed, the caller uses `jmpi` or other means to continue execution at the entry point of a function. The entry point of a function is a label definition marking the first instruction of the function.

The return address in a function call is the address of the instruction immediately following the `jmpi` instruction that continues execution at the called function.

Af the return address, the caller is responsible for deallocating the arguments pushed earlier. Note that the return address is popped by the callee, not the caller.

The caller cannot expect a callee to preserve the values in registers A, B, or C. If the callee returns a scalar-type value, the scalar-type return value is assume to be in register A when the callee returns.

## Callee's responsibility

A callee can assume the return address and arguments (if any) are pushed by the caller in the order specified in the previous section. At tne end of a callee, a callee is responsible to pop the return address, then use it to continue execution at the caller.

The allocation and deallocation of stack locations for local variables is the responsibility of the callee.

---
title: "Module 0434: TTP programming"
---

# _{{ page.title }}_

# General description of the architecture and instructions

A, B, C and D are the four instruction-addressable general-purpose registers. The program counter, PC, is not directly addressable in instructions.

The processor is an 8-bit processor, all registers are 8-bit wide. The RAM component has an 8-bit address port, which allows the addressing of 256 locations. Each location in RAM is 8-bit wide.

There are 5 flags in the flags register:

* the C flag is the overall borrow after a subtraction and the overall carry after an addition
* the Z flag is true if and only if the result of the previous operation is zero.
* the S flag is the sign flag (bit 7) of the result of the previous operation.
* the O flag is the overflow flag of the previous add or subtract operation. Overflow means the result of the operation is out of the range of a signed 8-bit integer.
* the L flag is the exclusive-or of the S and and O flags. The L flag is true if and only if the minuend is less than the subtrahend in the previous subtraction.

The flags are utilized in the conditional branch instructions jci, jzi, jsi, joi and jli. These conditional branches branch based on the value of a flag. 

# The instructions

The following instruction table uses `x` and `y` as placeholders of one of the four registers, A, B, C, and D. `i` is a placeholder for an immediate value, which must be specified by a postfix expression that is resolvable at assemble time. The register transfer language (RTL) description explains what happens when the instruction executes. Note that `PC` already points to one byte past the opcode being executed due to an autoincrement in the fetch phase of instruction execution.

Note that if a placeholder if x or y, the actual operand must be one of the four registers. For example, `add a,b` is valid, but `add a,1` is invalid.

Addressing modes in the instruction mnemonics:

* `x` or `y`: register, the operand is the value of the specified register, `x` and `y` are placeholders of registers `a`, `b`, `c`, or `d`.
* `i`: immediate, the operand is the value of a postfix expression, the value must be resolved at assemble time
* `(y)`: indirect, the operand is the content in RAM at the location pointed to by the register that `y` specifies.

|mnemonics|RTL|flags affected|number of bytes of the instruction|description|
|-|-|-|-|-|
|cpr x,y|x=y||1|copy y to x|
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
|cmp x,y|x-y|C,Z,S,O,L|1|compare x to y, x and y cannot be the same register|
|add x,y|x=x+y|C,Z,S,O,L|1|add y to x|
|sub x,y|x=x-y|C,Z,S,O,L|1|subtract y from x|
|and x,y|x=x&y|Z,S,L|1|store the bitwise-and of x and y to x|
|or x,y|x=x\|y|Z,S,L|1|store the bitwise-or of x and y to x|
|not x|x=~x|Z,S,L|1|store the bitwise-not of x to x|
|rsh x,y|x=x << y|Z,S,L|1|store x right-shifted by y to x|
|inc x|x=x+1||1|increment x|
|dec x|x=x-1||1|increment y|
|nop|||1|no operation|
|halt|||1|halt, execution cannot proceed any further|

The use of parentheses is neither optional nor arbitrary. A pair of parentheses should be used only in an "indirect" operand. The value of an indirect operand is the location or RAM pointed to by a specific register. Only the second operand of `ld` and the first operand of `st` are indirect operands.

Because the only way to dereference is to use the `ld` and `st` instructions, and each one uses one 8-bit register for the indirect address mode, a pointer in TTP is 8-bit wide.

# the `byte` directive

The `byte` directive is used to reserve and initialize the value of a byte:

```
byte 65 // allocate a byte and initialize it to 65
```

The general syntax of the `byte` directive is the word `byte`, followed by exactly one postfix expression that computes the value of the byte being allocated.

Comments start with two slashes. The following is an example of commenting an instruction:

```
ldi a,5 // a=5
```

# Label definition

A label definition starts at the beginning of a line, optionally with white spaces before. The syntax of a label definition is a valid C identifier (the first character can be an underscore or letters, subsequent characters can include digits) followed immediately by, without any white space character, a colon. No instruction can be specified on the same line as a label definition.

Using this syntax, a label is defined to the current location in the assembly process. A label can be followed by a postfix expression, then the expression defines the value of the label. The value of the postfix expression must be resolved at assemble time.

A postfix expression may include literal numerical constants, references to labels, or the single dot `.`. The single dot, `.`, represents the start address of the line containing the expression that references the dot.

In other words, 

```
L1:
```

is a simplification of 

```
L1: .
```

The dot notation can be used to specify the address of an instruction that is at a fixed offset, the following code calls `func`:

```ttpasm
ldi a,. 6 +
dec d
st (d),a
jmpi func
```


---
title: "Module 0384: TTP conditional jumps"
author: Tak Auyeung
---

# Description

A conditional jump is a jump instruction, like `jmpi` and the corresponding register-based instruction `jmp`, but only conditionally. A conditional jump instruction uses a specific bit in the `flags` register to determine whether to jump or not.

In general, if `x` represents one of the flags in the `flags` register, then the following TTPASM code

```text
   jxi dest
```

has the same effect as the following equivalent C code:

```c
if (x==1) goto dest;
```

The English description of `jxi dest` is as follows:

* if bit `x` of the `flags` register is a 1:
  * continue execution at `dest`
* else
  * continue execution at the instruction immediately following (`jxi dest`)

# How does it work?

Let's use `jci` as a specific example. The microcode of `jci` configures the processor as follows:

* `PCMuxMux` (from ROM.D) is `000`, connecting bit 0 of the `flags` register to the tunnel `PCMux`
* `PCEn` is `1`
* `AddrMux` is 1, connecting `PC.Q` to `RAM.A`
* `RO0En` is 0, *half* enabling the mux connecting to input 1 of the mux that outputs to `PC.D`

The trick is that `PCMux`, which is now connected to bit 0 of `flags.Q` (it is the carry flag), specifies the selection of the mux that outputs to `PC.D`. This allows the choosing of increment by one (when `PCMux==flags.Q[0]`) is 0, or to update using `*PC` (when `PCMux==flags.Q[0]`) is 1.

This is why the RTL description of `jci` is as follows:

```c
PC=C ? *PC : PC+1;
```

In essence, TTP uses one of the bits of the `flags` register to control the multiplexers that route content to `PC.D`.

# What about `jnci`?

Most architectures support a 'jump iff a flag is 0' variant. In RTL, most architectures offer a counterpart `jnci` to `jci` that can be described as follows:

```c
PC=(!C) ? *PC : PC+1;
```

However, such an instruction is really not necessary. The following *hypothetical* instruction

```text
jnci dest
```

can be implemented by the following sequence:

```ttpasm
jci  cont // continue if C=1
jmpi dest // otherwise go to dest
cont:     // continuation point
```



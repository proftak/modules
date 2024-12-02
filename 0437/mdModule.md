---
title: "Module 0437: Implementation structures in TTPASM
---

# _{{ page.title }}_

## Linked list example

```c
#include <stdint.h>

struct X
{
  uint8_t v;
  struct X *next;
};

struct X n3 = { 2, 0 };
struct X n2 = { 5, &n3 };
struct X n1 = { 16, &n2 };

int main() 
{
  struct X *ptr;
  uint8_t array[3];
  uint8_t i;
  ptr = &n1;
  i = 0;
  while (ptr)
  {
    array[i] = ptr->v;
    ++i;
    ptr = ptr->next;
  }
  return 0;
}
```

The above C code has three global initialized structures that forms a linked list. The following is the TTPASM implementation of the same code.

```ttpasm
  nop
  ldi d,0
  ldi a,. 6 +
  dec d
  st  (d),a
  jmpi main
  halt

// key concept: labels are used to describe a structure
X_v: 0 // offset of member v from the beginning of a struct X
X_next: X_v 1 + // offset of member next from the beginning of a struct X
X_size: X_next 1 + // size of a struct X

// key concept: global initialized struct X are allocated and initialized byte-by-byte
n3: // the label is the address of n3
  byte 2 // member v
  byte 0 // member next
n2:
  byte 5
  byte n3
n1:
  byte 16
  byte n2

main:
  main_ptr: 0
  main_array: main_ptr 1 +
  main_i: main_array 3 +
  main_lvs: main_i 1 +

  ldi b,main_lvs
  sub d,b

  ldi a,n1
  ldi b,main_ptr
  add b,d
  st  (b),a

  ldi a,0
  ldi b,main_i
  add b,d
  st  (b),a

  while0_begin:
    ldi  b,main_ptr
    add  b,d
    ld   c,(b)
    and  c,c
    jzi  while0_end

      // the value of member v of the structure
      // that is pointed to by ptr

      ldi  b,X_v
      add  c,b // c == &(ptr->v)
      ld   c,(c) // c == ptr->v
      ldi  a,main_i
      add  a,d
      ld   a,(a)
      ldi  b,main_array
      add  b,d
      add  b,a // b == &array[i]
      st   (b),c

      ldi  a,main_i
      add  a,d
      ld   b,(a)
      inc  b
      st   (a),b

      ldi  a,main_ptr
      add  a,d
      ld   c,(a)
      ldi  b,X_next
      add  c,b // c == &(ptr->next)
      ld   c,(c) // c == ptr->next
      st   (a),c

    jmpi while0_begin
  while0_end:

  ldi b,main_lvs
  add d,b

  ld  b,(d)
  inc d
  jmp b
```

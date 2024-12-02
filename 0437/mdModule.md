---
title: "Module 0437: Implementation structures in TTPASM"
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

## Initialization of a "free list"

The following C program illustrates how to initialize a linked list of free nodes, where one node points to the next one. All the nodes are allocated as an array of structures as a global variable.

```c
#include <stdint.h>

struct Node {
  uint8_t value;
  struct Node *next;
};

#define NUMNODES 5

struct Node nodes[NUMNODES];

struct Node *freePtr;

void initNodes() {
  struct Node *ptr;
  uint8_t count;

  ptr = nodes;
  count = NUMNODES-1;
  while (count)
  {
    ptr = (ptr->next = (ptr+1));
    count = count - 1;
  }
  ptr->next = 0;
  freePtr = &nodes[0];
}

int main()
{
  initNodes();
  return 0;
}
```

The following is the equivalent program implemented in TTPASM. Note that TTPASM does not have an easy way to "allocate a block of bytes" for the `nodes` array.

```ttpasm
  nop
  ldi  d,0
  ldi  a,. 6 +
  dec  d
  st   (d),a
  jmpi main
  halt

Node_value: 0
Node_next: Node_value 1 +
Node_size: Node_next 1 +

NUMNODES: 5

nodes:
  byte 0  // nodes[0].value
  byte 0  // nodes[0].next
  byte 0  // nodes[1].value
  byte 0  // nodes[1].next
  byte 0
  byte 0
  byte 0
  byte 0
  byte 0
  byte 0

freePtr:
  byte 0

initNodes:
  initNodes_ptr: 0
  initNodes_count: initNodes_ptr 1 +
  initNodes_lvs: initNodes_count 1 +

  ldi  b,initNodes_lvs
  sub  d,b

  ldi  a,nodes
  ldi  b,initNodes_ptr
  add  b,d
  st   (b),a

  ldi  a,NUMNODES 1 -
  ldi  b,initNodes_count
  add  b,d
  st   (b),a

  initNodes_while0_begin:
    ldi  a,initNodes_count
    add  a,d
    ld   a,(a)
    and  a,a
    jzi  initNodes_while0_end

      ldi   a,initNodes_ptr
      add   a,d
      ld    b,(a)
//      cpr   c,b
//      inc   c
//      inc   c 
      ldi   c,Node_size
      add   c,b 
      ldi   a,Node_next
      add   a,b
      st    (a),c
      ldi   a,initNodes_ptr
      add   a,d
      st    (a),c

      ldi   a,initNodes_count
      add   a,d
      ld    b,(a)
      dec   b
      st    (a),b

    jmpi initNodes_while0_begin
  initNodes_while0_end:

  ldi  a,initNodes_ptr
  add  a,d
  ld   a,(a)
  ldi  b,Node_next
  add  a,b
  ldi  b,0
  st   (a),b

  ldi  a,nodes
  ldi  b,freePtr
  st   (b),a

  ldi  b,initNodes_lvs
  add  d,b

  ld   b,(d)
  inc  d
  jmp  b

main:
  ldi  a,. 6 +
  dec  d
  st   (d),a
  jmpi initNodes

  ld   b,(d)
  inc  d
  jmp  b
```

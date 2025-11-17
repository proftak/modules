---
title: "Module 0461: Types and Structures"
---

# What is a type?

A "type" in programming specifies a category of values. We have already encountered a few up to this point:

* `int`: short for integer.
* `bool`: short for Boolean. This is a category of values that can only be true or false.
* `double`: short for "IEEE Double Precision Floating Point". This is a category of values that is *like* real numbers in mathematics.
  
# What is a structure?

A structure is the packaging of multiple items into a logical unit. Each component of a structure is called a member. Members are distinguished from each other by their unique names.

The main purpose of using structures is organization. Without structures, programs can still be written, but such programs also become prone to errors. 

Imagine that instead of a single page of a physical form, each field of the form is on a little slip of paper. This is an analogy of what happens without structures. 

If we think of a structure as a form, then it is a form *template*. Think of this as the master copy of a form. To make an actual form for a person to fill in, we use a copier to make a photocopy of the master copy, and the photocopy is the one that we let people write over.

In C++ terminology, the template is called the structure, and the photocopy is called an object, or an instance of the structure.

Another way to think of it is that a structure is a cookie-cutter, and an object or structure instance is a cookie cut out from cookie dough using the cookie-cutter.

# An example

```c
struct StudentRecord {
  int id;
  double gpa;
  bool active;
};
```


---
title: "Module 0461: Types and Structures"
---

# What is a type?

A "type" in programming specifies a category of values. We have already encountered a few up to this point:

* `int`: short for integer.
* `bool`: short for Boolean. This is a category of values that can only be true or false.
* `double`: short for "IEEE Double Precision Floating Point". This is a category of values that is *like* real numbers in mathematics.

All three are known as *built-in* types in C++. These are also called "scalar" types or "atomic" types because they are elemental and cannot be broken up into smaller pieces in C++.
  
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

This is the *definition* of a structure (the cookie cutter). The cookie cutter has a name of `StudentRecord`, and the structure has three members:

* `id` is an integer member.
* `gpa` is a real number member.
* `active` is a Boolean member.

A cookie cutter is fairly useless, let us expand the program as follows:


```c
struct StudentRecord {
  int id;
  double gpa;
  bool active;
};

int main() {
  struct StudentRecord aRec;

  aRec.id = 1920416;
  aRec.gpa = 3.5;
  aRec.active = true;

  return 0;
}
```

The line that reads `struct StudentRecord aRec;` uses the structure as a user-defined type to create the object (structure instance, or cookie) called `aRec`. The subsequent lines assign specific values to each member of the structure instance/object/cookie.

The "dot notation" can be thought of as the apostrophe-s in English (possessive). This means that the expression `aRec.gpa` can be interpreted as "aRec's GPA (member)" or "the GPA member of aRec". 

In a trace, a column is used for each member in a structure instance that is of a built-in type. This implies that structure definitions can nest. Consider the following:

```c
struct Academic {
  double gpa;
  bool active;
};

struct StudentRec {
  int id;
  struct Academic aData;
};

int main() {
  struct StudentRec aRec;

  aRec.aData.gpa = 3.5;
  aRec.aData.active = true;
  aRec.id = 1729384;

  return 0;
}
```

The execution of this code is traced as follows:

<div style="font-family: monospace;" markdown=1>

| |A|B|C|D|E|
|-|-|-|-|-|-|
|**1**|comments|line#||||
|**2**||pre||||
|**3**||11||||
|**4**||12|aRec.aData.gpa|aRec.aData.active|aRec.id|
|**5**|||?|?|?|
|**6**||14|3.5|||
|**7**||15||true||
|**8**||16|||1729384|
|**9**||18||||
|**10**||post||||

</div>

# Structure assignment

An single assignment statement can copy an entire structure instance to another.

# Passing a structure as a parameter

Unlike an array which can only be passed by reference, a structure can be passed by reference of by value.
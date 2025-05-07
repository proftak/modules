---
title: "Module 0456: A session of writing an algorithm"
---

# What is this?

This document serves multiple purposes. It states a problem to be solved, a log of how it is solved, and the distillation of the process involved. The distillation is a generalization of the approach that can be applied to general algorithm (code) development.

# The "Problem"

The word problem has a negative connotation. A "problem" in this context is more like "a task to automate."

## What is given

It is crucial to understand what the "input" of an algorithm consists of. For the task this article will automate, here are the inputs:

* An array "ids" where each element of the array corresponds to the ID number of a student. All elements of this array are unique. (What does unique mean?)
* An array "scores" where each element is a real (what does this mean?) value from 0 to 1, indicating the ratio of points earned divided by points possible. The position of elements of this array corresponds to the "ids" array. This means `scores[5]` is the score earned by the student corresponding to the ID of `ids[5]`.
* Neither `ids` nor `scores` is sorted.
* An array "grades" where each element specifies a threshold of a letter grade. `grades[0]` is the minimum score to earn a letter grade of "D", `grades[1]` is the minimum score to earn a letter grade of "C", etc.
* An integer "numStudents" that indicates the number of students in a class. The arrays `ids` and `scores` have `numStudents` elements.

## The output

It is equally important to understand what the expected output is:

* An array "grades" where each element of the array corresponds to the letter grade of a student of a matching element of the same index in the `ids` array. A value of 0 means a letter grade of F, etc.
* A real number "average" that is the "mean" of scores in the class.
* A real number "sd" that is the standard deviation (what does this mean?) of scores in the class.
* Bonus (good to have, but not necessary): an array "ranking" where each element of the array corresponds to the ranking of a student of a matching element of the same index in the `ids` array. In this context, rank 1 means the highest score, rank 2 means the second highest score, etc.

# Process log

We will do this in class!

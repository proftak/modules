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

## The top-down approach

The top-down approach is similar to outlining when writing essays. While top-down is an excellent way to divide a big problem into smaller logical units, the top-down approach is not exactly conducive to writing actual algorithms.

In our example, the top-down approach is great for breaking the overall program down into smaller parts. In this process, a larger component is broken into smaller components, *but not necessarily how the smaller components are structured in the larger component.*

For example, based on the output specification, we know that we need the logic to work on each student and figure out the letter grade. This suggests that the bigger problem of "for each student..." includes a smaller problem of "convert a score to a letter grade."

## The bottom-up step

In order to convert a score to a letter grade, we first examine what is needed and not so much how to specify the logic:

* the score
* an array of letter thresholds
* due to the limitation of C/C++, an array parameter also needs a length as a separate parameter
* the answer is an integer where 0 represents 'F', 1 represents 'D', etc.


Based on this analysis, we can determine the *prototype* of the function is as follows:

```c
int scoreToGrade(double score, double thresholds[], int numThresholds);
```

A prototype of a function expresses the *interface* (the "what") of a function, but it does not include the actual algorithm (the "how"). In a prototype specification, the return type, function name, and a parenthesized list of parameters are specified, much like a function *definition*. The main difference is that instead of a brace-enclosed block of code, a semicolon is used to terminate a prototype specification.

### Working out the algorithm

The first step in working out an algorithm is to perform the task by hand. In this case, a *typical* threshold table for grading is as follows:

|threshold|lowest grade if exceeding the threshold|
|-|-|
|60%|D|
|70%|C|
|80%|B|
|90%|A|

Given a score of 75%, what is the matching grade? In the attempt to perform this task, it is best to refrain from using the "eyeball" algorithm. The eyeball algorithm refers to quickly scanning and "intuitively" completing the task. 

Instead, try to think of a way to describe how to complete the task to a person who does not know how to perform this task. In this case, the description may be similar to the following:

The lowest possible grade is an 'F'. Compare the given score to the left column of the table. If the score is greater than the threshold, move to the next row. Keep doing this until one of the following happens:
the
* A letter grade of A, or
* The threshold is larger than the score.

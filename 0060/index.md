---
title: "Module 0060: Algorithms to search for an item in an array"
---

# About this module

-   Prerequisites: [0054](../0054)

-   Objectives: This module improves the linear search algorithm for
    sorted arrays. It also introduces binary search, a very efficient
    search algorithm for sorted arrays.

# Sorted arrays

The linear search algorithm in module [0054](../0054) is the only kind
of search algorithm that works on unsorted arrays. In the worst case,
*all* elements in the array must be examined to confirm that a value is
not in the array.

However, we can make some improvements with sorted arrays.

Assume that array `a` is sorted, and assume `n` is the number of elements in array `a`. Furthermore, let us assume that the array is
sorted in a non-decreasing order. This implies that we can have
duplicate values in the array. The mathematical way to say an array is
sorted in a non-decreasing order is as follows:

`a[i] <= a[i+1]` for `i` ranging inclusively from 0 to `n-2`. We can also spell this out as
`a[0] <= a[1] <= a[2]... a[n-1]`.

The following algorithm results in a value of true in variable `sorted` when it completes if and only if array `a` is sorted:

```c
i=0;                                 // line 1
sorted=true;                         // line 2
while (sorted && i<n-1) {            // line 3
  sorted = sorted && (a[i]<=a[i+1]); // line 4
  i=i+1;                             // line 5
}                                    // line 6
```

As an exercise, try tracing this algorithm using a sorted array and an unsorted array.

# Linear search

We can improve our linear search algorithm to work more efficiently. The original algorithm is described as the following algorithm.

```c
// Linear search algorithm that works for sorted and unsorted arrays
// Assume v contains the value to be search in an array a that has n elements
// Assume array a elements have specific values
i=0;
while ((i<n) && (a[i] != v))
  i = i + 1;
if (i=n)
  // conclude no element in a has a value of v
else
  // conclude a[i] is the first element with a value of v
```

Note that if array `a` is sorted in a non-decreasing way, and we find that `v < a[i]`, then we already know that
`v < a[i] <= a[i+1] <= a[i+2]... a[n-1]`. This also means that `v != a[i+1]$, v != a[i+2]`, all the way
up to `v != a[n-1]`.

This property of a sorted array means that we can exit the loop earlier
when we discover that `v < a[i]`. This is great news! On the other hand,
we need to modify the conditional statement because now we can exit with
`i < n` and still conclude that value $v$ is not anywhere in the
array. The condition that confirms that value `v` is not in the array
should be `(i == n) || (a[i] != v)`.

As a result, the algorithm is modified as in the following algorithm.

```c
// Improved linear search algorithm that works only for non-decreasingly sorted arrays.
i=0;
while ((i<n) && (a[i]<v))
  i=i+1;
if ((i==n) || (a[i] != v))
  // conclude no element in a has a value of v
else
  // conclude a[i] is the first element in a that has a value of v
```

With this modification, the number of elements to examine is variable
when the value $v$ is not in the array. In the worst case,
when `v > a[n-1]`, we still need to examine all `n` items in the array.

# Binary search

## Concept

Binary search works only if an array is sorted. The basic idea is to
compare the value to find with an element in the middle of the array.
Depending on the outcome, we can throw away one half of the candidates,
or confirm the value does exist.

Let us assume that we compare $v$ with $a[m]$, the first candidate has
an index of $b$, and the last candidate has an index of $e$. Then, there
are three possible outcomes:

-   $v = a[m]$: the search is over! We just confirmed that value $v$ can
    be found in the array.

-   $v < a[m]$: we can throw away $a[m]$, $a[m+1]$,\... $a[e]$.

-   $v > a[m]$: we can throw away $a[b]$, $a[b+1]$,\... $a[m]$.

If we pick $m$ to be half way between $b$ and $e$, then we can throw
away at least one half of the candidates after one comparison.

## Algorithm

The binary search algorithm is described in algorithm
[\[algorithm:bsearch\]](#algorithm:bsearch){reference-type="ref"
reference="algorithm:bsearch"}. This algorithm assumes that $a$ is an
array with at least one item, and $v$ is the value that we are searching
for.

``` {#algorithm:bsearch .numberLines .pseudocode language="pseudocode" numbers="left" label="algorithm:bsearch" caption="The binary search algorithm"}
%$e \leftarrow |a|-1$ \label{bsearch:inite}%
repeat %\label{bsearch:repeat}%
  %$m \leftarrow \lfloor \frac{b+e}{2} \rfloor$ \label{bsearch:computem}%
  if %$a[m] < v$% then %\label{bsearch:firsthalf}% then
    %$b \leftarrow m+1$ \label{bsearch:moveb}%
  else
    if %$v < a[m]$% then %\label{bsearch:secondhalf}% 
      %$e \leftarrow m - 1$ \label{bsearch:movee}%
    end if
  end if
until %$(b > e) \vee (a[m] = v)$ \label{bsearch:until}%
if %$b>e$% then %\label{bsearch:notfound}%
  // conclude %$v$% cannot be found in %$a$%
else
  // conclude %$v$% is found in %$a$%
end if
```

Let us dissect this algorithm.

-   Lines [\[bsearch:initb\]](#bsearch:initb){reference-type="ref"
    reference="bsearch:initb"} and
    [\[bsearch:inite\]](#bsearch:inite){reference-type="ref"
    reference="bsearch:inite"} initialize variables $b$ and $e$,
    respectively. $b$ is the index of the first element that can still
    contain value $v$. It is initialized to 0 because we need to
    consider all elements initially. For the same reason, $e$ is
    initialized to $|a|-1$ because that is the index of the last element
    in the entire array.

-   Everything between line
    [\[bsearch:repeat\]](#bsearch:repeat){reference-type="ref"
    reference="bsearch:repeat"} and line
    [\[bsearch:until\]](#bsearch:until){reference-type="ref"
    reference="bsearch:until"} is the logic of binary search.

-   Line [\[bsearch:computem\]](#bsearch:computem){reference-type="ref"
    reference="bsearch:computem"} computes the value of $m$ so it is
    half-way between $b$ and $e$. The symbol $\lfloor x \rfloor$ is
    called the "floor" of $x$. The floor of $x$ is the largest integer
    that is less than or equal to $x$. In *this context*, we are simply
    truncating any fractional value.

-   Line
    [\[bsearch:firsthalf\]](#bsearch:firsthalf){reference-type="ref"
    reference="bsearch:firsthalf"} checks to see if we can remove the
    first half of the candidates. If $a[m] < v$, then we know that
    $a[b] \le a[b+1] \le a[b+2] \ldots a[m] < v$, and so we can
    eliminate all those elements as candidates.

-   Line [\[bsearch:moveb\]](#bsearch:moveb){reference-type="ref"
    reference="bsearch:moveb"}: Once we know that we can eliminate the
    first half of the candidates, we can do so by changing $b$. Note
    that we do not change to $b$ to $m$ because $a[m] \ne v$. Instead,
    we move $b$ to $m+1$. This subtle point makes all the differences in
    terms of terminating the loop.

-   Lines
    [\[bsearch:secondhalf\]](#bsearch:secondhalf){reference-type="ref"
    reference="bsearch:secondhalf"} and
    [\[bsearch:movee\]](#bsearch:movee){reference-type="ref"
    reference="bsearch:movee"} are the counterparts of lines
    [\[bsearch:firsthalf\]](#bsearch:firsthalf){reference-type="ref"
    reference="bsearch:firsthalf"} and
    [\[bsearch:moveb\]](#bsearch:moveb){reference-type="ref"
    reference="bsearch:moveb"}. Instead of getting rid of the first
    half, these lines checks to see if we can eliminate the self half.

-   Line [\[bsearch:until\]](#bsearch:until){reference-type="ref"
    reference="bsearch:until"} specifies when we can get out of the
    loop. There are two reasons. First, when $b > e$, we have no
    candidates left. Note that when $b = e$, it means that there is one
    more element to be considered. Second, when $a[m] = v$, there is
    nothing to check anymore, because we have just found an element of
    value $v$.

-   Line [\[bsearch:notfound\]](#bsearch:notfound){reference-type="ref"
    reference="bsearch:notfound"} checks to see if value $v$ is found in
    the array or not. If $b > e$, it means that we exited the loop
    because we ran out of candidates. Therefore, we can then confirm
    that value $v$ does not exist in $a$.

## Now, that's efficient!

The binary search algorithm is very efficient because each comparison
eliminates at least one half of the remaining candidates. This means
that if we start off with 511 candidates, we'll end up with 255 after
one comparison, 127 after two comparisons, 63 after three comparisons,
and etc. It'll take 9 comparisons that confirm a value $v$ is not in an
array of 511 elements.

Let $n = |a|$, and $q$ be the number of comparisons needed to confirm
$v$ is not in $a$. Then $q = \lceil \log{(n)} / \log{(2)} \rceil$. The
symbol $\lceil x \rceil$ is the ceiling of $x$, which is the smallest
integer that is larger than or equal to $x$.

Using this formula, to look up a name in a phonebook with 6 billion
entries will only take up to 33 comparisons!

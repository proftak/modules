---
title: "Module 0090: Categories of Time Complexity"
---

# About this module

- Prerequisites: [0082](../0082), [0068](../0068)

- Objectives: This module explores various common categories of time
  complexities.

# Linear search

Linear search has a time complexity of $T(n) \in \Theta(n)$, where
$T(n)$ is the actual amount of time needed to search for an item in an
array of $n$ items. This part is proven in module [0085](../0085).

However, to make this more useful, any algorithm that has a time
complexity of $T(n) = k_1 + T(n-1)$ also has the same time complexity of
$T(n) \in \Theta(n)$. Note that this is a recursive definition of the
time complexity, which implies that it is only useful for recursive
algorithms.

It is fairly easy to turn the iterative linear search algorithm into a
recursive one. Listing
[\[listing:reclinsearch\]](#listing:reclinsearch){reference-type="ref"
reference="listing:reclinsearch"} is one:

``` {#listing:reclinsearch .numberLines .pseudocode language="pseudocode" numbers="left" caption="recursive linear search" label="listing:reclinsearch"}
define sub linsearch
  by reference a : array of valueType
  by value b : integer
  by value v : valueType
  return type : boolean
  local r : boolean
  r := 0
  if (b < |a|) then
    r := (a[b] = v) OR linsearch (a, b+1, v)
  end if
  return r
end define sub
```

# Selection sort, bubble sort, insertion sort, etc.

Selection sort, bubble sort and insertion sort can all be done
recursively without changing the time complexity. For example, selection
sort can be implemented as in listing
[\[listing:recselect\]](#listing:recselect){reference-type="ref"
reference="listing:recselect"}.

``` {#listing:recselect .numberLines .pseudocode language="pseudocode" numbers="left" caption="selection sort" label="listing:recselect"}
define sub selection
  by reference a : array
  by value b : integer
  if (|a|-1 > b) then
    local m : integer
    local i : integer
    m := b
    i := b+1
    while i < |a| do
      if a[i] < a[m] then
        m := i
      end if
      i := i + 1
    end while
    swap(a[b], a[m])
    selection(a,b+1)
  end if
end define sub
```

This make the analysis of time complexity much easier. Let us assume
$T(n)$ denotes the time required to sort an array of $n$ items. Then, we
know that $T(1) = k$ for some constant $k$. This is because the loop and
recursion only occurs when $|a| - 1 > b$, which means there are more
than 1 elements to sort.

In general, $\forall n > 1: T(n) = k_1 + k_2n + T(n-1)$. This is because
the loop looks for the index of the smallest element from index $b$ to
the end of the array, that requires $n$ time (remember, $n$ is not the
size of the array, but the number of items to sort). In addition, once
$a[b]$ is sorted, we proceed to call the subroutine recursively to sort
the portion of the array starting at index $b+1$.

Let us get rid of $k_1$ because it is a constant, and we already know
the term $k_2n$ is asymptotically dominant with respect to $k_1$. Then
we have a general recursive definition $T(n) = k_2n + T(n-1)$ and
$T(1) = k$. For estimate purposes, it is okay to make $k = k_2$ to
simplify the analysis.

I claim that $T(n)$ has a closed form of $T(n) = k\frac{n(n+1)}{2}$.
This can be proven by induction. The base case is when $n=1$, then
$T(1) = k\frac{1(1+1)}{2} = k$. The induction step states that if we
assume the closed form works for case $n=j, j \ge 1$, it should work for
case $n=j+1$. Here is the proof:

$$\begin{eqnarray}
  T(j+1) & = & k(j+1) + T(j) \\
         & = & k(j+1) + k\frac{j(j+1)}{2} \\
         & = & k\frac{2(j+1) + j(j+1)}{2} \\
         & = & k\frac{(j+2)(j+1)}{2}
\end{eqnarray}$$

Now that we know that $T(n) = k\frac{n(n+1)}{2}$, we can proceed to show
that $T(n) \in O(n^2)$ and $T(n) \in \Omega(n^2)$. Because $T(n)$ does
not oscilate, we can prove both at the same time:

$$\begin{eqnarray}
    \lim_{n \rightarrow \infty}\frac{T(n)}{n^2} 
      & = & 
        \lim_{n \rightarrow \infty}\frac{k\frac{n(n+1)}{2}}{n^2} \\
      & = &
        \frac{k}{2}\lim_{n \rightarrow \infty}\frac{n(n+1)}{n^2} \\
      & = &
        \frac{k}{2}\lim_{n \rightarrow \infty}\frac{n^2+n}{n^2} \\
      & = &
        \frac{k}{2}\lim_{n \rightarrow \infty}\frac{n^2}{n^2} +
        \frac{k}{2}\lim_{n \rightarrow \infty}\frac{n}{n^2} \\
      & = &
        \frac{k}{2}\lim_{n \rightarrow \infty}1 +
        \frac{k}{2}\lim_{n \rightarrow \infty}\frac{1}{n} \\
      & = &
        \frac{k}{2} +
        \frac{k}{2}0 \\
      & = &
        \frac{k}{2}
\end{eqnarray}$$

Because $\frac{k}{2} > 0$ and $\frac{k}{2} < \infty$, we know that
$T(n) \in \Theta(n^2)$.

What is significant about this proof is that the time complexity of any
algorithm that fits the profile of $T(n) = k_1 + K_2n + T(n-1)$ has a
time complexity of $\Theta(n^2)$.

# Binary search

We explored binary search in module [0085](../0085). We already know
that its time complexity is $\Theta(\log(n))$, where $n$ is the number
of elements in the array being searched.

The pattern of the time complexity of binary search is
$T(n) = k_1 + T(n/2)$. This is because it reduces the number of
candidates by half for each iteration. As it turns out, any algorithm
that fits the pattern of $T(n) = k_1 + T(r\cdot n)$ ($r < 1$) has a time
complexity of $\Theta(\log(n))$.

# Merge sort

Merge sort and the average case of quick sort have a complexity of
$T(n) \in \Theta(n\log(n))$, where $n$ is the number of elements in the
array being sorted. We proved this in module [0079](../0079) for the
iterative version of merge sort. We also proved this in module
[0087](../0087) for the recursive version of quicksort.

The general pattern of algorithms with this kind of time complexity is
$T(n) = k_1 + k_2n + T(rn) + T((1-r)n)$ ($0.5 \le r < 1$).

We can proof this informally as follows. If we look at the invocation
tree, each level needs to handle a total of at most $n$ items.
Consequently, the time complexity of each level is proportional to $n$.
The number of levels required $L$ depends on $r$, as $L = \lceil
  \frac{\log(n)}{\log(1/r)} \rceil$. As a result, the time complexity of
the entire invocation tree is proportional to $\frac{1}{\log(1/r)}n
  \log(n)$. Because $\log(1/r)$ is a term that is independent of $n$, it
is absorbed in the overall constant.

More formally, we can show that the first level has $n$ items. The
second level has two parts, $rn$ and $(1-r)n$. The third level has four
parts, $r^2n$, $(1-r)rn$, $r(1-r)n$ and $(1-r)^2n$, and etc. The fourth
level has 8 parts, $r^3n$, $r^2(1-r)n$, $r(1-r)rn, (1-r)r^2n,
  \ldots (1-r)^3n$. In general, at level $i+1$, each part can be
expressed as a permutation of $n$ times $i$ coefficients, each
coefficient is either $r$ or $(1-r)$. Each coefficient represents a
split point in the invocation tree that splits the number of elements
into $r$ and $1-r$ proportions. This means in terms of combinations,
there are $i \choose i$ terms with the $r^i$ coefficient,
$i \choose {i-1}$ terms with the $r^{i-1}(1-r)$ coefficient, and etc.

As an exercise, draw the invocation tree, and indicate the number of
operations (excluding those from recursive calls) of each node of the
tree. It is helpful to at least show up to level 3, or a part of level
4.

If we group by coefficients of the form $r^j(1-r)^{i-j}$, there are
${i \choose j}$ of those parts. Consequently, the total of all the parts
at level $i+1$ is $x = \sum_{j=0}^{i} {i \choose j}r^{j}(1-r)^{i-j}$. We
know that $x = 1$ because the formula is the same as the total
probabilities of a binomial distribution with a success ratio of $r$ and
$i$ trials! You can refer to module [0062](../0062) for a more detailed
discussion of the binomial distribution.

This proves that the total number of operations per level of the
invocation tree is $n$. The tree only needs to go as deep as
$L = \frac{\log(n)}{\log(1/r)}$ levels because $T(1)$ is the base case.
As a result, the total number of operations of the entire invocation
tree is proportional to $nL = 
  n\frac{\log(n)}{\log({1/r})} = \frac{1}{\log(1/r)}n\log(n)$.

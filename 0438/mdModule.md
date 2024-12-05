---
title: "Module 0438: CIS sections offering and full-time schedule sign up (proposed)"
---

# _{{ page.title }}_

## Section offering

## Section request/assignment

### Priority determination

According to the LRCFT contract, the dean of a division has the right of assignment. As such, this section only applies to the prioritization of *requests*.

A somewhat random and fair way to change priority per semester is to serialize all possible permutations, then use a large prime number to step through the generated results. This can be done using a script like the following:

```javascript
"use strict";
module.paths.unshift('/usr/local/lib/node_modules')
const combinatorics = require('/usr/local/lib/node_modules/js-combinatorics/commonjs/combinatorics.js')

let x = [...(new combinatorics.Permutation([0,1,2,3,4,5,6,7,8,9]))]
console.log(x.length)
const p = 1000861
for (let i = 0, j=p; i < 20; ++i)
{
  console.log(x[j].join(','))
  j = (j + p) % 3628800
}
```

The output of this script is as follows:

```text
2,7,8,5,0,4,6,1,9,3
5,4,7,1,2,0,3,8,6,9
8,2,4,7,1,5,6,3,9,0
1,0,4,5,6,2,3,9,7,8
3,8,0,9,4,5,6,7,2,1
6,4,9,3,5,0,2,1,7,8
9,2,7,0,5,4,8,1,6,3
2,0,6,7,8,1,4,5,3,9
4,8,3,1,7,5,9,2,6,0
7,5,1,8,9,0,3,6,2,4
0,4,1,5,9,6,8,7,3,2
3,0,9,1,2,4,7,5,6,8
5,8,6,4,0,7,1,2,9,3
8,5,4,1,2,0,7,6,3,9
1,4,3,8,2,7,0,6,9,5
4,1,2,5,6,0,8,9,3,7
6,8,9,7,2,4,0,5,3,1
9,5,7,3,4,0,8,1,2,6
2,4,7,0,6,8,3,1,9,5
5,1,4,7,8,0,9,3,2,6
```

Each faculty member can be assigned a particular position in a list, and each list is for one semester. As a result, this list is enough for about 6 years because there are three chances to sign up for classes per academic year.

### Request iterations

For the Fall and Spring semesters, each semester has 3 iterations of requesting sections.

In the **first** iteration, the priority determines the order in which each faculty member can sign up for up to 0.5 FTE. This means the total FTE request in this iteration cannot exceed an entire section beyond 0.5 FTE. 

In the **second** iteration, the same priority determines the order in which each faculty member can sign up for up to 1.0 FTE. Again, this means the total FTE request of the first and the second iterations combined cannot exceed an entire section beyond 1.0 FTE.

The **third** iteration is for overload. Faculty members are offered an opportunity in the same priority assignment to request overload FTEs. Combining the first, second, and third iterations, the total FTE requested cannot exceed 1.4 FTE.


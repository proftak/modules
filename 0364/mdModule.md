---
title: "Module 0364: An example of how to understand something"
author: Tak Auyeung
---

# Why do I want to read this article?

This article outlines my (Tak's) process of understanding new technical documents. Why would you want to read about someone else's learning process?

Let us first address the importance of self-learning. When you are "in school", be it high school or college, there are teachers and professors to help you understand academic material. However, as a STEM worker, you may be unable to rely on your employer to provide guided education.

The guided learning environment in elementary school all the way up to college is a form of training wheels. As such, it is important to learn how to self-learn before the training wheels disappear.

Note that a career in a fast-changing STEM field like computer science requires *constant* self-learning. 

# Credit

The quantum computing example used in this module is from a publication *Quantum Algorithm Implementation for Beginners* published by Los Alamos National Lab. The full paper is published in [the ACM (Association for Computing Machinery) Digit Library](https://dl.acm.org/doi/10.1145/3517340). 

# How to read this document

If you have a strong interest in learning about quantum computing, read this document sentence-by-sentence! However, I suspect the average reader is not interested in quantum computing.


<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

The right boxes contain points related to the general process of understanding abstract and technical concepts. You can focus on the content in these right boxes and ignore the rest of the content.

</div>

If you are not interested in quantum computers and just want to get the main points of this article, read just the "right boxes" of this document. These boxes contain just the points related to learning and understanding material without reference to actual topics in quantum computing.

Furthermore, the section titled [A bit of non-technical discussion](#a-bit-of-non-technical-discussion) is a non-technical FAQ/FYI section intended to address some of the most common issues that many people encounter.

# The definition of the state of a qubit (section 1.1.1)

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

Read a paragraph or two at a time. As you read, jot down the terms and/or concepts that need additional clarification or definition. Many writers first introduce a concept or definition, *then* proceed to lay out the terminology and assumptions used in the explanation. 

**It is important to use notes to track what concepts or terms remain to be resolved.** There will be another module focusing on note-taking.

</div>

We will start with the following definition, which is the very first definition of the quoted publication.

> The state of a qubit can be expressed as $\ket{\phi} = \alpha \ket{0} + \beta \ket{1}$. 

First, we need to know what each symbol represents. As with most definitions, the explanations of the symbols used *follow* the definition. This means it is helpful to read ahead a little after encountering a new definition.

The explanations of the symbols are as follows:

> Here $\alpha$ and $\beta$ are complex numbers such that, $\|\alpha\|^2+\|\beta\|^2 = 1$.


Fortunately, I vaguely remember what a complex number is. A quick search finds that a complex number has two components, one coefficient for a real component, and one coefficient for the imaginary component. In other words, if $x$ is a complex number, it can be expressed as $x=x_r + x_i i$ where $i$ is the imaginary number of $\sqrt{-1}$.


<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

A *vague* memory is not sufficient! Spending the extra few minutes to *confirm* an understanding of a concept learned some time ago is important. A wrong assumption can end up wasting far more than the amount of time taken to verify.

</div>

The $\ket{\dots}$ symbol is new to me. There is a little explanation in the publication:

> In the *ket-notation* or the *Direac notation*, $\ket{0}=\pmatrix{1 \\ 0}$ and $\ket{1} = \pmatrix{0 \\ 1}$ are shorthands for the vectors encoding the two basis states of a two-dimensional vector space.

This explanation seems to be very specific to $\ket{0}$ and $\ket{1}$, but it does not quite explain the general "ket" notation. So I looked it up.

A quick search found an entry in Wikipedia, explaining:

> A **ket** is of the form $\ket{v}$. Mathematically, it denotes a vector, $v$, in an abstract (complex) vector space $V$, and physically it represents a state of some quantum system.


<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

One new definition or concept ~~may~~ *often* require an understanding of other definitions or concepts. Your mind can probably track three new concepts being learned.

As a result, it is important to write your own notes as you drill down this "folder structure" of concepts. One effective method to track and organize concepts is using a nested bullet list:

* quantum computing
  * qubit (section 1.1.1)
    * ket notation
      * complex number
      * complex vector space
      * meaning of $\ket{0}$ and $\ket{1}$
    * unit vector length requirement

</div>

From linear algebra, I understand what a vector (like an array in programming) is. However, the term of "abstract (complex) vector space" is new to me. I know what a general vector is, and I know what a complex number is. However, I am not sure how to combine these two concepts as "complex vector space."

Note that I do not move on thinking that I "sort of" understand the concept and "call it good enough!"

Wikipedia defines a vector space as follows:

> In mathematics, physics, and engineering, a vector space is a set whose elements, often called vectors, may be added together and multiplied ("scaled") by numbers called scalars. Scalars are often real numbers, but can be complex numbers or, more generally, elements of any field. ... The terms real vector space and complex vector space are often used to specify the nature of the scalars: real coordinate space or complex coordinate space.

From this, I understand that what differentiates a "real/normal" vector space from an "abstract/complex vector space" is *whether the scalar can only be a real number or a complex number*. Note that it is also *inferred* that a vector that is scaled remains as a vector itself. I feel comfortable with these concepts, for now.


<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

You may realize that the explanation of quantum computing has prerequisites of: complex numbers, linear algebra, and abstract algebra. This dependency is also why courses have prerequisites.

A prerequisite course is not just a check box for a learner to "tick", but rather an important assumption that the learner already has most, if not all, of the concepts needed to *start* learning new concepts.

Obviously, I do not have all the requisite knowledge to understand quantum computing, hence the steps to look up the definitions and explanations of many mentioned concepts. This means the proportion of requisite knowledge already possessed is *inversely* proportional to the need to look up and understand concepts in addition to the core concepts of the actual learning objectives.

Needing to learn the requisite concepts as necessitated can significantly lengthen the learning process. If this were a class, it means a student may not be able to keep up with the pace of a class.

</div>

So getting back to the notation $\ket{0}$ and $\ket{1}$, it is important to note that $0$ and $1$ are not really the values of zero and one as we know it. $0$ and $1$ are just symbols, where the definition of $\ket{0}$ is $\pmatrix{1 \\ 0}$, and likewise for $\ket{1}$. I get this part because I have taken a class in abstract algebra and also from the description mentioning that $\ket{0}$ is a shorthand (hence a definition) of $\pmatrix{1 \\ 0}$.

Now that I am comfortable with what $\ket{0}$ and $\ket{1}$ are representing, the representation of a qubit state $\ket{\phi}=\alpha \ket{0}+\beta \ket{1}$ essentially means the state of a qubit is a "mixture of 0 and 1". It is important to remember that $\alpha$ and $\beta$ are complex numbers, but the idea of "a mixture of" still applies.

The explanation then adds the following:

> Eq. (1) expresses the fact that the state of the qubit is the two-dimensional complex vector $\pmatrix{\alpha \\ \beta}$. 

Ah, this confirms the earlier fuzzy conclusion that the state of a qubit is a "mixture of zero and one". However, what this new statement adds is another *perspective*. If the zeroness and the oneness each is a continuum, then the state of a qubit is a point in the 2D plane spanned by the two continuums.

As last part of the explanation of what a qubit is, the explanation continues to compare a qubit with a conventional bit (binary digit):

> Unlike a classical bit, the state of a qubit cannot be measured without changing it. Measuring a qubit, whose state given by Eq. (1), will yield the classical value of either zero ($\ket{0}$) with probability $\|\alpha\|^2$ or one ($\ket{1}$) with probability $\|\beta\|^2$. 

When this sentence is encountered, I can recall *some* quantum physics that I have studied in the past. However, I am not relying on those faint memory when reading technical content. Instead, I use the definition provided by the material.

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

A paper may implicitly or explicitly make claims without further explanations or proofs. It is important to practice **critical thinking** to:

* identify such claims, and
* verify, prove, or otherwise validate such claims

This is not so much that a reader should not trust the author, but rather use every opportunity to make connections between concepts. Such connections facilitate the *application* of knowledge, especially in the process of **problem-solving**.

</div>

I also *question* the claim that $\|\alpha\|^2$ is a "probability". A probability is a value between 0 and 1 (inclusively), and it cannot be a complex number. The first hurdle is "how to compute the absolute value of a complex number"? Recall that a complex number has two components, a real component, and an imaginary component. 

To crystalize this question, what is $\|\alpha_r + \alpha_i i\|$?

Instead of guessing it, I am looking this up. After reading a few articles on the absolute value of a complex number, the definition is as follows: $\|x_r + x_i i\|=\sqrt{x_r^2 + x_i^2}$. And a pictorial picture of how $x_r$ and $x_i$ are seen as coordinates of a point on a circle centered at $(0,0)$, and the absolute value is the radius of the circle.

Does this make sense? A real number can be seen as a complex number with a zero for the imaginary component. Ah, this method (radius of a circle) of interpreting absolute value works out for real numbers as special cases of complex numbers. Because the coefficients $x_r$ and $x_i$ of a complex number $x$ are both real numbers, the square root of their squares must be a real number, as well.

Plugging this understanding of "the absolute value of a complex number" in our qubit discussion, $\|\alpha\|^2 = {\sqrt{\alpha_r^2 + \alpha_i^2}}^2 = \alpha_r^2+\alpha_i^2$. This is, indeed, a real number and it can serve as a probability. The same argument applies to $\|\beta\|^2$. The earlier constraint that $\|\alpha\|^2+\|\beta\|^2 = 1$ restricts both terms to a range of 0 to 1, further qualifying each term as being suitable as a probability.

This section concludes with the following sentence:

> Qubit implementations and technologies are a very active area of research that is not the focus of our review, and interested refer is referred to [80] for a survey.

This means the implementation does not affect the definition of a qubit, and therefore is not further discussed. 

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

As you practice **critical thinking** and read teaching material, your mind may generate questions "but how?" and "but why?" because "certain things do not add up." Because most teaching material is linear, the sequencing of the material may mean the answer to those questions can be *way* further down. 

It is important to write down these questions, periodically go through such questions and write down their answers *only if* the answers become available. This is another way to weave connections between concepts, which then helps with **problem-solving** later on.

</div>

At this point, I have some questions. Because a qubit can only be observed to be in $\ket{0}$ or $\ket{1}$ state with the probabilities determined earlier, one single observation is not sufficient to know the actual state (defined by $\alpha$ and $\beta$) of the qubit. Under "normal" conditions, one can observe many times, and approximate the actual $\alpha^2$ (and hence $\beta^2$). In this case, quantum mechanics throws a wrench into the mechanism because it is clearly stated  that "the state of a qubit cannot be measured *without changing it (referring to the state of a qubit)*". In other words, my mind is prompting questions as concepts are being understood.

# Qubit systems (section 1.1.2)

The next section discusses the state of a system of qubits. In the second paragraph, the tensor product is mentioned:

> The joint state of a system of qubits is described using an operation known as the *tensor product*, $\otimes$. Mathematically, taking the tensor product of two states is the same as taking the Kronecker product of their corresponding vectors. 

The concepts of "tensor product" and "Kronecker product" are new to me. Although the paper also illustrates those concepts in the next two sentences, I feel that it is necessary to look up the definitions of these operators.

Wikipedia explains as follows:

> In mathematics, the tensor product $V \otimes W$ of two vector spaces $V$ and $W$ (over the same field) is a vector space to which is associated a bilinear map $V \times W \rightarrow V \otimes W$ that maps a pair $(v,w), v \in V, w \in W$ to an element of $V \otimes W$ denoted $v \otimes w$.

This presents more terms that I am not familiar with. The first one is "field". The first sentence of the explanation of a field is as follows:

> In mathematics, a field is a set on which addition, subtraction, multiplication and division are defined and behave as the corresponding operations on rational and real numbers do.

Because I took a class in abstract algebra a long time ago, I understand this sentence. One unfamiliar (forgotten due to lack of use) term is resolved.

The next term that I need to clarify is "vector space." I *think* that I have a basic understanding that a vector space is a set where each element can be expressed as a weighted sum of the basis (vectors) of that space. However, I am not 100% sure! So I look up the term.

As it turns out, Wikipedia explains a vector space as:

> A vector space is a set whose elements, often called vectors, may be added together and multiplied ("scaled") by numbers called scalars.

Alright, I think I get this, too. I took linear algebra a *very* long time ago, but this is consistent with what I learned in that class.

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px">

Depending on how much requisite knowledge you already possess, you may find that you are far down one branch of a rabbit hole (think more in tree branches for a squirrel!). This can make it difficult to backtrack to the higher-level concept that you were trying to understand.

This is another reason why it is important to take notes and use a structured representation, as you go through teaching material. As suggested earlier, a bullet list makes it easy to visualize the dependencies of concepts and to backtrack "where you left off" earlier.

</div>

Where were we? Right, the definition of "tensor product"! The next term that I am also not familiar with is "bilinear map". Condensed, Wikipedia explains it as follows:

> $B$ is a bilinear map (function) of the vectors spaces $V$, $W$ and $X$ $B: V \times W \rightarrow X$ such that for all $w \in W$, the map $B_w$ $v \mapsto B(v,w)$ is a linear map from $V$ to $X$, and for all $v\in V$, the map $B_v$ $w \mapsto B(v,w)$ is a linear map from $W$ to $X$.

The term "linear map" seems simple, but I am not taking any chances. Looking up the term "linear map", the definition is as follows:

> Let $V$ and $W$ be vector spaces over the same field $K$. A function $f:V \rightarrow W$ is said to be a linear map if for any two vectors $u,v \in V$ and any scalar $c \in K$ the following is true: $F(u+v) = f(u)+f(w)$ and $f(cu)=cf(u)$.

Since I *teach* discrete structures, the notation of a function is well understood. However, note the phrase "over the ... field" is used here again. With respect to a vector space, when "over a field" is mentioned, it specifies what can be used as scalars to multiply vectors with. This answers a *future* question because the definition of "tensor product" also used the same phrase of "over the ... field".

If I were to take notes (which I am because this module is *also* a kind of "note to self"), I would also write down "linear map means addition of the domain and scaling of the domain transfers to equivalent operations in the codomain."

And where were we? Bilinear map! The $\mapsto$ notation is new to me. It is harder to find out what this symbol means. However, it is not impossible. Right-clicking on an equation using this symbol gives me the option to open the equation as its own page, and the title of the PNG is `v \mapsto B(v,w)`. Since I know Wikipedia uses $\LaTeX$ to specify the math notations, I know how to look up `\mapsto`. The first link of this search finds an explanation that $f:V \rightarrow W$ specifies that $f$ is a function using $V$ as a domain and $W$ as a codomain, whereas $v \mapsto w$ specifies that $v \in V$ as an element maps to $w \in W$. In other words, $\rightarrow$ is a notation to specify the domain and codomain of a function, whereas $\mapsto$ specifies which element of the domain maps to which element in the codomain.

Getting back to the explanation of bilinear map, the sentence "for all $w \in W$, the map $B_w$ $w \mapsto B(v,w)$ is a linear map from $W$ to $X$" means that if we look at a specific $w \in W$, and define $B_w(v)=B(v,w)$ (this is just syntax candy!), then $B_w: V \rightarrow X$ is a linear map. This has to be true regardless of which $w \in W$ that we choose. Flipping $W$ and $V$ around is similarly true, hence the name *bi*linear map.

The main question in my mind is "why is a bilinear map important in the definition of tensor product?"

Now we are back to the definition of "tensor product." To utilize what I just learned, I am expanding the definition. Consider $f: V \times W \rightarrow V \otimes W$ as a bilinear map. This means that $\forall w \in W$, if I define $f_w(v)=f(v,w)$, then $f_w: V \rightarrow V \otimes W$ is a linear map. Likewise, $\forall v \in V$, if I define $f_v(w)=f(v,w)$, then $f_v: W \rightarrow V \otimes W$ is also a linear map. This is how I reinforce the knowledge and understanding of prerequisite concepts: to utilize it right away to further explain the depender concept.

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

Though not common, certain people with high levels of curiosity can occasionally overshoot rabbit hole/squirrel tree traversing and start to learn about concepts that are no longer relevant to the learning objectives.

This kind of overshooting is not inherently a problem. In fact, it is beneficial in the long run because it builds even more connections between concepts and make future learning more effective. 

In the context of a class, however, such overshooting endeavors consume time that may be necessary to complete coursework within the allotted duration. The key is to **maintain a balance between curiosity and learning objectives**.

</div>

At this point, we have *overshot* the original motivation to understand tensor product. The vector space of the tensor product is spanned by a set of basis, each basis vector is a product of the contributing vector spaces. In other words, if $V$ is spanned by a set of basis $B_V$, and $W$ is spanned by a set of basis $B_W$, then the basis set of $V \otimes W$ is defined by $(v \in B_V, w \in B_W) \Leftrightarrow (v \otimes w \in B_{V \otimes W})$. Note that the notation $\otimes$ means the outer product of multiplying two vectors (and yes, I had to look that up, too based on the $\LaTeX$ notation of $\otimes$ (`\otimes`). 

The definition of outer product can be defined as follows. Given $v$ is a 1 column by $m$ row vector, and $w$ is a 1 column by $n$ row vector, and we are using 1-oriented indexing ($v_1$ refers to the value of the first row of $v$), then $(v \otimes w)_{i,j} = v_i w_j$. The indexing of a 2D matrix is row major, meaning that given $A$ is a 2D matrix, $A_{i,j}$ refers to row $i$, column $j$.

An *example* is a 3 row by 2 column matrix $A = \begin{pmatrix}a_{1,1} & a_{1,2} \\ a_{2,1} & a_{2,2} \\ a_{3,1} & a_{3,2}\end{pmatrix}$.

Getting back (*again*) to a system of qubits. Recall that the state of a single qubit is represented as $\ket{phi}=\alpha \ket{0} + \beta \ket{1}$. This means that the state of one qubit can be seen as a vector in the vector space spanned by the basis vectors $\ket{0}$ and $\ket{1}$. In a system of multiple qubits, the state of the system can be seen as a vector in the vector space corresponding to the tensor product of the vector space of each qubit in the system. 

This is not clearly written in the quoted paper, but it is inferred. It is crucial to make connections and take notes of such connections that may be missing from the original material.

The original paper continues to explain the following:

> Say we have two single qubit states $\ket{\phi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$ and $\ket{\phi'} = \pmatrix{\alpha ' \\ \beta '}$. Then the full state of a system composed of two independent qubits is given by, $\ket{\phi} \otimes \ket{\phi'} = \pmatrix{\alpha \\ \beta} \otimes \pmatrix{\alpha' \\ \beta'} =  \pmatrix{\alpha \alpha ' \\ \alpha \beta' \\ \beta \alpha' \\ \beta \beta'}$

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

Practicing **critical thinking** as you read teaching material, you may discover that your understanding of a symbol, a definition, or a concept, may differ from what is explicitly stated.

This can be due to many reasons, using the same symbol for different meanings is one of them. As much as people in STEM tend to define a symbol uniquely for each meaning, there are only so many symbols available. 

The key is to *notice* the disagreement between your understanding and what is stated in the teaching material, and to "resolve" the disagreement. 


</div>

Do you see a problem? The outer product is *not* a two by two matrix, instead, it is a one-column by four-rows vector! This makes sense, in a way, because a vector should be one-dimensional. As it turns out, this is why "Kronecker product" was mentioned. After looking up outer products, Wikipedia states:

> The outer product and Kronecker product are closely related; in fact the same symbol is commonly used to denote both operations.

In other words, in the context of computing the tensor product, $\otimes$ denotes the Kronecker product. A Kronecker product is a flattened outer product where rows are traversed one by one. This explains the tensor product $\ket{\phi} \otimes \ket{\phi'}$ quoted earlier.

This is an example of how I check for consistency of my understanding of the concepts. When there is a difference, I immediately look into it! This (initial) confusion would not have happened if I looked up the definition of "Kronecker product" earlier, but since I was doing a "depth-first search" of concepts, the definition of "Kronecker product" would have been looked up later. 

In the last part of this section, a simplification notation is introduced so that $\ket{\gamma_1 \gamma_2 \gamma_3} = \ket{\gamma_1} \otimes \ket{\gamma_2} \otimes \ket{\gamma_3}$. 

# Pausing for some reflection

Understanding the definitions (and lots of them) is one aspect of understanding concepts, but making connections between the concept is another. In other words, if formal definitions are pine needles, it is important to step back and look at the general shape of the tree once in a while.

It helps to compare the concepts being learned to concepts that I am already familiar with. A bit has two states, 0 or 1. A qubit, on the other hand, has an infinite number of states because the state of a qubit, $\ket{phi}$ is described by the complex coefficients of two basis vectors, $\ket{0}$ and $\ket{1}$. Due to the constraints placed on the coefficients (scalars) $\ket{\phi}=\alpha \ket{0} + \beta \ket{1}, \|\alpha\|^2+\|\beta\|^2=1$, $\alpha$ and $\beta$ are not independent variables if one is known the other one can be derived. For all practical purposes, if we are only examining one qubit, $\alpha$ (the scalar of $\ket{0}$) is sufficient to describe its state.

However, $\alpha$ is not a binary digit. $\alpha$ is a complex number, and it can be seen as a real number two-tuple. As such, unless extra constraints are placed on $\alpha$, $\alpha$ alone can encode "more information" than a single binary digit. Think of a qubit as the hand of a clock, it is "continuous" 

# Superposition and entanglement (section 1.1.3)

In this section, the first definition is as follows:

> The orthonormal basis formed by the $2^n$ bit-string states is called the computational basis.

In this definition, each individual basis vector set is $B=(\ket{0}, \ket{1})$, and the new space is spanned by the members of the $n$th Cartesian product of $B$.

Then something caught my eye:

> But it is possible for three qubits to be in a state that cannot be written as the tensor product of three single qubit states. An example of such a state is, $\ket{\psi} = \frac{1}{\sqrt{2}}(\|\ket{000}+\ket{111})$.

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

Keep in mind that authors of any teaching material are probably experts. This means the material may trivialize the importance of a claim or the proof thereof. As a learner, taking such claims without proof may *seem* to be a good use of time, but this kind of practice is missing out on golden opportunities to **practice, problem-solve, and gain a deeper understanding** of the material.

Many learners express "We need exercises", referring to canned exercise questions typically located after a section or chapter in a book. These exercise questions often help to verify a learner has specific knowledge of the material or the know-how of a "mechanical" process (of repeating the same steps to different configurations). However, almost any teaching material has some hidden *gems* of exercise opportunities.

These gems are presented in the form of a claim that is not proven or otherwise validated, such as "an example of ... is ..." *Completing the proof or validating* such examples or claims can help in many ways:

* to exercise **problem solving** skills with prerequisite material
* build connections between concepts
* build confidence of possessing a deep understanding of the material

Unlike the explicit (with a neon sign) exercise questions at the end of a section or chapter, these gems often disguise themselves as trivial statements that flow naturally with the teaching material, almost as a FYI (for your information) side note. 

Spotting and hunting down these elusive gems is, by itself, an exercise of **critical thinking**. After reading a statement that explicitly or implicitly makes a claim, ask the following questions:

* What learned concepts relate to this exercise?
* How do I use learned concepts to complete this proof?
* Can I prove or validate this logically in steps that are logically connected?


</div>

Instead of just taking this statement for granted, I need to know why that is the case.

First, by definition, since $\psi$ is a sequence of three qubits, we can use the earlier definitions and say that $ \ket{\psi} = \ket{\gamma_1} \otimes \ket{\gamma_2} \otimes \ket{\gamma_3}$. Assuming $\ket{\gamma_i}=\pmatrix{\alpha_i \\ \beta_i}$, 

$\begin{eqnarray} \ket{\psi} & = & \alpha_1 \alpha_2 \alpha_3 \ket{000} + \\ & & \alpha_1 \alpha_2 \beta_3 \ket{001} + \\ & & \alpha_1 \beta_2 \alpha_3 \ket{010} + \\ & & \alpha_1 \beta_2 \beta_3 \ket{011} + \\ & & \beta_1 \alpha_2 \alpha_3 \ket{100} + \\ & &  \beta_1 \alpha_2 \beta_3 \ket{101} + \\ & & \beta_1 \beta_2 \alpha_3 \ket{110} +  \\ & & \beta_1 \beta_2 \beta_3 \ket{111}\end{eqnarray}$ 

This part is just using the definitions and expand the system state of three qubits.

As we can see, the scalar of $\ket{000}$ is $\alpha_1 \alpha_2 \alpha_3 = \frac{1}{\sqrt{2}}$, and the scalar of $\ket{111}$ is $\beta_1 \beta_2 \beta_3 = \frac{1}{\sqrt{2}}$. However, the corresponding scalars of all the other basis vectors are zeroes. Not being very familiar with complex multiplication, one can easily see how this is impossible if $\alpha_i$ and $\beta_i$ are real numbers.

Since we know $\alpha_i$ and $\beta_i$ are complex numbers, then is this scenario possible? Looking up complex multiplication: 

$\begin{eqnarray}(v+wi)(x+yi) & = & vx+vyi+wxi+wyi^2 \\ & = &(vx-wy)+(vy+wx)i\end{eqnarray}$

A complex number is non-zero if at least one component is non-zero. In order for $vy+wx=0$, at least one of $v,y$ is zero, and at least one of $w,x$ is zero. However, $v,w$ cannot both be zero, and $x,y$ cannot be both zero because $v+wi$ is non-zero and $x+yi$ is non-zero. This means we can choose $v,w$ be zero for one case, and $w,y$ be zero for the other case.

In case $v,x$ are zero, then $w,y$ are both non-zero. This means real part of the complex number is non-zero, and the complex number is non-zero.

In case $w,y$ are zero, then $v,x$ are both non-zero. This means the real part is once again non-zero. 

The exercise to make the real part of the product zero also makes the imaginary part of the complex product non-zero.

In other words, in order to make the product of two complex numbers zero, at least one of the two complex numbers must be zero.

But in this scenario, we already know that none of $\alpha_1, \alpha_2, \alpha_3$ is zero, and the same applies to the $\beta$s. This is why it is impossible to have the scalars of basis vectors other than $\ket{000}$ and $\ket{111}$ be non-zero.

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

Understanding definitions and knowing how to derive proofs is one aspect of learning, but finding the "meaning" of a concept is equally, if not more, important.

Where symbols and definitions define a part of the language that allows individuals exchange ideas and concepts, "meaning" is the interconnection of concepts within the cognition of an individual.

A proof is an external process to utilize analytical skills, logical thinking and critical thinking to mechanically show the *objective* connections between statements. A proof (or validation) *is important* because it relates to the *truthfulness* of statements. 

A "meaning" relates the mechanical and abstract to "what matters", or "why something is important", or "how this applies to..." 

</div>

Now that we have proven that it is possible for a system state that is *not* the tensor product of the individual qubits of the system, __what does it mean__?

The text continues to explain as follows:

> States of a system of which cannot be expressed as a tensor product of states of its individual subsystems (qubits) are called *entangled states*. ... The existence of entangled states is a physical fact that has important consequences for quantum computing, and quantum information processing in general. In fact, without the existence of such states quantum computers would be no more powerful than their classical counterparts. 

Okay, so *this* is why quantum computing is more powerful. Then the last sentence of this section concludes as follows:

> Entanglement makes it possible to create a complete $2^n$ dimensional complex vector space to do our computations in, using just $n$ physical qubits.

One way to read this sentence is "cool, so quantum computers are more powerful than conventional computers." However, What exactly is stated by this last sentence?

In the case of a conventional computer of $n$ bits, there are exactly $2^n$ states, and the system state is described as a tuple of all the individual bits. In other words, there is no system state that cannot be described by a concatenation of the component bits.

A quantum computer, on the other hand, has a system *state space* that has $2^n$ dimensions. Within this space, some portion can be described by the tensor product (a fancy way to concatenate) the component qubits. However, there is also a portion that *cannot* be described by the tensor product of individual qubits. In other words, the system state of a quantum computer is vaster than that of a conventional computer.

However, this conclusion also begs the question "but how?" Section 1.1.3 does not exactly explain it, but it started with mentioning the word "superposition." At this point, I am *suspecting* the observable system state is a sum (superposition) of many tensor products of individual qubits. But this means the qubits can be simultaneous and synchronously (with each other) be in different states. The "synchronously" part suggest a connection with "entanglement". This is all speculation based on what I understand so far, and it is important to differentiate this as a "speculation" and not an actual "understanding."

But this speculation also explains why a system of qubits is much more powerful than a system of conventional bits. A system of qubits can be in many states at the same time, whereas a system of conventional bits can only be in one state at any time.

# Inner and output products (1.1.4)

<div style="position: static; float: right; border: thin solid; width: 40%; padding: 10px 10px 10px 10px" markdown="1">

By now, the reader probably recognizes that "understanding" does not come easily nor quickly. How quantum computing relate to this author is probably about the same as how a class relates to a student who has fulfilled the prerequisite (and occasionally co-requisite) requirements.

One key factor to consider is to allocate sufficient time as well as finding an suitable environment to go through all the processes related to understanding technical material in a deep way.

The number of "units" of a class is a mere suggestion. One semester unit means 18 lecture hours and 36 out-of-lecture hours to complete homework assignment and to study. In other words, one semester lecture unit suggests a total of 54 hours of focused concentration and active participation. **A "typical" 3 semester lecture unit class suggests the allocation of 162 hours.**

A full-time enrollment is 12 units, and that translates to 648 hours. Assuming a semester has 16 weeks, this roughly translates to 40 hours per week, which is exactly why 12 units is the magic number of units of a full-time student.

</div>

This section introduces more notations. The first significant sentence is as follows:

> First of these (algebraic notions) is the *inner product* or *overlap* between two quantum states.

Right here, I have some questions in my mind. Exactly what is an inner product? And in quantum physics, what is the overlap between two quantum states. I would have written these questions down for this section if this was a class and make sure that I eventually get these concepts clarified.

The next significant sentence is as follows:

> The overlap between these two states is denoted in the ket notation as $\braket{\psi\|\phi} = \gamma^* \alpha + \delta^* \beta$ ($\ket{\phi}=\alpha \ket{0} + \beta\ket{1}, \ket{\psi}=\gamma \ket{0}+ \delta \ket{1}$) where $^*$ denotes the complex conjugate.

The concept that was not explicitly explained here is "complex conjugate." [Wikipedia](https://en.wikipedia.org/wiki/Complex_conjugate) uses a different notation (of overbar), but states that the conjugate of $a+bi$ is $a-bi$. [Wolfram MathWorld](https://mathworld.wolfram.com/ComplexConjugate.html) also confirms this and that both $\bar{z}$ and $z^*$ can be used to represent the conjugate of a complex number $z$.

Note that looking up the definition of "complex conjugate" and confirming the notation is important before continuing with the article. This is because although "conjugate" *is* an English word meaning "different form", there are many ways to think of a "different form" for a complex number. Furthermore, if one source mentions $\bar{z}$ means the conjugate of $z$, it is important to confirm that $z^*$ also represents the conjugate of $z$ to eliminate any potential misunderstanding.

But wait, we are not quite ready to move on, yet. This is because $\braket{\psi \| \phi}=\gamma^* \alpha + \delta^* \beta$ is not a definition, but the consequence of the notation representing the *inner product* of $\psi$ and $\phi$. At this point, it is crucial to look up the definition of inner product.

[Wikipedia](https://en.wikipedia.org/wiki/Inner_product_space#Complex_coordinate_space) defines the inner product on a complex space as $\braket{x,y}=y^\dagger \mathbf{M}x$, where $\mathbf{M}$ is any Hermitian positive-definite matrix. The first question is whether $\braket{x,y} = \braket{x\|y}$ as an alternative notation. The second question is "what is a Hermitian positive-definite matrix?"

The answer to the first question turns out not to be trivial. [A PDF from Clark University](https://mathcs.clarku.edu/~ma130/inner2.pdf) defines $\braket{v\|w} = \sum_{k=1}^{n}v_k\bar{w_k}$ where $v=(v_1,\dots v_n)$ and $w=(w_1, \dots w_n)$. 

This means that $\braket{x,y}$ is related to $\braket{x\|y}$, but they are not the same. [Looking up Hermitian matrix](https://en.wikipedia.org/wiki/Hermitian_matrix), the simplest definition is "a complex square matrix that is equal to its own conjugate transpose." Because $1=1+0i=1-0i=\bar{1}$, the identity matrix is, indeed Hermitian. Furthermore, $1$ is an identity with respect to multiplication for complex numbers because $(x+yi)(1)=x1+yi1=(x+yi)$. In other words, the identity matrix for real vectors also works for complex vectors.

*So*, $\braket{x\|y}$ is a special case of $\braket{x,y}$ where $\mathrm{M}$ is the identity matrix. This clarification is important because now we understand all the properties of $\braket{x,y}$ also apply to $\braket{x\|y}$.

Now we are ready to continue. The article then claims the following:

> Notice that $\braket{\psi \| \phi} = \braket{\phi \| \psi}^*$. 

Although generally speaking we can trust the author(s), it is a good exercise to prove this claim. Using the same definitions of $\ket{\phi}$ and $\ket{\psi}$ from before, 

$\begin{eqnarray}\braket{\psi\|\phi} & = & \gamma^* \alpha + \delta^* \beta \\ & = & \gamma_r * \alpha_r + \\ & & (-\gamma_i \alpha_r + \gamma_r \alpha_i)i + \\ & &  \gamma_i \alpha_i + \\ & & \delta_r \beta_r + \\ & & (-\delta_i \beta + \delta_r \beta_i)i + \\ & & \delta_i \beta_i \\ & = & \gamma_r \alpha_r + \gamma_i \alpha_i + \delta_r \beta_r + \delta_i \beta_i + \\ & &  (-\gamma_i \alpha_r + \gamma_r \alpha_i - \delta_i \beta_r + \delta_r \beta_i)i\end{eqnarray}$ 

where subscript-i means the imaginary coefficient and subscript-r means the real coefficient of a complex number. 

By definition, 

$\begin{eqnarray}(\braket{\phi\|\psi})^* & = & (\alpha^* \gamma + \beta^* \delta)^* \\ & = & ((\alpha_r \gamma_r + \alpha_i \gamma_i + \beta_r \delta_r + \beta_i \delta_i)+ \\ & & (\alpha_r \gamma_i - \alpha_i \gamma_r + \beta_r \delta_i - \beta_i \delta_r)i)^* \\ & = & (\alpha_r \gamma_r + \alpha_i \gamma_i + \beta_r \delta_r + \beta_i \delta_i) + \\ & &  (-\alpha_r \gamma_i + \alpha_i \gamma_r - \beta_r \delta_i + \beta_i \delta_r)i\end{eqnarray}$ 

Using the commutative law of multiplication, we can then establish $\braket{\psi\|\phi} = \braket{\phi\|\psi}^*$

This step may seem like a waste of time because the paper already claims the equality. There are two reasons to take on these steps. The first one is to verify that the claim is, indeed true, *just in case* the authors had a mistake. A more important reason, however, is to *practice* proof techniques, and in doing so, exercise the use of the definitions mentioned and understood up to this point. In other words, this is a built-in exercise to help strengthen the understanding of the concepts, *but only if the reader chooses to do so.* 


# A bit of non-technical discussion

## "I am drowning in unfamiliar terms and symbols"

It is important that psychology plays an important part in this whole process of "understanding." The first one is to take care of the anxiety/fear when we first encounter terms, symbols, and definitions that we are not (yet) familiar with. 

There are several factors contributing to the anxiety and/or fear when we encounter something new that we do not understand. The first one is "I fear I cannot understand this." The key to resolve this fear is to learn an effective approach to understand new concepts. This will be addressed later.

If one imagines learning a collection of new concepts as achieving a certain altitude (height), the initial fear is looking at the height and thinking that the approach is to scale a cliff without safety equipment. More often than not, upon closer inspection, there is a staircase with safety rails and benches to rest along the way. It will take some effort, but it can be achieved.

## "But I don't have time to spend on this (understanding)"

This factor is a matter of preferences, priority, and choice. In order to succeed in a STEM field, it is crucial to possess an inherent interest, and *choose* to invest time and energy upfront to understand concepts thoroughly. 

It is only after this fear/anxiety is quelled that we can *be patient*. If we encounter a term that we do not understand for sure, look it up! And do this "recursively." This means while looking at the explanation or definition of a concept, you may realize that you need to first look up and understand a more fundamental concept, and this can nest many levels.

As such, taking notes is important. This is not only referring to taking notes in a lecture or during class but also to taking notes when you are drilling down the nested structure of concepts and definitions.

## Finding excuses to apply what is learned

Instead of just accepting the claims, apply the more fundamental learned concepts to *validate* and *verify* the depender concepts. Do not take "This means..." for granted, ask why, and ask how you can prove it. 

## "But I am not smart enough"

Deep understanding of concepts has more to do with preferences and priorities than intelligence. As an example of understanding a new concept, my own experience of learning about quantum computing is anything but "quick." However, I kept at it, and I did not gloss over details or choose to accept statements as is. The "preference" to drill down to a solid understanding of dependee concepts is what enables a person to understand concepts in a deeper way.


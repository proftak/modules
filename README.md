# modules

First of all, all the content pages, including this one, are supposed to be [rendered by Jekyll](https://auyeunt.github.io/modules). If the URL on your browser is `https://github.com/...`, click the link in the previous sentence!

This is a `GitHub` repository that hosts Prof. Tak's instructional content. The majority of the content is located at [his site](http://dtkb.org/~auyeunt/teaches/modules). However, some newer content is being developed here. Some older content is being converted into GitHub Markdown format.

The [directory](directory.md) is automatically regenerated whenever there is an update to the module files. For the [GitHub workflow to work](https://docs.github.com/en/actions/using-workflows), the heading of a module should follow this template:

```markdown
---
title: "Module 0000: Whatever"
---
# _{{ page.title }}
```

Also, for the GitHub workflow to work, [the GitHub bot should have read/write permissions](https://github.com/marketplace/actions/github-push).

# Fork, contribute and pull request

If you see an issue, you can fork the file(s), make your edits, and then submit a pull request to merge your contribution to the main branch.

# Tricks, Tips and Caveats

## Jekyll-imposed issues

### Set element delimiters

`{` and `}` in an equation are normally specified as `\{` and `\}` in an equation environment. However, the GitHub equation rendering mechanism requires two backslashes.

```markdown
$\{a,b,c\}$ is a set
```

is rendered as "$\{a,b,c\}$ is a set".

However,

```markdown
$\\{a,b,c\\}$ is a set
```

is rendered as "$\\{a,b,c\\}$ is a set".

Using the built-in editor of `github.com`, the following find-and-replace configuration will change `\{` and `\}` to `\\{` and `\\}`:

* Search for `(?:[^\\])(\\[\{\}])`
* Replace with `\\$1`

Note that equation blocks that are standalone (using `$$` to start and end the equation) do not need to escape the backslash. 

```markdown
$$\{a,b,c\}$$

is a set
```
is rendered as follows:

---

$$\{a,b,c\}$$

is a set

---

### No Markdown in HTML elements by default

Markdown content that is nested in HTML content is not rendered. 

```html
<div>
Isn't this **bold**?
</div>
```

is rendered as

<p>
Isn't this **bold**?
</p>

This limitation can be overcome by specifying the nested text is in Markdown.

```html
<p markdown="1">
Isn't this **bold**?
</p>
```

is rendered as follows:

<p markdown="1">
Isn't this **bold**?
</p>


### Set delimiters inside HTML elements

`{` and `}` are rendered correctly with a single backslash in equations inside HTML elements.

```HTML
<div>
$\{a,b,c\}$
</div>
```

is rendered as 

<div>
$\{a,b,c\}$
</div>

|equation|description|
|-|-|
|$E=mc^2$|Einstein's mass-energy equation|

### Verticle bars in equations

Jekyll incorrectly prioritizes the detection of tables over equations. Observe the following $\LaTeX$ code:

```latex
$|a|=(a<0)?-a:a$
```

It is rendered as follows:

$|a|=(a<0)?-a:a$

In order to fix this problem, escape the vertical bar with a backslash. The code becomes the follows.

```latex
$\|a\|=(a<0)?-a:a$
```

It is rendered as follows:

$\|a\|=(a<0)?-a:a$

### Underscores in equations

This is yet another Jekyll issue. Because Jekyll prioritizes looking for pairs of underscores (to italicize), it "eats" up pairs of underscores even in equations. This only happens in some very specific situations when an underscore is right after a close brace.

```latex
${m}_i=m_{i-1}$
```

is rendered incorrectly as follows:

${m}_i=m_{i-1}$

However, if the underscores are escaped, then it works:

```latex
${m}\_i=m\_{i-1}$
```

is rendered as follows:

${m}\_i=m\_{i-1}$


## ChatGPT prompts

### AI-generated questions

First, select the content of a module. It is best to use the editor to copy and paste the raw Markdown content so that the equations are properly captured.

In ChatGPT, use the following initial prompt: 

> Please read the following content about *the module title or a more detailed description.* I will ask some questions in the following prompts.
> *Shift-ENTER to enter 2 empty lines.*
> *Copy and paste content*

To ask for questions and answers, the following prompt generates HTML code that can be viewed in a browser:

> Generate 10 questions with answers so I can check my understanding of this material as well as the application of the concepts. Please format the questions and answers using HTML details and summary elements. Use the dollar sign "$" to begin and end equations.

The ChatGPT web interface does not appear to be able to render HTML `details` and `summary` elements.

---
title: "Module 0408: What's up with GitHub and Open Educational Resources?"
---

[GitHub](https://github.com) is a web-based repository for all kinds of projects. One of the original purposes of `GitHub` is for coding. However, it is also well suited to any text-based content. If OER (open educational resources) is created in a text-based format, `GitHub` is, potentially, a great place to host the content.

# Getting Started

1.  Go to [GitHub](https://github.com) and sign up for an account or sign in if you already have an account.
2.  Click "New"

That's it! Well, not really. Let us go over the concepts involved.

The term "repository" refers to a resource where:

* It can host a variety of files and folders. In a sense, a repository is similar to a file system.
* The content stored in a repository is revision-controlled.

What does "revision-controlled" mean? It means a lot of things, including the following:

* Changes are tracked. A file can be reverted to an earlier version.
* The current state of a file can be compared to an earlier version to see the differences.
* A repository can be "cloned." This means another party, if permitted, can duplicate all the files of a repository.
* Multiple parties can simultaneously make changes to even the same files as long as the changes are not conflicting.
* A version can be "forked." This creates multiple versions of the repository so that the changes made to each branch stay independent from each other.
* Branches of a repository can be "merged", meaning that the changes converge to a single branch.

In addition to providing a web-based method to manage repositories, `GitHub` also offers additional resources. For example, the "Issues" tab of a repository allows others to leave comments. This facilitates a great mechanism for readers/learners to provide feedback. However, "issues" is accessible only to signed-in `GitHub` users. Considering `GitHub` is free, this should not deter a reader/learner from signing up and then reporting issues.

If the readership of an OER item is tech-savvy enough, each reader/learner can "fork" the repository, make a suggested change, and then place a "pull request" to update the main branch of the repository where all browsers see. This is a great method for readers and others to contribute and improve the content of a repository.

## Granularity of a repository

There are no hard-and-fast rules. If the granularity is too fine, then the author ends up with many repositories. This can make projects difficult to maintain. On the other hand, if the granularity is too coarse, then it is difficult for another person to make only one change to a small part of the project. 

At the end of the day, text files are relatively small. If the OER is in book form, then it makes sense that each book has a repository. However, if the OER is in smaller independent modules, then a single repository to host all the modules makes sense.

## Naming of a repository

For others to quickly locate content, it is best not to make the name of a repository too complex. The URL to a single file of a repository contains the author's account name as well as the name of the repository. Therefore, there is no need to duplicate these components in the name of a file in a repository.

# Learn Markdown!

[Markdown](https://www.markdownguide.org) is essentially a simple, text-only, and intuitive mark **up** language. Compared to HTML (hypertext markup language), Markdown is much easier to type, less prone to syntax issues, and far more effective as a language to create text (and beyond!) content.

Markdown has many features that make it suitable for text-based content in many domains. For example, it can handle equations like $E=mc^2$. It can also be used to generate simple graphs like the following:

```mermaid
flowchart LR
id1[Node 1]
id2[Node 2]
id1 --> id2
```

MarkDown can also syntax highlight code blocks:

```c
int main()
{
  return 0;
}
```

Because Markdown is a text-only markup language, any text editor can edit content! `GitHub` has a decent in-browser editor. It does not have all the fancy spell-check and grammar-check features, however. That being said, it is fairly easy to copy and paste text-only content between fancy desktop editors and the web interface.

Each section is automatically an anchor that a URL can reference. However, you can also additional <a href="#customsanchor">custom anchor</a> using a little bit of HTML code. The special anchor uses the HTML code `<a href="#customanchor">custom anchor</a>`.

You can also have multiline derivations:

$$
\begin{align}
&x+x+x\\ 
=& 2x+x\\ 
=& 3x
\end{align}$$

You can also easily add "special visual sections" in the flow of the main text.

---

> [!NOTE]
> Salt dissolves faster in hot water.

---

> [!WARNING]
> This is a warning.

---

> [!TIP]
> Use a microwave oven to quickly heat up water.

---

> [!CAUTION]
> The water is hot!

---

> [!IMPORTANT]
> Don't pour hot water on yourself!

---

# Other fancy but easy features

## Flashcards

You can use the `<detail>` element in HTML. Let's take a look at the following Markdown/HTML code:

```html
<details>
  <summary>Energy equation</summary>
  $E=mc^2$
</details>
```

It is rendered, using GitHub's web interface, as follows:

<details>
  <summary>Energy equation</summary>
  $E=mc^2$
</details>

# To contribute

There are multiple ways to contribute and/or utilize GitHub-hosted OER content.

## Sign up for a GitHub account

First, go to [GitHub](https://github.com), click "Sign up" (upper right corner) and create a GitHub account. This step is necessary for all the methods to contribute to the project. 

## Reporting an issue

An issue usually refers to a software bug for most GitHub repositories. However, in the context of OER, an issue can be a typo, mistake, inaccuracy, or other items that need to be fixed. Users with a "contributor" role of a GitHub repository can, then, investigate and potentially resolve the issue. When an issue is resolved, it will be marked as such, and the user who originates the issue will be notified. 

1.  Go to any file of the project where an issue is to be reported.
2.  Sign in to GitHub.
3.  Click "Issues"
4.  Click "New Issue"
5.  Fill in the title and description
    * Please be clear about which document is in question. The best way is to include either a "path" or the full URL to the document in question.
    * The description of the issue also needs clarity.   
7.  Click "Submit new issue"

## Discussions

A discussion differentiates from an issue because a discussion does not reflect something to be fixed. GitHub provides 5 built-in categories of discussions. In the context of OER, this is how each category can be utilized:

* **General**: just chatting. Do not expect OER developers to check these discussions regularly.
* **Ideas**: suggestions of new OER content, or extensions to current OER content.
* **Polls**: this can be used to decide whether an idea should make it to the "Ideas" category. An OER developer may originate a poll to gauge whether a project is worth doing.
* **Q&A**: this category is special because it allows other users to answer specific questions.
* **Show and tell**: this category can be utilized in at least two ways. An OER developer may use this to announce new content or significant updates to existing content. However, a user can also showcase how the OER content is utilized in classes or other settings.

Discussions are a great way to contribute to an OER project by talking to the developers and other users of the OER content. Any user can participate.

## Forking

Users who are comfortable with Markdown can use the edit (writing instrument icon) tool to change the OER content. Any user can fork a public GitHub repository. A fork creates a new branch in the repository, and there can be many revisions and even further forks along this branch.

After each revision, click "Commit Change" so that the revision is tracked *along the forked branch*. This means the revision does not make it to the `MAIN` branch for everyone to see. While changes are being made to a forked branch, the `MAIN` branch can also have its own revisions.

### Forking with the intention to merge

A forked branch can remain forked forever. Typically, however, a forked branch is *merged* with the main branch once the changes are finalized. This allows the contribution to be shared with the general user base.

When a forked branch is ready to be merged to the `MAIN` branch, click "Create pull request". This notifies the owner of a repository about the availability of a forked branch to be merged. In a "pull request," be descriptive of what the fork is about.

Fork/pull is better than using "Issues." Fork/pull only needs the manager of the repository to *verify* the changes before merging to the `MAIN` branch. This is the most effective way to contribute to OER content. However, unlike the previous approaches, fork/pull does require the contributor to be comfortable editing content in Markdown (or whatever the source language is).

### Forking permanently

A learner may want to create a fork permanently to incorporate the learner's own notes and annotations. At the same time, the learner may also want to get the latest updates to the original document. This can be done entirely using the GitHub web interface.

* The learner creates the initial fork.
* The learner updates this forked branch with annotations and notes.
* When the main branch is updated, the learner uses "Sync fork" to incorporate non-conflicting updates from the main branch.

## Cloning (importing)

A forked branch is still a part of the original repository. Cloning allows an entire repository to be cloned and has an entirely different team of managers and contributors. 

Any GitHub user can import another public repository. To do this, click the `+` drop-down next to the search bar, then click "Import repository." Copy and paste the URL of the source repository, and fill in the rest of the form.

* Note the URL is not the viewing URL. To get the URL for importing from the web interface of a GitHub project, navigate to the top level of a repository, then click `<> Code`, and then copy the HTTPS. For example, the URL of the repository containing this document is `https://github.com/proftak/modules.git`.

Clone/import is the *ultimate* expression of "open" in OER. Like the content, but not so much the management of the content? Clone it and manage it yourself!
* If a repository is public, you should not need to specify `username` or `access token`.
* The clone of an OER project should remain public!

Cloning/importing differentiates from fork/pull because a new repository is created out of the original, and the new repository can belong to a different GitHub user. 



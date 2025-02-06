---
title: "Module 0433: Fust: a framework to integrate Creative Commons, Open Educational Resources, and GitHub"
---

# How the components connect

## Open Educational Resource (OER)

OER refers to books, articles, activities, etc. that are "open" and for educational purposes. "Open" has multiple meanings. The most essential element of "open" is "free of charge." Unlike materials that are paid for by a college and therefore free of charge to students, OER is free of charge to be redistributed. 

There are some nuances regarding how "open" is "open". For example, some OER content is free-of-charge to be redistributed, but not open to be modified. Some OER material is open for any type of redistribution and even incorporation into commercial products, others have restrictions. This is where Creative Commons licenses become important.

## Creative Commons (CC)

CC is both the name of an organization and also the licenses that it creates. There are several CC licenses. For the purpose of this module, we will focus on licenses that do not include "No Derivatives" (ND) as a part of the CC license. This is because `GitHub` is a mechanism that benefits OER and is intended to be remixed and derived.

## `GitHub`

`GitHub` is a cloud resource that integrates the use of `git` at the core. `git` is the name of a revision control tool that is commonly used by (software) developers to keep track of changes and also to facilitate expansive teamwork.

While there are many other platforms to author, publish, and adopt OER, `GitHub` is unique in some ways. In the context of OER, `git` (as a tool) offers the following:

* "Clone": duplicate an OER project.
* "Fork": revise an OER project with possibilities to integrate the changes back into the project, or to split it as a new project.
* "Pull": if the original project is called the "parent", and a forked project is the "child", this allows revisions to propagate from the parent to the child.

"Pull" is a feature unique to `git`, by extension, `GitHub`.

## Putting everything together

For the purposes of this work, the `GitHub` repository that publishes this work is called Fust (pronounced fOOst), in honor of the financier who did not invent the printing press, but financed Gutenberg (the inventor) and later operated the first printing firm.

# Licensing

The strength of `GitHub` is the ease of spinning off an OER project. As such, while `GitHub` is also useful for OERs that have ND in their CC licenses, OERs that are CC licensed without ND benefit even more from the `git` mechanisms.

For `GitHub` to publish content, some customization is needed. Such customization has coding involved and is therefore licensed separately. In other words, any OER developer who chooses to use Fust can specify different licenses for the *content* while maintaining the licensing of Fust.

# On the technical side

`GitHub` supports Markdown (MD) as a markup language. MD is a fairly rich markup language that can fall back to HTML when necessary. However, even by itself, it supports normal text formatting, equations, drawing various types of diagrams, formatting tables, etc. Compared to HTML, MD is easier to learn and type even with a plain-text editor like `notepad` in Windows. Many open-source and free previewing editors can render MD side-by-side with the MD document. 

However, the *implementation* of MD rendering at `GitHub` has many inconsistencies and issues. Many of these inconsistencies are discovered and managed in the OER project that hosts this page. The architecture of this OER project is as follows:

* The content is hosted by `github.com`. All the MD and associated graphics files are parts of a `GitHub` repository.
* Content is organized as "modules." Each module has its folder to contain the MD file and potentially additional media files that the MD file references.
* The content is processed and published by `github.io`. There is a delay in the update of the source material and the actual publication of the content. This lag depends on many factors, including the amount of content in a project.

While `GitHub` can natively do this, this OER project includes the configuration and customization necessary to render MD as correctly as possible. Please note that the "preview" of the editor does not render some MD code correctly, especially those involving equations, diagrams (using `Mermade`), and HTML/Javascript for rendering purposes.

For content quality assurance, the following steps are suggested. Assume `username` is the user name of the repository, and `reponame` is the name of the repository, and `moduleNum` is the 4-digit number of the module:

* Go to `https://github.com/username/reponame/actions` and check to make sure all workflow runs are completed, each with a check in a green circle. If a workflow is in progress (a turning yellow circle), wait for it to complete.
* Go to `https://username.github.io/reponame/moduleNum/mdModule.html` to check the content.

In order to circumvent issues related to static and out-of-date Markdown rendering, the configuration of this repository relies on client-side (browser side) Javascript rendering.

# Getting started

## Setting up an account

To get started, an OER developer first registers with [GitHub](https://github.com) for a free account using the "Sign up" button. On the last page of the registration process, it is best to identify as a "Teacher." In order to finish the registration as a teacher, you will need to use a school email address (one that ends with `.edu`).

As for the top 2 things you want to do with GitHub, "Connect with other developers" and "Contribute to Open Source projects" are good choices for an OER project.

Here are the detailed steps:

- [ ] Visit [https://github.com](https://github.com). Click `Sign up` in the upper right corner to register for an account.
- [ ] You can use any email address. However, use the "w1234567@arc.losrios.edu" email to get some additional free benefits for educators.
- [ ] Choose a password that is difficult to guess.
- [ ] Think of a username.
- [ ] Check your email for the launch code and enter it.
- [ ] Sign in.
- [ ] Answer a few questions. (There are more questions if you sign up as a teacher; you must upload a picture of your ID.)

## Cloning the project

Go to the [home page](https://github.com) after you sign in. Click ["Import repository"](https://github.com/new/import). You will need to fill in the details of the repository.

- [ ] "The URL for your *source* repository:" This is the URL of the repository from which to clone. Specify `https://github.com/proftak/modules.git` here.
- [ ] "Your username for your source repository" and "Your access token or password for your source repository": Leave both blank because you are cloning from a public repository, and there is a username or password to specify.
- [ ] Under "Your new repository details", you can use any repository name.
- [ ] You can also mark your project as "Public" or "Private".
  - [ ] If you intend the OER to be ND (no derivatives), choose "Private."

Click "Begin import" to start the process. It may take a few minutes to import the project.

## Configuring GitHub to publish HTML

Once cloned, you need to change a few settings. Click "Settings" when you are viewing the repo. The URL to the repo's main page is `https://github.com/<username>/<reponame>`, replace `<username>` with your GitHub user name, and replace `<reponame>` with the name of the repository.

First, click `Settings` on the top bar, then follow these steps:

- [ ] `Pages`:
  - [ ]  Click `Pages` on the left to specify how the HTML documents are published.
  - [ ] In `Build and deployment`,
    - [ ] Select "Deplay from a branch" for `Source`,
    - [ ] Select "main" and "/root" for `Branch`.
- [ ]  `Code and automation`:
  - [ ] Click `Actions` under `Code and automation`
  - [ ] Click `General`
  - [ ] On the right-hand side, scroll down to `Workflow permissions`
    - [ ] Select the radio button `Read and write permissions`
 
After the content is built, the URL to the published content will be `https://<username>.github.io/<repo>`, replace `<username>` with your GitHub user name, and replace `<repo>` with the name of the repository. Note that the initial publication can take some time!

On the left, click `Actions`, then `General`. Under "Workflow permissions", click "Read and write permissions". Click "Save".

## Cleaning up the content

The repository comes with its own OER content that you probably do not need. To remove the current modules, follow these instructions:

- [ ] First, navigate to the home of your repository at `https://github.com/<username>/<reponame>`
- [ ] To safely remove modules one by one:
  - [ ] Click on a module (a four-digit folder name).
    - [ ] Click the "..." on the right-hand side.
    - [ ] Click "Delete Directory"
    - [ ] Click "Commit changes"
    - [ ] Confirm by clicking "Commit changes" again.
- [ ] To (dangerously!) remove all modules:
  - [ ] First, consider backing up all the files by downloading the repo as a ZIP file!
  - [ ] Click "Actions" on the horizontal menu bar.
  - [ ] On the left pane, under "Actions", "All workflows", click `rmModules` (remove Modules).
  - [ ] Make sure this is what you want to do!
  - [ ] On the right pane, click "Run workflow".
  - [ ] Click "Run workflow" in the pop-up.
  - [ ] There is a lag, then the pop-up will show that the workflow is in progress (turning a yellow circle to the left).

## Writing a new module

To start a new module:

- [ ] Navigate to the home of the repository `https://github.com/<username>/<reponame>`.
- [ ] Note the number of the last module.
- [ ] Depending on the width of your screen, click the `+` button or the button labeled `Add file`.
- [ ] Select "Create new file".
- [ ] In the textbox immediately to the right side of your repository name, type something like `0241/mdModule.md`, and replace `0241` with a number that is after the number of the last module.
- [ ] In the main text area, start with the following content (change the number 0241 and the title "Some module"!).

```markdown
---
title: "Module 0241: Some module"
---
```

The explanation is as follows:

* `---` is the marker to begin and end the YAML (yet another markup language) section.
* In this section, `title: "Module 0241: Some module"` specifies the title of the page. If this is not the format you want to use, some additional customization needs to be done.

Then type the actual content in this document after the YAML section. Remember to to click "Commit changes..." when you are done, or at a point that you want to save the document.

# Customization

## Choice of CC license for the content

If you remove all the modules that came with the repository, you can choose your own content license. To change your content license, modify `_layouts/default.html`. Specifically, locate the line that starts with "This site is licensed under..", then modify the URL to the Creative Commons license and update the symbols.

Note that the licensing of the content is independent of the licensing of the HTML and YAML files that form the framework of the publication mechanism.

# Learners

`GitHub` has mechanisms that benefit learners. Each repository has mechanisms for people to report "issues" as well as to participate in "discussions." Learners or OER collaborators can make use of these two features to officially report problems or to engage in discussions.

However, the feature that has the most potential is the ability to "fork" a repository. Anyone with a `GitHub` account can click on the link "Improve this page by contributing and editing." (at the bottom of this page). `GitHub` then prompts whether the user wants to fork the repository.

A fork is a spinoff, but it is not a clone. A clone is, by default, independent from the source. This means changes of the origin cannot reach a clone, and changes to a clone cannot reach the origin. However, a fork allows revisions to flow in both directions.

For this discussion, it is helpful to introduce the concept of a "branch." Every repository starts with a `main` branch. A branch is a sequence of tracked revisions. The addition of a file is a revision, the editing of a file is a revision, etc. `Fust` publishes only the `main` branch of a repository.

A fork is, as the name implies, a split-off point of a branch. Let us name a forked branch "T" from the `main` branch. After the fork, branch "T" can track its own sequence of revisions, independent of the revisions to the `main` branch. This mechanism is helpful in several use cases:

* A major revision that takes a significant amount of time. During the revision, the `main` branch remains to be the one published. This way, learners do not get affected by the partial updates that may render a document unsuitable for publication.
* A learner may fork a repository for interleaving notes in the source material. This is, in a way, equivalent to making a photocopy of an entire book to mark up the photocopy without affecting what other learners see in the published version.

In the first case, when the revision is completed, it needs to be merged into the `main` branch. In the second case, however, a student may continue to keep a fork permanently without merging it back to the `main` branch.

In the second scenario, what if the OER developers make significant revisions after the learner forked for note-taking purposes? This is where `GitHub` (it is a feature of `git`, the underlying tool) offers a unique feature. The learner can choose to "sync fork" to integrate all changes to the `main` branch of the repository to the forked branch.


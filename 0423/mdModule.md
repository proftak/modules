---
title: "Module 0423: Markdown, GitHub and OER"
---

# Rationale

OER (Open Educational Resources) can replace paid publisher content, but it can also be used to supplement existing text/teaching material. While the "free of charge" aspect of OER is important, the "freedom to change" aspect can be just as important for educators who have diverse student populations and may need more diverse teaching approaches.

Developing and publishing OER content can be a daunting task, more so when there are mathematic symbols and other special formatting needs. $\LaTeX$ has been the standard typesetting language to publish STEM content for decades. However, $\LaTeX$ is not easy to learn, and the publication of $\LaTeX$ content requires specific tools.

`Markdown`, on the other hand, is a simple markup language that remains easy to read in a plain text editor. While `Markdown` does not have all the features and flexibilities of $\LaTeX$, Markdown is compatible with HTML (HyperText Markup Language) and CSS (Cascading Style Sheet). As such, `Markdown` also inherits the ability of page layout control, etc.

There are many options for publishing `Markdown` content because `Markdown` is a widely accepted content format. For example, a Linux virtual server can be configured to publish `Markdown` content. Running and maintaining a server is not practical for many educators. The know-how is one aspect, but more importantly, the maintenance takes up valuable time. It is often better to utilize a platform where there is no need to maintain a Linux environment.

[`GitHub`](https://github.com) is a for-profit cloud resource. At the same time, it offers free hosting of content to individuals. By default, `GitHub` already has the ability to develop/author and publish basic `Markdown` content. For individuals with little formatting needs, this default ability already goes a long way. However, OER developers who need more specific control over the content or require more customization will also find the optional (but free) *publication* mechanism to be highly flexible.

One unique feature of `GitHub` is the underlying `git` utility. Most OER publication platforms allow learners to download and access content. `GitHub` also allows learners to "fork" content in case a learner wants to include notes in the original material. `git` also allows any "upstream" changes to the published material to be incorporated into forked branches. This unique mechanism makes `GitHub` uniquely suitable for OER developers who adopt the [Agile](https://en.wikipedia.org/wiki/Agile_software_development) methodology. The same mechanism also allows and encourages crowd-sourcing if this methodology is appropriate.

# GitHub

GitHub is an online revision control repository (repo) service with a user-friendly web interface. Everything in this module requires a registered account. You can ignore the following steps if you already have a GitHub account.

* [ ] Visit [https://github.com](https://github.com). Click `Sign up` in the upper right corner to register for an account.
* [ ] You can use any email address. However, use the "w1234567@arc.losrios.edu" email to get some additional free benefits for educators.
* [ ] Choose a password that is difficult to guess.
* [ ] Think of a username.
* [ ] Check your email for the launch code and enter it.
* [ ] Sign in.
* [ ] Answer a few questions. (There are more questions if you sign up as a teacher; you must upload a picture of your ID.)

Everything starts with the Dashboard.

# Markdown

Markdown is technically a "markup" language, like HTML. However, unlike HTML, Markdown is visual, even in plain text. Markdown is also much easier to type because it does not rely on HTML elements' open and close tags. Learn more about [how Markdown is used in GitHub](https://docs.github.com/en/get-started/writing-on-github).

Unfortunately, GitHub has multiple inconsistent ways to *render* Markdown in HTML for viewing. While the most basic method will work for most people, getting useful additional features to work while publishing MArkdown content using GitHub can be challenging.

# Cloning from Tak's repo

Tak has learned most of the tricks for publishing HTML content from Markdown source documents! You can clone Tak's repo and save time trying to figure out everything independently. GitHub provides a very convenient method to clone from another repository. 

In the Dashboard, click "Import repository", then specify `https://github.com/proftak/modules` as "the URL for your source repository". You can ignore the credential questions, but name your repository before clicking "Begin import."

It will take some time to finish the cloning. Once completed, click on the new repository. 

# Repo settings

Once cloned, you need to change a few settings. Click "Settings" when you are viewing the repo.

* [ ] `Pages`:
  * [ ]  Click `Pages` on the left to specify how the HTML documents are published.
  * [ ] In `Build and deployment`,
    * [ ] Select "Deplay from a branch" for `Source`,
    * [ ] Select "main" and "/root" for `Branch`.
* [ ]  `Code and automation`
  * [ ] Click `Actions` under `Code and automation`
  * [ ] Click `General`
  * [ ] On the right-hand side, scroll down to `Workflow permissions`
    * [ ] Select the radio button `Read and write permissions`
 
After the content is built, the URL to the published content will be `https://<username>.github.io/<repo>`, replace `<username>` with your GitHub username, and replace `<repo>` with the name of the repository. Note that the initial publication can take some time!

On the left, click `Actions`, then `General`. Under "Workflow permissions", click "Read and write permissions". Click "Save".

# Editing

## Modules

A module is a unit (quantum) of publication. The repo is set up to recognize the title of a module automatically and make a directory. When you clone the repo, it inherits all the published modules. 

### Remove a module

To remove a module, navigate to the directory of the module (usually a number, such as `0279`). Click `...`, then click "Delete directory". You also need to confirm by clicking "Commit changes..." A new dialog box asks for one more confirmation with an optional description.

### Add a module

To add a new module, first navigate to the root of the repo. The URL of the root of the repo is `github.com/<username>/<repo>`.

Click the `+` icon, then "Create a new file".

In the textbox with a description of "Name your file...", type `<module number>/<mdModule.md`. `<module number>` should be replaced by a number that identifies the module. The name of the Markdown file can be `index.md` or any filename with an extension of `md`.

Then, edit the content in the main editing area. Remember to click "Commit changes..." to save the content.

Note that as soon as the content is committed, the "workflow" to publish the committed content will start. 

---
title: "Module 0423: Markdown, GitHub and OER"
---

# GitHub

GitHub is an online revision control repository (repo) service that has a user-friendly web interface. Everything in this module requires a registered account. If you already have a GitHub account, you can ignore the following steps.

1. Visit [https://github.com](https://github.com). Click `Sign up` in the upper right corner to register for an account.
2. You can use any email address. However, use the "w1234567@arc.losrios.edu" email to get some additional benefits that are free to educators.
3. Choose a password that is difficult to guess.
4. Think of a username.
5. Check your email for the launch code and enter it.
6. Sign in.
7. Answer a few questions. (More questions if you sign up as a teacher, you need to upload a picture of your ID.)

Everything starts with the Dashboard.

# Markdown

Markdown is technically a "markup" language, like HTML. However, unlike HTML, Markdown is visual even in plain text. Markdown is also much easier to type because it does not rely on HTML elements' open and close tags. Learn more about [how Markdown is used in GitHub](https://docs.github.com/en/get-started/writing-on-github).

Unfortunately, GitHub has multiple inconsistent ways to *render* Markdown in HTML for viewing. While the most basic method will work for most people, getting useful additional features to work while publishing MArkdown content using GitHub can be challenging.

# Cloning from Tak's repo

Tak has learned most of the tricks for publishing HTML content from Markdown source documents! You can clone Tak's repo and save much time trying to figure out everything on your own. GitHub provides a very convenient method to clone from another repository. 

In the Dashboard, click "Import repository", then specify `https://github.com/proftak/modules` as "the URL for your source repository". You can ignore the credential questions, but name your repository before clicking "Begin import".

It will take some time to finish the cloning. Once completed, click on the new repository. 

# Repo settings

Once cloned, you need to change a few settings. Click "Settings" when you are viewing the repo.

* `Pages` Click `Pages` on the left to specify how the HTML documents are published.
* In `Build and deployment`, s
  * Select "Deplay from a branch" for `Source`.  
  * Select "main" and "/root" for `Branch`.
 
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

Then edit the content in the main editing area. Remember to click "Commit changes..." to save the content.

Note that as soon as the content is committed, the "workflow" to publish the committed content will start. 






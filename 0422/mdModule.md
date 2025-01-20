---
title: "Module 0422: Introduction to `git`"
---

# What is `git`?

`git` is a tool designed for collaboration in terms of coding. However, `git` can also be used for projects that involve mostly or wholly documentation. `git` works best for source material that is in plain text.

# Concepts

## Files, folders and objects

From the user's perspective, `git` works with files and folders. However, regular files and folders are represented as objects internally. Most users do not need to understand or access the underlying objects.

## Repository

A repository refers to the underlying objects representing the files and folders that are revision-controlled. A repository can be local, meaning that it exists in the same file system as the files and folders that are being represented. In this context "in the same file system" is almost the same as saying "on the same computer."

A local repository can be initialized by an `init` in a folder that will contain the files and folders. `git` automatically creates the repository in a "hidden" subfolder in the same folder that will contain the files and folders of a project.

A remote repository consists of the objects that are used to represent files and folders, but such objects exist on a remote computer that is accessible via networking.

A remote repository can be `clone`d to a local repository so that a user can view and edit the files and folders. Note that a remote repository can be simultaneously `clone`d to multiple local repositories on different computers. As a result, files and folders can be modified by multiple users at the same time.

## Commit

A `commit` applies to a local repository. A `commit` updates the objects of a local repository to record the modifications of files and folders.

Because a `commit` is local, a user can perform as many commits as practical to keep track of changes. `git` offers tools to show differences between commits. This is helpful to find out changes between commits as a part of debugging.

## Push

A `push` first analyzes all the modifications of a local repository since the initial `clone` or the last `push`. Then these modifications are sent to and integrated into the associated remote repository.

A `push` should occur only after the user of the local repository has achieved a milestone of a roadmap that the team has agreed upon. This often means the code that is pushed should be debugged and has been verified to meet all the specifications as agreed.

Each `push` is an atomic event. If two local repositories are pushing at the same time, one will be completed before the other one starts.

Note that a `push` does not automatically propagate the modifications to all the local repositories that are associated with the remote repository.

## Pull

A `pull` queries the remote repository and analyzes all the modifications to the remote repository since the initial `clone` or the previous `pull` operation. Then the modifications are applied to the local repository where the `pull` operation is executed.

A `pull` allows the user of a local repository to bring in all the released (pushed) updates from other teammates.

## Branch and Merge

Every repository starts with a default `MAIN` branch. A single branch is a chain of `push` operations. The latest `push` is also called the `HEAD` of a branch.

`branch` is also an action. A remote repository can be branched to create additional parallel chains of push operations.

The most common situation to create a branch is for debugging purposes. Let's say a user reports a bug while using version 3.1.2 of a program. If the program is under active development, the `HEAD` of the `MAIN` branch may be in version 3.2.2. 

In order to address the issue reported based on version 3.1.2, a developer needs to `clone` the 3.1.2 version. At this point, the developer also creates a new branch, let's call it 3.1.2.1. Internal to the team, the development team can use `push` and `pull` to extend the new branch (3.1.2.1) until the reported issue is resolved. The entire 3.1.2.1 branch is independent of the `MAIN` branch. When the issue/bug is resolved, the `HEAD` of the new branch 3.1.2.1 can be released as a bug-fixed version of 3.1.2 to customers who have been using version 3.1.2.

If the addressed issue should also be applied to the `MAIN` branch (version 3.2.2), `git` can `merge` the 3.1.2.1 branch to the `MAIN` branch. This `merge` operation consists of analyzing all the changes in the entire 3.1.2.1 branch and applying those changes to the `HEAD` of the `MAIN` 3.2.2 branch. In other words, the bug fix is also now applied to the latest version of the program.

A `merge` may encounter conflicting changes. In this example, the modifications of the entire 3.1.2.1 branch may conflict with modifications from the version 3.1.2 release of the `MAIN` branch to the current `HEAD`. In such a situation, the `merge` attempt reports the conflict and the conflict must be resolved by a manual modification of the `HEAD` of the `MAIN` branch or the 3.1.2.1 branch.

# Using GitHub

While `git` can operate entirely as a single local repository, any collaborative work will need a remote (centralized) repository. Because `git` is an open-source tool, any team can create and maintain their own remote repository. However, GitHub is free, and it offers many features in addition to revision control.

## Account Registration

The first step is to register an account at [GitHub](https://github.com).

## Using `git` in Linux with GitHub

`git` is the command line executable that does all the work, as opposed to GitHub being the service to host remote repositories, along with the support to handle issues and discussions.

### SSH and GPG keys

Click on the user avatar, then "settings", then "SSH and GPG keys."

An SSH key enables convenient communication between a local repository and the remote repository using SSH. SSH (Secure SHell) is an encrypted communication protocol that is useful for many purposes. `git` (as a command line executable) can utilize SSH for secure communication.

To use SSH, use `ssh-keygen` on the computer that is hosting a local repository if an SSH is not already generated. Then copy the content of the file `id_rsa.pub` to the "key". 

The key should be generated using the email account associated with the GitHub account. This means the command to generate the key should look like `ssh-keygen -t ed25519 -C "abc@def.com" -f ~/.ssh/id_blah` where `abc@def.com` is the email address associated with the GitHub account. `id_blah` should be replaced by the desired file name of the key.

If there are multiple SSH keys on the local system, then `~/ssh/config` should include an entry like the following:

```text
Host github.com
  HostName github.com
  IdentityFile ~/.ssh/id_blah
```

Replace `id_blah` with the actual *private key* file name. Then the file permission should changed (other `ssh` refuses to use it) using the following command: `chmod 600 ~/.ssh/config`.

Last, but not least, make sure the SSH agent is running and knows the key using the following command:

```text
ssh-add ~/.ssh/id_blah
```
### Create a local repository

Create a new folder for the project. In a command line interface, change the directory using `cd` to the folder, and execute the following command:

```bash
git init
```

That's it!

In this folder, you can now use `add` and `commit` to create files and folders and modify them. Create files the usual way. Then use `add` to add the file(s) to the local repository, for example, `git add README.md` adds the newly created `README.md` file to the local repository.

After adding some files, you can use `git commit` to make the changes to the local repository. The `add` command only registers that a new file is in the repository, but the content of the new file is not reflected in the internal object representation until the `commit` executes.

### Creating a new GitHub repository

Use the web interface of [GitHub](https://github.com) to create a new repository.

Pay attention to the box titled "Quick setup -- if you have done this kind of thing before". Click "SSH" (as opposed to "HTTPS") to get the SSH remote repository designator. Copy that.

Then run the following commands:

```bash
git branch -M main # name the only branch main
git remote add origin git@github.com:username/repository.git # set up the remote repository substitute username and repository!
git push -u origin main # perform the first push to update the remote repository
```

## Using GitHub Desktop in Windows or MacOS

[GitHub Desktop](https://docs.github.com/en/desktop) is available for Windows and MacOS. GitHub Desktop makes GitHub easier to use compared to the CLI method in Linux. However, the key concepts still apply. 

Start with [installing GitHub Desktop](https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop).

There are a few downsides to using GitHub Desktop. The first one is this requires installation on a computer. Many school computers are locked down and do not allow the installation of software. The second one is that the GUI hides the actual commands. It is much more difficult to transition from GitHub Desktop to the `git` CLI than the other way around!

## Using `git` CLI in Windows or MacOS

[Download `git`](https://git-scm.com/downloads) and "install" it. 

### Windows

Note that in Windows, `git` is available in a "portable" edition that does not require an installation. In Windows, another alternative is to install [portable Cygwin](https://sourceforge.net/projects/cygwin-portable/), then install `git` in Cygwin. Cygwin is interesting because it emulates the Linux/Unix environment so that most CLI instructions intended for Linux or MacOS `terminal` also work in Cygwin.

A portable distribution in Windows is intended to run directly from a thumb drive. This allows the user to put all the source files, along with `git` and other tools, on a thumb drive and utilize any Windows machine to continue development. 

### MacOS

MacOS `terminal` is a Unix CLI. Once `git` is installed, all the commands described in the Linux section should also work.

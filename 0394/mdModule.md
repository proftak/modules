---
title: "Module 0394: Installing riverSpider"
---

# What is `riverSpider`?

`riverSpider` is a tool that allows effective debugging using the TTP
tool chain. It consists of a BASH (Borne-again shell) script that makes
use of several typical Unix/Linux tools.

Because `riverSpider` started as a Linux tool to help the instructor
improve programming efficiency, it was never designed to work on
Windows. As more students who use Windows exclusively want to benefit
from this tool, the instructor looked into ways to get `riverSpider` to
work on Windows. There is already a solution using PowerShell, but that
still has dependency on the installation of PowerShell 7, and the script
is significantly different from the BASH version.

Note that `riverSpider` includes `logisim310.jar`. As such,
`riverSpider` is also useful for projects that do not involve the use of
TTP and the assembler.

# What is Cygwin?

Cygwin consists of a DLL (dynamically linked library) that provides an
emulation layer so that programs designed for a Unix/Linux environment
can cross compile and run on Windows. Cygwin also includes a typical set
of command line tools that exist in Unix/Linux systems.

Typically, Cygwin requires an installation that is not designed to be
"portable." This means the installation requires administrative
permission, and it is not easy to transport the installation from one
computer to another. A *portable* Cygwin installation, however, allows
the installation (a folder) to be put on a thumbdrive or any portable
medium, and have the tool to run on most Windows computers.

The main advantage of using Cygwin is that Unix/Linux commands will work
in Windows without installing a Linux VM.

# Getting the Cygwin-based `riverSpider` to work

-   Download
    [cygRiverSpider.7z](https://drive.google.com/file/d/1REBrhNtwiNTDC4EHHfEaOBJOuYxYrlWb/view?usp=drive_link).
    This file has a size of about 330 MB.
-   Use [7-zip](https://www.7-zip.org/) to extract the files.
    -   You can extract to a folder on a thumb drive so that the
        "installation" is portable.
    -   The extraction can take *very* long using slower thumb drives,
        be patient!
    -   Even in a virtualized environment, extraction to a hard drive
        takes 6 minutes.
-   The "home folder" is located at
    `cygRiverSpider/cygwin/cygwin/home/root`, assuming `cygRiverSpider`
    is where the ZIP file is extracted to.
    -   You can create additional folders in the "home folder" for your
        projects.
-   Once extracted, use `cygwin-portable.cmd` to start a Cygwin shell.
-   It is best to download files to the home folder, or subfolders there
    of.
    -   You can change your browser to always ask the destination when
        you download files.
-   If you are writing programs for TTP:
    -   In the Cygwin shell, use `cd riverSpider` to change the working
        directory to `riverSpider`.
    -   Use `notepad READM.md` to read the markDown read-me file.
    -   after setting up all the files as described in the read-me file
        (this also involves some work in the corresponding Google Sheets
        document), use `./submit.sh` to submit a TTPASM file.
-   For general use:
    -   A shell script `logisim.sh` is created to make it easier to
        launch Logisim. You can supply additional arguments and
        switches.

---
title: "Module 0371: Tracing TTP code execution"
---

# To start

You will need your own copy of the assembler. You can clone [the assembler](https://docs.google.com/spreadsheets/d/1TcbAnH3Qj4xTizfTpMcDmXEq9CN_rVDQIa2BwSSEeXQ/edit?usp=sharing) by using the menu item "File \| Make a copy", be sure to specify the (destination) Folder as some folder in *your own* Google Drive.

Also, every program should start with a `nop` instruction. This is due to a bug in Logisim that only seems to matter when Logisim is run from the CLI (command line interface).

# The longer way

First, use an editor to edit the source code in mnemonics.

Then copy and paste the code to column A of the source sheet of the assembler. If the assembler reports any errors, fix the errors in the editor, and repaste the entire program in column A of the "source" sheet.

Switch to the "RAM file" sheet, and use the menu item "File \| Download \| Comma Separated Values" to download the CSV file.

On a command line, run the program. The exact command depends on the OS, but generally, it is something like the following:

```
java -jar path/to/logisim310.jar path/to/processor0004.circ -load path/to/ramContent.csv -tty table > path/to/logFile.tsv
```

The way you specify a path depends on your operating system, please Google search for a tutorial that is specific to your operating system. 

* `ranContent.csv`: this is the file that you downloaded earlier from the "RAM file" sheet of the assembler.
* `logFile.tsv`: this is the log file that is in a TSV (tab-separated values) format.

Go back to the assembler, switch to the "traceRawData" sheet, then use the menu item "File \| Import" to trigger the "Import file" dialog. Click "Upload", and select the `logFile.tsv` from earlier.

You will then be presented with the option of importing the TSV, be sure to follow these specifications:

* Import location: Replace Current Sheet
* Separator type: tab
* Convert text to numbers, dates, and formulas: uncheck

After the import, the "analysis" sheet displays the log of the execution of your code.

# The shorter way

You can use `riverSpider` to automate a large portion of the steps. Go to the [shared folder](https://drive.google.com/drive/folders/0BxsMACqxAFNwUkJxWmJKZ0R3Ync?resourcekey=0--R62aR3g30jRuZT_YoC30Q&usp=drive_link) and download `riverSpiderMac.zip` for Mac OS or `cygRiverSpider.7z` for Windows. Watch [this video](https://youtu.be/SO_uWlbsZkk) for a step-by-step explanation. Windows users should watch the entire video, while Mac OS users can skip to the 10:00 mark after downloading and unzipping `riverSpiderMac.zip`.

## Windows

If you get the Windows version, you need to download and install [7-zip](https://www.7-zip.org/download.html) to decompress the "7z" file. I suggest that you right-click on `cygRiverSpider.7z`, then `7-Zip`, then `Extract Here` or `Extract files...`. The file decompresses to use about 1.5GB of space.

The Windows version is "portable," which means you can decompress to a folder on a thumb drive and it will work from a thumb drive!

To get started, double-click on `cygRiverSpider` (as a folder after decompression), then `cygwin`. Then double-click `cygwin-portable` to start the command-line interface (CLI). 

Cygwin can access your files in other folders, but it gets complicated. It is best to put your files in the `riverSpider` subfolder.

## Applicable to both Windows and MacOS

To use `riverSpider`, type the following command first:

`cd riverSpider`

Read `README.md` first! You can use your favorite text editor to read it. In Windows, you can even use Notepad—just type `notepad READM.md`! The script does not work until you follow the instructions and set up your own assembler Google Sheets.

Then you can use the following command to run your code:

`./submit.sh test.ttpasm`

# Reading the analysis sheet

* Column A: this is the address of the instruction that executed. You can cross reference this hexadecimal address with column W of the `assemble` sheet to find out exactly which instruction of your program corresponds to a particular trace entry
* Column B: if RAM is read from, there is an entry here. Note that there are "false entries" in this column for certain instructions. This means not every item is significant in column B.
* Column C: if RAM is written to, there is an entry here that specifies which location is overwritten by which value. Both the address and the content are specified in hexadecimal.
* Column D: if a register is updated, there is an entry here.
* Column E: if the flags register is updated, there is an entry here.
* Column F: this is the line number corresponding to the program in the `Source` sheet that executes
* Column G: this is the actual line of code that executes

## Skipping to the end

Some traces are very long. If you want to skip to the end, you can find the row number in the "summary" sheet, cell A1.

Skipping to the end of a trace is helpful if you just want to check whether the program terminates with the correct outcome or to find out how it stopped.

## Searching for specific items

Google Sheets offers some great features for searching and finding items. Use control-H or the menu item "Edit \| Find and Replace" to trigger the dialog box.

Do not replace any values in the analysis sheet, that will break the mechanism! 

The search range control is very helpful if you want to find a pattern only in a specific column. For example, you may be interested in only when a register is updated, then the search can focus on column D. To specify column D, change the drop-down of "Search" to "Specific range", then specify "analysis!D:D" to search the entire column D.

Another great feature that is more advanced is "Search using regular expressions." This allows you to use regular expressions to specify a pattern. This can be helpful in instances where a search is not for a specific value, but for a pattern that can be used to describe many individual values.

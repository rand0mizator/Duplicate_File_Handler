# Duplicate_File_Handler
JetBrains Academy project https://hyperskill.org/projects/176

STAGE 1\4:
Theory
Let's get straight to the point. For our task, we need the os.walk method. The Tutorial's Point guide can shed some light on how to use it.

Description
A computer is a great thing. It helps us store and manage tons of information. Every user knows how to work with folders. In this step, we will learn how to get a list of files and folders within a specific directory.

Objectives
In this stage, your program should:

Accept a command-line argument that is a root directory with files and folders. Print Directory is not specified if there is no command-line argument;
Iterate over folders and print file names with their paths. The direction of the slashes in the printed out paths do not matter. Tests are platform independent, so different style of slashes ("/" or "\") are valid.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Suppose, you have the following set of files and folders:

+---[root_folder]
    |
    +---wall.png
    +---pass.txt
    +---[docs]
    |   |
    |   +---project.py
    |   +---calc.xls
    |   +---tutorial.mp4
    |   +---[res]
    |       |
    |       +---data.json
    |   +---[output]
    |       |
    |       +---result.json
    +---[masterpiece]
        |
        +---rick_astley_never_gonna_give_you_up.mp3
Program output:

> python handler.py root_folder

root_folder/wall.png
root_folder/pass.txt
root_folder/docs/project.py
root_folder/docs/calc.xls
root_folder/docs/tutorial.mp4
root_folder/docs/res/data.json
root_folder/docs/output/result.json
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3




STAGE 2\4:
Description
In this stage, we start by identifying files of the same size in bytes. The os.path module allows you to get access to file extension and size. The Official Documentation can help you with that.

Of course, we cannot be absolutely sure that files of the same size and format are duplicates. This will help us, however, narrow down the search. It is also important to keep track of the scanned files. Add an ability to search for files of a specific file format and then sort the found files by size.

Objectives
Keep the functionality from the previous stage. To complete this stage, your program should:

Accept a command-line argument that is a root directory with files and folders. Print Directory is not specified if there is no command-line argument;
Read user input that specifies the file format (see examples). Empty input should match any file format;
Print a menu with two sorting options: Descending and Ascending. They both represent the respective order by size of groups of files. Read the input. Print Wrong option if any other input is entered. Repeat until a correct input is provided;
Iterate over folders and print the information about files of the same size: their size, path, and names.
Please note: you should use full path to file from root directory when printing or reading.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Suppose, you have the following set of files and folders:

+---[root_folder]
    +---gordon_ramsay_chicken_breast.avi /4590560 bytes
    +---[audio]
    |   |
    |   +---voice.mp3 /2319746 bytes
    |   +---sia_snowman.mp3 /4590560 bytes
    |   +---nea_some_say.mp3 /3232056 bytes
    |   +---[classic]
    |   |   |
    |   |   +---unknown.mp3 /3422208 bytes
    |   |   +---vivaldi_four_seasons_winter.mp3 /9158144 bytes
    |   |   +---chopin_waltz7_op64_no2.mp3 /9765504 bytes
    |   +---[rock]
    |       |
    |       +---smells_like_teen_spirit.mp3 /4590560 bytes
    |       +---numb.mp3 /5786312 bytes
    +---[masterpiece]
        |
        +---rick_astley_never_gonna_give_you_up.mp3 /3422208 bytes
Program output:

> python handler.py root_folder

Enter file format:
>mp3

Size sorting options:
1. Descending
2. Ascending

Enter a sorting option:
> 3

Wrong option

Enter a sorting option:
> 2

3422208 bytes
root_folder/audio/classic/unknown.mp3
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3

4590560 bytes
root_folder/audio/rock/smells_like_teen_spirit.mp3
root_folder/audio/sia_snowman.mp3

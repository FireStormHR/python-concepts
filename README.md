![python logo pluys text](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)

# Welcome to the exercise project of the python course
Here we can put all discussed topics to the test.
Whenever you get stuck at an exercise, make sure to check out the tips section in this md below.

## Installation
To edit and run this project, you can undertake the following steps
1. Install [Python](https://www.python.org/downloads/), at least v3.9, make sure Python get added to the system PATH (checkable option during installation wizard).
2. Download this project to your machine, press the green `code` button followed by `Download zip`. Unpack the Zip afterwards.
3. Download an editor/IDE, many good options. If no personal preference, [VScode](https://code.visualstudio.com/download) is recommended.
    1. Open VScode, select open folder, select the unpacked Zip from step **2**
    2. Install the following extensions `Ctrl + Shift + x`.
        - autopep8
        - intellicode
        - powershell
        - pylance
        - python
        - (optional) Black Formatter
    3. Link the downloaded python Interpreter to VScode by doing: `Ctrl + Shift + p -> Python: select interpreter` and select the interpreter which is like at `%user%\AppData\Local\Programs\Python\Python311`
4. Open a terminal and check if py is callable `py --version`. (In VScode an integrated terminal is available `` Ctrl + Shift + ` ``)
5. Ready to exercise! Look at the tasks and fill in the blanks. Everytime you want to try out an exercise enter in the terminal: `py app.py`

## Tips for exercises
### Exercise 1
View it as a cabinet with documents. The '=' sign is telling everyone: 'At this location ive named myself I will put this bit of information'.
So for example: `drawerB = 5`


### Exercise 2
When googling a solution for this task, changing the type of a value is often called parsing or casting.
For checking if the type-changing code worked, you need to use a try-except block (so not an if)
# Background

A question consists of the following files:

-   Description file - A description of the problem, in Markdown format
-   test.py - The main testfile for a question, this will be ran by
    mypytutor
-   attempt.py - The student\'s question attempt, this will be the
    default code provided to a student when they start a question, during
    testing make sure to test with a complete solution to check the
    tests work correctly

When running a question, Mypytutor will load some files. When writing
new questions these files can be added to the same folder as attempt.py
and test.py

-   python\_test\_case.py - Contains a customized unittest.TestCase
    class with some functions to write questions easily (such as
    checking if a variable or function is defined)

# Writing a new question

Make a copy of the sample question folder and start writing a question,
some example questions are provided for reference.

## Write the description

The description is written in Markdown format, for a reference look here
[Markdown Reference](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Note about images

Images work in markdown, however the image itself needs to be hosted online
somewhere, currently there is no way for mypy to host the image so in the
meantime you can use a online image hosting service.

# Uploading questions

Once you are happy with the question, it can be uploaded through the
mypy interface

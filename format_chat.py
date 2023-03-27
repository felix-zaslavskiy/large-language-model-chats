# Program to take a chat log and format it in MD format.
"""
Python program will take a filename on command line.
Load the filename into memory. If file not found produce error.
The format for the file is described next.
Header of the file like so:
# ChatGPT4 - Some description goes here - 16

* **Date of conversation:** March 26, 2023
* Analyze some ideas of famous people on current events.

> **User1**
Text text text text

> **ChatGPT**
Text text text.

text text text text

text text..

> **User1**
Text text text text

> **ChatGPT**
Text text text...

and on to continue alternating between users.

The text in the file will be transformed to valid Markdown format.
Text will be added to the blockquote of the user or chatbot it is associate with.
For example:
> **ChatGPT**
Text text text.

text text text text.

Becomes:
> **ChatGPT**
> Text text text.
>
> text text text text



"""
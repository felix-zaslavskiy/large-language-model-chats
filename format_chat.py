# Program to take a chat log and format it in MD format.
"""
Python program will take a filename on command line.
Load the filename into memory. If file not found produce error.
"""

import sys
import os


"""
Function transform_lines() takes a list of lines (ending with \n).
Function will transform these lines into a valid Markdown format.
Start with header section
After > **User1** the templated section start. The example is below:

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

continue alternating between users.

Text lines will be added to the blockquote of the user or chatbot it is associate with.
For example:
> **ChatGPT**
Text text text.

text text text text.

Becomes:
> **ChatGPT**
>
> Text text text.
>
> text text text text

Note the extra > after the > **ChatGPT** line

For example 
> **ChatGPT**
Text1

text2

> **User**
text3

> **ChatGPT**

Becomes:
> **ChatGPT**
> Text1
>
> text2

> **User**
> text3

> **ChatGPT**
Return the transformed text as a list of lines.
"""
def transform_lines(lines):
    output_lines = []
    inside_header = True
    inside_blockquote = False

    for line in lines:
        if inside_header:
            output_lines.append(line)
            if line.startswith("> **"):
                inside_header = False
                inside_blockquote = True
                output_lines.append(">\n")
        elif inside_blockquote:
            if line.startswith("> **"):
                if not output_lines[-1].startswith(">"):
                    output_lines.append(">\n")
                output_lines.append(line)
                output_lines.append(">\n")
            else:
                if line.strip():
                    output_lines.append("> " + line)
                else:
                    output_lines.append(">\n")

    return output_lines




def process_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        output_lines = []

        output_lines =  transform_lines(lines)

        with open(filename, "w") as output_file:
            output_file.writelines(output_lines)

        print(f"Markdown file updated: {filename}")

    except FileNotFoundError:
        print(f"Error: {filename} not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py filename")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        sys.exit(1)

    process_file(filename)


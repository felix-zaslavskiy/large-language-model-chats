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
>
> Text text text.
>
> text text text text

Note the extra > after the > **ChatGPT** line

"""

import sys
import os

def process_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        output_lines = []
        inside_blockquote = False
        header = True
        for line in lines:
            if header:
                output_lines.append(line)
                if line.startswith("> **"):
                    header = False
                    output_lines.append(">\n")
                    inside_blockquote = True
            elif line.startswith("> **"):
                output_lines.append(line.rstrip() + "\n>\n")
                inside_blockquote = True
            elif line.strip() == "":
                if inside_blockquote:
                    output_lines.append(">\n" + line)
                else:
                    output_lines.append(line)
                inside_blockquote = False
            else:
                if inside_blockquote:
                    output_lines.append("> " + line)
                else:
                    output_lines.append(line)

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


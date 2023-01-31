# # python-to-markdown

# This is a utility for turning the python files into markdown. Its intended as
# a intermediate step for executing a jupyter notebook via the shell. 

# Top level comments (i.e. with no indentation) are interpretted as paragraphs, while code is interpretted as code blocks. You can put whatever markdown you like nested in the top level comments.

# Indented code blocks are not interpretted as comments

# Pipe python source code to this utility. Eg/
# 
# ```sh
# cat example.doc.py | ./python-to-markdown.py > example-output.md
# ```

# ## Why?

# I like editing my jupyter notebooks in vim, at first I was storing them as
# markdown and converting them with `jupyter nbconvert` but this approach loses
# out on language server, and takes quite a long time to run.

# So now the idea is write them as `.py` files (which can be run quiclky using python, require no special set up for langauge server or be used as modules). If I want to use them to generate documentation the process is convoluted, but works well for me at least:
#
# 1. Convert python src to markdown using this utility (interpretting top level comments as markdown).
# 2. Execute in the shell using `jupyter nbconvert` sending output to an html file.
# 3. Use pandoc to covert html back into markdown.

# ## Implementation:


import sys
import re

number_of_blanks = 0
def print_blanks():
    global number_of_blanks
    for i in range(0, number_of_blanks):
        print("")
    number_of_blanks = 0

last_block_type = "paragraph"
for line in sys.stdin:
    if re.search("^$", line):
        number_of_blanks += 1

    elif re.search("^# ?", line):

        if last_block_type == "code":
            print("```")

        print_blanks()

        uncommented = re.sub("^# ?", "", line, 1)
        print(uncommented, end="")
        last_block_type = "paragraph"
        
    else:
        print_blanks()
        if last_block_type == "paragraph":
            print("```code")
        print(line, end="")
        last_block_type = "code"

if last_block_type == "code":
    print("```")

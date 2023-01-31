# # Example document
#
# This is an example 

print("Hello world")

# Another comment block becomes a paragraph
# 
# Let's set a variable

greeting = "Hiyyya"

# Blank lines don't count as code blocks...

# ...there should be no code block between this line and the one above

print("{} world (Variable is carried from previous code block)".format(greeting))

# Gaps between code lines don't interupt the block either:

a = 1

b = 2

print(a + b)


# Indented comments should not be interpretted as paragraph blocks

def say_hello():
    # This shouldn't be a paragraph
    print("Hello")

# If the document ends with a code block, be sure to close it!

print("Thanks for listening")

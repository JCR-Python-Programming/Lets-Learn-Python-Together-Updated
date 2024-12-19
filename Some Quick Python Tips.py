# Here are some quick tips for the print() function and others in Python.

# Created by Joseph C. Richardson, GitHub.com

# Invoke the ( \ ) backslash in print() function text to force a hard
# line break to make Python print() function text code be on multiple
# lines.

print('This is a paragraph inside a print() function, using the \
backslash to create a hard line break. We can keep on typing \
as many lines of text we need inside a print() function.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the ( \n ) backslash 'n' to force a line break in the printed
# screen output text on multiple lines.

print('This is a paragraph inside a print() function, using the \
backslash to create a hard line break.\nWe can keep on typing \
as many lines of text we need inside a print() function.\nWe can \
force printed screen output text on multiple lines.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a variable to store the above print() function text code.

text = 'This is a paragraph inside a print() function, using the \
backslash to create a hard line break.\nWe can keep on typing \
as many lines of text we need inside a print() function.\nWe can \
force printed screen output text on multiple lines.'

print(text) # prints out the value inside the variable called 'text'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try another way to create printed text paragraphs, without
# invoking the ( \ ) backslash and the ( \n ) backslash 'n'.
# Let's use three single ( ''' ''' ) quote marks instead.

print('''This is a paragraph inside a print() function, using the
backslash to create a hard line break. We can keep on typing
as many lines of text we need inside a print() function. We can
force printed screen output text on multiple lines.''')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a variable to store the above print() function text code.

text = '''This is a paragraph inside a print() function, using the
backslash to create a hard line break. We can keep on typing
as many lines of text we need inside a print() function. We can
force printed screen output text on multiple lines.'''

print(text)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a poem, I once wrote through tears of failure.

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

print(poem)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Welcome to the the split() function. This split() function has a dot '. '
# in front of it that joins the variable, 'poem' to the split() function
# using another variable called, 'text'. What the split() function does
# is turns any text paragraphs into an actual list of words, which you
# can then use their indexes [index] to pick out words within the poem.

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

# For example: the first word in the poem is 'Knowledge', which
# is index[0] with the single quote marks as in no spaces in between
# them or the word Knowledge. Any words therafter dosen't have
# quote marks; only the title of the poem as in normal poems,
# sometimes you want quote marks in a title or word/words alike.

text_values = poem.split()

print(text_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Did you know you can create variables for some of these Python
# commands/functions? This will give us much more opertunities
# to use variables as Python code in a for loop that loops through
# a list of values, which are actual Python commands/functions.
# You can create two or more Python commands/functions with
# just one for loop alone. Let's explore what these variables can
# do for us, using actual Python code itself.

absolute_num = abs
add_nums = sum
ascii_character = ascii
ascii_character_num = ord
ascii_character_value = chr
binary_base_2 = bin
character_string = str
convert_to_list = list
convert_to_set = set
convert_to_tuple = tuple
dictionary = dict
execute_program_code = exec
exit_program = exit
float_num = float
George_Boole = bool
hexadecimal_base_16 = hex
index_error = IndexError
integer_num = int
maximum_num = max
memory_error = MemoryError
minimum_num = min
octal_base_8 = oct
redundant_code = exec
round_num = round
super_function = super
text_input = input
text_print = print
value_error = ValueError
value_length = len
you_quitter = quit

# Let's try a simple print() command/function and see what this does
# We will also create a variable to be a text placeholder, so we don't
# have to keep rewriting text sentences over and over again.

text = "This was Python's print() command/function."

# this:

print("This was Python's print() command/function.")

# or this:

text_print(text) # use variables instead if you like

# Let's try a few more to get the hange of things. Let's add some numbers
# together with the sum() command/function, we renamed to 'add_nums'
# using a variable to store the actual sum() command/function. We also
# need to create a variable we'll call nums, so we can store a default tuple
# of numbers without any parenthesese, ie: (1,2,3,4,5,6,7,8,9)

nums = 1,2,3,4,5,6,7,8,9 # this is a tuple by default, without parentheses ' () '

# this:

print(sum(nums))

# or this:

text_print(add_nums(nums))

# Let's try a simple input() command/function and see what this does We will
# create a variable to be a text placeholder, so we don't have to keep rewriting
# text sentences over and over again. We also have to create an 'user_input'
# variable so the user can type into it.

input_text = "This was Python's input() command/function."

# this:

user_input = input("This was Python's input() command/function.")

# or this:

user_input = text_input(input_text)

# Let's use a for loop to loop through a tuple of variables, which
# are actual Python commands/functions. Let's creat our tuple called
# loop.

loop = integer_num,binary_base_2,hexadecimal_base_16

for i in loop:
    text_print(f'{i(255)}. You only need one print statement with a list of variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some ways to create Binary Base 2, Hexadecimal
# Base 16 and Octal Base 8 systems in Python.

print(bin(255))  # 0b11111111 = 255

print(f'{255:b}')  # 11111111 = 255

print(hex(255))  # 0xff = 255

print(f'{255:x}')  # ff = 255

print(oct(255))  # 0o377 = 255

print(f'{255:o}')  # 377 = 255
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ASCII (American Standard Code for Information Interchange)

# Let's create ASCII code values and use them inside a print()
# function, so we can see what letters or numbers they are.

# lowercase ASCII code values

print(ord('a'))  # 97

print(chr(97))  # a

print(ord('b'))  # 98

print(chr(98))  # b

print(ord('c'))  # 99

print(chr(99))  # c

# uppercase ASCII code values

print(ord('A'))  # 65

print(chr(65))  # A

print(ord('B'))  # 66

print(chr(66))  # B

print(ord('C'))  # 67

print(chr(67))  # C

# Let's create a for loop that will print out the alphabet in lowercase
# characters. We will also use the (end=' ') prefix to keep all the
# printed alphabet values to stay on one, single line.

for i in range(97,123):print(chr(i),end=' ')

# Let's create a for loop that will print out the alphabet in uppercase
# characters. We will also use the (end=' ') prefix to keep all the
# printed alphabet values to stay on one, single line.

for i in range(65,91):print(chr(i),end=' ')

# Let's create integer characters from 0 through 9 with a for loop,
# using ASCII code values.

for i in range(48,58):print(chr(i),end=' ')

# Let's create integer character values out of ASCII code values
# and add them.

print(chr(48+1))  # 0 + 1 = 1

print(chr(49+1))  # 1 + 1 = 2

print(chr(50+1))  # 2 + 1 = 3

print(chr(51+1))  # 3 + 1 = 4

print(chr(52+1))  # 4 + 1 = 5
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The ascii() function returns a readable version of any object, like
# strings, tuples, lists, etc.

print(ascii('sam'))  # 'sam'

print(ascii('s\am'))  # 's\x07m'

print(ascii('sa\m'))  # 'sa\\m'

print(ascii('\a'))  # '\x07'

print(ascii('\b'))  # '\x08'

print(ascii('\c'))  # '\\c'

# Store the ascii() function inside a variable called 'ascii_function'.

ascii_function = ascii('s\am')

print(ascii_function)  # 's\x07m'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the := Walrus Operator to create the following Python prgram
# examples, using tuples(), lists[] and dictionaries{}.

if my_tuple := (
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5'):pass

for value in my_tuple:print(value)

if my_list := [
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5']:pass

for value in my_list:print(value)

if my_dictionary := {
    1:'Value 1',2:'Value 2',3:'Value 3',
    4:'Value 4',5:'Value 5',6:'Value 6'}:pass

for value in my_dictionary:print(
    my_dictionary.get(value+1,f"There are no more values to loop \
through after 'Value {value}'."))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use Python's Error Handlers to not only stop errors from occurring.
# But you can also use Error Handlers to manipulate Python code flow
# of control. As you may notice, I used the walrus := operator to write
# less lines of code. Play around with the values within these program
# examples and call wrong indexes, and wrong strings together to force
# these exception handlers to do their work, which is to stop programs
# from crashing, and they are also used for program manipulation
# purposes to change program flow control.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# The 'pass' prefix is for code place holding if you don't wish to write
# any code blocks underneath expressions that use code blocks, such
# as the Python program above shows in our first example.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Without the use of the walrus := operator.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# With the 'pass' prefix placeholder for code blocks.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Let's use one 'try:' and two exception handlers, alongside the walrus
# := operator. We will use one 'IndexError:' handler and one 'TypeError:'
# handler to create some programming manipulation within our Python
# program examples below.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
        print(x[4]+'character string')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')

# Python executes/runs its programs from the top downward, as the
# very same way you can see the code order. Each instruction is first
# to execute, is the first to be serviced. In most cases multiple exception
# handlers can only execute one or the other, depending on the code order.

if x := (0,1,2,3,4,5):
    try:
        print(x[4]+'character string text.')
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the := Walrus Operator to tempararly check for values in tuples,
# lists, dictionaries and sets. That way, you can be a bit lazy and
# not have to write two lines of code only to check for values. Note:
# default tuples won't work with the := walrus operator for indexing.
# Python cannot seem to see the values as either strings, nor integers
# when using the := walrus operator.

print(x := 1,2,3,4,5,6,7,8,9)  # x creates a default tuple of values

print(x[0]) # TypeError: 'int' object is not subscriptable

print(x := (1,2,3,4,5,6,7,8,9))  # x creates a tuple of values

print(x[0]) # tuple index[0] is the value '1'

print(x := [1,2,3,4,5,6,7,8,9])  # x creates a list of values

print(x[0]) # list index[0] is the value '1'

print(x := {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9})  # x creates a dictionary of values

print(x.get(1,'Not Found!'))

print(x := {1,2,3,4,5,6,7,8,9})  # x creates a set of values
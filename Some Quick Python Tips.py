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
# Invoke the str() string function to mix string characters with
# non-string characters, like numbers to do calculations within
# print() function text strings.

print('String Value mixed with a non-String Value',str(1+2))  # 3

# or:

print('String Value mixed with a non-String Value '+str(1+2))  # 3
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Did you know you can create variables for these Python
# commands/functions? From here onward, we are going
# to store Python commands/functions inside variables
# and use them instead of actual Python command/functions,
# such as abs(), sum(), ascii() and so on. Copy down and
# refer to this Python command/functions chart below:

absolute_value = abs
add_number_values = sum
ascii_character = ascii
ascii_character_num = ord
ascii_character_value = chr
binary_base_2 = bin
cast_to_list = list
cast_to_set = set
cast_to_tuple = tuple
character_string = str
create_dictionary = dict
execute_program_code = exec
exit_program = exit
float_num = float
George_Boole = bool
hexadecimal_base_16 = hex
index_error = IndexError
integer_num = int
range_loop = range
maximum_num = max
memory_error = MemoryError
minimum_num = min
octal_base_8 = oct
redundant_code = exec
round_num = round
sorted_values = sorted
super_function = super
text_input = input
text_print = print
type_error = TypeError
value_error = ValueError
value_length = len
quit_program = quit

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

print(add_number_values(nums))

# or this:

text_print(add_number_values(nums))

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

text_print(binary_base_2(255))  # 0b11111111 = 255

text_print(f'{255:b}')  # 11111111 = 255

text_print(hexadecimal_base_16(255))  # 0xff = 255

text_print(f'{255:x}')  # ff = 255

text_print(octal_base_8(255))  # 0o377 = 255

text_print(f'{255:o}')  # 377 = 255
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ASCII (American Standard Code for Information Interchange)

# Let's create ASCII code values and use them inside a print()
# function, so we can see what letters or numbers they are.

# lowercase ASCII code values

text_print(ascii_character_num('a'))  # 97

text_print(ascii_character_value(97))  # a

text_print(ascii_character_num('b'))  # 98

text_print(ascii_character_value(98))  # b

text_print(ascii_character_num('c'))  # 99

text_print(ascii_character_value(99))  # c

# uppercase ASCII code values

text_print(ascii_character_num('A'))  # 65

text_print(ascii_character_value(65))  # A

text_print(ascii_character_num('B'))  # 66

text_print(ascii_character_value(66))  # B

text_print(ascii_character_num('C'))  # 67

text_print(ascii_character_value(67))  # C

# Let's create a for loop that will print out the alphabet in lowercase
# characters. We will also use the (end=' ') prefix to keep all the
# printed alphabet values to stay on one, single line.

for i in range_loop(97,123):text_print(ascii_character_value(i),end=' ')

# Let's create a for loop that will print out the alphabet in uppercase
# characters. We will also use the (end=' ') prefix to keep all the
# printed alphabet values to stay on one, single line.

for i in range_loop(65,91):text_print(ascii_character_value(i),end=' ')

# Let's create integer characters from 0 through 9 with a for loop,
# using ASCII code values.

for i in range_loop(48,58):text_print(ascii_character_value(i),end=' ')

# Let's create integer character values out of ASCII code values
# and add them.

text_print(ascii_character_value(48+1))  # 0 + 1 = 1

text_print(ascii_character_value(49+1))  # 1 + 1 = 2

text_print(ascii_character_value(50+1))  # 2 + 1 = 3

text_print(ascii_character_value(51+1))  # 3 + 1 = 4

text_print(ascii_character_value(52+1))  # 4 + 1 = 5
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The ascii() function returns a readable version of any object, like
# strings, tuples, lists, etc.

text_print(ascii_character('sam'))  # 'sam'

text_print(ascii_character('s\am'))  # 's\x07m'

text_print(ascii_character('sa\m'))  # 'sa\\m'

text_print(ascii_character('\a'))  # '\x07'

text_print(ascii_character('\b'))  # '\x08'

text_print(ascii_character('\c'))  # '\\c'

# Store the ascii() function inside a variable called 'ascii_function'.

ascii_function = ascii_character('s\am')

text_print(ascii_function)  # 's\x07m'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the := Walrus Operator to create the following Python prgram
# examples, using tuples(), lists[] and dictionaries{}.

if my_tuple := (
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5'):pass

for value in my_tuple:text_print(value)

if my_list := [
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5']:pass

for value in my_list:text_print(value)

if my_dictionary := {
    1:'Value 1',2:'Value 2',3:'Value 3',
    4:'Value 4',5:'Value 5',6:'Value 6'}:pass

for value in my_dictionary:text_print(
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
        text_print(x[6],'is in the "x" variable tuple().')
    except index_error:
        text_print('The IndexError handler stops index errors from occurring.')

# The 'pass' prefix is for code place holding if you don't wish to write
# any code blocks underneath expressions that use code blocks, such
# as the Python program above shows in our first example.

if x := (0,1,2,3,4,5):
    try:
        text_print(x[6],'is in the "x" variable tuple().')
    except index_error:
        pass

# Without the use of the walrus := operator.

x = (0,1,2,3,4,5)

if x == x:
    try:
        text_print(x[6],'is in the "x" variable tuple().')
    except index_error:
        text_print('The IndexError handler stops index errors from occurring.')

# With the 'pass' prefix placeholder for code blocks.

x = (0,1,2,3,4,5)

if x == x:
    try:
        text_print(x[6],'is in the "x" variable tuple().')
    except index_error:
        pass

# Let's use one 'try:' and two exception handlers, alongside the walrus
# := operator. We will use one 'IndexError:' handler and one 'TypeError:'
# handler to create some programming manipulation within our Python
# program examples below.

if x := (0,1,2,3,4,5):
    try:
        text_print(x[6],'is in the "x" variable tuple().')
        text_print(x[4]+'character string')
    except index_error:
        text_print('The IndexError handler stops index errors from occurring.')
    except type_error:
        text_print('The TypeError handler stops Type errors from occurring.')

# Python executes/runs its programs from the top downward, as the
# very same way you can see the code order. Each instruction is first
# to execute, is the first to be serviced. In most cases multiple exception
# handlers can only execute one or the other, depending on the code order.

if x := (0,1,2,3,4,5):
    try:
        text_print(x[4]+'character string text.')
        text_print(x[6],'is in the "x" variable tuple().')
    except index_error:
        text_print('The IndexError handler stops index errors from occurring.')
    except type_error:
        text_print('The TypeError handler stops Type errors from occurring.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the := Walrus Operator to tempararly check for values in tuples,
# lists, dictionaries and sets. That way, you can be a bit lazy and
# not have to write two lines of code only to check for values. Note:
# default tuples won't work with the := walrus operator for indexing.
# Python cannot seem to see the values as either strings, nor integers
# when using the := walrus operator.

text_print(x := 1,2,3,4,5,6,7,8,9)  # x creates a default tuple of values

text_print(x[0]) # TypeError: 'int' object is not subscriptable

text_print(x := (1,2,3,4,5,6,7,8,9))  # x creates a tuple of values

text_print(x[0]) # tuple index[0] is the value '1'

text_print(x := [1,2,3,4,5,6,7,8,9])  # x creates a list of values

text_print(x[0]) # list index[0] is the value '1'

text_print(x := {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9})  # x creates a dictionary of values

text_print(x.get(1,'Not Found!'))

text_print(x := {1,2,3,4,5,6,7,8,9})  # x creates a set of values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the int() integer function to create integer numbers.

text_print(integer_num(4.5))  # 4

# Invoke the float() floating point function to create floats

text_print(float_num(4))  # 4.0

# Invoke the int() integer function to convert string characters
# into non-string integer numbers

text_print('1'+'2')  # 12 is wrong!

text_print(integer_num('1')+integer_num('2'))  # 3 correct!

# Invoke the float() float function to convert string characters
# into non-string floating point numbers.

text_print('1.2'+'2.1')  # 1.22.1 is wrong!

text_print(float_num('1.2')+float_num('2.1'))  # 3.3 correct!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Return an absolute value of a negative integer number with the
# abs() function.

text_print(absolute_value(-3))  # 3

# or:

x = absolute_value(-3)  # 3

text_print(x)  # 3
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's find the minimum number in this nums_list with the min()
# function.

nums_list = [1,2,3,4,5,6,7,8,9]

text_print(minimum_num(nums_list))

# Let's find the maximum number the nums_list with the max()
# function.

text_print(maximum_num(nums_list))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's round off numbers with the round() function.

text_print(round_num(3.5))  # 4

# Round off two decimal places to the right.

text_print(round_num(3.567,2))  # 3.57
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the exec() function to store a for loop inside it and
# make it execute every time we call the exe() function. Invoke
# three single ( ''' ''' ) quote marks on each side of the code
# block as shown below.

redundant_code = '''
for i in range(10):print(i,end=',')
'''
execute_program_code(redundant_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's turn an immutable tuple into a mutable list by casting it
# with the list() function.

tuple_variable = ('Dog','Cat','Bird','Fish')

convert = cast_to_list(tuple_variable)

text_print(convert)  # ['Dog', 'Cat', 'Bird', 'Fish']

# Let's sort the list values with the sorted() function, without sorting
# the actual list values.

sort_values = sorted_values(convert)

text_print(sort_values)  # ['Bird', 'Cat', 'Dog', 'Fish']

# Let's turn the sorted mutable list back into an immutable sorted
# tuple by casting it with the tuple() function.

convert = cast_to_tuple(sort_values)

# Check to see how many values there are in the convert tuple.

text_print(convert)  # ('Bird', 'Cat', 'Dog', 'Fish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's turn an immutable tuple into a set by casting it with the set()
# function. Sets allow us to get rid of duplicate values to be sure
# that none get mistaken, due to programmer error. Note: set values
# are always in random order on the screen output as shown below.

tuple_variable = ('Fish','Dog','Cat','Dog','Bird','Fish')

convert = cast_to_set(tuple_variable)

# Check to see how many values there are in the convert set.

text_print(convert)  # {'Cat', 'Dog', 'Fish', 'Bird'}

# Let's turn the converted set into a sorted out converted list by casting
# it with the list() function, and then using the sorted() function to sort
# the values. Now we have no more duplicates in our converted, sorted
# list, that was an immutable tuple.

reconvert = cast_to_list(convert)

sort_values = sorted_values(reconvert)

# Check to see how many values there are in the sort_values list.

text_print(sort_values)  # ['Bird', 'Cat', 'Dog', 'Fish']

# Let's check the length of the sort_values list values with the len(),
# length function to know how many values there are.

text_print('You have',value_length(sort_values),'values:')  # You have 4 values:

# Call a sort_value list value by its index[] number.

text_print('I love my',sort_values[0],'so much...')

text_print('I love my',sort_values[1],'so much...')

text_print('I love my',sort_values[2],'so much...')

text_print('I love my',sort_values[3],'so much...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a dictionary with the dict() dictionary function.

dictionary = create_dictionary(key1='Value One',key2='Value Two',key3='Value Three')

# Check to see how many keys and values there are in the dictionary.

text_print(dictionary)  # {'key1': 'Value One', 'key2': 'Value Two', 'key3': 'Value Three'}

# Check to see how many keys there are in the dictionary.

for key,value in dictionary.items():text_print(key)

# Check to see how many values there are in the dictionary.

for key,value in dictionary.items():text_print(value)

# Check to see how many keys and values there are in the dictionary.

for key,value in dictionary.items():print(key,value)

# Let's call a dictionary value by getting a key.

text_print(dictionary.get('key1'))  # Value One

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs...

"Python Programmer's Glossary Bible"

# By Joseph C. Richardson

# Hello and welcome to the knowledge of programming, with Python. Python
# is an object oriented programming language, such as C++. Python’s object
# oriented programming language makes Python very easy to understand,
# especially if you are coming from another type of computer programming
# language like C++; Python and C++ are very similar to each other. And as a
# matter of fact, Python derived from C++. However, with object oriented
# programming languages, there are no line numbers to type and there are no
# such things as ‘gosub’ or ‘goto’ commands. Instead, Python uses ‘functions’
# to call for subroutines. Functions can also do much more than simply call for
# subroutines; we will get into functions later. Python is very picky about how
# you place your programming statements. Python executes/runs its programs
# from the top of the programming list, downward. If you don’t have some
# program statements on the right line of the program list, then Python will bypass
# those commands, or even execute them at the wrong time. It’s very important
# on how you type your Python programs. One other thing Python is very, very
# picky about, with Python programming it is imperative to properly ‘indent’ your
# code; you may need some practice to get comfortable with how to properly
# indent your code, without creating indentation errors and not knowing why. To
# remedy such unwanted indentation errors from occurring, simply press the
# ‘ENTER’ key after each line of code you type. The cursor will automatically indent
# for you on the next line; all you do is type your code and let the cursor do the
# indents for you each time you press the ‘ENTER’ key. Note: all indentations
# must be exactly in-line, or an ‘unexpected indent syntax error’ dialog box will occur.
# See example below:

# Here are some examples of line-indentations in Python, which always proceeds
# right after the use of a colon (:). For example, consider the following with yellow
# highlighted colons (:) showing where they are.
'''
for key,value in dictionary_list.items():
    print(key,value[0])

def my_second_function():
    print('My second function.')

class Dunder_str:
    def __init__(self,num1,num2):
        self.num1 = num1

while True:
    while True:
        os.system('cls')

if Boole == True:
    if not Boole:
        print(Boole)
'''
# For those such as myself, who are quite new to object oriented programming, it takes
# about a good year or more to fully start to understand it. But with a little bit of practice
# and patience each and every single day, your Python programming skills will get sharper
# as you learn. You will make all kinds of mistakes along the way, but that’s also part of
# learning anything new. So let’s get started and take the journey into the knowledge of
# Python Object Oriented Programming Language with my "Python Programmer's Glossary
# Bible". Because great programming always starts with a great programmer’s manual.

# Tips & Tricks for Novice Programmers:

# For those who are very new to programming, here are some very important things to keep
# in mind. When writing programs always create nice, clean and meaningful code; don’t create
# strings that are hard to understand. For example, create a string like this: name = ‘Jim’, not
# like this: n = ‘Jim’. Use meaningful names for strings of all types, such as character strings,
# integer strings, including tuples, lists and dictionaries alike. Creating meaningful strings also
# reduces accidental syntax errors from occurring in your programming code. Another very
# important thing to keep in mind is commenting your programming code so that you and other
# programmers, who are sharing the same project will be able to tell what parts of the programming
# code are doing what and such. Comments start with the '#' number sign followed by the
# commented word, or words. For example, # This is a print statement’s string variable ‘name’.
# Here is another example of what a comment might look like, # This loop counts all the items in
# the names list. Comments help the programmer express in meaningful ways how the program
# works and other programmers can easily pick up the pieces when they take over the nightshift.
# Another type of comment is with the use of three single quote marks (''') at the beginning of the
# comment statement and at the end of the comment statement. This type of comment can hold
# complete paragraphs, whereas the '#' comment statement can only hold words on a single line.
# The two examples of comments are as follows:

# This is a comment statement on a single line.
'''
This is a commented paragraph statement, which can hold a complete
paragraph about the program and how it works. You can use as many
lines of commented words as you please.
'''
# Note: comments do not execute/run, while a program is executing or running. Comments are
# ignored by the program; only the programmers know that comments exist within the programming
# code. As you study the "Python Programmer's Glossary Bible", you will constantly notice how
# everything written is in the form of these, two types of comment statements.

# Case Sensitivity:

# Case sensitivity in programming of every kind is very important to understand. This means that
# text must be typed correctly. For example, if you type a string's variable name with a capital letter,
# then you will also have to keep using that string's variable name with a capital letter. Likewise, if
# you type a string's variable name with a small letter, then you will also have to keep using that
# string's variable name with a small letter. However, programmers understand case sensitivity as
# 'Uppercase' and 'Lowercase', which simply means 'Caps and Non-Caps.

# For example, take a close look at these two string variable names. (A = 'Value') and (a = 'Value').
# Both of these strings are exactly the same, but with one exception, the variable name 'A' is also
# shown as 'a' in the other string variable name example. To gain a much better understanding of
# case sensitivity in programming, here are two examples of yellow, highlighted string variable
# names, which involve case sensitivity in the Python code. For example, consider the following:

# Correct case sensitivity:

A = 'Value'
print(A)

a = 'Value'
print(a)

# Incorrect case sensitivity

A = 'Value'
print(a)

a = 'Value'
print(A)

# If you take a close look at these two Python program examples below, you will clearly see how
# case sensitivity works. Both variable names are of the letter 'A' and 'a', but Python thinks they
# are different variable names that belong to different values. So it's very important that you
# always keep string variable names with different, unique letters to avoid any potential naming
# errors, which may occur, such as in these two illustrated Python program examples below.

A = " I'm the Value for uppercase A "
print(A)

a = " I'm the Value for lowercase a "
print(a)

# However, case sensitivity doesn't stop at string variable names alone, input statements are
# also governed by case sensitivity, so are classes and functions alike. Some Python commands
# start with an uppercase letter, such as 'Canvas, Label, Entry, Tk(), True, False. And some, such
# as class functions always start with a capital letter in the variable name as a standard, but
# lowercase letters can also be used in class variable names as well. Note: most, basic string
# variable names are usually written as lowercase letters as a standard, but uppercase letters can
# also be written as well.

# DRY (Don't Repeat Yourself)

# When it comes to programming, especially those who are brand new to programming will often
# write repetitious code, without realizing it. Repetitious code simply means using the same code,
# or command statements over and over again. For example, consider the following:

# Don't Repeat Yourself!

print("Hello Sun!")
print("Hello Moon!")
print("Hello Stars!")
print("Hello World!")

# Keep it DRY!

words_tuple = ("Hello Sun!","Hello Moon!","Hello Stars!","Hello World!")

for words in words_tuple:
    print(words)

# Single-Line Multiple Command Statements:

#Python supports single-line multiple command statements, which means most command statements
# can be written on the same line using commas (,) as command-line separators. For example,
# consider the following:

print("Hello Sun!")
print("Hello Moon!")
print("Hello Stars!")
print("Hello World!")

print("Hello Sun!"),print("Hello Moon!"),print("Hello Stars!"),print("Hello World!")

# Python supports single-line multiple strings, which means multiple strings can be written on the
# same line using semicolons (;) as string separators. For example, consider the following:

string_1 = ' "Python'
string_2 = "Programmer's"
string_3 = 'Glossary'
string_4 = 'Bible" '

string_1 = ' "Python';string_2 = "Programmer's";string_3 = 'Glossary';string_4 = 'Bible" '

print(string_1,string_2,string_3,string_4)

# Python supports single-line multiple import function statements, which means multiple import
# function statements can be written on the same line using semicolons (;) as import function
# statement separators. For example, consider the following:

import os
import time
import math
from math import*
import winsound

import os;import time;import math;from math import*;import winsound

import os,time,math,winsound;from math import*

# Note: to keep things simple, especially for the novice programmer, all program statements
# and program examples will remain on separate command lines. To the novice programmer,
# this is especially important to be able to mitigate any programming errors, which will occur
# from time to time as you write programs, especially complex programs. However, it is good
# practice to keep nice, neat program code on separate command lines to make it easy to
# understand; professional programmers prefer such.

# Writing Dirty Code Programming:

# Now, let's talk 'dirty'. I mean, let's talk about 'dirty code programming' and why you shouldn't
# do it. What dirty code programming simply means, is how you write it. For example, if you
# create a print string that looks like this:

d = 'dirty';c = 'code';p = 'Programming';print(d,c,p,'is very hard to understand!')

# As you can see, dirty code programming makes it very hard to understand what's happening
# in the program. Now consider the following:

program = 'Programming'
nice = 'Nice,'
clean = 'Clean'
code = 'Code'

print(program,nice,clean,code,'is much easier to understand.')

# Here is another example of clean code programming, using semicolons (;) to separate strings
# on the same line.

program = 'Programming';nice = 'Nice,';clean = 'Clean';code = 'Code.'

print(program,nice,clean,code,'is much easier to understand.')

# Notice how both program examples are very easy to understand, whereas the dirty code program
# example is very hard to understand. Also notice how it's less likely to create text errors and syntax
# errors using a clean code programming style approach, whereas dirty code leaves programs
# vulnerable to text errors and syntax errors alike. Now that you have a general idea of what Python
# programming is all about, let's get started with some simple 'print' statement program examples.

# Print Statement Examples:

# Print statement values are encased with round brackets '()' on each end of the 'print' statement
# value. Quotation marks (" ") denote what kind of 'print' statement value it is. If the value is a string,
# then no quotation marks are used inside the 'print' statement value. However, quotation marks
# are used within the 'print' statement string value instead. Note: double quotation marks (" ") or
# single quotation marks (' ') can be used in 'print' statements, string values, tuples and lists alike.
# If the value is not a string, then quotation marks are used inside the 'print' statement value itself,
# such as these two 'print' statement examples below.

# Print statement examples:

# Double Quotation marks (" ")

print("Hello World!")

# Single Quotation marks (' ')

print('Hello World!')

# Print statement string examples:

# Double Quotation marks (" ")

my_string_example = "Hello World!"

print(my_string_example)

# Single Quotation marks (' ')

my_string_example = 'Hello World!'

print(my_string_example)

# Fancy Print Statement Examples:

# All 'print' statements and all 'input' statements also support the '\n' line-break implementer, which
# acts like a normal line-break in between sentences. The '\n' line-break implementer can also be
# implemented into string values, tuple values and list values alike. From here on, the '\n' line-break
# implementer will be implemented into all 'print' statements, 'input' statements, string values, tuple
# values and list values. The '\n' line-break implementer makes the screen printout much more
# cleaner and nicer looking with actual line-breaks in between sentences. Note: two '\n\n' or more
# '\n\n\n' line-break implementers can be implemented at once within a single 'print' statement.

# Here are some 'print' statement examples of the '\n' line-break
# implementer.

print('\nHello World!')

print('\n\nHello World!')

print('\n\n\nHello World!')

print('\n\n\n\nHello World!')

print('Hello world!\nHello world!\nHello world!\nHello world!')

# The upper() function turns the words 'hello world!'
# into the words 'HELLO WORLD!' example:

print('\nhello world!'.upper())

# The title() function turns the words 'hello world!'
# into the words 'Hello World!' example:

print('\nhello world!'.title())

# The lower() function turns the words 'HELLO WORLD!'
# into the words 'hello world!' example:

print('\nHELLO WORLD!'.lower())

# Make 'print' statement values in reverse by omitting
# the slice '[::]' emitter.

print('\nHello World!'[::-1])

# Try these 'print' statement value in reverse program
# examples, while using other combined functions.

print('\nhello world!'[::-1].upper())

print('\nhello world!'[::-1].title())

print('\nHELLO WORLD!'[::-1].lower())

# The slice [::] emitter can be omitted into tuples, lists, dictionaries
# and 'print' statements, such as in these 'print' statement program
# examples:

# The slice [::] emitter takes one to three positive or negative values.
# The 'print' statement string value 'HELLO WORLD!' is sliced.
# When slicing a 'print' statement string value, the values can be
# sliced from left to right, or from right to left. For example, the 'print'
# string value 'HELLO WORLD!' looks like these sliced 'print' string
# value examples:

#	0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#	H,E,L,L,O, ,W,O,L,R,D,!

#	-12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
#	H,E,L,L,O, ,W,O,L,R,D,!

# [ start value : end value : step value ]

# Note: step values must start at 1 not 0

# empty slice: no values

print('HELLO WORLD!'[:])

# Screen output:	HELLO WORLD!

# slice start value 0

print('HELLO WORLD!'[0:])

# Screen output:	HELLO WORLD!

# slice end value -1

print('HELLO WORLD! '[:-1])

# Screen output:	HELLO WORLD!

# slice start and slice end values 1 and -2

print('HELLO WORLD! '[1:-2])

# Screen output:	ELLO WORLD

# slice start, slice end and slice step 2

print('HELLO WORLD!'[0:-1:2])

# Screen output:	HLOWRD

# In this example, the start and end slice emitter values are
# positive. Notice how the screen output shows 'HE'.

# slice start and slice end values 0 and 2

print('HELLO WORLD! '[0:2])

# Screen output:	HE

# In this example, the start and end slice emitter values are
# negative. Notice how the screen output shows 'D!'.

# slice start and slice end values -3 and -1

print('HELLO WORLD! '[-3:-1])

# Screen output:	D!

# Make this 'print' statement print 'Hello World!' 3 times.

print('Hello World! '*3)

# Make this 'print' statement print 'Hello World!' go in the top,
# middle of the screen. Note: use an empty space in between
# the single quotation marks (' '*45)

print(' '*45+'Hello World!')

# Try these 'print' statement program examples:

print('Hello World! '*3+'Python')

print('Python '*3+'Hello World!')

print('Python '*45+'Hello World!')

print('Python '*45)

# The 'len' function counts how many characters, including spaces
# there are inside of a 'print' statement. The length of these two words
# "Hello World!", including the space in between 'Hello' and 'World!'
# are counted. For example: "Hello World!" including one space is
# twelve characters long. The printout on the screen will only# show
# the number "12", not the actual words "Hello World!".

print(len('Hello World!'))

# Character Strings:

character_string_example = '\nHello World!'

print(character_string_example)


# Character stings can be any name, letters or letters combined with numbers, starting with a
# letter first and then a number afterwards. Note: character strings must have different, unique
# names assigned to them. Also note: character strings cannot contain numbers alone as
# character strings; a "can't assign to literal" error will occur. Character strings must be one,
# whole word only. Use the underscore key to make two or more words. Example: use
# 'character_string_example', instead of using 'characterstringexample'. Character strings
# cannot contain two or more separate words with spaces in between them. Example: 'character
# string example' cannot be used as a string, but 'character_string_example' can be used as a
# string.

# Character strings are used to hold important, key data information, which can be used over
# again and again throughout a program's execution/run. Using character strings also makes
# programming code very efficient, without manual redundancy on the programmer's part.

# Character String Variable Name Change Examples:

animal_canine = 'Fox'
animal_name = 'Ed'
animal_age = '19'

print(f'\n{animal_name} the crazy {animal_canine} is {animal_age} years old.')

animal = 'Fox'
name = 'Ed'
age = '19'

print(f'\n{name} the crazy {animal} is {age} years old.')

animal1 = 'Fox'
name1 = 'Ed'
age1 = '19'

print(f'\n{name1} the crazy {animal1} is {age1} years old.')

a = 'Fox'
n = 'Ed'
age = '19'

print(f'\n{n} the crazy {a} is {age} years old.')

a1a = 'Fox'
n2n = 'Ed'
a55a = '19'

print(f'\n{n2n} the crazy {a1a} is {a55a} years old.')

# Replace part of a string's value 'Ed the Fox is great!'
# with 'Ed the Canine is great!' example:

list_string_name = '\nEd the Fox is great!'
my_replace_word = list_string_name.replace('Fox','Canine')

print(my_replace_word)

# Numeric Strings:

# Numeric strings can be any name, letters or letters combined with numbers, starting with a
# letter first and then a number afterwards. Numeric strings do not contain quote ('') marks
# around the values, like character strings do. Note: numeric strings must have different,
# unique names assigned to them. Note: numeric strings cannot contain numbers alone as
# numeric strings; a "can't assign to literal" error will occur. Numeric strings must be one,
# whole word only. Use the underscore key to make two or more words. Example: use
# 'numeric_string_example', instead of using 'numericstringexample'. Numeric strings cannot
# contain two or more separate words with spaces in between them. Example: 'numeric string
# example' cannot be used as a string, but 'numeric_string_example' can be used as a string.

# Numeric strings are used to hold important, key data information, which can be used over
# again and again throughout a program's execution run. Using numeric strings also makes
# programming code very efficient, without manual redundancy on the programmer's part.

# Numeric strings do not contain quote ('') marks, because they are not character strings.
# Numeric strings have to be able to do actual calculations throughout a program’s execution
# run.

# Numeric String Examples:

# BEDMAS! Order of Operation:

# All computers, and computer programs, which involve
# mathematics dictate the order of operation. BEDMAS:

# (Brackets)
# (Exponents)
# (Division)
# (Multiplication)
# (Addition)
# (Subtraction)

numeric_string1 = 3;numeric_string2 = 5

print(numeric_string1+numeric_string2*2+2)

# 5*2 = 10, 3+10+2 = 15

print(3+5*2+2)

# 3+10+2 = 15

num1 = 3
num2 = 5

print(num1+num2*2+2)

num1 = 3
num2 = 5
num3 = 2

print(num1+num2*num3+num3)

# num2*num3 = 10, num1+num2+num3 = 15

# Numbers can also used within the 'print' statement example
# as follows:

print('\nAlbert Einstein loves to count to',3+5*2+2,'using the order of operation.')

# New format example of the 'input' 'print' string statement:
# Note: the (f') format is now the standard in Python 3 and up.

num1 = 3
num2 = 5
num3 = 2

print(f'\nAlbert Einstein loves to count to \
{num1+num2*num3+num3} using the order of operation.')

# Non format example of the 'print' numeric string statement:

num1 = 3
num2 = 5
num3 = 2

print('\nAlbert Einstein loves to count to',(num1+num2*num3+num3),
      'using the order of operation.')

# Old format example of the 'print' numeric string statement:
# Now depreciated in Python 3 and up.

num1 = 3
num2 = 5
num3 = 2

print('\nAlbert Einstein loves to count to {} \
using the order of operation.'.format(num1+num2*num3+num3))

# String Concatenation:

# Strings such as character strings and numeric strings can be concatenated or joined together,
# using the comma ',' or the plus sign '+'. Note: string concatenation is only needed in non-formatted
# command statements. However, with the 'f' format function, there is no need for string concatenation.
# Consider the following:

numeric_string = 2+2*4
character_string = 'printed text.'

print('Numeric string calculation',
      str(numeric_string),'mixed in with',character_string)
'''--------------------------------------------------------------------------------------------'''
numeric_string = 2+2*4
character_string = 'printed text.'

print('Numeric string calculation '
      +str(numeric_string)+' mixed in with '+character_string)
'''--------------------------------------------------------------------------------------------'''
numeric_string = 2+2*4
character_string = 'printed text.'

print(f'Numeric string calculation {str(numeric_string)} \
mixed in with {character_string}')
'''--------------------------------------------------------------------------------------------'''
numeric_string = 2+2*4
character_string = 'printed text.'

print('Numeric string calculation {} \
mixed in with {}'.format(str(numeric_string),character_string))
'''--------------------------------------------------------------------------------------------'''
# Notice how the 'f' format function and the old format command statements have no, such commas
# ',' or plus signs '+' needed for string concatenation. Curly braces '{}' are all that are needed for string
# concatenation, which makes it much simpler for the programmer in the long run.

# Here are some string concatenation program examples to
# practice with. See what happens when you type and execute/
# run each of these program examples below.

numeric_string = 2+2*4
character_string = 'printed text.'

print('Numeric string calculation '
      +str(numeric_string)+' mixed in with '+character_string)

numeric_string = str(2+2*4)
character_string = 'printed text.'

print('Numeric string calculation '
      +(numeric_string)+' mixed in with '+character_string)

numeric_string = 2+2*4
character_string = 'printed text.'

print('Numeric string calculation',
      str(numeric_string),'mixed in with',character_string)

numeric_string = str(2+2*4)
character_string = 'printed text.'

print('Numeric string calculation',
      (numeric_string),'mixed in with',character_string)

numeric_string = 2+2*4
character_string = 'printed text.'

print(f'Numeric string calculation {str(numeric_string)} \
mixed in with {character_string}')

numeric_string = str(2+2*4)
character_string = 'printed text.'

print(f'Numeric string calculation {numeric_string} \
mixed in with {character_string}')

numeric_string = 2+2*4
character_string = 'printed text.'

print('Numeric string calculation {} \
mixed in with {}'.format(str(numeric_string),character_string))

numeric_string = str(2+2*4)
character_string = 'printed text.'

print('Numeric string calculation {} \
mixed in with {}'.format(numeric_string,character_string))

# Let's have some fun with string concatenation. See what happens
# when you type and execute/run these program examples below.

p1 = ' "Pyt';p2 = 'hon';p3 = 'Pro';p4 = 'gram'
p5 = "mer's";p6 = 'Glos';p7 = 'sary';p8 = 'Bib';p9 = 'le" '

print(p1+p2,p3+p4+p5,p6+p7,p8+p9,'\nBy Joseph C. Richardson')

# When commas ',' are used, they act as spaces in between strings.
# However, when plus signs '+' are used, there are no spaces in
# between strings. When using a plus sign '+' it is important to create
# spaces in the values themselves, example. p3 = ' Pro'.

p1 = ' "Pyt';p2 = 'hon';p3 = ' Pro';p4 = 'gram'
p5 = "mer's";p6 = ' Glos';p7 = 'sary';p8 = ' Bib';p9 = 'le" '

print(p1+p2+p3+p4+p5+p6+p7+p8+p9+'\nBy Joseph C. Richardson')

# Tuple String Examples:

# Tuples are strings that can hold multiple values. Tuples are immutable, meaning they cannot be
# changed or modified once they are created. Tuple values are surrounded with round brackets '( )'.
# Tuple values always start at position '0', then position '1', and so on.

# Example: tuple_string_name = ('Position 0','Position 1','Position 2')
# Tuple string examples are as follows.
# Non format example of the 'print' tuple string:

tuple_string_name = ('Superman','Batman','Spiderman')

print('\nMy name is '+(tuple_string_name[0])+' and I\'m a SuperHero.')

print('\nMy name is '+(tuple_string_name[1])+' and I\'m a SuperHero.')

print('\nMy name is '+(tuple_string_name[2])+' and I\'m a SuperHero.')

# New format example of the 'print' tuple string: Note:
# the (f') format is now the standard in Python 3 and up.

tuple_string_name = ('Superman','Batman','Spiderman')

print(f'\nMy name is {tuple_string_name[0]} and I\'m a SuperHero.')

print(f'\nMy name is {tuple_string_name[1]} and I\'m a SuperHero.')

print(f'\nMy name is {tuple_string_name[2]} and I\'m a SuperHero.')

# Old format example of the 'print' tuple string:
# Now depreciated in Python 3 and up.

tuple_string_name = ('Superman','Batman','Spiderman')

print('\nMy name is {} and I\'m a SuperHero.'.format(tuple_string_name[0]))

print('\nMy name is {} and I\'m a SuperHero.'.format(tuple_string_name[1]))

print('\nMy name is {} and I\'m a SuperHero.'.format(tuple_string_name[2]))

# Call up individual tuple values with the slice [::] emitter.

tuple_string = ('Python','Programmer\'s','Glossary','Bible')

print(f' "{tuple_string[0]} {tuple_string[1]} {tuple_string[2]} {tuple_string[3]}" ')

# Loop through a tuple string with a for-loop.

tuple_string = ('Python','Programmer\'s','Glossary','Bible')
for i in tuple_string:
    print(i)

# This tuple program example omits the 'min' and 'max' functions
# for each tuple set: 'min_num', and 'max_num'. The 'add_values'
# variable adds min_num and max_num' tuple values together
# which equals 11.

min_num = min(1,2,3,4,5,6,7,8,9,10)
max_num = max(1,2,3,4,5,6,7,8,9,10)
add_values = min_num+max_num

print(f'Numbers: (1,2,3,4,5,6,7,8,9,10)\n\nMinimum \
number = {min_num}\nMaximum number = {max_num}\n\nMinimum \
number plus maximum number={add_values}')

# Screen output:	Numbers: (1,2,3,4,5,6,7,8,9,10)

# 			Minimum number = 1
# 			Maximum number = 10

# 			Minimum number plus maximum number = 11

# Create a tuple list with an 'IndexError' handler. If a value is not
# found, then the 'try' and 'except IndexError' handler will execute.
# If a value is found, the 'try' and 'except IndexError' handler are
# ignored, but the 'finally' statement will always execute no matter
# the outcome.

tuple_list = (
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    )

try:
    print(tuple_list[16])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

# List String Examples:

# Lists are strings that can hold multiple values. Lists are mutable, meaning they can be changed
# or modified once they are created. List values are surrounded with square brackets '[ ]'. List values
# always start at position '0', then position '1', and so on.

# Example: list_string_name = ['Position 0','Position 1','Position 2']

# List string examples are as follows.

# Non format example of the 'print' list string:

list_string_name = ['Superman','Batman','Spiderman']

print('\nMy name is '+(list_string_name[0])+' and I\'m a SuperHero.')

print('\nMy name is '+(list_string_name[1])+' and I\'m a SuperHero.')

print('\nMy name is '+(list_string_name[2])+' and I\'m a SuperHero.')

# New format example of the 'print' list string: Note: the (f') format
# is now the standard in Python 3 and up.

list_string_name = ['Superman','Batman','Spiderman']

print(f'\nMy name is {list_string_name[0]} and I\'m a SuperHero.')

print(f'\nMy name is {list_string_name[1]} and I\'m a SuperHero.')

print(f'\nMy name is {list_string_name[2]} and I\'m a SuperHero.')

# Old format example of the 'print' list string: Now depreciated
# in Python 3 and up.

list_string_name = ['Superman','Batman','Spiderman']

print('\nMy name is {} and I\'m a SuperHero.'.format(list_string_name[0]))

print('\nMy name is {} and I\'m a SuperHero.'.format(list_string_name[1]))

print('\nMy name is {} and I\'m a SuperHero.'.format(list_string_name[2]))

# Loop through a list string with a for-loop.

list_string = ['Python','Programmer\'s','Glossary','Bible']
for i in list_string:
    print(i)

# List String Modification Examples:

# A list can always be changed or modified, but a tuple cannot
# be changed or modified. List values are mutable, whereas tuple
# values are immutable. The extra list value: 'Wonder Woman' is
# now appended or added to the string's name range: list_string_
# name.

list_string_name = ['Superman','Batman','Spiderman']
list_string_name.append('Wonder Woman')

print(f'\nMy name is {list_string_name[2]} and I\'m a SuperHero.')

# The inserted list value: 'The Tick' is now at position '0' where
# the list value: 'Superman' was. The list value: 'Superman' got
# moved from position'0' into position '1' instead.

list_string_name = ['Superman','Batman','Spiderman']
list_string_name.insert(0,'The Tick')

print(f'\nMy name is {list_string_name[1]} and I\'m a SuperHero.')

# The removed list value: 'Spiderman' is gone from the string's
# name range: list_string_name. Position '0', and position '1' are
# all that is left in the string's name range: list_string_name.

list_string_name = ['Superman','Batman','Spiderman']
list_string_name.remove('Spiderman')

print(f'\nMy name is {list_string_name[1]} and I\'m a SuperHero.')

# The popped list value: 'Superman' at position '0' is now 'Batman'
# at position '0', where the value 'Superman' was.

list_string_name = ['Superman','Batman','Spiderman']
list_string_name.pop(0)

print(f'\nMy name is {list_string_name[0]} and I\'m a SuperHero.')

# The sort list values: 'Superman','Batman','Spiderman' get reversed
# as list values: 'Superman','Spiderman','Batman'. The sort list value
# 'Superman' remains at position '0', while the other two values get
# reversed positions.

list_string_name = ['Superman','Batman','Spiderman']
list_string_name.sort(reverse = True)

print(f'\nMy name is {list_string_name[1]} and I\'m a SuperHero.')

# Note: the sorted list program example below only returns a
# preview of what the list would look like if it was sorted; it
# doesn't modify or change the actual characteristics of the list.

sorted(list_string_name)
print(list_string_name)

# Create a single list with an 'IndexError' handler. If a value is not
# found, then the 'try' and 'except IndexError' handler will execute.
# If a value is found, the 'try' and 'except IndexError' handler are
# ignored, but the 'finally' statement will always execute no matter
# the outcome.

single_list = [
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

try:
    print(single_list[16])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

# Extend the single_list1 and the single_list2 with the '.extend()'
# function. Once again, If a value is not found, then the 'try' and
# 'except IndexError' handler will execute. If a value is found, the
# 'try' and 'except IndexError' handler are ignored, but the 'finally'
# statement will always execute no matter the outcome.

single_list1 = [
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

single_list2 = [
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

single_list1.extend(single_list2)

try:
    print(single_list1[32])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

# Two Dimensional List Examples:

# A two dimensional list is simply a list within another list.
# For example, a one dimensional list looks like this:

my_1d_list = ['value 1','value 2']

# A two dimensional list looks like this:

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

# A two dimensional list can hold as many list value blocks as one
# sees fit. For example: the my_2d_list variable has three list value
# blocks in it.

my_2d_list = [['value 1','value 2'],['value 3','value 4'],['value 5','value 6']]

# A two dimensional list can be numeric values as well as character
# values. Example:

my_2d_list = [[1,2],[3,4]]

# Display a two dimensional list's character values to check them.

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

print(my_2d_list)

# Screen output:	[['value 1', 'value 2'], ['value 3', 'value 4']]

# Display a two dimensional list's numeric values to check them.

my_2d_list = [[1,2],[3,4]]

print(my_2d_list)

# Screen output:	[[1, 2], [3, 4]]

# Display a two dimensional list's character value pair to check them.

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

print(my_2d_list[0])

# Screen output:	['value 1', 'value 2']

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

print(my_2d_list[1])

# Screen output:	['value 3', 'value 4']

# Display a two dimensional list's numeric value pair to check them.

my_2d_list = [[1,2],[3,4]]

print(my_2d_list[0])

# Screen output:	[1, 2]

my_2d_list = [[1,2],[3,4]]

print(my_2d_list[1])

# Screen output:	[3, 4]

# Display a single character value from a two dimensional list.
# Examples:

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

print(my_2d_list[0][0])

# Screen output:	value 1

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

print(my_2d_list[1][0])

# Screen output:	value 3

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

print(my_2d_list[0][1])

# Screen output:	value 2

my_2d_list = [['value 1','value 2'],['value 3','value 4']]

print(my_2d_list[1][1])

# Screen output:	value 4

# Display a single numeric value from a two dimensional list.
# Examples:

my_2d_list = [[1,2],[3,4]]

print(my_2d_list[0][0])

# Screen output:	1

my_2d_list = [[1,2],[3,4]]

print(my_2d_list[1][0])

# Screen output:	3

my_2d_list = [[1,2],[3,4]]

print(my_2d_list[0][1])

# Screen output:	2

my_2d_list = [[1,2],[3,4]]

print(my_2d_list[1][1])

# Screen output:	4

# Create a multiple two dimensional list, using letter and
# number values. Create a simple 'print' program example,
# which will use a two dimensional list.

name = [
     ['Tomy','Brian','Jim','Paul'],
     ['Mary','Terry','Jane','Patty'],
     [0,1,2,35,4,5,6,7,8,9],
     ['Dog','Cat','Bird','Fish']
     ]

print(f'My name is {name[0][0]} I am {name[2][3]} years old.')

print(f'I have a {name[3][0]}. My Sister {name[1][3]} wants a {name[3][2]}.')

print(f'{name[1][0]} loves {name[3][3]} so much. But {name[0][1]} \
wants a {name[3][1]} instead.')

# Create a multi dimensional list with an 'IndexError' handler.
# If a value is not found, then the 'try' and 'except IndexError'
# handler will execute. If a value is found, the 'try' and 'except
# IndexError' handler are ignored, but the 'finally' statement
# will always execute no matter the outcome.

multi_dim_list = [
    ['Value pos:0','Value pos:1','Value pos:2','Value pos:3'],
    ['Value pos:4','Value pos:5','Value pos:6','Value pos:7'],
    ['Value pos:8','Value pos:9','Value pos:10','Value pos:11'],
    ['Value pos:12','Value pos:13','Value pos:14','Value pos:15']
    ]

try:
    print(multi_dim_list[0][4])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

# Multiple String Variables and Multiple String Values Examples:

# Multiple tuple string variables and multiple tuple values can be stored right inside one,
# single 'print' statement. Note: multiple tuple strings and multiple tuple values must be
# the same; four tuple strings equals four tuple values. Also note that multiple tuple stings
# and multiple tuple values are always in the order they are given. For example, string (a)
# is always equal to the string value 'Andy' and string (b) is always equal to the string value
#'Bob' and so on.

# Multiple tuple string variables and multiple tuple values example:

a,b,c,d = ('Andy','Bob','Chris','Dave')

print(a,b,c,d)

print(d,c,b,a)

print(c,b,a,d)

# The 'len' function is excellent at keeping track of how many tuple
# values or list values there are. Checking to see how many values
# there are in a tuple or list makes programming much more efficient,
# while the 'len' function checks exactly how many values there are.
# The printout on the screen will only show the number "8", not the
# actual tuple values or list values.

tuple_len = (
     'Value 0','Value 1',
     'Value 2','Value 3',
     'Value 4','Value 5',
     'Value 6','Value 7'
     )

print(len(tuple_len))

list_len = [
    'Value 0','Value 1',
    'Value 2','Value 3',
    'Value 4','Value 5',
    'Value 6','Value 7'
    ]

print(len(list_len))

#Dictionary Examples:

# Dictionaries are like lists, but they hold "key" values that point to other values in the list.
# For example: the key value "animal" points to the list value "canine", and the key value
# "name" points to the list value "Mogie". The key value "age" points to the list value "13",
# and the key value "kind" points to the value "Husky/Chow mix". Lastly, the key value
# "colour" points to the list value "gold". Think of dictionaries as lists on heavy steroids.
# Dictionary values are surrounded with curly braces '{ }', which are also surrounded with
# round brackets '({ })'. Note: you can leave out the round brackets '()' if you like, but in
# some cases it's necessary that you have them, like these examples below illustrate.

# Type and execute/run this 'dictionary_list' dictionary program example:

dictionary_list = (
     {'animal':'canine',
      'name':'Mogie','age':13,
      'kind':'Husky/Chow mix',
      'colour':'gold'}
     )

print(dictionary_list['animal'])

print(dictionary_list['name'])

print(dictionary_list['age'])

print(dictionary_list['kind'])

print(dictionary_list['colour'])

# Update the dictionary_list values with the '.update' statement
# followed by the new dictionary_list:

# dictionary_list.update({'animal':'monkey','name':'Cheetah',
# 'age':20,'kind':'Chimpanzee','colour':'brown'})

dictionary_list = (
     {'animal':'canine','name':'Mogie','age':13,
      'kind':'Husky/Chow mix','colour':'gold'}
     )

dictionary_list.update(
     {'animal':'monkey','name':'Cheetah','age':20,'kind':'Chimpanzee','colour':'brown'}
     )

print(dictionary_list['animal'])

print(dictionary_list['name'])

print(dictionary_list['age'])

print(dictionary_list['colour'])

# This dictionary_list example illustrates how key values can point to
# multiple values, denoted by square brackets '[ ]' around the list value
# groups. For example: the key value 'Animals' has four list values
# assigned to it instead of just one list value, such as in the dictionary_
# list program example above illustrates.

dictionary_list = (
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

print(dictionary_list['Animals'][0])
print(dictionary_list['Animals'][1])
print(dictionary_list['Animals'][2])
print(dictionary_list['Animals'][3])

print(dictionary_list['Reptiles'][0])
print(dictionary_list['Reptiles'][1])
print(dictionary_list['Reptiles'][2])
print(dictionary_list['Reptiles'][3])

print(dictionary_list['Insects'][0])
print(dictionary_list['Insects'][1])
print(dictionary_list['Insects'][2])
print(dictionary_list['Insects'][3])

# Update the dictionary_list values with the '.update' statement
# followed by the new dictionary_list:

# dictionary_list.update({'Animals':['Wolf','Lion','Bat','Shark'],'
# Reptiles':['Tortoise','Alligator','Python','Toad'],'Insects':
# ['Moth','Cricket','Fly','Wasp']})

dictionary_list = (
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

dictionary_list.update(
     {'Animals':['Wolf','Lion','Bat','Shark'],'Reptiles':['Tortoise','Alligator','Python','Toad'],
      'Insects':['Moth','Cricket','Fly','Wasp']}
     )

print(dictionary_list['Animals'][0])
print(dictionary_list['Animals'][1])
print(dictionary_list['Animals'][2])
print(dictionary_list['Animals'][3])

print(dictionary_list['Reptiles'][0])
print(dictionary_list['Reptiles'][1])
print(dictionary_list['Reptiles'][2])
print(dictionary_list['Reptiles'][3])

print(dictionary_list['Insects'][0])
print(dictionary_list['Insects'][1])
print(dictionary_list['Insects'][2])
print(dictionary_list['Insects'][3])

# Display the dictionary key values to check them.

dictionary_list = (
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

print(dictionary_list.keys())

# Screen output:	dict_keys(['Animals', 'Reptiles', 'Insects'])

# Display the dictionary list values to check them.

dictionary_list = (
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

print(dictionary_list.values())

# Screen output:	dict_values([['Dog', 'Cat', 'Bird', 'Fish'],
# ['Turtle','Lizard','Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant',
# 'Bee']])

# Delete a dictionary key value and check it.

dictionary_list = (
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

del dictionary_list['Animals']

print(dictionary_list.keys())

# Screen output:	dict_keys(['Reptiles', 'Insects'])

# Delete a dictionary list value and check it.

dictionary_list = (
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

del dictionary_list['Animals'][0]

print(dictionary_list.values())

# Screen output:	dict_values([['Cat', 'Bird', 'Fish'], ['Turtle',
# 'Lizard','Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant', 'Bee']])

# Pop a dictionary key value and check it. The key value "Animals"
# is not deleted, but it's no longer in the dictionary list. However,
# it is returnable.

dictionary_list = (
     {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
      'Insects':['Butterfly','Beetle','Ant','Bee']}
     )

pop_key = dictionary_list.pop('Animals')

print(dictionary_list.keys())

print(pop_key)

# Screen output:	dict_keys(['Reptiles', 'Insects'])

# Screen output:	['Dog', 'Cat', 'Bird', 'Fish']

# Display the length of dictionary key values to check them.

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(len(dictionary_list))

print(dictionary_list.keys())

# Screen output:	3

# Screen output:	dict_keys(['Animals', 'Reptiles', 'Insects'])

# Display the length of dictionary list values to check them.

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(len(dictionary_list['Animals']))

print(dictionary_list.values())

# Screen output:	4

# Screen output:	dict_values([['Dog', 'Cat', 'Bird', 'Fish'], ['Turtle',
# 'Lizard', 'Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant', 'Bee']])

# To add a new dictionary key value, simply use: ['Set Key name
# example'] = 'New Value' to display the length of dictionary list key
# values to check them. Note: one dictionary value must be created
# along with setting a new dictionary key value.

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

dictionary_list['Fish'] = 'Angelfish'

print(len(dictionary_list.keys()))

print(dictionary_list.keys())

# Screen output:	4

# Screen output:	dict_keys(['Animals', 'Reptiles', 'Insects', 'Fish'])

# To add new dictionary values, simply use: ['Set Key name
# example'] = 'Value','New Value','New Value',New Value' Display
# the length of dictionary list values to check them. Note: a
# dictionary key value must be [set] first, then add the new
# dictionary values.

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

dictionary_list['Fish'] = 'Angelfish','Devilfish','Catfish','Dogfish'

print(len(dictionary_list.values()))

print(dictionary_list.values())

# Screen output:	4

# Screen output:	dict_values([['Dog', 'Cat', 'Bird', 'Fish'],
# ['Turtle','Lizard', 'Snake', 'Frog'], ['Butterfly', 'Beetle', 'Ant',
# 'Bee'], ('Angelfish','Devilfish', 'Catfish', 'Dogfish')])

# To look for a dictionary key value, simply use the '.get' method
# to search for it. Display the dictionary key values to check them.

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(dictionary_list.get('Fish'))

# Screen output:	None

# The screen output says None. However, by adding
# 'Not Found!' the screen output now looks like this:

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(dictionary_list.get('Fish','Not Found!'))

# Screen output:	Not Found!

# This time, let's look for an actual key value and check it,
# using the 'get' method. The screen output now looks like this:

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

print(dictionary_list.get('Animals'))

# Screen output:	['Dog', 'Cat', 'Bird', 'Fish']

# Create a dictionary with a 'KeyError' handler. If a value is not
# found, then the 'try' and 'except KeyError' handler will execute.
# If a value is found, the 'try' and 'except KeyError' handler are
# ignored, but the 'finally' statement will always execute no matter
# the outcome.

dict_key = {
    'key:0':'Value:0','key:1':'Value:1',
    'key:2':'Value:2','key:3':'Value:3',
    'key:4':'Value:4','key:5':'Value:5'
    }

try:
    print(dict_key['key:6'])
except KeyError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')

# The '.get()' function does exactly the same thing as the 'try' and
# 'except KeyError' handler does. However, the '.get()' function
# works with dictionaries only.

dict_key = {
    'key:0':'value:0','key:1':'value:1',
    'key:2':'value:2','key:3':'value:3',
    'key:4':'value:4','key:5':'value:5'
    }

print(dict_key.get('key:6','Value not found.'))

# The '.update({})' function updates the dictionary's keys and values
# alike. Notice how the '.get()' function is still being used instead of
# the 'try' and 'except KeyError' handler. However, in some cases it's
# a good idea to use error handlers.

dict_key.update({
    'key:0':'New value','key:1':'value:1',
    'key:2':'value:2','key:3':'value:3',
    'key:4':'value:4','key:5':'value:5'
    })

print(dict_key.get('key:0','Value not found.'))

# Conditionals and Logical Operators: (<) (>) (<=) (>=) (==) (!=)

# Conditionals change the outcome of a program's execution run, depending on what the
# program is doing at the time. The conditionals in Python are the 'if:' statement, 'elif:'
# statement and the 'else:' statement, along with the 'True:' and 'False:' statements.
# Conditionals are mainly used in conjunction with 'input' statements and conditional
# while-loops. However, Logical operators are also used to test whether a condition is less
# than (<), greater than (>), less than (<=) or equal to, greater than (>=) or equal to, equals
# (==) equals and not (!=) equal to. For example, 5 is greater (>) than 4 and 4 is less (<) than
# 5. Here are a few examples of logical operators, which test integer values against other
# integer values within 'print' statements. These 'print' statement illustration examples below
# will either display on the screen output as "True" or "False", depending on the outcome
# of the results.

# print(4 < 5) True: 4 is less than 5
# print(4 >5 ) False: 4 is not greater than 5
# print(4 <= 5) True: 4 is less than or equal to 5
# print(4 >= 5) False: 4 is not greater than or equal to 5
# print(4 == 5) False: 4 does not equal 5
# print(4 != 5) True: 4 does not equal 5

# Type and execute/run this simple 'print' statement program
# example below, using the logical operators in different
# combinations as was illustrated above and see what happens
# when you change the logical operators.

print(4 < 5)

# Screen output:	True

# Type and execute/run these 'print' statement program examples,
# using the (f') format implementer.

# The 'int' statement is for integer values only.

num = int(input('Type in a number and I will condition the result against 5 as either \
"true" or false" ').strip())

print(f'{num < 5}')
print(f'{num > 5}')
print(f'{num <= 5}')
print(f'{num >= 5}')
print(f'{num == 5}')
print(f'{num !=5 }')

# Boolean Logic:

# IF" "ELIF" "ELSE" "TRUE" "FALSE" "AND" "OR" "NOT"

# There once was a man, named 'George Boole' who was a famous mathematician. He
# invented these conditionals called Boolean Logic, which indirectly brought about the
# computer age we now live. The conditionals of George Boole are as follows.

# These conditionals are: 'IF', 'ELSE', 'TRUE', 'FALSE', 'AND', 'OR' 'NOT'

# In computer terminology, these conditionals are called "Boolean Logic". Boolean Logic
# is simply all about the concept of decision making laws, meaning if something is true,
# then it is not false. Likewise, if something is false, then it is not true.

# When it comes to program development, sometimes logical operators aren't enough
# alone to do the job. In most cases, other conditionals are needed to help the logical
# operators do the job. With the 'if:', 'elif:', 'else', 'true', 'false', 'and', 'or' and 'not' conditionals,
# the logical operators can do the job as they were designed for doing, which are to test
# values against other values and comparing data against user input data.

# Using simple 'print' statements, you can do simple True and
# False tests to help you determine the outcome of a conditional
# against another conditional, such as True and False conditionals.
# For example:

print(True and True)
print(False and False)
print(True and False)
print(False and True)

print(True or True)
print(False or False)
print(True or False)
print(False or True)

print(True and not True)
print(False and not False)
print(True and not False)
print(False and not True)

print(True or not True)
print(False or not False)
print(True or not False)
print(False or not True)

print(True is not True)
print(False is not False)
print(True is not False)
print(False is not True)

# Use operators to check to see if a value is True or False.

print(True == True)
print(False == False)
print(True != False)
print(False != True)
print(True >= False)
print(True <= False)

# Here is a prime example of how these conditionals work in
# conjunction with the logical operators. In this program example,
# the conditionals 'if:' and 'elif:' are implemented along with the
# logical operators. The user is asked to type in a number, if the
# number is equal equals: == 5, the first conditional 'if:' statement
# is executed "print(f'True! {num} equals equals 5.')". If the number
# is less than 5, the first 'elif:' statement is executed "print(f'True!
# {num} is less than 5.')". If the number is greater than 5, the second
# 'elif:' statement is executed "print(f'False! {num} is not greater
# than 5.')". If the number is less than or equal to 5, the third 'elif:'
# statement is executed "print(f'True! {num} is less than or equal
# to 5.')". If the number is greater than or equal to 5, the last 'elif:'
# statement is executed "print(f'False! {num} is is not greater than or
# equal to 5.')".

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order
# that Python executes/runs its program statements in the background.

# Type and execute/run this program example below and see what happens.

# The 'int' statement is for integer values only.

num = int(input('Type in a number and I will condition the result against 5 as either \
"true" or false" ').strip())

if num == 5:
    print(f'True! {num} equals equals 5.')

elif num < 5:
    print(f'True! {num} is less than 5.')

elif num > 5:
    print(f'False! {num} is not greater than 5.')

elif num <= 5:
    print(f'True! {num} is less than or equal to 5.')

elif num >= 5:
    print(f'False! {num} is is not greater than or equal to 5.')

# In this program example, the conditional 'else:' statement is
# executed only when the value 5 equals itself. Type and execute/
# run the program below and see what happens.

# The 'int' statement is for integer values only.

integer = int(input("Please enter an integer less than 5 or greater than 5: ").strip())

if integer < 5:
    print(f'{integer} is less than 5')

elif integer > 5:
    print(f'{integer} is greater than 5')

else:
    if integer == 5:
        print(f'True! {integer} equals equals 5.')

# Type and execute/run this program example and change the
# value 'num = 5' to different values, such as 'num = 9', 'num =- 7'.....

num = 6

if num < 5:
    print(f'{num} is less than 5')

elif num > 5:
    print(f'{num} is greater than 5')

else:
    if num == 5:
        print(f'{num} equals equals 5.')

# The conditionals 'True' and 'False' will only be true if both
# conditions are true. They can also be true if both conditionals
# are false. Conditionals cannot be true and false at the same
# time, nor can it be 'yes' and 'no' at the same time. For example,
# if 'True' and 'True' are the same, they equal true. Likewise if
# 'False' and 'False' are the same, they too are equally true.
# However, 'True' and 'False' are not the same, so they are equally
# false. Likewise False' and 'True' are not the same, so they equal
# false as well. Type and execute/run these programs examples
# below.

conditional = False

if conditional == True:
     print('True!')

elif conditional == False:
     print('False!')

conditional = True

if conditional == False:
     print('Both conditions are true!')
     print('True and True equals true.')

else:
     print('Both conditions are false!')
     print('True and False equals False.')

conditional = False

if conditional == True:
     print('Both conditions are true!')
     print('True and True equals true.')

else:
     print('Both conditions are false!')
     print('False and True equals False.')

conditional = True

if conditional == True:
     print('Both conditions are true!')
     print('True and True equals true.')

else:
     print('Both conditions are false!')
     print('True and False equals False.')

conditional = False

if conditional == False:
     print('Both conditions are true!')
     print('False and False equals true.')

else:
     print('Both conditions are false!')
     print('True and False equals False.')

conditional = True

if conditional == True:
     print('True!')

elif conditional == False:
     print('False!')

# This small program example waits for the user to type "True"
# or "False". If the user types 'true', then the 'print' statement
# 'print('True!')' is executed. If the user types 'false', then the
# 'print' statement 'print('False!')' is executed.

conditional = input('Type the words "True" or "False" ').strip()

if conditional == 'true':
     print('True!')

elif conditional == 'false':
     print('False!')

else:
     print('Oops! Wrong keys:')

# This program example waits for the user to type in a number
# against 5 to see if it's true or false. Type and execute/run this
# program example and type numbers, either less than 5 or
# greater than 5 or equal to 5.

try:
    num = int(input('Type in a number and I will condition the result against 5 as either \
"true" or false" ').strip())

    if num == 5:
        print(f'True! {num} equals equals 5.')

    elif num < 5:
        print(f'True! {num} is less than 5.')

    elif num > 5:
        print(f'False! {num} is not greater than 5.')

    elif num <= 5:
        print(f'True! {num} is less than or equal to 5.')

    elif num >= 5:
        print(f'False! {num} is is not greater than or equal to 5.')

except ValueError:
    print('That is incorrect!')

# Type and execute/run this fun true/false program example
# below and see what happens when you type either 'START',
# 'STOP' 'HELP' or 'Q'.

start = False

while True:
    command = input('SPACECRAFT\n').lower().strip()

    if command == 'start':
        if start:
            print('Spacecraft has already took off.')

        else:
            start = True
            print('Spacecraft is taking off!')

    elif command == 'stop':
            if not start:
                print('Spacecraft has already landed.')

            else:
                start = False
                print('Spacecraft is landing.')

    elif command == 'help':
        print('Type "START" to fly the spacecraft or type "STOP" to land the spacecraft. \
Press "Q" to quit.\n')

    elif command == 'q':
        break

    else:
        print(f'Sorry! cannot understand "{command}".')

# For-Loop Examples:

# Loops are instructions, which tell the computer to iterate/repeat a part of a program a
# certain numbers of times before it stops. When a loop reaches its final iteration, it stops
# and comes to an end. Loops make programming code very efficient, without the manual
# redundancy on the programmer's part. Loops can also manipulate data by incrementing
# it or decrementing it.

# The 'for i in range(5):' for-loop causes the 'print' statement
# value to print 'Hello World!' five times:

for i in range(5):
    print('\nHello World!')

# Here is a manual, redundant example of this tuple string code
# without using a for-loop:

tuple_string_name = ('Superman','Batman','Spiderman')

print(f'\nMy name is {tuple_string_name[0]} and I\'m a SuperHero.')

print(f'\nMy name is {tuple_string_name[1]} and I\'m a SuperHero.')

print(f'\nMy name is {tuple_string_name[2]} and I\'m a SuperHero.')

# Here is a manual, redundant example of this list string code
# without using a for-loop:

list_string_name = ['Superman','Batman','Spiderman']

print(f'\nMy name is {list_string_name[0]} and I\'m a SuperHero.')

print(f'\nMy name is {list_string_name[1]} and I\'m a SuperHero.')

print(f'\nMy name is {list_string_name[2]} and I\'m a SuperHero.')

# Here is a non manual example of this very same code, using a
# for-loop. The for-loop also increments the string's data values,
# which makes the code more efficient, without the manual
# redundancy on the programmer's part.

tuple_string_name = ('Superman','Batman','Spiderman')

for i in range(3):
    print(f'\nMy name is {tuple_string_name[i]} and I\'m a SuperHero.')

list_string_name = ['Superman','Batman','Spiderman']

for i in range(3):
    print(f'\nMy name is {list_string_name[i]} and I\'m a SuperHero.')

# The new 'list_string_name' value 'Halk' is appended/added at
# the end of the for-loop.

list_string_name = ['Superman','Batman','Spiderman']

list_string_name.append('Halk')

for i in range(4):
    print(f'\nMy name is {list_string_name[i]} and I\'m a SuperHero.')

# This for-loop example loops by using the string's variable,
# instead of using the range values.

list_string_name = ['Superman','Batman','Spiderman']

list_string_name.append('Halk')

for i in list_string_name:
        print(f'\nMy name is {i} and I\'m a SuperHero.')

# How to make a for-loop count, starting from 0 to 9 with a
# 'print' statement using the (f') format along with the words
# 'Count Loop!', with # a loop range equal to 10.

for i in range(10):
    print(f'\nCount Loop! "{i}" ')

# Here is a fun list looping program example with the for-loop.
# The animal_list variable gets incremented by (i) each cycle
# through the for-loop. The animal_list variable will keep iterating
# in the for-loop, until the values in animal_list gets completely
# cycled through the for-loop.

animal_list = ['dog','cat','bird','duck','chicken']

for i in animal_list:
    print(f'\nI would love to own a {i}. I just love {i}s so much!')

# In this example the for-loop will cycle through the nums list,
# containing real integer values. When it encounters the 'if i == 5:'
# statement, the 'print' statement (f'{i}: I found number "{i}" ') will
# execute followed by the 'break' statement. When the 'break'
# statement is executed, the for-loop stops iterating through the
# rest of the nums list values.

nums = [1,2,3,4,5,6,7,8,9]

for i in nums:
    if i == 5:
        print(f'\n{i}: I found number "{i}" ')
        break
    print(f'\n{i}')

# In this example the for-loop will cycle through the nums list,
# containing real integer values. When it encounters the 'if i == 5:'
# statement, the 'print' statement (f'\n{i}: I found number "{i}" ')
# will execute followed by the 'continue' statement. When the
# 'continue' statement is executed, the for-loop runs its complete
# iteration through the nums list values.

nums = [1,2,3,4,5,6,7,8,9]

for i in nums:
    if i == 5:
        print(f'\n{i}: I found number "{i}" ')
        continue
    print(f'\n{i}')

# In this example the for-loop will cycle through the dictionary_list
# key value's values. The key value "Animals" points to four values
# ['Dog','Cat','Bird','Fish]. When the first for-loop ends, the second
# for-loop will cycle through the key value "Reptiles", which points
# to four values ['Turtle','Lizard','Snake','Frog']. When the second
# for-loop ends, the third for-loop will cycle through the key value
# "Insects", which points to four values ['Butterfly','Beetle','Ant','Bee'].

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

for values in range(4):
    print(dictionary_list['Animals'][values])

for values in range(4):
    print(dictionary_list['Reptiles'][values])

for values in range(4):
    print(dictionary_list['Insects'][values])

# In this example the for-loop will cycle through each of the dictionary_
# list key values only. The 'print' statement 'print(key,value[0])' only
# prints out the first item of every key value's value. For example: the key
# value 'Animals' will only access the value 'Dog', then the for-loop will
# cycle over again to the next key value 'Reptiles', which again will only
# access the value 'Turtle'. The final for-loop will cycle through the
# dictionary_list key value 'Insects', which, once again will only access
# the value 'Butterfly'. However each of these key values are also printed
# along the left side of the values; example: "Animals Dog", "Reptiles
# Turtle", "Insects Butterfly". If you change the 'print' statement value
# 'value[0]' to 'value[1]' the for-loop will only access the values "Animals
# Cat", "Reptiles Lizard", "Insects Beetle". Now, if you change the 'print'
# statement value to 'value[2]' the "Animals key value will become
# "Animals Bird" and "Reptiles key value will become "Reptiles Snake"
# and Insects key value will become "Insects Ant". If you change the 'print'
# statement value to 'value[3]', the last items in the key value's value will
# look like this:

# "Animals Fish", "Reptiles Frog" and "Insects Bee". Try changing the
# 'print' statement 'value[number]' and see what happens when you
# execute/run the program.

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

for key,value in dictionary_list.items():
    print(key,value[0])

# Take a very close look at the program example below. It's like a
# for-loop but it's a manual-loop. You decide how long this manual-
# loop will manually be. Take a close look at the highlighted 'iter'
# function and the highlighted 'next' function in the 'print' statements.
# These functions are what make this manual loop possible. However,
# if you want to add more 'print' statements with 'next' functions in
# them, you also need to add more values inside the variable. For
# example, the variable 'book' has the values of the name of this book.
# Type and execute/run the program example below; add more values,
# change values and see what happens each time you execute/run the
# program.

book = ('Python',"Programmer's",'Glossary','Bible')

manual_loop = iter(book)
print(next(manual_loop),end = ' ')
print(next(manual_loop),end = ' ')
print(next(manual_loop),end = ' ')
print(next(manual_loop))

# For-loops can have other for-loops nested inside them, called a 'Nest'.
# The main, outer for-loop repeats one whole cycle through, while the
# nested, inner for-loop repeats its entire cycles through on each cycle
# of the main, outer for-loop. On the next cycle of the main, outer for-
# loop, the nested, inner for-loop repeats its entire cycles all over again.

for i in range(3):
    print(f'\nRepeat main loop "for i in range({i}):" cycles.\n')
    for x in range(4):
        print(f'Repeat nested loop "for x in range({x}):" cycles.')

# While-loop Examples:

# While-loops are conditional loops that end when a certain condition is met, or when a
# certain value is found to be true. In Python, while-loops also work in conjunction with
# 'If' and 'Elif' and 'Else' statements.

# Here is just one example of a conditional while-loop, which counts,
# starting from 0 to 9 with a 'print' statement using the (f') format along
# with the words 'Count Loop!', with a loop conditional value of 10. As
# long as (i) is less (<) than 10, the while-loop will keep on looping until
# (i) is equal to 10. Note: you can also use 'i = i+1' if you wish.

i = 0
while i < 10:
    print(f'\nCount Loop! "{i}" ')
    i += 1

# This conditional while-loop example will never ever stop looping,
# until the user presses either "y" or "n" followed by pressing the
# "Enter" key to confirm. If the user presses any other key except "y"
# or "n", the conditional while loop will keep on looping forever. After
# the while-loop gets broken, the final 'print' statement ('"Yay!" You
# broke the while-loop example.') will execute/run, which ends the
# conditional while-loop example. You can add as many 'if' and 'elif'
# statements you like within a while-loop. Note: these two 'break'
# statements cause the while -loop to stop looping. If the 'break'
# statements weren't used, the while-loop would just keep on going
# forever, making the user press the same keys forever. All loops must
# come to an end, such as for-loops and conditional while-loops alike.
# If a loop is infinite, running away, the program and/or computer will
# eventually crash. It's important to make sure loops always break out
# or end when a certain condition is met, such as in this conditional
# while-loop example.

# The '.strip()' function clears away unwanted white spaces, via user
# input data.

while True:
    Letter = input('\nYou must press "y" or "n" then press (ENTER) to break out of this \
conditional while-loop example: ').strip()

    if Letter == ('y'):
        print('\nThe "y" key was pressed and the while-loop breaks.')
        break

    elif Letter == ('n'):
        print('\nThe "n" key was pressed and the while-loop breaks.')
        break

print('\n"Yay!" You broke out of the while-loop example.')

# This conditional while-loop example will never ever stop looping,
# until the user presses "y" followed by the "Enter" key to confirm.
# If the user presses any other key except "y", the conditional while-
# loop will keep on looping forever. After the while- loop gets broken,
# the final 'print' statement (f'You gave me "{letter}", so I broke out of
# the conditional while loop example.') will execute/run. Now if the
# user doesn't press the right key, either less (<) than "y" or greater (>)
# than "y", the key mapping range will always execute/run the 'print'
# statement (f'Oops! You give me "{letter}", so I won\'t stop this
# conditional while-loop example, until you give me "y".'), and the loop
# keeps on iterating over and over, until the user presses 'y'. After the
# while-loop gets broken, the final 'print' statement ('This is the end of
# the entire conditional while-loop example.') will execute/run.

# Note: Python executes/runs programs starting from the top,
# downward. Be very careful on how you place statements. Some
# statements cannot execute right, even if they work. This is simply
# because of the order that Python executes/runs its program statements.

while True:
    letter = input('\nGive Me "y": ').strip()
    if letter == 'y':
        print(f'\nYou gave me "{letter}", so I broke out of the conditional \
while-loop example.')
        break

    elif letter < 'y' or letter > 'y':
        print(f'\nOops! You give me "{letter}", so I won\'t stop this conditional \
while-loop example, until you give me "y".')

print('\nThis is the end of the entire conditional while-loop example:')

# This conditional while-loop example will never ever stop looping,
# until the user types the number "10" followed by pressing the "Enter"
# key to confirm. If the user types any other number keys except "10",
# the conditional while-loop will keep on looping forever. After the
# while-loop gets broken, the final 'print' statement ('This is the end
# of the entire conditional while-loop example.') will execute/run.

# Note: the 'int' statement is for integer values only.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order that
# Python executes/runs its program statements.

while True:
    number = int(input('\nGive Me "10": ').strip())
    if number == 10:
        print(f'\nYou gave me "{number}", so I broke out of the conditional \
while-loop example.')
        break

    elif number < 10:
        print(f'\nOops! You give me "{number}", which is too small. I won\'t \
stop this conditional while-loop example, until you give me "10".')

    elif number > 10:
        print(f'\nOops! You give me "{number}", which is too big. I won\'t stop \
this conditional while-loop example, until you give me "10".')

print('\nThis is the end of the entire conditional while-loop example:')

# Try and Except Error Handlers:

# This code below is exactly the same as the code above, but with one exception. The
# code below has an error handler called 'try:' and 'except:' whereas the very same code
# above does not have an error handler at all. This spells disaster when you want the user
# to type numbers only. Without an error handler, if the user types a letter instead of a
# number, the program will crash leaving the user very unhappy with your newly developed
# software. It's imperative that in some situations, error handlers must be implemented into
# the program to prevent unwanted errors from occurring, such as in this error handler
# example code. Below is a complete list of exception handlers. From here on, any 'input'
# statements with numeric examples given will contain 'try:' and 'except:' error handlers.

while True:
    try:
        number = int(input('\nGive Me "10": ').strip())
        if number == 10:
            print(f'\nYou gave me "{number}", so I broke out of the conditional \
while-loop example.')
            break

        elif number < 10:
            print(f'\nOops! You give me "{number}", which is too small. I won\'t \
stop this conditional while-loop example, until you give me "10".')

        elif number > 10:
            print(f'\nOops! You give me "{number}", which is too big. I won\'t stop \
this conditional while-loop example, until you give me "10".')

    except ValueError:
        print('\nThe \'try:\' and \'except ValueError:\' handlers prevent any unwanted \
value errors from occurring, via user input data.')

        print('\nIf the user presses any letter keys instead of pressing number keys, \
the \'try:\' and \'except:\'block executes/runs.')

print('This is the end of the entire conditional while-loop example:')

# This is a basic layout of the 'try and except', 'finally' program
# example. The program does work fine, but it does nothing.
# The program example below simply shows the basic layout
# of the 'try and except', 'finally' statements. The 'finally' statement
# is executed no matter the outcome the 'try and except' handler
# block does. Note: you can also leave out the 'finally' statement
# if you like, but it can come in handy if you want the final outcome
# to execute no matter what the 'try and except' handler block does.
# The 'pass' statements are just empty placeholders for the empty
# code blocks until they are needed, via the programmer.

try:
     pass
except:
     pass
else:
     pass
finally:
     pass

# Here is the very same 'try and except' program example below.
# Type and execute/run the program and see what happens.

try:
     message = int(input('Pick a number. ').lower().strip())
except ValueError:
     print('Numbers only please.')
else:
     print('You picked a number.')
finally:
     print("'finally' executed no matter what.")

# The 'finally' statement is executed no matter the outcome the
# 'try and except' handler block does.

# These two 'input' statements in this program example asks the
# user their name and their age, using the 'try:' and 'except:' error
# handlers.

name = input('\nWhat is your name please? ').lower().strip()

try:
    age = int(input(f'\nHow old are you {name}? ').lower().strip())
    print(f'\n{name}. You are {age} years old.')

except ValueError:
    print('\nThe \'try:\' and \'except ValueError:\' block executes/runs whenever a letter \
key is pressed instead of a number key.')

# Now, put this very same program code above into a conditional
# while-loop and see what happens when the user tries to type letters,
# instead of typing numbers for their age. When the 'try:' statement is
# executed, the 'break' statement causes the conditional while-loop to
# break out and the 'print' statement ('End of program') is then executed.

name = input('\nWhat is your name please? ').lower().strip()

while True:
    try:
        age = int(input(f'\nHow old are you {name}? ').lower().strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print('\nThe \'try:\' and \'except ValueError:\' block executes/runs whenever a \
letter key is pressed instead of a number key.')

# This little flip flop game is a great example of how the conditional while-
# loop works. The 'else' statement executes/runs when the user types the
# wrong keys, and the while-loop iterates/repeats over again while ignoring
# the 'break' statement.

print('\nWelcome to Flip! Flop!')

print('\nPlease type the words "flip" or "flop", then press (ENTER)')

print('\nWhen you give up, press (ENTER) to quit playing Flip! Flop!')

while True:
    flip = input('\nFlip? or Flop? ').strip()

    if flip == 'flip':
        print('\nFlop!')

    elif flip == 'flop':
        print('\nFlip!')

    elif flip == '':
        print('\nThanks for playing Flip! Flop!')
        break

    else:
        print('\nYou can\'t cheat now! Do you flip? or do you flop?')

# This conditional while-loop will loop as long as the value is less (<)
# than 3, then it will stop its iteration no matter what wrong keys the
# user tries to type.

chance = 0

name = input('\nWhat is your name please? ').strip()

while chance < 3:
    try:
        age = int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print(f'\nYou have 3 chances left before the while-loop breaks out anyway!')

        chance += 1

# This for-loop example does exactly the same thing, the above
# while-loop example shows. The only difference is, the while-loop
# is a conditional loop, whereas the for-loop is an iterate. While-
# loops can also be 'True:' or 'False:', depending on the outcome
# of a program's execution run. While-loops also compare data
# greater than or less than other data, as shown in the examples
# above.

name = input('\nWhat is your name please? ').strip()

for chance in range(3):
    try:
        age = int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print('\nYou have 3 chances left before the while-loop breaks out anyway!')

        chance += 1

# This conditional while-loop example types out the words "Python
# Programmer\'s Glossary Bible". As long as 'length' is less (<) than
# 'len' starting at "0", the while-loop will keep on looping until  'length'
# is equal to 'len'. The 'os.system('cls')' function clears the screen each
# cycle through the while-loop, and the 'time.sleep(.05)' function delays
# the while-loop in between cycles. This fun, little program example
# makes the printout on the screen appear as if it were actually typing
# letters.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order that
# Python executes/runs its program statements.

# Note: The 'import os' module and the 'import time' module must be
# imported first.

import os
import time

letters = '\n"Python Programmer\'s Glossary Bible"'
length = 0

while length <= len(letters):
    os.system('cls')
    print(letters[:length])
    time.sleep(.05)
    length += 1

# This conditional while-loop example compares a random number
# against user input data. If the user picks the right number by luck
# alone, the while-loop will break out and the program ends. If the
# user picks the wrong number, the less (<) than or greater (>) than
# 'random_num' variable gets conditioned and the while-loop keeps
# on iterating until the right number is picked, via user input data.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order that
# Python executes/runs its program statements.

# Note: The 'import random' module must be imported first.

import random

random_num = random.randint(1,10)

while True:
    try:
        pick_num = int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())

        if pick_num < random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num > random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations! You won. "{random_num}" was the \
number I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')

# This very same program example as above works exactly the same
# way, but with one major difference; the while loop will only iterate
# three times. If the user picks the right number, the while loop breaks.
# If the user doesn't pick the right number after three times, the 'else'
# statement executes and says 'Sorry! You lost.', which ends the
# program.

# Note: the 'import random' module must be imported first.

import random

random_num = random.randint(1,10)

i = 0

while i < 3:
    try:
        pick_num = int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())

        i += 1

        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')

else:
    print('\nSorry. You lost!')

# Once again, this is the very same program example as above before.
# However, this time the loop iterates in reverse instead of forward and
# the user is shown how many guesses they have left before they win
# or lose.

# Note: the 'import random' module must be imported first.

import random

random_num = random.randint(1,10)

i = 3

while i > 0:
    try:
        pick_num = int(input(f'\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10:\n\nYou have {i} gesses left. ').strip())

        i -= 1

        if pick_num<random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num>random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')

else:
    print('\nSorry. You lost!')

# This program example has three, separate conditional while-loops,
# each of them compares data against user input data. The first while-
# loop asks for the user's first name. The second while-loop asks for
# the user's last name, and the third while-loop asks for the user's age.
# In the first and second while-loop, the user's first name and the user's
# last name is compared by how many letters the user types. The
# 'str([first_name])' statement makes the user type in text only, not
# integers.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order that
# Python executes/runs its program statements.

while True:
    first_name = input('\nWhat is your name please? ').strip()

    if first_name<str([first_name]):
        print('\nError: text only please!')

    elif len(first_name)<3:
        print('\nYour first name must be over 2 characters long.')

    elif len(first_name)>10:
        print('Your first name must be under 10 characters long.')

    else:
        break

while True:
    last_name = input(f'\nNice to meet you {first_name.title()}. \
What is your last name please? ').strip()

    if last_name < str([last_name]):
        print('\nError: text only please!')

    elif len(last_name) < 3:
        print('\nYour last name must be over 2 characters long.')

    elif len(last_name) > 10:
        print('\nYour last name must be under 10 characters long.')

    else:
        break

while True:
    try:
        age = int(input(f'\nHow old are you {first_name.title()}? ').strip())
        break

    except ValueError:
        print('\nError: integers only please!')

print(f'\nYour first name = {first_name.title()}:\nYour last name = \
{last_name.title()}:\nYour age = {age}:\n')

# Type and execute/run this program example and see how the while-
# loop only breaks when one of the two 'break' statements is executed.
# If none of them gets executed, the while-loop keeps on iterating. This
# program example is another great example of how the conditional 'if:'
# and 'elif:' statements work in conjunction with the logical operators.

while True:
    try:
        stars = int(input('How many stars would you like? ').strip())
        if stars > 1:
            print(f'\n{stars} Stars: [',' * '*stars,f']\n\nI gave you {stars} \
Stars!\n\nI hope you enjoy your {stars} Stars...')
            break

        elif stars == 1:
            print(f'\n{stars} Star: [','*'*stars,f']\n\nI gave you {stars} \
Star!\n\nI hope you enjoy your \'One\' \
and \'Only\', single Star...')
            break

        elif stars == 0:
            print('\nSorry Hero! Zero doesn\'t count.\n')
    except ValueError:
        print('\nNumbers only please!\n')

# While-loops can loop through dictionary values. The three 'print'
# statements show the dictionary names: "Animals", "Reptiles" and
# "Insects". The variable (i) increments the dictionary values four
# times, which prints out all the values in all three dictionary names.
# Type and execute/run this 'dictionary_list' program example:

dictionary_list = (
    {'Animals':['Dog','Cat','Bird','Fish'],
     'Reptiles':['Turtle','Lizard','Snake','Frog'],
     'Insects':['Butterfly','Beetle','Ant','Bee']}
    )

i = 0

while i < 4:
    print(dictionary_list['Animals'][i])
    print(dictionary_list['Reptiles'][i])
    print(dictionary_list['Insects'][i])

    i += 1

# This keyboard dictionary program example displays the keys that
# the user presses. This program example has a different 'try:' and
# 'except:' error handler called 'TypeError:', which prevents punctuation
# keys from causing user text typing errors. The '.get()' method returns
# the dictionary key's values as the user types either letters and/or number
# keys. The for-loop block increments the values of the '.get()' method by
# (i) each time the user presses letters and/or number keys.

keyboard_dictionary = {
'0':'Number Zero','1':'Number One','2':'Number Two',
'3':'Number Three','4':'Number Four','5':'Number Five',
'6':'Number Six','7':'Number Seven','8':'Number Eight',
'9':'Number Nine','a':'Letter A','b':'Letter B','c':'Letter C',
'd':'Letter D','e':'Letter E','f':'Letter F','g':'Letter G','h':'Letter H',
'i':'Letter I','j':'Letter J','k':'Letter K','l':'Letter L','m':'Letter M',
'n':'Letter N','o':'Letter O','p':'Letter P','q':'Letter Q','r':'Letter R',
's':'Letter S','t':'Letter T','u':'Letter U','v':'Letter V','w':'Letter W',
'x':'Letter X','y':'Letter Y','z':'Letter Z'
}

print('Type any key, then press (ENTER)')
print('Type \'QUIT\' to quit!\n')

while True:
     try:
         letters = input().lower().strip()
         if letters == 'quit':
             break

         get_key_value = ''

         for i in letters:
             get_key_value += keyboard_dictionary.get(i)+' '

         print(get_key_value)

     except TypeError:
         print('Letters or numbers only please!')

# "AND" "OR" and "NOT"

# The 'and' statement is only "True", if both values are true. If both values are
# "False", the 'and' statement is still true because they are the same, regardless
# of their values. However, if the 'and' statement values are different, nothing
# will happen, and this is where the 'or' statement comes into play. The 'or'
# statement will only be "True" if both values are different.

# Here is another prime example of how these conditionals: 'True'
# and 'False' actually work in conjunction with 'and' and 'or'. Depending
# on the outcome, this program example will either be 'True' or 'False'.
# Type and execute/run this program example and change the values of
# 'gate1 = True', and 'gate2 = False' to different 'True' and 'False' combinations,
# for example: 'gate1 = False, 'gate2 = False.

gate1 = True
gate2 = False

if gate1 and  gate2:
    print(f' "AND" is true because gate1 is "{gate1}" and gate2 is "{gate2}".')

elif gate1 or gate2:
    print(f' "OR" is true because gate1 is "{gate1}" and gate2 is "{gate2}".')

else:
    print(f' "AND" is true because gate1 is "{gate1}" and gate2 is "{gate2}".')

# Type and execute/run The George Boole Game program example
# to get a better understanding of how Boolean Logic works and why
# it works.Type different "True" and "False" combinations and see
# what Gearoge Boole does. Press 'Q' to quit playing.

print('\nThe George Boole Game\n')

print('George loves to play "True" or "False",\nbut he needs your help to play it.')

print('\nPress "Q" to quit!')

while True:
    Boole1 = input('\nType "True" or "False" for the first value. ').strip()
    if Boole1 == 'q':
        print('Thanks for playing!')
        break

    print(f'\nYou chose "{Boole1.title()}" for your first value.\n')
    Boole2 = input('\nType "True" or "False" for the second value. ').strip()

    if Boole2 == 'q':
        print('Thanks for playing!')
        break

    print(f'You chose "{Boole2.title()}" for your second value.\n')

    if Boole1 == 'true' and  Boole2 == 'true':
        print(f' "AND" is true because Boole1 is "{Boole1.title()}" \
and Bool2 is "{Boole2.title()}".\n')

    elif Boole1 == 'false' and Boole2 == 'false':
        print(f' "AND" is true because Boole1 is "{Boole1.title()}" and Boole2 is \
"{Boole2.title()}".\n')

    elif Boole1 == 'true' or Boole2 == 'true':
        print(f' "OR" is true because Boole1 is "{Boole1.title()}" and Boole2 is \
"{Boole2.title()}".\n')

    elif Boole1 == 'false' or Boole2 == 'false':
        print(f' "OR" is true because Boole1 is "{Boole1.title()}" and Boole2 is \
"{Boole2.title()}".\n')

    else:
        print('Type the right vales please!')

# The 'not' Operator

# The 'not' operator simply turns true values into false values, and visa versa;
# false values into true values. For example, true 'and' true is 'True' and false
# 'and' false is 'False'. Now here is where things get a little bit weird when
# implementing a 'not' operator against true and false values. Here are some
# examples of the 'not' operator and how it turns true values into false values,
# and false values into true values.

# Here are some examples of how the 'not' operator works. Type and
# execute/run each of these program examples to see how they work.

Boole = True

if Boole == True:
    print(Boole)

print('George Boole says \'True\' because \'True\' and \'True\' are true.')

Boole = False

if Boole == False:
    print(Boole)

print('George Boole says \'False\' because \'False\' and \'False\' are false.')

# Here are two examples of how 'True' and 'False' values contradict
# one another, which causes these two program examples below not
# to show any output on the screen, except the 'print' statement, that
# says George Boole does not contradict himself.

Boole = True

if Boole == False:
    print(Boole)

print('George Boole does not contradict himself.')

Boole = False

if Boole == True:
    print(Boole)

print('George Boole does not contradict himself.')

# Remember that if 'True' equals 'True', then the outcome will
# also equal 'True'. However, when a 'not' operator is implemented
# into the mix of a 'True equals 'True' comparison, that's when
# things get strangely confusing. However, the confusion is nothing
# to fret about. The 'not' operator simply turns a 'True' equals 'True'
# into a 'True' equals 'False', which acts like the program examples
# under the following program example. All three program examples
# won't show any output on the screen, but the 'print' statement
# 'George Boole does not contradict himself.'

Boole = True

if Boole == True:
    if not Boole:
        print(Boole)

print('George Boole does not contradict himself.')

Boole = True

if Boole == False:
    print(Boole)

print('George Boole does not contradict himself.')

Boole = False

if Boole == True:
    print(Boole)

print('George Boole does not contradict himself.')

# These two program examples below show how a 'not' operator
# makes a true value become a false value, and how a false value
# becomes a true value.

variable = True

if not  variable:
    print('False becomes True')

else:
    print('True Becomes False')

variable = False

if not  variable:
    print('False becomes True')

else:
    print('True Becomes False')

# Here are some more examples of 'True' and 'False' conditionals.
# Type and execute/run each of these program examples below
# and see what happens when 'True' and 'False' values become
# 'False' and 'True' values instead.

Boole = True

if Boole == True:
     print('True')

else:
     Boole == False
     print('False')

Boole = False

if Boole == True:
     print('True')

else:
     Boole == False
     print('False')

# Here are some more examples of the 'not' operator. Type and
# execute/run each of these program examples below and see
# what happens when a 'True' value is 'not' 'True' and when a
# 'False' value is 'not' 'False'.

Boole = True

if not Boole == True:
     print('True')

else:
     Boole == False
     print('False')

Boole = False

if not Boole == True:
     print('True')

else:
     Boole == False
     print('False')

# The Definition Function:

# Most Python programs consist of functions. Functions in Python allow programmers
# to add functionality in their programs that might be needed again and again throughout
# the program's execution run. With functions, programmers can call/execute functions
# from another file as part of the main program’s execution run from the main file. Note:
# calling files from other files must be stored within the same directory path or folder; via
# Windows for example. Functions can also return values, which can be changed or
# modified throughout the program’s execution run. Just remember that functions simply
# add functionality. Also remember the acronym or abbreviation (DRY): Don’t Repeat Yourself!

# Definition functions are called def functions for short. Def function
# statements always start with the word ‘def’ followed by parameters
# or without parameters. However, all def statements must proceed with
# a semicolon (:) at the end of all def statements. For example, def example():
# is a function without parameters, whereas def example(self,name,age):
# has three parameters. The semicolon assures that any program statements
# underneath the def statements are always indented, which is Python’s way
# of keeping the program statements as part of the complete def function.
# Note: any program statements, which are not indented will simply be
# bypassed altogether, meaning they won’t be executed as part of the def
# function at all; thus creating potential errors to occur. Now it's time to get
# your feet a little bit more wet. Are you ready?

# Like strings, def functions must not have any empty spaces
# between words. Use an underscore ie: (_) in place of empty
# spaces instead.

# This small program shows no output whatsoever on the screen.

def my_first_function():
    print('My first function')

# Now, let's call the function with the following statement
# so we can see the output on the screen.

my_first_function()

# Type and execute/run the program with the def function
# call statement my_first_function() to see the actual output
# on the screen.

def my_first_function():
    print('My first function')

my_first_function()

# Now, let's expand our understanding of functions by adding
# more program statements to truly create some functionality
# in our def function program. Remember to 'call the function'
# to see the output on the screen with the statement
# 'my_second_function()'

def my_second_function():
    print('My second function.')
    print('add some more functionality.')
    print('Wow! This was so easy to create!')

my_second_function()

# Now, let's dive a little deeper into program functionality with
# a simple for-loop in our def statement block. Type and execute/
# run the program and see what happens.

def my_third_function():
    for i in range(3):
        print('My third function example.')

my_third_function()

# Now, let’s combine some strings with a for-loop inside our
# fourth def function block program example. Type and execute/
# run the program and see what happens.

tuple_string = ('Python','Programmer\'s','Glossary','Bible')

def my_fourth_function():
    for i in tuple_string:
        print(i,end= ' ')

my_fourth_function()

# The (end=' ') emitter forces the print statement to keep printing
# on the same line. Below is the very same program example as
# above, but without the (end=' ') emitter. Type and execute/run
# the program and see what happens.

tuple_string = ('Python','Programmer\'s','Glossary','Bible')

def my_fourth_function():
    for i in tuple_string:
        print(i)

my_fourth_function()

# Now, let's use some parameters in our def function statement
# program example. Type and execute/run the program below and
# see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)

my_function('first parameter','second parameter','third parameter')

# When using parameters inside def function statements, you must
# also take note that you must use the exact number of variables to
# how many values you use within the function's call statement.
# For example, if you use three parameter variables, you must also
# use exactly three values to satisfy all three parameter variables.
# If you exceed the number of variables, or exceed the number of
# parameter values within the function's call statement, you will get an
# index out of range error; thus crashing the program. It's imperative
# that, including simple strings or anything that takes variables and
# values must always be equal to be satisfied. As for the print statement,
# you can leave out arguments, and use them later on. Here is an example
# of what the very same program below does when you leave out some
# arguments within the print statement; the program continues to run
# fine. However, if you try to add an argument that does not exist inside
# the def function's parameter variables, a crash will occur.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)

my_function('first parameter','second parameter','third parameter')

# Here is the very same program example, but with arguments
# that don't belong to the function's parameter variables at all.
# When you 'try' to run the program, a crash will occur. Type
# and execute/run the program below and see what happens,
# when you try to use non-existent arguments within the print
# statement.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parametr,second_parameter,third_paramete)

my_function('first parameter','second parameter','third parameter')

# The program above has two arguments, which don't belong
# named 'first_ parametr' and 'third_paramete'. The programmer
# didn't catch the error, because the 'e' and the 'r' were left out
# of the argument's variables, which was the root cause of the
# error. Variables and values must be literal, meaning they must
# be the same, unless they are modified, which the program
# example below shows. Type and execute/run the program
# below and see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print('mod first_parametr',second_parameter,'mod third_paramete')

my_function('first parameter','second parameter','third parameter')

# Single (') or double (") quote marks can be used to modify the print
# statement argument variables. However, if you use single quote
# marks, you have to use only single quote marks. If you use double
# quote marks, you must use only double quote marks. The quote
# marks always have to be the same regardless. Here is a simple print
# statement that uses the wrong quote marks. Type and execute/run
# the one line program example below and see how the program
# causes an error.

print("the program will crash, because the quotes are wrong')

# Here are the two correct ways to use single or double quote marks.

print('The program runs, because the quote marks are the same')

print("The program runs, because the quote marks are the same")

# Now, let's use the very same def function program example
# below and change some values in the function's call statement,
# so we can understand functions a little bit better. However, this
# topic on functions is quite lengthy; we have much to cover before
# we get into class functions, which is also quite the lengthy topic
# in itself.

# We already know that using one variable means using just one
# value. We also know that if we use two variables, we must also
# use two values to satisfy the two variables, i.e. For example:

#	variable_1 = 'value 1'

#	variable_1,variable_2 = 'value 1','value 2'

#	variable_1,variable_2,variable_3 = 'value 1','value 2','value 3'

variable_1,variable_2,variable_3 = 'value 1','value 2','value 3'

print(variable_1)

# The print statement contains the argument variable, variable_1,
# which is called 'value 1'. The argument variable passes
# the value, 'value 1' right into the print statement, 'variable_1'. You
# can use as many of the same argument variables you so desire.
# You can save argument variables for later use as well. You can
# also use and reuse argument variables over and over again, such
# in this program example below. Type and execute/run the program
# example below and see what happens.

variable_1,variable_2,variable_3 = 'value 1','value 2','value 3'

print(variable_1,variable_1,variable_3,variable_2,variable_3)

# Take a look at the call statement 'my_function' and change the
# word 'value 1' to say the word "Python". Make sure you use single
# or double quote marks in each value. Double quote marks are used
# as an example for one value to show how quote marks behave.
# Type and execute/run the program below and see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)

my_function("Value 1",'Value 2','Value 3')

# Take a close look at the quote marks at "value2" in the function's
# call statement. You can use single or double quotes, but you cannot
# mix double quotes with single quotes on the same value. For example:

#	my_function("Python',"Value 2",'Value 3')

#	my_function('Python","Value 2",'Value 3")

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter)

my_function("Python","Value 2",'Value 3')

# Note: always use commas to separate multiple variables, multiple
# values and multiple arguments, including strings, tuples, lists and
# dictionaries alike. Use the (\) inline emitter to wrap long statements
# of any sort.

# Now, let's add some more argument variables in our def function
# program example. Note: if you have three variables, and three values,
# you can only use three, named arguments. However, you can use and
# reuse arguments over and over again, and as many times as you like.

def my_function(first_parameter,second_parameter,third_parameter):
    print(first_parameter,second_parameter,third_parameter,first_parameter,
          third_parameter,first_parameter)

my_function("Python",'Value 2','Value 3')

# You can also save arguments for later use, such as the case
# with this very same program example below. Type and execute/run
# the program and see what happens.

def my_function(first_parameter,second_parameter,third_parameter):
    print('I don\'t want to use any arguments for now.')

my_function("Python",'Value 2','Value 3')

# Now it's time to ratchet things up a bit with more def functions.
# Are you ready?

# Take a close look at this def function's parameter variables. Just
# like before, but this time the values are inside the def function
# statement along with the def function's variables. Also take a close
# look at the def function's call statement; nothing needs to be inside
# the call statement 'my_function'. That's because the variables and
# the values are inside the def function statement parameters
# themselves. Type and execute/run the program below and see what
# happens.

def my_function(var1 = 'value1',var2 = 'value2',var3 = 'value3'):
    print(var1)
    print(var2)
    print(var3,var1,var3,var2)

my_function()

# Remember you can use and reuse arguments over and over again.

# Def functions can return values via the 'return' statement.
# Type and execute/run the programs below and see what happens.

def get_value(name):
    return name

print(get_value('Python Programmer\'s Glossary Bible'))

# This program example below does the very same thing as the
# program example above illustrates. If name values are too long,
# they can be stored inside a variable instead. For example, the
# variable 'get_name' takes the place of this really long string value:

#	get_value('Python Programmer\'s Glossary Bible')

def get_value(name):
    return name

get_name = get_value('Python Programmer\'s Glossary Bible')

print(get_name)

def get_value(name,program):
    return name

get_name = get_value('Python','Programmer\'s Glossary Bible')

print(get_name)

def get_value(name,program):
    return program

get_name = get_value('Python','Programmer\'s Glossary Bible')

print(get_name)

# Use the index [ ] emitter to create nicer looking screen output.

def get_value(name,program,book):
    return name,program,book

get_name = get_value('Python','Programmer\'s','Glossary Bible')

print(get_name[0],get_name[1],get_name[2])

# Without the index [ ] emitter, the screen output looks sort of
# unfinished such as in this program example below illustrates.

def get_value(name,program,book):
    return name,program,book

get_name = get_value('Python','Programmer\'s','Glossary Bible')

print(get_name)

# Use the (f') format function to concatenate/add words with
# strings. Use curly braces { } in conjunction with the (f') format
# function. Type and execute/run the program example below
# and see what happens.

def  software(name,program,book):
    return f'I love my {name} {program} {book} very much!'

Python = software('Python','Programmer\'s','Glossary Bible')

print(Python)

# Def functions can return the result of a given number value.
# For example 'num's value is equal to '4', which is in the print
# statement. When multiplying 'num*num, the value '4' also gets
# multiplied ie: '4*4', which now equals '16'. So the result of the
# returning value is '16'. Type and execute/run each program
# example below and see what happens.

def multiply(num):
    return num*num

print(multiply(4))

# You can add versatility to functions with the 'return' statement.
# You can return 'num as much as you like. For example:

def multiply(num):
    return num*num+num

print(multiply(4))

# You can also combine ordinary integer numbers with values,
# such as this program example below illustrates. Just remember
# the golden rules of "BEDMAS" -2+5 = 3+2 = 5-2 = '3'.

def multiply(num):
    return num*num+num+num-2+5

print(multiply(4))

# The 'return' statement returns the results of the value 'num'.

# The result of the returned value 'num' is: 4*4+4+4-2+5 = '27'

def multiply(num):
    return num*num+num+num-2+5

print(multiply(4+3))

# The result of the returned value 'num' is: 7*7+7+7-2+5 = '66'

# Let's create a return function that returns two values called 'num1
# and 'num2'. The value of 'num1 = 4' and the value of 'num2 = 3'.

def multiply(num1,num2):
    return num1*num2

print(multiply(4,3))

# The result of the returned values of 'num1' and 'num2' is: 4*3 = '12'

# You can keep these two values as separate values, which return
# their separate results. for example:

#	4*3,3+4 = 12,7

# Use a comma (,) to separate values inside the 'return' statement.

#	return num1*num2,num1+num2

def multiply(num1,num2):
    return num1*num2,num1+num2

print(multiply(4,3))

# Type and execute/run the program example above and see
# what happens.

# Let's cube a number with a return function and see what
# happens when you type and execute/run the program
# example below.

def cube(num):
    return num**num

print(cube(3))

# Use a double asterisk (**) to cube numbers.
# The value 3 works like this:

#	3*3*3 = '27'

#	print(3*3*3)

# Return an integer number with the 'int' function.

def multiply(num1,num2):
    return int(num1*num2)

print(multiply(4,3.0))

# Return a floating-point number with the 'float' function.

def multiply(num1,num2):
    return float(num1*num2)

print(multiply(4,3))

# Let's create an outer function and an inner function, then call
# the outer function by assigning the variable 'get_function' to
# it. Type and execute/run the program example below and see
# what happens.

def outer_function():
    message = 'Python'
    def inner_function():
        print(f'{message} Programmer\'s Glossary Bible')

    return inner_function

get_function = outer_function()

get_function()

# Let's pass the variable 'message' into the outer function and
# return the value through the inner function. Next, let's call the
# outer and inner functions by assigning the variables 'get_function1'
# and 'get_function2' to them. Type and execute/run this program
# example below and see what happens.

def outer_function(message):
    message = message
    def inner_function():
        print(message)

    return inner_function

get_function1 = outer_function('Get Function One.')
get_function2 = outer_function('Get Function Two.')

get_function1()
get_function2()

# Let's pass the variable 'message' right into the inner function and
# then call the outer and inner functions by assigning the variables
# 'get_function1' and 'get_function2 to them. Type and execute/run
# the program example below and see what happens.

def outer_function(message):
    def inner_function():
        print(message)

    return inner_function

get_function1 = outer_function('Get Function One.')
get_function2 = outer_function('Get Function Two.')

get_function1()
get_function2()

# Python or any other object oriented programming languages, such
# as 'C' has no 'goto', 'gosub' or any 'jump to subroutine' commands
# at all. To get around this problem, Python uses 'def functions' to
# create subroutines. Type and execute/run the program example
# below and see what happens.

def subroutine_1():
    print('This is subroutine 1')

def subroutine_2():
    print('This is subroutine 2')

def subroutine_3():
    print('This is subroutine 3')

while True:

    get_subroutine = input("Press '1', '2' or '3' to get the subroutine \
you want to display: ").lower().strip()

    while True:

        if get_subroutine == '1':
            subroutine_1()
            break

        elif get_subroutine == '2':
            subroutine_2()
            break

        elif get_subroutine == '3':
            subroutine_3()
            break

        else:
             print('Sorry! No subroutine exist for',
                   get_subroutine)
             break

    display_again = input("Would you like to display any more subroutines? \
Type 'Yes' or 'No' to confirm. ").lower().strip()

    if display_again == 'yes':
        continue

    elif display_again == 'no':
        break

    else:
        print('Sorry! I don\'t understand that.')

# Now it's time to get into working with classes.

# The Class Function:

# The class function in Python is like a super function, which can have multiple def functions
# right inside it. Class functions may consist of parent classes and child classes alike.
# The child classes inherit the parent classes, which means giving functions the ability
# to change their behavior outcome, throughout a program's execution run. You can use
# as many parent/upper classes you wish. However, only one child class can be used, which
# is always the last class act. You don't need to invoke def functions to use classes either.
# However, we are going to learn about both types such as this program example below,
# which doesn't invoke def functions at all.

# Type and execute/run the program example below and see what
# happens.

class Grandma:
    gm = 'I\'m the Grandma class'

class Grandpa:
    gp = 'I\'m the Grandpa class'

class Mom:
    m = 'I\'m the Mom class'

class Dad:
    d = 'I\'m the Dad class'

class Child(Grandma,Grandpa,Mom,Dad):
    pass

print(Child.gm)
print(Child.gp)
print(Child.m)
print(Child.d)

# The 'pass' function tells the program to ignore the empty code
# block until later use, via the programmer's choice.

# Now let's place a 'print' statement where the 'pass' function was.
# Type and execute/run the program below and see what happens.

class Grandma:
    gm = 'I\'m the Grandma class'

class Grandpa:
    gp = 'I\'m the Grandpa class'

class Mom:
    m = 'I\'m the Mom class'

class Dad:
    d = 'I\'m the Dad class'

class Child(Grandma,Grandpa,Mom,Dad):
    print("The 'pass' function is now a print statement.")

print(Child.gm)
print(Child.gp)
print(Child.m)
print(Child.d)

# Sometimes a code block needs information, but you, the programmer
# does not wish to provide that, and that's where the 'pass' function
# comes in handy. Sometimes you don't want to use any code in a code
# block at all; that's the whole purpose of what the 'pass' function is all
# about. The 'pass' function ignores the code block and caries on its
# way, without the potential risk of errors. Here is an example of such an
# error. Type and execute/run the program examples below and see what
# happens.

class syntax_error:

# You will get a syntax error: 'expected an indented block'

class pass_function:
    pass

# The 'pass' function ignores the empty code block, which allows the
# programmer to decide what to do later on, or simply 'pass' the empty
# code block altogether. Use the 'pass' function in any type of empty
# code block to avoid potential errors from occurring.

# Classes can also be single classes, such as the program example
# below illustrates. Type and execute/run the program below and see
# what happens.

class Single_class:
    sc = 'I\'m a single class.'

print(Single_class.sc)

# Here is a simple Mom class and a simple Dad class, along with
# their simple Child class. Type and execute/run the program
# example below and see what happens.

class Mom:
    mom = 'I\'m Chid\'s Mom.'

class Dad:
    dad = 'I\'m Child\'s Dad.'

class Child(Mom,Dad):
    pass

print(Child.mom)
print(Child.dad)

# Let's call up the class function called 'Mom'.

print(Mom.mom)

# Let's call up the class function called 'Dad'.

print(Dad.dad)

# Let's call up Mom and Dad inside one, single 'print' statement.

print(Mom.mom,Dad.dad)

# Let's call up the Child class inside one, single 'print' statement.

print(Child.mom,Child.dad)

# Here is our very same Mom and Dad class program example,
# which uses list variables called 'mom' and 'dad'. Type and
# execute/run the program below and see what happens.

class Mom:
    mom = [
        'Class Mom with list item position [0]',
        'Class Mom with list item position [1]',
        'Class Mom with list item position [2]',
        ]

class Dad:
    dad = [
        'Class Dad with list item position [0]',
        'Class Dad with list item position [1]',
        'Class Dad with list item position [2]',
        ]

class Child(Mom,Dad):
    pass

print(f'The Child class inherits all classes:\n{Child.mom[0]}')
print(f'The Child class inherits all classes:\n{Child.dad[1]}')

# Now let's have some fun and change the words in the list.
# Let's also use double (") quote marks instead of single (')
# quote marks. Note: the (f') format function is not invoked
# inside the 'print' statements. However, you can still invoke
# the (f') format function if you like. Type and execute/run
# the program below and see what happens.

class Mom:
    mom = [
        "Mom's are the best!",
        "Mom's care so much!",
        "Mom's make dreams happen!",
        ]

class Dad:
    dad = [
        "Dad's are the best!",
        "Dad's care so much!",
        "Dad's make dreams happen!",
        ]

class Child(Mom,Dad):
    pass

print(Child.mom[0])
print(Child.dad[1])

# Tip: invoke the 'pass' function to make it much easier to create
# classes. Remove any 'pass' functions you no longer need, when
# adding code inside empty code blocks. Type and execute/run
# the program example below and see what doesn't happen.

class Mom:
    pass

class Dad:
    pass

class Child(Mom,Dad):
    pass

# The program above works just fine even if it shows no output on the
# screen. The reason that is, is simply because the 'pass' functions are
# just empty placeholders that occupy the empty code blocks, until the
# programmer decides to add code inside the empty code blocks.

# Type and execute/run the program example below and see what
# happens.

class Mom:
    mom = 'Mom'

class Dad:
    pass

class Child(Mom,Dad):
    pass

print(Mom.mom)
print(Child.mom)
print(Mom.mom,Child.mom)

# Now it's time to grow up and learn some more about classes,
# without Mom and Dad around. Classes don't need to be called
# Mom and Dad or Child to work. You can give classes any name
# you wish. Classes always start with an uppercase letter like
# 'Mom', 'Dad' and 'Child'. However, you can use lowercase
# letters if you like.

# The program example below illustrates a single class function,
# which invokes two def function blocks. Single class functions
# with two or more def function blocks work similar to parent and
# child class functions. Creating function classes simply means
# adding more versatility to functions in general. Type and execute/
# run the program below and see what happens.

class My_Shapes:
    def __init__(self,shape,sides):
        self.shape = shape
        self.sides = sides

    def shape_sides(self):
        return f'{self.shape} {self.sides}'

a = My_Shapes('Hexagon','Six Sides')
b = My_Shapes('Octagon','Eight Sides')
c = My_Shapes('Dodecagon','Twelve Sides')

print(f'{a.shape} {b.shape} {c.shape}')
print(f'{a.shape_sides()} {b.shape_sides()} {c.shape_sides()}')

# The program example below is the very same program example
# above. The only difference is, 'num' was added to create a third
# argument.

class Shapes:
    def __init__(self,shape,num,sides):
        self.shape = shape
        self.num = num
        self.sides = sides

    def shape_sides(self):
        return f'{self.shape} {self.num} {self.sides}'

a = Shapes('Hexagon',6,'sides')
b = Shapes('Octagon',8,'sides')
c = Shapes('Dodecagon',12,'sides')

print(f'{a.shape} {b.shape} {c.shape}')
print(f'{a.num} {b.num} {c.num}')
print(f'{a.shape_sides()} {b.shape_sides()} {c.shape_sides()}')

# To reduce code let's rewrite the class 'My_Shapes' program
# below. You can also notice how the code looks much cleaner
# and more meaningful, than in our first example. Also, notice
# how the name 'shape_sides' is no longer in our class 'My_
# Shapes' program example. The 'return' function simply returns
# the 'sides' value, without the need to manually add the 'shape_
# sides' function's name inside the 'print' statements, such as
# the examples above show. The 'shape_sides' value was returned
# through the 'print' statement instead. Like before, you can do
# things either way, but always remember to keep it DRY!: Don't
# Repeat Yourself!

class My_Shapes:
    def __init__(self,shape,sides):
        self.shape = shape
        self.sides = sides

    def shape_sides(self):
        return self.shape,self.sides

a = My_Shapes('Hexagon','Six Sides')
b = My_Shapes('Octagon','Eight Sides')
c = My_Shapes('Dodecagon','Twelve Sides')

print(f'{a.shape} has {a.sides}')
print(f'{b.shape} has {b.sides}')
print(f'{c.shape} has {c.sides}')

# Let's get rid of the repeating 'print' statements in the class 'My_Shapes'
# program with a for-loop. First, let's create a very short string list called
# 'dry' so we can tell the for-loop what to print out. Each time the for-loop
# executes, (i) increments by one value in our 'dry' list. Once all the values
# loop through the for-loop, the for-loop ends. It's just as if we used three
# 'print' statements, but the for-loop just shortened our program once
# again keeping it 'DRY', without any repeating 'print' statements.

dry = a,b,c

for i in dry:
    print(f'{i.shape} has {i.sides}')

# The program example above uses a dunder method, which consists
# of two double underscores '__ __', called dunders. The dunder 'init'
# method is one of the most used methods. These special dunder
# methods are sometimes called 'Magic Methods', and these special
# methods allow us to emulate built-in data types or implement operator
# overloading. You probably didn't know it, but you've been using these
# dunder methods all along. These methods can be extremely powerful
# if they are used correctly. The dunder 'init' means to initialize a function.
# The word 'Dunder' simply means 'Double__Underscore'.

# These two 'print' statements below use the dunder method 'add',
# which is the same as the 'print' statements 'print(2+3)' and 'print('a'+'b')'.
# The 'int' function adds only integer numbers together, whereas the 'str'
# function concatenates-joins character strings together.

print(int.__add__(2,3))

# Screen output:	5

print(str.__add__('a','b'))

# Screen output:	ab

# Dunder methods assure functionality inside class functions. For
# example, you wouldn't use a dunder '__str__' method with integer
# values; likewise, you wouldn't use a dunder '__add__' method with
# character string values.

# Take a close look at these two program examples below. You notice
# there are yellow highlighted variables. These variables indicate how
# these two, very same program examples can be written. Both program
# examples do exactly the same thing, even though they look a wee bit
# different. Type and execute/run these two program examples below
# and see what happens.

# Program example 1:

class Dunder_add:
    def __init__(self,num):
        self.num = num

    def __add__(self,plus):
        return self.num+plus

a = Dunder_add(6)
b = Dunder_add(8)
c = Dunder_add(12)

print(a.num+b.num+c.num)

# Program example 2:

class Dunder_add:
    def __init__(self,num):
        self.num = num

    def __add__(self,plus):
        return self.num+plus.num

a = Dunder_add(6)
b = Dunder_add(8)
c = Dunder_add(12)

print(a+b+c.num)

# There are several types of dunder methods in Python. However,
# we will only focus on the ones we will learn for now.

# Take a close look at these two program examples below. You
# notice there are yellow highlighted variables. These variables
# indicate how these two, very same program examples can be
# written. Both program examples do exactly the same thing, even
# though they look a wee bit different. Type and execute/run these
# two program examples below and see what happens.

# Program example 1:

class Shapes:
    def __init__(self,shape,sides):
        self.shape = shape
        self.sides = sides

    def shape_sides(self):
        return f'{self.shape} {self.sides}'

    def __add__(self,add_num):
        return self.sides+add_num

a = Shapes('Hexagon',6)
b = Shapes('Octagon',8)
c = Shapes('Dodecagon',12)

print(a.sides+b.sides+c.sides)

print(a.shape_sides(),b.shape_sides(),c.shape_sides())

# Program example 2:

class Shapes:
    def __init__(self,shape,sides):
        self.shape = shape
        self.sides = sides

    def shape_sides(self):
        return f'{self.shape} {self.sides}'

    def __add__(self,add_num):
        return self.sides+add_num.sides

a = Shapes('Hexagon',6)
b = Shapes('Octagon',8)
c = Shapes('Dodecagon',12)

print(a+b+c.sides)

print(a.shape_sides(),b.shape_sides(),c.shape_sides())

# The program example below converts two integers into string
# characters, while still being able to calculate the result of the
# actual integer values themselves. Type and execute/run the
# program example below and see what happens.

class Dunder_str:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return str(f'{self.num1}/{self.num2}, and I want more text')

dunder = Dunder_str(26,2+3)

print ("I want these integers to be a string, using 'str'.",str(dunder),'here.')

# The program example below uses the dunder method '__repr__',
# which follows the dunder method '__str__' as a fallback for
# programmers to see code as human, readable text. Type and
# execute/run the program example below and see what happens.

class Dunder_str:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return str(f'{self.num1}/{self.num2}, and I want more text')

    def __repr__(self):
        return str(f'{self.num1},{self.num2}, and I want more text')

dunder = Dunder_str(26,2+3)

print("I want these integers to be a string, using 'str'.",str(dunder),'here.')

print("I want these integers to be an object, using 'repr'.",repr(dunder),'here.')

# Here is a small multi-class function program that inherits all the
# properties of all the other classes with the last class act being the
# 'Child Class', called 'Shape_Features'. Type and execute/run the
# program example below and see what happens when you change
# values, such as 'shape', 'sides' and 'colour' values.

class My_Shapes:
    def __init__(self,shape,sides):
        self.shape = shape
        self.sides = sides

    def shape_sides(self):
        return self.shape,self.sides

class Shape_Colours:
    def colours(self):
        return self

class Shape_Features(My_Shapes,Shape_Colours):
    pass

a = Shape_Features('Hexagon','Six Sides')
b = Shape_Features('Octagon','Eight Sides')
c = Shape_Features('Dodecagon','Twelve Sides')

aa = Shape_Features.colours('Gold')
bb = Shape_Features.colours('Silver')
cc = Shape_Features.colours('Chrome')

print(f'{a.shape} has {a.sides} colour {aa}')
print(f'{b.shape} has {b.sides} colour {bb}')
print(f'{c.shape} has {c.sides} colour {cc}')

# Here is another multi-class function program that inherits all the
# properties of all the other classes with the last class act being
# the 'Child Class', called 'Sum'. Each def statement has a different
# return math operation, such as addition, subtraction, multiplication,
# division, square and cube operations. The asterisk (*) is used for
# multiplying numbers together. Type and execute/run the program
# example below and see what happens when you change values,
# such as numbers and operators alike.

class Math0:
    def addit(num1,num2):
        return num1+num2

class Math1:
    def subtr(num1,num2):
        return num1-num2

class Math2:
    def multi(num1,num2):
        return num1*num2

class Math3:
    def divis(num1,num2):
        return num1/num2

class Math4:
    def square(num1,num2):
        return num1**num2

class Math5:
    def cube(num1,num2):
        return num1**num2*num1

class Sum (
    Math0,Math1,
    Math2,Math3,
    Math4,Math5
    ):
    pass

print(Sum.addit(5,2))
print(Sum.subtr(5,2))
print(Sum.multi(5,2))
print(Sum.divis(5,2))
print(Sum.square(5,2))
print(Sum.cube(5,2))

# Let's add three class functions together inside the 'print' statement.

print(Sum.addit(5,2)+Sum.subtr(5,2)+Sum.cube(5,2))

# Now, let's create a list called 'x' and add all the class functions
# together inside the 'print' statement. Remember to use list indexing
# ie: [ ] starting at list index [0]. Also remember that Python always
# starts at index [0] with tuples, lists and dictionaries alike.

x = (
    Sum.addit(5,2),
    Sum.subtr(5,2),
    Sum.multi(5,2),
    Sum.divis(5,2),
    Sum.square(5,2),
    Sum.cube(5,2)
    )

print(x[0]+x[1]+x[2]+x[3]+x[4]+x[5])

# Let's call up all the actual functions, which are inside the
# multi-class function program example.

print(Math0.addit(5,2))

print(Math1.subtr(5,2))

print(Math2.multi(5,2))

print(Math3.divis(5,2))

print(Math4.square(5,2))

print(Math5.cube(5,2))

# The class function program example below works exactly the
# same as the class 'Shapes' function program example does.
# Type and execute/run the program and see what happens.

class Scientists:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

a = Scientists('Stephen','Hawking')
b = Scientists('Albert','Einstein')
c = Scientists('Isaac','Newton')
d = Scientists('Galileo','Galilei')

# Try these 'print' statement examples below and change the letter
# 'b' to the letter 'a' and try the letter 'c' and so on. Re-execute/run
# the program and see what happens.

print(f'{b.first_name}')
print(f'{b.last_name}')
print(f'{b.full_name()}')

# Make a sentence out of this 'print' statement program example:

print(f'{b.full_name()} loves science, and \
so does {a.full_name()}, along with {d.first_name}.')

# Type and execute/run the program example below and see what
# happens.

class Mathematics:
    def __init__(self,addition,subtraction,
                 multiplication,division):
        self.addition = addition
        self.subtraction = subtraction
        self.multiplication = multiplication
        self.division = division
    def Math_Functions(self):
        return self.addition,self.subtraction
        return self.multiplication,self.division

nums = Mathematics(3+2,3-2,3*2,6/2)

names = Mathematics(
    'Stephen Hawking',
    'Albert Einstein',
    'Isaac Newton',
    'Galileo Galilei'
    )

print(
    f'{nums.addition}',f'{names.addition}\n'
    f'{nums.subtraction}',f'{names.subtraction}\n'
    f'{nums.multiplication}',f'{names.multiplication}\n'
    f'{int(nums.division)}',f'{names.division}'
    )

# OS Text Colour Codes:

# Let's have some fun and colour some text with special OS text colour codes that create
# colourful text output onto the OS output screen. Note: some Python programs require
# modules to be imported first, such as this print text colour program example below illustrates.

# Type and execute/run the program example below and see what
# happens. Note: you must execute/run the program from the OS
# output screen, via double-clicking the Python program file itself.

# Save the Python file as 'Text Colour Codes'

import os
os.system('')

print('\x1b[31mRed')
print('\x1b[32mGreen')
print('\x1b[34mBlue')
print('\x1b[33mYellow')
print('\x1b[35mPurple')

input("\x1b[37mPress 'Enter' to quit the OS output screen.").strip()

# Create variables to make the colour codes much easier to understand
# and to work with. Use the (f') format to simplify the variables inside
# the 'print' statement. Type and execute/run the program example below
# and see what happens. Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python program file itself.

# Save the Python file as 'Text Colour Variables'

import os
os.system('')

red = '\x1b[31m'
green = '\x1b[32m'
blue = '\x1b[34m'
yellow = '\x1b[33m'
purple = '\x1b[35m'
white = '\x1b[37m'

print(f'{red}Red text colour.')
print(f'{green}Green text colour.')
print(f'{blue}Blue text colour.')
print(f'{yellow}Yellow text colour.')
print(f'{purple}Purple text colour.')

input(f"{white}Press 'Enter' to quit the OS output screen.").strip()

# Now, let's create three simple tuples called 'text_words', 'text_colour'
# and 'text_all' to, not only shrink down the code, but to also manipulate
# the code. Type and execute/run the program example below and see
# what happens when you change or rearrange the tuple values inside
# the 'text_all' tuple itself. Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python program file itself.

# Save the Python file as 'Text All'

import os
os.system('')

text_words = (
    "Python","Programmer's",
    "Glossary","Bible"
    )

text_colour = (
    '\x1b[31m','\x1b[32m',
    '\x1b[34m','\x1b[33m',
    )

text_all = (f'\n{text_colour[0]}{text_words[0]} {text_colour[1]}{text_words[1]} \
{text_colour[2]}{text_words[2]} {text_colour[3]}{text_words[3]}'
    )

print(text_all)

input("\x1b[37mPress 'Enter' to quit the OS output screen.").strip()

# This program example below is exactly the same as the program
# example above. The only difference is, that this program example
# below illustrates the use of the 'exec' function, which allows
# programmers to use and reuse redundant code, without having
# to retype it over and over. Type and execute /run this program
# example below and see what happens. Note: you must execute/run
# the program from the OS output screen, via double-clicking the
# Python program file itself.

# Save the Python file as 'Text All 2'

import os
os.system('')

text_words = (
    "Python","Programmer's",
    "Glossary","Bible"
    )

text_colour = (
    '\x1b[31m','\x1b[32m',
    '\x1b[34m','\x1b[33m',
    '\x1b[37m'
    )

text_all = (f'{text_colour[0]}{text_words[0]} {text_colour[1]}{text_words[1]} \
{text_colour[2]}{text_words[2]} {text_colour[3]}{text_words[3]}'
    )

redundant_code = '''
print('')
print(text_all)
print(f'{text_colour[4]}I love my {text_all}')
'''

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)

input(f"{text_colour[4]}Press 'Enter' to quit the OS output screen.").strip()

# Remember to use three single quote (''') marks at the beginning and
# at the end of program code as illustrated below. Also remember, you
# can name the 'redundant_code' variable any name you wish. Type
# and execute/run the program example below and see what happens.

redundant_code = '''
print("I'm a piece of code that needs to be used and reused.")
'''

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)

# There are also OS screen colours, which also colours text. However,
# the OS screen colours are not as flexible as text colours are. For
# example, If you try to make one line of text blue and try to make the
# next line of text green. When you execute/run the program, the next
# line of text you coloured green will override the blue text, making it
# green text too. Note: you must execute/run the program from the OS
# output screen, via double-clicking the Python program file itself.

# Save the Python file as 'OS screen colours'

import os

white = ('color f')
blue = ('color 9')
red = ('color 4')
green = ('color a')
cyan = ('color b')
pink = ('color c')

os.system(blue)
print('The text is blue')

os.system(green)
print('The text is green')

# Python Clock Functions:

# Python clock functions allow you to program the actual time in real time. Python clock
# functions work internally, in sync with the Windows clock. With Python clock functions;
# you can set the hour, minute, second, month, week, day and date. See Python clock
# function prefix descriptions below.

# '%I'	12-hour prefix
# '%H'	24-hour prefix
# '%M'	Minutes prefix
# '%S'	Seconds prefix
# '%p'	AM/PM prefix
# '%A'	Day of week prefix
# '%B'	Month prefix
# '%d'	Date prefix
# '%Y'	Year prefix
# '%U'	Weeks per year prefix
# '%j'	Days per year prefix

# Let's create a simple Python clock by invoking the Python clock function
# prefixes. First, however, we also need to import two modules; 'time' and
# 'datetime'. Type and execute/run the program example below and see
# what happens.

import time
import datetime

print(datetime.datetime.now().strftime('%I:%M:%S:%p'))
print(datetime.datetime.now().strftime('%H:%M:%S'))
print(datetime.datetime.now().strftime('%A %B %d,%Y'))
print(datetime.datetime.now().strftime('Week %U'))
print(datetime.datetime.now().strftime('Day %j'))

# Remember you can reduce balky code via, using string variables. Let's
# use 'timer' as the variable and use 'datetime.datetime.now()' as the value.
# Type and execute/run the program example below and see what happens.

import time
import datetime

timer = datetime.datetime.now()

print(timer.strftime('%I:%M:%S:%p'))
print(timer.strftime('%H:%M:%S'))
print(timer.strftime('%A %B %d,%Y'))
print(timer.strftime('Week %U'))
print(timer.strftime('Day %j'))

# Now, let's create a tuple variable called 'show_time' so we can reduce
# even more balky code, and also gain greater manipulative programming
# skills at the same time. Type and execute/run the program example
# below and see what happens.

import time
import datetime

show_time = (
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

timer = datetime.datetime.now()

print(timer.strftime(show_time[0]))
print(timer.strftime(show_time[1]))
print(timer.strftime(show_time[2]))
print(timer.strftime(show_time[3]))
print(timer.strftime(show_time[4]))

# Now change and rearrange the tuple number values [0] through [4] in
# the program example above and re-execute/run the program and see
# what happens.

# Now, let's make our Python clock come to life. Let's also keep the code
# less balky and much more program manipulative at the same time. To
# make the Python clock come to life, we are simply going to use a while-
# loop to constantly refresh the screen output. A 'time.sleep()' function
# will also be implemented to create a one-second sleep delay in the screen
# output. Let's also implement the 'os.system()' function to clear the screen
# output right after every one-second 'time.sleep' delay. Type and execute/
# run the program example below and see what happens.

import os
import time
import datetime

show_time = (
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

while True:
    timer = datetime.datetime.now()
    print(timer.strftime(show_time[0]))
    print(timer.strftime(show_time[1]))
    print(timer.strftime(show_time[2]))
    print(timer.strftime(show_time[3]))
    print(timer.strftime(show_time[4]))

    time.sleep(1)
    os.system('cls')

# Python Wave Sounds:

# Python wave sounds are easy to create, because they are simply wave sounds you already
# have on your Windows computer system. Note: Python limits to wave sound format only.
# Wave sound files must be stored in the same folder/directory where your Python program
# files are also stored.

# Type and execute/run the wave sound program example below.
# Use the name of the wave sound file only, such as 'SPEECH OFF'
# for example.

import winsound

winsound.PlaySound('SPEECH OFF',winsound.SND_ASYNC)

# The wave sound program below looks similar to the one above.
# The only difference is, the wave sound program below waits to
# play the wave sound before continuing on with the rest of the
# Python program. Type and execute/run the program example
# below and see what happens.

import winsound

winsound.PlaySound('SPEECH OFF',winsound.SND_ALIAS)

# Here are some projects that require quite a bit of patience and
# dedication. The program examples below demand that you should
# have a basic understanding of strings, tuples, tuple indexes, for-
# loops and while-loops alike. Save these projects as Python files on
# your computer. You can give the files any name you wish, but they
# must be unique, different names assigned to them.

# Take your "time" and create the 'TIMERNATOR' clock program. Type
# and execute/run the program example below and see what happens.
# Note: you must execute/run the program from the OS output screen,
# via double-clicking the Python program file itself.

# Save the Python file as 'Timernator'

import os
import time
import datetime
import winsound

os.system(f'title TIMERNATOR')

text_colour = (
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m'
    )

special_fx = (
    f'{text_colour[0]}TIMERNATOR',

    'SPEECH OFF',

    'cls','\n','\n\n',' '
    )

time_fx = (
f'{text_colour[1]}12 Hour {text_colour[0]}%I{text_colour[1]}:\
{text_colour[0]}%M{text_colour[1]}:{text_colour[0]}%S {text_colour[1]}%p',

f'{text_colour[1]}24 Hour {text_colour[0]}%H{text_colour[1]}:\
{text_colour[0]}%M{text_colour[1]}:{text_colour[0]}%S',

f'{text_colour[2]}%A %B {text_colour[0]}%d{text_colour[1]}:\
{text_colour[0]}%Y',f'{text_colour[2]}Week{text_colour[1]}:\
{text_colour[0]}%U {text_colour[2]}Day{text_colour[1]}:\
{text_colour[0]}%j'
    )

text_fx = (
    f'{text_colour[2]}You\'re TIMERNATED!',

    f'{text_colour[2]}Look at me if you want the time.',

    f'{text_colour[2]}I need your hours, your minutes and your seconds.',

    f'{text_colour[2]}I swear I will tell the time.',

    f'{text_colour[2]}I cannot self timernate.'
    )

redundant_code1 = '''
print(
    special_fx[3],
    special_fx[5]*1,
    special_fx[0],
    special_fx[4],
    special_fx[5]*1,
    text_fx[x]
    )
'''
redundant_code2 = '''
print(
    special_fx[3],
    special_fx[5]*1,
    timer.strftime(time_fx[y])
    )
'''
while True:

    for x in range(4):
        os.system(special_fx[2])
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer = datetime.datetime.now()
            exec(redundant_code2)

        time.sleep(1)
        os.system(special_fx[2])
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer = datetime.datetime.now()
            exec(redundant_code2)

        time.sleep(1)
        os.system(special_fx[2])
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer = datetime.datetime.now()
            exec(redundant_code2)

        time.sleep(1)

# Take your "time" and create the 'FANTASTIQUE PLASTIQUE Easy Mix
# Converter' program. Type and execute/run the program example below
# and see what happens. Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python program file itself.

# Save the Python file as 'Fantastic Plastique'

import os
import time
import math
import winsound

os.system(f'title FANTASTIQUE PLASTIQUE Easy Mix Converter')

text_colour = (
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[37m'
    )

win_sound = (
    'Windows Notify System Generic',
    'Windows Background',
    'Windows Notify Email','BUZZ'
    )

text_words = (
    f'\n{text_colour[2]}FANTASTIQUE {text_colour[1]}PLASTIQUE {text_colour[2]}Easy \
{text_colour[1]}Mix {text_colour[2]}Converter',

    f'\n{text_colour[4]}Liquid Acrylic Mix: 8.oz = (1) Cup',

    f'\nLiquid Acrylic Mix: 4.oz = One Half Cup',

    f'\nGlow Powder Pigment: 28.349523 Grams = (1) Ounce',

    f'\nGlow Powder Pigment: 14.1747615 Grams = One Half Ounce',

    f'\nLiquid Acrylic Mix and Glow Powder Pigment Ratios: \
(4 = Parts LAM) to (1 = Part GPP)',

    f'\n1.0 Ounce = 28.349523 Grams or 28.35 Grams.',
    )

text_info = (
    f'\n{text_colour[2]}Please Enter Ounce Amount:{text_colour[1]}',

    f'\n{text_colour[4]}Press (Enter) to convert again or press (Q) to quit.',

    f'\n{text_colour[1]}Thanks for measuring with FANTASTIQUE PLASTIQUE \
Easy Mix Converter.',

    f'\n{text_colour[0]}ERROR! Input numbers only please.'
    )

text_works = ('cls','q')

ounce0 = float()
grams0 = float(28.349523)
ounce1 = float()
grams1 = round(28.349523,3)

while True:
    os.system(text_works[0])
    winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)

    for i in text_words:
        print(i)

    try:
        ounce0 = float(input(text_info[0]).strip())
        os.system(text_works[0])
        for i in text_words:
            print(i)

        winsound.PlaySound(win_sound[1],winsound.SND_ASYNC)
        print(f'\n{text_colour[2]}{ounce0} Ounce = {text_colour[1]}{ounce0*grams0} \
{text_colour[2]}Grams or {text_colour[1]}{ounce0*grams1} {text_colour[2]}Grams.')
        button = input(text_info[1]).strip()

        if button == (''):
            continue

        elif button == (text_works[1]):
            os.system(text_works[0])
            winsound.PlaySound(win_sound[2],winsound.SND_ASYNC)
            print(text_info[2])
            time.sleep(3)
            break

    except ValueError:
        os.system(text_works[0])

        for i in text_words:
            print(i)

        winsound.PlaySound(win_sound[3],winsound.SND_ASYNC)

        print(text_info[3])

        time.sleep(2)

# Take your "time" and create the 'ONTARIO LOTTO 6/49 RANDOM NUMBER
# GENERATOR' program. Type and execute/run the program example below
# and see what happens. Note: you must execute/run the program from the
# OS output screen, via double-clicking the Python program file itself.

# Save the Python file as 'Ontario Lotto'

import os
import time
import math
import random
import winsound

os.system(f'title ONTARIO LOTTO 6/49 RANDOM NUMBER GENERATOR')

text_colour = (
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[35m',
    '\x1b[36m',
    '\x1b[37m'
    )

text_words = (
    f'\n{text_colour[1]}Welcome to ONTARIO LOTTO 6/49 RANDOM NUMBER \
GENERATOR. Good Luck!\n\nPress (Enter) to activate the ONTARIO LOTTO \
6/49 RANDOM NUMBER GENERATOR:',

    f'\n{text_colour[1]}ONTARIO LOTTO 6/49 RANDOM NUMBER GENERATOR \
is activated.\n\nONTARIO LOTTO 6/49 RANDOM NUMBER GENERATOR SEQUENCE:',

    f'\n{text_colour[2]}Press (N) then press (Enter) to randomly pick a different set of \
Ontario Lotto 6/49 numbers.\n\nPress (Q) then press (Enter) to quit:{text_colour[1]}',

    f'\n{text_colour[1]}Thanks for playing ONTARIO LOTTO 6/49 RANDOM NUMBER \
GENERATOR. Good Luck!'
    )

random_num = (
    random.randint(1,9),
    random.randint(10,17),
    random.randint(18,25),
    random.randint(26,33),
    random.randint(34,41),
    random.randint(42,49)
    )

win_sound = ('TYPE','Windows Notify Messaging')

text_fx = ('cls','n','q')

y = 0

while y <= len(text_words[0]):
    winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
    print(text_words[0][:y])
    time.sleep(.06)
    os.system(text_fx[0])

    y += 1

button = input(text_words[0]).strip()

y = 0

while y <= len(text_words[1]):
    winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
    print(text_words[1][:y])
    time.sleep(.06)
    os.system(text_fx[0])

    y += 1

while True:
    winsound.PlaySound(win_sound[1],winsound.SND_ASYNC)
    print(
        f'{text_words[1]}{text_colour[0]}({random_num[0]}) ({random_num[1]}) \
({random_num[2]}) ({random_num[3]}) ({random_num[4]}) ({random_num[5]})'
        )

    button = input(text_words[2]).strip()

    os.system(text_fx[0])

    if button == (text_fx[1]):
        random_num = (
        random.randint(1,9),
        random.randint(10,17),
        random.randint(18,25),
        random.randint(26,33),
        random.randint(34,41),
        random.randint(42,49)
        )

    elif button == (text_fx[2]):
        break

y = 0

while y <= len(text_words[3]):
    winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
    print(text_words[3][:y])
    time.sleep(.06)
    os.system(text_fx[0])

    y += 1

print(text_words[3])

time.sleep(3)

# ASCII CODES:

# American Standard Code for Information Interchange

# All modern day computers that support text characters such as keyboard interfaces use
# ASCII codes. Since computers can only see numbers, not actual characters, ASCII codes
# make it possible to use numbers to represent one, single character. Each character is seven
# bits long, which makes it equal to one eight-bit byte; the eighth, leftmost bit is the 'sign-bit'.
# If the number is positive, the 'sign-bit' will be a 'zero', and if the number is a negative number,
# the 'sign-bit will be a 'one'. Take a look at the illustration below to gain a better understanding.

# One eight-bit binary byte = 11111111 = 255 = -128 and +127

# One half byte value 00000100 = '4'
# One byte value 1000100 = '-4'
# The 'sign-bit' can only be one of two states; either negative or positive.

# However, ASCII code values are read as human decimal numbers. For example, the ASCII
# code value for the capital later 'A' = '65'. The ASCII code value for the lowercase 'a' = '97'.
# The ASCII code value for the capital letter 'B' = '66', and the ASCII code value for the lowercase
# 'b' = '98'. Just remember every letter and every number on a computer keyboard has an
# ASCII code value to it. Below are some basic examples of how to use ASCII code characters
# in your programs.

# To get the ASCII code value of any letter or number key, simply type
# and execute/run the program examples below and see what happens.
# Try using different letters and numbers to see their ASCII code values.

print(chr(65))
print(ord('A'))

print(chr(97))
print(ord('a'))

print(chr(66))
print(ord('B'))

print(chr(98))
print(ord('b'))

print('ASCII code',ord('A'),'is the uppercase letter',chr(65))
print('ASCII code',ord('a'),'is the lowercase letter',chr(97))

print('ASCII code',ord('B'),'is the uppercase letter',chr(66))
print('ASCII code',ord('b'),'is the lowercase letter',chr(98))

# These simple dictionary program examples below illustrates the entire
# ASCII code alphabet character sets: uppercase and lowercase character
# sets. Type and execute/run the program examples below and see what
# happens.

ascii_lowercase_chars = (

    {'a':97,'b':98,'c':99,'d':100,

     'e':101,'f':102,'g':103,'h':104,

     'i':105,'j':106,'k':107,'l':108,

     'm':109,'n':110,'o':111,'p':112,

     'q':113,'r':114,'s':115,'t':116,

     'u':117,'v':118,'w':119,'x':120,

     'y':121,'z':122}
    )

ascii_uppercase_chars = (

    {'A':65,'B':66,'C':67,'D':68,

     'E':69,'F':70,'G':71,'H':72,

     'I':73,'J':74,'K':75,'L':76,

     'M':77,'N':78,'O':79,'P':80,

     'Q':81,'R':82,'S':83,'T':84,

     'U':85,'V':86,'W':87,'X':88,

     'Y':89,'Z':90}
    )

print("Uppercase 'A' = ASCII code value",
      (ascii_uppercase_chars['A']))

print("Lowercase 'a' = ASCII code value",
      (ascii_lowercase_chars['a']))

print("Uppercase 'B' = ASCII code value",
      (ascii_uppercase_chars['B']))

print("Lowercase 'b' = ASCII code value",
      (ascii_lowercase_chars['b']))

# These simple dictionary program examples below illustrates the
# ASCII code number characters and the ASCII code math operators.
# Type and execute/run the program examples below and see what
# happens.

ascii_number_chars = (
    {'0':48,'1':49,'2':50,'3':51,'4':52,

     '5':53,'6':54,'7':55,'8':56,'9':57}
    )

ascii_math_operator_chars = (
    {'+':43,'-':45,'*':42,'/':47}
    )

print("Number character '0' = ASCII code value",(ascii_number_chars['0']))

print("Number character '1' = ASCII code value",(ascii_number_chars['1']))

print("Number character '2' = ASCII code value",(ascii_number_chars['2']))

print("Number character '3' = ASCII code value",(ascii_number_chars['3']))

print("Math operator character '+' = ASCII code value",
      (ascii_math_operator_chars['+']))

print("Math operator character '-' = ASCII code value",
      (ascii_math_operator_chars['-']))

print("Math operator character '*' = ASCII code value",
      (ascii_math_operator_chars['*']))

print("Math operator character '/' = ASCII code value",
      (ascii_math_operator_chars['/']))

# Take your "time" and create the 'ASCII CODE TRANSLATOR'
# program. Type and execute/run the program example below
# and see what happens. Note: you must execute/run the
# program from the OS output screen, via double-clicking the
# Python program file itself.

# Save the Python file as 'Ascii Code Translator'

import os
import time
import math

os.system('title ASCII CODE TRANSLATOR')

text_features = (
    'cls',
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[37m'
    )

text_words = (
    f'\n{text_features[3]}ASCII CODE NUMERIC VALUE TRANSLATOR\n',

    f'\n{text_features[3]}ASCII CODE CHARACTER VALUE TRANSLATOR\n',

    f'\n{text_features[3]}ASCII CODE TRANSLATOR',

    f'\n{text_features[2]}Thanks for choosing ASCII CODE TRANSLATOR'
    )

word_info = (
    f'{text_features[5]}Please type a number, then press (Enter) to \
confirm:{text_features[2]}',

    f'{text_features[5]}Please type a letter key or a number key, then press (Enter) to \
confirm:{text_features[2]}',

    f'\n{text_features[3]}Please choose which ASCII code translator you would like to \
use:\n\n{text_features[5]}Press (1) for ASCII code number values.\nPress (2) for \
ASCII code character values.\nPress (Q) to quit.{text_features[2]} ',

    f'\n\n{text_features[3]}Do you wish to continue? Press (Enter) or press (Q) to \
quit:{text_features[2]}',

    f'\n{text_features[1]}This is a Value Error!',

    f'\n{text_features[1]}This is a Type Error!'
    )

button = ('1','2','q')

def subroutine1():
    while True:
        os.system(text_features[0])
        print(text_words[0])

        try:
            ascii_code = int(input(word_info[0]).strip())
            ascii_code = input(f'\n{text_features[2]}{chr(ascii_code)}{text_features[5]} = \
ASCII code: " {text_features[2]}{ascii_code}{text_features[5]} " {word_info[3]}').strip()

            if ascii_code == button[2]:
                break

        except ValueError:
            print(word_info[4])
            time.sleep(1)

def subroutine2():
    while True:
        os.system(text_features[0])
        print(text_words[1])

        try:
            ascii_code = input(word_info[1]).strip()
            ascii_code = input(f'\n{text_features[2]}{ascii_code}{text_features[5]} = \
ASCII code: " {text_features[2]}{ord(ascii_code)}{text_features[5]} " \
{word_info[3]}').strip()

            if ascii_code == button[2]:
                break
        except TypeError:
            print(word_info[5])
            time.sleep(1)

while True:
    os.system(text_features[0])
    print(text_words[2])
    butt = input(word_info[2]).strip()

    if butt == button[0]:
        subroutine1()

    elif butt == button[1]:
       subroutine2()

    else:
        if butt == button[2]:
            os.system(text_features[0])
            print(text_words[3])
            time.sleep(3)
            break

# Generate computer numbers in binary base 2, hexadecimal base
# 16 and octal base 8. Type in ASCII codes and see what they look
# like. For example: 'print(bin(65))' is the ASCII code value for the
# capital letter 'A' in binary base 2 as: '0b1000001'. Note: the '0b' is
# Python's prefix, which simply tells Python to work with binary
# base 2 numbers.

# Convert any number into a binary base 2 number.

print(bin(255))

# Convert any number into a hexadecimal base 16 number.

print(hex(255))

# Convert any number into an octal base 8 number.

print(oct(255))

# Type and execute/run each of these program examples below
# and see what happens.

comp_nums = int(input('Please type any number to see its binary base 2 number \
value: ').strip())

print(f'The number {comp_nums} = the binary base 2 number value: \
{bin(comp_nums)}.')

comp_nums = int(input('Please type any number to see its hexadecimal base 16 \
number value: ').strip())

print(f'The number {comp_nums} = the hexadecimal base 16 number value: \
{hex(comp_nums)}.')

comp_nums = int(input('Please type any number to see its octal base 8 \
number value: ').strip())

print(f'The number {comp_nums} = the octal base 8 number value: \
{oct(comp_nums)}.')

# The program example below uses ASCII code values for the math
# operator characters such as (+), (-), (*), (/) as well as an ASCII code
# value '113' for the lowercase letter 'q'. The 'Enter' key has no, such
# ASCII code value at all, but the 'ord('\r') or 'ord('\n') is like an ASCII
# code value for the 'Enter' key instead. In the program example below,
# the 'ord('\r') is used, which simply means 'return'; the '\n' means
# 'new line'. Both work fine for getting an ASCII code value for the
# 'Enter' key.

# Take your "time" and create the 'Magic Calculator' program. Type and
# execute/run the program example below and see what happens. Note:
# you must execute/run the program from the OS output screen, via
# double-clicking the Python program file itself.

# Save the Python file as 'Magic Calculator'

import os
import time
import math

os.system('title Magic Calculator')

mc = '\nMagic Calculator\n\n'

text_info = (
    f'\nWelcome to Magic Calculator. Press (Enter) to begin.',

    f'\nMagic Calculator\n\nEnter First Number: ',

    f'\nEnter (+) (-) (*) (/) Operator: ',

    f'\nEnter Second Number: ',

    f'\nMagic Calculator\n\nInvalid operator!',

    f'\nMagic Calculator\n\nERROR!',

    f'\nMagic Calculator\n\nERROR! Cannot divide by zero.',

    f'\nDo you wish to continue? Press \
(Enter) or press (Q) to quit: ',

    f'\nThanks for choosing Magic Calculator.'
    )

ascii_code = (
    f'\nchar(43) is the ASCII code for the  plus " + " sign.',

    f'\nchar(45) is the ASCII code for the negative " - " sign.',

    f'\nchar(42) is the ASCII code for the multiplication " * " sign.',

    f'\nchar(47) is the ASCII code for the division " / " sign.'
    )

operator = (chr(43),chr(45),chr(42),chr(47))
input(text_info[0]).lower().strip()

while True:
    while True:
        os.system('cls')

        try:
            num1 = int(input(text_info[1]).lower().strip())
            oper = input(text_info[2]).lower().strip()
            num2 = int(input(text_info[3]).lower().strip())

            if oper == operator[0]:
                os.system('cls')
                print(f'{mc}{num1} + {num2} = {num1+num2}')
                print(ascii_code[0])
                break

            elif oper == operator[1]:
                os.system('cls')
                print(f'{mc}{num1} - {num2} = {num1-num2}')
                print(ascii_code[1])
                break

            elif oper == operator[2]:
                os.system('cls')
                print(f'{mc}{num1} * {num2} = {num1*num2}')
                print(ascii_code[2])
                break

            elif oper == operator[3]:
                os.system('cls')
                print(f'{mc}{num1} / {num2} = {num1/num2}')
                print(ascii_code[3])
                break

            else:
                os.system('cls')
                print(text_info[4])
                time.sleep(1)

        except  ZeroDivisionError:
            os.system('cls')
            print(text_info[6])
            time.sleep(1)

        except ValueError:
            os.system('cls')
            print(text_info[5])
            time.sleep(1)

    repeat_calculator = input(text_info[7]).lower().strip()

    if repeat_calculator == ord('\r'):
        continue

    elif repeat_calculator == chr(113):
        os.system('cls')
        print(text_info[8])
        time.sleep(3)
        break

# Find out how many hours there are in one year.

print(f'\n{365*24:,} hours in one year.')

# Find out how many minutes there are in one year.

print(f'\n{365*24*60:,} minutes in one year.')

# Find out how many seconds there are in one year.

print(f'\n{365*24*60*60:,} seconds in one year.')

# Find out how many months there are in ten years.

print(f'\n{12*10:,} months in ten years.')

# Find out how many weeks there are in ten years.

print(f'\n{52*10:,} weeks in ten years.')

# Here's a fun, simple program example, which tells you how many
# seconds you have been on Earth for. Type and execute/run the
# program example below and see what happens when you type your
# age, then press the 'Enter' key. Note: this program example also
# uses the 'finally' statement to illustrate the use of the how the 'finally'
# command works. The 'finally' command will always execute, no
# matter the outcome. Also note that the 'finally' command only works
# with the 'try' and 'except' command blocks.

months = 12
weeks = 52
days = 365

hours_per_day = 24
minuts_per_hour = 60
seconds_per_minute = 60

string_tuple = (
    months,weeks,days,
    hours_per_day,
    minuts_per_hour,
    seconds_per_minute
    )

while True:

    try:
        age = int(input('How old are you? ').strip())

        print(f'\nYou have been on Earth for {age} years.')

        print(f'\nYou have been on Earth for {age*string_tuple[0]:,} months.')

        print(f'\nYou have been on Earth for {age*string_tuple[1]:,} weeks.')

        print(f'\nYou have been on Earth for {age*string_tuple[2]:,} days.')

        print(f'\nYou have been on Earth for {age*string_tuple[2]*string_tuple[3]:,} hours.')

        print(f'\nYou have been on Earth for \
{age*string_tuple[2]*string_tuple[3]*string_tuple[4]:,} minutes.')

        print(f'\nYou have been on Earth for \
{age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]:,} seconds.')

        break

    except ValueError:
        print('\nSorry! Numbers only please.\n')

    finally:
        print('Finally will always execute no matter the outcome.')

# See what happens when you type and execute/run this guessing
# game program example below. Note: you must execute/run the
# program from the OS output screen, via double-clicking the Python
# program file itself.

# Save the Python file as 'Know Your Stuff'

import os

tc = (
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[35m',
    '\x1b[36m',
    '\x1b[37m',
    'cls'
    )

question_prompts1 = (
    f'{tc[2]}How many sides does a Triangle have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}two sides',

    f'{tc[2]}How many sides does a Square have?\n\n{tc[1]}(a) {tc[2]}Two sides\n\
{tc[1]}(b) {tc[2]}Three sides\n{tc[1]}(c) {tc[2]}Four sides',

    f'{tc[2]}How many sides does a Pentagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}Three sides',

    f'{tc[2]}How many sides does a Hexagon have?\n\n{tc[1]}(a) {tc[2]}six sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}two sides',

    f'{tc[2]}How many sides does a Octagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}six sides\n{tc[1]}(c) {tc[2]}eight sides',

    f'{tc[2]}How many sides does a Dodecagon have?\n\n{tc[1]}(a) {tc[2]}eight \
sides\n{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}twelve sides',

    f'{tc[2]}How many sides does a Hexadecagon have?\n\n{tc[1]}(a) {tc[2]}sixteen \
sides\n{tc[1]}(b) {tc[2]}eight sides\n{tc[1]}(c) {tc[2]}six sides'
    )

prompt = ('b','c','b','a','c','c','a')

score = 0
loop = 0

while loop <= 6:

    os.system(tc[7])
    button = input((tc[1])+'\nKnow Your Stuff!\n\n'+(tc[2])+'Know Your Polygons\n\n'+\
    question_prompts1[loop]+'\n\n'+(tc[0])+'READY:'+(tc[1])).strip()

    if button == (prompt[loop]):
        score += 1

    loop += 1

    os.system(tc[7])

print(f'\n{tc[2]}Know Your Polygons\n\n{tc[2]}You got \
{score}/{len(question_prompts1)} questions correct.\nCongratulations! Your total \
Prize Winnings: {tc[1]}${score*100*score:,}.00 {tc[2]}Dollars.\n\n{tc[0]}READY:')

input('\nEND OF PROGRAM! Press Enter to quit.')

# TKINTER:

# Welcome to tkinter, the canvas part of Python. With tkinter you can draw lines and shapes
# such as ovals, arcs and rectangles. You can also create some wild digital string-art designs
# with for-loops. With tkinter you can also create buttons and input boxes. We will get into all
# this and more about tkinter, the fun part of Python programming.

# Let's create a simple tkinter window. Type and execute/run
# this tkinter program example below and see what happens.

from tkinter import*

root = Tk()

# This simple tkinter program will create an empty window, which
# is 500 X 500 pixels. Type and execute/run this tkinter program
# example below and see# what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500)
draw.pack()

root.mainloop()

# So far the tkinter window is empty; no canvas colours or anything,
# but a simple grayed out, empty tkinter window. Now, let's add colour
# to our empty tkinter window to sort of see where we are going with
# tkinter. Type and execute/run the tkinter program example below and
# see what happens when we add the colour black to our empty tkinter
# window.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.pack()

root.mainloop()

# Now that we have our empty tkinter window, which is now a
# black, empty tkinter window. Let's add a simple, blue diagonal
# line drawing inside our black, empty tkinter window and see
# what happens when you execute/run the tkinter program
# example below.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.create_line(0,0,500,500,fill = 'blue')
draw.pack()

root.mainloop()

# Note: hexadecimal values can also be used with the tkinter
# canvas colour as well as the tkinter graphics colour scheme
# alike. All hexadecimal values in Python startswith the '#' number
# sign, then preceding with a six digit hexadecimal number to
# the right, for example '#000000' = black, '#ffffff' = white. See
# below, a basic hexadecimal RGB colour codes list as follows:

# Black = '#000000'
# White = '#ffffff'
# Red = '#ff0000'
# Green = '#00ff00'
# Blue = '#000fff'
# Yellow = '#fff000'
# Pink = '#ff00ff'
# Cyan = '#00ffff'

# Now let's add another diagonal line in the tkinter window and
# colour it red and change the background colour to the hexadecimal
# colour code, black. type and execute/run the tkinter program
# example below and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = '#000000')
draw.create_line(0,0,500,500,fill = 'blue')
draw.create_line(0,500,500,0,fill = 'red')
draw.pack()

root.mainloop()

# Let's now draw a complete yellow square right in the middle of
# our X-shaped lines and see what happens when you execute/run
# the tkinter program example below.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.create_line(0,0,500,500,fill = 'blue')
draw.create_line(0,500,500,0,fill = 'red')
draw.create_line(50,50,450,50,450,50,450,450,50,450,50,50,fill = 'yellow')
draw.pack()

root.mainloop()

# Now let's make all the lines in our tkinter drawing thicker.
# Type and execute/run the tkinter program example below
# and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.create_line(0,0,500,500,fill = 'blue',width = 5)
draw.create_line(0,500,500,0,fill = 'red',width = 5)
draw.create_line(50,50,450,50,450,50,450,450,50,450,50,50,fill = 'yellow',width = 5)
draw.pack()

root.mainloop()

# Let's draw a simple rectangle with tkinter's 'rectangle' command.
# Type and execute/run the tkinter program example below and
# see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.create_rectangle(150,100,340,400,outline = 'cyan',width = 5)
draw.pack()

root.mainloop()

# Let's fill the inside of the rectangle with the colour red.
# Type and execute/run the tkinter program example below
# and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.create_rectangle(150,100,340,400,fill = 'red',outline = 'cyan',width = 5)
draw.pack()

root.mainloop()

# Let's draw a simple oval with tkinter's 'oval' command.
# Type and execute/run the tkinter program example below
# and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.create_oval(150,100,340,400,fill = 'red',outline = 'cyan',width = 5)
draw.pack()

root.mainloop()

# Let's draw a simple arc with tkinter's 'arc' command.
# Type and execute/run the tkinter program below and
# see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
draw.create_arc(120 ,120,400,400,extent = 180,fill = 'red',outline = 'cyan',width = 5)
draw.pack()

root.mainloop()

# Now let's create a tkinter digital string-art design using a
# for-loop. Type and execute/run the tkinter program example
# below and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
for i in range(0,400,3):
    draw.create_line(50+i,50+i,450,50,450,50,450,450,50,450,50+i,50+i,fill = 'cyan')
draw.pack()

root.mainloop()

# Now let's create a tkinter digital string-art design using a tkinter
# 'rectangle' command with a for-loop. Type and execute/run the
# tkinter program example below and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
for i in range(0,96,5):
    draw.create_rectangle(150+i,100+i,340-i,400-i,outline = 'cyan')
draw.pack()

root.mainloop()

# Now let's create a tkinter digital string-art design using a tkinter
# 'oval' command with a for-loop. Type and execute/run the tkinter
# program example below and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
for i in range(0,96,5):
    draw.create_oval(150+i,100+i,340-i,400-i,outline = 'cyan')
draw.pack()

root.mainloop()

# Now let's create a tkinter digital string-art design using a tkinter
# 'arc' command with a for-loop. Type and execute/run the tkinter
# program example below and see what happens.

from tkinter import*

root = Tk()

draw = Canvas(root,height = 500,width = 500,bg = 'black')
for i in range(0,140,5):
    draw.create_arc(120+i ,120+i,400-i,400-i,extent = 180,outline = 'cyan')
draw.pack()

root.mainloop()

# Let's import an image from your computer with tkinter. See what
# happens when you type and execute/run the tkinter program
# example below.

from tkinter import*

root = Tk()

photo = PhotoImage(file = 'C:\\Users\\JCR\\Documents\\Pictures\\image.jpg')
label = Label(root,image = photo)
label.pack()

root.mainloop()

# Let's set the canvas width and the canvas height, then import
# an image from your computer with tkinter. See what happens
# when you type and execute/run the tkinter program example
# below.

from tkinter import*

root = Tk()

canvas = Canvas(width = 600,height = 600,bg = 'blue')
canvas.pack()

photo = PhotoImage(file = 'C:\\Users\\JCR\\Documents\\Pictures\\image.jpg')
canvas.create_image(300,300,image = photo)

root.mainloop()

# Let's add anchoring to an image and position it in the center of the
# canvas. The anchor emitter has up to nine positional value settings:
# CENTER, N, S, E, W, NW, NE, SW, SE. See what happens when you
# type and execute/run the tkinter program example below.

from tkinter import*

root = Tk()

canvas = Canvas(width = 600,height = 600,bg = 'blue')
canvas.pack()

photo = PhotoImage(file = 'C:\\Users\\JCR\\Documents\\Pictures\\image.jpg')
canvas.create_image(300,300,image = photo,anchor = CENTER)

root.mainloop()

# Let's create a button with tkinter and see what happens when
# you type and execute/run the tkinter program example below.

from tkinter import*

button = Tk()

button.geometry('500x500')
button_1 = Button(button,text = 'Click Me!')
button_1.pack()

button.mainloop()

# Let's create a label for our tkinter button and see what happens
# when you type and execute/run the tkinter program example below.

from tkinter import*

button = Tk()

button.geometry('500x500')
label_1 = Label(button,text = ' "Python Programmer\'s Glossary Bible" ')
button_1 = Button(button,text = 'Click Me!')
label_1.pack()
button_1.pack()

button.mainloop()

# Let's make the tkinter button call the label with a 'def' function.
# Every time the 'Click Me!' button is clicked, the 'def' function gets
# called and the label is displayed again. See what happens when
# you type and execute/run the tkinter program example below.

from tkinter import*

button = Tk()

def call_the_def_function():
    label_1 = Label(button,text = ' "Python Programmer\'s Glossary Bible" ')
    label_1.pack()

button.geometry('500x500')
button_1 = Button(button,text = 'Click Me!',command = call_the_def_function)
button_1.pack()

button.mainloop()

# Let's reposition the tkinter button and its label by invoking the 'side =
# TOP' statement for the label and the 'side = LEFT' statement for the
# tkinter button. See what happens when you type and execute/run the
# tkinter program example below.

from tkinter import*

button = Tk()

def call_the_def_function():
    label_1 = Label(button,text = ' "Python Programmer\'s Glossary Bible" ')
    label_1.pack(side = TOP)

button.geometry('500x500')
button_1 = Button(button,text = 'Click Me!',command = call_the_def_function)
button_1.pack(side = LEFT)

button.mainloop()

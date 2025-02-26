# Easy print() function Python program examples with
# variables and their values. For those, who are just
# starting Python or any other computer programming
# language, a variable is a container that holds a value
# much like a box that can hold stuff. A variable is any
# text letters you want to use, along with an equals = sign
# and a value. The value is what you see on the screen
# at execution/run time. You can name variables any name
# or letters you please. However, if you want more than
# one word such as 'hello world' to be a variable name,
# you must use an underscore _ such as this example
# below:

hello_world = "I'm the value you see on the output screen."

print(hello_world)

# Note: you can use numbers within variables, but you
# cannot use numbers alone for variables and you cannot
# create variables with numbers in front of them. Here are
# some example ways to create variables, combined with
# numbers.

# the right way:

variable1 = 'value'

variable_1 = 'value'

# the wrong way:

1 = 'value'

1variable = 'value'

1_variable = 'value'

# Tip: Sometimes, it's a greate idea to create variables combined
# with numbers. Most times, you might want to use variables
# combined with numbers if you are naming more than one
# variable the same name, but a different letter or different number
# anywhere within the variable names that will make them different
# from one another. Note: all variable names are case sensitive,
# meaning they are different names if you use capital letters and
# non-capital letters. For example: varaiable a = and variable A =
# are two, different variable names. take a look at the examples
# below:

a = "I'm the value that belongs to the varaible (a)"

A = "I'm the value that belongs to the varaible (A)"

print(a)

print(A)

name1 = 'Rob'

name2 = 'Bob'

print(name1)

print(name2)

# Use the underscore _ to create nice spaces between character
# names or character names combined with numbers if you like.

name_1 = 'Rob'

name_2 = 'Bob'

print(name_1)

print(name_2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can also create variables that can use other variables as
# their values. For example:

name1 = 'Rob'

name2 = 'Bob'

person1 = name1

person2 = name2

print(person1)

print(person2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tip: you do not need any spaces between variables and their =
# equals signs, nor their values alike. For example:

variable1='value'

variable_1='value1'

print(variable1)

print(variable_1)

variable255twothree='value'

variable_255_two_three='value'

print(variable255twothree)

print(variable_255_two_three)

# Tip: If you are just starting out into computer programming, I
# strongly suggest that you create spaces in between your variables,
# their = equals signs and their values alike to create clean and
# recognizable computer programming code, until you become
# accustom to computer programming in any programming language
# you choose, including Python; the computer programming language
# I chose to learn, to use and to teach others while teaching myself
# all this Object Oriented Python programming language stuff.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now learn how to unpack multiple variables with one equals =
# sign and their separate values. For example:

a,b,c = 'Apple value','Banana value','Cherry value'

print(a)

print(b)

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create variables that can store and calculate number values.

a = 2

b = 6

print(a+b)

print(b-a)

print(a*b)

print(b/a)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a tuple by default without parentheses, and then
# call each value by its index number. For example:

Monster_Variable = 'Value One','Value Two','Value Three','Value Four','Value Five'

print(Monster_Variable[0])

print(Monster_Variable[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a tuple with parentheses, and then call each value
# by its index number. For example:

Monster_Variable_tuple = ('Value One','Value Two','Value Three','Value Four','Value Five')

print(Monster_Variable_tuple[0])

print(Monster_Variable_tuple[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a list with square brackets, and then call each value
# by its index number. For example:

Monster_Variable_list = ['Value One','Value Two','Value Three','Value Four','Value Five']

print(Monster_Variable_list[0])

print(Monster_Variable_list[4])

# To learn more about tuples and lists, please watch my Python
# video manual called 'Learn Variables in Python'.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a dictionary with curly braces, and then get each value
# by its key. For example:

Monster_Variable_dictionary = {'key1':'Value One','key2':'Value Two','key3':'Value Three'}

print(Monster_Variable_dictionary.get('key1'))

print(Monster_Variable_dictionary.get('key2'))

print(Monster_Variable_dictionary.get('key3'))

print(Monster_Variable_dictionary.get('key4','value not found:'))  # optional

# To learn more about dictionaries, please watch my Python video
# manual called 'Learn Variables in Python'.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a set with curly braces. Note: sets do not use indexing
# at all; they are in random order and get rid of any duplicate values,
# whereas tuples, lists and dictionaries don't get rid of duplicate values.
# For example:

Monster_Variable_set = {'Value One','Value Two','Value Three','Value Four','Value Five'}

print(Monster_Variable_set)


Monster_Variable_set = {'Value One','Value Two','Value Three','Value Four','Value Five','Value One'}

print(Monster_Variable_set)

# To learn more about sets, please watch my Python video manual
# called 'Learn Variables in Python'.

# The reasons why computer programmers use variables instead of
# actual text within print() functions and such. Variables make
# programming more efficient and far less code redundant on the
# programmer's part. Variables can also be used to manipulate user
# interaction within a computer program. And most importantly,
# variables are great, that if you make spelling mistakes in someone's
# name, you can quickly correct it. For example:

name = 'Ssam'

print(f'Hi {name}. How are you?')


name = 'Sam'

print(f'Hi {name}. How are you?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use what we've learned about variables and have some fun and
# experiment with variables and their values alike.

name1 = 'Bob'
name2 = 'Rob'
name3 = 'Terry'
name4 = 'Mary'

print(f"Hello. My name is {name1}. What's your name?")

print(f"Hello. My name is {name2}. What's your name?")

print(f"Hello. My name is {name3}. What's your name?")

print(f"Hello. My name is {name4}. What's your name?")

print(f'{name1} and his friend {name2} are going to the store.')

print(f'{name3} and her friend {name4} are going to the store.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create variables that calculate numbers.

num1 = 10
num2 = 5
num3 = 2

print(num1+num2-num3)

print(num1*num2/num3)

# Let's pack the variables above to create one, single line of Python code.

num1,num2,num3 = 10,5,2

print(num1+num2-num3)

print(num1*num2/num3)

# When you use variables to store number values, they calculate
# with the rules of BEDMAS, just like real numbers do in our everyday
# world. All calculators dictate the rules of BEDMAS, regardless if
# you know it or not. Search math subjects about BEDMAS to learn
# more.

num1,num2,num3 = 10,5,2

print(num1+num2*num3)

print(num1*num2-num3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's have some BONUS fun with what we've learned about variables
# and their values alike. Let's create some for loop examples, using
# tuples, lists and dictionaries.

# this is a tuple by default, without parentheses

Monster_Variable = 'Value One','Value Two','Value Three','Value Four','Value Five'

for i in Monster_Variable:
    print(f'I am {i}')

# this is a tuple with parentheses ( )

Monster_Variable_tuple = ('Value One','Value Two','Value Three','Value Four','Value Five')

for i in Monster_Variable_tuple:
    print(f'I am {i}')

# this is a list with square brackets [ ]

Monster_Variable_list = ['Value One','Value Two','Value Three','Value Four','Value Five']

for i in Monster_Variable_list:
    print(f'I am {i}')

# this is a dictionary with curly braces { }

Monster_Variable_dictionary = {'key1':'Value One','key2':'Value Two','key3':'Value Three'}

for i in Monster_Variable_dictionary:
    print(Monster_Variable_dictionary.get(i))

# Let's use numbers as keys, so we can do the following Python
# program example:

Monster_Variable_dictionary = {1:'Value One',2:'Value Two',3:'Value Three'}

for i in Monster_Variable_dictionary:
    print(Monster_Variable_dictionary.get(i))

print(Monster_Variable_dictionary.get(i+1,'key not found:'))

print(Monster_Variable_dictionary.get(i-1,'key not found:'))

# Now that you have quite a brief idea of what variables and values
# are in computer programming. Why not search all my other Python
# programming video manuals to learn so much more at your very
# own pace. Because great programming always starts with a great
# programmer's manual. Please check out my Python Programmer's
# Glossary Bible by Joseph C. Richardson. You can also find me on
# GitHub.com under the username Robomaster S1 to gain full access
# to my entire Python research studies.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bonus: Heads up, Head start! Let's unpack variables that have value
# groups. Each value group has one, extra value in it than the other.
# Call each variable, along with its grouped values by their index number.
# Note: you can use outside parentheses to achieve the following
# code layout to stop code from wrapping around on the screen.

a,b,c = (
    ('a0','a1','a2','a3'),
    ('b0','b1','b2','b3','b4'),
    ('c0','c1','c2','c3','c4','c5'))  # tuple( ) value groups

print(a[0],b[0],c[0])

print(a[1],b[1],c[1])

print(a[2],b[2],c[2])


a,b,c = (
    ['a0','a1','a2','a3'],
    ['b0','b1','b2','b3','b4'],
    ['c0','c1','c2','c3','c4','c5'])  # list[ ] value groups

print(a[0],b[0],c[0])

print(a[1],b[1],c[1])

print(a[2],b[2],c[2])

# Let's unpack variables that have value groups. Each value group
# has one, extra value in it than the other. Call each variable, along
# with its grouped values by their keys. Note: you can use outside
# parentheses to achieve the following code layout to stop code
# from wrapping around on the screen.

a,b,c = (
    {'key1':'a1','key2':'a2','key3':'a3'},
    {'key1':'b1','key2':'b2','key3':'b3','key4':'b4'},
    {'key1':'c1','key2':'c2','key3':'c3','key4':'c4','key5':'c5'})  # dictionary{ } value groups

print(a.get('key1'))

print(b.get('key2'))

print(c.get('key3'))

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

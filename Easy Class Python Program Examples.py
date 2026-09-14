
# Easy Class Python Program Examples:

# by Joseph C. Richardson,GitHub.com

# These Easy Classes are designed for the novice/beginner.

# These easy class Python program examples show step by
# step ways to create classes. This lesson clearly shows
# manual, redundant ways to create Python classes. These
# redundant print() functions show how print() functions work
# in classes, so the novice/beginner can learn to not only create
# classes. But the novice/beginner can also learn why classes
# work in the first place. As we go, we will learn how to keep our
# code completely DRY!: (Don't Repeat Yourself!). For now, let's
# take things slow and easy. Most importantly. Do not over
# concentrate. Take your time to learn Python. Now, let's WAX
# on and WAX off. Shall we...

# First of all, we must learn the three parts that make up a class.
# The class blueprint or empty template looks like this example
# below. The word 'self' can be any name you wish to use. How-
# ever, programmers use 'self' as the standard. The 'self' word
# is an address in memory that points back to its attribute, so it
# can be accessible to itself. The class constructor __init__
# initiates the attributes of an instance to gain access to arguments
# within an instance of a class. Class constructors can also be
# called dunder methods or magic methods. However, the term
# class constructor is the true name. Two double underscores
# __ __ are required to create class constructors. Simply press
# and hold down the shift key, while pressing the minus key.

# The attribute, like a feature someone has, such as brown hair,
# blue eyes; anything about their appearance are their attributes.
# In our first example, we only have one attribute property, but we
# didn't put any features into it yet. We need to create an instance
# for this class, along with its attribute's name:

# print(Easy_class('Hello').attribute)

# Please note: arguments are nothing more than the values you
# see on a computer's monitor at run time, such as the word 'Hello'
# that prints out onto the screen when you type and execute/run
# this Python program example below.

class Easy_class:

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one attribute

print(Easy_class('Hello').attribute)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's type and execute/run this same Easy_class Python program
# example. This time we will create a variable called easy_class_value
# so we can store the instance in it.

class Easy_class:

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one attribute property

print(Easy_class('Hello').attribute)  # Hello

# or this:

easy_class_value = Easy_class('Hello')  # Create a variable to store the instance.

print(easy_class_value.attribute)  # Hello

# or this:

easy_class_value = Easy_class('Hello').attribute  # Create a variable to store the instance along with its attribute.

print(easy_class_value)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's type and execute/run this Easy_class Python program
# example. This time, we have two attribute properties and two
# arguments, Hello and World! The two print() functions demonstrate
# how two attribute extensions: attribute1 and attribute2 are invoked
# at the end of the two print() functions.

class Easy_class:

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two attribute properties

print(Easy_class('Hello','World!').attribute1)  # Hello

print(Easy_class('Hello','World!').attribute2)  # World!

# or this:

easy_class_values = Easy_class('Hello','World!')  # Create a variable to store the instance.

# Invoke a + sign or a comma to concatenate strings together.

print(easy_class_values.attribute1+easy_class_values.attribute2)  # HelloWorld!

print(easy_class_values.attribute1,easy_class_values.attribute2)  # Hello World!

# or this:

easy_class_values = Easy_class('Hello','World!').attribute1,Easy_class('Hello','World!').attribute2

# Invoke a + sign or a comma to concatenate strings together.

print(easy_class_values[0]+easy_class_values[1])  # HelloWorld!

print(easy_class_values[0],easy_class_values[1])  # Hello World!

# or this:

easy_class_values = (
  Easy_class('Hello','World!').attribute1,
  Easy_class('Hello','World!').attribute2)

print(easy_class_values[0]+easy_class_values[1])  # HelloWorld!

print(easy_class_values[0],easy_class_values[1])  # Hello World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do this again, but we will use the very last way and the
# shortest way to create code. We will also add two more attributes
# to our very same class examples, as shown above.

class Easy_class:

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3
    self.attribute4 = attribute4  # four attribute properties

easy_class_values = (
  Easy_class('Hello','World!','Computer','Science.').attribute1,
  Easy_class('Hello','World!','Computer','Science.').attribute2,
  Easy_class('Hello','World!','Computer','Science.').attribute3,
  Easy_class('Hello','World!','Computer','Science.').attribute4)

# Invoke a + sign or a comma to concatenate strings together.

print(
  easy_class_values[0]+
  easy_class_values[1]+
  easy_class_values[2]+
  easy_class_values[3])  # HelloWorld!ComputerScience

print(
  easy_class_values[0],
  easy_class_values[1],
  easy_class_values[2],
  easy_class_values[3])  # Hello World! Computer Science
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for loop that increments through a tuple of values.

class Easy_class:

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3
    self.attribute4 = attribute4  # four attribute properties

easy_class_values = (
  Easy_class('Hello','World!','Computer','Science.').attribute1,
  Easy_class('Hello','World!','Computer','Science.').attribute2,
  Easy_class('Hello','World!','Computer','Science.').attribute3,
  Easy_class('Hello','World!','Computer','Science.').attribute4)

for i in easy_class_values:
  print(i)

# or invoke the end='' suffix to keep text on one line.

for i in easy_class_values:
  print(i,end='')  # HelloWorld!ComputerScience.

# or this:

for i in easy_class_values:
  print(i,end=' ')  # Hello World! Computer Science.

# or this:

for i in easy_class_values:
  print(i,end=' space ')  # Hello space World! space Computer space Science. space
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Stay DRY: Don't Repeat Yourself. Let's create a default tuple
# of values so we don't have to repeat attribute values over and over.

class Easy_class:

  def __init__(self,attribute1,attribute2,attribute3,attribute4): # five parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3
    self.attribute4 = attribute4  # four attribute properties

arg_placeholder_value = 'Hello','World!','Computer','Science.'  # no more repeated attribute values

easy_class_values = (
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute1,
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute2,
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute3,
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute4)

print(easy_class_values[0])  # Hello

print(easy_class_values[1])  # World!

print(easy_class_values[2])  # Computer

print(easy_class_values[3])  # Science.

# or this:

for i in easy_class_values:
  print(i,end=' ')  # Hello World! Computer Science.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create implicit attribute values with our very same class
# example above.

class Easy_class:

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'
    self.attribute3 = 'Computer'
    self.attribute4 = 'Science.'  # four attribute properties with four implicit arguments

arg_placeholder_value = '','','',''  # no more repeated implicit attribute values

easy_class_values = (
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute1,
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute2,
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute3,
  Easy_class(arg_placeholder_value[0],arg_placeholder_value[1],arg_placeholder_value[2],arg_placeholder_value[3]).attribute4)

print(easy_class_values[0])  # Hello

print(easy_class_values[1])  # World!

print(easy_class_values[2])  # Computer

print(easy_class_values[3])  # Science.

# or this:

for i in easy_class_values:
  print(i,end=' ')  # Hello World! Computer Science.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create four implicit attributes with one, single attribute
# property. Let's also create a for loop to keep our code DRY.

class Easy_class:

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

    self.attribute = 'Hello','World!','Computer','Science.'  # one attribute property with four implicit arguments

arg_placeholder_value = '','','',''  # no more repeated implicit attribute values

DRY = Easy_class(
  arg_placeholder_value[0],
  arg_placeholder_value[1],
  arg_placeholder_value[2],
  arg_placeholder_value[3])

# Invoke the try and except IndexError handler to catch index range
# errors, without crashing this Python program example.

try:
  for i in range(5):
    print(DRY.attribute[i],end=' ')  # Hello World! Computer Science.
except IndexError:
  print('\nIndex Range Error:')

# or this:

try:
  for i in range(5):
    print(DRY.attribute[i],end=' ')  # Hello World! Computer Science.
except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what *args and **kwargs do. These are easy, once
# you learn them. We will take it step by step, like we did before.
# Invoke the asterisk * in front of the *args attribute. Note: *args
# can be any name you wish. However, the Python standard is
# invoked as *args for its name, which is short for the name
# 'arguments'.

# With *args, we don't have to worry about how many parameters
# we need to satisfy how many arguments we need as we had to
# before. *args are great when there are far too many arguments
# needed to satisfy the exact number of parameter values.

class Easy_class:

  def __init__(self,*args):  # two parameters

    self.args = args  # one attribute

print(Easy_class('Hello','World!','Computer','Science.').args[0])  # Hello

print(Easy_class('Hello','World!','Computer','Science.').args[1])  # World!

print(Easy_class('Hello','World!','Computer','Science.').args[2])  # Computer

print(Easy_class('Hello','World!','Computer','Science.').args[3])  # Science.

# or this:

easy_class_values = Easy_class('Hello','World!','Computer','Science.')

# Invoke the try and except IndexError handler to catch index range
# errors, without crashing this Python program example.

try:
  for i in range(5):
    print(easy_class_values.args[i],end=' ')  # Hello World! Computer Science.
except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's see what **kwargs do. Invoke the double asterisk ** in
# front of the **kwargs attribute. Note: **kwargs can be any name
# you wish. However, the Python standard is invoked as **kwargs
# for its name, which is short for the name 'keyword_arguments'.

# With **kwargs, we don't have to worry about how many parameters
# we need to satisfy how many keyword arguments we need as we
# had to before. **kwargs are great when there are far too many keyword
# arguments needed to satisfy the exact number of parameter values.

class Easy_class:
  def __init__(self,**kwargs):

    self.kwargs = kwargs

# Invoke the try and except KeyError handler to catch keyword
# argument errors and keyword argument index errors without
# crashing this Python program example.

try:
  print(Easy_class(kwargs = 'Hello').kwargs['kwargs1','Error! Not to worry...'])
except KeyError:
  print('Value not found:')

# or this:

try:
  print(Easy_class(kwargs = 'Hello').kwargs['kwargs1','Error! Not to worry...'])
except KeyError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's invoke the .get() function so we don't have to use an
# error handler, which also creates less code for us to write.

class Easy_class:
  def __init__(self,**kwargs):

    self.kwargs = kwargs

# Notice how keyword arguments also reside within the instance?

# Easy_class(kwargs = 'Hello').kwargs.get('kwargs')

print(Easy_class(kwargs = 'Hello').kwargs.get('kwargs'))

# or this:

print(Easy_class(kwargs = 'Hello').kwargs.get('kwargs','Value not found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  def __init__(self,**kwargs):

    self.kwargs = kwargs

print(
  Easy_class(
    kwargs1 = 'Hello',
    kwargs2 = 'World!').kwargs.get('kwargs1','Attribute Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  def __init__(self,**kwargs):

    self.kwargs = kwargs

print(
  Easy_class(
    kwargs1 = 'Hello',
    kwargs2 = 'World!',
    kwargs3 = 'Computer',
    kwargs4 = 'Science.').kwargs.get('kwargs4','Attribute Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to break Python's standard naming convention
# rules. Please note: the boss wouldn't be too happy when breaking
# such naming convention rules in Python syntax. Let's use some
# of our early Python class examples of what not to do in Python
# or any other programming languages. Let's change the word 'self'
# to 'selfie'

class Easy_class:

  def __init__(selfie,attribute):  # two parameters

    selfie.attribute = attribute  # one attribute

print(Easy_class('Hello').attribute)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:

  def __init__(selfie,*arguments):  # two parameters

    selfie.arguments = arguments  # one attribute

print(Easy_class('Hello','World!','Computer','Science.').arguments[0])  # Hello

print(Easy_class('Hello','World!','Computer','Science.').arguments[1])  # World!

print(Easy_class('Hello','World!','Computer','Science.').arguments[2])  # Computer

print(Easy_class('Hello','World!','Computer','Science.').arguments[3])  # Science.

# or this:

easy_class_values = Easy_class('Hello','World!','Computer','Science.')

# Invoke the try and except IndexError handler to catch index range
# errors, without crashing this Python program example.

try:
  for i in range(5):
    print(easy_class_values.arguments[i],end=' ')  # Hello World! Computer Science.
except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  def __init__(selfie,**keyword_arguments):

    selfie.keyword_arguments = keyword_arguments

# Notice how keyword arguments also reside within the instance?

# Easy_class(kwargs = 'Hello').kwargs.get('kwargs')

print(Easy_class(keyword_arguments = 'Hello').keyword_arguments.get('kwargs'))

# or this:

print(Easy_class(keyword_arguments = 'Hello').keyword_arguments.get('kwargs','Value not found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# We can also use different variable names in attribute properties.
# For example:

class Easy_class:

  def __init__(self,attribute1,attribute2):  # three parameters

    self.my_attribute1 = attribute1
    self.my_attribute2 = attribute2  # two attribute properties

print(Easy_class('Hello','World!').my_attribute1)  # Hello

print(Easy_class('Hello','World!').my_attribute2)  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a docstring for our last class act example. We
# need to invoke three double quote marks """ on each side of
# the docstring title: """Easy class""". The getattr() function
# simply means the word: 'get attribute'. With docstrings, we
# can see the documentation payload/description block of the
# class at execution/run time.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one attribute

print(getattr(Easy_class,'__doc__'))  # Easy class

print(Easy_class('Hello').attribute)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# BONUS LESSON!

# Let's learn what __slots__ do! Slots reserve exact memory
# for class attributes. You don't need a huge, empty warehouse
# just to store a few attributes. Slots optimize memory and performance.
# Research Python __slots__ to learn more about them. Two double
# underscores __ __ are required to create __slots__. Simply
# press and hold down the shift key, while pressing the minus key.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute1','attribute2')  # __slots__ optimizes memory and performance

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two attribute properties

print(getattr(Easy_class,'__doc__'))  # Easy class

print(Easy_class('Hello','World!').attribute1)  # Hello

print(Easy_class('Hello','World!').attribute2)  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These two Python command lines below are what are called
# 'instances'. The green text, 'Hello' and 'World!' are the actual
# arguments you see on the computer screen at execution/run
# time. Any text you see on the screen at execution/run time,
# are the actual arguments every easy class Python program
# illustrated here. All the green text are the actual 'arguments'.

Easy_class('Hello','World!').attribute1  # Hello

Easy_class('Hello','World!').attribute2  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Well, that's all folks! We are at the end of this grueling Python
# programming lesson on Python classes. I sure hope I've cleared
# the fog and set the path for the novice/beginner to follow...

# Believe me, this last part of our lesson on Easy Classes wasn't
# so easy for me to create, as well as creating comments for
# these last two lessons from docstrings, onward to __slots__.
# I am heading into my ninth year into Python programming, since
# Christmas day, 2017. And it was all because of my Best Friend,
# Brian, who lit the fire inside me to take up computer programming
# again. He introduced me to that little Cozo Robot, and I haven't
# looked back since that day...


# Easy Class Python Program Examples Two:

# by Joseph C. Richardson,GitHub.com

# These Easy Classes are designed for the novice/beginner.

# These easy class Python program examples show step by step
# ways to create classes. Please note: for those who haven't yet
# studied Easy Class Python Program Examples first; it is highly
# recommended that you do so.

# Here is a constant reminder: a class is an object, and an attribute
# is a class object's feature, or part of a class object. These parts
# of a class object are called 'attribute properties'. The attribute, like
# a feature someone has, such as brown hair, blue eyes; anything
# about their appearance are their attributes. In our first example,
# we only have one attribute property, but we didn't put any features
# into it yet. We need to create an instance for this class, along
# with its attribute's name:

# print(Easy_class('Hello').attribute)

# Let's create docstrings for our easy class Python program examples.
# We need to invoke three double quote marks """ on each side
# of the docstring title: """Easy class""". The getattr() function
# simply means the word: 'get attribute'. With docstrings, we can
# see the documentation payload/description block of the class
# at execution/run time.

# As we go, we will learn how to keep our code completely DRY!:
# (Don't Repeat Yourself!). For now, let's take things slow and easy.
# Most importantly. Do not over concentrate. Take your time to
# learn Python. Now, let's WAX on and WAX off. Shall we...

# Please note: arguments are nothing more than the values you
# see on a computer's monitor at run time, such as the word 'Hello'
# that prints out onto the screen when you type and execute/run
# this Python program example below:

# Let's learn what 'documentation strings' do with classes. In Python,
# we call these 'doctrings'. We  need to invoke three double quote
# marks """ on each side of the docstring title: """Easy class""".
# The getattr() function simply means the word: 'get attribute'. With
# docstrings, we can see the documentation payload/description
# block of the class at execution/run time. Docstrings are like a
# comment; they descibe what the class is about at execution/run
# time.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one explicit attribute

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Below is our 'instance', along with its argument value: 'Hello'
# and its attribute name: 'attribute'

print(Easy_class('Hello').attribute)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# We can also create 'implicit attributes', where the actual value
# 'Hello' is set as an attribute property. We only need to add an
# 'argument placeholder value' in our instance, along with its
# attribute name, called 'attribute'. We can name attributes any
# names we wish. However, in our lesson on easy class Python
# program examples, we will use the attribute name as 'attribute',
# like we did in our Easy Class Python Program Examples: volume
# one.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  def __init__(self,attribute):  # two parameters

    self.attribute = 'Hello'  # one implicit attribute

print(getattr(Easy_class,'__doc__'))  # Easy class

print(Easy_class('argument placeholder value').attribute)  # Hello

# or this:

print(Easy_class('').attribute)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  """Easy class"""  # documentation payload/description block

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attributes

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Below is our 'instances', along with their two argument values: 'Hello'
# and 'World!' with their attribute names: 'attribute1' and attribute2.

print(Easy_class('Hello','World!').attribute1)  # Hello

print(Easy_class('Hello','World!').attribute2)  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the implicit version of the same class example above.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attributes

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Below is our 'instances', along with their two argument values: 'Hello'
# and 'World!' with their attribute names: 'attribute1' and attribute2.

print(Easy_class('argument placeholder value','argument placeholder value').attribute1)  # Hello

print(Easy_class('argument placeholder value','argument placeholder value').attribute2)  # World!

# or this:

print(Easy_class('','').attribute1)  # Hello

print(Easy_class('','').attribute2)  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's get out of this downpour of redundant code and get
# lazy and DRY: (Don't Repeat Yourself). Let's do the same class
# example above, but this time, we will create a for loop with only
# one print() function. The for loop will increment the two instance
# attributes into one print() function alone. We need to also create
# a tuple named: 'easy_class_values' to store our two attributes,
# attribute1 and attribute2. Let's also invoke the end=' ' suffix to
# keep our text output on one line only.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attributes

easy_class_values = (
  Easy_class('Hello','World!').attribute1,
  Easy_class('Hello','World!').attribute2)

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

for i in easy_class_values:
  print(i,end=' ')  # Hello World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the implicit version of the same class example above.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attributes

easy_class_values = (
  Easy_class('argument placeholder value','argument placeholder value').attribute1,
  Easy_class('argument placeholder value','argument placeholder value').attribute2)

# or this:

easy_class_values = (
  Easy_class('','').attribute1,
  Easy_class('','').attribute2)

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

for i in easy_class_values:
  print(i,end=' ')  # Hello World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's type a small paragraph with docstrings only. We will create
# an empty class this time, without attribute properties to illustrate
# commented output about the class object description on the
# screen

class Easy_class:
  """Docstrings are so much fun.
They are so easy to create."""  # documentation payload/description block

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what __slots__ do! Slots reserve exact memory
# for class attributes. You don't need a huge, empty warehouse
# just to store a few attributes. Slots optimize memory and performance.
# Research Python __slots__ to learn more about them. Two double
# underscores __ __ are required to create __slots__. Simply
# press and hold down the shift key, while pressing the minus key.

# Note: when invoking __slots__ with only one attribute, you must
# place a comma ',' at the end of the slot's single attribute, as not
# to confuse it as a tuple value at execution/run time.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute',)  # __slots__ optimizes memory and performance

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one explicit attribute

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Below is our 'instance', along with its argument value: 'Hello'
# and its attribute name: 'attribute'

print(Easy_class('Hello').attribute)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute',)  # __slots__ optimizes memory and performance

  def __init__(self,attribute):  # two parameters

    self.attribute = 'Hello'  # one implicit attribute

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Below is our 'instance', along with its argument value: 'Hello'
# and its attribute name: 'attribute'

print(Easy_class('argument placeholder value').attribute)  # Hello

# or this:

print(Easy_class('').attribute)  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute1','attribute2')  # __slots__ optimizes memory and performance

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attributes

easy_class_values = (
  Easy_class('Hello','World!').attribute1,
  Easy_class('Hello','World!').attribute2)

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

for i in easy_class_values:
  print(i,end=' ')  # Hello World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the implicit version of the same class example above.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute1','attribute2')  # __slots__ optimizes memory and performance

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attributes

easy_class_values = (
  Easy_class('argument placeholder value','argument placeholder value').attribute1,
  Easy_class('argument placeholder value','argument placeholder value').attribute2)

# or this:

easy_class_values = (
  Easy_class('','').attribute1,
  Easy_class('','').attribute2)

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

for i in easy_class_values:
  print(i,end=' ')  # Hello World!
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
  """Easy class"""  # documentation payload/description block

  __slots__ = ('args',)  # __slots__ optimizes memory and performance

  def __init__(self,*args):  # two parameters

    self.args = args  # one explicit attribute

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

print(Easy_class('Hello','World!','Computer','Science.').args[0])  # Hello

print(Easy_class('Hello','World!','Computer','Science.').args[1])  # World!

print(Easy_class('Hello','World!','Computer','Science.').args[2])  # Computer

print(Easy_class('Hello','World!','Computer','Science.').args[3])  # Science.

# or this:

easy_class_values = Easy_class('Hello','World!','Computer','Science.')

# Invoke the try and except IndexError handler to catch index range
# errors, without crashing this Python program example.

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

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
  """Easy class"""  # documentation payload/description block

  __slots__ = ('kwargs',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):

    self.kwargs = kwargs

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Invoke the try and except KeyError handler to catch keyword
# argument errors and keyword argument index errors without
# crashing this Python program example.

try:
  print(Easy_class(kwargs = 'Hello').kwargs['kwargs1'])
except KeyError:
  print('Attribute not found:')

# or this:

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

try:
  print(Easy_class(kwargs = 'Hello').kwargs['kwargs1'])
except KeyError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's invoke the .get() function so we don't have to use an
# error handler, which also creates less code for us to write.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('kwargs',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):

    self.kwargs = kwargs

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Notice how keyword arguments also reside within the instance?

# Easy_class(kwargs = 'Hello').kwargs.get('kwargs')

print(Easy_class(kwargs = 'Hello').kwargs.get('kwargs'))

# or this:

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

print(Easy_class(kwargs = 'Hello').kwargs.get('kwargs','Attribute not found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('kwargs',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):

    self.kwargs = kwargs

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

print(
  Easy_class(
    kwargs1 = 'Hello',
    kwargs2 = 'World!').kwargs.get('kwargs1','Attribute Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('kwargs',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):

    self.kwargs = kwargs

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

print(
  Easy_class(
    kwargs1 = 'Hello',
    kwargs2 = 'World!',
    kwargs3 = 'Computer',
    kwargs4 = 'Science.').kwargs.get('kwargs4','Attribute Not Found:'))  # optional'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# BONUS LESSON FUN!

# Why use bulky try and except error handlers, when we can simply
# invoke the getattr() 'get attribute' function to make less lines of code,
# unlike a try and except error handler that requires more lines of code.

# You must add the attribute 'Fallback Attribute' as a FALLBACK, or you
# will get an attribute error. that will crash the program, execution/run.
# The getattr() 'get attribute' function takes place of the bulky try and
# except error handler block with far less Python code.

# print(getattr(Easy_class('Hello'),'attribute','Fallback Attribute'))

class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute',)  # __slots__ optimizes memory and performance

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one explicit attribute

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

print(getattr(Easy_class('Hello'),'attribute','Fallback Attribute'))  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute1','attribute2')  # __slots__ optimizes memory and performance

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attributes

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Below is our 'instances', along with their two argument values: 'Hello'
# and 'World!' with their attribute names: 'attribute1' and attribute2.

print(getattr(Easy_class('Hello','World!'),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class('Hello','World!'),'attribute2','Sorry! Attribute not found:'))  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the implicit version of the same class example above.

class Easy_class:
  """Easy class"""  # documentation payload/description block

  __slots__ = ('attribute1','attribute2')  # __slots__ optimizes memory and performance

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attributes

print(getattr(Easy_class,'__doc__'))  # docstring: Easy class

# Below is our 'instances', along with their two argument values: 'Hello'
# and 'World!' with their attribute names: 'attribute1' and attribute2.

print(getattr(Easy_class('',''),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class('',''),'attribute2','Sorry! Attribute not found:'))  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Well, that's all folks! We are at the end of this grueling Python
# programming lesson on Python classes. I sure hope I've cleared
# the fog and set the path for the novice/beginner to follow...

# To those who have learned Python through me. I may
# not speak in any of my Python manuals. I write better
# than I can speak, when it comes to explaining anything.
# However, I strive to bring others with me all the way, or
# we don't go at all! I'm no teacher by a longshot, but I
# will make sure what I learn through others about
# Python and computers in general. I will always make
# learning fun and easy, no matter the complexity of
# what I solve. I want to pass onward the torch of those
# who had taught me, when they once passed the torch
# onto me...

# I now pass onward the torch of which, I had learned to
# light, so I could light the way for others abound.

# Yours truly, Joe

# And please note: my grammar might not ever be the best
# and brightest. However, I make darn sure that my Python
# programing skills are solid steel. Nonetheless...

# I am almost a complete Walking Human Computer Science Research Laboratory Machine on Two Legs... 😁

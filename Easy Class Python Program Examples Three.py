
# Easy Class Python Program Examples Three:

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

# As we go, we will learn how to keep our code completely DRY!:
# (Don't Repeat Yourself!). For now, let's take things slow and easy.
# Most importantly. Do not over concentrate. Take your time to
# learn Python. Now, let's WAX on and WAX off. Shall we...

# Please note: arguments are nothing more than the values you
# see on a computer's monitor at run time, such as the word 'Hello'
# that prints out onto the screen when you type and execute/run
# this Python program example below:

# Lets create a simple easy class, and create a default tuple of
# different text string values, so we can reuse classes that have
# different text argument values in each instance we create from
# one, single class attribute alone.

arguments = 'Hello','World!','Computer','Science','is Fun!!!'

class Easy_class:

  def __init__(self,attribute):

    self.attribute = attribute  # one explicit attribute property

print(getattr(Easy_class(arguments[0]),'attribute','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class(arguments[1]),'attribute','Sorry! Attribute not found:'))  # World!

print(getattr(Easy_class(arguments[2]),'attribute','Sorry! Attribute not found:'))  # Computer

print(getattr(Easy_class(arguments[3]),'attribute','Sorry! Attribute not found:'))  # Science

print(getattr(Easy_class(arguments[4]),'attribute','Sorry! Attribute not found:'))  # is Fun!!!

# Let's keep it DRY! ( Don't Repeat Yourself! )

# Let's do the same class example as above, but we will create a
# for loop that will help us do away with redundant print() functions,
# while our Python code is short and sweet. Nice and DRY.

arguments = 'Hello','World!','Computer','Science','is Fun!!!'  # default tuple

class Easy_class:

  def __init__(self,attribute):

    self.attribute = attribute  # one explicit attribute property

for i in arguments:
  print(getattr(Easy_class(i),'attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# There are two types of classes that do not require try and except
# error handlers. Explicit and implicit attributes do not require try
# and except error handlers. Keyword arguments do not require try
# and except error handlers as well. Keyword arguments require
# the dictionary's .get() method. However, we can use bulky error
# handlers all you want. But why use them, when we can completely
# do without them?

class Easy_class:

  def __init__(self,attribute):

    self.attribute = attribute  # one explicit attribute property

print(getattr(Easy_class('Hello'),'attribute','Sorry! Attribute not found:'))  # Hello
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:

  def __init__(self,attribute):

    self.attribute = 'Hello'  # one implicit attribute property

print(getattr(Easy_class('argument placeholder value'),'attribute','Sorry! Attribute not found:'))  # Hello

# or this:

print(getattr(Easy_class(''),'attribut','Sorry! Attribute not found:'))  # optional: text for None
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attribute properties

print(getattr(Easy_class('Hello','World!'),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class('Hello','World!'),'attribute2','Sorry! Attribute not found:'))  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attribute properties

print(getattr(Easy_class(
  'argument placeholder value',
  'argument placeholder value'),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class(
  'argument placeholder value',
  'argument placeholder value'),'attribute2','Sorry! Attribute not found:'))  # World!

# or this:

print(getattr(Easy_class('',''),'attribute','Sorry! Attribute not found:'))  # optional: text for None
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:

  def __init__(self,**kwargs):

    self.kwargs = kwargs

# Notice how keyword arguments also reside within the instance?

# Easy_class(kwargs = 'Hello').kwargs.get('kwargs')

print(Easy_class(kwargs = 'Hello').kwargs.get('kwargs'))  # Hello

# or this:

print(Easy_class(kwargs = 'Hello').kwargs.get('kwarg','Sorry! Attribute not found:'))  # optional: text for None
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class:

  def __init__(self,**kwargs):

    self.kwargs = kwargs

# Notice how keyword arguments also reside within the instance?

# Easy_class(kwargs = 'Hello','World!').kwargs.get('kwargs')

print(
  Easy_class(
    kwargs1 = 'Hello',
    kwargs2 = 'World!').kwargs.get('kwargs1'))  # Hello

print(
  Easy_class(
    kwargs1 = 'Hello',
    kwargs2 = 'World!').kwargs.get('kwargs2'))  # World!

# or this:

print(
  Easy_class(
    kwargs1 = 'Hello',
    kwargs2 = 'World!').kwargs.get('kwarg','Sorry! Attribute not found:'))  # optional: text for None
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create sentences out of an instance of our easy class
# Python program example:

arguments = 'Hello','World!','Computer','Science','is Fun!!!'  # default tuple

class Easy_class:

  def __init__(self,attribute):

    self.attribute = attribute  # one explicit attribute property

print(getattr(Easy_class(arguments[0]+' everyone!'),'attribute','Sorry! Attribute not found:'))

print(getattr(Easy_class(arguments[0]+' '+arguments[1]+' How are you?'),'attribute','Sorry! Attribute not found:'))

print(getattr(Easy_class(arguments[0]+' '+arguments[1]+' How are you?'),'attribute','Sorry! Attribute not found:'),'More text.')

print(getattr(Easy_class(arguments[0]+' '+arguments[1]+' How are you?'),'attribute','Sorry! Attribute not found:')+' More text.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a class with an instance variable that will keep our
# print() function lean, clean and short.

arguments = ('Hello','World!','Computer','Science','is Fun!!!')  # default tuple

class Easy_class:

  def __init__(self,attribute):

    self.attribute = attribute  # one explicit attribute property

instance = Easy_class(arguments[0]+' '+arguments[1]+' How are you?')

print(getattr(instance,'attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# We can create one attribute property with as many implicit attributes
# as we wish.

class Easy_class:

  def __init__(self,attribute):

    self.attribute = 'Hello','World!','Computer','Science'  # one attribute property with four implicit attributes

print(getattr(Easy_class(''),'attribute')[0])

print(getattr(Easy_class(''),'attribute')[1])

print(getattr(Easy_class(''),'attribute')[2])

print(getattr(Easy_class(''),'attribute')[3])

# or this:

for i in range(4):
  print(getattr(Easy_class(''),'attribute')[i])

# or this:

for i in range(4):
  print(getattr(Easy_class(''),'attribute')[i],end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# BONUS LESSON!

# Let's learn what the super() function is all about. The super()
# function allows us to create a brand new class, without having
# to create redundant attribute properties. Here is a skeletal outline
# of the super() function Python program example:

class Easy_class_main:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attribute properties

class Easy_class_super(Easy_class_main):

  def __init__(self,attribute1,attribute2):
    super().__init__(attribute1,attribute2)

print(getattr(Easy_class_main('Hello','World!'),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class_super('Hello','World!'),'attribute2','Sorry! Attribute not found:'))  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# With the super() function, we can add attributes without having
# to rewrite old, redundant attributes over and over.

class Easy_class_main:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attribute properties

class Easy_class_super(Easy_class_main):

  def __init__(self,attribute1,attribute2,attribute3):  # add the new explicit attribute property
    super().__init__(attribute1,attribute2)

    self.attribute3 = attribute3  # add an explicit attribute property

print(getattr(Easy_class_main('Hello','World!'),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class_main('Hello','World!'),'attribute2','Sorry! Attribute not found:'))  # World!

print(getattr(Easy_class_super('Hello','World!','Fun!!'),'attribute3','Sorry! Attribute not found:'))  # Fun!!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_main:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attribute properties

class Easy_class_super(Easy_class_main):

  def __init__(self,attribute1,attribute2):
    super().__init__(attribute1,attribute2)

print(getattr(Easy_class_main('',''),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class_super('',''),'attribute2','Sorry! Attribute not found:'))  # World!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# With the super() function, we can add attributes without having
# to rewrite old, redundant attributes over and over.

class Easy_class_main:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attribute properties

class Easy_class_super(Easy_class_main):

  def __init__(self,attribute1,attribute2,attribute3):  # add an implicit attribute property
    super().__init__(attribute1,attribute2)

    self.attribute3 = 'Fun!!'  # add an implicit attribute property

print(getattr(Easy_class_main('',''),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class_main('',''),'attribute2','Sorry! Attribute not found:'))  # World!

print(getattr(Easy_class_super('','',''),'attribute3','Sorry! Attribute not found:'))  # Fun!!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_main:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1
    self.attribute2 = attribute2  # two explicit attribute properties

class Easy_class_super(Easy_class_main):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # add two new explicit attribute properties
    super().__init__(attribute1,attribute2)

    self.attribute3 = attribute3  # add an explicit attribute property

    self.attribute4 = attribute4  # add an explicit attribute property

print(getattr(Easy_class_main('Hello','World!'),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class_main('Hello','World!'),'attribute2','Sorry! Attribute not found:'))  # World!

print(getattr(Easy_class_super('Hello','World!','Fun!!','Computers'),'attribute3','Sorry! Attribute not found:'))  # Fun!!

print(getattr(Easy_class_super('Hello','World!','Fun!!','Computers'),'attribute4','Sorry! Attribute not found:'))  # Computers
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_main:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = 'Hello'
    self.attribute2 = 'World!'  # two implicit attribute properties

class Easy_class_super(Easy_class_main):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # add two new implicit attribute properties
    super().__init__(attribute1,attribute2)

    self.attribute3 = 'Fun!!'  # add an implicit attribute property

    self.attribute4 = 'Computers'  # add an implicit attribute property

print(getattr(Easy_class_main('',''),'attribute1','Sorry! Attribute not found:'))  # Hello

print(getattr(Easy_class_main('',''),'attribute2','Sorry! Attribute not found:'))  # World!

print(getattr(Easy_class_super('','','',''),'attribute3','Sorry! Attribute not found:'))  # Fun!!

print(getattr(Easy_class_super('','','',''),'attribute4','Sorry! Attribute not found:'))  # Computers

# The super() function can be as complex as you please. However,
# you should research: Memory Resolution Order (MRO) first.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Whoever learns Python through me. You'd better supersede me!!
# A true teacher doesn't hold back their knowledge and keep students
# beneath them. By doing such, they aren't teaching anything at all.
# If I can make those, who learn from me become a brighter light than
# myself, I have done my job as a true teacher, even if I'm not a real,
# licensed teacher of any sort.

# As a true teacher, I will bring you all the way with me. Or we won't go at all...

# I am almost a complete Walking Human Computer Science Research Laboratory Machine on Two Legs... 😁

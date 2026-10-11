
# Easy Class Python Program Examples Four:

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
# Most importantly: Do not over concentrate. Take your time to
# learn Python. Now, let's WAX on and WAX off. Shall we...

# Let's learn class inheritance, so we can create attribute properties
# and pass them down to another, non related class. We can create
# classes that share attribute properties from another class.

class Easy_class_parent:

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one explicit attribute property

class Easy_class_child(Easy_class_parent):  # child class inherits parent class attribute properties/features
  pass

print(getattr(Easy_class_parent('Parent'),'attribute','Sorry! Attribute not found:'))  # Parent

print(getattr(Easy_class_child('Child'),'attribute','Sorry! Attribute not found:'))  # Child
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_mom:

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one explicit attribute property

class Easy_class_dad:

  def __init__(self,attribute):  # two parameters

    self.attribute = attribute  # one explicit attribute property

# Note: if two, separate classes share the same attribute name 'attribute'.
# The child class can inherit from either the 'Easy_class_mom', or the
# 'Easy_class_dad'.

class Easy_class_child(Easy_class_mom):  # child class inherits parent class attribute properties/features
  pass

print(getattr(Easy_class_mom('Mom'),'attribute','Sorry! Attribute not found:'))  # Mom

print(getattr(Easy_class_dad('Dad'),'attribute','Sorry! Attribute not found:'))  # Dad

print(getattr(Easy_class_child('Child'),'attribute','Sorry! Attribute not found:'))  # Child
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a class inheritance that has two, unrelated
# attribute property names: 'attribute1' and 'attribute2'.

class Easy_class_mom:

  def __init__(self, attribute1):  # two parameters

    self.attribute1 = attribute1 # one explicit attribute property, named: 'attribute1'

class Easy_class_dad:

  def __init__(self, attribute2):  # two parameters

    self.attribute2 = attribute2  # one explicit attribute property, named: 'attribute2'

class Easy_class_child:

  def __init__(self, attribute1, attribute2):
    Easy_class_mom.__init__(self, attribute1)
    Easy_class_dad.__init__(self, attribute2)

print(getattr(Easy_class_mom('Mom'),'attribute1','Sorry! Attribute not found:'))  # Mom

print(getattr(Easy_class_dad('Dad'),'attribute2','Sorry! Attribute not found:'))  # Dad

print(getattr(Easy_class_child('Mom','Dad'),'attribute1','Sorry! Attribute not found:'))  # Mom

print(getattr(Easy_class_child('Mom','Dad'),'attribute2','Sorry! Attribute not found:'))  # Dad
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's see how implicit attribute properties behave within class
# objects. Note: you can place an 'argument placeholder value'
# if you like, or leave it out altogether; you must use either two
# single ('') quote marks, or two double ("") quote marks for both
# argument placeholder values and empty argument
# placeholder values alike.

class Easy_class_parent:

  def __init__(self,attribute):  # two parameters

    self.attribute = 'Parent'  # one implicit attribute property

class Easy_class_child(Easy_class_parent):  # child class inherits parent class attribute properties/features
  pass

# Argument placeholder values can contain any text value names you
# like, or leave them empty if you like.

print(getattr(Easy_class_parent('text'),'attribute','Sorry! Attribute not found:'))  # Parent

print(getattr(Easy_class_parent(''),'attribute','Sorry! Attribute not found:'))  # Parent

print(getattr(Easy_class_child('text'),'attribute','Sorry! Attribute not found:'))  # Parent

print(getattr(Easy_class_child(''),'attribute','Sorry! Attribute not found:'))  # Parent
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example of two, separate classes with different implicit
# attribute properties. Remember, back in Easy Class one, we talked
# about how 'arguments' are the actual text you see on your computer
# screen at execution/run time.

class Easy_class_mom:

  def __init__(self,attribute):  # two parameters

    self.attribute = 'Mom'  # one implicit attribute property

class Easy_class_dad:

  def __init__(self,attribute):  # two parameters

    self.attribute = 'Dad'  # one implicit attribute property

# Note: implicit attributes with like names, such as 'attribute', can
# only call one implicit argument at a time. The child class can only
# display the value 'Mom', or the value 'Dad' in its base class; not
# both.

class Easy_class_child(Easy_class_mom):  # child class inherits parent class attribute properties/features
  pass

print(getattr(Easy_class_mom(''),'attribute','Sorry! Attribute not found:'))  # Mom

print(getattr(Easy_class_dad(''),'attribute','Sorry! Attribute not found:'))  # Dad

print(getattr(Easy_class_child(''),'attribute','Sorry! Attribute not found:'))  # Mom
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try this Easy Class example, but with two, unique implicit
# attributes in each of the Mom and Dad classes.

class Easy_class_mom:

  def __init__(self, attribute1):  # two parameters

    self.attribute1 = 'Mom'  # one implicit attribute property

class Easy_class_dad:

  def __init__(self, attribute2):  # two parameters

    self.attribute2 = 'Dad'  # one implicit attribute property

class Easy_class_child:

  def __init__(self, attribute1, attribute2):
    Easy_class_mom.__init__(self, attribute1)
    Easy_class_dad.__init__(self, attribute2)

print(getattr(Easy_class_mom(''),'attribute1','Sorry! Attribute not found:'))  # Mom

print(getattr(Easy_class_dad(''),'attribute2','Sorry! Attribute not found:'))  # Dad

print(getattr(Easy_class_child('',''),'attribute1','Sorry! Attribute not found:'))  # Mom

print(getattr(Easy_class_child('',''),'attribute2','Sorry! Attribute not found:'))  # Dad
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Note: use different, unique attribute names when dealing with
# two or more attribute properties in each class act. This makes
# testing and debugging much easier. From here on, try the rest
# of the Easy Class Python programming examples below:

class Easy_class_mom:

  def __init__(self, attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1  # one explicit attribute property, named: 'attribute1'
    self.attribute2 = attribute2  # one explicit attribute property, named: 'attribute2'

class Easy_class_dad:

  def __init__(self, attribute3,attribute4):  # three parameters

    self.attribute3 = attribute3  # one explicit attribute property, named: 'attribute3'
    self.attribute4 = attribute4  # one explicit attribute property, named: 'attribute4'

class Easy_class_child:

  def __init__(self,attribute1,attribute2,attribute3,attribute4):
    Easy_class_mom.__init__(self, attribute1,attribute2)
    Easy_class_dad.__init__(self, attribute3,attribute4)

print(getattr(Easy_class_mom('Jane','Smith'),'attribute1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_mom('Jane','Smith'),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_dad('John','Smith'),'attribute3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_dad('John','Smith'),'attribute4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute4','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_mom:

  def __init__(self, attribute1,attribute2):  # three parameters

    self.attribute1 = 'Jane'  # one implicit attribute property, named: 'attribute1'
    self.attribute2 = 'Smith'  # one implicit attribute property, named: 'attribute2'

class Easy_class_dad:

  def __init__(self, attribute3,attribute4):  # three parameters

    self.attribute3 = 'John'  # one implicit attribute property, named: 'attribute3'
    self.attribute4 = 'Smith'  # one implicit attribute property, named: 'attribute4'

class Easy_class_child:

  def __init__(self, attribute1, attribute2,attribute3,attribute4):
    Easy_class_mom.__init__(self,attribute1,attribute2)
    Easy_class_dad.__init__(self,attribute3,attribute4)

print(getattr(Easy_class_mom('',''),'attribute1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_mom('',''),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_dad('',''),'attribute3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_dad('',''),'attribute4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','',''),'attribute1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child('','','',''),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','',''),'attribute3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child('','','',''),'attribute4','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_grandmother:

  def __init__(self, attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1  # one explicit attribute property, named: 'attribute1'
    self.attribute2 = attribute2  # one explicit attribute property, named: 'attribute2'

class Easy_class_grandfather:

  def __init__(self, attribute3,attribute4):  # three parameters

    self.attribute3 = attribute3  # one explicit attribute property, named: 'attribute3'
    self.attribute4 = attribute4  # one explicit attribute property, named: 'attribute4'

class Easy_class_mom:

  def __init__(self, attribute5,attribute6):  # three parameters

    self.attribute5 = attribute5  # one explicit attribute property, named: 'attribute5'
    self.attribute6 = attribute6  # one explicit attribute property, named: 'attribute6'

class Easy_class_dad:

  def __init__(self, attribute7,attribute8):  # three parameters

    self.attribute7 = attribute7  # one explicit attribute property, named: 'attribute7'
    self.attribute8 = attribute8  # one explicit attribute property, named: 'attribute8'

class Easy_class_child:

  def __init__(self,
               attribute1,attribute2,attribute3,attribute4,
               attribute5,attribute6,attribute7,attribute8):  # nine parameters

    Easy_class_grandmother.__init__(self,attribute1,attribute2)
    Easy_class_grandfather.__init__(self,attribute3,attribute4)
    Easy_class_mom.__init__(self,attribute5,attribute6)
    Easy_class_dad.__init__(self,attribute7,attribute8)

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute1','Sorry! Attribute not found:'))  # Mary

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute3','Sorry! Attribute not found:'))  # Jerry

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute5','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute6','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute7','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute8','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_grandmother:

  def __init__(self, attribute1,attribute2):  # three parameters

    self.attribute1 = 'Mary'  # one implicit attribute property, named: 'attribute1'
    self.attribute2 = 'Smith'  # one implicit attribute property, named: 'attribute2'

class Easy_class_grandfather:

  def __init__(self, attribute3,attribute4):  # three parameters

    self.attribute3 = 'Jerry'  # one implicit attribute property, named: 'attribute3'
    self.attribute4 = 'Smith'  # one implicit attribute property, named: 'attribute4'

class Easy_class_mom:

  def __init__(self, attribute5,attribute6):  # three parameters

    self.attribute5 = 'Jane'  # one implicit attribute property, named: 'attribute5'
    self.attribute6 = 'Smith'  # one implicit attribute property, named: 'attribute6'

class Easy_class_dad:

  def __init__(self, attribute7,attribute8):  # three parameters

    self.attribute7 = 'John'  # one implicit attribute property, named: 'attribute7'
    self.attribute8 = 'Smith'  # one implicit attribute property, named: 'attribute8'

class Easy_class_child:

  def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7,attribute8):

    Easy_class_grandmother.__init__(self,attribute1,attribute2)
    Easy_class_grandfather.__init__(self,attribute3,attribute4)
    Easy_class_mom.__init__(self,attribute5,attribute6)
    Easy_class_dad.__init__(self,attribute7,attribute8)

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child('','','','','','','',''),'attribute1','Sorry! Attribute not found:'))  # Mary

print(getattr(Easy_class_child('','','','','','','',''),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','','','','','',''),'attribute3','Sorry! Attribute not found:'))  # Jerry

print(getattr(Easy_class_child('','','','','','','',''),'attribute4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','','','','','',''),'attribute5','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child('','','','','','','',''),'attribute6','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','','','','','',''),'attribute7','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child('','','','','','','',''),'attribute8','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a class inheritance, using the super() function.
# We have to play, 'Pass The Baton' to create a chain, so the
# super() function can construct a chain of explicit attribute
# properties from one class to the next class.

class Easy_class_mom:

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1  # one explicit attribute property, named: 'attribute1'
    self.attribute2 = attribute2  # one explicit attribute property, named: 'attribute2'

# Easy_class_dad(Easy_class_mom) passes the baton up to Easy_class_mom:

class Easy_class_dad(Easy_class_mom):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

     super().__init__(attribute1,attribute2)  # two positional arguments

     self.attribute3 = attribute3  # one explicit attribute property, named: 'attribute3'
     self.attribute4 = attribute4  # one explicit attribute property, named: 'attribute4'

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

    super().__init__(attribute1,attribute2,attribute3,attribute4)  # four positional arguments

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child('Jane','Smith','John','Smith'),'attribute4','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a class inheritance, using the super() function.
# We have to play, 'Pass The Baton' to create a chain, so the
# super() function can construct a chain of implicit attribute
# properties from one class to the next class.

class Easy_class_mom:

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = 'Jane'  # one implicit attribute property, named: 'attribute1'
    self.attribute2 = 'Smith'  # one implicit attribute property, named: 'attribute2'

# Easy_class_dad(Easy_class_mom) passes the baton up to Easy_class_mom:

class Easy_class_dad(Easy_class_mom):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

     super().__init__(attribute1,attribute2)  # two positional arguments

     self.attribute3 = 'John'  # one implicit attribute property, named: 'attribute3'
     self.attribute4 = 'Smith'  # one implicit attribute property, named: 'attribute4'

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

    super().__init__(attribute1,attribute2,attribute3,attribute4)  # four positional arguments

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child('','','',''),'attribute1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child('','','',''),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','',''),'attribute3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child('','','',''),'attribute4','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_grandmother:

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = attribute1  # one explicit attribute property, named: 'attribute1'
    self.attribute2 = attribute2  # one explicit attribute property, named: 'attribute2'

# Easy_class_grandfather(Easy_class_grandmother) passes the baton up to
# Easy_class_grandmother:

class Easy_class_grandfather(Easy_class_grandmother):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

     super().__init__(attribute1,attribute2)  # two positional arguments

     self.attribute3 = attribute3  # one explicit attribute property, named: 'attribute3'
     self.attribute4 = attribute4  # one explicit attribute property, named: 'attribute4'

# Easy_class_mom(Easy_class_grandfather) passes the baton up to
# Easy_class_grandfather(Easy_class_grandmother)

class Easy_class_mom(Easy_class_grandfather):

  def __init__(self,
               attribute1,attribute2,attribute3,
               attribute4,attribute5,attribute6):  # seven parameters

    super().__init__(attribute1,attribute2,attribute3,attribute4)  # four positional arguments

    self.attribute5 = attribute5  # one explicit attribute property, named: 'attribute5'
    self.attribute6 = attribute6  # one explicit attribute property, named: 'attribute6'

# Easy_class_dad(Easy_class_mom) passes the baton up to Easy_class_mom(Easy_class_grandfather)

class Easy_class_dad(Easy_class_mom):

  def __init__(self,
               attribute1,attribute2,attribute3,attribute4,
               attribute5,attribute6,attribute7,attribute8):  # nine parameters

    super().__init__(
      attribute1,attribute2,attribute3,
      attribute4,attribute5,attribute6)  # six positional arguments

    self.attribute7 = attribute7  # one explicit attribute property, named: 'attribute7'
    self.attribute8 = attribute8  # one explicit attribute property, named: 'attribute8'

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,
               attribute1,attribute2,attribute3,attribute4,
               attribute5,attribute6,attribute7,attribute8):  # nine parameters

    super().__init__(
      attribute1,attribute2,attribute3,attribute4,
      attribute5,attribute6,attribute7,attribute8)  # eight positional arguments

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child(
  'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute1','Sorry! Attribute not found:'))  # Mary

print(getattr(Easy_class_child(
  'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
  'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute3','Sorry! Attribute not found:'))  # Jerry

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
  'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute5','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child(
    'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute6','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
  'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute7','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child(
  'Mary','Smith','Jerry','Smith','Jane','Smith','John','Smith'),'attribute8','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_grandmother:

  def __init__(self,attribute1,attribute2):  # three parameters

    self.attribute1 = 'Mary'  # one implicit attribute property, named: 'attribute1'
    self.attribute2 = 'Smith'  # one implicit attribute property, named: 'attribute2'

# Easy_class_grandfather(Easy_class_grandmother) passes the baton up to
# Easy_class_grandmother:

class Easy_class_grandfather(Easy_class_grandmother):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters

    super().__init__(attribute1,attribute2)  # two positional arguments

    self.attribute3 = 'Jerry'  # one implicit attribute property, named: 'attribute3'
    self.attribute4 = 'Smith'  # one implicit attribute property, named: 'attribute4'

# Easy_class_mom(Easy_class_grandfather) passes the baton up to
# Easy_class_grandfather(Easy_class_grandmother)

class Easy_class_mom(Easy_class_grandfather):

  def __init__(self,
               attribute1,attribute2,attribute3,
               attribute4,attribute5,attribute6):  # seven parameters

    super().__init__(attribute1,attribute2,attribute3,attribute4)  # four positional arguments

    self.attribute5 = 'Jane'  # one implicit attribute property, named: 'attribute5'
    self.attribute6 = 'Smith' # one implicit attribute property, named: 'attribute6'

# Easy_class_dad(Easy_class_mom) passes the baton up to
# Easy_class_mom(Easy_class_grandfather)

class Easy_class_dad(Easy_class_mom):

  def __init__(self,
               attribute1,attribute2,attribute3,attribute4,
               attribute5,attribute6,attribute7,attribute8):  # nine parameters

    super().__init__(
      attribute1,attribute2,attribute3,
      attribute4,attribute5,attribute6)  # six positional arguments

    self.attribute7 = 'John'  # one implicit attribute property, named: 'attribute7'
    self.attribute8 = 'Smith'  # one implicit attribute property, named: 'attribute8'

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,
               attribute1,attribute2,attribute3,attribute4,
               attribute5,attribute6,attribute7,attribute8):  # nine parameters

    super().__init__(
      attribute1,attribute2,attribute3,attribute4,
      attribute5,attribute6,attribute7,attribute8)  # eight positional arguments

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child('','','','','','','',''),'attribute1','Sorry! Attribute not found:'))  # Mary

print(getattr(Easy_class_child('','','','','','','',''),'attribute2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','','','','','',''),'attribute3','Sorry! Attribute not found:'))  # Jerry

print(getattr(Easy_class_child('','','','','','','',''),'attribute4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','','','','','',''),'attribute5','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child('','','','','','','',''),'attribute6','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child('','','','','','','',''),'attribute7','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child('','','','','','','',''),'attribute8','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what '*args' is all about. Imagine you have a whole
# bunch of attribute properties, alongside with a whole bunch of
# arguments. After awhile, you would go completely bonkers trying
# to keep up with them. With *args, we don't need to worry about
# how many attribute properties we need to satisfy the number of
# arguments. The word *args means '*arguments' for short.

# Note: *args contains one asterisk '*' and it can be any name you
# you wish. However, Python programming standards prefer the
# conventional name: *args.

class Easy_class_mom:

  def __init__(self,*args):  # two parameters

    self.args = args  # one args attribute property

# Easy_class_dad(Easy_class_mom) passes the baton up to Easy_class_mom:

class Easy_class_dad(Easy_class_mom):

  def __init__(self,*args):  # two parameters

     super().__init__(*args)  # one positional argument

     self.args = args  # one args attribute property

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,*args):  # two parameters

    super().__init__(*args)  # one positional argument

print(getattr(Easy_class_mom('Jane','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Jane

print(getattr(Easy_class_mom('Jane','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_dad('John','Smith'),'args',['Sorry! Attribute not found:'])[0])  # John

print(getattr(Easy_class_dad('John','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child('Jane','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Jane

print(getattr(Easy_class_child('Jane','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_child('John','Smith'),'args',['Sorry! Attribute not found:'])[0])  # John

print(getattr(Easy_class_child('John','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what '**kwargs' is all about. Imagine you have a whole
# bunch of attribute properties, alongside with a whole bunch of
# keyword arguments. After awhile, you would go completely bonkers
# trying to keep up with them. With **kwargs, we don't need to worry
# about how many attribute properties we need to satisfy the number
# of keyword arguments. The word **kwargs means '**keyword arguments'
# for short.

# Note: **kwargs contains two asterisks '**' and it can be any name you
# you wish. However, Python programming standards prefer the
# conventional name: **kwargs.

class Easy_class_mom:

  def __init__(self,**kwargs):  # two parameters

    self.kwargs = kwargs  # one args attribute property

# Easy_class_dad(Easy_class_mom) passes the baton up to Easy_class_mom:

class Easy_class_dad(Easy_class_mom):

  def __init__(self,**kwargs):  # two parameters

     super().__init__(**kwargs)  # one positional argument

     self.kwargs = kwargs  # one args attribute property

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,**kwargs):  # two parameters

    super().__init__(**kwargs)  # one positional argument

print(getattr(Easy_class_mom(
  kwargs1 = 'Jane',kwargs2 = 'Smith'),'kwargs').get('kwargs1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_mom(
  kwargs1 = 'Jane',kwargs2 = 'Smith'),'kwargs').get('kwargs2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_dad(
  kwargs3 = 'John',kwargs4 = 'Smith'),'kwargs').get('kwargs3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_dad(
  kwargs3 = 'John',kwargs4 = 'Smith'),'kwargs').get('kwargs4','Sorry! Attribute not found:'))  # Smith

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child(
  kwargs1 = 'Jane',kwargs2 = 'Smith'),'kwargs').get('kwargs1','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child(
  kwargs1 = 'Jane',kwargs2 = 'Smith'),'kwargs').get('kwargs2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
  kwargs3 = 'John',kwargs4 = 'Smith'),'kwargs').get('kwargs3','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child(
  kwargs3 = 'John',kwargs4 = 'Smith'),'kwargs').get('kwargs4','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# All we need to do now, is try out these last *args and **kwargs
# Python program exercise examples:

class Easy_class_grandmother:

  def __init__(self,*args):  # two parameters

     self.args = args  # one args attribute property

# Easy_class_grandfather(Easy_class_grandmother) passes the baton up to class
# Easy_class_grandmother

class Easy_class_grandfather(Easy_class_grandmother):

  def __init__(self,*args):  # two parameters

     super().__init__(*args)  # one positional argument

     self.args = args  # one args attribute property

# Easy_class_mom(Easy_class_grandfather) passes the baton up to class
# Easy_class_grandfather(Easy_class_grandmother)

class Easy_class_mom(Easy_class_grandfather):

  def __init__(self,*args):  # two parameters

    super().__init__(*args)  # one positional argument

    self.args = args  # one args attribute property

# Easy_class_dad(Easy_class_mom) passes the baton up to
# Easy_class_mom(Easy_class_grandfather)

class Easy_class_dad(Easy_class_mom):

  def __init__(self,*args):  # two parameters

     super().__init__(*args)  # one positional argument

     self.args = args  # one args attribute property

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,*args):  # two parameters

    super().__init__(*args)  # one positional argument

print(getattr(Easy_class_grandmother('Mary','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Mary

print(getattr(Easy_class_grandmother('Mary','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_grandfather('Jerry','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Jerry

print(getattr(Easy_class_grandfather('Jerry','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_mom('Jane','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Jane

print(getattr(Easy_class_mom('Jane','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_dad('John','Smith'),'args',['Sorry! Attribute not found:'])[0])  # John

print(getattr(Easy_class_dad('John','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child('Mary','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Mary

print(getattr(Easy_class_child('Mary','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_child('Jerry','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Jerry

print(getattr(Easy_class_child('Jerry','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_child('Jane','Smith'),'args',['Sorry! Attribute not found:'])[0])  # Jane

print(getattr(Easy_class_child('Jane','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith

print(getattr(Easy_class_child('John','Smith'),'args',['Sorry! Attribute not found:'])[0])  # John

print(getattr(Easy_class_child('John','Smith'),'args',['Sorry! Attribute not found:'])[1])  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Easy_class_grandmother:

  def __init__(self,**kwargs):  # two parameters

     self.kwargs = kwargs  # one args attribute property

# Easy_class_grandfather(Easy_class_grandmother) passes the baton up to Easy_class_grandmother

class Easy_class_grandfather(Easy_class_grandmother):

  def __init__(self,**kwargs):  # two parameters

     super().__init__(**kwargs)  # one positional argument

     self.kwargs = kwargs  # one args attribute property

# Easy_class_mom(Easy_class_grandfather) passes the baton up to
# Easy_class_grandfather(Easy_class_grandmother)

class Easy_class_mom(Easy_class_grandfather):

  def __init__(self,**kwargs):  # two parameters

    super().__init__(**kwargs)  # one positional argument

    self.kwargs = kwargs  # one args attribute property

# Easy_class_dad(Easy_class_mom) passes the baton up to Easy_class_mom:

class Easy_class_dad(Easy_class_mom):

  def __init__(self,**kwargs):  # two parameters

     super().__init__(**kwargs)  # one positional argument

     self.kwargs = kwargs  # one args attribute property

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,**kwargs):  # two parameters

    super().__init__(**kwargs)  # one positional argument

print(getattr(Easy_class_grandmother(
  kwargs1 = 'Mary',kwargs2 = 'Smith'),'kwargs').get('kwargs1','Sorry! Attribute not found:'))  # Mary

print(getattr(Easy_class_grandmother(
  kwargs1 = 'Mary',kwargs2 = 'Smith'),'kwargs').get('kwargs2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_grandfather(
  kwargs3 = 'Jerry',kwargs4 = 'Smith'),'kwargs').get('kwargs3','Sorry! Attribute not found:'))  # Jerry

print(getattr(Easy_class_grandfather(
  kwargs3 = 'Jerry',kwargs4 = 'Smith'),'kwargs').get('kwargs4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_mom(
  kwargs5 = 'Jane',kwargs6 = 'Smith'),'kwargs').get('kwargs5','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_mom(
  kwargs5 = 'Jane',kwargs6 = 'Smith'),'kwargs').get('kwargs6','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_dad(
  kwargs7 = 'John',kwargs8 = 'Smith'),'kwargs').get('kwargs7','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_dad(
  kwargs7 = 'John',kwargs8 = 'Smith'),'kwargs').get('kwargs8','Sorry! Attribute not found:'))  # Smith

# The beauty about child classes means you can access every single
# inherited class attribute from within the child class alone.

print(getattr(Easy_class_child(
  kwargs1 = 'Mary',kwargs2 = 'Smith'),'kwargs').get('kwargs1','Sorry! Attribute not found:'))  # Mary

print(getattr(Easy_class_child(
  kwargs1 = 'Mary',kwargs2 = 'Smith'),'kwargs').get('kwargs2','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
  kwargs3 = 'Jerry',kwargs4 = 'Smith'),'kwargs').get('kwargs3','Sorry! Attribute not found:'))  # Jerry

print(getattr(Easy_class_child(
  kwargs3 = 'Jerry',kwargs4 = 'Smith'),'kwargs').get('kwargs4','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
  kwargs5 = 'Jane',kwargs6 = 'Smith'),'kwargs').get('kwargs5','Sorry! Attribute not found:'))  # Jane

print(getattr(Easy_class_child(
  kwargs5 = 'Jane',kwargs6 = 'Smith'),'kwargs').get('kwargs6','Sorry! Attribute not found:'))  # Smith

print(getattr(Easy_class_child(
  kwargs7 = 'John',kwargs8 = 'Smith'),'kwargs').get('kwargs7','Sorry! Attribute not found:'))  # John

print(getattr(Easy_class_child(
  kwargs7 = 'John',kwargs8 = 'Smith'),'kwargs').get('kwargs8','Sorry! Attribute not found:'))  # Smith
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# BONUS LESSON!

class Easy_class_grandmother:

  def __init__(self,*args):  # two parameters

     self.args = args  # one args attribute property

# Easy_class_grandfather(Easy_class_grandmother) passes the baton up to class
# Easy_class_grandmother

class Easy_class_grandfather(Easy_class_grandmother):

  def __init__(self,*args):  # two parameters

     super().__init__(*args)  # one positional argument

     self.args = args  # one args attribute property

# Easy_class_mom(Easy_class_grandfather) passes the baton up to class
# Easy_class_grandfather(Easy_class_grandmother)

class Easy_class_mom(Easy_class_grandfather):

  def __init__(self,*args):  # two parameters

    super().__init__(*args)  # one positional argument

    self.args = args  # one args attribute property

# Easy_class_dad(Easy_class_mom) passes the baton up to
# Easy_class_mom(Easy_class_grandfather)

class Easy_class_dad(Easy_class_mom):

  def __init__(self,*args):  # two parameters

     super().__init__(*args)  # one positional argument

     self.args = args  # one args attribute property

# Easy_class_child(Easy_class_dad) passes the baton up to Easy_class_dad(Easy_class_mom)

class Easy_class_child(Easy_class_dad):

  def __init__(self,*args):  # two parameters

    super().__init__(*args)  # one positional argument

# Create for loops to loop through the child class instances.
# Invoke the end=' ' to keep text output on one line.

for i in range(2):
  print(getattr(Easy_class_child('Mary','Smith'),'args',['Sorry! Attribute not found:',''])[i],end=' ')  # Mary Smith

for i in range(2):
  print(getattr(Easy_class_child('Jerry','Smith'),'args',['Sorry! Attribute not found:',''])[i],end=' ')  # Jerry Smith

for i in range(2):
  print(getattr(Easy_class_child('Jane','Smith'),'args',['Sorry! Attribute not found:',''])[i],end=' ')  # Jane Smith

for i in range(2):
  print(getattr(Easy_class_child('John','Smith'),'args',['Sorry! Attribute not found:',''])[i],end=' ')  # John Smith

# We can also add more arguments in a child class instance, via invoking *args.

for i in range(8):
  print(getattr(Easy_class_child(
    'Mary','Smith','Jerry',
    'Smith','Jane','Smith',
    'John','Smith'),'args',['Sorry! Attribute not found:',''])[i],end=' ')

# I am almost a complete Walking Human Computer Science Research Laboratory Machine on Two Legs... 😁

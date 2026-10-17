
# EaZy Class Smash Python Program Examples:

# Note: this Python program exercise is rated PG 13,
# "Parental Guidance: Some material may be inappropriate
# for children under 13."

# by Joseph C. Richardson,GitHub.com

# Welcome to our last Easy Class Python program examples:
# volume six, when we can fully understand C3 Linearization
# and the 'DIAMOND PROBLEM' with class inheritance.

# As we go, we will learn how to keep our code completely DRY!:
# (Don't Repeat Yourself!). For now, let's take things slow and
# easy. Most importantly: Do not over concentrate. Take your
# time to learn Python. Now, let's WAX on and WAX off. Shall we...

# Let's learn what C3 Linearization is all about.

# C3 Linearization is a type of MRO: (Method Resolution Order)
# when one or more classes inherit parent classes. Note: these
# easy class examples do not require class constructors or
# attributes. In our first easy class example, we do not have to
# worry about C3 Linearization, MRO: (Method Resolution Order)
# in the final Child class act.

# This is a normal, happy family. But wait and see how other families
# don't do normal things. There are families here that commit 'INCEST'
# These abnormal, inbred families are so ugly; they smash each other.

class Grandmother:  # parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather:  # sub parent class

  def grandfather(self):  # define function
    print('Jerry')

class Mom:  # sub parent class

  def mom(self):  # define function
    print('Jane')

class Dad:  # sub parent class

  def dad(self):  # define function
    print('John')

class Child(Grandmother,Grandfather,Mom,Dad):pass

# Each class can be called up by itself; we can gain direct
# access to individual classes, along with a dot notation and
# def function name, associated with that individual class.
# Grandmother.grandmother('')

Grandmother.grandmother('argument placeholder value')
Grandfather.grandfather('argument placeholder value')
Mom.mom('argument placeholder value')
Dad.dad('argument placeholder value')

# We can use the Child class alone to call up any classes we
# like. Remember the dot notation, along with the associated
# def function name.

Child.grandmother('argument placeholder value')
Child.grandfather('argument placeholder value')
Child.mom('argument placeholder value')
Child.dad('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is when C3 Linearization, MRO: (Method Resolution Order)
# does matter. Let's call this 'Diamond Problem', "Class-Incest",
# when a sub parent class inherits a parent class above it. For
# example, let's make the Grandfather(Grandmother) become a
# child class of the Grandmother class.

# Note: for classes to work correctly, they have to contain at least
# one define function, so the class waits to be accessed. If def functions
# are not within a class, the class will act as a bottomless cup; it won't
# wait to be accessed. Here is a quick refresh for those, who are just
# learning how to create classes without class constructors or class
# attribute properties.

def my_def_function():  # define function
    print('Mary')

my_def_function()  # Call up the def function: my_def_function()

# Here is the very same def function() example, but we need the
# 'self' parameter when invoking def functions within classes.

def my_def_function(self):  # define function
    print('Mary')

# Call up the def function: my_def_function('argument placeholder value')

my_def_function('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try one class-incest-diamond problem and see what happens
# when the Grandfather, becomes the child class act of the Grandmother
# class.

# This family is just one of these abnormal families, who do incest
# and smash one another.

class Grandmother:  # non class-incest parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather(Grandmother):  # single class-incest child

  def grandfather(self):  # define function
    print('Jerry')

class Mom:  # non class-incest sub parent class

  def mom(self):  # define function
    print('Jane')

class Dad:  # non class-incest sub parent class

  def dad(self):  # define function
    print('John')

# When a class-incest child happens, we must make sure that the child
# class, Grandfather has to stay to the left side of its non class-incest
# parent class, or non class-incest sub parent class: Grandmother, in
# the final non class-incest Child class below is where this matters.
# Grandfather must stay to the left of any non class-incest parent, or
# non class-incest sub parent: Grandmother for example.

# Note: this Child class is one, messed up puppy! Wouldn't you say?

class Child(Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

Child.grandmother('argument placeholder value')
Child.grandfather('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# All "class-incest" sub child classes cannot step over the boundary
# of any non-incest parent classes. An MRO conflict will occur.

# This abnormal family is really taking incest and smashing to a whole
# other level.

class Grandmother:  # non class-incest parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather(Grandmother):  # single class-incest child

  def grandfather(self):  # define function
    print('Jerry')

class Mom(Grandmother):  # single class-incest child

  def mom(self):  # define function
    print('Jane')

class Dad:  # non class-incest sub parent class

  def dad(self):
    print('John')

class Child(Mom,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

# All class-incest children can be swapped in any order, as long
# as to never overstep the boundary of their parent class.

class Child(Grandfather,Mom,Grandmother):pass  # Oh, you poor Child class act. lol

# The non class-incest Dad class can play around all he wants and
# won't ever get caught in the act. He's not a parent class at all. Dad
# can also play in between class-incest classes all he likes. Dad can
# play around from one end, to the other if he likes, and he never gets
# caught in the act.

class Child(Dad,Mom,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Dad,Grandfather,Mom,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Mom,Dad,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Mom,Grandfather,Dad,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Mom,Grandfather,Grandmother,Dad):pass  # Oh, you poor Child class act. lol

class Child(Grandfather,Mom,Grandmother,Dad):pass  # Oh, you poor Child class act. lol

# The class-incest Mom child class overstepped her boundary.
# All class-incest children classes can never overstep their non-
# incest parent classes. The incest-class Mom class oversteps
# her non class-incest parent class, Grandmother. Class-incest
# Grandfather class and class-incest Mom classes are Grandmother's
# children now, through incest.

class Child(Grandfather,Grandmother,Mom,Dad):pass  # MRO: Method Resolution Order error

Child.grandmother('argument placeholder value')
Child.grandfather('argument placeholder value')
Child.mom('argument placeholder value')
Child.dad('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's step back and explain what 'self' is and why 'self' is needed
# within the def function's parameter. The 'self' parameter always
# starts at position zero, not position one. The 'self' parameter
# ensures that each def function stays defined within its own class
# scope, locking the function directly to the class structure. The
# argument placeholder values assure that each defined function
# can be called through the argument placeholder values.

# Note: argument placeholder values do not have to acquire text
# values at all. However, we need to invoke two single quote marks
# (''), or two double quote marks ("") to satisfy the self parameter.

# Child.grandmother('')
# Child.grandfather('')
# Child.m('')
# Child.d('')

# Child.grandmother("")
# Child.grandfather("")
# Child.m("")
# Child.d("")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are three 'class-incest' child classes that inherit the Grandmother
# class.

# This abnormal family is pushing things way too far. I can't imagine
# how that poor Child class must feel? That's one messed up puppy.

class Grandmother:  # non class-incest parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather(Grandmother):  # single class-incest child

  def grandfather(self):  # define function
    print('Jerry')

class Mom(Grandmother):  # single class-incest child

  def mom(self):  # define function
    print('Jane')

class Dad(Grandmother):  # single class-incest child

  def dad(self):  # define function
    print('John')

class Child(Mom,Grandfather,Dad,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Grandfather,Mom,Dad,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Grandfather,Dad,Mom,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Dad,Grandfather,Mom,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Mom,Dad,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Dad,Mom,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

# The incest-class, Grandfather class has overstepped his parent,
# the Grandmother class.

# Well, it looks like this poor Grandfather class couldn't get his
# Grandmother class to smash with him; she knows incest is wrong!

class Child(Dad,Mom,Grandmother,Grandfather):pass  # MRO: Method Resolution Order error

Child.grandmother('')
Child.grandfather('')
Child.mom('')
Child.dad('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these class-incest/diamond problem Python program examples:

# It looks like the Dad class wanted incest with the Mom and
# Grandfather classes. Whatever floats his boat. Smash away...

class Grandmother:  # non class-incest parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather:  # non class-incest sub parent class

  def grandfather(self):  # define function
    print('Jerry')

class Mom:  # non class-incest sub parent class

  def mom(self):  # define function
    print('Jane')

class Dad(Mom,Grandfather):  # double class-incest child

  def dad(self):  # define function
    print('John')

# Yup! This is one messed up Puppy of a Child class. Wouldn't
# you say? The Grandmother class can flirt around all she wants
# and never gets caught in the act.

class Child(Dad,Mom,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Dad,Mom,Grandmother,Grandfather):pass  # Oh, you poor Child class act. lol

class Child(Dad,Grandmother,Mom,Grandfather):pass  # Oh, you poor Child class act. lol

class Child(Grandmother,Dad,Mom,Grandfather):pass  # Oh, you poor Child class act. lol

class Child(Mom,Dad,Grandfather,Grandmother):pass  # MRO: Method Resolution Order error

class Child(Dad,Grandfather,Mom,Grandmother):pass  # MRO: Method Resolution Order error

class Child(Grandfather,Dad,Mom,Grandmother):pass  # MRO: Method Resolution Order error

Child.grandmother('')
Child.grandfather('')
Child.mom('')
Child.dad('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now this family really went off the deep end of the gene pool.

class Grandmother:  # non class-incest parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather:  # non class-incest sub parent class

  def grandfather(self):  # define function
    print('Jerry')

class Mom(Grandfather):  # single class-incest child

  def mom(self):  # define function
    print('Jane')

class Dad(Mom,Grandfather):  # double class-incest child

  def dad(self):  # define function
    print('John')

# This poor Child class baby is so interbred. He's got three
# direct, ancestral blood lines. This is one messed up
# family tree, I must say...

class Child(Dad,Mom,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

Child.grandmother('')
Child.grandfather('')
Child.mom('')
Child.dad('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This poor, abnormal family really took things too far. Dad is
# a complete, messed up child class act. Yet he was a parent
# before all this incest. Like they say: 'incest is relative' and it's
# all in the same family tree at that!

class Grandmother:  # non class-incest parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather:  # non class-incest sub parent class

  def grandfather(self):  # define function
    print('Jerry')

class Mom:  # non class-incest sub parent class

  def mom(self):  # define function
    print('Jane')

class Dad(Mom,Grandfather,Grandmother):  # triple class-incest child

  def dad(self):  # define function
    print('John')

class Child(Dad,Mom,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Dad,Mom,Grandmother,Grandfather):pass  # MRO: Method Resolution Order error

Child.grandmother('')
Child.grandfather('')
Child.mom('')
Child.dad('')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, this family really took things way too far. I mean way too
# far. This family totally locked out their own family tree with too
# much interbreeding. Nothing can supply a fresh gene pool now.

class Grandmother:  # non class-incest parent class

  def grandmother(self):  # define function
    print('Mary')

class Grandfather:  # non class-incest sub parent class

  def grandfather(self):  # define function
    print('Jerry')

class Mom(Grandfather):  # single class-incest child

  def mom(self):  # define function
    print('Jane')

class Dad(Mom,Grandfather,Grandmother):  # triple class-incest child

  def dad(self):  # define function
    print('John')

# This poor Child class act is so messed up, that he can't even breed anymore.

class Child(Dad,Mom,Grandfather,Grandmother):pass  # Oh, you poor Child class act. lol

class Child(Dad,Mom,Grandmother,Grandfather):pass  # MRO: Method Resolution Order error

Child.grandmother('')
Child.grandfather('')
Child.mom('')
Child.dad('')

# I am almost a complete Walking Human Computer Science Research Laboratory Machine on Two Legs... 😁

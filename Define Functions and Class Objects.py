
# Let's learn some heavy Python programming skills with define functions
# and class objects. These Python programming examples are not for the
# beginner/novice Python programmer. To those, who are starting into
# computer programming, do not start off with these Python program
# examples. You will quickly get lost trying to understand such examples
# as these. These Python programming examples are for advanced
# programmers only. However, if you are brave enough to try these Python
# programming examples, I say. Why not!! But you might become lost
# and quickly confused if you are just starting fresh into computer
# programming at large...

# Created by Joseph C. Richardson, GitHub.com

# Create a simple define function along with the print() function.

def define_function_example_one():
    print('This is a basic define function() example.')

define_function_example_one()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function with one parameter variable along with
# the print() function.

def define_function_example_two(argument):
    print('This is a basic define function() with an argument example.')

define_function_example_two('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function with two parameter variables along with
# the print() function.

def define_function_example_three(argument1,argument2):
    print('This is a basic define function() with two arguments example.')

define_function_example_three('argument placeholder value','argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When you are not sure of how many parameter variables to use
# within a define function, you can invoke the *args prefix to satisfy
# any number of argument placeholder values without the worry of
# how many are needed to satisfy the parameter variables.

def define_function_Class_example_four(*args):
    print('This is a basic define function() with an *args example.')

define_function_Class_example_four('argument placeholder value','argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that returns a value, via invoking one
# parameter variable, along with one argument placeholder value.

def define_function_Class_example_five(argument):
    return 'I am the actual returned value.'

print(define_function_Class_example_five(
    'This is a return define function() with an argument placeholder value.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that returns two values, via invoking two
# parameter variables, along with two argument placeholder values.

def define_function_example_six(argument1,argument2):
    return 'I am the actual returned value one.','I am the actual returned value two.'

print(define_function_example_six(
    'This is a return define function() with an argument example.',
    'This is a return define function() with an argument example.')[1])

# or this:

def define_function_example_six(argument1,argument2):
    return (
        'I am the actual returned value one.',
        'I am the actual returned value two.')

print(define_function_example_six(
    'This is a return define function() with an argument example.',
    'This is a return define function() with an argument example.')[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When you are not sure of how many parameter variables to use
# within a return define function, you can invoke the *args prefix to
# satisfy any number of argument placeholder values without the
# worry of how many are needed to satisfy the parameter variables.

def define_function_example_seven(*args):
    return 'I am the actual returned value one.','I am the actual returned value two.'

print(define_function_example_seven('This is a return define function() with an argument example.')[1])

# or this:

def define_function_example_seven(*args):
    return (
        'I am the actual returned value one.',
        'I am the actual returned value two.')

print(define_function_example_seven(
    'This is a return define function() with an argument example.')[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what **kwargs are all about. The word 'kwargs' simply means
# the words 'keyword arguments' for short. Two asterisks ** are used for
# **kwargs. Use **kwargs when you don't know how many keyword argument
# variables you want within your define function parameters. Note: you do
# not need to call the word '**kwargs' as kwargs. However, you will need to
# invoke two asterisks ** to make **kwargs work. Programmers know the word
# as **kwargs by standard definition, but you can use your own words.

def keyword_arguments(**kwargs): # one keyword argument variable
    print('I am the actual value.')

keyword_arguments(
    keyword1='keyword argument placeholder value1',
    keyword2='keyword argument placeholder value2') # two keyword argument values

# This example is without any **kwargs at all; we have to
# satisfy the exact number of keyword arguments to the
# exact number of keyword argument placeholder values.

def keyword_arguments(keyword_arg1,keyword_arg2): # two keyword argument variables
    print('I am the actual value.')

keyword_arguments(
    keyword_arg1='keyword argument placeholder value1',
    keyword_arg2='keyword argument placeholder value2') # two keyword argument values

# As shown in the define function() example above, how we
# needed the exact number of keyword argument values to the
# exact number of keyword argument variables. However, with
# **kwargs you no longer have to worry about how many keyword
# argument values you will need to satisfy the number of keyword
# argument variables within the define function parameters.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# define functions can also return keyword arguments. In this
# first example, the exact number of keyword arguments are
# required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(kwarg1,kwarg2):
    return 'I am the actual returned value one.','I am the actual returned value two.',

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))

# define functions can also return keyword arguments. In this
# second example, the exact number of keyword arguments are
# not required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(**kwargs):
    return 'I am the actual returned value.'

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# define functions can also return keyword arguments. In this
# first example, the exact number of keyword arguments are
# required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(num1,num2):
    return num1*num2

print(keyword_arguments(num1=2,num2=4))

# define functions can also return keyword arguments. In this
# second example, the exact number of keyword arguments are
# not required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(**kwargs):
    return 2*4

print(keyword_arguments(num1='placeholder value 1',num2='placeholder value 2'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do a quick recap about *args and **kwargs syntex only,
# so we can fully understand in a simpler way of what *args and
# **kwargs are all about.

def arguments(*args): # one argument variable
    print('I am the actual value.')

arguments(
    'argument placeholder value1',
    'argument placeholder value2')  # two argument values

def keyword_arguments(**kwargs): # one keyword argument variable
    print('I am the actual value.')

keyword_arguments(
    kwargs1='keyword argument placeholder value1',
    kwargs2='keyword argument placeholder value1')  # two keyword argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some define functions that act like subroutines.

# Since there are no line numbers in Python, also means that we
# cannot create any such 'go to', or 'go sub' commands at all with
# Python. So how can we create subroutines with Python?. How
# can we create subroutines without making them jump to line
# numbers, like we did in the old days? Well the answer is quite
# simple. Let's use define functions() with a while loop to create
# our subroutine examples, using define functions() only.

def subroutine_one():
    print('You picked subroutine one:')

def subroutine_two():
    print('You picked subroutine two:')

def subroutine_three():
    print('You picked subroutine three:')

while True:
    message=input('Please type 1, 2 or 3 to select the subroutine you wish to \
display or type (q) to quit: ').lower().strip()  # strip() clears whitespace)

    if message=='q':
        break
    while True:
        if message=='1':
            subroutine_one()
            break
        elif message=='2':
            subroutine_two()
            break
        elif message=='3':
            subroutine_three()
            break
        else:
            print('Sorry! No subroutine for that.')
            break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a class with three parameter variables, including the 'self'
# variable. Create three print() functions outside the class that will
# display the three class values on the screen output, when executed.

class Class_example_one:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

print(Class_example_one('John','Smith',23).first_name)
print(Class_example_one('John','Smith',23).last_name)
print(Class_example_one('John','Smith',23).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a class with three parameter variables, including the 'self'
# variable. Create three print() functions inside the class that will
# display the three class values on the screen output, when executed.
# be sure to invoke the 'self' variable within the  three print() functions.

class Class_example_two:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_two('John','Smith',23)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same class example as the one above. The only difference
# is, that a separate return function is also created within the class object by
# itself, inside a print() function, called 'pets'.

class Class_example_three:

    def pets(pet1,pet2,pet3,pet4):
        return 'Dog','Cat','Bird','Fish'

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_three('John','Smith',23)

print(Class_example_three.pets(
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value')[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same class example as the one above. The only
# difference is, that the *args prefix is invoked. When you are not
# sure of how many parameter variables to use within a return define
# function, you can invoke the *args prefix to satisfy any number of
# argument placeholder values without the worry of how many are
# needed to satisfy the parameter variables.

class Class_example_four:

    def pets(*args):
        return 'Dog','Cat','Bird','Fish'

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_four('John','Smith',23)

print(Class_example_four.pets('argument placeholder value')[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same class example as the one above. The only
# difference is, a variable is used to store the class name and the
# return function name, 'pets'.

class Class_example_five:

    def pets(*args):
        return 'Dog','Cat','Bird','Fish'

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_five('John','Smith',23)

return_function = Class_example_five.pets('argument placeholder value')[2]

print(return_function)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's, this time create a Main class and a Sub class so we can
# inherit all attribute properties from the main class to the subclass.

class Main_class_example_one:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

class Sub_class_example_one(Main_class_example_one):  # inherit all attribute properties from the main class
    pass

Main_class_example_one('John','Smith',23)

Sub_class_example_one('Jane','Smith',22)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a small example of the 'super()' function to show how it works.
# The 'super()' function not only inherits all attribute properties from the
# main class, but it also carries its very own sub class attribute properties
# as well. This way, we can create different sub class attribute properties
# as you will clearly notice in the next class example.

class Main_class_example_two:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

class Sub_class_example_two(Main_class_example_two):  # inherit all attribute properties from the main class

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)

Main_class_example_two('John','Smith',23)

Sub_class_example_two('Jane','Smith',22)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This sub class act has the exact, but redundant attribute properties
# that are the very same attribute properties within the Main class act.

class Main_class_attributes:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class_attributes:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

print(Main_class_attributes('Jane','Smith',22).first_name)

print(Sub_class_attributes('John','Smith',23).first_name)

# Let's fix this redundant attribute property problem, once and for all with
# the super() function.

class Main_class_attributes:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class_attributes(Main_class_attributes):

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)

print(Main_class_attributes('Jane','Smith',22).first_name)

print(Sub_class_attributes('John','Smith',23).first_name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now we can reach a much better understanding of what the super()
# function does. We can create a sub class with its very own atribute
# properties, without having to create redundancy on our programming
# part. We have to invoke all the main class atribute properties into the
# super() function, along with the sub class attribute properties. But
# we don't have to recreate main class atribute property redundancy at all.

class Main_class_example_three:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

# Inherit all attribute properties from the main class.

class Sub_class_example_three(Main_class_example_three):

# inherit all attribute properties from the main class to the sub class, without
# redundancy while, only creating the sub class attribute properties of their
# very own set of atribute properties only. In this example, we are creating
# four pet attribute properties. Note: You cannot call sub class atrubes, which
# are different to those that are in the main class, unless you use the super()
# function. Always invoke the __init__ constructor, which initalizes all the
# atribute properites from the main class, while we can add some new class
# atribute properties to the sub class act, without recreating all the attribute
# properties of the main class act.

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print(self.dog)
        print(self.cat)
        print(self.bird)
        print(self.fish)

Main_class_example_three('John','Smith',23)

Sub_class_example_three('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same main class Python program example as
# shown above. The only difference is, the print() functions are
# all outside from the two classes: main class and the sub class acts.

class Main_class_example_four:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class_example_four(Main_class_example_four):

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

# All print() functions are outside from the main class and the sub class acts.

print(Main_class_example_four('John','Smith',23).first_name)
print(Main_class_example_four('John','Smith',23).last_name)
print(Main_class_example_four('John','Smith',23).age)

print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').first_name)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').last_name)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').age)

print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').dog)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').cat)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').bird)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').fish)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now take all that we've learned so far and start to have some
# serious Python programming fun! Let's create some text strings
# to make the Python program be a piece of programming art, as
# well as taking a huge step into computer science in general. Believe
# it or not!

class Main_class_example_five:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

# Keep all the print() functions inside the main class.

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_five(Main_class_example_five):

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

# Keep all the print() functions inside the sub class.

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

# Now, simply call up the two class names alone, along with
# their argument placeholder values, without invoking the
# print() function outside the classes as we did before in the
# last example, shown above; thus creating longer Python
# command code on the programmer's part.

Main_class_example_five('John','Smith',23)

Sub_class_example_five('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')

# or this:

# Break up all Python commands so they won't disappear off
# the left edge of the screen.

Main_class_example_five('John','Smith',23)

Sub_class_example_five(
    'Jane','Smith',22,'German Shepherd',
    'Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's ratchet things up a bit and take all we've learned about
# classes and return functions, along with learning what the
# super() function does, along with its __init__ constructor,
# which initializes all the attribute properties from the main
# class to the sub class, without having to recreate main class
# attribute properties, when we want the sub class to have its
# very own, unique set of attribute properties, while being able
# to inherit the main class attribute properties without redundancy
# on the programmer's part.

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

# Call the 'main_class_example_six' variable, followed by its
# return function, called 'number_one_example'.

print(Main_class_example_six.number_one_example(2,5))

# Call the 'main_class_example_six' variable, followed by its
# return function, called 'number_two_example'.

print(Sub_class_example_six.number_two_example(2,5))

# Lastly, call the two classes, the main class and the sub class
# acts, along their own, unique argument placeholder values.

Main_class_example_six('John','Smith',23)

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same Python program example as the one above.
# The only difference is, this time we have all the print() functions
# inside the two classes. All we need to do is call the two classes
# without having to call the separate return functions outside the
# classes as we did before.

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

    print(Main_class_example_six.number_one_example(2,5))
    print(Sub_class_example_six.number_two_example(2,5))

Main_class_example_six('John','Smith',23)

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same Python program example as the one above.
# Let's just imagine that the super() function does not exist at all.
# Imagine the redundancy of the attribute properties of the main
# class to the sub class? The sub class has redundant Python code
# related to the main class which, without the super() function, we
# have to repeat this bit of Python code illustrated below:

#  self.first_name=fname
#  self.last_name=lname
#  self.age=age

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):

# redundant Python code from the main class attribute properties:

        self.first_name=fname
        self.last_name=lname
        self.age=age

# sub class attribute properties

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

    print(Main_class_example_six.number_one_example(2,5))
    print(Sub_class_example_six.number_two_example(2,5))

Main_class_example_six('John','Smith',23)

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')

# Now you know why the super() function is invoked into classes,
# who's sub classes have different attribute properties of their very
# own. The super() function stops upper class attribute property
# redundancy on the programmer's part.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bonus Python String Concatenation Tips:

# Create a tuple called 'tuple_varianble', so we can use its values in
# text trings.

tuple_variable = 'Dog','Cat','Bird','Fish'

# Non formatted string concatenation example:

print('I love my',tuple_variable[0],'and my',tuple_variable[1],'so very much!')

print('I love my '+tuple_variable[0]+' and my '+tuple_variable[1]+' so very much!')

# old formatted string concatenation example:

print('I love my {} and my {} so very much!'.format(tuple_variable[0],tuple_variable[1]))

# New f' string concatenation format:

print(f'I love my {tuple_variable[0]} and my {tuple_variable[1]} so very much!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When it comes to computer programming, text strings and
# integer strings do not mix at all. To tackle this string concatenation
# problem, we invoke the 'str()' string function, so we can mix
# them both together with ease, while doing real calculations
# with integer strings, within text strings.

# Non formatted string concatenation example:

print('Invoke the str() function to concatenate text and integer strings together:',3+4,'just like that.')

print('Invoke the str() function to concatenate text and integer strings together: '+str(3+4)+' just like that.')

# New f' string concatenation format:

print(f'Invoke the str() function to concatenate text and integer strings together: {str(3+4)} just like that.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
# Let's try another way to create printed text paragraphs, without
# invoking the ( \ ) backslash and the ( \n ) backslash 'n'.
# Let's use three single ( ''' ''' ) quote marks instead.

print('''This is a paragraph inside a print() function, using the
backslash to create a hard line break. We can keep on typing
as many lines of text we need inside a print() function. We can
force printed screen output text on multiple lines.''')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a variable to store the above print() function text code.

text_string_variable = 'This is a paragraph inside a print() function, \
using the backslash to create a hard line break.\nWe can keep on typing \
as many lines of text we need inside a print() function.\nWe can \
force printed screen output text on multiple lines.'

print(text_string_variable)  # prints out the value inside the variable called 'text'

# or this without the ( \ ) backslash and the ( \n ) backslash 'n'

text_string_variable = '''This is a paragraph inside a print() function,
using the backslash to create a hard line break. We can keep on typing
as many lines of text we need inside a print() function. We can
force printed screen output text on multiple lines.'''

print(text_string_variable)  # prints out the value inside the variable called 'text
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke index values within print() functions

print('Hello World!')  # Hello World!

print('Hello World!'[0])  # H

print('Hello World!'[-1])  # !

print('Hello World!'[0:5])  # Hello

print('Hello World!'[6:12])  # World!

print('Hello World!'[::-1],'is backwards.')  # !dlroW olleH is backwards.

# or this:

print('Hello World!'[::-1]+' is backwards.')  # !dlroW olleH is backwards.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len(), length function to count how many characters their
# are, including any spaces in between print() function text strings.

print(
    'There are',len('Hello World!'),
    'characters, including spaces.')  # There are 12 characters, including spaces.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len() length function to count how many tuple values
# there are.

tuple_value_length = ('value 1','value 2','value 3','value 4','value 5')

print('There are',len(tuple_value_length),'tuple values.')  # There are 5 tuple values.

# or this:

print('There are '+str(len(tuple_value_length))+' tuple values.')  # There are 5 tuple values.

# or this:

print(f'There are {len(tuple_value_length)} tuple values.')  # There are 5 tuple values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len() length function to count how many list values
# there are.

list_value_length = ['value 1','value 2','value 3','value 4','value 5']

print('There are',len(list_value_length),'list values.')  # There are 5 list values.

# or this:

print('There are '+str(len(list_value_length))+' list values.')  # There are 5 list values.

# or this:

print(f'There are {len(list_value_length)} list values.')  # There are 5 list values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len() length function to count how many dictionary
# values there are.

dictionary_value_length = {'key1':'value 1','key2':'value 2','key3':'value 3','key4':'value 4','key5':'value 5'}

print('There are',len(dictionary_value_length),'dictionary values.')  # There are 5 dictionary values.

# or this:

print('There are '+str(len(dictionary_value_length))+' dictionary values.')  # There are 5 dictionary values.

# or this:

print(f'There are {len(dictionary_value_length)} dictionary values.')  # There are 5 dictionary values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's take all we've learned about string concatenation and
# recreate this very same class act, we've learned also, as well.
# Let's invoke the f' string format to make string concatenation
# much easier to create, instead of invoking commas ',' or
# plus '+' signs to concatenate strings together.

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(f'Hi. My first name is {self.first_name}. What is your first name?')
        print(f'My last name is {self.last_name}. What is your last name?')
        print(f'My age is {str(self.age)}. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print(f'I have a {self.dog}')
        print(f'I have a {self.cat}')
        print(f'I have a {self.bird}')
        print(f'I have a {self.fish}')

    print(Main_class_example_six.number_one_example(2,5))
    print(Sub_class_example_six.number_two_example(2,5))

# this:

Main_class_example_six('John','Smith',23).first_name

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').dog

# or this:

a = Main_class_example_six('John','Smith',23).first_name

b = Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').dog

print(a)
print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bonus Mega Superclass Python Program Exercise

class Main_class_attribute_properties:

    def __init__(self,cars,boats,planes):
        self.cars=cars
        self.boats=boats
        self.planes=planes

class Sub_class1_attribute_properties(Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters):
        super().__init__(cars,boats,planes)

        self.helicopters=helicopters

class Sub_class2_attribute_properties(
    Sub_class1_attribute_properties,Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones):
        super().__init__(cars,boats,planes,helicopters)

        self.drones=drones

class Sub_class3_attribute_properties(
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones,starships):
        super().__init__(cars,boats,planes,helicopters,drones)

        self.starships=starships

class Sub_class4_attribute_properties(
    Sub_class3_attribute_properties,
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones,starships,submarines):
        super().__init__(cars,boats,planes,helicopters,drones,starships)

        self.submarines=submarines

# The Sub_class5_attribute_properties have the exact same attribute
# properties as the Sub_class4_attribute_properties. No other new class
# attribute properties exist in the Sub_class5_attribute_properties.

class Sub_class5_attribute_properties(
    Sub_class4_attribute_properties,
    Sub_class3_attribute_properties,
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones,starships,submarines):
        super().__init__(cars,boats,planes,helicopters,drones,starships,submarines)

main_class = Main_class_attribute_properties('My car','My boat','My plane').planes

sub_class1 = Sub_class1_attribute_properties(
    'My car','My boat','My airplane','My helicopter').helicopters

sub_class2 = Sub_class2_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone').drones

sub_class3 = Sub_class3_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone','My starship').starships

sub_class4 = Sub_class4_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone','My starship','My submarine').submarines

# The Sub_class5_attribute_properties have the exact same attribute
# properties as the Sub_class4_attribute_properties. No other new class
# attribute properties exist in the Sub_class5_attribute_properties.

sub_class5 = Sub_class5_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone','My starship','My submarine').submarines

# Create a variable called 'auto_class' to store all six class object values.

auto_class = (
    main_class,sub_class1,
    sub_class2,sub_class3,
    sub_class4,sub_class5)

# Create a for loop that loops through all six auto_class values

for i in auto_class:
    print(i)

# Now, we can clearly see how this all pans out to be. We've come such a
# very long way, as we've learned so much about how to create define functions,
# return define functions and classes, along with the super() function and
# string concatenation. Let's now take a much needed break! But practice,
# practice and more practice, practice; we must constantly practice at anything
# we strive to become. Even while being great at what we do, we should
# always continue to practice, practice, practice and more practice, practice,
# practice to keep on top of our game. No matter what!

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs...

# These are my own, different ways of how I practice with Python
# programming. I always start from the ground and then up to
# be able to understand Python programming. When I did BASIC:
# (Beginner's All-purpose Symbolic Instruction Code) back in
# the good old days, I always started from the ground and then
# up. I never started off with hard things; instead, I would dissect
# these hard things. And with trial and error, I soon began to teach
# myself these hard things. You will quickly notice how I show
# each and every step of how to learn some of these hard Python
# programming examples, I illustrate here. In everything I teach
# about Python programming, I always show the learner how to
# dissect and break down hard Python code, so the learner can
# then learn Python much quicker like I do.

# Created by Joseph C. Richardson, GitHub.com

# Create a define function that have no arguments to be satisfied.

def non_arguments():
    print('I do not need any argument values at all. Thank you...')

non_arguments()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that have arguments to be satisfied.

def arguments(arg1,arg2,arg3):
    print('I need these three argument values to be satisfied. Thank you...')

arguments(
    'argument placeholder value1',
    'argument placeholder value2',
    'argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that have keyword arguments to be satisfied.

def keyword_arguments(kwarg1,kwarg2,kwarg3):
    print('I need these three keyword argument values to be satisfied. Thank you...')

keyword_arguments(
    kwarg1='keyword argument placeholder value1',
    kwarg2='keyword argument placeholder value2',
    kwarg3='keyword argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that have no arguments to be satisfied.

def return_non_arguments():
    return 'I do not need any return argument values at all. Thank you...'

print(return_non_arguments())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that have arguments to be satisfied.

def return_arguments(arg1,arg2,arg3):
    return 'I need these three return argument values to be satisfied. Thank you...'

argument_placeholder_values = return_arguments(
    'return argument placeholder value1',
    'return argument placeholder value2',
    'return argument placeholder value3')

print(argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that have keyword arguments
# to be satisfied.

def return_keyword_arguments(kwarg1,kwarg2,kwarg3):
    return 'I need these three return keyword argument values to be satisfied. Thank you...'

keyword_argument_placeholder_values = return_keyword_arguments(
    kwarg1='return keyword argument placeholder value1',
    kwarg2='return keyword argument placeholder value2',
    kwarg3='return keyword argument placeholder value3')

print(keyword_argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that invokes the *args prefix to satisfy
# any number of argument values.

def args_arguments(*args):
    print('I do not need the exact argument values to be satisfied. Thank you...')

args_arguments(
    '*args argument placeholder value1',
    '*args argument placeholder value2',
    '*args argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that invokes the **kwargs prefix to satisfy
# any number of keyword argument values.

def kwargs_arguments(**kwargs):
    print('I do not need the exact keyword argument values to be satisfied. Thank you...')

kwargs_arguments(
    kwarg1='keyword argument placeholder value1',
    kwarg2='keyword argument placeholder value2',
    kwarg3='keyword argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that invokes the *args prefix to satisfy
# any number of argument values.

def return_args_arguments(*args):
    return 'I do not need the exact argument values to be satisfied. Thank you...'

return_args_argument_placeholder_values = return_args_arguments(
    'return *args argument placeholder value1',
    'return *args argument placeholder value2',
    'return *args argument placeholder value3')

print(return_args_argument_placeholder_values)

# You can also cheat in Python with the *args prefix this example shows.

def return_args_arguments(*args):
    return 'I do not need the exact argument values to be satisfied. Thank you...'

return_args_argument_placeholder_values = return_args_arguments()

print(return_args_argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that invokes the **kwargs prefix to satisfy
# any number of keyword argument values.

def return_kwargs_arguments(**kwargs):
    return 'I do not need the exact keyword argument values to be satisfied. Thank you...'

return_kwargs_argument_placeholder_values = return_kwargs_arguments(
    kwarg1='return **kwargs argument placeholder value1',
    kwarg2='return **kwargs argument placeholder value2',
    kwarg3='return **kwargs argument placeholder value3')

print(return_kwargs_argument_placeholder_values)

# You can also cheat in Python with the **kwargs prefix this example shows.

def return_kwargs_arguments(**kwargs):
    return 'I do not need the exact keyword argument values to be satisfied. Thank you...'

return_kwargs_argument_placeholder_values = return_kwargs_arguments()

print(return_kwargs_argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a single class object with one attribute
# property.

class Single_class:

    def __init__(self,var1):
        self.class_var1=var1

print(Single_class('This is a single class object with attribute class_var1..').class_var1)

# Let's use a variable inside the print() function instead.

variable = Single_class('This is a single class object with attribute class_var1..').class_var1

print(variable)

# Let's do this if we like.

variable = Single_class('This is a single class object with attribute class_var1.')

print(variable.class_var1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a single class object with two attribute
# properties.

class Single_class:

    def __init__(self,var1,var2):
        self.class_var1=var1
        self.class_var2=var2

print(Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.').class_var2)

# Let's use a variable inside the print() function instead.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.').class_var2

print(variable)

# Let's do this if we like.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.')

print(variable.class_var2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a single class object with three attribute
# properties.

class Single_class:

    def __init__(self,var1,var2,var3):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

print(Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.').class_var3)

# Let's use a variable inside the print() function instead.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.').class_var3

print(variable)

# Let's do this if we like.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.')

print(variable.class_var3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inherit the properties of the main class into all sub classses.
# Invoke the 'pass' statement to tell Python that you do not
# want anymore indented code blocks below.

class Main_class_attribute_properties:

    def __init__(self,var1,var2,var3):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

class Sub_class1_attribute_properties(  # inhert main class properties
    Main_class_attribute_properties):pass

class Sub_class2_attribute_properties(  # inhert sub class1 and main class properties
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):pass

class Sub_class3_attribute_properties(  # inhert sub class2, sub class1 and main class properties
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):pass

class Sub_class4_attribute_properties(  # inhert sub class3, sub class2, sub class1 and main class properties
    Sub_class3_attribute_properties,
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):pass

a = Main_class_attribute_properties(
    'This is an instance of a main class object with three attribute properties 1',
    'This is an instance of a main class object with three attribute properties 2',
    'This is an instance of a main class object with three attribute properties 3')

b = Sub_class1_attribute_properties(
    'This is an instance of a sub class1 object with three attribute properties 1',
    'This is an instance of a sub class1 object with three attribute properties 2',
    'This is an instance of a sub class1 object with three attribute properties 3')

c = Sub_class2_attribute_properties(
    'This is an instance of a sub class2 object with three attribute properties 1',
    'This is an instance of a sub class2 object with three attribute properties 2',
    'This is an instance of a sub class2 object with three attribute properties 3')

d = Sub_class3_attribute_properties(
    'This is an instance of a sub class3 object with three attribute properties 1',
    'This is an instance of a sub class3 object with three attribute properties 2',
    'This is an instance of a sub class3 object with three attribute properties 3')

e = Sub_class4_attribute_properties(
    'This is an instance of a sub class3 object with three attribute properties 1',
    'This is an instance of a sub class3 object with three attribute properties 2',
    'This is an instance of a sub class3 object with three attribute properties 3')

# Print out all individual class attribute property values.

print(a.class_var1)
print(b.class_var1)
print(c.class_var1)
print(d.class_var1)
print(e.class_var1)

print(a.class_var2)
print(b.class_var2)
print(c.class_var2)
print(d.class_var2)
print(e.class_var2)

print(a.class_var3)
print(b.class_var3)
print(c.class_var3)
print(d.class_var3)
print(e.class_var3)

# Here are some different ways to concatenate strings together.

# Non formatted string concatenation example one.

print(a.class_var1,'\n',a.class_var2,'\n',a.class_var3)

print(b.class_var1,'\n',b.class_var2,'\n',b.class_var3)

print(c.class_var1,'\n',c.class_var2,'\n',c.class_var3)

print(d.class_var1,'\n',d.class_var2,'\n',d.class_var3)

# Non formatted string concatenation example two.

print(a.class_var1+'\n'+a.class_var2+'\n'+a.class_var3)

print(b.class_var1+'\n'+b.class_var2+'\n'+b.class_var3)

print(c.class_var1+'\n'+c.class_var2+'\n'+c.class_var3)

print(d.class_var1+'\n'+d.class_var2+'\n'+d.class_var3)

# Old formatted string concatenation example three.

print('{}\n{}\n{}'.format(a.class_var1,a.class_var2,a.class_var3))

print('{}\n{}\n{}'.format(b.class_var1,b.class_var2,b.class_var3))

print('{}\n{}\n{}'.format(c.class_var1,c.class_var2,c.class_var3))

print('{}\n{}\n{}'.format(d.class_var1,d.class_var2,d.class_var3))

# New formatted f' string concatenation example four.

print(f'{a.class_var1}\n{a.class_var2}\n{a.class_var3}')

print(f'{b.class_var1}\n{b.class_var2}\n{b.class_var3}')

print(f'{c.class_var1}\n{c.class_var2}\n{c.class_var3}')

print(f'{d.class_var1}\n{d.class_var2}\n{d.class_var3}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do a super class with sub super classes that have their
# very own attribute properties. The super() function stops
# redundant class attribute properties, while new attribute
# properties can be added to sub super classes, without having
# to rewrite the main class attribute properties again, just to
# add new ones to each sub super class object. Let's also
# create some return functions within the main super class
# so we can call them through it. These return functions have
# no argument variables and no keyword argument variables.
# However, you can create some of your own if you like.

class Main_super_class_attribute_properties:

    def return_pet():
        return 'Dog','Cat','Bird','Fish'

    def return_pet_care():
        return 'Leash','Litter box','Cage','Aquarium'

    def return_pet_toys():
        return 'Ball','Mouse toy','Bells','Air stone'

    def return_pet_cost():
        return 10,20,8,100

    def __init__(self,var1,var2,var3):

        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

class Sub_super_class1_attribute_properties(
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4):
        super().__init__(var1,var2,var3)

        self.class_var4=var4

class Sub_super_class2_attribute_properties(
    Sub_super_class1_attribute_properties,
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4)

        self.class_var5=var5

class Sub_super_class3_attribute_properties(
    Sub_super_class2_attribute_properties,
    Sub_super_class1_attribute_properties,
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4,var5,var6):
        super().__init__(var1,var2,var3,var4,var5)

        self.class_var6=var6

class Sub_class4_same_attribute_properties(
    Sub_super_class3_attribute_properties,
    Sub_super_class2_attribute_properties,
    Sub_super_class1_attribute_properties,
    Main_super_class_attribute_properties):pass

a = Main_super_class_attribute_properties(
    'This is an instance of a main super class object with three attribute properties 1',
    'This is an instance of a main super class object with three attribute properties 2',
    'This is an instance of a main super class object with three attribute properties 3').class_var3

b = Sub_super_class1_attribute_properties(
    'This is an instance of a sub super class1 object with four attribute properties 1',
    'This is an instance of a sub super class1 object with four attribute properties 2',
    'This is an instance of a sub super class1 object with four attribute properties 3',
    'This is an instance of a sub super class1 object with four attribute properties 4').class_var4

c = Sub_super_class2_attribute_properties(
    'This is an instance of a sub super class2 object with five attribute properties 1',
    'This is an instance of a sub super class2 object with five attribute properties 2',
    'This is an instance of a sub super class2 object with five attribute properties 3',
    'This is an instance of a sub super class2 object with five attribute properties 4',
    'This is an instance of a sub super class2 object with five attribute properties 5').class_var5

d = Sub_super_class3_attribute_properties(
    'This is an instance of a sub super class3 object with six attribute properties 1',
    'This is an instance of a sub super class3 object with six attribute properties 2',
    'This is an instance of a sub super class3 object with six attribute properties 3',
    'This is an instance of a sub super class3 object with six attribute properties 4',
    'This is an instance of a sub super class3 object with six attribute properties 5',
    'This is an instance of a sub super class3 object with six attribute properties 6').class_var6

e = Sub_class4_same_attribute_properties(
    'This is an instance of a sub class4 object with six attribute properties 1',
    'This is an instance of a sub class4 object with six attribute properties 2',
    'This is an instance of a sub class4 object with six attribute properties 3',
    'This is an instance of a sub class4 object with six attribute properties 4',
    'This is an instance of a sub class4 object with six attribute properties 5',
    'This is an instance of a sub class4 object with six attribute properties 6').class_var6

# Print out all individual class attribute property values.

print(a)

print(b)

print(c)

print(d)

print(e)

# Print out returned values within the main super class object.

f = (
    Main_super_class_attribute_properties.return_pet()[0],
    Main_super_class_attribute_properties.return_pet()[1],
    Main_super_class_attribute_properties.return_pet()[2],
    Main_super_class_attribute_properties.return_pet()[3])

g = (
    Main_super_class_attribute_properties.return_pet_care()[0],
    Main_super_class_attribute_properties.return_pet_care()[1],
    Main_super_class_attribute_properties.return_pet_care()[2],
    Main_super_class_attribute_properties.return_pet_care()[3])

h = (
    Main_super_class_attribute_properties.return_pet_toys()[0],
    Main_super_class_attribute_properties.return_pet_toys()[1],
    Main_super_class_attribute_properties.return_pet_toys()[2],
    Main_super_class_attribute_properties.return_pet_toys()[3])

i = (
    Main_super_class_attribute_properties.return_pet_cost()[0],
    Main_super_class_attribute_properties.return_pet_cost()[1],
    Main_super_class_attribute_properties.return_pet_cost()[2],
    Main_super_class_attribute_properties.return_pet_cost()[3])

print(f[3])

print(g[3])

print(h[3])

print(i[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tip: If you invoke the plus + sign instead of a comma, you may
# have to use the str(), string function in some cases. For example,
# you might want to add or subtract integer numbers, while wanting
# to use the plus + sign to concatenate strings with integer numbers.
# Here are two examples of both types, using commas and plus +
# signs, along with one str(), string function when plus + signs are
# invoked instead of commas such as in our second example.

num1 = 10
num2 = 5

print("Let's add some numbers together:",num1+num2,'like this.')

print("Let's subtract some numbers:",num1-num2,'like this.')

# Or this when invoking plus + signs to concatenate strings together
# with integer numbers, via invoking the str(), string function.

print("Let's add some numbers together: "+str(num1+num2)+' like this.')

print("Let's subtract some numbers: "+str(num1-num2)+' like this.')

# Invoke the new f' string format to make string concatenation much easier.

print(f"Let's add some numbers together: {num1+num2} like this.")

print(f"Let's subtract some numbers: {num1-num2} like this.")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do some experimenting with define functions and see
# what we can conjure up. Let's create an outer and inner
# define function. Note: you cannot directly call inner
# define functions. You must call the inner define function
# within the outer define function to gain access to the inner
# function at execution/run time.

def outer_define_function():
    print('Outer define function.')

    def inner_define_function():
        print('Inner define function.')

    inner_define_function()

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same define function experiment as the example
# above; all we did was add more inner define functions inside the
# outer define function block.

def outer_define_function():
    print('Outer define function.')

    def inner_define_function1():
        print('Inner define function one.')

    def inner_define_function2():
        print('Inner define function two.')

    def inner_define_function3():
        print('Inner define function three.')

    inner_define_function1()
    inner_define_function2()
    inner_define_function3()

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try some inner return define functions within an outer define
# function.

def outer_define_function():

    def inner_define_function1():
        return 'Return inner define function one.'

    def inner_define_function2():
        return 'Return inner define function two.'

    def inner_define_function3():
        return 'Return inner define function three.'

    print(inner_define_function1())
    print(inner_define_function2())
    print(inner_define_function3())

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try some more inner return define functions within an outer
# define function. Let's create multiple return values within each
# inner define function. Let's also invoke the " \ " backslash to force
# hard line breaks.

def outer_define_function():

    def inner_define_function1():

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2():

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3():

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    print(inner_define_function1()[2])
    print(inner_define_function2()[2])
    print(inner_define_function3()[2])

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's pack global variables to be called outside the outer define
# function. Invoke the " \n " backslash 'n' to create line breaks in
# the screen output at execution/run time.

def outer_define_function():

    global a,b,c

    def inner_define_function1():

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2():

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3():

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1()[2]
    b = inner_define_function2()[2]
    c = inner_define_function3()[2]

outer_define_function()

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will
# create argument variables to satisfy argument placeholder values.

def outer_define_function(argument_variable):

    global a,b,c

    def inner_define_function1(argument_variable):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(argument_variable):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(argument_variable):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1('argument placeholder value')[2]
    b = inner_define_function2('argument placeholder value')[2]
    c = inner_define_function3('argument placeholder value')[2]

outer_define_function('agument placeholder value')

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will
# create multiple argument variables to satisfy multiple argument
# placeholder values.

def outer_define_function(
    argument_variable1,
    argument_variable2,
    argument_variable3):

    global a,b,c

    def inner_define_function1(
        argument_variable1,
        argument_variable2,
        argument_variable3):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(
        argument_variable1,
        argument_variable2,
        argument_variable3):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(
        argument_variable1,
        argument_variable2,
        argument_variable3):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    b = inner_define_function2(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    c = inner_define_function3(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

outer_define_function(
    'agument placeholder value',
    'agument placeholder value',
    'agument placeholder value')

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will
# create multiple keyword argument variables to satisfy multiple
# keyword argument placeholder values.

def outer_define_function(
    keyword_argument_variable1,
    keyword_argument_variable2,
    keyword_argument_variable3):

    global a,b,c

    def inner_define_function1(
        keyword_argument_variable1,
        keyword_argument_variable2,
        keyword_argument_variable3):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(
        keyword_argument_variable1,
        keyword_argument_variable2,
        keyword_argument_variable3):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(
        keyword_argument_variable1,
        keyword_argument_variable2,
        keyword_argument_variable3):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    b = inner_define_function2(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    c = inner_define_function3(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

outer_define_function(
    keyword_argument_variable1 = 'argument placeholder value',
    keyword_argument_variable2 = 'argument placeholder value',
    keyword_argument_variable3 = 'argument placeholder value',)

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will invoke
# the *args prefix to satisfy any number argument placeholder values,
# without the worry of how many argument placeholder values are
# needed to be satisfied.

def outer_define_function(*args):

    global a,b,c

    def inner_define_function1(*args):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(*args):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(*args):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    b = inner_define_function2(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    c = inner_define_function3(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

outer_define_function(
    'agument placeholder value',
    'agument placeholder value',
    'agument placeholder value')

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will invoke
# the **kwargs prefix to satisfy any number keyword argument placeholder
# values, without the worry of how many keyword argument placeholder
# values are needed to be satisfied.

def outer_define_function(**kwargs):

    global a,b,c

    def inner_define_function1(**kwargs):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(**kwargs):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(**kwargs):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    b = inner_define_function2(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    c = inner_define_function3(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

outer_define_function(
    keyword_argument_variable1 = 'argument placeholder value',
    keyword_argument_variable2 = 'argument placeholder value',
    keyword_argument_variable3 = 'argument placeholder value',)

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Have some fun with these return define function examples.

def return_variable(name='John'):

    return f'Hello {name} and welcome to Python programming!'

print(return_variable())

print(return_variable('Jack'))

print(return_variable('Jim'))

print(return_variable('Bob'))

print(return_variable('Rob'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion'))

print(return_variable('ostrich'))

print(return_variable('shark'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1} and my {pet2} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion','tiger'))

print(return_variable('ostrich','shoebill'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1}, {pet2} and my {pet3} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion','tiger'))

print(return_variable('ostrich','shoebill','vulture'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1}, {pet2}, {pet3} and my {pet4} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion','tiger'))

print(return_variable('ostrich','shoebill','vulture'))

print(return_variable('octopus','squid','cuttlefish','sea monster'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create define functions that return integer number calculations.
# Let's also invoke the int(), integer function to create integer number
# calculations only.

def int_num_cal(nums):
    return int(nums+nums)

print(int_num_cal(5))  # 5+5 = 10
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(nums):
    return int(nums-nums)

print(int_num_cal(5))  # 5-5 = 0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(nums):
    return int(nums*nums)

print(int_num_cal(5))  # 5*5 = 25
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(nums):
    return int(nums/nums)

print(int_num_cal(5))  # 5/5 = 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1+num2)

print(int_num_cal(10,5))  # 10+5 = 15
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1-num2)

print(int_num_cal(10,5))  # 10-5 = 5
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1*num2)

print(int_num_cal(10,5))  # 10*5 = 50
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1/num2)

print(int_num_cal(10,5))  # 10/5 = 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create define functions that return floating point number
# calculations. Let's also invoke the float(), floating point function
# to create floating point number calculations only.

def float_num_cal(nums):
    return float(nums+nums)

print(float_num_cal(5))  # 5+5 = 10.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(nums):
    return float(nums-nums)

print(float_num_cal(5))  # 5-5 = 0.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(nums):
    return float(nums*nums)

print(float_num_cal(5))  # 5*5 = 25.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(nums):
    return float(nums/nums)

print(float_num_cal(5))  # 5/5 = 1.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1+num2)

print(float_num_cal(10,5))  # 10+5 = 15.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1-num2)

print(float_num_cal(10,5))  # 10-5 = 5.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1*num2)

print(float_num_cal(10,5))  # 10*5 = 50.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1/num2)

print(float_num_cal(10,5))  # 10/5 = 2.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try a couple of more return function math calculations
# with more argument values to be satisfied and calculated.

def int_num_cal(num1,num2,num3,num4):
    return int(num1*num2+num3-num4)

print(int_num_cal(10,5,3,2))  # 10*5+3-2 = 51
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2,num3,num4):
    return float(num1*num2+num3-num4)

print(float_num_cal(10,5,3,2))  # 10*5+3-2 = 51.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# We can also reuse Python code over and over again and again.

def int_num_cal(num1,num2,num3,num4):
    return int(num1*num2+num3-num4+num1/num4)

print(int_num_cal(10,5,3,2))  # 10*5+3-2+10/2 = 56
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2,num3,num4):
    return float(num1*num2+num3-num4+num1/num4)

print(float_num_cal(10,5,3,2))  # 10*5+3-2+10/2 = 56.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create exponents in Python, via invoking a
# double ** asterisk to create exponents. Exponents are numbers
# that are multiplied by the same number. For example: 2*2 = 4

def int_num_cal(num1,num2):
    return int(num1**num2)

print(int_num_cal(10,2))  # 10*10 = 100
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1**num2)

print(float_num_cal(10,2))  # 10*10 = 100.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create cube exponents in Python, via invoking
# a double ** asterisk to create cube exponents. Cube exponents are
# numbers that are multiplied by the same number three times.
# For example: 2*2*2 = 8

def int_num_cal(num1,num2):
    return int(num1**num2)

print(int_num_cal(10,3))  # 10*10*10 = 1000
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1**num2)

print(float_num_cal(10,3))  # 10*10*10 = 1000.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1**num2)

print(int_num_cal(10,4))  # 10*10*10*10 = 10000
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1**num2)

print(float_num_cal(10,4))  # 10*10*10*10 = 10000.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can create exponents with the pow(), power function.

print(int(10**2))   # 10*10 = 100

# or this example:

print(int(pow(10,2)))   # 10*10 = 100

# Or this if you want floating point number calculations.

print(float(10**2))   # 10*10 = 100.0

# or this example:

print(float(pow(10,2)))   # 10*10 = 100.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python has a square root function that finds the square root of a
# number. You have to import the math module for the sqrt() function
# to work. Invoke the int(), integer function to create integer number
# calculations only.

import math

print(int(math.sqrt(9)))  # 9 squared = 3

# Or this if you want floating point number calculations.

print(float(math.sqrt(9)))  # 9 squared = 3.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some little tidbits, I've picked up along my Python
# programming journey over seven years since Christmas day, 2017.

# When writing large numbers in Python code, you can do this to
# break down large number units like this example:

print(2_000_000_000)  # 2000000000

# If you want the output screen to display broken-down number
# units in Python, you can simply do this example:

# Note: you must invoke the f' string format to be able to do the
# following Python programming examples.

print(f'{2000000000:,}')  # 2,000,000,000

# or this example:

print(f'{2_000_000_000:,}')  # 2,000,000,000
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the ord(), ordinal function to generate ascii code values.

ordinal = (
    '0','1','2','3','4','5','6','7','8','9',

    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',

    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z')

print('lowercase a =',ord('a'),'and uppercase A =',ord('A'))

# invoke the chr(), character function to generate ascii code characters.

character = (
    '48','49','50','51','52','53','54','55','56','57',

    '97','98','99','100','101','102','103','104','105','106',
    '107','108','109','110','111','112','113','114','115','116',
    '117','118','119','120','121','122',

    '65','66','67','68','69','70','71','72','73','74',
    '75','76','77','78','79','80','81','82','83','84',
    '85','86','87','88','89','90')

print(ord('a'),'= lowercase',chr(97),'and',ord('A'),'= uppercase',chr(65))

# Invoke the new f' string format for easier string concatenation.

print(f'{ord("a")} = lowercase {chr(97)} and {ord("A")} = uppercase {chr(65)}' )
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Make the decimal base 10 number system calculate, then convert
# the result in binary base 2, hexadecimal base 16 and octal base 8
# number systems. Note: you must invoke the f' string format to be
# able to do the following Python programming examples.

num_convert = 5+250

print(f'Binary number: {num_convert:b} = decimal number: {num_convert}...')

# Binary number: 11111111 = decimal number: 255...

print(f'Hexadecimal number: {num_convert:x} = decimal number: {num_convert}...')

# Hexadecimal number: ff = decimal number: 255...

print(f'Octal number: {num_convert:o} = decimal number: {num_convert}...')

# Octal number: 377 = decimal number: 255...

# You can also use these prefixes for generating binary base 2 numbers,
# hexadecimal base 16 numbers and octal base 8 numbers.

print(bin(255))  # 0b11111111

print(hex(255))  # 0xff

print(oct(255))  # 0o377

# See the illustration examples below:

num_convert = 5+250

print('Binary number:',bin(num_convert),'= decimal number:',str(num_convert)+'...')

# Binary number: 0b11111111 = decimal number: 255...

print('Hexadecimal number:',hex(num_convert),'= decimal number:',str(num_convert)+'...')

# Hexadecimal number: 0xff = decimal number: 255...

print('Octal number:',oct(num_convert),'= decimal number:',str(num_convert)+'...')

# Octal number: 0o377 = decimal number: 255...

# Invoke the f' string format to make string concatenation much easier if you like.

print(f'Binary number: {bin(num_convert)} = decimal number: {num_convert}...')

print(f'Hexadecimal number: {hex(num_convert)} = decimal number: {num_convert}...')

print(f'Octal number: {oct(num_convert)} = decimal number: {num_convert}...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a working binary to hexadecimal to octal to decimal
# counter with a for loop that will count all the way up to 255, which
# is exactly one 8b byte: 11111111 = decimal: 255. We have to import
# the time module to use the time.sleep() function within our for loop.

import time

for i in range(256):
    print(f'Binary number: {i:b} = decimal number: {i}...')

    print(f'Hexadecimal number: {i:x} = decimal number: {i}...')

    print(f'Octal number: {i:o} = decimal number: {i}...')

    time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's recreate the Python program example above, but we will make
# it more articulated with how many actual bits in one binary 8 bit byte
# there are as the binary digits count on 0 through to 255, which is exactly
# the equivalent of an 8 bit binary byte. To make this possible, we will
# need to invoke the len(), length function to count out how many bits
# to whatever binary number values there are.

import time

for i in range(256):
    print(
        'Binary number bits in one 8b byte =',\
        len(f'{i:b}'),f'bits = Binary number: {i:b} = decimal number: {i}...')

    print(f'Hexadecimal number: {i:x} = decimal number: {i}...')

    print(f'Octal number: {i:o} = decimal number: {i}...')

    time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now reconstruct the very same Python program above, but we
# will drastically reduce Python code down to just one, single print()
# function.

import time

for i in range(256):
     print(
'Binary number bits in one 8b byte =',\
len(f'{i:b}'),f'bits = Binary number: {i:b} = decimal number: {i}...\n\
Hexadecimal number: {i:x} = decimal number: {i}...\n\
Octal number: {i:o} = decimal number: {i}...')

     time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# also create a problem, purposely to know that I'm starting to understand
# something in programming code, and why it works like it does. Here are
# some examples of what I keep, so I can gain instant copy and paste to reuse
# the code, instead of having to always start fresh, when I know I will use this
# code again down the road. So why not create programming layers to make
# programming much faster on your part, when you can have tons of Python
# programming snippets over time. It sure does pay off in spades to kep them...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is an easy to understand define function example, I kept, so I could
# reuse it again down the road for another Python program, I create.

def my_define_function():
    print('Python is Great!!')

my_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example of a simple return define function, I kept.

def my_return_argument_value():
    return 'I need no return argument values to be satisfied. Thank you...'

print(my_return_argument_value())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example of a return define function with one argument value,
# I kept.

def my_return_argument_value(argument):
    return 'I need one return argument value to be satisfied. Thank you...'

print(my_return_argument_value('one return argument placeholder value.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a default class setup, I created, so I could reuse it someday down the
# road, whenever I might need to use it again for another program, I create.

class Single_class:

    def __init__(self,arg):
        self.arg=arg

print(Single_class('Hello World!').arg)

# or this goofy ha ha class example:

class Single_class:

    def __init__(me_myself_and_i,arg):
        me_myself_and_i.goofy=arg

print(Single_class('Python goes Goofy!').goofy)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is another class program snippet, I kept. I break things down
# to where and when I can start to finally understand what the Python
# code is all about and why it works the way it does.

class Single_class:

    def __init__(self,var1,var2,var3):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

print(Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.').class_var3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a main class and a sub class Python program snippet, I kept
# so I could reuse it down the road for another Python program, I create.

class Main_class_attribute_properties:

    def __init__(self,var1,var2,var3):
        self.var1=var1
        self.var2=var2
        self.var3=var3

class Sub_class_attribute_properties(  # inhert main class properties
    Main_class_attribute_properties):pass

print(Main_class_attribute_properties('I am value1','I am value2','I am value3').var3)

print(Sub_class_attribute_properties('I am value1','I am value2','I am value3').var3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a main super class and a sub super class Python program snippet,
# I kept so I could reuse it down the road for another Python program, I create.

class Main_super_class_attribute_properties:

    def __init__(self,var1,var2,var3):
        self.var1=var1
        self.var2=var2
        self.var3=var3

class Sub_super_class_attribute_properties(
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3)

        self.var4=var4
        self.var5=var5

print(Main_super_class_attribute_properties('I am value1','I am value2','I am value3').var3)

print(Sub_super_class_attribute_properties(
    'I am value1','I am value2','I am value3','I am value4','I am value5').var5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# List Comprehension in Python

# Like always, I research when I want to learn something new, or new to me.
# Since the years I've played around with Python programming, I never ever
# explored list comprehension at all. This is like killing two birds with one
# stone's throw. I'm only experimenting with this tonight; I kept on ignoring it.
# But it shortens for loops down, when looping through a list, using a for loop
# right inside the list[ ] brackets. Believe it or not, I'm also new to this list
# comprehension thing. So you are not alone on this one. But try these out and
# tinker with them. I did that here. I just play and tinker and see what works and
# what won't work. This is what computer science is all about. Sometimes you
# just have to keep on learning and do constant research; you can only avoid
# something for so long, like I did with this headache. But like everything we
# learn; it gets easier over time. Happy researching. I'm also happily doing
# research with these below.

text_list = ['dog','cat','bird','fish','turtle']

words = [text for text in text_list]

print(words)

text_list = ['dog','cat','bird','fish','turtle']

words = [text if text == 'dog' else 'none' for text in text_list]

print(words[1])

num_list = [1,2,3,4,5]

nums = [num for num in num_list]

print(nums)

num_list = []

nums = [num for num in range(20)]

print(nums)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the enumerate() function to loop through a list, using
# only two lines of code; one for the for-index enumerate()
# function and the other for the 'print' statement.

name_list=['John','Bob','Rob','Tom']

# Here is a simple for-loop that will loop through the name_list
# values starting with index 0, followed by index 1 and then
# index 2, and finally index 3.

for index in name_list:
    print(index)

# The for-loop example above is fine, but it has its limitations
# when it comes to multi indexing through a tuple or list alike.
# With the enumerate() function, such things are possible.
# Try these enumerate() function Python program examples
# below and see what happens when you experiment with them.

for index,name in enumerate(name_list):
    print(index)

for index,name in enumerate(name_list):
    print(name)

for index,name in enumerate(name_list):
    print(index,name)

for index,name in enumerate(name_list,start=1):
    print(index,name)

name=['John','Bob','Rob','Tom']
pet=['Dog','Cat','Bird','Fish']
computer=['Desktop','Laptop','Cellphone','Notebook']

# Note: the zip() function only goes to the shortest length
# in a multi list. However, you can simply keep them the
# same size such as the list examples above, which shows
# three lists called name, pet and computer. Each list has
# four values in them. This way, every value gets called inside
# one, single 'print' statement. Try these different examples
# below. Note: you can rename the words 'index1, index2 and
# index3' to any names you wish. You can also rename the
# name variable if you like.

for index1,index2,index3 in zip(name,pet,computer):
    print(index1)

for index1,index2,index3 in zip(name,pet,computer):
    print(index2)

for index1,index2,index3 in zip(name,pet,computer):
    print(index3)

for index1,index2,index3 in zip(name,pet,computer):
    print(index1,index2,index3)

# Let's try the enumerate() function with a 2d-list.

my_2d_list=[
    ['John','Bob','Rob','Tom'],
    ['Desktop','Laptop','Cellphone','Notebook']]

for index,name in enumerate(my_2d_list):
    print(index)

for index,name in enumerate(my_2d_list):
    print(name[0])

for index,name in enumerate(my_2d_list):
    print(index,name[0])

for index,name in enumerate(my_2d_list,start=1):
    print(index,name[0])

# Let's try the zip() function with a 2d-list.

my_2d_list=[
    ['John','Bob','Rob','Tom'],
    ['Desktop','Laptop','Cellphone','Notebook']]

for index in zip(my_2d_list):
    print(index[0][0])

for index in zip(my_2d_list):
    print(index[0][0],index[0][1],index[0][2],index[0][3])

# Let's try some fun experiment examples with some of what
# we've learned so far about the enumerate() function. Let's
# create a program that uses a sentence for each value in the
# fun_list1,  fun_list2 and fun_list3 lists. Let's use the f' format
# to make string concatenations much easier to create.

fun_list1=['John','Bob','Rob','Tom']
fun_list2=['Dog','Cat','Bird','Fish']
fun_list3=['Desktop','Laptop','Cellphone','Notebook']

for index,name in enumerate(fun_list1):
    print(f"My name is {name}. I'm the value from the fun_list1, position {index}")

for index,name in enumerate(fun_list2):
    print(f"I am a {name}. I'm the value from the fun_list2, position {index}")

for index,name in enumerate(fun_list3):
    print(f"I am a {name}. I'm the value from the fun_list3, position {index}")

# These enumerate() function examples are great, but let's beef it up just a lot
# more with the zip() function, so we can create complex actions with all our
# fun_lists combined into complete, separate sentences, just simply using two
# lines of code. See what happens when you type and execute/run this Python
# program example below:

for list1,list2,list3 in zip(fun_list1,fun_list2,fun_list3):
    print(f"My name is {list1} and I have a {list2} picture on my {list3} screen.")

# The zip() function is very useful, but it can only reach as far as its shortest
# list length. That means, if you have two, three or more lists, the shortest list
# out of the three or more lists values will be cut off from the rest if one or more
# lists have extra values inside them. To avoid this from occurring, make all your
# lists the same size in each of their values. take a look at the example below:

fun_list1=['John','Bob','Rob','Tom'] # four values
fun_list2=['Dog','Cat','Bird','Fish'] # four values
fun_list3=['Desktop','Laptop','Cellphone','Notebook'] # four values

# The zip() function is sometimes better than a simple for-loop or a
# simple enumerate() function, in that it uses less lines of code and
# it can also achieve a far better programming style approach over
# program code redundancy on the programmer's part.

# Let's try one more example to prove this to be true. let's create another
# fun_list, zip() function Python program example. Type and execute/run
# this Python program below and see what happens with the output.

fun_list1=['John','Bob','Rob','Tom']
fun_list2=['Dog','Cat','Bird','Fish']
fun_list3=['Desktop','Laptop','Cellphone','Notebook']
fun_list4=['loves my','hates my','found my','lost my']
fun_list5=['fed his',"didn't feed his",'plays with his',"doesn't play with his"]

for list1,list2,list3,list4,list5 in zip(fun_list1,fun_list2,fun_list3,fun_list4,fun_list5):
    print(f'{list1} {list4} {list3} and {list5} {list2}.')

# Well, I think we pretty much learned what the enumerate() and zip()
# functions do. Now, it's practice, practice and more practice, practice...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sometimes if you are going to be using and reusing small bits of
# Python code over and over again, you might want to consider using
# the 'exec()' function. The 'exec()' function can be used in such
# examples as these examples below.

redundant_code='''
print("Python Programmer's Glossary Bible")
print('This block of code can be used and reused again and again.')
'''
# Call the 'exec()' function as many times as you please.

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example, using a for-loop to call the 'exec()' function.

for i in range(3):
    exec(redundant_code)

# Let's create a for loop inside an exec() function and see what happens
# when execute/run this Python program example:

reuse_code='''
for i in range(10):print(i)
'''
exec(reuse_code) # call the exec() function as many times as you wish
exec(reuse_code)
exec(reuse_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# BONUS! Flip Flop Game Python program example:

# This little flip flop game is a great example of how the conditional
# while-loop works. The 'else' statement executes/runs when the user
# types the wrong keys, and the while-loop iterates/repeats over again
# while ignoring the 'break' statement.

print('\nWelcome to the Flip Flop Game')

print('\nPlease type the words "flip" or "flop", then press (ENTER)')

print('\nWhen you get bored, press (ENTER) to quit playing Flip Flop')

while True:
    flip_flop=input('\nFlip? or Flop? ').strip()

    if flip_flop=='flip':
        print('\nFlop')

    elif flip_flop=='flop':
        print('\nFlip')

    elif flip_flop=='':
        print('\nThanks for playing Flip! Flop!')
        break

    else:
        print('\nYou can\'t cheat now! Do you flip? or do you flop?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I Never ever use these myself, but they are another tool I might one
# day have a usefulness for. But here is some researching I had done
# with 'lambda functions() These are, what they call anonymous functions,
# because you use them, then throw them away; whatever that means
# is still unclear to me at this time. So every time I learn something new,
# I always try to expand on it myself with different approaches to whatever
# it is, I might be wanting to learn or understand. Python has so many
# bells and whistles, that I won't in my entire lifetime live to be able to use
# them all, or even understand them all. I'm an almost a Pythonista programmer,
# but I'm not God either. But this is stuff I had learned but I might never
# ever use such bells and whistles at all. But, sometimes we all have to
# learn new tricks in our fields of interests even if we never use such things
# in our fields, whatever they might be. Every field of interest has their own
# fair share of bells and whistles, just like my chosen field of interest does.
# I love robots, computer science, and had also developed a keen ability to
# do breadboard electronics with a Raspberry Pi 4, since the last two years.
# Anyway, have some fun with these lambda functions(), or not. lol

lambda_func = lambda x:x + 2

print(lambda_func(5))

lambda_func = lambda x:x - 2

print(lambda_func(7))

lambda_func = lambda x,y:x + y

print(lambda_func(5,2))

lambda_func = lambda x,y:x - y

print(lambda_func(7,2))

lambda_func = lambda x,y,z:x + y + z

print(lambda_func(4,2,1))

lambda_func = lambda x,y,z:x - y + z

print(lambda_func(7,5,3))

lambda_func = lambda x,y,z:x - y + z + 2

print(lambda_func(7,5,3))

lambda_func = lambda first,middle,last:first+middle+last

print(lambda_func('Joseph',' C.',' Richardson'))

lambda_func = lambda first,middle,last,science:first+middle+last+science

print(lambda_func('Joseph',' C.',' Richardson',' is into Computer Science.'))

lambda_func = lambda x:True if x> 2 else False

print(lambda_func(2))

lambda_func = lambda x:'Thank you.' if x> 2 else 'I want a higher number than two!'

print(lambda_func(2))

lambda_func = lambda x:True if x> 2 else False

print(lambda_func(2))

lambda_func = lambda x:True if x>= 2 else False
print(lambda_func(2))

lambda_func = lambda x:'Thank you.' if x>= 2 else 'I want a number to equal two or \
higher than two!'

print(lambda_func(2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Backward Poem Text Python program example:

# This poem was written by Joseph C. Richardson

poem = ('''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''[::-1],

'''.tneduts tsetaerg rieht era uoy roF !flesruoy ni eveileB
…su fo srehcaet tsetaerg eht ,suht era dnim eht dna traeh eht roF
.noitanigami ruo fo noitaerc s’maerd eht
,lla fo amolpid tsetaerg eht ot yek eht dloh dnim eht dna traeh eht roF
.rednow otni rednop ot yek eht si nettirw eb ot maxe ylno ehT
.dnim eht dna traeh eht era ,dedeen skoobtxet ylno ehT
!flesti dnim eht fo dna traeh eht fo noitnevni eerf a si
’egdelwonK‘'''[::-1])

print(poem[0])

print(poem[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Well folks, it looks like the end of the line. We've covered such a lot
# about Python programming. We learned how to dissect and break
# down hard Python programming examples with a step-by-step approach.

# What I've illustrated here are ways, I learn and retain knowledge about
# Python programming in general. I keep Python program snippets to
# quickly recall and reuse them down the road. Keeping snippets of Python
# code makes creating the next Python program even faster than one
# would without snippets of Python code to reuse down the road.

# Also most importantly is writing down comments about the Python program
# or Python code you want to remember how to write, should you forget
# how to write it over a period of time. Please keep this in mind at all times.
# Get into the habit of writing down comments about Python programs and/or
# Python programming code alike.

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs...

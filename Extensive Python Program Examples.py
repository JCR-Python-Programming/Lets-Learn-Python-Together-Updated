# Here are some extensive hands-on, in depth Python program examples.

# Let's learn what Python lists are all about with these
# Python program examples.

# print out list values onto the screen output

my_list = ['Python',"Programmer's",'Glossary','Bible']

print(my_list[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# change 'my_list' value 'Bible' to the value 'Book'

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list[3] = 'Book'

print(my_list[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# insert three new values into my_list with indexing

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list[2:0] = ['Fun','Greate','Book']

print(my_list[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# add the value 'Book' to my_list with the append( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.append('Book')

print(my_list[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# insert a new value 'Book' into my_list at index[3]
# with the 'insert( )' function

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.insert(3,'Book')

print(my_list[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# remove the last value at the end of my_list with the
# pop( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

# create a variable called popped, so you can see the
# value that was removed or popped off my_list, via the pop()
# function

popped = my_list.pop()

print(popped)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# remove the second value of my_list with the pop( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

# create a variable called popped, so you can see the
# value that was removed or popped off my_list, via the pop()
# function

popped = my_list.pop(1)

print(popped)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# remove a value from my_list with the remove( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.remove("Programmer's")

print(my_list[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# empty all values in my_list with the clear( ) function,
# without deleting the my_list variable

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.clear()

print(my_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# delete the entire my_list variable and values, via
# invoking the 'del' prefix. Note: when you type and
# execute/run this Python program example, the program
# will cause and error and crash the program. This is
# simply because my_list doesn't exist anymore

my_list = ['Python',"Programmer's",'Glossary','Bible']

del my_list

print(my_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# delete the my_list value at index[1], via invoking the 'del'
# prefix

my_list = ['Python',"Programmer's",'Glossary','Bible']

del my_list[1]

print(my_list[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# copy all the values in my_list to the items_list with the
# copy( ) function, then check the two lists to view them
# on the screen output at program execution time

my_list = ['Python',"Programmer's",'Glossary','Bible']

items_list = my_list.copy()

print(items_list)

print(my_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# join two lists together with the extend( ) function, then
# check my_list1 to view them on the screen output at
# execution time

my_list1 = ['Python',"Programmer's",'Glossary','Bible']

my_list2 = ['We','Sure','Love','Python','Programming']

my_list1.extend(my_list2)

print(my_list1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what Python dictionaries are all about with these
# Python program examples.

# print out key values onto the screen output

my_dictionary = {
    'key1':'Python','key2':"Programmer's",'key3':'Glossary','key4':'Bible'}

print(my_dictionary.get('key1'))

print(my_dictionary.get('key2'))

print(my_dictionary.get('key3'))

print(my_dictionary.get('key4'))

print(my_dictionary.get('key5'))

print(my_dictionary.get('key5','Key Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# print out key values with a partial tuple within 'my_dictionary_list'

my_dictionary_tuple = {
    'key1':'Python','key2':("Programmer's",'Glossary','Bible'),'key3':'is','key4':'Great!'}

print(my_dictionary_tuple.get('key1'))

print(my_dictionary_tuple.get('key2')[0])

print(my_dictionary_tuple.get('key2')[1])

print(my_dictionary_tuple.get('key2')[2])

print(my_dictionary_tuple.get('key3'))

print(my_dictionary_tuple.get('key4'))

print(my_dictionary_tuple.get('key1','Key Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# print out key values with a partial list within 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

print(my_dictionary_list.get('key1'))

print(my_dictionary_list.get('key2')[0])

print(my_dictionary_list.get('key2')[1])

print(my_dictionary_list.get('key2')[2])

print(my_dictionary_list.get('key3'))

print(my_dictionary_list.get('key4'))

print(my_dictionary_list.get('key5','Key Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# update a key's value to change its value in 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list.update({'key1':'Book'})  # key1 value was 'Python'

print(my_dictionary_list.get('key1'))  # Book
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# update a key's value to change its value in 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list['key1'] = 'Book'  # key1 value was 'Python'

print(my_dictionary_list.get('key1'))   # Book
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'pop( )' function to delete/pop 'key2' from 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list.pop('key2')

print(my_dictionary_list.get('key2','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# return a 'poopped' dictionary{ } 'key' from 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

popped = my_dictionary_list.pop('key1')

print(popped)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# completely delete a dictionary{ } 'key' from 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

del my_dictionary_list['key1']

print(my_dictionary_list.get('key1','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# clear the entire 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list.clear()

print(my_dictionary_list.get('key1','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'items()' function to view the complete 'my_dictionary_list'
# with 'keys' and 'key values'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

list_items = my_dictionary_list.items()

print(list_items)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'items()' function to view the 'my_dictionary_list' 'keys' and 'key values'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

# invoke the 'items()' function to view the 'my_dictionary_list' 'keys' only

print(my_dictionary_list.keys())

# invoke the 'items()' function to view the 'my_dictionary_list' 'values' only

print(my_dictionary_list.values())

# invoke the 'items()' function using a for loop to view the 'my_dictionary_list'
# 'keys' and 'key values'

for keys, values in my_dictionary_list.items():
  print(keys, values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# change a key's value in 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list['key1'] = 'We Sure Love Python!'

print(my_dictionary_list.get('key1'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create an animals dictionary so we can use its values.

animals={
    'Dog':'Wolf',
    'Cat':'Lion',
    'Bird':'Eagle',
    'Fish':'Shark'
    }

print(animals.get('dog'))

print(animals.get('dog','Not Found!'))  # optional

print(animals.get('Dog','Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for key,value in animals.items():
    print(key)

for key,value in animals.items():
    print(value)

for key,value in animals.items():
    print(key,value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some sentences out of our animals dictionary list.

d=animals.get('Dog')
c=animals.get('Cat')
b=animals.get('Bird')
f=animals.get('Fish')

print(f'My dog is really a {d}.')
print(f'My Cat is really a {c}.')
print(f'My Bird is really a {b}.')
print(f'My Fish is really a {f}.')

# Let's create some sentences out of our animals dictionary list
# using a 'for in' items() function to drastically reduce lines of
# code and code redundancy in our Python program example.

for keys,values in animals.items():
    print(f'My {keys} is really a {values}.')

# Rename the key and value variables if you wish.

for my_keys,my_values in animals.items():
    print(f'My {my_keys} is really a {my_values}.')

for animal_keys,animal_values in animals.items():
    print(f'My {animal_keys} is really a {animal_values}.')

# Try this dictionary Python program example below and recap
# what happens when you type and execute/run this program.

animals={
    'Dog':'Wolf',
    'Cat':'Lion',
    'Bird':'Eagle',
    'Fish':'Shark'}

people={              
    'Person1':'Tom',
    'Person2':'Bob',
    'Person3':'Rob',
    'Person4':'Ron'}

for key,value in animals.items():
    print(key,value)

for key,value in people.items():
    print(key,value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a dictionary that's also a complete list of values
# to one, single key each.

my_dictionary_list={
  'key1':['Dog,','Cat','Bird','fish'],
  'key2':['Tom','Bob','Rob','Ron']}

print(my_dictionary_list.get('key1')[0])

print(my_dictionary_list.get('key2')[0])

print(my_dictionary_list.get('key5','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python can show you what 'type' of string, integer and float values
# you are using to help you understand what 'str', 'int', and 'float values
# are.

print(type('text string'))  # <class 'str'>

print(type(1))  # <class 'int'>

print(type(1.0))  # <class 'float'>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The 'dir( )' function shows you the complete directory of what you can
# use within Python programs you create. Type and execute/run these
# simple Python program examples and study the screen output.

print(dir('text'))

print(dir(1))

print(dir(1.0))

# Type help() for interactive help, or help(object) for help about object.

print(help)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a class inheritance using only the class name 'Parent'.
# This will allow us to inherit properties from the Parent class to the
# inherited class called 'Inherit'. Any attributes in the Parent or main
# class are all passed onto the inherited class called 'Inherit'

class Person:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # fname attribute
        self.last_name=lname  # lname attribute
        self.age=age  # age attribute

# All we need to do is place the Person class name inside parentheses
# of the Inherit class act. If you don't want to use any code blocks within
# the Inherit class, simply invoke the 'pass' statement. Not shown here,
# but you can create as many inherited sub classes as you please. However,
# you must give them different names such as Inherit1 and Inherit2; you
# can name your classes any names you wish, but the first letter is always
# capitalized by Python programming standard, but you don't have to
# capitalize anything if you don't want to. Just keep the other square
# programmers happy and capitalize your class names so you don't get in
# trouble from the square boss.

class Inherit(Person):
    pass

my_variable1 = Person('John','Smith',23).first_name

my_variable2 = Inherit('Joe','Swift',23).first_name

print(my_variable1,my_variable2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use three single quote marks at the beginning and
# at the end of the print() function text.

print('''print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please.''')

# Use three double quote marks at the beginning and
# at the end of the print() function text.

print("""print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please.""")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use one variable to satisfy the print() function.

my_text = '''print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please.'''

print(my_text)

my_text = """print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please."""

print(my_text)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create two packed variables with different text paragraphs
# in them.

my_text1,my_text2 =  ("""Don't be afraid of making mistakes, they are our greatest
lessons through life. When we learn from them, they become our greatest teachers
through life and we become their greatest, lifelong student...""",

"""Science is not just for smart people from a university. Science can and often
does happen for anyone. All you really need is a bit of imagination and a whole
lot of trial and error. Anyone can achieve anything they so wish. All you have to
do is believe in yourself, while you make all kinds of mistakes along the way.
Sooner or later, what doesn't work now will eventually work out, when you least
expect it. Science and discovery is all about trial and error. So don't become
discouraged when something won't work out right. Give it some time, before you
know it, you will start to see the sparks fly...""")

# use a plus '+' sign after the double '\n\n' line break

print(my_text1,'\n\n'+my_text2)

# or use plus '+' signs before and after the double '\n\n' line break

print(my_text1+'\n\n'+my_text2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Person:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # fname attribute
        self.last_name=lname  # lname attribute
        self.age=age  # age attribute

person1 = Person('John','Smith',32)
person2 = Person('Jane','Swift',29)
person3 = Person('Joan','White',26)

print(person1.first_name,person1.last_name,person1.age)

print(person2.first_name,person2.last_name,person2.age)

print(person3.first_name,person3.last_name,person3.age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a class that has def function( ) with attributes in it.
# Use the __init__( ) initialize constructor to be able to use the
# def function's attributes: self, fname, lname and age within
# the My_first_class_act Python program example. Note: you
# can call the word 'self' any name you wish, but Python
# programmers always, always use 'self' as a standard. The
# 'self' variable calls the def function( ) attributes. Thus, the
# def function( ) calls itself back up with 'self', along with its
# class attributes, which are inside the def function( ).

class My_first_class_act:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # fname attribute
        self.last_name=lname  # lname attribute
        self.age=age  # age attribute

print(My_first_class_act('John','Smith',19).first_name)

print(My_first_class_act('John','Smith',19).last_name)

print(My_first_class_act('John','Smith',19).age)

# Let's shorten some of these bulky print( ) functions using variables.

my_variable = My_first_class_act('John','Smith',19)

print(my_variable.first_name)

print(my_variable.last_name)

print(my_variable.age)

# Now we can keep things short and sweet with just one print( ) function.

print(my_variable.first_name,my_variable.last_name,my_variable.age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create classes with return def functions() inside them and call each one up.

class Return_result_addition:
    def class_return_result_addition(num1,num2):
        return int(num1 + num2)

    addition = class_return_result_addition

print(Return_result_addition.addition(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_subtraction:
    def class_return_result_subtraction(num1,num2):
        return int(num1 - num2)

    subtraction = class_return_result_subtraction

print(Return_result_subtraction.subtraction(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_multiplication:
    def class_return_result_multiplication(num1,num2):
        return int(num1 * num2)

    multiplication = class_return_result_multiplication

print(Return_result_multiplication.multiplication(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_division:
    def class_return_result_division(num1,num2):
        return int(num1 / num2)

    division = class_return_result_division

print(Return_result_division.division(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_exponent:
    def class_return_result_exponent(num1,num2):
        return int(num1 ** num2)

    exponent = class_return_result_exponent

print(Return_result_exponent.exponent(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_power:
    def class_return_result_pow(num1,num2):
        return int(pow(num1,num2))

    power = class_return_result_pow

print(Return_result_power.power(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Child class that inherits all the other def functions of the
# upper parent class attributes.

class Inherit_return_result(
    Return_result_addition,
    Return_result_subtraction,
    Return_result_multiplication,
    Return_result_division,
    Return_result_exponent,
    Return_result_power):pass

print(Inherit_return_result.addition(8,2))  # call me up
print(Inherit_return_result.subtraction(8,2))  # call me up
print(Inherit_return_result.multiplication(8,2))  # call me up
print(Inherit_return_result.division(8,2))  # call me up
print(Inherit_return_result.exponent(8,2))  # call me up
print(Inherit_return_result.power(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's get lazy and shorten some Python code within the print() function
# with a tuple( ). Note: you can also create a list[ ] if you like, but a tuple( )
# is what we are using in our Python program example below.

class Inherit_return_result(
    Return_result_addition,
    Return_result_subtraction,
    Return_result_multiplication,
    Return_result_division,
    Return_result_exponent,
    Return_result_power):pass

class_inherit = (
              Inherit_return_result.addition,
              Inherit_return_result.subtraction,
              Inherit_return_result.multiplication,
              Inherit_return_result.division,
              Inherit_return_result.exponent,
              Inherit_return_result.power)

num1,num2 = 8,2  # variable and value packing with one equals = sign

print(class_inherit[0](num1,num2))  # call me up
print(class_inherit[1](num1,num2))  # call me up
print(class_inherit[2](num1,num2))  # call me up
print(class_inherit[3](num1,num2))  # call me up
print(class_inherit[4](num1,num2))  # call me up
print(class_inherit[5](num1,num2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's get real lazy and shorten some more Python code within the print( )
# function using a for loop to iterate through the 'class_inherit( ) tuple.

class Inherit_return_result(
    Return_result_addition,
    Return_result_subtraction,
    Return_result_multiplication,
    Return_result_division,
    Return_result_exponent,
    Return_result_power):pass

class_inherit = (
              Inherit_return_result.addition,
              Inherit_return_result.subtraction,
              Inherit_return_result.multiplication,
              Inherit_return_result.division,
              Inherit_return_result.exponent,
              Inherit_return_result.power)

num1,num2 = 8,2  # variable and value packing with one equals = sign

for i in class_inherit:print(i(num1,num2))  # call me up in a for loop

# Tip: remember to keep it DRY (Don't Repeat Yourself). Use a for loop
# to allow the use of just one print( ) function. That way, you can
# easily change your num1 and num2 values on the fly instead of
# having to change values in a bunch of repeated print( ) functions.

# Create classes with def functions() inside them and call each one up.

class Grandpa:
    def first_def_function_grandpa():
        print("I'm the first def function() within the Grampa class")
    def second_def_function_grandpa():
        print("I'm the second def function() within the Grandpa class")
    def third_def_function_grandpa():
         print("I'm the third def function() within the Grandpa class")

Grandpa.first_def_function_grandpa()  # call me up
Grandpa.second_def_function_grandpa()  # call me up
Grandpa.third_def_function_grandpa()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Grandma:
    def first_def_function_grandma():
        print("I'm the first def function() within the Grandma class")
    def second_def_function_grandma():
        print("I'm the second def function() within the Grandma class")
    def third_def_function_grandma():
        print("I'm the third def function() within the Grandma class")

Grandma.first_def_function_grandma()  # call me up
Grandma.second_def_function_grandma()  # call me up
Grandma.third_def_function_grandma()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Dad:
    def first_def_function_dad():
        print("I'm the first def function() within the Dad class")
    def second_def_function_dad():
        print("I'm the second def function() within the Dad class")
    def third_def_function_dad():
        print("I'm the third def function() within the Dad class")

Dad.first_def_function_dad()  # call me up
Dad.second_def_function_dad()  # call me up
Dad.third_def_function_dad()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Mom:
    def first_def_function_mom():
        print("I'm the first def function() within the Mom class")
    def second_def_function_mom():
        print("I'm the second def function() within the Mom class")
    def third_def_function_mom():
        print("I'm the third def function() within the Mom class")

Mom.first_def_function_mom()  # call me up
Mom.second_def_function_mom()  # call me up
Mom.third_def_function_mom()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Child class that inherits all the other def functions of the
# upper parent class attributes.

class Child(Grandpa,Grandma,Dad,Mom): # four inherited variable parameters
    pass

Child.first_def_function_grandpa()  # call me up
Child.second_def_function_grandpa()  # call me up
Child.third_def_function_grandpa()  # call me up

Child.first_def_function_grandma()  # call me up
Child.second_def_function_grandma()  # call me up
Child.third_def_function_grandma()  # call me up

Child.first_def_function_dad()  # call me up
Child.second_def_function_dad()  # call me up
Child.third_def_function_dad()  # call me up

Child.first_def_function_mom()  # call me up
Child.second_def_function_mom()  # call me up
Child.third_def_function_mom()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's shorten these Python commands down using variables.

gpf1 = Child.first_def_function_grandpa
gpf2 = Child.second_def_function_grandpa
gpf3 = Child.third_def_function_grandpa

gpf1()  # call me up
gpf2()  # call me up
gpf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
gmf1 = Child.first_def_function_grandma
gmf2 = Child.second_def_function_grandma
gmf3 = Child.third_def_function_grandma

gmf1()  # call me up
gmf2()  # call me up
gmf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
df1 = Child.first_def_function_dad
df2 = Child.second_def_function_dad
df3 = Child.third_def_function_dad

df1()  # call me up
df2()  # call me up
df3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
mf1 = Child.first_def_function_mom
mf2 = Child.second_def_function_mom
mf3 = Child.third_def_function_mom

mf1()  # call me up
mf2()  # call me up
mf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create an immutable default tuple for loop of our class def functions, using the
# hard return backslash ' \ ' instead of using parentheses ' ( ) '

class_def_functions = \
                    Child.first_def_function_grandpa,\
                    Child.second_def_function_grandpa,\
                    Child.third_def_function_grandpa

for i in class_def_functions:
    i()

class_def_functions = \
                    Child.first_def_function_grandma,\
                    Child.second_def_function_grandma,\
                    Child.third_def_function_grandma

for i in class_def_functions:
    i()

class_def_functions = \
                    Child.first_def_function_dad,\
                    Child.second_def_function_dad,\
                    Child.third_def_function_dad

for i in class_def_functions:
    i()

class_def_functions = \
                    Child.first_def_function_mom,\
                    Child.second_def_function_mom,\
                    Child.third_def_function_mom

for i in class_def_functions:
    i()

class Grandma:
    def gm():
        print("I'm the Grandma class")

class Dad:
    def d():
        print("I'm the Dad class")

class Mom:
    def m():
        print("I'm the Mom class")

class Child(Grandpa,Grandma,Dad,Mom):
     def c():
         print('I\'m the Child class act')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Class inheritance with the print() function

class Grandpa:
    gp="I'm the Grandpa class"

class Grandma:
    gm="I'm the Grandma class"

class Dad:
    d="I'm the Dad class"

class Mom:
    m="I'm the Mom class"

class Child(Grandpa,Grandma,Dad,Mom):
     c='I\'m the Child class. I inherit all the other classes above me, as well as my own.'

print(Grandpa.gp)
print(Grandma.gm)
print(Dad.d)
print(Mom.m)

print(Child.gp)
print(Child.gm)
print(Child.d)
print(Child.m)
print(Child.c,"I have a copy of my own D&A")

# Use the 'pass' statement if you don't want any code blocks
# inside your Child class act.

class Grandpa:
    gp="I'm the Grandpa class"

class Grandma:
    gm="I'm the Grandma class"

class Dad:
    d="I'm the Dad class"

class Mom:
    m="I'm the Mom class"

class Child(Grandpa,Grandma,Dad,Mom):
     pass

print(Grandpa.gp)
print(Grandma.gm)
print(Dad.d)
print(Mom.m)

print(Child.gp)
print(Child.gm)
print(Child.d)
print(Child.m)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Class inheritance with the def function()

class Grandpa:
    def gp():
        print("I'm the Grandpa class")

class Grandma:
    def gm():
        print("I'm the Grandma class")

class Dad:
    def d():
        print("I'm the Dad class")

class Mom:
    def m():
        print("I'm the Mom class")

class Child(Grandpa,Grandma,Dad,Mom):
     def c():
         print('I\'m the Child class act')

Grandpa.gp()
Grandma.gm()
Dad.d()
Mom.m()

Child.gp()
Child.gm()
Child.d()
Child.m()
Child.c()

# Use the 'pass' statement if you don't want any code blocks
# inside your Child class act.

class Grandpa:
    def gp():
        print("I'm the Grandpa class")

class Grandma:
    def gm():
        print("I'm the Grandma class")

class Dad:
    def d():
        print("I'm the Dad class")

class Mom:
    def m():
        print("I'm the Mom class")

class Child(Grandpa,Grandma,Dad,Mom):
     pass

Grandpa.gp()
Grandma.gm()
Dad.d()
Mom.m()

Child.gp()
Child.gm()
Child.d()
Child.m()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some easy ways to create math operations with return functions.

def addition(num1,num2):
    return num1 + num2 # num1 = 5, and num2 = 4

print(addition(5,4)) # These are the actual vaules

def subtraction(num1,num2):
    return num1 - num2 # num1 = 5, and num2 = 4

print(subtraction(5,4)) # These are the actual vaules

def addition(num1,num2):
    return num1 + num2 # num1 = 5, and num2 = 4

print(addition(5,4)) # These are the actual vales

def multiplication(num1,num2):
    return num1 * num2 # num1 = 5, and num2 = 4

print(multiplication(5,4)) # These are the actual vales

def division(num1,num2):
    return num1 / num2 # num1 = 5, and num2 = 4

print(division(5,4)) # These are the actual vales

def exponents(num1,num2):
    return num1 ** num2 # num1 = 5, and num2 = 4

print(exponents(5,4)) # These are the actual vales. five to the same power of four (5 * 5 * 5 * 5) = 625

# You can also use the pow() function instead of the double asterisks **

def pow_expon(num1,num2):
    return pow(num1,num2) # num1 = 5, and num2 = 4

print(pow_expon(5,4)) # These are the actual vales. five to the same power of four (5 * 5 * 5 * 5) = 625

# The sum() function can only be used with a tuple or a list. This tuple below
# is a 'default tuple'; parentheses are not used with default tuples. Any list of
# anything, text or numbers without parentheses is a tuple by default, regardless.
# Tuples are not mutable; they cannot be changed or modified in the same way
# lists[ ] can. Therefore, tuples are immutable; they cannot be changed or modified.

add_nums = 1,2,3,4,5,6,7,8,9  # default tuple
print(sum(add_nums))  # equals '45'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these Python program return function examples.

def my_first_return_value(book): # (one variable parameter)
    return "I am the actual value called 'Python'"

print(my_first_return_value(
    "placeholder argument value for the variable \
'book' that contains the value 'Python' "))


def my_second_return_value(book,python): # (two variable parameters)
    return "I am the actual value called 'Python'"

print(my_second_return_value(
    "placeholder argument value for the variable 'book'",
    "placeholder argument value for the variable 'Python'"))


def my_third_return_value(book,python,program): # (three variable parameters)
    return "I am the actual value called 'Python'"

print(my_third_return_value(
    "placeholder argument value for the variable 'book'",
    "placeholder argument value for the variable 'Python'",
    "placeholder argument value for the variable 'program'"))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn some def functions that return number values

def my_first_return_num(num): # (one variable parameter)
    return 1 # I am the actual value called 1

print(my_first_return_num("placeholder argument value for the variable 'num1'"))


def my_second_return_num(num1,num2): # (two variable parameters)
    return 2 # I am the actual values called 2

print(my_second_return_num(
    "placeholder argument value for the variable 'num1'",
    "placeholder argument value for the variable 'num2'"))


def my_third_return_num(num1,num2,num3): # (three variable parameters)
    return 3 # I am the actual values called 3

print(my_third_return_num(
    "placeholder argument value for the variable 'num1'",
    "placeholder argument value for the variable 'num2'",
    "placeholder argument value for the variable 'num3'"))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these example Python programs out. Refer to the post below of what functions and
# def functions are all about.

def my_first_funtion_variable(variable): # (one variable parameter)
    print('One parameter variable inside the def function.') # print() function

# call me up to use me!

my_first_funtion_variable('placeholder argument variable')

def my_second_function_variables(variable1,variable2): # (two variable parameters)
    print('Two parameter variables inside the def function.') # print() function

# call me up to use me!

my_second_function_variables('placeholder argument variable1','placeholder argument variable2') # three values

def my_third_function_variables(variable1,variable2,variable3): # (three variable parameters)
    print('Three parameter variables inside the def function.') # print() function

# call me up to use me!

my_third_function_variables(
    'placeholder argument variable1', # value 1
    'placeholder argument variable2', # value 2
    'placeholder argument variable3') # value 3
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
For those who are very new to Python programming or just programming
at all. If you are getting into Python, you will often hear the word called:
'def functions' short for (define function) and functions. Now here is where
I also became confused. Any type of functions you see, they are simply Python
commands that use parentheses () right after the Python command. Here
are examples of most of them, and what they do. Lastly, I will talk about def
functions and what they do.

int() is the integer function for turning number values into integer numbers
instead of default floating point numbers.

float() is the floating point function for turning integer numbers into floating
point numbers.

print() is the print function that allows you to type text inside the parentheses

input() is input function for allowing text to be used to ask for user data.

These are just some of the basic functions that always proceed parentheses at
the very end of the Python command line.

Now, let's explain what 'define functions' are. These type of functions are really
cool. You can create programming inside the def function block, and then when
you call up the def function's name, you simply type the name of whatever you
want to call the def function. Note: you cannot rename any functions that are
the kind above this text paragraph. With def functions, you can create any name
you wish. Here are some examples, using easy Python commands for the new
people, such was myself. And in a way, I'm still a newbie because I always find
something else in Python through their updates on the programming of it.
'''
def my_first_function():
    print("I'm the def function you created. I executed/ran when I was called.") # print() function

# Let's call up the def function, my_first_function() without the 'def' part.

my_first_function()

def my_second_function():
    print("I'm the other def funciton you created.") # print() function
    print('You can create yoru own code inside the def functions.')  # print() function

my_second_function()

def my_third_function():
    for i in range(5):
        print("def functions can also play for loops and while loops inside them.") # print() function
        print('You can create your own Python code inside def functions.')  # print() function

my_third_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TIP: After using the colon : in a def function, just press your Enter Key on your keyboard
# and the spacebar will be automatically indented for you. Keep all the indents the same.
# On the next press of he Enter key, if you have other commands you want inside your
# def functions, you just keep pressing Enter and the indented new line will let you type
# your code without the worry of how much you need to have proper indentation within
# your Python code. For loops and while loops also use colons : Colons always indicate
# that your code will be indented every time you press the Enter key. So, instead let the
# curser do all the indentation work for you.

def return_logical_num_value(num):
    return f'{num+2:b}'

num = return_logical_num_value(8)

print(num)  # addition: 8 + 2 = 10
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num-2:b}'

num = return_logical_num_value(8)

print(num)  # subtraction: 8 - 2 = 6
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num*2:b}'

num = return_logical_num_value(8)

print(num)  # multiplication: 8 * 2 = 16
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num//2:b}'

num = return_logical_num_value(8)

print(num)  # division: 8 / 2 = 4
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num**2:b}'

num = return_logical_num_value(8)

print(num)  # **exponent: 8 ** 2 = 64
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num//2:b}'

num = return_logical_num_value(8)

print(int(num))  # division: 8 / 2 = 4

# Use the floating point float() functions.

def return_logical_num_value(num):
    return f'{num//2:b}'

num = return_logical_num_value(8)

print(float(num))  # division: 8 / 2 = 4.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return f'{num1+num2:b}',f'{num1-num2:b}'

num = return_logical_nums_tuple_values(10,5)

print(num[0])
print(num[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return f'{num1*num2:b}',f'{num1//num2:b}'

num = return_logical_nums_tuple_values(10,5)

print(num[0])
print(num[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return\
             (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(num[0],num[1],num[2],num[3],num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the integer int() functions.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(int(num[0]))
print(int(num[1]))
print(int(num[2]))
print(int(num[3]))
print(int(num[4]))

# Use the floating point float() functions.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(float(num[0]))
print(float(num[1]))
print(float(num[2]))
print(float(num[3]))
print(float(num[4]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Print everything on one line, separated with commas between argument variables.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(int(num[0]),int(num[1]),int(num[2]),int(num[3]),int(num[4]))

print(float(num[0]),float(num[1]),float(num[2]),float(num[3]),float(num[4]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a for loop, using the variable name 'num' as part of the for loop
# to count through the index values [n] in the 'num' variable indexes.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

for i in num:
    print(i)

# or:

for i in num:
    print(int(i))

# or:

for i in num:
    print(float(i))

# or:

for i in num:
    print(int(i))
    print(float(i))

# or:

for i in num:
    print(int(i),float(i))

# You can leave out the int() and float() functions if you like; a floating point
# number by default is what the value will be in some cases.

for i in num:
    print(i,i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use these dunder methods to calculate numbers, such as integers and floats.

print(int.__add__(8,2))  # equals 10

print(int.__sub__(8,2))  # equals 6

print(int.__mul__(8,2))  # equals 16

print(int.__floordiv__(8,2))  # equals 4

print(int.__pow__(8,2))  # equals 64


print(float.__add__(8.0,2.0))  # equals 10.0

print(float.__sub__(8.0,2.0))  # equals 6.0

print(float.__mul__(8.0,2.0))  # equals 16.0

print(float.__floordiv__(8.0,2.0))  # equals 4.0

print(float.__pow__(8.0,2.0))  # equals 64.0

# Use the 'dir( ) function with nothing inside the parentheses

print(dir())

# screen output:
'''
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__']
'''
# Use the 'dir( ) function with a number inside the parentheses

print(dir(1))

# screen output:
'''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__',
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__',
'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
'__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
'__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
'__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
'__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
'__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
'imag', 'numerator', 'real', 'to_bytes']
'''
# Use the __str__ dunder method for text strings.

print(str.__str__('text string'))

# Use the __repr__ dunder method to represent integer and float strings.

print(int.__repr__(8+2))

print(float.__repr__(8.0+2.0))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create a single class.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

print(Single_class('argument1','argument2','argument3').arg1)

# This is a skeletal scheme of how to create a single class without
# attributes but only a def function( ) inside it.

class Single_class:
    def inner_function():
        print('Add me to the Single class.')

Single_class.inner_function()

# This is a skeletal scheme of how to create a single class with
# attributes and a def function( ) inside it. Note: you cannot call
# the def function, 'inner_function( )' at the same time you call
# the 'Single_class' attributes. Instead, you have to call each
# one separately.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute
    def inner_function():
        print('Add me to the Single class.')

print(Single_class('argument1','argument2','argument3').arg1)

Single_class.inner_function()

# It does not matter the order of how you place the inner def
# function( ) and the Single_class attributes. However, you still
# cannot call both at the same time. The example above is less
# confusing looking than the example shown here.

class Single_class:
    def inner_function():
        print('Add me to the Single class.')
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

print(Single_class('argument1','argument2','argument3').arg1)

Single_class.inner_function()

# Let's create a def function with a return statement inside the
# Single_class act. Once again, you cannot call both the Single_class
# attributes and the inner def function( ) at the same time. However,
# in this example below, it does matter about the order you place
# the single class attributes in. Once you create a return function,
# the cursor will automatically jump right out of the indented
# class Python code when the 'Enter key' is pressed.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute
    def inner_function(self):
        return 'Return me to the Single class.'

print(Single_class('argument1','argument2','argument3').arg1)

print(Single_class.inner_function('argument placeholder value'))

# Let's create a 'Super_class' and invoke the 'super( ) function so we
# don't have to repeat any attributes with in our super_function_class.

class Super_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

# The super( ) function reduces redundant Python code, so you can keep
# Python code nice and 'DRY!' ( "Don't Repeat Yourself!" )

class Super_function_class(Super_class):
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

print(Super_function_class('argument1','argument2','argument3').arg1)

# Let's create the same 'Super_class' act, but let's now expand/add to the
# 'Super_function_class' act with attributes of its own, while not having
# to repeat the attributes from the 'Super_class' act.

class Super_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Super_function_class(Super_class):
    def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6):
        self.arg4=arg4  # attribute
        self.arg5=arg5  # attribute
        self.arg6=arg6  # attribute
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method        

print(Super_function_class(
    'argument1','argument2','argument3','argument4','argument5','argument6').arg5)

# It does not matter the order of how you place the Super_function_class
# attributes. You can place the super( ) function before the Super_function_class
# attributes. However, the example above is less confusing looking than the
# example shown here.

class Super_function_class(Super_class):
    def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method
        self.arg4=arg4  # attribute
        self.arg5=arg5  # attribute
        self.arg6=arg6  # attribute
             
print(Super_function_class(
    'argument1','argument2','argument3','argument4','argument5','argument6').arg5)

# Lastly, if we create a class with just a simple 'print( )' function, it won't really do
# anything, but print out text inside the print( ) function as if we didn't even create
# a class at all; there is simply nothing to call. So the class is practically ignored;
# the print( ) function executes/runs anyway. So avoid stuff like this if you want
# your Python classes to work properly. Classes love 'ATTRIBUTES' and proper
# classes need attributes to work correctly, so we call them when we want to
# call them. Not when they want to be called. Remember! We're the Boss, not
# the classes. The class attributes make sure that they obey the Boss's orders.
# Not the other way around.

class Single_class:
    print("I don't really do anything, but show printed text.")

# By now you should have a stern, but general idea of how Python classes work.
# I hope this extensive lesson on Python classes helped. Until next time. Peace!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create a single class, using variables.
# Next, we will get into for loops, using a tuple( ) for our class argument
# values. Tuples are immutable; they cannot be changed or modified.
# Tuple indexes[ ] always start at zero, not one. Let's create a tuple( ) that
# will hold all our class attribute argument values

class_arguments_tuple = ('argument1','argument2','argument3')

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

# If you don't have enough room to see the whole print( ) function text and or
# variables on one line, you can do the following.

print(
    Single_class(
    class_arguments_tuple[0],  # index[0]
    class_arguments_tuple[1],  # index[1]
    class_arguments_tuple[2]   # index[2]
    ).arg1)

# Here is the very same print( ) function that's all on one line. When you type this
# out, you won't be able to see all the Python code inside the print( ) function
# without having to scroll your cursor all the way to the end, until you can see the
# text and or variables at the end of the entire print( ) function. So to keep things
# like this from occurring, we will always use the above example for our print( )
# functions

print(Single_class(class_arguments_tuple[0],class_arguments_tuple[1],class_arguments_tuple[2]).arg1)

# Let's create a for loop that will loop through all the class argument variables
# and show all the class argument values on the screen with only one print( )
# function. Again, we will use a tuple, and then use the tuple's variable name
# to count the actual for loop values. We can also do this all with one, single
# line of Python code. We can place the print( ) function right after the for loop's
# colon : on the same line as the for loop. However, this will only work if you
# don't have any other code blocks within the for loop. This will not work if you
# have other indented Python commands within the for loop.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

tuple_loop = (
    Single_class('argument1','argument2','argument3').arg1,
    Single_class('argument1','argument2','argument3').arg2,
    Single_class('argument1','argument2','argument3').arg3)

# See how we drastically reduced our Python code, using a tuple( )?
# Also, we used the tuple's variable name 'tuple_loop' to do the counting
# of the tuple_loop values for us automatically without the worry of how
# high we have to make the for loop count.

for i in tuple_loop:print(i)

# Now, let's create a list[ ] and do exactly the same as we did before with
# with our tuple( ). Lists are mutable, meaning they can be changed or
# modified, whereas tuples cannot be changed or modified. In most
# cases, it's a good idea to use a list[ ] if you want your list of values to
# change over time throughout your Python program.

class_arguments_list = ['argument1','argument2','argument3']

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

# If you don't have enough room to see the whole print( ) function text and or
# variables on one line, you can do the following.

print(
    Single_class(
    class_arguments_list[0],  # index[0]
    class_arguments_list[1],  # index[1]
    class_arguments_list[2]   # index[2]
    ).arg1)

# Let's create a for loop that will loop through all the class argument variables
# and show all the class argument values on the screen with only one print( )
# function. Again, we will use a list, and then use the list's variable name
# to count the actual for loop values. We can also do this all with one, single
# line of Python code. We can place the print( ) function right after the for loop's
# colon : on the same line as the for loop. However, this will only work if you
# don't have any other code blocks within the for loop. This will not work if you
# have other indented Python commands within the for loop.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

list_loop = [
    Single_class('argument1','argument2','argument3').arg1,
    Single_class('argument1','argument2','argument3').arg2,
    Single_class('argument1','argument2','argument3').arg3]

# See how we drastically reduced our Python code, using a list[ ]?
# Also, we used the list's variable name 'list_loop' to do the counting
# of the list_loop values for us automatically without the worry of how
# high we have to make the for loop count.

for i in list_loop:print(i)

# Now, let's create a dictionary{ } and do exactly the same as we did
# before with our tuple( ) and our list[ ] Python program examples.
# We are about to get our feet just a wee bit more wet this time.

class_arguments_dictionary = {1:'argument1',2:'argument2',3:'argument3'}

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

# If you don't have enough room to see the whole print( ) function text and or
# variables on one line, you can do the following.

print(
    Single_class(
    class_arguments_dictionary.get(1),  # dictionary key 1
    class_arguments_dictionary.get(2),  # dictionary key 2
    class_arguments_dictionary.get(3)   # dictionary key 3
    ).arg1)

# Let's create a for loop that will loop through all the class argument variables
# and show all the class argument values on the screen with only one print( )
# function. Again, we will use a dictionary. However, we need to use the 'range( )
# function this time. The variable ' i ' won't work within the .get() function part,
# so we have to use the variable 'dictionary_loop.get(i+1)'. Why the variable ' i '
# does not work for the variable dictionary_loop is a complete mystery? However,
# this will only work if you don't have any other code blocks within the for loop.
# This will not work if you have other indented Python commands within the for
# loop.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

dictionary_loop = (
    {1:Single_class('argument1','argument2','argument3').arg1,
     2:Single_class('argument1','argument2','argument3').arg2,
     3:Single_class('argument1','argument2','argument3').arg3})

# See how we drastically reduced our Python code, using a dictionary{ }
# with a for loop?

for i in range(3):print(dictionary_loop.get(i+1))

# I hope this helped you understand how to create classes with for loops
# using one, single 'print( )' function, which drastically reduces redundant
# Python code.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create classes with sub classes,
# along with a child class act. Keep this class scheme as something
# to easily memorize, which will help you when you need to refer to
# it. Note: you can create just one class if you like as well. This class
# scheme shows you the complete class sets, should you wish to use
# them all. I hope this will help those who are new to creating classes,
# such as myself am; I'm still pretty new to adapting to creating classes.
# You can also create as many sub classes as you please. Just make
# sure you give the child class act all the sub classes you create, along
# with the Main class, which comes first in your child class inheritance
# variables. Other than this, go Crazy and create your own class acts.

class Main_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class1:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class2:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class3:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class4:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class All_classes(
    Main_class,Sub_class1,
    Sub_class2,Sub_class3,
    Sub_class4): # Multi Inheritance
    
    def __init__(self,arg1,arg2,arg3):
        Main_class.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class1.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class2.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class3.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class4.__init__(self,arg1,arg2,arg3)  # inheritance

print(Main_class('argument1','argument2','argument3').arg1)
print(Main_class('argument1','argument2','argument3').arg2)
print(Main_class('argument1','argument2','argument3').arg3)

print(Sub_class1('argument1','argument2','argument3').arg1)
print(Sub_class1('argument1','argument2','argument3').arg2)
print(Sub_class1('argument1','argument2','argument3').arg3)

print(Sub_class2('argument1','argument2','argument3').arg1)
print(Sub_class2('argument1','argument2','argument3').arg2)
print(Sub_class2('argument1','argument2','argument3').arg3)

print(Sub_class3('argument1','argument2','argument3').arg1)
print(Sub_class3('argument1','argument2','argument3').arg2)
print(Sub_class3('argument1','argument2','argument3').arg3)

print(Sub_class4('argument1','argument2','argument3').arg1)
print(Sub_class4('argument1','argument2','argument3').arg2)
print(Sub_class4('argument1','argument2','argument3').arg3)

print(All_classes('argument1','argument2','argument3').arg1)
print(All_classes('argument1','argument2','argument3').arg2)
print(All_classes('argument1','argument2','argument3').arg3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create classes with sub classes,
# along with a child class act. Keep this class scheme as something
# to easily memorize, which will help you when you need to refer to
# it. Note: you can create just one class if you like as well. This class
# scheme shows you the complete class sets, should you wish to use
# them all. I hope this will help those who are new to creating classes,
# such as myself am; I'm still pretty new to adapting to creating classes.
# You can also create as many sub classes as you please.

# The super( ) function reduces redundant Python code, so you can keep
# Python code nice and 'DRY!' ( "Don't Repeat Yourself!" ) 

class Main_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class1(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class Sub_class2(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class Sub_class3(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class Sub_class4(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class All_classes(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

print(Sub_class1('argument1','argument2','argument3').arg1)
print(Sub_class1('argument1','argument2','argument3').arg2)
print(Sub_class1('argument1','argument2','argument3').arg3)

print(Sub_class2('argument1','argument2','argument3').arg1)
print(Sub_class2('argument1','argument2','argument3').arg2)
print(Sub_class2('argument1','argument2','argument3').arg3)

print(Sub_class3('argument1','argument2','argument3').arg1)
print(Sub_class3('argument1','argument2','argument3').arg2)
print(Sub_class3('argument1','argument2','argument3').arg3)

print(Sub_class4('argument1','argument2','argument3').arg1)
print(Sub_class4('argument1','argument2','argument3').arg2)
print(Sub_class4('argument1','argument2','argument3').arg3)

print(All_classes('argument1','argument2','argument3').arg1)
print(All_classes('argument1','argument2','argument3').arg2)
print(All_classes('argument1','argument2','argument3').arg3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a simple way to learn multi class inheritance. The first example will
# demonstrate this without the use of the super( ) function, and the next example
# will demonstrate the use of the super( ) function with class inheritance.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Child(Mom,Dad): # Multi Inheritance
    def __init__(self,name,age):
        Mom.__init__(self,name,age)  # inheritance
        Dad.__init__(self,name,age)  # inheritance

print(Mom('Jan',30).name)
print(Dad('John',35).age)

print(Child('Jan',30).name)
print(Child('John',35).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unlike the class example above, the super( ) function is very useful in that you
# don't have to repeat your class attributes in the 'Dad' class and the 'Child' class act.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad(Mom):  # class inheritance variable
     def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

class Child(Mom):  # class inheritance variable
    def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

print(Mom('Jan',30).name)
print(Dad('John',35).age)

print(Child('Jan',30).name)
print(Child('Joh',35).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a simple way to learn multi class inheritance. The first example will
# demonstrate this without the use of the super( ) function, and the next example
# will demonstrate the use of the super( ) function with class inheritance.
# We will use variables this time for the print( ) functions.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Child(Mom,Dad): # Multi Inheritance
    def __init__(self,name,age):
        Mom.__init__(self,name,age)  # inheritance
        Dad.__init__(self,name,age)  # inheritance

variable1 = Mom('Jan',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jan',30).name
variable4 = Child('John',35).age

print(variable1)
print(variable2)
print(variable3)
print(variable4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unlike the class example above, the super( ) function is very useful in that you
# don't have to repeat your class attributes in the 'Dad' class and the 'Child' class act.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad(Mom):  # class inheritance variable
     def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

class Child(Mom):  # class inheritance variable
    def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

variable1 = Mom('Jan',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jan',30).name
variable4 = Child('John',35).age

print(variable1)
print(variable2)
print(variable3)
print(variable4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the simplest way I could explain what the super( ) function does.
# Take a look at the two examples and you will see how the super( ) function
# makes it so you don't have to repeat all the class attributes in the Dad class

# Without the super( ) function, you would have to repeat your code.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28).first_name)

# This is much better as not to repeat your code using the super( ) function.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad(Mom):  # inheritance variable 'Mom'

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)  # no repeated attributes

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28).first_name)

print(Mom('Jane','Smith',23).last_name)

print(Dad('John','Smith',28).last_name)

print(Mom('Jane','Smith',23).age)

print(Dad('John','Smith',28).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# As we did before, you can also add brand new attributes to the
# Dad class.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad(Mom):  # inheritance variable 'Mom'

    def __init__(self,fname,lname,age,fishing):
        super().__init__(fname,lname,age)
        self.fishing=fishing  # one brand new attribute

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28,'Trout').fishing)

print(Mom('Jane','Smith',23).last_name)

print(Dad('John','Smith',28,'Bass').fishing)

print(Mom('Jane','Smith',23).age)

print(Dad('John','Smith',28,'Pike').fishing)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a multiple inheritance class, called 'Child'. However,
# we cannot use the super( ) function here. In the Child class we
# only need to call the def __init__ parameters, without repeating
# our code. Although, we do have to repeat the Mom and Dad class
# code as shown below.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad:  # inheritance variable 'Mom'

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

# Make the Child class have one attribute of its own. However,
# the new Child class attribute 'playing' will only work with
# the Child class. If you try to make the attribute 'playing' work
# in the Mom and Dad class, it will not work. The Child class
# has its own attributes that will only work within that class act.

class Child(Mom,Dad):
    def __init__(self,fname,lname,age,play):
        Mom.__init__(self,fname,lname,age)
        Dad.__init__(self,fname,lname,age)
        self.playing=play  # one brand new attribute

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28).first_name)

print(Child('Tommy','Smith',3,'Toy Cars').first_name)

print(Child('Tommy','Smith',3,'Toy Cars').playing)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these class acts Python program examples with return statements.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute
    def mom(self):
        return "I'm still your Mom Son!"

class Dad:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute
    def dad(self):
        return "I'm still your Dad Son!"

class Child(Mom,Dad): # Multi Inheritance
    def __init__(self,name,age):
        Mom.__init__(self,name,age)  # inheritance
        Dad.__init__(self,name,age)  # inheritance
    def child(self):
        return "I'm still your Child, Mom and Dad!"

variable1 = Mom('Jane',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jane',30).name
variable4 = Child('John',35).age

variable5 = Mom('Jane',30).mom()
variable6 = Dad('John',35).dad()
variable7 = Child('Jane',30).mom()
variable8 = Child('John',35).dad()
variable9 = Child('George',10).child()

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable6)
print(variable7)
print(variable8)
print(variable9)

# You can also use these, via the return statements.

print(Mom.mom('placeholder'))  # return argument placeholder value
print(Dad.dad('placeholder'))  # return argument placeholder value
print(Child.mom('placeholder'))  # return argument placeholder value
print(Child.dad('placeholder'))  # return argument placeholder value
print(Child.child('placeholder'))  # return argument placeholder value

# Let's use variables to shrink down our print( ) functions.

variable1 = Mom.mom('placeholder')  # return argument placeholder value
variable2 = Dad.dad('placeholder')  # return argument placeholder value
variable3 = Child.mom('placeholder')  # return argument placeholder value
variable4 = Child.dad('placeholder')  # return argument placeholder value
variable5 = Child.child('placeholder')  # return argument placeholder value

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these class acts Python program examples with return statements.
# and the super( ) function. Note: the Child class has to call up the Dad class
# when using return statements and the super( ) function. The Child class
# calls up the Dad class and the Dad class calls up the Mom class. This allows
# the Child class to have full access to the Mom and Dad class; the Child calls
# the Dad class and the Dad class calls the Mom class.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute
    def mom(self):
        return "I'm still your Mom Son!"

class Dad(Mom):  # call the Mom class inheritance variable
     def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method
     def dad(self):
         return "I'm still your Dad Son!"

class Child(Dad):  # call the Dad class inheritance variable
    def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method
    def child(self):
        return "I'm still your Child, Mom and Dad!"

# Let's use variables to shrink down our print( ) functions.

variable1 = Mom('Jan',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jan',30).name
variable4 = Child('John',35).age

print(variable1)
print(variable2)
print(variable3)
print(variable4)

# Let's use variables to shrink down our print( ) functions.

variable1 = Mom('Jane',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jane',30).name
variable4 = Child('John',35).age

variable5 = Mom('Jane',30).mom()
variable6 = Dad('John',35).dad()
variable7 = Child('Jane',30).mom()
variable8 = Child('John',35).dad()
variable9 = Child('George',10).child()

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable6)
print(variable7)
print(variable8)
print(variable9)

# You can also use these, via the return statements.
# Let's use variables to shrink down our print( ) functions.

variable1 = Mom.mom('placeholder')  # return argument placeholder value
variable2 = Dad.dad('placeholder')  # return argument placeholder value
variable3 = Child.mom('placeholder')  # return argument placeholder value
variable4 = Child.dad('placeholder')  # return argument placeholder value
variable5 = Child.child('placeholder')  # return argument placeholder value

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some argument def function( ) examples.

def arg_funct(fname,lname,age):
    print(fname,lname,age)

arg_funct('John','Smith',30)

# return one value with the return statement.

def arg_funct(fname,lname,age):
    return fname  # return each argument variable one at a time

print(arg_funct('John','Smith',30))

def arg_funct(fname,lname,age):
    return lname  # return each argument variable one at a time

print(arg_funct('John','Smith',30))

def arg_funct(fname,lname,age):
    return age  # return each argument variable one at a time

print(arg_funct('John','Smith',30))

# create a variable 'x' to return one value with the return statement.

def arg_funct(fname,lname,age):
    return fname  # return each argument variable one at a time as shown above

x = arg_funct('John','Smith',30)

print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with argument def function( ) examples.

class Function:
    def arg_funct(fname,lname,age):
        print(fname,lname,age)

Function.arg_funct('John','Smith',30)

# return one value with the return statement.

class Function:
    def arg_funct(fname,lname,age):
        return fname  # return each argument variable one at a time

print(Function.arg_funct('John','Smith',30))

class Function:
    def arg_funct(fname,lname,age):
        return lname  # return each argument variable one at a time

print(Function.arg_funct('John','Smith',30))

class Function:
    def arg_funct(fname,lname,age):
        return age  # return each argument variable one at a time

print(Function.arg_funct('John','Smith',30))

# create a variable 'x' to return one value with the return statement.

class Function:
    def arg_funct(fname,lname,age):
        return fname  # return each argument variable one at a time as shown above

x = Function.arg_funct('John','Smith',30)

print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with attributes and return argument
# def functions( ), along with a 'child' class act Python program example.

class Return_class_function1:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct1(fname,lname,age):
        return fname  # return each argument variable one at a time

class Return_class_function2:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct2(fname,lname,age):
        return lname  # return each argument variable one at a time

class Return_class_function3:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct3(fname,lname,age):
        return age  # return each argument variable one at a time

class Return_all_class_functions(
    Return_class_function1,
    Return_class_function2,
    Return_class_function3):

    def __init__(self,fname,lname,age):
        Return_class_function1.__init__(first_name,last_name,age)  # inheritance
        Return_class_function2.__init__(first_name,last_name,age)  # inheritance
        Return_class_function3.__init__(first_name,last_name,age)  # inheritance

# print out each individual class by themselves

print(Return_class_function1.arg_funct1('Jane','Smith',30))
print(Return_class_function2.arg_funct2('John','Smith',35))
print(Return_class_function3.arg_funct3('Ron','Smith',10))

# print out the Return_all_class_functions child class acts

print(Return_all_class_functions.arg_funct1('Jane','Smith',30))
print(Return_all_class_functions.arg_funct2('John','Smith',35))
print(Return_all_class_functions.arg_funct3('Ron','Smith',10))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with attributes and return argument
# def functions( ), along with a 'child' class act Python program example.

class Return_class_function1:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct1(fname,lname,age):
        return fname  # return each argument variable one at a time

class Return_class_function2:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct2(fname,lname,age):
        return lname  # return each argument variable one at a time

class Return_class_function3:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct3(fname,lname,age):
        return age  # return each argument variable one at a time

class Return_all_class_functions(
    Return_class_function1,
    Return_class_function2,
    Return_class_function3):

    def __init__(self,fname,lname,age):
        Return_class_function1.__init__(first_name,last_name,age)  # inheritance
        Return_class_function2.__init__(first_name,last_name,age)  # inheritance
        Return_class_function3.__init__(first_name,last_name,age)  # inheritance

# Let's now create three tuples called fnames, lnames and ages to use within
# 'zip( )' functions. Here are three separate zip( ) function examples for the three
# individual classes.

fnames = 'Jane','John','Ron'
lnames = 'Smith','Smith','Smith'
ages = 30,35,10

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function1.arg_funct1(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function2.arg_funct2(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function3.arg_funct3(index1,index2,index3))

# Here are three separite zip( ) function examples for the three child class acts.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct1(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct2(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct3(index1,index2,index3))

# Let's shrink down these Python program examples, using just one zip( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function1.arg_funct1(index1,index2,index3))
    print(Return_class_function2.arg_funct2(index1,index2,index3))
    print(Return_class_function3.arg_funct3(index1,index2,index3))

# Let's shrink down these Python program examples, using just one zip( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct1(index1,index2,index3))
    print(Return_all_class_functions.arg_funct2(index1,index2,index3))
    print(Return_all_class_functions.arg_funct3(index1,index2,index3))

# Let's shrink down this Python program even more, with just one print( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(
        Return_class_function1.arg_funct1(index1,index2,index3),
        Return_class_function2.arg_funct2(index1,index2,index3),
        Return_class_function3.arg_funct3(index1,index2,index3))

# Let's shrink down this Python program even more, with just one print( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(
        Return_all_class_functions.arg_funct1(index1,index2,index3),
        Return_all_class_functions.arg_funct2(index1,index2,index3),
        Return_all_class_functions.arg_funct3(index1,index2,index3))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with attributes and return argument
# def functions( ), along with a 'child' class act Python program example.

class Return_class_function1:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct1(fname,lname,age):
        return fname  # return each argument variable one at a time

class Return_class_function2:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct2(fname,lname,age):
        return lname  # return each argument variable one at a time

class Return_class_function3:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct3(fname,lname,age):
        return age  # return each argument variable one at a time

class Return_all_class_functions(
    Return_class_function1,
    Return_class_function2,
    Return_class_function3):

    def __init__(self,fname,lname,age):
        Return_class_function1.__init__(first_name,last_name,age)  # inheritance
        Return_class_function2.__init__(first_name,last_name,age)  # inheritance
        Return_class_function3.__init__(first_name,last_name,age)  # inheritance

# Let's now create three tuples called fnames, lnames and ages to use within
# 'enumerate( )' functions. Here are three separate enumerate( ) function examples
# for the three individual classes.

fnames = 'Jane','John','Ron'
lnames = 'Smith','Smith','Smith'
ages = 30,35,10

for index,fname_lname_age in enumerate(fnames):
    print(Return_class_function1.arg_funct1(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(lnames):
    print(Return_class_function2.arg_funct2(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(ages):
    print(Return_class_function3.arg_funct3(
        fname_lname_age,fname_lname_age,fname_lname_age))

# Let's use the child class acts to do as we did in the examples above.

for index,fname_lname_age in enumerate(fnames):
    print(Return_class_function1.arg_funct1(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(lnames):
    print(Return_class_function2.arg_funct2(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(ages):
    print(Return_class_function3.arg_funct3(
        fname_lname_age,fname_lname_age,fname_lname_age))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can use Emojis in Python. I just discovered this on my own, just to see if
# it would work. And it does work! WOW!! Use YouTube Emojis in your very own
# Python program examples. Use them for creating logical programs that if
# the user doesn't press the right key, you can program the Emojis to make
# an angry face. If the user does what he wants, them make the Emojis make
# a happy face and so on. Who knows? I just might create us a Python program
# to do such. Copy and then paste this program into your Python App and
# execute/run it and see what happens. Double click the file to open it so you
# can see the colour of the Emojis face. Save the file as Emojis and run it.

print('I am almost a complete Walking Human Computer Science \
Research Laboratory Machine on Two Legs. 😁')

input('Press Enter to exit the program')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are 90 emojis you can use within your Python programs.
# Please note: these were not easy to create. The emojis can't
# be copied into a list as easy as ordinary Python lists. If
# you add any of your own, make sure you don't make any mistakes.
# Python's undo button and or ctrl+z does not work; you have
# to keep undoing the mistake or the ones you don't want in the
# list, and emojis you add to the Python list. As I said, these
# weren't easy to create at all. I think 90 emojis is more than
# a great start. Don't you?

# Save the file as Emojis and then double click the Python file's
# icon to see the emojis in colour as shown in the Python program
# example. Please note: These emojis in the actual Python idle are
# green and outlined, not coloured as shown on this YouTube
# community page.

emojis_list = [
    '😀','😄','😁','😆','😅','🤣','😂','🙂','🙃','😉',
    '😊','😇','🥰','😍','🤩','😘','😗','😚','🥲','😋',
    '😛','😜','🤪','😝','🤑','🤗','🤭','🤫','🤔','🤐',
    '🤨','😐','😑','😶','😶‍🌫','😏','😒','🙄','😬','😮‍💨',
    '🤥','😌','😔','😪','🤤','😴','😷','🤒','🤕','🤢',
    '🤧','🥵','🥶','🥴','😵','😵‍💫','🤯','🤠','🥳','🥸',
    '😎','🤓','🧐','😕','😟','🙁','😮','😯','😲','😳',
    '🥺','😦','😧','😨','😰','😥','😢','😭','😱','😖',
    '😣','😞','😓','😩','😫','🥱','😤','😡','😠','🤬']

print(emojis_list[2])

input('Press Enter to exit the program.')

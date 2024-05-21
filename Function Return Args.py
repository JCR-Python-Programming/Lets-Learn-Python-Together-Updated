# Created by Joseph C. Richardson, GitHub.com

# These Python program examples shows how to use *args with return functions.
# Using *args can by quite handy and useful. Especially if you don't know how
# many arguments you might need inside your define function parameters. You
# can also notice how you can create two different ways to print() the placeholder
# values, which must satisfy the function's argument variables.

def return_function(Python_book):
    return 'Python',"Programmer's",'Glossary','Bible'

rf = return_function

a = 'placeholder'

print(rf(a)[0])

# or this:

print(rf(a)[0],rf(a)[1],rf(a)[2],rf(a)[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(Python_book0,Python_book1,Python_book2,Python_book3):
    return 'Python',"Programmer's",'Glossary','Bible'

rf = return_function

a = 'placeholder'

print(rf(a,a,a,a)[0])

# or this:

print(rf(a,a,a,a)[0],rf(a,a,a,a)[1],rf(a,a,a,a)[2],rf(a,a,a,a)[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(*Python_book):
    return 'Python',"Programmer's",'Glossary','Bible'

rf = return_function

a = 'placeholder'

print(rf(a)[0])

# or this:

print(rf(a)[0],rf(a)[1],rf(a)[2],rf(a)[3])

# Global Variables Python program examples

# Created and written by Joseph C. Richardson, GitHub.com

# What are 'global variables'? Global variables are used within def functions()
# when you want to call a variable outside the actual def function(), you need
# the prefix 'global' to be able to call a variable outside the actual def function()
# itself. For example here is what calling a variable, using the prefix 'global' does.

def global_variable():
    global a
    a = 'global variables work outside their functions()'

global_variable()

print(a)

# If you try to call a variable outside a def function() with no 'global' prefix attached to it,
# you will get an error such as this:

def non_global_variable():
    a = 'non global variables won\'t work outside their functions()'

non_global_variable()

print(a)

#    Traceback (most recent call last):
#      File "C:\Users\mogie54321\Desktop\EXP Python.py", line 16, in <module>
#        print(a)
#    NameError: name 'a' is not defined

# You can, however do this if you don't want to invoke the 'global' prefix. So
# instead, we can do this:

c = 'outside variables work outside their def functions()'
def non_global_variable():
    print(c)    

non_global_variable()

# Simply create a variable outside the def function and then call it in from outside it.
# Let's do more global variables to get the hang of things with a group of them.

def global_variables():
    global a
    global b
    global c
    a = 'global variable (a) works outside its def functions()'
    b = 'global variable (b) works outside its def functions()'
    c = 'global variable (c) works outside its def functions()'

global_variables()

print(a)

# Here is one thing you should avoid doing. If you call an outside variable with the
# same name as this example below shows, you won't get the desired output you want.
# If you want outside variables outside of global variables, you must give them different
# names so they can know who is who.

a = 'oops! This outside variable (a) was overwritten by the global variable (a).'
def global_variables():
    global a
    global b
    global c
    a = 'global variable (a) works outside its def functions()'
    b = 'global variable (b) works outside its def functions()'
    c = 'global variable (c) works outside its def functions()'

global_variables()

print(a)

# Now that we used a different name for the outside variable, the global variables and the
# outside variable will know who is who, when being called upon. Note: you can also use
# an uppercase 'A' for the outside variable; computers are case sensitive: 'a' and 'A' are not
# the same to a computer. Therefore, the computer treats the variables as totally different
# names. So please keep this in mind at all times.

abc = 'Now I know which one of us variables are being called.'
def global_variables():
    global a
    global b
    global c
    a = 'global variable (a) works outside its def functions()'
    b = 'global variable (b) works outside its def functions()'
    c = 'global variable (c) works outside its def functions()'

global_variables()

print(abc)
print(a)

# The computer thinks this is a totally different variable name altogether.

A = 'I still know which one of us variables are being called.'
def global_variables():
    global a
    global b
    global c
    a = 'global variable (a) works outside its def functions()'
    b = 'global variable (b) works outside its def functions()'
    c = 'global variable (c) works outside its def functions()'

global_variables()

print(A)
print(a)

# Let's pack global variables with just one 'global' prefix to use them outside the def function().

def global_variables():
    global a,b,c
    a = 'pack global variable (a) works outside its def functions()'
    b = 'pack global variable (b) works outside its def functions()'
    c = 'pack global variable (c) works outside its def functions()'

global_variables()

print(b)

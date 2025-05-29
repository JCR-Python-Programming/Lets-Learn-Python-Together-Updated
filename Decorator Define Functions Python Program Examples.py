# Decorator Define Functions Python Program Examples:

# Created by JCR, GitHub.com

# Decorator define functions extend the base define function,
# without modifying or changing the base define function.
# Decorators make base define functions more powerful; they
# can be called into the base define function, when you want
# to extend the capabilities of the base define function, via
# invoking the @ symbol along with the name of the decorator
# define function's name, such as @add_define_function_one,
# for example.

# Create as many decorator define functions as you wish.

# Decorator define functions without *args and **kwargs

def add_define_function_one(funct):
  def inner_define_function():
    print('Add a decorator define function to the base define function.')
    funct()
  return inner_define_function

def add_define_function_two(funct):
  def inner_define_function():
    print('Add another decorator define function to the base define function.')
    funct()
  return inner_define_function

def add_define_function_three(funct):
  def inner_define_function():
    print('Add a third decorator define function to the base define function.')
    funct()
  return inner_define_function

def add_define_function_four(funct):
  def inner_define_function():
    print('Add a fourth decorator define function to the base define function.')
    funct()
  return inner_define_function

def add_define_function_five(funct):
  def inner_define_function():
    print('Add a fifth decorator define function to the base define function.')
    funct()
  return inner_define_function

@add_define_function_one
@add_define_function_two
@add_define_function_three
@add_define_function_four
@add_define_function_five

def base_define_function():
  print('Add other decorator define functions to the base define \
function,\nwithout modifying or changing the base define function.')

base_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Decorator define functions with *args and **kwargs

def add_define_function_one(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_two(funct):
  def inner_define_function(*args,**kwargs):
    print('Add another decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_three(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a third decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_four(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a fourth decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_five(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a fifth decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

@add_define_function_one
@add_define_function_two
@add_define_function_three
@add_define_function_four
@add_define_function_five

def base_define_function():
  print('Add other decorator define functions to the base define \
function,\nwithout modifying or changing the base define function.')

base_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create the same decorator define function Python program
# example as above. However, let's also give the base define function
# some argument variables of its own.

def add_define_function_one(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_two(funct):
  def inner_define_function(*args,**kwargs):
    print('Add another decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_three(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a third decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_four(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a fourth decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_five(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a fifth decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

@add_define_function_one
@add_define_function_two
@add_define_function_three
@add_define_function_four
@add_define_function_five

def base_define_function(text1,text2,text3):
  print(f'Add other {text1} define functions to the {text2} define \
{text3},\nwithout modifying or changing the {text2} define {text3}.')

base_define_function('decorator','base','function')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create the same decorator define function Python program
# example as above. However, let's also give the base define function
# only one argument variable of its own, via invoking the *args prefix
# to satisfy as many argument placeholder values as we wish. We
# have to use index brackets with index numbers [n] to call up each
# argument placeholder value: 'decorator','base','function', via invoking
# args[n] to do the job. Note: you can call *args any name you wish, but
# the argument variable name 'args' is the standard for the *args prefix.

def add_define_function_one(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_two(funct):
  def inner_define_function(*args,**kwargs):
    print('Add another decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_three(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a third decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_four(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a fourth decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

def add_define_function_five(funct):
  def inner_define_function(*args,**kwargs):
    print('Add a fifth decorator define function to the base define function.')
    funct(*args,**kwargs)
  return inner_define_function

@add_define_function_one
@add_define_function_two
@add_define_function_three
@add_define_function_four
@add_define_function_five

def base_define_function(*args):
  print(f'Add other {args[0]} define functions to the {args[1]} define \
{args[2]},\nwithout modifying or changing the {args[1]} define {args[2]}.')

base_define_function('decorator','base','function')

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

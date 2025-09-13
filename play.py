
# Easy define function program example:

def function():
  print('This define function prints text only.')

function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy define function with one parameter variable and one argument value program
# example:

def function_argument(argument):
  print('This define function retrieves one argument',argument)  # non formatted string

function_argument('value.')


def function_argument(argument):
  print('This define function retrieves one argument '+argument)  # non formatted string

function_argument('value.')


def function_argument(argument):
  print('This define function retrieves one argument {}'.format(argument))  # old formatted string

function_argument('value.')


def function_argument(argument):
  print(f'This define function retrieves one argument {argument}')  # new f' string format

function_argument('value.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy define function with two parameter variables and two argument values program
# example:

def function_argument(argument1,argument2):
  print(f'This define function retrieves two {argument1} {argument2}')

function_argument('argument','values.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy define function with three parameter variables and three argument values program
# example:

def function_argument(argument1,argument2,argument3):
  print(f'This define {argument1} retrieves three {argument2} {argument3}')

function_argument('function','argument','values.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy define function with one return value program example:

def return_function(argument):
  return 'value.'

print('This define function returns one argument',return_function(  # non formatted string
  'argument placeholder value'))


def return_function(argument):
  return 'value.'

print('This define function returns one argument '+return_function(  # non formatted string
  'argument placeholder value'))


def return_function(argument):
  return 'value.'

print('This define function returns one argument {} '.format(return_function(  # old formatted string
  'argument placeholder value')))


def return_function(argument):
  return 'value.'

print(f'This define function returns one argument \
{return_function ("argument placeholder value")}')  # new f' string format
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy define function with two return values program example:

def return_function(argument1,argument2):
  return 'argument','values.'

print(f'This define function returns two \
{return_function("argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value")[1]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# With *args, you can create as many argument placeholder values without the worry of
# how many argument placeholder values to how may parameter variables, needed to be
# satisfied.

def return_function(*args):
  return 'argument','values.'

print(f'This define function returns two \
{return_function("argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value")[1]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy define function with three return values program example:

def return_function(argument1,argument2,argument3):
  return 'argument','values.','WOW!'

print(f'This define function returns three \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[1]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[2]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# With *args, you can create as many argument placeholder values without the worry of
# how many argument placeholder values to how may parameter variables, needed to be
# satisfied.

def return_function(*args):
  return 'argument','values.','WOW!'

print(f'This define function returns three \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[1]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[2]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Return math calculations program examples:

def return_function(num1,num2):
  return num1+num2

print(return_function(5,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(num1,num2):
  return num1-num2

print(return_function(5,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(num1,num2):
  return num1*num2

print(return_function(5,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(num1,num2):
  return num1/num2

print(return_function(5,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(num1,num2):
  return num1**num2

print(return_function(5,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(num1,num2,num3,num4,num5,num6):
  return num1+num2-num3*num4/num5**num6

print(return_function(5,4,3,6,3,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# With *args, you can create as many argument placeholder values without the worry of
# how many argument placeholder values to how may parameter variables, needed to be
# satisfied.

def return_function(*args):
  return args[0]+args[1]-args[2]*args[3]/args[4]**args[5]

print(return_function(5,4,3,6,3,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create multi return functions program example:

def return_fuction_one(arg):
  return arg

def return_fuction_two(arg):
  return arg

def return_fuction_three(arg):
  return arg

def return_fuction_four(arg):
  return arg

print(return_fuction_one('One'))
print(return_fuction_two('Two'))
print(return_fuction_three('Three'))
print(return_fuction_four('Four'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create multi return functions inside one define function program example:

def multi_return_function():
  def return_fuction_one(arg):
    return arg

  def return_fuction_two(arg):
    return arg

  def return_fuction_three(arg):
    return arg

  def return_fuction_four(arg):
    return arg

  print(return_fuction_one('One'))
  print(return_fuction_two('Two'))
  print(return_fuction_three('Three'))
  print(return_fuction_four('Four'))

multi_return_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create multi return functions inside one define function with one parameter variable and
# one argument placeholder value program example:

def multi_return_function(arg):
  def return_fuction_one(arg):
    return arg

  def return_fuction_two(arg):
    return arg

  def return_fuction_three(arg):
    return arg

  def return_fuction_four(arg):
    return arg

  print(return_fuction_one('One'))
  print(return_fuction_two('Two'))
  print(return_fuction_three('Three'))
  print(return_fuction_four('Four'))
  print(f"And that's how it's {arg}")

multi_return_function('Done!!')  # argument placeholder value
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Lambda functions are nameless, throwaway functions program examples:

lambda_function = lambda first_name,last_name: first_name+last_name

print(lambda_function('Jim',' Doe'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x: x

print(lambda_function(4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x: x+x

print(lambda_function(4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x: x-x

print(lambda_function(4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x: x*x

print(lambda_function(4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x: x/x

print(lambda_function(4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x,y: x+y

print(lambda_function(4,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x,y: x-y

print(lambda_function(4,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x,y: x*y

print(lambda_function(4,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x,y: x/y

print(lambda_function(4,4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda a,b,x,y,z: a+b-x*y/y == z

print(lambda_function(2,12,2,2,12))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda a,b,x,y,z: a+b-x*y/y == z if z == z else False

print(lambda_function(2,12,2,2,12))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Follow the rules for 'ORDER of OPERATION' to get the correct answer. First multiply or
# divide integer numbers. Next add or subtract integer numbers. Watch the signs + and -
# are used for creating positive and negative integer numbers. For example: -2*3 = -6 not
# +6, which is just 6, without writing the + sign. Negative integer numbers always show
# the - sign. All computers follow the 'Order of Operation', which also means that you
# must have an understanding of 'BEDMAS' and the order of operation. A wee bit of basic
# algebra knowledge wouldn't hurt, but it's not required for computer programming; it
# just makes computer programming that much more dynamic and fun.

try:
  user_input = int(input('What does 2+12-2*2/2 equal? ').strip())   # 2+12 -2*2/2 = 2+12 -4/2 = 2+12-2 = 14-2 = 12

  lambda_function = lambda a,b,x,y,z: a+b-x*y/y == z if z == user_input else False

  print(lambda_function(2,12,2,2, user_input))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Lambda functions with conditional operators program examples:

lambda_function = lambda x,y: x == y if x > y else x

print(lambda_function(3,6))


lambda_function = lambda x,y: x == y if x > y else y

print(lambda_function(3,6))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x,y: x == y if x < y else x

print(lambda_function(6,3))


lambda_function = lambda x,y: x == y if x < y else y

print(lambda_function(6,3))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x,y: x > y if x < y else x

print(lambda_function(6,3))


lambda_function = lambda x,y: x > y if x < y else y

print(lambda_function(6,3))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda x,y: x < y if x > y else x

print(lambda_function(3,6))


lambda_function = lambda x,y: x < y if x > y else y

print(lambda_function(3,6))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create lambda functions that check odd or even numbers program examples:

num = 4

lambda_function = lambda x: x if num%2 == 0 else f'{num} is an odd number.'

print(lambda_function(f'{num} is an even number.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
num = 4

lambda_function = lambda x: x if num%2 == 1 else f'{num} is an even number.'

print(lambda_function(f'{num} is an odd number.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that asks the user for an odd or even number, via the input()
# function, along with a lambda function.

try:
  user_input = int(input('Give me an odd or even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 0 else f'{user_input} is an odd number.'

  print(lambda_function(f'{user_input} is an even number.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that asks the user for an odd or even number, via the input()
# function, along with a lambda function.

try:
  user_input = int(input('Give me an odd or even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 1 else f'{user_input} is an even number.'

  print(lambda_function(f'{user_input} is an odd number.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that demands the user for an even number only, via the input()
# function, along with a lambda function.

try:
  user_input = int(input('Give me an even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 0 else 'I want an even number only.'

  print(lambda_function(f'{user_input} is an even number.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that demands the user for an even number only, via the input()
# function, along with a lambda function.

try:
  user_input = int(input('Give me an even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 1 else f'{user_input} is an even number.'

  print(lambda_function('I want an even number only.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that asks the user for an odd or even number, via the input()
# function and the modulo % operator.

try:
  user_input = int(input('Give me an odd or even number: ').strip())

  if user_input%2 == 0:
    print(f'{user_input} is an even number.')
  else:
    print(f'{user_input} is an odd number.')

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that asks the user for an odd or even number, via the input()
# function and the modulo % operator.

try:
  user_input = int(input('Give me an odd or even number: ').strip())

  if user_input%2 == 1:
    print(f'{user_input} is an odd number.')
  else:
    print(f'{user_input} is an even number.')

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Note: the different ways you can create these Python program examples below...

count = 100

for i in range(1,count+1):
  if i%2 == 0:
    print(f'{i} is an even number.')


for i in range(1,count+1):
  if i%2 == 1:
    print(f'{i} is an odd number.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
count = 100

for i in range(1,count+1):
 if i%2 == 0:
   print(f'{i} is an even number.')

 else:
   print(f'{i} is an odd number.')


for i in range(1,count+1):
  if i%2 == 1:
    print(f'{i} is an odd number.')

  else:
    print(f'{i} is an even number.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This Python program example is an accidental, Happy Accident. It's probably one of my
# later and one of my most favorite computer programming discoveries to happen. I will be
# using this discovery within my future robotics and Raspberry Pi4 Python programs. The
# modulo % operator is fascinating; the things you can do with it.

message = (
  "Type a number equal to or higher than '8': ",
  '\nThe value is not high enough.\n',
  '\nNumbers only please:\n')

add_even = 'Even numbers: ','Odd numbers: '

while True:
  try:
    user_input = int(input(message[0]).strip())

    if user_input < 8:print(message[1])

    elif user_input >= 8:

      for i in range(2):  # If you increase this value, the IndexError: handler will execute.
        nums = []
        for j in range(1,user_input+1):
          if j%2 == i:nums.append(j)
        print('\n'+add_even[i],nums)
      break

  except ValueError:
    print(message[2])

  except IndexError:
    pass;break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that demands the user for an even number only, via the input()
# function and the modulo % operator. Let's create a while loop that won't end, until the
# user types an even number only.

while True:
  try:
    user_input = int(input('Give me an even number: ').strip())

    if not user_input%2==0:
      print('I want an even number only.')

    elif not user_input%2==1:
      print(f'{user_input} is an even number:')
      break

  except ValueError:
    print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create auto typing text with Python.

import time,os

text,knowledge_poem = print,(f'''
'Knowledge'
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream's creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.

THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
Never give up your dream, no matter how far away it may seem to be, because that is when it is
ever so close to becoming true. If you dream of something long enough and strong enough, your
dream will come true, when you least expect it. Always remember, we are never too young or too
old to dream and use our imagination, for we only get one and it is ours forever. May your heart
be filled with courage and compassion, and your mind be as limitless and as wondrous as the
universe itself! If you dream it, you can be it. Believe it!''','cls',len)

length=0

while length<=knowledge_poem[2](knowledge_poem[0]):
  text(knowledge_poem[0][:length])
  time.sleep(.05)
  os.system(knowledge_poem[1])
  length+=1

text(knowledge_poem[0])

input('\nPress Enter to close this Python program:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create reverse text with Python, and then ask the user to type letters or words, via the
# input() function. Invoke the count() function that counts how many times letters or
# words have been used within the text. Lastly, invoke the reverse indexing [::-1] method
# to create reverse text effects.

text,message,knowledge_poem = print,input,(f'''
!ti eveileB .ti eb nac uoy ,ti maerd uoy fI !flesti esrevinu
eht sa suordnow sa dna sseltimil sa eb dnim ruoy dna ,noissapmoc dna egaruoc htiw dellif eb
traeh ruoy yaM .reverof sruo si ti dna eno teg ylno ew rof ,noitanigami ruo esu dna maerd ot dlo
oot ro gnuoy oot reven era ew ,rebmemer syawlA .ti tcepxe tsael uoy nehw ,eurt emoc lliw maerd
ruoy ,hguone gnorts dna hguone gnol gnihtemos fo maerd uoy fI .eurt gnimoceb ot esolc os reve
si ti nehw si taht esuaceb ,eb ot mees yam ti yawa raf woh rettam on ,maerd ruoy pu evig reveN
DLIHC DNA NAMOW ,NAM YREVE OT SGNOLEB SIHT

.tneduts tsetaerg rieht era uoy roF !flesruoy ni eveileB
…su fo srehcaet tsetaerg eht ,suht era dnim eht dna traeh eht roF
.noitanigami ruo fo noitaerc s'maerd eht
,lla fo amolpid tsetaerg eht ot yek eht dloh dnim eht dna traeh eht roF
.rednow otni rednop ot yek eht si nettirw eb ot maxe ylno ehT
.dnim eht dna traeh eht era ,dedeen skoobtxet ylno ehT
!flesti dnim eht fo dna traeh eht fo noitnevni eerf a si
'egdelwonK'
''')

text(knowledge_poem[::-1])

user_input = message(
  " :nettirw neeb s'ti semit ynam woh uoy llet nac I dna ,meop siht ni drow ro rettel a epyT"[::-1]).strip()

text(f"\n'{user_input}' has been written {knowledge_poem.lower().count(user_input[::-1])} times.")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the 'match' and 'case' methods that shows the days in a week and the days in a
# weekend. Note: the 'case_' which tells Python to return a case, without returning a week
# day or a weekend day value.

def week_day(day):
  match day:
    case 'Monday'|'Tuesday'|'Wednesday'|'Thursday'|'Friday':
      return 'week day'

    case 'Saturday'|'Sunday':
      return 'weekend day'

    case _:
      return 'I cannot understand that...'

print(week_day('Saturday'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create decorator @ define functions in Python. Add other define functions to the base
# define function, without changing the base define function itself.

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
# Decorator @ define functions with *args and **kwargs

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
# Let's create the same decorator @ define function Python program example as above.
# However, let's also give the base define function some argument variables of its own.

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
# Let's create the same decorator define function Python program example as above.
# However, let's also give the base define function only one argument variable of its own,
# via invoking the *args prefix to satisfy as many argument placeholder values as we wish.
# We have to use index brackets with index numbers [n] to call up each argument placeholder
# value: 'decorator','base','function', via invoking args[n] to do the job. Note: you can call
# *args any name you wish, but the argument variable name 'args' is the standard for the
# *args prefix.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
redundant_code='''
print("Python Programmer's Glossary Bible")
print('This block of code can be used and reused again and again.')
'''
# Call the 'exec()' function as many times as you please.

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)

# Here is an example, using a for-loop to call the 'exec()' function.

for i in range(3):
    exec(redundant_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for loop inside an exec() function and see what happens when
# execute/run this Python program example:

reuse_code='''
for i in range(10):print(i)
'''
exec(reuse_code) # Call the exec() function as many times as you please.
exec(reuse_code)
exec(reuse_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create an integer number line using list comprehension.

values = [value for value in range(-10,+11)]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Find the mean of a list of number values in Python. Create a list of number
# values, and then add them all up, and then divide by how many number
# values there are in the list of number values.

mean_value = [1,2,3,4,5,6,7,8,9,10]
total = sum(mean_value)/len(mean_value)
answer = round(total,3)  # round to three decimal places optional

# this:

print(sum(mean_value),'divided by',len(mean_value),'= '+str(answer)+':')  # non formatted string

# this:

print(str(sum(mean_value))+' divided by '+str(len(mean_value))+' = '+str(answer)+':')  # non formatted string

# this:

print('{} divided by {} = {}:'.format(sum(mean_value),len(mean_value),answer))  # old formatted string

# or this:

print(f'{sum(mean_value)} divided by {len(mean_value)} = {answer}:')  # new f' string format
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Find the mean of a list of number values in Python. Create a list comprehension
# of number values, and then add them all up, and then divide by how many
# number values there are in the list comprehension of number values.

mean_value = [value for value in range(1,11)]

total = sum(mean_value)/len(mean_value)
answer = round(total,3)  # round to three decimal places optional

# this:

print(sum(mean_value),'divided by',len(mean_value),'= '+str(answer)+':')  # non formatted string

# this:

print(str(sum(mean_value))+' divided by '+str(len(mean_value))+' = '+str(answer)+':')  # non formatted string

# this:

print('{} divided by {} = {}:'.format(sum(mean_value),len(mean_value),answer))  # old formatted string

# or this:

print(f'{sum(mean_value)} divided by {len(mean_value)} = {answer}:')  # new f' string format
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Find the range of a list of number values, via invoking the min() and max() functions.

range_values = [1,2,3,4,5,6,7,8,9,10]

# this:

print(min(range_values),'and',max(range_values),'are the range values.')  # non formatted string

# this:

print(str(min(range_values))+' and '+str(max(range_values))+' are the range values.')  # non formatted string

# this:

print('{} and {} are the range values.'.format(min(range_values),max(range_values)))  # old formatted string

# or this:

print(f'{min(range_values)} and {max(range_values)} are the range values.')  # new f' string format
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Find the range of a list comprehension of number values, via invoking the min() and max()
# functions.

range_values = [value for value in range(1,11)]

# this:

print(min(range_values),'and',max(range_values),'are the range values.')  # non formatted string

# this:

print(str(min(range_values))+' and '+str(max(range_values))+' are the range values.')  # non formatted string

# this:

print('{} and {} are the range values.'.format(min(range_values),max(range_values)))  # old formatted string

# or this:

print(f'{min(range_values)} and {max(range_values)} are the range values.')  # new f' string format
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Join two lists together with the + sign.

list_values1 = [1,2,3,4,5,6,7,8,9,10]
list_values2 = [11,12,13,14,15,16,17,18,19,20]

join_lists = list_values1 + list_values2

print(join_lists)

# or this:

# Join two list comprehensions together with the + sign.

list_values1 = [value for value in range(1,11)]
list_values2 = [value for value in range(11,21)]

join_lists = list_values1 + list_values2

print(join_lists)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Join two lists together with the extend() function.

list_values1 = [1,2,3,4,5,6,7,8,9,10]
list_values2 = [11,12,13,14,15,16,17,18,19,20]

list_values1.extend(list_values2)

print(list_values1)

# or this:

# Join two list comprehensions together with the extend() function.

list_values1 = [value for value in range(1,11)]
list_values2 = [value for value in range(11,21)]

list_values1.extend(list_values2)

print(list_values1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# reverse two lists, and then join two lists together with the extend() function.

list_values1 = [1,2,3,4,5,6,7,8,9,10]
list_values2 = [11,12,13,14,15,16,17,18,19,20]

list_values1.reverse()
list_values2.reverse()

list_values1.extend(list_values2)

print(list_values1)

# or this:

# reverse two list comprehensions, and then join two list comprehensions together with the
# extend() function.

list_values1 = [value for value in range(1,11)]
list_values2 = [value for value in range(11,21)]

list_values1.reverse()
list_values2.reverse()

list_values1.extend(list_values2)

print(list_values1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create three different integer sets that will combine/unionize all three sets into one single
# set. Convert the single set into a list, using the list() function. Next, view the contents
# of the list, along with the slice() function to set the range of list content values to display
# on the screen.

# Type and execute/run this Python program example below.

# To reduce lines of code, create packed variables and their
# packed values.

x,y,z = (
    {1,2,3,4,9,6,7,8,5,9,10},
    {11,12,13,14,15,16,17},
    {18,19,20,21,22,23,24})

a = slice(24) # slice the set with the slice() function

# To reduce lines of code, create packed variables and their
# packed values.

length1,length2,length3 = len(x),len(y),len(z)

unionize = x.union(y,z) # unionize x to y and z with the value v.union() function

convert = list(unionize) # cast the set to a list with the list() function

answer = length1,length2,length3

# Add the total values between length1, length2 and length3 with the sum()
# function.

total_sum = sum(answer) # add all three values of answer together with the sum() function

# View the contents of x, y and z in their combined, converted sets to a list.

print('View the value contents of the unionized list to check it:\n\n'+str(convert[a]))

# Create a variable called sentence_loop, along with all its values.

sentence_loop = (
    f'\nThe length of (x) = {length1}',f'The length of (y) = {length2}',
    f'The length of (z) = {length3}',f'\nThe total lengths of x+y+z = {total_sum}')

# Create a for loop that will loop through the sentence_loop variable, using a single print()
# function. The for loop will iterate until all the values are cycled through the sentence_loop
# variable.

for i in sentence_loop:print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 | nums2)  # Union

print(nums1.union(nums2))  # Union

nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 & nums2)  # Intersection

print(nums1.intersection(nums2))  # Intersection

nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 - nums2)  # Difference

print(nums1.difference(nums2))  # Difference

nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 ^ nums2)  # Symmetric Difference

print(nums1.symmetric_difference(nums2))  # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1 = {0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2 = {1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1.union(nums2))  # Union
print(nums1.intersection(nums2))  # Intersection
print(nums1.difference(nums2))  # Difference
print(nums1.symmetric_difference(nums2))  # Symmetric Difference

# or this:

nums1 = {0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2 = {1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2)  # Union
print(nums1 & nums2)  # Intersection
print(nums1 - nums2)  # Difference
print(nums1 ^ nums2)  # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Cast two integer lists into two, sorted sets, via the set() function.

nums1 = [0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23]
nums2 = [1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22]

convert1,convert2 = set(nums1),set(nums2)

print(convert1 | convert2)  # Union
print(convert1 & convert2)  # Intersection
print(convert1 - convert2)  # Difference
print(convert1 ^ convert2)  # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the enumerate() function to loop through a list, using only two lines of code; one
# for the for-index enumerate() function and the other for the 'print' statement.

name_list = ['John','Bob','Rob','Tom']

# Here is a simple for-loop that will loop through the name_list values starting with index
# 0, followed by index 1 and then index 2, and finally index 3.

for index in name_list:
    print(index)

# The for-loop example above is fine, but it has its limitations when it comes to multi indexing
# through a tuple or list alike. With the enumerate() function, such things are possible. Try
# these enumerate() function Python program examples below and see what happens when
# you experiment with them.

for index,name in enumerate(name_list):
    print(index)

for index,name in enumerate(name_list):
    print(name)

for index,name in enumerate(name_list):
    print(index,name)

for index,name in enumerate(name_list,start=1):
    print(index,name)

name = ['John','Bob','Rob','Tom']
pet = ['Dog','Cat','Bird','Fish']
compute = ['Desktop','Laptop','Cellphone','Notebook']

# Note: the zip() function only goes to the shortest length in a multi list. However, you can simply
# keep them the same size such as the list examples above, which shows three lists called name,
# pet and computer. Each list has four values in them. This way, every value gets called inside
# one, single 'print' statement. Try these different examples below. Note: you can rename the words
# 'index1, index2 and index3' to any names you wish. You can also rename the name variable if
# you like.

for index1,index2,index3 in zip(name,pet,computer):
    print(index1)

for index1,index2,index3 in zip(name,pet,computer):
    print(index2)

for index1,index2,index3 in zip(name,pet,computer):
    print(index3)

for index1,index2,index3 in zip(name,pet,computer):
    print(index1,index2,index3)

# Let's try the enumerate() function with a 2d-list.

my_2d_list = [
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

my_2d_list = [
    ['John','Bob','Rob','Tom'],
    ['Desktop','Laptop','Cellphone','Notebook']]

for index in zip(my_2d_list):
    print(index[0][0])

for index in zip(my_2d_list):
    print(index[0][0],index[0][1],index[0][2],index[0][3])

# Let's try some fun experiment examples with some of what we've learned so far about the
# enumerate() function. Let's create a program that uses a sentence for each value in the fun_list1,
# fun_list2 and fun_list3 lists. Let's use the f' format to make string concatenations much easier
# to create.

fun_list1 = ['John','Bob','Rob','Tom']
fun_list2 = ['Dog','Cat','Bird','Fish']
fun_list3 = ['Desktop','Laptop','Cellphone','Notebook']

for index,name in enumerate(fun_list1):
    print(f"My name is {name}. I'm the value from the fun_list1, position {index}")

for index,name in enumerate(fun_list2):
    print(f"I am a {name}. I'm the value from the fun_list2, position {index}")

for index,name in enumerate(fun_list3):
    print(f"I am a {name}. I'm the value from the fun_list3, position {index}")

# These enumerate() function examples are great, but let's beef it up just a lot more with the
# zip() function, so we can create complex actions with all our fun_lists combined into complete,
# separate sentences, just simply using two lines of code. See what happens when you type
# and execute/run this Python program example below:

for list1,list2,list3 in zip(fun_list1,fun_list2,fun_list3):
    print(f"My name is {list1} and I have a {list2} picture on my {list3} screen.")

# The zip() function is very useful, but it can only reach as far as its shortest list length. That
# means, if you have two, three or more lists, the shortest list out of the three or more lists
# values will be cut off from the rest if one or more lists have extra values inside them. To
# avoid this from occurring, make all your lists the same size in each of their values. take a
# look at the example below:

fun_list1 = ['John','Bob','Rob','Tom']  # four values
fun_list2 = ['Dog','Cat','Bird','Fish']  # four values
fun_list3 = ['Desktop','Laptop','Cellphone','Notebook']  # four values

# The zip() function is sometimes better than a simple for-loop or a simple enumerate() function,
# in that it uses less lines of code and it can also achieve a far better programming style approach
# over program code redundancy on the programmer's part.

# Let's try one more example to prove this to be true. let's create another fun_list, zip() function
# Python program example. Type and execute/run this Python program below and see what
# happens with the output.

fun_list1 = ['John','Bob','Rob','Tom']
fun_list2 = ['Dog','Cat','Bird','Fish']
fun_list3 = ['Desktop','Laptop','Cellphone','Notebook']
fun_list4 = ['loves my','hates my','found my','lost my']
fun_list5 = ['fed his',"didn't feed his",'plays with his',"doesn't play with his"]

for list1,list2,list3,list4,list5 in zip(fun_list1,fun_list2,fun_list3,fun_list4,fun_list5):
    print(f'{list1} {list4} {list3} and {list5} {list2}.')

# Well, I think we pretty much learned what the enumerate() and zip() functions do. Now,
# it'spractice, practice, practice and more practice, practice, practice...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Just a little something else to gnaw on, while you practice.

# Use underscores _ to create readable numbers.

num1 = 10_000_000_000
num2 = 100_000_000

total = num1+num2

# Use :, to create readable output.

print(f'{total:,}')  # output: 10,100,000,000

# Use :_ to create readable output.

print(f'{total:_}')  # output: 10_100_000_000
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# which of these two Python programs use less lines of code?

george_boole = True

if george_boole:
    x = 1
else:
    x = 0

print(x)

# This one uses far less lines of code, yet both do the very same thing.

george_boole = True

x = 1 if george_boole else 0

print(x)

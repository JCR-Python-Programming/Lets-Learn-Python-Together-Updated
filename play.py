
# Welcome to the Wonderful World of Python Programming. Welcome to Python World!

# This is my most advanced Python programming materials yet, thus far. I've studied
# Python just about every single day for the past seven and a half years, since Christmas
# day, 2017. Everyone is more than welcome to learn Python through my Python
# programming manuals. I create these videos for when I cannot get access to github.com
# for any reason, I can at least refer to my own research notes, via YouTube, without
# losing my research, entirely. I can also be away from home and just quickly refer to
# my research notes on YouTube, without having to log onto github.com to refer to
# my research note studies.

# Created by Joseph C. Richardson, GitHub.com

# Because a Great Programmer always starts with a Great Programmer's Manual... 😁
'''---------------------------------------------------------------------------------------------------------------------------'''

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
# With *args, you can create as many argument placeholder values without the worry
# of how many argument placeholder values to how may parameter variables, needed
# to be satisfied.

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
# Create multi return functions inside one define function with one parameter variable
# and one argument placeholder value program example:

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
# Follow the rules for 'ORDER of OPERATION' to get the correct answer. First multiply
# or divide integer numbers. Next add or subtract integer numbers. Watch the signs +
# and - are used for creating positive and negative integer numbers. For example:
# -2*3 = -6 not +6, which is just 6, without writing the + sign. Negative integer numbers
# always show the - sign. All computers follow the 'Order of Operation', which also means
# that you must have an understanding of 'BEDMAS' and the order of operation. A wee
# bit of basic algebra knowledge wouldn't hurt, but it's not required for computer
# programming; it just makes computer programming that much more dynamic and fun.

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
# Create a Python program that demands the user for an even number only, via the
# input() function, along with a lambda function.

try:
  user_input = int(input('Give me an even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 0 else 'I want an even number only.'

  print(lambda_function(f'{user_input} is an even number.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that demands the user for an even number only, via the
# input() function, along with a lambda function.

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
# This Python program example is an accidental, Happy Accident. It's probably one
# of my later and one of my most favorite computer programming discoveries to happen.
# I will be using this discovery within my future robotics and Raspberry Pi4 Python
# programs. The modulo % operator is fascinating; the things you can do with it.

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
# Create a Python program that demands the user for an even number only, via the
# input() function and the modulo % operator. Let's create a while loop that won't end,
# until the user types an even number only.

while True:
  try:
    user_input = int(input('Give me an even number: ').strip())

    if not user_input%2 == 0:
      print('I want an even number only.')

    elif not user_input%2 == 1:
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

while length <= knowledge_poem[2](knowledge_poem[0]):
  text(knowledge_poem[0][:length])
  time.sleep(.05)
  os.system(knowledge_poem[1])
  length += 1

text(knowledge_poem[0])

input('\nPress Enter to close this Python program:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Count how many times a number appears in a list of integer values with the count()
# function.

count_like_values = [1,2,3,4,5,2,6,7,3,8,2,9,10].count(2)

print(count_like_values)

# Count how many times a letter appears in a list of text values with the count() function.

count_like_values = ['a','b','c','d','d','c','d','e','f'].count('d')

print(count_like_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create reverse text with Python, and then ask the user to type letters or words, via
# the input() function. Invoke the count() function that counts how many times letters
# or words have been used within the text. Lastly, invoke the reverse indexing [::-1]
# method to create reverse text effects.

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
# Invoke these text functions to create lower case text, upper case text, capital text
# and title text.

lower_case = 'LOWER CASE TEXT:'.lower()

print(lower_case)


upper_case = 'upper case text:'.upper()

print(upper_case)


capital_case = 'capital case text:'.capitalize()

print(capital_case)


title_case = 'title case text'.title()

print(title_case)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke these text functions to right justify text, left justify text and center justify text.

right_justified = 'Right Justified Text:'.rjust(40)

print('Right justified:',right_justified)


left_justified = 'Left Justified Text:'.ljust(40)

print(left_justified,'Left justified:')


center_justified = 'Center Justified Text:'.center(40)

print('Center justified:',center_justified,'Center justified:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create 30 blank spaces to indent text with this ' '*n

print(' '*30,'My indented text')  #                               My indented text

# this:

print(' '*30+'My indented text')  #                              My indented text

# or this:

print(f'{' '*30}My indented text')  #                             My indented text

# Create 30 dashes with this ' '*n

print('-'*30)  # ------------------------------

# Create 10 text words with this ' '*n

print('text '*10)  # text text text text text text text text text text

# or this:

print(' '*20+'text '*10)  #                    text text text text text text text text text text
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the 'match' and 'case' methods that shows the days in a week and the days
# in a weekend. Note: the 'case_' which tells Python to return a case, without returning
# a week day or a weekend day value.

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
# Create decorator @ define functions in Python. Add other define functions to the
# base define function, without changing the base define function itself.

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
# However, let's also give the base define function only one argument variable of its
# own, via invoking the *args prefix to satisfy as many argument placeholder values
# as we wish. We have to use index brackets with index numbers [n] to call up each
# argument placeholder value: 'decorator','base','function', via invoking args[n] to do
# the job. Note: you can call *args any name you wish, but the argument variable name
# 'args' is the standard for the *args prefix.

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
redundant_code = '''
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
# Let's create a for loop inside an exec() function and see what happens
# when execute/run this Python program example:

reuse_code = '''
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
# Find the range of a list comprehension of number values, via invoking the min()
# and max() functions.

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
# Append/add values to a list, via invoking the append() function.

list_values = [1,2,3,4,5,6,7,8,9,10]

list_values.append(11)

print(list_values)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# reverse two lists, and then join two lists together with the extend() function.

list_values1 = [1,2,3,4,5,6,7,8,9,10]
list_values2 = [11,12,13,14,15,16,17,18,19,20]

list_values1.reverse()
list_values2.reverse()

list_values1.extend(list_values2)

print(list_values1)

# or this:

# reverse two list comprehensions, and then join two list comprehensions together
# with the extend() function.

list_values1 = [value for value in range(1,11)]
list_values2 = [value for value in range(11,21)]

list_values1.reverse()
list_values2.reverse()

list_values1.extend(list_values2)

print(list_values1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Replace string letters, numbers and text strings, via the replace() function.

print('I love my dog so very much!'.replace('dog','cat'))

# or this:

text_string = 'I love my dog so very much!'

print(text_string.replace('dog','cat'))

# or this:

text_string = 'I love my dog so very much!'.replace('dog','cat')

print(text_string)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create three different integer sets that will combine/unionize all three sets into one
# single set. Convert the single set into a list, using the list() function. Next, view the
# contents of the list, along with the slice() function to set the range of list content
# values to display on the screen.

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

# Create a for loop that will loop through the sentence_loop variable, using a single
# print() function. The for loop will iterate until all the values are cycled through the
# sentence_loop variable.

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
# Use the enumerate() function to loop through a list, using only two lines of code;
# one for the for-index enumerate() function and the other for the 'print' statement.

name_list = ['John','Bob','Rob','Tom']

# Here is a simple for-loop that will loop through the name_list values starting with index
# 0, followed by index 1 and then index 2, and finally index 3.

for index in name_list:
    print(index)

# The for-loop example above is fine, but it has its limitations when it comes to multi indexing
# through a tuple or list alike. With the enumerate() function, such things are possible.
# Try these enumerate() function Python program examples below and see what happens
# when you experiment with them.

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
computer = ['Desktop','Laptop','Cellphone','Notebook']

# Note: the zip() function only goes to the shortest length in a multi list. However, you
# can simply keep them the same size such as the list examples above, which shows
# three lists called name, pet and computer. Each list has four values in them. This way,
# every value gets called inside one, single 'print' statement. Try these different examples
# below. Note: you can rename the words 'index1, index2 and index3' to any names you
# wish. You can also rename the name variable if you like.

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

# Let's try some fun experiment examples with some of what we've learned so far
# about the enumerate() function. Let's create a program that uses a sentence for
# each value in the fun_list1, fun_list2 and fun_list3 lists. Let's use the f' format to
# make string concatenations much easier to create.

fun_list1 = ['John','Bob','Rob','Tom']
fun_list2 = ['Dog','Cat','Bird','Fish']
fun_list3 = ['Desktop','Laptop','Cellphone','Notebook']

for index,name in enumerate(fun_list1):
    print(f"My name is {name}. I'm the value from the fun_list1, position {index}")

for index,name in enumerate(fun_list2):
    print(f"I am a {name}. I'm the value from the fun_list2, position {index}")

for index,name in enumerate(fun_list3):
    print(f"I am a {name}. I'm the value from the fun_list3, position {index}")

# These enumerate() function examples are great, but let's beef it up just a lot more
# with the zip() function, so we can create complex actions with all our fun_lists combined
# into complete, separate sentences, just simply using two lines of code. See what
# happens when you type and execute/run this Python program example below:

for list1,list2,list3 in zip(fun_list1,fun_list2,fun_list3):
    print(f"My name is {list1} and I have a {list2} picture on my {list3} screen.")

# The zip() function is very useful, but it can only reach as far as its shortest list length.
# That means, if you have two, three or more lists, the shortest list out of the three or
# more lists values will be cut off from the rest if one or more lists have extra values
# inside them. To avoid this from occurring, make all your lists the same size in each
# of their values. take a look at the example below:

fun_list1 = ['John','Bob','Rob','Tom']  # four values
fun_list2 = ['Dog','Cat','Bird','Fish']  # four values
fun_list3 = ['Desktop','Laptop','Cellphone','Notebook']  # four values

# The zip() function is sometimes better than a simple for-loop or a simple enumerate()
# function, in that it uses less lines of code and it can also achieve a far better programming
# style approach over program code redundancy on the programmer's part.

# Let's try one more example to prove this to be true. let's create another fun_list,
# zip() function Python program example. Type and execute/run this Python program
# below and see what happens with the output.

fun_list1 = ['John','Bob','Rob','Tom']
fun_list2 = ['Dog','Cat','Bird','Fish']
fun_list3 = ['Desktop','Laptop','Cellphone','Notebook']
fun_list4 = ['loves my','hates my','found my','lost my']
fun_list5 = ['fed his',"didn't feed his",'plays with his',"doesn't play with his"]

for list1,list2,list3,list4,list5 in zip(fun_list1,fun_list2,fun_list3,fun_list4,fun_list5):
    print(f'{list1} {list4} {list3} and {list5} {list2}.')

# Well, I think we pretty much learned what the enumerate() and zip() functions do.
# Now, it'spractice, practice, practice and more practice, practice, practice...
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pack three separate list variables, along with their separate value groups with just
# one equals = sign. This also works with tuples ( ), sets { } and dictionaries { } alike.

list_one,list_two,list_three = [1,2,3,4,5],['a','b','c','d','e'],['text 1','text 2','text 3','text 4','text 5']

print(list_one)
print(list_two)
print(list_three)

# or this:

list_one,list_two,list_three = [
  [1,2,3,4,5],['a','b','c','d','e'],['text 1','text 2','text 3','text 4','text 5']]

print(list_one,list_two,list_three)

# or this:

list_one,list_two,list_three = [
  [1,2,3,4,5],
  ['a','b','c','d','e'],
  ['text 1','text 2','text 3','text 4','text 5']]

print(list_one,list_two,list_three)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pack three separate tuple variables, along with their separate value groups with just
# one equals = sign. This also works with lists [ ], sets { } and dictionaries { } alike.

tuple_one,tuple_two,tuple_three = (
  (1,2,3,4,5),
  ('a','b','c','d','e'),
  ('text 1','text 2','text 3','text 4','text 5'))

print(tuple_one,tuple_two,tuple_three)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pack three separate set variables, along with their separate value groups with just
# one equals = sign. This also works with tuples ( ), lists [ ] and dictionaries { } alike.
# Note: sets are always in random order, and sets also get rid of duplicate values.
# However, sets with integer values only, are always ordered and also gets rid of
# duplicate values as well.

set_one,set_two,set_three = (
  {1,2,3,4,5,2,4},
  {'a','b','c','d','d','e'},
  {'text 1','text 2','text 3','text 4','text 5','text 4'})

print(set_one,set_two,set_three)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pack three separate dictionary variables, along with their separate key and value
# groups with just one equals = sign. This also works with tuples ( ), lists [ ] and sets
# { } alike.

dictionary_one,dictionary_two,dictionary_three = (
  {1:1,2:2,3:3,4:4,5:5},
  {1:'value1',2:'value2',3:'value3',4:'value4',5:'value5,'},
  {'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5,'})

print(dictionary_one,dictionary_two,dictionary_three)  # Check to see all the values.

print(dictionary_one.get(1))

print(dictionary_two.get(1))

print(dictionary_three.get('key1'))

# or this:

# If a dictionary key is not found, it will display the screen output as ' None '.
# However, you can place a message that tells the user that a key is not
# found. For example:

print(dictionary_three.get('key'))  # None

# The example below will assure a better user friendly experience for your Python
# programs you create.

print(dictionary_three.get('key','key not found:'))  # key not found:
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Display dictionary keys and dictionary values, via the keys() function and the values()
# function.

dictionary_one,dictionary_two,dictionary_three = (
  {1:1,2:2,3:3,4:4,5:5},
  {1:'value1',2:'value2',3:'value3',4:'value4',5:'value5,'},
  {'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5,'})

print(dictionary_one.keys())
print(dictionary_two.keys())
print(dictionary_three.keys())

print(dictionary_one.values())
print(dictionary_two.values())
print(dictionary_three.values())

# Invoke the length, len() function to check how many dictionary keys there are.

print(len(dictionary_one.keys()))
print(len(dictionary_two.keys()))
print(len(dictionary_three.keys()))

# Invoke the length, len() function to check how many dictionary values there are.

print(len(dictionary_one.values()))
print(len(dictionary_two.values()))
print(len(dictionary_three.values()))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Update a dictionary with the update() function, and then check the updated dictionary
# keys and values in each dictionary Python program example.

dictionary_one,dictionary_two,dictionary_three = (
  {1:1,2:2,3:3,4:4,5:5},
  {1:'value1',2:'value2',3:'value3',4:'value4',5:'value5,'},
  {'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5,'})

dictionary_one.update({6:6})
dictionary_two.update({6:'value6'})
dictionary_three.update({'key6':'value6'})

print(dictionary_one)  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
print(dictionary_two)  # {1: 'value 1', 2: 'value2', 3: 'value3', 4: 'value4', 5: 'value5,', 6: 'value6'}
print(dictionary_three)  # {'key1': 'value 1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5,', 'key6': 'value6'}

print(dictionary_one.get(6))  # 6
print(dictionary_two.get(6))  # value6
print(dictionary_three.get('key6'))  # value6
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi 2d tuple collection and check it, and then call up two indexes to display
# an actual value by itself.

multi_2d_tuple_collection = (
  (1,2,3,4,5),
  ('a','b','c','d','e'),
  ('text 1','text 2','text 3','text 4','text 5'))

print(multi_2d_tuple_collection)  # ((1, 2, 3, 4, 5), ('a', 'b', 'c', 'd', 'e'), ('text 1', 'text 2', 'text 3', 'text 4', 'text 5'))

print(multi_2d_tuple_collection[1][0])  # a
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi 2d tuple and check it, and then call up two indexes to display an actual
# value by itself.

tuple_one,tuple_two,tuple_three = (
  (1,2,3,4,5),
  ('a','b','c','d','e'),
  ('text 1','text 2','text 3','text 4','text 5'))

multi_2d_tuple = tuple_one,tuple_two,tuple_three

print(tuple_one,tuple_two,tuple_three)  # (1, 2, 3, 4, 5) ('a', 'b', 'c', 'd', 'e') ('text 1', 'text 2', 'text 3', 'text 4', 'text 5')

print(multi_2d_tuple[1][0])  # a
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi 2d list collection and check it, and then call up two indexes to display
# an actual value by itself.

multi_2d_list_collection = [
  [1,2,3,4,5],
  ['a','b','c','d','e'],
  ['text 1','text 2','text 3','text 4','text 5']]

print(multi_2d_list_collection)  # ([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], ['text 1', 'text 2', 'text 3', 'text 4', 'text 5'])

print(multi_2d_list_collection[1][0])  # a
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi 2d list and check it, and then call up two indexes to display an actual
# value by itself.

list_one,list_two,list_three = [
  [1,2,3,4,5],
  ['a','b','c','d','e'],
  ['text 1','text 2','text 3','text 4','text 5']]

multi_2d_list = list_one,list_two,list_three

print(list_one,list_two,list_three)  # [1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], ['text 1', 'text 2', 'text 3', 'text 4', 'text 5']

print(multi_2d_list[1][0])  # a
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi 2d set collection and check it.

multi_2d_set_collection = (
  {1,2,3,4,5,2,4},
  {'a','b','c','d','d','e'},
  {'text 1','text 2','text 3','text 4','text 5','text 4'})

print(multi_2d_set_collection)  # ({1, 2, 3, 4, 5}, {'d', 'b', 'e', 'a', 'c'}, {'text 2', 'text 4', 'text 3', 'text 5', 'text 1'})
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi 2d set collection and check it. Note: sets do not have indexes [ ] for
# them; you have to cast a set into a list, via the list() function to display values by
# themselves. Invoke the sort() function to sort random list values from the random
# set of values.

multi_2d_set_collection = (
  {1,2,3,4,5,2,4},
  {'a','b','c','d','d','e'},
  {'text 1','text 2','text 3','text 4','text 5','text 4'})

print(multi_2d_set_collection)  # ({1, 2, 3, 4, 5}, {'d', 'b', 'e', 'a', 'c'}, {'text 2', 'text 4', 'text 3', 'text 5', 'text 1'})

cast_my_set_into_list = list(multi_2d_set_collection[2])

cast_my_set_into_list.sort()  # invoke the sort() function to sort the list

print(cast_my_set_into_list[0])  # text 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a default tuple and tuple index[n][n] mix

test = 1,2,3,4,5,('a','b','c','d','e',('one','two','three','four','five'))

print(test[0])  # 1

print(test[5][2])  # c

print(test[5][5][2])  # three

# Create a tuple index[n][n] mix

test = (1,2,3,4,5,('a','b','c','d','e',('one','two','three','four','five')))

print(test[0])  # 1

print(test[5][2])  # c

print(test[5][5][2])  # three
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a default tuple and list index[n][n] mix.

test = 1,2,3,4,5,['a','b','c','d','e',['one','two','three','four','five']]

print(test[0])  # 1

print(test[5][2])  # c

print(test[5][5][2])  # three

# Create a list index[n][n] mix

test = [1,2,3,4,5,['a','b','c','d','e',['one','two','three','four','five']]]

print(test[0])  # 1

print(test[5][2])  # c

print(test[5][5][2])  # three
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sort a list without sorting the actual list, via invoking the sorted() function.

my_list = ['a','c','b','e','d']

my_list_sorted = sorted(my_list)

print(my_list_sorted)  # ['a', 'b', 'c', 'd', 'e']

print(my_list)  # ['a', 'c', 'b', 'e', 'd']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sort an actual list, via invoking the sort() function.

my_list = ['a','c','b','e','d']

my_list.sort()

print(my_list)  # ['a', 'b', 'c', 'd', 'e']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sort and then reverse an actual list, via invoking the sort() function and the reverse()
# function.

my_list = ['a','c','b','e','d']

my_list.sort(reverse = True)

print(my_list)  # ['e', 'd', 'c', 'b', 'a']

# or this:

my_list.sort(reverse = False)

print(my_list)  # ['a', 'b', 'c', 'd', 'e']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Reverse a list, without reversing the actual list, via invoking the reversed() function.

my_list = ['a', 'b', 'c', 'd', 'e']

my_list_reversed = reversed(my_list)

for i in my_list_reversed:print(i)

# or this:

my_list = ['a', 'b', 'c', 'd', 'e']

my_list_reversed = reversed(my_list)

my_list_comprehension = [value for value in my_list_reversed]

print(my_list_comprehension)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the insert() function to add new values to a list. Type an index[n] number, along
# with the new value called 'apple'.

my_list = ['a','b','c','d','e']

my_list.insert(1,'apple')

print(my_list)  # ['a', 'apple', 'b', 'c', 'd', 'e']

my_list.insert(3,'banana')

print(my_list)  # ['a', 'b', 'c', 'banana', 'd', 'e']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Change values in a list, via inserting an index[n] number, along with the new list value:
# 'apple'.

my_list = ['a','b','c','d','e']

my_list[0] = 'apple'

print(my_list)  # ['apple', 'c', 'b', 'e', 'd']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Remove values from a list, via invoking the pop(n) function.

my_list = ['a','b','c','d','e']

print(my_list)  # ['a', 'b', 'c', 'd', 'e']

my_list.pop(1)

print(my_list)  # ['a', 'c', 'd', 'e']

# Return popped values from a list, via invoking the pop(n) function.

my_list = ['a','b','c','d','e']

popped_value = my_list.pop(1)

print(popped_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Remove values from a list, via invoking the remove() function.

my_list = ['a','b','c','d','e']

print(my_list)  # ['a', 'b', 'c', 'd', 'e']

my_list.remove('c',)

print(my_list)  # ['a', 'b', 'd', 'e']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Clear all values from a list, via invoking the clear() function.

my_list = ['a','b','c','d','e']

print(my_list)  # ['a', 'b', 'c', 'd', 'e']

my_list.clear()

print(my_list)  # []
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Delete an entire list, along with its name and its values alike.

my_list = ['a','b','c','d','e']

print(my_list)  # ['a', 'b', 'c', 'd', 'e']

del my_list

try:
  print(my_list)
except NameError:
  print('my_list[ ] no longer exists:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Copy a list with the copy() function.

my_list = ['text 1','text 2','text 3','text 4','text 5']

list_copy = my_list.copy()

print(list_copy)  # ['text 1', 'text 2', 'text 3', 'text 4', 'text 5']

print(list_copy[0])  # text 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Copy a dictionary with the copy() function.

my_dictionary = {'key1':'value 1','key2':'value2','key3':'value3','key4':'value4','key5':'value5'}

dictionary_copy = my_dictionary.copy()

print(dictionary_copy)  # {'text 5', 'text 2', 'text 1', 'text 3', 'text 4'}

print(dictionary_copy.get('key1'))  # value 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Copy a set with the copy() function.

my_set = {'text 1','text 2','text 3','text 4','text 5'}

set_copy = my_set.copy()

print(set_copy)  # {'text 5', 'text 2', 'text 1', 'text 3', 'text 4'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can do a lot with for loops. I practice Python everyday and I'm always tripping
# onto things, just by trial and error alone. I wasn't shown this at all. This is one of my
# own happy accidents. I got really bored and did this for us all.

names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

for i,x,y,z in names1,names2,names3:
    print('Hello',i+'. How are you? You bought a cute',y,'I see...')
    print('Hello',x+'. How are you? You bought a cute',z,'I see...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence= 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print(sentence[0],i+sentence[1],y,sentence[2])
    print(sentence[0],x+sentence[1],z,sentence[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence = 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print('{} {} {} {}'.format(sentence[0],i+sentence[1],y,sentence[2]))  # old formatted string
    print('{} {} {} {}'.format(sentence[0],x+sentence[1],z,sentence[2]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence = 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print(f'{sentence[0]} {i}{sentence[1]} {y} {sentence[2]}')  # new f' string format
    print(f'{sentence[0]} {x}{sentence[1]} {z} {sentence[2]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what casting a tuple( ), a list[ ] and a set{ } are all about, with these
# casting functions: tuple(), list() and set(). Note, the dict() function only works
# to create a dictionary from scratch; the dict() function is not a casting function.
# However, we will learn to create a dictionary from scratch, via the dict() function.

# Here is a really neat trick about casting tuples and such. Tuples can be casted
# to lists, via the list() function to be able to sort the list, and then cast it back into
# an immutable tuple, if you wish not to change or modify any tuple values after
# casting the list back into a tuple. Here are some great cast examples below:

my_tuple = ('dog','bird','fish','cat')

cast_tuple_into_list = list(my_tuple)

print(cast_tuple_into_list)  # ['dog', 'bird', 'fish', 'cat']

print(cast_tuple_into_list[1])  # bird

# Let's cast the list back into a tuple.

cast_list_into_tuple = tuple(cast_tuple_into_list)

print(cast_list_into_tuple)  # ('dog', 'bird', 'fish', 'cat')

print(cast_list_into_tuple[1])  # bird
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tuples cannot be modified or sorted. However, we can cast this tuple of values into
# a sorted list of values, and then cast the sorted list back into a sorted tuple of values.

my_tuple = ('dog','bird','fish','cat')

cast_tuple_into_list = list(my_tuple)

cast_tuple_into_list.sort()

print(cast_tuple_into_list)  # ['bird', 'cat', 'dog', 'fish']

# # Let's cast the list back into a sorted tuple.

cast_list_into_tuple = tuple(cast_tuple_into_list)

print(cast_list_into_tuple)  # ('bird', 'cat', 'dog', 'fish')

print(cast_list_into_tuple[1])  # cat
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sets are great, they get rid of any duplicate values. Set's can also sort integer number
# values automatically only; sets cannot sort text string values, but they can still get
# rid of duplicate text string values. Note: sets do not contain indexes [ ] and the
# only way to get values from a set is to cast it into a tuple( ) or a list[ ]. Sets are also
# in random order, which is probably why sets don't have any index[ ] value ranges.
# Note: sets that have a mix of text string values and integer number values cannot
# be sorted. Sets automatically sort integer number values. You have to create one
# set{ } for integer values only, and one set{ } for text string values only. The sort()
# and sorted() functions can only sort converted sets that have text string values only.
# Sets are best used for integer number values; that's what sets are truly used for.

my_set = {'dog','bird','fish','cat'}

cast_set_into_list = list(my_set)

cast_set_into_list.sort()

print(cast_set_into_list)  # ['bird', 'cat', 'dog', 'fish']

print(cast_set_into_list[1])  # cat

# Let's cast the list back into a random, unsorted set.

cast_list_into_set = set(cast_set_into_list)

print(cast_list_into_set)  # {'fish', 'bird', 'cat', 'dog'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a dictionary from scratch with the dict() function. Note:
# you cannot invoke integer numbers for keys when creating a dictionary from scratch.
# This only works with actual dictionaries; you have to use text strings for keys, or
# text strings with integer numbers to the right of the text strings as shown below:

create_dictionary = dict(key1 = 'value1',key2 = 'value2',key3 = 'value3',key4 = 'value4',key5 = 'value5')

print(create_dictionary)  # {'key1': 'value 1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

print(create_dictionary.get('key2','key not found:'))  # value 2

# You can clearly see how dictionary keys can be numbers if you like, or be a mixture of
# number and text strings.

my_dictionary = {1:'value1',2:'value2',3:'value3',4:'value4',5:'value5'}

print(my_dictionary.get(2,'key not found:'))  # value 2

# This dictionary{ } has a mixture of both number and text lettrs as keys

my_dictionary = {1:'value1','key2':'value2',3:'value3','key4':'value4',5:'value5'}

print(my_dictionary)  # {1: 'value1', 2: 'value2', 3: 'value3', 4: 'value4', 5: 'value5'}

print(my_dictionary.get('key2','key not found:'))  # value 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Generate computer numbers in binary base 2, hexadecimal base 16 and octal base
# 8. Type in ASCII codes and see what they look like. For example: print(bin(65)) is the
# ASCII code value for the capital letter 'A' in binary base 2 as: '0b1000001'. Note: the
# '0b' is Python's prefix, which simply tells Python to work with binary base 2 numbers.

# Convert any number into a binary base 2 number.

print(bin(255))

# Convert any number into a hexadecimal base 16 number.

print(hex(255))

# Convert any number into an octal base 8 number.

print(oct(255))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run each of these program examples below and see what happens.

comp_nums = int(input('Please type any number to see its binary base 2 number value: ').strip())

print(f'The number {comp_nums} = the binary base 2 number value: {bin(comp_nums)}.')

comp_nums = int(input('Please type any number to see its hexadecimal base 16 number value: ').strip())

print(f'The number {comp_nums} = the hexadecimal base 16 number value: {hex(comp_nums)}.')

comp_nums = int(input('Please type any number to see its octal base 8 number value: ').strip())

print(f'The number {comp_nums} = the octal base 8 number value: {oct(comp_nums)}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Generate computer numbers in binary base 2, hexadecimal base 16 and octal base
# 8. Type in ASCII codes and see what they look like. For example: print(f'{65:b}') is the
# ASCII code value for the capital letter 'A' in binary base 2 as: '1000001'. Note: the 'b'
# is Python's prefix, which simply tells Python to work with binary base 2 numbers.

# Convert any number into a binary base 2 number.

print(f'{255:b}')

# Convert any number into a hexadecimal base 16 number.

print(f'{255:x}')

# Convert any number into an octal base 8 number.

print(f'{255:o}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run each of these program examples below and see what happens.

comp_nums = int(input('Please type any number to see its binary base 2 number value: ').strip())

print(f'The number {comp_nums} = the binary base 2 number value: {comp_nums:b}.')

comp_nums = int(input('Please type any number to see its hexadecimal base 16 number value: ').strip())

print(f'The number {comp_nums} = the hexadecimal base 16 number value: {comp_nums:x}.')

comp_nums = int(input('Please type any number to see its octal base 8 number value: ').strip())

print(f'The number {comp_nums} = the octal base 8 number value: {comp_nums:o}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is for advanced Python programmers, who want something a little bit saltier.
# Create this Welcome To The Binary Beat In Motion Python program using a single
# print() function. Use the backslash '\' to create line breaks within the print() function.

# Welcome to Python Programming Boot Camp!

# It's now time to forget all about the f' string format. Let's also forget all about creating
# variables, assigned to text messages. Let's do it the old fashioned pioneering way,
# when computer programming was young and looked a bit like this. However the old
# way of programming was much more confusing looking, than what you can only see
#  here. Just imagine having to do computer programming without any formatting of
# strings at all. Variables are always, always a must; they help make data much more
# flexible and manipulative to the core. Let's have some 'Dirty Code' fun with one of
# my faves below:

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

from time import sleep as delay;import os;os.system('title binary beat'.title())

red = '\x1b[31m'
green = '\x1b[32m'
blue = '\x1b[34m'
yellow = '\x1b[33m'
purple = '\x1b[35m'
white = '\x1b[37m'
os.system('cls')
n=0

while True:
    print(white+'\n'+' '*6+'welcome to the binary beat in motion python program example:'.title()
          +yellow+'\n\n'+' '*6+'1     1    1    1    1   1   1   1 = eight bits or one byte'
          +'\n\n'+' '*6+'128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = decimal number: 255''\n\n'+' '*2
          +'binary base: 2, octal base: 8, hexadecimal base: 16, decimal base: 10'.title()
          +'\n\n'+' '*3+yellow,len(f'{n:b}'),green+'binary digits: '.title()
          +yellow+f'{n:b} '+red+'=\n\n'+' '*3+yellow,len(f'{n:o}'),green+'octal digits: '.title()
          +yellow+f'{n:o} '+red+'=\n\n'+green+' '*3+yellow,len(f'{n:x}'),green+'hexadecimal digits: '.title()
          +yellow+f'{n:X} '+red+'= '+green+'\n\n'+' '*3+yellow,len(f'{n:d}'),green+'decimal digits: '.title()
          +red+'= '+yellow+f'{n:d}');delay(1);os.system('cls');n+=1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is for advanced Python programmers, who want something a little bit saltier.
# Create this Fibonary Bits In Action! Python program using a single print() function.
# Use the backslash '\' to create line breaks within the print() function.

# Welcome to Python Programming Boot Camp!

# Type and execute/run this Python program example below and see what happens.

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

import os;os.system('title fibonary bits in action!'.title())
from time import sleep as delay

red = '\x1b[31m'
green = '\x1b[32m'
blue = '\x1b[34m'
yellow = '\x1b[33m'
purple = '\x1b[35m'
white = '\x1b[37m'

title_text = f'fibonary bits in action!'.title(),'fibonacci natural number sequence:'.title()
text = (' binary digits: ',' octal digits: ',' hexadecimal digits: ',' decimal digits:',' fibonacci digits: '.title())

lb = '\n';lbb = '\n\n'; elb = ' =\n';eq = ' = ';sp = ' '

num1 = 0;num2 = 1
fib = [num1,num2]

pause=1

while True:
    os.system('cls')
    num3 = num1+num2
    fib.append(num3)
    num1 = num2;num2 = num3

    b = f'{num3:b}';o = f'{num3:o}'
    x = f'{num3:X}';d = f'{num3:d}'

# f' string formatted print() function example:

    print(f'{white}{lb}{sp*16}{title_text[0]}{lb}{red}{lb}{sp*4}{len(b)}{green}{text[0].title()}'
          f'{yellow}{b}{blue}{elb}{sp*4}{green}{red}{len(o)}{green}{text[1].title()}{yellow}'
          f'{o}{blue}{elb}{sp*4}{green}{red}{len(x)}{green}{text[2].title()}{yellow}{x}'
          f'{blue}{eq}{green}{lb}{sp*4}{red}{len(d)}{green}{text[3].title()}{blue}{eq}{yellow}'
          f'{d}{lbb}{white}{sp*11}{title_text[1]}{lbb}{green}{sp*3}{text[4]}{yellow}{num3:,d}')

    delay(pause)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is for advanced Python programmers, who want something a little bit saltier.
# Create this Fibonacci Natural Number Sequence in Action... Python program using
# a single print() function. Use the backslash '\' to create line breaks within the print()
# function.

# Welcome to Python Programming Boot Camp!

# Type and execute/run this Python program example below and see what happens.

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

import os,time;os.system(f'title fibonacci natural number sequence'.title())

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

text_words = (
    f'{text_colours[1]}Fibonacci Natural Number Sequence in Action...',

    f'\n\n{text_colours[2]}Fibonacci Natural Number Sequence example: \
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610...]',

    f'\n\n{text_colours[5]}Fibonacci Natural Numbers go on forever!',
    f'\n\nFibonacci Natural Numbers can only be found in \
nature, such as plants and animals...'
    )

for i in range(25):
    print('\n',' '*i,text_words[0])
    time.sleep(.25)
    os.system('cls')

num1 = 0
num2 = 1
fib = [num1,num2]

while True:
    num3 = num1+num2
    fib.append(num3)
    num1 = num2
    num2 = num3
    clock = (time.asctime())

    print('\n',' '*25,text_words[0],text_words[1],text_words[2])

    print(f'\nFibonacci Natural Number Sequence: {text_colours[2]}\
{num1} {text_colours[5]}+ {text_colours[2]}{num2}{text_colours[5]} = \
({text_colours[0]}{num1+num3}{text_colours[5]}){text_colours[5]}\n\n\
Fibonacci Natural Numbers: "{text_colours[0]}{num1+num3:,}{text_colours[5]}\
"\n\n{text_colours[0]}Date & Time:\n\n{clock}')

    time.sleep(1),os.system('cls')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# input Fibonacci Number Sequence program example, using a set{}

num1,num2 = 0,1

fib = {num1,num2}

words = (
    'is in the Fibonacci Sequence.',
    'is not in the Fibonacci Sequence.',
    'Please enter a correct Fibonacci Sequence Number: ',
    'Sorry! Numbers only.',
    'Memory Error!'
    )

while True:
    try:
        x=int(input(words[2]).strip())

        for i in range(x):
            fib_num=num1+num2
            fib.add(fib_num)
            num1=num2
            num2=fib_num

        if x in fib:
            print(x,words[0])
            break

        elif x not in fib:
            print(x,words[1])

    except ValueError:
        print(words[3])

    except MemoryError:
        print(words[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#                ASCII: (American Standard Code for Information Interchange)

# Below is the ascii code character chart. Each character has an ascii code value. Note:
# the ascii code value for the spacebar, or blank space character key is 32

# blank space = 32, ! = 33, " = 34, # = 35, $ = 36, % = 37, & = 38, ' = 39, ( = 40, ) = 41, * = 42
# + = 43, , = 44, - = 45, . = 46, / = 47, 0 = 48, 1 = 49, 2 = 50, 3 = 51, 4 = 52, 5 = 53, 6 = 54, 7 = 55
# 8 = 56, 9 = 57, : = 58, ; = 59, < = 60, = = 61, > = 62, ? = 63, @ = 64, A = 65, B = 66, C = 67
# D = 68, E = 69, F = 70, G = 71, H = 72, I = 73, J = 74, K = 75, L = 76, M = 77, N = 78, O = 79
# P = 80, Q = 81, R = 82, S = 83, T = 84, U = 85, V = 86, W = 87, X = 88, Y = 89, Z = 90, [ = 91
# \ = 92, ] = 93, ^ = 94, _ = 95, ` = 96, a = 97, b = 98, c = 99, d = 100, e = 101, f = 102, g = 103
# h = 104, i = 105, j = 106, k = 107, l = 108, m = 109, n = 110, o = 111, p = 112, q = 113, r = 114
# s = 115, t = 116, u = 117, v = 118, w = 119, x = 120, y = 121, z = 122, { = 123, | = 124, } = 125
# ~ = 126

# To get the ASCII code value of any letter, number or symbol keys, simply type and execute/run
# the program examples below and see what happens. Try using different letters, numbers
# and symbols to see their ASCII code values.

print(chr(65))
print(ord('A'))

print(chr(97))
print(ord('a'))

print(chr(66))
print(ord('B'))

print(chr(98))
print(ord('b'))

print('ASCII code',ord('A'),'is the uppercase letter',chr(65))
print('ASCII code',ord('a'),'is the lowercase letter',chr(97))

print('ASCII code',ord('B'),'is the uppercase letter',chr(66))
print('ASCII code',ord('b'),'is the lowercase letter',chr(98))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a for loop that prints out the ascii code character chart, via invoking the chr(n)
# character function. Tip: if you use small code within a for loop, you can place it right
# on the same line as the for loop, as shown.

for i in range(32,127):print(chr(i),'=',i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is for advanced Python programmers, who want something a little bit saltier.
# Create this Fibonacci ASCII CODE NUMERIC VALUE TRANSLATOR Python program.
# Use the backslash '\' to create line breaks within the print() function.

# Welcome to Python Programming Boot Camp!

# Type and execute/run this Python program example below and see what happens.

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

import os,time

text_features = (
    'cls', # index 0 = clear screen
    '\x1b[31m', # index 1 = red
    '\x1b[32m', # index 2 = green
    '\x1b[33m', # index 3 = yellow
    '\x1b[34m', # index 4 = blue
    '\x1b[37m'  # index 5 = red
    )

text_words = (
    f'\n{text_features[3]}ASCII CODE NUMERIC VALUE TRANSLATOR\n', # index 0 = text_words

    f'\n{text_features[3]}ASCII CODE CHARACTER VALUE TRANSLATOR\n', # index 1 = text_words

    f'\n{text_features[3]}ASCII CODE TRANSLATOR', # index 2 = text_words

    f'\n{text_features[3]}Thanks for choosing ASCII CODE TRANSLATOR', # index 3 = text_words

    'title ASCII CODE TRANSLATOR' # index 4 = text_words
    )

word_info = (
    f'{text_features[5]}Please type a number, then press \
(Enter) to confirm: {text_features[2]}', # index 0 = word_info

    f'{text_features[5]}Please type a letter key or a number key, then press \
(Enter) to confirm: {text_features[2]}', # index 1 = word_info

    f'\n{text_features[3]}Please choose which ASCII code translator you \
would like to use:\n\n{text_features[5]}Press (1) for ASCII code number \
values.\nPress (2) for ASCII code character values.\nPress \
(Q) to quit.{text_features[2]} ', # index 2 = word_info

    f'\n\n{text_features[3]}Do you wish to continue? Press \
(Enter) or press (Q) to quit: {text_features[2]}', # index 3 = word_info

    f'\n{text_features[1]}This is a Value Error!', # index 4 = word_info

    f'\n{text_features[1]}This is a Type Error!' # index 5 = word_info
    )

button = ('1','2','q')

def ascii_codes():

    os.system(text_words[4])

    def subroutine1():

        while True:
            os.system(text_features[0])
            print(text_words[0])

            try:
                ascii_code = int(input(word_info[0]).strip())
                ascii_code = input(f'\n{text_features[2]}{chr(ascii_code)}\
{text_features[5]} = ASCII code: " {text_features[2]}{ascii_code}\
{text_features[5]} " {word_info[3]}').lower().lower().strip()
                if ascii_code == button[2]:
                    break

            except ValueError:
                print(word_info[4])
                time.sleep(2)

    def subroutine2():
        while True:
            os.system(text_features[0])
            print(text_words[1])

            try:
                ascii_code = input(word_info[1]).strip()
                ascii_code = input(f'\n{text_features[2]}{ascii_code}\
{text_features[5]} = ASCII code: " {text_features[2]}{ord(ascii_code)}\
{text_features[5]} " {word_info[3]}').lower().strip()
                if ascii_code == button[2]:
                    break

            except TypeError:
                print(word_info[5])
                time.sleep(2)

    while True:
        os.system(text_features[0])
        print(text_words[2])

        butt=input(word_info[2]).lower().strip()
        if butt == button[0]:
            subroutine1()
        elif butt == button[1]:
           subroutine2()

        else:
            if butt == button[2]:
                os.system(text_features[0])
                print(text_words[3])
                time.sleep(3)
                break

ascii_codes()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I created The Devil's Lucky Number Python program example out of sheer boredom.
# This was a complete accident, when I was just playing with names of animals and names
# of things. About the forth name of an animal was the fox, and when I saw the output
# on my computer screen. I sort of jumped back in my seat. I tried the word 'dog'. I tried
# the word 'cat', I then tried the word bird. After that, I was playing with names of things,
# and then I tried the word 'fox' for another attempt at finding a number of some sort,
# and I found it. It scares the heck right out of me actually. This is the only time, that one
# of my own computer programming discoveries actually, really scares me. I'm not new
# to self taught computer programming. Not by a longshot. But this discovery still scares
# me. Yet however, computer science is sometimes a scary, mathematical reality in itself...

# Invoke the ord() function to get the ascii code values to the lower case letters of the word 'fox'

animal = (chr(102)+chr(111)+chr(120))  # fox

fox = (ord('f')+ord('o')+ord('x'))*2  # 102+111+120 = 333, 333*2 = The Devil's Lucky Number

print(animal)

print("And The Devil's Lucky Number is:",fox)

print("And The Devil's Lucky Number is: "+str(fox))

print("And The Devil's Lucky Number is: {}".format(fox))

print(f"And The Devil's Lucky Number is: {fox}")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python clock functions allow you to program the actual time in real time.Python clock
# functions work internally, in sync with the Windows clock. With Python clock functions;
# you can set the hour, minute, second, month, week, day and date. See Python clock
# function prefix descriptions below.

#  '%I' 12-hour prefix
#  '%H' 24-hour prefix
#  '%M' Minutes prefix
#  '%S' Seconds prefix
#  '%p' AM/PM prefix
#  '%A' Day of week prefix
#  '%B' Month prefix
#  '%d' Date prefix
#  '%Y' Year prefix
#  '%U' Weeks per year prefix
#  '%j' Days per year prefix

# Let's create a simple Python clock by invoking the Python clock function prefixes.
# First, however, we also need to import two modules; 'time' and 'datetime'. Type
# and execute/run the program example below and see what happens.

import time,datetime

print(datetime.datetime.now().strftime('%I:%M:%S:%p'))
print(datetime.datetime.now().strftime('%H:%M:%S'))
print(datetime.datetime.now().strftime('%A %B %d,%Y'))
print(datetime.datetime.now().strftime('Week %U'))
print(datetime.datetime.now().strftime('Day %j'))

# Remember you can reduce balky code via, using string variables. Let's use 'timer'
# as the variable and use 'datetime.datetime.now()' as the value. Type and execute/run
# the program example below and see what happens.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import time,datetime

timer = datetime.datetime.now()

print(timer.strftime('%I:%M:%S:%p'))
print(timer.strftime('%H:%M:%S'))
print(timer.strftime('%A %B %d,%Y'))
print(timer.strftime('Week %U'))
print(timer.strftime('Day %j'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's create a tuple variable called 'show_time' so we can reduce even more
# balky code, and also gain greater manipulative programming skills at the same time.
# Type and execute/run the program example below and see what happens.

import time,datetime

show_time = (
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

timer = datetime.datetime.now()

print(timer.strftime(show_time[0]))
print(timer.strftime(show_time[1]))
print(timer.strftime(show_time[2]))
print(timer.strftime(show_time[3]))
print(timer.strftime(show_time[4]))

# Now change and rearrange the tuple number values [0] through [4] in# the program
# example above and re-execute/run the program and see what happens.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's make our Python clock come to life. Let's also keep the code less balky
# and much more program manipulative at the same time. To make the Python clock
# come to life, we are simply going to use a while loop to constantly refresh the screen
# output. A 'time.sleep()' function will also be implemented to create a one-second
# sleep delay in the screen output. Let's also implement the 'os.system()' function to
# clear the screen output right after every one-second 'time.sleep' delay. Type and
# execute/run the program example below and see what happens.

import os,time,datetime

show_time = (
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

while True:
    timer = datetime.datetime.now()
    print(timer.strftime(show_time[0]))
    print(timer.strftime(show_time[1]))
    print(timer.strftime(show_time[2]))
    print(timer.strftime(show_time[3]))
    print(timer.strftime(show_time[4]))

    time.sleep(1)
    os.system('cls')

# Let's shorten our code by reducing our print() functions down to only one, using a for
# loop inside the while loop.

while True:
    for i in range(5):
        timer = datetime.datetime.now()
        print(timer.strftime(show_time[i]))

    time.sleep(1)
    os.system('cls')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use Python to open .txt files, such as notepad files. These two program examples
# do the exact same thing. However, with the first program example, you must tell
# Python to close the .txt file after reading it. In the second program example. Python
# will automatically close the .txt file for you. You can create a notepad file, and then
# save it in the same folder as your Python program with these program examples
# below to see how they work. This is my notepad file's text message: Computer
# Science is Soo Much Fun!!. I named the notepad file as Computer Science.txt;
# notepad will create the .txt extension for you. All you have to do is name the notepad
# file whatever name you wish, and not worry about the .txt extension. However, you
# will need to invoke the .txt extension part of the notepad file name, when using
# Python to open and read notepad files.

notepad_file = open('Computer Science.txt','r')  # .txt extension, 'r' means read

print(notepad_file.read())  # Computer Science is Soo Much Fun!! is read from notepad.txt file text.

notepad_file.close()

# or this:

with open('Computer Science.txt') as notepad_file:
          print(notepad_file.read())  # Computer Science is Soo Much Fun!! is read from notepad.txt file text.

# You can assign variables to create clean, cut code.

text = 'Computer Science.txt'

notepad_file = open(text,'r')  # .txt extension, 'r' means read

print(notepad_file.read())  # Computer Science is Soo Much Fun!! is read from notepad.txt file text.

notepad_file.close()

# or this:

text = 'Computer Science.txt'

with open(text) as notepad_file:
          print(notepad_file.read())  # Computer Science is Soo Much Fun!! is read from notepad.txt file text.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use Python to write to .txt files, such as notepad files.

notepad_file = open('Computer Science.txt','w')  # .txt extension, 'w' means write

print(notepad_file.write('Welcome to Python World'))

notepad_file.close()

# or this:

with open('Computer Science.txt','w') as notepad_file:
          print(notepad_file.write('Welcome to Python World'))

# You can assign variables to create clean, cut code.

text1 = 'Computer Science.txt','w'
text2 = 'Welcome to Python World'

notepad_file = open(text1)  # .txt extension, 'w' means write

print(notepad_file.write(text2))

notepad_file.close()

# or this:

text1 = 'Computer Science.txt','w'
text2 = 'Welcome to Python World'

with open(text1,'w') as notepad_file:
          print(notepad_file.write(text2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use Python to append/add text to .txt files, such as notepad files.

notepad_file = open('Computer Science.txt','a')  # .txt extension, 'a' means append

print(notepad_file.write('\nPython is Cool!!'))

notepad_file.close()

# or this:

with open('Computer Science.txt','a') as notepad_file:
          print(notepad_file.write('\nPython is Cool!!'))

# You can assign variables to create clean, cut code.

text1 = 'Computer Science.txt'
text2 = '\nPython is Cool!!'

notepad_file = open(text1,'a')  # .txt extension, 'a' means append

print(notepad_file.write(text2))

notepad_file.close()

# or this:

text1 = 'Computer Science.txt'
text2 = '\nPython is Cool!!'

with open(text1,'a') as notepad_file:
          print(notepad_file.write(text2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use Python to copy .txt files, such as notepad files. You must import the 'shutil' module.

import shutil

shutil.copyfile('Computer Science.txt','King Python.txt')  # .txt extension

# You can assign variables to create clean, cut code.

text1 = 'Computer Science.txt'
text2 = 'King Python.txt'

shutil.copyfile(text1,text2)  # .txt extension
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Delete/remove a .txt file, via the remove() function. You must import the 'os' module.

import os

os.remove('Computer Science.txt')  # .txt extension

# You can assign variables to create clean, cut code.

text = 'Computer Science.txt'

os.remove(text)  # .txt extension
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Walrus Operator Python program example.

# Use the := Walrus Operator to create the following Python prgram examples, using
# tuples(), lists[] and dictionaries{}.

if my_tuple := (
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5'):pass

for value in my_tuple:print(value)

if my_list := [
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5']:pass

for value in my_list:print(value)

if my_dictionary := {
    1:'Value 1',2:'Value 2',3:'Value 3',
    4:'Value 4',5:'Value 5',6:'Value 6'}:pass

for value in my_dictionary:print(
    my_dictionary.get(value+1,f"There are no more values to loop \
through after 'Value {value}'."))

# Look what you can do with Python's print() function.

# Use three single ''' quotes to make string concatenation much easier and much more
# text oriented.

print('''That's 'GREAT' to "TRIPPLE QUOTES" ''')

# Use three double " quote marks to make string concatenation much easier and much
# more text oriented.

print("""That's 'GREAT' to "TRIPPLE QUOTES" """)

# Use Python's Error Handlers to not only stop errors from occurring. But you can also
# use Error Handlers to manipulate Python code flow of control. As you may notice, I used
# the walrus := operator to write less lines of code. Play around with the values within these
# program examples and call wrong indexes, and wrong strings together to force these
# exception handlers to do their work, which is to stop programs from crashing, and they
# are also used for program manipulation purposes to change program flow control.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# The 'pass' prefix is for code place holding if you don't wish to write any code blocks
# underneath expressions that use code blocks, such as the Python program above shows
# in our first example.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Without the use of the walrus := operator.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# With the 'pass' prefix placeholder for code blocks.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Let's use one 'try:' and two exception handlers, alongside the walrus := operator. We will
# use one 'IndexError:' handler and one 'TypeError:' handler to create some programming
# manipulation within our Python program examples below.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
        print(x[4]+'character string')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')

# Python executes/runs its programs from the top downward, as the very same way you
# can see the code order. Each instruction is first to execute, is the first to be serviced.
# In most cases multiple exception handlers can only execute one or the other, depending
# on the code order.

if x := (0,1,2,3,4,5):
    try:
        print(x[4]+'character string text.')
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')

# Use the := Walrus Operator to temporarily check for values in tuples, lists, dictionaries
# and sets. That way, you can be a bit lazy and not have to write two lines of code only to
# check for values. Note: default tuples won't work with the := walrus operator for indexing.
# Python cannot seem to see the values as either strings, nor integers when using the :=
# walrus operator.

print(x := 1,2,3,4,5,6,7,8,9)  # x creates a default tuple of values

print(x[0]) # TypeError: 'int' object is not subscripted

print(x := (1,2,3,4,5,6,7,8,9))  # x creates a tuple of values

print(x[0]) # tuple index[0] is the value '1'

print(x := [1,2,3,4,5,6,7,8,9])  # x creates a list of values

print(x[0]) # list index[0] is the value '1'

print(x := {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9})  # x creates a dictionary of values

print(x.get(1,'Not Found!'))

print(x := {1,2,3,4,5,6,7,8,9})  # x creates a set of values

x = sum([1,2,3,4,5,6,7,8,9])
y = sum([10,11,12,13,14,15,16,17,18,19])

print(f'x = {x} and y = {y}. x+y = {x+y}') # x = 45 and y = 145. x+y = 190

# Here is something else we can do with the Walrus := operator. Here are two Python program
# examples that will show you the 'if' statement, using the none walrus := operator, and the
# use of the walrus := operator with the 'if' statement.

x = 3

if x == 3:print(x)

# Notice how the very same Python code above is exactly the very same Python code as
# below. As you can clearly see, the walrus := operator reduces the usual two lines of
# Python code down to just one, single line of Python code.

if x := 3:print(x) # the walrus := operator makes x act as if it were named first.

# You don't have to create a variable first, to then place it within an
# 'if' statement using the walrus := operator.

# Welcome to the the split() function. This split() function has a dot '. ' in front of it that
# joins the variable, 'poem' to the split() function using another variable called, 'text'.
# What the split() function does is turns any text paragraphs into an actual list of words,
# which you can then use their indexes [index] to pick out words within the poem.

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

# For example: the first word in the poem is 'Knowledge', which is index[0] with the single
# quote marks as in no spaces in between them or the word Knowledge. Any words thereafter
# doesn't have quote marks; only the title of the poem as in normal poems, sometimes you
# want quote marks in a title or word/words alike.

text = poem.split()

print(text[0]) # index[0] is the word with single quote marks: 'Knowledge'

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

# Here, we can use Python's Walrus Operator := to check our list of words within the poem
# right on the spot and on one, single line of Python code# at that.

print(text := poem.split())

# Here is the old way, I taught you, as others had taught you. Let's check our list of words
# without the help of the walrus := operator and see how we have to use two lines of Python
# code to create the same thing as we did above using the walrus := operator. When you
# are happy with your list of words, you can throw away only one line of Python code, instead
# throwing away two lines of Python code. The walrus := operator makes this a single line
# snap that you can just throw away one line of Python code.

text = poem.split()

print(text)

# Now that I'm happy with my list. I can start picking out words, via their indexes.

print(text[1]) # index[1] is the word: is

# Let's use a for loop to call up all the words to the poem, without showing ugly commas
# ' , ' and index[ ] brackets.

for i in text:print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python scoping with strings and integer values.

print(type('string'))

# <class 'str'>

print(type(2))

# <class 'int'>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# View string functions and string methods. These dir(n) functions reveal a list of dunder
# methods. Some of these dunder methods are shown in the following example. Note:
# dunder methods are mainly used as class constructors, that tells the class how to
# behave, with the given data attributes, such as text strings and integer numbers.

print(dir('string'))

# View integer fuctions and integer methods.

print(dir(2))

# Get the id from a string.

print(id('string'))

# Get the id from an integer.

print(id(2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These two 'print' statements below use the dunder method 'add', which is the same
# as the 'print' statements 'print(2+3)' and 'print('a'+'b')'. The 'int' function adds only
# integer numbers together, whereas the str' function concatenates/joins character
# strings together.

print(int.__add__(2,3))

# Screen output:	5

print(str.__add__('a','b'))

# Screen output:	ab
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use dunder methods to do math calculations within print() functions.

print(int.__add__(8,2))  # 10

print(int.__sub__(8,2))  # 6

print(int.__mul__(8,2))  # 16

print(int.__divmod__(8,2))  # (4, 0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do a quick recap on define() functions, so we can learn what classes are and
# how define() functions become instances, within a class, called class objects. We
# will use these programming examples below so can learn what classes are all about.

def return_message():
        return 'Returned Message 1','Returned Message 2','Returned Message 3'

message = return_message()[1]

print(message)  # Returned Message 2

# or this:

def return_message():
        return 'Returned Message 1','Returned Message 2','Returned Message 3'

message = return_message()

print(message[1])  # Returned Message 2

# or this:

def return_message(message1,message2,message3):
        return message1,message2,message3

message = return_message('Returned Message 1','Returned Message 2','Returned Message 3')[1]

print(message)  # Returned Message 2

# or this:

def return_message(message1,message2,message3):
        return message1,message2,message3

message = return_message('Returned Message 1','Returned Message 2','Returned Message 3')

print(message[1])  # Returned Message 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_answer():
        return 6+2+3

answer = return_answer()

print(answer)  # 11

# or this:

def return_answer(num1,num2,num3):
        return num1+num2+num3

answer = return_answer(6,2,3)

print(answer)  # 11
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Classes are objects and define() functions are instances of class objects. Note:
# classes do not need return functions to work. However, they do need define functions
# to work properly, nonetheless. These class examples below show the use of return
# define() function values, so the define() function can do more instances, instead of
# just one. This return function is also a Message class object by itself. With the use
# of return define() functions, we can return values directly to print() functions outside
# the define() function block, without calling the actual define() function to execute/run
# any Python code inside it. return define functions are great for returning values
# through class objects.

class Message:

  def return_message():
    return 'Returned Message 1','Returned Message 2','Returned Message 3'

print(Message.return_message()[0])  # Returned Message 1

print(Message.return_message()[1])  # Returned Message 2

print(Message.return_message()[2])  # Returned Message 3

# or this:

class Message:

  def return_message():
    return 'Returned Message 1','Returned Message 2','Returned Message 3'

message1 = Message.return_message()[0]   # Returned Message 1
message2 = Message.return_message()[1]   # Returned Message 2
message3 = Message.return_message()[2]   # Returned Message 3

print(message2)   # Returned Message 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Classes are objects and define() functions are instances of class objects.

class Math:

  def return_answer():
    return 6+2+3

print(Math.return_answer())  # 11

# or this:

class Math:

  def return_answer(num1,num2,num3):
    return num1+num2+num3

answer = Math.return_answer(6,2,3)

print(answer)  # 11
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These two class object examples show how class objects do not need return define()
# functions to work properly. However, class do need define() functions to work properly,
# nonetheless, as illustrated here:

class Message:

  def message():
    print('This is a text string value inside this message define() function block.')

text = Message.message

text()  # This is a text string value inside this message define() function block.

class Math:

  def answer():
    print(6+2+3)

numbers = Math.answer

numbers()  # This is a text string value inside this message define() function block.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now create really cool classes and class objects to learn how they truly work.

# These define() functions are instances within this Animals class. This class below is
# what Object Oriented Programming in Python is truly all about.

class Animals:

  def dog():
    print('This is a German Shepherd.')

  def cat():
    print('This is a Taby')

  def bird():
    print('This is Macaw')

  def fish():
      print('This is a Pleco')

Animals.dog()  # This is a German Shepherd.
Animals.cat()  # This is a Taby
Animals.bird()  # This is Macaw
Animals.fish()  # This is a Pleco

# Let's create a Math class act that has math calculation instances within it. Note:
# invoke the int() function to create integer numbers only. You can also try the
# float() function to create floating-point numbers.

class Math:

  def addition():
    print(int(6+2+3))

  def subtraction():
    print(int(6-2-3))

  def multiplication():
    print(int(6*2*3))

  def division():
      print(int(6/2/3))

Math.addition()  # 11
Math.subtraction()  # 1
Math.multiplication()  # 36
Math.division()  # 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Animals:

  def dog():
    return 'This is a German Shepherd.'

  def cat():
    return 'This is a Taby'

  def bird():
    return 'This is Macaw'

  def fish():
    return 'This is a Pleco'

print(Animals.dog())  # This is a German Shepherd.
print(Animals.cat())  # This is a Taby
print(Animals.bird())  # This is Macaw
print(Animals.fish())  # This is a Pleco

# Let's do the same thing with our Math class act.

class Math:

  def addition():
    return int(6+2+3)

  def subtraction():
    return int(6-2-3)

  def multiplication():
    return int(6*2*3)

  def division():
      return int(6/2/3)

print(Math.addition())  # 11
print(Math.subtraction())  # 1
print(Math.multiplication())  # 36
print(Math.division())  # 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create return define() functions so we can use their returned values outside
# their define() functions, via the print() function. We will use class constructors, called
# magic methods or better known as dunder methods. The '__init__' initialize constructor
# allows the class to talk to its attribute properties, such as self,animal for example.
# The 'self' attribute calls itself to call the class constructor, along with its attributes
# and attribute properties alike.

class Animals:

  def __init__(self,animal):

    self.animal = animal

  def pets(animal):
    return animal

print(Animals.pets('This is a German Shepherd.'))

# or this:

animals_class = Animals.pets('This is a German Shepherd.')

print(animals_class)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Math:

  def __init__(self,num):

    self.num = num

  def addition(num):
    return num

print(int(Math.addition(6+2+3)))

# or this:

math_class = int(Math.addition(6+2+3))

print(math_class)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's broaden our understanding and invoke more class attribute properties that
# can be returned through the pets() define function. Note: You can call each returned
# value by its index[n] number: 0, 3.

class Animals:

  def __init__(self,animal1,animal2,animal3,animal4):

    self.animal1 = animal1
    self.animal2 = animal2
    self.animal3 = animal3
    self.animal4 = animal4

  def pets(animal1,animal2,animal3,animal4):
    return animal1,animal2,animal3,animal4

print(Animals.pets('This is a German Shepherd.','This is a Taby','This is Macaw','This is a Pleco')[0])
print(Animals.pets('This is a German Shepherd.','This is a Taby','This is Macaw','This is a Pleco')[1])
print(Animals.pets('This is a German Shepherd.','This is a Taby','This is Macaw','This is a Pleco')[2])
print(Animals.pets('This is a German Shepherd.','This is a Taby','This is Macaw','This is a Pleco')[3])

# this:

print(Animals.pets(
  'This is a German Shepherd.',
  'This is a Taby','This is Macaw',
  'This is a Pleco')[0])

# or this:

animals_class = Animals.pets(
  'This is a German Shepherd.',
  'This is a Taby','This is Macaw',
  'This is a Pleco')[0]

print(animals_class)

# or this:

animals_class = Animals.pets(
  'This is a German Shepherd.',
  'This is a Taby','This is Macaw',
  'This is a Pleco')

print(animals_class[0])
print(animals_class[1])
print(animals_class[2])
print(animals_class[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a class that calculates returned values. Let's invoke more class attribute
# properties like we did before with the Animals class act.

class Math:

  def __init__(self,num1,num2,num3,num4):

    self.num = num1
    self.num = num2
    self.num = num3
    self.num = num4

  def addition(num1,num2,num3,num4):
    return int(num1+num2+num3+num4)

print(Math.addition(6,2,3,1))
print(Math.addition(4,8,5,3))
print(Math.addition(9,9,2,5))
print(Math.addition(5,3,2,10))

# or this:

math_class1 = Math.addition(6,2,3,1)
math_class2 = Math.addition(4,8,5,3)
math_class3 = Math.addition(9,9,2,5)
math_class4 = Math.addition(5,3,2,10)

print(math_class2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can have as many return define() functions as you please within a class; only
# two return define() functions are shown in this Python program example.

class Animals:

  def __init__(self,animal1,animal2,animal3,animal4):

    self.animal1 = animal1
    self.animal2 = animal2
    self.animal3 = animal3
    self.animal4 = animal4

  def pets(animal1,animal2,animal3,animal4):
    return animal1,animal2,animal3,animal4

  def wild(animal1,animal2,animal3,animal4):
    return animal1,animal2,animal3,animal4

animal_pets = Animals.pets(
  'This is a German Shepherd.',
  'This is a Taby.','This is Macaw.',
  'This is a Pleco.')

animal_wild = Animals.wild(
  'This is a Wolf.','This is a Tiger.',
  'This is Hawk.','This is a Shark.')

print(animal_pets[0])

print(animal_wild[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# With classes, you can create mathematical objects with return define() functions
# that can be called outside the actual define() function blocks and directly into
# print() functions that reside outside, both the class block and the return define()
# function block. Just remember that the 'return' statement means to return a value
# or result of a define() function outside the define function block, via the print()
# function.

class Math:

  def __init__(self,num1,num2,num3,num4):

    self.num = num1
    self.num = num2
    self.num = num3
    self.num = num4

  def addition(num1,num2,num3,num4):
    return int(num1+num2+num3+num4)

  def subtraction(num1,num2,num3,num4):
    return int(num1-num2-num3-num4)

  def multiplication(num1,num2,num3,num4):
    return int(num1*num2*num3*num4)

  def division(num1,num2,num3,num4):
    return int(num1/num2/num3/num4)

math_addition = Math.addition(20,10,5,5)
math_subtraction = Math.subtraction(40,20,10,5)
math_multiplication = Math.multiplication(2,2,5,2)
math_division = Math.division(40,2,2,1)

print(math_addition)  # 40

print(math_subtraction)  # 5

print(math_multiplication)  # 40

print(math_division)  # 10
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use what we've learned so far about classes and create different kinds of
# define() functions within the class object. We will create return define functions and
# define() functions without the 'return' statement, and to see how they behave; the
# way each define() function handles values and their results.

class Class_object_mix:

  def __init__(self,num1,num2,num3,num4):

    self.num = num1
    self.num = num2
    self.num = num3
    self.num = num4

  def animal_pets(animal1,animal2,animal3,animal4):
    return animal1,animal2,animal3,animal4

  def animal_wild():
    print('This is a Wolf.')

  def addition(num1,num2,num3,num4):
    return int(num1+num2+num3+num4)

  def subtraction():
    print(int(40-20-10-5))

  def multiplication(num1,num2,num3,num4):
    return int(num1*num2*num3*num4)

  def division(num1,num2,num3,num4):
    return int(num1/num2/num3/num4)

animal_pet = Class_object_mix.animal_pets(
  'This is a German Shepherd.',
  'This is a Taby','This is Macaw',
  'This is a Pleco')

animal_wild = Class_object_mix.animal_wild

math_addition = Class_object_mix.addition(20,10,5,5)
math_subtraction = Class_object_mix.subtraction
math_multiplication = Class_object_mix.multiplication(2,2,5,2)
math_division = Class_object_mix.division(40,2,2,1)

print(animal_pet[0])

animal_wild()

print(math_addition)

math_subtraction()

print(math_multiplication)
print(math_division)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use our knowledge about classes and let's create what is called, a class inheritance.
# Classes can share and use attribute properties from other classes, hence class inheritance.
# It's the Child_class act that contains the attribute properties from both the Mom_class
# and the Dad_class acts. However, classes can have more than one child class act.
# Classes can also have more than two parent class acts. Take a look at the synapses
# of this class inheritance Python program example. All we need to do now is create
# class constructors, along with class constructor attribute properties as we had learned.

class Mom_class:
  def text1():
    print('I am in the Mom class act.')

class Dad_class:
  def text2():
    print('I am in the Dad class act.')

# The Child_class inherits all the properties from the Mom_class and the Dad_class acts.

class Child_class(Mom_class,Dad_class):
  pass

Mom_class.text1()

Dad_class.text2()

Child_class.text1()

Child_class.text2()

# You can also give parent class and child class acts their own properties.

class Child_class(Mom_class,Dad_class):
  def name():
    print('My name is Billy The Child!')

Child_class.name()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's invoke the '__init__' initialize constructor to create class attribute properties.
# In this Python program example below, the Mom and Dad classes each have one,
# single attribute property only. The 'self' attribute calls itself to call the class constructor,
# along with its attributes and attribute properties alike. And, remember that return
# define() functions return values directly into print() functions outside the actual define()
# functions themselves. Now, let's expand our understanding and add more class
# attribute properties to each class act.

class Mom_class_attributes:

  def __init__(self,mom1,mom2,mom3,mom4):

    self.mom1 = mom1
    self.mom2 = mom2
    self.mom3 = mom3
    self.mom4 = mom4

  def mom(mom1,mom2,mom3,mom4):
      return mom1,mom2,mom3,mom4

class Dad_class_attributes:

  def __init__(self,dad1,dad2,dad3,dad4):

    self.dad1 = dad1
    self.dad2 = dad2
    self.dad3 = dad3
    self.dad4 = dad4

  def dad(dad1,dad2,dad3,dad4):
      return dad1,dad2,dad3,dad4

class Child_class_inheritance(Mom_class_attributes,Dad_class_attributes):
  pass

mom_class_act = Mom_class_attributes.mom(
  'I am the returned text value message from the Mom_class attribute: mom1.',
  'I am the returned text value message from the Mom_class attribute: mom2.',
  'I am the returned text value message from the Mom_class attribute: mom3.',
  'I am the returned text value message from the Mom_class attribute: mom4.')

dad_class_act = Dad_class_attributes.dad(
  'I am the returned text value message from the Dad_class attribute: dad1.',
  'I am the returned text value message from the Dad_class attribute: dad2.',
  'I am the returned text value message from the Dad_class attribute: dad3.',
  'I am the returned text value message from the Dad_class attribute: dad4.')

child_class_act1 = Child_class_inheritance.mom(
  'I am the returned text value message from the child_class attribute: mom1.',
  'I am the returned text value message from the child_class attribute: mom2.',
  'I am the returned text value message from the child_class attribute: mom3.',
  'I am the returned text value message from the child_class attribute: mom4.')

child_class_act2 = Child_class_inheritance.dad(
  'I am the returned text value message from the child_class attribute: dad1.',
  'I am the returned text value message from the child_class attribute: dad2.',
  'I am the returned text value message from the child_class attribute: dad3.',
  'I am the returned text value message from the child_class attribute: dad4.')

print(mom_class_act[0])  # 'I am the returned text value message from the Mom_class attribute: mom1.

print(dad_class_act[0])  # 'I am the returned text value message from the Mad_class attribute: dad1.

print(child_class_act1[0])  # I am the returned text value message from the child_class attribute: mom1.

print(child_class_act2[0])  # I am the returned text value message from the child_class attribute: dad1.

# You can also give parent class and child class acts their own properties.

class Child_class_inheritance(Mom_class_attributes,Dad_class_attributes):

  def name():
    print('My name is Billy The Child!')

Child_class_inheritance.name()  # My name is Billy The Child!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now create similar classes that calculates attribute properties and returns the
# result of values outside the define() functions, and directly into print() functions.

class Math_class_attributes_addition:

  def __init__(self,num1,num2,num3,num4):

    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    self.num4 = num4

  def addition(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_subtraction:

  def __init__(self,num1,num2,num3,num4):

    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    self.num4 = num4

  def subtraction(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_multiplication:

  def __init__(self,num1,num2,num3,num4):

    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    self.num4 = num4

  def multiplication(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_division:

  def __init__(self,num1,num2,num3,num4):

    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    self.num4 = num4

  def division(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_inheritance(
  Math_class_attributes_addition,Math_class_attributes_subtraction,
  Math_class_attributes_multiplication,Math_class_attributes_division):
  pass

math_class_act1 = Math_class_attributes_addition.addition(20+10+5+5, 40+20+10+5, 2+2+5+2, 40+2+2+1)
math_class_act2 = Math_class_attributes_subtraction.subtraction(20-10-5-5, 40-20-10-5, 2-2-5-2, 40-2-2-1)
math_class_act3 = Math_class_attributes_multiplication.multiplication(20*10*5*5, 40*20*10*5, 2*2*5*2, 40*2*2*1)
math_class_act4 = Math_class_attributes_division.division(20/10/5/5, 40/20/10/5, 2/2/5/2, 40/2/2/1)

print(int(math_class_act1[0]))  # 40

print(int(math_class_act2[0]))  # 0

print(int(math_class_act3[0]))  # 5000

print(math_class_act4[0])  # 0.08

# You can also give parent class and child class acts their own properties.

class Math_class_inheritance(
  Math_class_attributes_addition,Math_class_attributes_subtraction,
  Math_class_attributes_multiplication,Math_class_attributes_division):

  def name():
    print('My name is Billy The Child!')

Math_class_inheritance.name()  # My name is Billy The Child!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to use the super() function within class attribute properties. If there
# are two or more classes that have the same attribute variable names, the super()
# function can be used on classes, underneath other classes that have the same
# attribute variable names, such as these:

#   self.num1 = num1
#   self.num2 = num2
#   self.num3 = num3
#   self.num4 = num4

# What the super() function does is help the programmer reuse code, not rewrite it.
# Since all the classes have the same attribute variable names, this is where the super()
# function truly shines. This is what the super() function looks like with its class attribute
# properties inside it. Note: If you have different attribute variable names in each class,
# the super() function cannot be used; they are not the same attribute variable names,
# such was the case in our Mom and Dad class act Python program example.

# super().__init__(num1,num2,num3,num4)

class Math_class_attributes_addition:

  def __init__(self,num1,num2,num3,num4):

    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    self.num4 = num4

  def addition(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_subtraction:

  def __init__(self,num1,num2,num3,num4):
    super().__init__(num1,num2,num3,num4)

  def subtraction(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_multiplication:

  def __init__(self,num1,num2,num3,num4):
    super().__init__(num1,num2,num3,num4)

  def multiplication(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_division:

  def __init__(self,num1,num2,num3,num4):
      super().__init__(num1,num2,num3,num4)

  def division(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_inheritance(
  Math_class_attributes_addition,Math_class_attributes_subtraction,
  Math_class_attributes_multiplication,Math_class_attributes_division):
  pass

math_class_act1 = Math_class_attributes_addition.addition(20+10+5+5, 40+20+10+5, 2+2+5+2, 40+2+2+1)
math_class_act2 = Math_class_attributes_subtraction.subtraction(20-10-5-5, 40-20-10-5, 2-2-5-2, 40-2-2-1)
math_class_act3 = Math_class_attributes_multiplication.multiplication(20*10*5*5, 40*20*10*5, 2*2*5*2, 40*2*2*1)
math_class_act4 = Math_class_attributes_division.division(20/10/5/5, 40/20/10/5, 2/2/5/2, 40/2/2/1)

print(int(math_class_act1[0]))  # 40

print(int(math_class_act2[0]))  # 0

print(int(math_class_act3[0]))  # 5000

print(math_class_act4[0])  # 0.08

# You can also give parent class and child class acts their own properties.

class Math_class_inheritance(
  Math_class_attributes_addition,Math_class_attributes_subtraction,
  Math_class_attributes_multiplication,Math_class_attributes_division):

  def name():
    print('My name is Billy The Child!')

Math_class_inheritance.name()  # My name is Billy The Child!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now learn how to add attribute variables to super() functions. These are easy
# peasy. If we want to have more attribute properties within a class, we can do this:

class Math_class_attributes_addition:

  def __init__(self,num1,num2,num3,num4):

    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
    self.num4 = num4

  def addition(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_subtraction:

  def __init__(self,num1,num2,num3,num4,num5): # Add the num5 attribute variable here.
    super().__init__(num1,num2,num3,num4)

    self.num5 = num5  # Create the attribute property for num5

  def subtraction(num1,num2,num3,num4,num5):  # Add the num5 attribute variable here.
      return num1,num2,num3,num4,num5  # Add the num5 attribute variable here.

class Math_class_attributes_multiplication:

  def __init__(self,num1,num2,num3,num4):
    super().__init__(num1,num2,num3,num4)

  def multiplication(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_attributes_division:

  def __init__(self,num1,num2,num3,num4):
      super().__init__(num1,num2,num3,num4)

  def division(num1,num2,num3,num4):
      return num1,num2,num3,num4

class Math_class_inheritance(
  Math_class_attributes_addition,Math_class_attributes_subtraction,
  Math_class_attributes_multiplication,Math_class_attributes_division):
  pass

math_class_act1 = Math_class_attributes_addition.addition(20+10+5+5, 40+20+10+5, 2+2+5+2, 40+2+2+1)
math_class_act2 = Math_class_attributes_subtraction.subtraction(20-10-5-5, 40-20-10-5, 2-2-5-2, 40-2-2-1,'Hurray! You did it!')
math_class_act3 = Math_class_attributes_multiplication.multiplication(20*10*5*5, 40*20*10*5, 2*2*5*2, 40*2*2*1)
math_class_act4 = Math_class_attributes_division.division(20/10/5/5, 40/20/10/5, 2/2/5/2, 40/2/2/1)

print(int(math_class_act1[0]))  # 40

print(int(math_class_act2[0]))  # 0

print(math_class_act2[4])  # Hurray! You did it!

print(int(math_class_act3[0]))  # 5000

print(math_class_act4[0])  # 0.08

# You can also give parent class and child class acts their own properties.

class Math_class_inheritance(
  Math_class_attributes_addition,Math_class_attributes_subtraction,
  Math_class_attributes_multiplication,Math_class_attributes_division):

  def name():
    print('My name is Billy The Child!')

Math_class_inheritance.name()  # My name is Billy The Child!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# And before we go, I have just one more Python programming exercise. Believe me,
# this Monster Class Act really took me out for a complete spin and back. This is one
# of my hardest things, I had ever problem solved with computer programming, since
# I started Python back on Christmas day, 2017. All I can say is when I first started
# Python, it looked very confusing without actual line numbers to tell the code where
# to go to, and act like a normal subroutine. That wouldn't come until much later, when
# I finally just kept on tinkering with define() functions, and when I put a conditional
# while loop into the mix, I had finally found my subroutine solution. Define() functions
# and classes can call other define() functions and classes. However, you must include
# the class variable name, followed by a period '.' and, then call the define() function
# variable name. For example: 'Math_class_attributes_division.division'. It's now time
# to take a much needed break. Because believe me, you will need it after this Monster
# Class Act Python program exercise. All I can say, it's Head Banging time. Good Luck!

# The very first thing we must do here is, create as many variables and their values as
# we need them. Creating variables helps to keep the spaghetti of long string values
# out of the way, while creating this Monster Class Python program. After you create
# your long string values, such as these below, You can then move onto the actual
# code that make these classes and subclasses sing and dance, along with their
# define() function from within them.

main_class = (
    'This is an instance of a main class object with three attribute properties value 1',
    'This is an instance of a main class object with three attribute properties value 2',
    'This is an instance of a main class object with three attribute properties value 3')

subclass1 = (
    'This is an instance of a subclass1 object with three attribute properties value 1',
    'This is an instance of a subclass1 object with three attribute properties value 2',
    'This is an instance of a subclass1 object with three attribute properties value 3')

subclass2 = (
    'This is an instance of a subclass2 object with three attribute properties value 1',
    'This is an instance of a subclass2 object with three attribute properties value 2',
    'This is an instance of a subclass2 object with three attribute properties value 3')

super_subclass1 = (
     'This is an instance of a super subclass1 object with four attribute properties value 1',
     'This is an instance of a super subclass1 object with four attribute properties value 2',
     'This is an instance of a super subclass1 object with four attribute properties value 3',
     'This is an instance of a super subclass1 object with four attribute properties value 4')

super_subclass2 = (
     'This is an instance of a super subclass2 object with five attribute properties value 1',
     'This is an instance of a super subclass2 object with five attribute properties value 2',
     'This is an instance of a super subclass2 object with five attribute properties value 3',
     'This is an instance of a super subclass2 object with five attribute properties value 4',
     'This is an instance of a super subclass2 object with five attribute properties value 5')

super_subclass3 = (
     'This is an instance of a super subclass3 object with five attribute properties value 1',
     'This is an instance of a super subclass3 object with five attribute properties value 2',
     'This is an instance of a super subclass3 object with five attribute properties value 3',
     'This is an instance of a super subclass3 object with five attribute properties value 4',
     'This is an instance of a super subclass3 object with five attribute properties value 5',
     'This is an instance of a super subclass3 object with five attribute properties value 6')

super_subclass4 = (
     'This is an instance of a super subclass4 object with seven attribute properties value 1',
     'This is an instance of a super subclass4 object with seven attribute properties value 2',
     'This is an instance of a super subclass4 object with seven attribute properties value 3',
     'This is an instance of a super subclass4 object with seven attribute properties value 4',
     'This is an instance of a super subclass4 object with seven attribute properties value 5',
     'This is an instance of a super subclass4 object with seven attribute properties value 6',
     'This is an instance of a super subclass4 object with seven attribute properties value 7')

super_subclass5 = (
     'This is an instance of a super subclass5 object with eight attribute properties value 1',
     'This is an instance of a super subclass5 object with eight attribute properties value 2',
     'This is an instance of a super subclass5 object with eight attribute properties value 3',
     'This is an instance of a super subclass5 object with eight attribute properties value 4',
     'This is an instance of a super subclass5 object with eight attribute properties value 5',
     'This is an instance of a super subclass5 object with eight attribute properties value 6',
     'This is an instance of a super subclass5 object with eight attribute properties value 7',
     'This is an instance of a super subclass5 object with eight attribute properties value 8')

super_subclass6 = (
     'This is an instance of a super subclass6 object with nine attribute properties value 1',
     'This is an instance of a super subclass6 object with nine attribute properties value 2',
     'This is an instance of a super subclass6 object with nine attribute properties value 3',
     'This is an instance of a super subclass6 object with nine attribute properties value 4',
     'This is an instance of a super subclass6 object with nine attribute properties value 5',
     'This is an instance of a super subclass6 object with nine attribute properties value 6',
     'This is an instance of a super subclass6 object with nine attribute properties value 7',
     'This is an instance of a super subclass6 object with nine attribute properties value 8',
     'This is an instance of a super subclass6 object with nine attribute properties value 9')

super_subclass7 = (
     'This is an instance of a super subclass7 object with ten attribute properties value 1',
     'This is an instance of a super subclass7 object with ten attribute properties value 2',
     'This is an instance of a super subclass7 object with ten attribute properties value 3',
     'This is an instance of a super subclass7 object with ten attribute properties value 4',
     'This is an instance of a super subclass7 object with ten attribute properties value 5',
     'This is an instance of a super subclass7 object with ten attribute properties value 6',
     'This is an instance of a super subclass7 object with ten attribute properties value 7',
     'This is an instance of a super subclass7 object with ten attribute properties value 8',
     'This is an instance of a super subclass7 object with ten attribute properties value 9',
     'This is an instance of a super subclass7 object with ten attribute properties value 10')

return_values = (
    '"The Main Class Act"',
    'Subclass Act One.',
    'Subclass Act Two',
    'Super Subclass Act One',
    'Super Subclass Act Two',
    'Super Subclass Act Three',
    'Super Subclass Act Four',
    'Super Subclass Act Five',
    'Super Subclass Act Six',
    'Super Subclass Act Seven')

# This is where you do your Clean, Cut Python Code, without all that spaghetti of
# long string values getting in the way while you continue to write your code code.

class Main_class_attribute_properties:

    def return_function():
        return return_values

    def __init__(self,attribute1,attribute2,attribute3):

        self.attribute1=attribute1
        self.attribute2=attribute2
        self.attribute3=attribute3

class Subclass1_same_attribute_properties(  # inhert main class attribute properties only
    Main_class_attribute_properties):pass

class Subclass2_same_attribute_properties(  # inhert main class attribute properties only
    Main_class_attribute_properties):pass

class Super_subclass1_new_attribute_properties(
    Subclass1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1, attribute2,attribute3)

        self.attribute4=attribute4

class Super_subclass2_new_attribute_properties(
    Super_subclass1_new_attribute_properties,
    Subclass2_same_attribute_properties,
    Subclass1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5):

        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.attribute5=attribute5

class Super_subclass3_new_attribute_properties(
    Super_subclass2_new_attribute_properties,
    Super_subclass1_new_attribute_properties,
    Subclass2_same_attribute_properties,
    Subclass1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5)

        self.attribute6=attribute6

class Super_subclass4_new_attribute_properties(
    Super_subclass3_new_attribute_properties,
    Super_subclass2_new_attribute_properties,
    Super_subclass1_new_attribute_properties,
    Subclass2_same_attribute_properties,
    Subclass1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6)

        self.attribute7=attribute7

class Super_subclass5_new_attribute_properties(
    Super_subclass4_new_attribute_properties,
    Super_subclass3_new_attribute_properties,
    Super_subclass2_new_attribute_properties,
    Super_subclass1_new_attribute_properties,
    Subclass2_same_attribute_properties,
    Subclass1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7)

        self.attribute8=attribute8

class Super_subclass6_new_attribute_properties(
    Super_subclass5_new_attribute_properties,
    Super_subclass4_new_attribute_properties,
    Super_subclass3_new_attribute_properties,
    Super_subclass2_new_attribute_properties,
    Super_subclass1_new_attribute_properties,
    Subclass2_same_attribute_properties,
    Subclass1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8,

        attribute9):
        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7,attribute8)

        self.attribute9=attribute9

class Super_subclass7_new_attribute_properties(
    Super_subclass6_new_attribute_properties,
    Super_subclass5_new_attribute_properties,
    Super_subclass4_new_attribute_properties,
    Super_subclass3_new_attribute_properties,
    Super_subclass2_new_attribute_properties,
    Super_subclass1_new_attribute_properties,
    Subclass2_same_attribute_properties,
    Subclass1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8,
        attribute9,attribute10):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7,attribute8,
            attribute9)

        self.attribute10=attribute10

a = Main_class_attribute_properties(main_class[0],main_class[1],main_class[2])

b = Subclass1_same_attribute_properties(subclass1[0],subclass1[1],subclass1[2])

c = Subclass2_same_attribute_properties(subclass2[0],subclass2[1],subclass2[2])

d = Super_subclass1_new_attribute_properties(
    super_subclass1[0],super_subclass1[1],
    super_subclass1[2],super_subclass1[3])

e = Super_subclass2_new_attribute_properties(
    super_subclass2[0],super_subclass2[1],
    super_subclass2[2],super_subclass2[3],
    super_subclass2[4])

f = Super_subclass3_new_attribute_properties(
    super_subclass3[0],super_subclass3[1],
    super_subclass3[2],super_subclass3[3],
    super_subclass3[4],super_subclass3[5])

g = Super_subclass4_new_attribute_properties(
    super_subclass4[0],super_subclass4[1],
    super_subclass4[2],super_subclass4[3],
    super_subclass4[4],super_subclass4[5],
    super_subclass4[6])

h = Super_subclass5_new_attribute_properties(
    super_subclass5[0],super_subclass5[1],
    super_subclass5[2],super_subclass5[3],
    super_subclass5[4],super_subclass5[5],
    super_subclass5[6],super_subclass5[7])

i = Super_subclass6_new_attribute_properties(
    super_subclass6[0],super_subclass6[1],
    super_subclass6[2],super_subclass6[3],
    super_subclass6[4],super_subclass6[5],
    super_subclass6[6],super_subclass6[7],
    super_subclass6[8])

j = Super_subclass7_new_attribute_properties(
    super_subclass7[0],super_subclass7[1],
    super_subclass7[2],super_subclass7[3],
    super_subclass7[4],super_subclass7[5],
    super_subclass7[6],super_subclass7[7],
    super_subclass7[8],super_subclass7[9])

class_attribute_tuple = (

a.attribute1,a.attribute2,a.attribute3,

b.attribute1,b.attribute2,b.attribute3,

c.attribute1,c.attribute2,c.attribute3,

d.attribute1,d.attribute2,d.attribute3,
d.attribute4,

e.attribute1,e.attribute2,e.attribute3,
e.attribute4,e.attribute5,

f.attribute1,f.attribute2,f.attribute3,
f.attribute4,f.attribute5,f.attribute6,

g.attribute1,g.attribute2,g.attribute3,
g.attribute4,g.attribute5,g.attribute6,
g.attribute7,

h.attribute1,h.attribute2,h.attribute3,
h.attribute4,h.attribute5,h.attribute6,
h.attribute7,h.attribute8,

i.attribute1,i.attribute2,i.attribute3,
i.attribute4,i.attribute5,i.attribute6,
i.attribute7,i.attribute8,i.attribute9,

j.attribute1,j.attribute2,j.attribute3,
j.attribute4,j.attribute5,j.attribute6,
j.attribute7,j.attribute8,j.attribute9,
j.attribute10)

return_value = (

    Main_class_attribute_properties.return_function(),

    Subclass1_same_attribute_properties.return_function(),
    Subclass2_same_attribute_properties.return_function(),

    Super_subclass1_new_attribute_properties.return_function(),
    Super_subclass2_new_attribute_properties.return_function(),
    Super_subclass3_new_attribute_properties.return_function(),
    Super_subclass4_new_attribute_properties.return_function(),
    Super_subclass5_new_attribute_properties.return_function(),
    Super_subclass6_new_attribute_properties.return_function(),
    Super_subclass7_new_attribute_properties.return_function())

print(f'\n{return_value[0][0]}\n\n{a.attribute1}')

print(f'\n{return_value[0][1]}\n\n{b.attribute1}')

print(f'\n{return_value[0][2]}\n\n{c.attribute1}')

print(f'\n{return_value[0][3]}\n\n{d.attribute1}')

print(f'\n{return_value[0][4]}\n\n{e.attribute1}')

print(f'\n{return_value[0][5]}\n\n{f.attribute1}')

print(f'\n{return_value[0][6]}\n\n{g.attribute1}')

print(f'\n{return_value[0][7]}\n\n{h.attribute1}')

print(f'\n{return_value[0][8]}\n\n{i.attribute1}')

print(f'\n{return_value[0][9]}\n\n{j.attribute1}')

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

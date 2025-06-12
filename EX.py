def function():
  print('This define function prints text only.')

function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def function_argument(argument):
  print('This define function retrieves one argument',argument)  # non formatted string

function_argument('value.')


def function_argument(argument):
  print('This define function retrieves one argument '+argument)  # non formatted string

function_argument('value.')


def function_argument(argument):
  print('This define function retrieves one argument {}'.format(argument))  # old format string

function_argument('value.')


def function_argument(argument):
  print(f'This define function retrieves one argument {argument}')  # new f' string format

function_argument('value.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def function_argument(argument1,argument2):
  print(f'This define function retrieves two {argument1} {argument2}')

function_argument('argument','values.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def function_argument(argument1,argument2,argument3):
  print(f'This define {argument1} retrieves three {argument2} {argument3}')

function_argument('function','argument','values.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

print('This define function returns one argument {} '.format(return_function(  # old format string
  'argument placeholder value')))


def return_function(argument):
  return 'value.'

print(f'This define function returns one argument \
{return_function ("argument placeholder value")}')  # new f' string format
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(argument1,argument2):
  return 'argument','values.'

print(f'This define function returns two \
{return_function("argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value")[1]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(*args):
  return 'argument','values.'

print(f'This define function returns two \
{return_function("argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value")[1]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(argument1,argument2,argument3):
  return 'argument','values.','WOW!'

print(f'This define function returns three \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[1]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[2]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function(*args):
  return 'argument','values.','WOW!'

print(f'This define function returns three \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[0]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[1]} \
{return_function("argument placeholder value","argument placeholder value","argument placeholder value")[2]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
def return_function(*args):
  return args[0]+args[1]-args[2]*args[3]/args[4]**args[5]

print(return_function(5,4,3,6,3,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

multi_return_function('Done!!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

print(lambda_function(2,12,2,2, 12))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
lambda_function = lambda a,b,x,y,z: a+b-x*y/y == z if z == z else False

print(lambda_function(2,12,2,2, 12))
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
num = 4

lambda_function = lambda x: x if num%2 == 0 else f'{num} is an odd number.'

print(lambda_function(f'{num} is an even number.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
num = 4

lambda_function = lambda x: x if num%2 == 1 else f'{num} is an even number.'

print(lambda_function(f'{num} is an odd number.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
  user_input = int(input('Give me an odd or even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 0 else f'{user_input} is an odd number.'

  print(lambda_function(f'{user_input} is an even number.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
  user_input = int(input('Give me an odd or even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 1 else f'{user_input} is an even number.'

  print(lambda_function(f'{user_input} is an odd number.'))
except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
  user_input = int(input('Give me an even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 0 else 'I want an even number only.'

  print(lambda_function(f'{user_input} is an even number.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
  user_input = int(input('Give me an even number: ').strip())

  lambda_function = lambda x: x if user_input%2 == 1 else f'{user_input} is an even number.'

  print(lambda_function('I want an even number only.'))

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
  user_input = int(input('Give me an odd or even number: ').strip())

  if user_input%2 == 0:
    print(f'{user_input} is an even number.')
  else:
    print(f'{user_input} is an odd number.')

except ValueError:
  print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
# This Python program example is an accidental, Happy Accident. It's probably
# one of my later and one of my most favorite computer programming discoveries
# to happen. I will be using this discovery within my future robotics and Raspberry
# Pi4 Python programs. The '%' modulo operator is fascinating; the things you can
# do with it.

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

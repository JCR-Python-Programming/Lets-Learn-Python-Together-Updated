# The correct 'if', 'elif' and 'else' Python program structure example:

# by Joseph C. Richardson, GitHub.com

# Note: Python executes/runs programs starting from the top,
# downward. Be very careful on how you place statements.
# Some statements cannot execute right, even if they work.
# This is simply because of the order that Python executes/runs
# its program statements.

while True:
  user_input = input('User input: ').strip()  # remove leading and trailing whitespace characters

# lowercase/uppercase characters for Caps Lock and shift keys

  if user_input in ('q','Q'):
    print('I Quit!:')
    break

  elif user_input in ('Good','Great','Perfect'):
    print("That's how it's done!")
    break

  else:
    continue  # continue the while loop iterataion
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# We can use as many 'elif', control flow statements as we wish.

while True:
  user_input = input('User input: ').strip()  # remove leading and trailing whitespace characters

# lowercase/uppercase characters for Caps Lock and shift keys

  if user_input in ('q','Q'):
    print('I Quit!:')
    break

  elif user_input == 'Good':
    print('Good!')
    break

  elif user_input == 'Great':
    print('Great!')
    break

  elif user_input == 'Perfect':
    print('Perfect!')
    break

  else:
    continue  # continue the while loop iterataion
'''----------------------------------------------------------------------'''
# Here is practical 'if', 'elif' and 'else' Python program structure example:

while True:
  user_input = input('Give me the number $10.00 dollars please: ').strip()  # remove leading and trailing whitespace characters

# lowercase/uppercase characters for Caps Lock and shift keys

  if user_input in ('q','Q'):
    print('I Quit!:')
    break  # breaks out of the while loop

  elif user_input == '10':
    print('I gave you back $'+str(int(user_input)+100),'dollars.')  # nonformatted string concatenation
    break  # breaks out of the while loop

  else:
    print('You must give me the number 10 please:')
    continue  # continues the while loop iterataion

# Why not try these formatted string concatenation examples out:

print('I gave you back $'+str(int(user_input)+100),'dollars.')  # nonformatted string concatenation

print('I gave you back $'+str(int(user_input)+100)+' dollars.')  # nonformatted string concatenation


print('I gave you back ${}'.format(int(user_input)+100),'dollars.')  # old school formatted string concatenation

print('I gave you back ${}'.format(int(user_input)+100)+' dollars.')  # old school formatted string concatenation


print(f'I gave you back ${int(user_input)+90} dollars.')  # the new f' formatted string concatenation
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a basic layout of the 'try and except', 'finally' program
# example. The program does work fine, but it does nothing.
# The program example below simply shows the basic layout
# of the 'try and except', 'finally' statements. The 'finally' statement
# is executed no matter the outcome the 'try and except' handler
# block does. Note: you can also leave out the 'finally' statement
# if you like, but it can come in handy if you want the final outcome
# to execute no matter what the 'try and except' handler block
# does. The 'pass' statements are just empty placeholders for the
# empty code blocks until they are needed, via the programmer.

try:
  pass
except:   # Invoke the right kind of error handler for the right kind of error.
  pass
else:
  pass
finally:  # the finally statement is optional
  pass

# Here is the very same 'try and except' program example below.
# Type and execute/run the program and see what happens.

try:
  message = int(input('Pick a number: ').strip())  # remove leading and trailing whitespace characters

except ValueError:
  print('Numbers only please.')

else:
  print('You picked a number.')

finally:
  print("'finally' executed no matter what.")

# The 'finally' statement is executed no matter the outcome the
# 'try and except' handler block does.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is another practical 'if' Python program structure example,
# with a try and except error handler for the int(), integer function:

while True:
  try:
    user_input = int(input('Give me some money please: ').strip())  # remove leading and trailing whitespace characters

    if user_input == user_input:
      print('I gave you back $'+str(user_input+100),'dollars.')  # nonformatted string concatenation
      break

  except ValueError:
    print('You must give me some money please:')
  finally:
    pass

# Why not try these formatted string concatenation examples out:

print('I gave you back $'+str(user_input+100),'dollars.')  # nonformatted string concatenation

print('I gave you back $'+str(user_input+100)+' dollars.')  # nonformatted string concatenation


print('I gave you back ${}'.format(user_input+100),'dollars.')  # old school formatted string concatenation

print('I gave you back ${}'.format(user_input+100)+' dollars.')  # old school formatted string concatenation


print(f'I gave you back ${user_input+100} dollars.')  # the new f' formatted string concatenation
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is another practical 'if' Python program structure example,
# using conditionals, < less than and > greater than with a try and
# except error handler for the int(), integer function. Invoke the ':,'
# colon with a comma to create readable numeric output.

while True:
  try:
    user_input = int(input('Give me $10.00 dollars or more please: ').strip())  # remove leading and trailing whitespace characters

    if user_input == 10:
      print('I gave you back $'+str(user_input+100),'dollars.')  # nonformatted string concatenation
      break

    elif user_input < 10:
      print('You cheapskate! You get nothing now.')
      break

    elif user_input > 10:
      print('I gave you back $'+str(f'{user_input+1000:,}'),'dollars.')  # nonformatted string concatenation
      break

  except ValueError:
    print('You must give me some money please:')
  finally:
    pass

# Why not try these formatted string concatenation examples out:

print('I gave you back $'+str(user_input+100),'dollars.')  # nonformatted string concatenation

print('I gave you back $'+str(user_input+100)+' dollars.')  # nonformatted string concatenation


print('I gave you back ${}'.format(user_input+100),'dollars.')  # old school formatted string concatenation

print('I gave you back ${}'.format(user_input+100)+' dollars.')  # old school formatted string concatenation


print(f'I gave you back ${user_input+100} dollars.')  # the new f' formatted string concatenation
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This program example has three, separate conditional while
# loops, each of them compares data against user input data.
# The first while loop asks for the user's first name. The second
# while-loop asks for the user's last name, and the third while
# loop asks for the user's age. In the first and second while loop,
# the user's first name and the user's last name is compared
# by how many letters the user types. The 'str([first_name])'
# statement makes the user type in text only, not integers.

# Note: Python executes/runs programs starting from the top,
# downward. Be very careful on how you place statements.
# Some statements cannot execute right, even if they work.
# This is simply because of the order that Python executes/runs
# its program statements.

while True:
    first_name = input('\nWhat is your name please?: ').strip()  # remove leading and trailing whitespace characters

    if first_name < str([first_name]):
        print('\nError! text only please:')

    elif len(first_name) < 3:
        print('\nYour first name must be over 2 characters long.')

    elif len(first_name) > 10:
        print('Your first name must be under 10 characters long.')

    else:
        break

while True:
    last_name = input(f'\nNice to meet you {first_name.title()}. \
What is your last name please?: ').strip()  # remove leading and trailing whitespace characters

    if last_name < str([last_name]):
        print('\nError! text only please:')

    elif len(last_name) < 3:
        print('\nYour last name must be over 2 characters long.')

    elif len(last_name) > 10:
        print('\nYour last name must be under 10 characters long.')

    else:
        break

while True:
    try:
        age = int(input(f'\nHow old are you {first_name.title()}?: ').strip())  # remove leading and trailing whitespace characters
        break

    except ValueError:
        print('\nError! integers only please!')

print(f'\nYour first name = {first_name.title()}:\nYour last name = \
{last_name.title()}:\nYour age = {age}:\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create this fun password Python program example below. Let's
# also create some variables for print() function text arguments.

message = 'Please type your password to enter: '
password = 'open sesame'
welcome = "Welcome!\n\nYou've gained access into HEXADECACOM A.I."
incorrect_password = 'PASSWORD INCORRECT!'
denied_entry = 'You have entered the incorrect password too many times.\n\nAccess Denied!'
end_program = 'Now you know how to make Python create a password, that only you know.'
line_break = '\n'

count = 1
while count <= 3:

    user_input = input(message),strip()  # remove leading and trailing whitespace characters

    if user_input == password:
        print(line_break+welcome+line_break) # This is where you would put all your nice, complex Python code
        break

    else:
        print(line_break+incorrect_password+line_break)
    count += 1

    if count == 4:
        print(denied_entry+line_break)

print(end_program)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create this fun Python program example below. Make the computer
# find a number from 1 to 100. Let's also create two variables for
# print() function text arguments. Note: make sure you manually
# line up the break statement with the exact, same outer indentation
# as the for loop.

message = 'Pick a number from of 1 to 100 and I will find it: '
error_message = 'Sorry! Numbers only please.'

while True:
  try:
    user_input = int(input(message).strip())  # remove leading and trailing whitespace characters

    for i in range(1,101):
        if i == user_input:
            print(f'{i}: I found number "{i}" from 1 to 100:')
            continue
        print(i)
    break

  except ValueError:
    print(error_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create the same Python program example as the one
# above. Only this time, the computer will stop counting at the
# number that was picked, instead of counting onward. Note:
# make sure you manually line up the break statement with the
# exact, same outer indentation as the for loop.

message = 'Pick a number and I will count to it: '
error_message = 'Sorry! Numbers only please.'
line_break = '\n'

while True:
  try:
    user_input = int(input(message).strip())  # remove leading and trailing whitespace characters

    for i in range(1,user_input+1):
        if i == user_input:
            print(f'{i}{line_break}I counted to number "{i}" ')
            break
        print(i)
    break

  except ValueError:
    print(error_message)

# I am almost a complete Walking Human Computer Science Research Laboratory Machine on Two Legs... 😁

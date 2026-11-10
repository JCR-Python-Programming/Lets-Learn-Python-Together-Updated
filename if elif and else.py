# The correct 'if', 'elif' and 'else' Python program structure example:

while True:
  user_input = input('User input: ')  # user text input

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
# or this example to keep the Python code shorter.

while True:
  user_input = input('User input: ')  # user text input

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
# Here is practical 'if', 'elif' and 'else' Python program structure example:

while True:
  user_input = input('Give me the number $10.00 dollars please: ')  # user text input

# lowercase/uppercase characters for Caps Lock and shift keys

  if user_input in ('q','Q'):
    print('I Quit!:')
    break

  elif user_input == '10':
    print('I gave you back $'+str(int(user_input)+100),'dollars.')  # nonformatted string concatenation
    break

  else:
    print('You must give me the number 10 please:')
    continue  # continue the while loop iterataion

# Why not try these formatted string concatenation examples out:

print('I gave you back $'+str(int(user_input)+100),'dollars.')  # nonformatted string concatenation

print('I gave you back $'+str(int(user_input)+100)+' dollars.')  # nonformatted string concatenation


print('I gave you back ${}'.format(int(user_input)+100),'dollars.')  # old school formatted string concatenation

print('I gave you back ${}'.format(int(user_input)+100)+' dollars.')  # old school formatted string concatenation


print(f'I gave you back ${int(user_input)+90} dollars.')  # the new f' formatted string concatenation
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is another practical 'if' Python program structure example,
# with a try and except error handler for the int(), integer function:

while True:
  try:
    user_input = int(input('Give me some money please: '))  # user integer input

    if user_input == user_input:
      print('I gave you back $'+str(user_input+100),'dollars.')  # nonformatted string concatenation
      break

  except ValueError:
    print('You must give me some money please:')

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
    user_input = int(input('Give me $10.00 dollars or more please: '))  # user integer input

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

# Why not try these formatted string concatenation examples out:

print('I gave you back $'+str(user_input+100),'dollars.')  # nonformatted string concatenation

print('I gave you back $'+str(user_input+100)+' dollars.')  # nonformatted string concatenation


print('I gave you back ${}'.format(user_input+100),'dollars.')  # old school formatted string concatenation

print('I gave you back ${}'.format(user_input+100)+' dollars.')  # old school formatted string concatenation


print(f'I gave you back ${user_input+100} dollars.')  # the new f' formatted string concatenation

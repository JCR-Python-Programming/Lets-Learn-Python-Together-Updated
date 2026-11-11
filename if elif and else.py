# The correct 'if', 'elif' and 'else' Python program structure example:

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
  message = int(input('Pick a number. ').strip())  # remove leading and trailing whitespace characters

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

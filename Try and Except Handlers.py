# Try and except Error Handler Python program examples:

# Created by Joseph C. Richardson, GitHub.com

while True:
    number = int(input('\nGive me "10" please: ').strip())
    if number == 10:
        print(f'\nYou gave me "{number}", so I broke out of the \
conditonal while-loop example.')
        break

    elif number < 10:
        print(f'\nOops! You gave me "{number}", which is too small.\
I won\'t stop this condional while-loop example, until you give me "10".')

    elif number > 10:
        print(f'\nOops! You gave me "{number}", which is too big. \
I won\'t stop this condional while-loop example, until you give me "10".')

print('This is the end of the entire conditional while-loop example:')

# This Python program below is exactly the same as the Python
# program above, but with one exception. The Python program
# below has an error handler called 'try:' and 'except:' whereas
# the very same code above does not have an error handler at all.
# This spells disaster when you want the user to type numbers
# only. Without an error handler, if the user types a letter instead
# of a number, the program will crash leaving the user very unhappy
# with your newly developed software. It's imperative that in some
# situations, error handlers must be implemented into the program
# to prevent unwanted errors from occurring, such as in these 'try'
# and 'except' error handler Python program examples. From here
# onward, any 'input' statements with numeric examples given will
# contain 'try:' and 'except:' error handlers, along with some different
# 'try:' and 'except:' error handlers that deal with incorrect variable
# names, incorrect index[ ] values and incorrect typing code error
# handlers.

while True:
    try:
        number = int(input('\nGive me "10" please: ').strip())
        if number == 10:
            print(f'\nYou gave me "{number}", so I broke out of the \
conditonal while-loop example.')
            break

        elif number < 10:
            print(f'\nOops! You gave me "{number}", which is too small.\
I won\'t stop this condional while-loop example, until you give me "10".')

        elif number > 10:
            print(f'\nOops! You gave me "{number}", which is too big. \
I won\'t stop this condional while-loop example, until you give me "10".')

    except ValueError:
        print('\nThe \'try:\' and \'except ValueErorr:\' handlers prevent \
any unwanted value errors from occurring, via user input data.')

        print('\nIf the user presses any letter keys instead of pressing \
number keys, the \'try:\' and \'except:\'block executes/runs.')

print('This is the end of the entire conditional while-loop example:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is the very same 'try and except' program example below.
# Type and execute/run the program and see what happens.

try:
     message = int(input('Pick a number. ').strip())

except ValueError:
     print('Numbers only please.')

else:
     print('You picked a number.')

finally:
     print("'finally' executed no matter what.")

# The 'finally' statement is executed no matter the outcome the
# 'try and except' handler block does
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These two 'input' statements in this program example asks the
# user their name and their age, using the 'try:' and 'except:' error
# handlers.

name = input('\nWhat is your name please? ').strip()

try:
    age = int(input(f'\nHow old are you {name}? ').strip())
    print(f'\n{name}. You are {age} years old.')

except ValueError:
    print('\nThe \'try:\' and \'except ValueError:\' block executes/runs \
whenever a letter key is pressed instead of a number key.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, put this very same program code above into a conditional
# while-loop and see what happens when the user tries to type
# letters, instead of typing numbers for their age. When the 'try:'
# block is executed, the 'break' statement causes the conditional
# while-loop to break out and the 'print' function statement ('End
# of program') is then ran/executed.

name = input('\nWhat is your name please? ').strip()

while True:
    try:
        age = int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print('\nThe \'try:\' and \'except ValueError:\' block executes/runs \
whenever a letter key is pressed instead of a number key.')

print('End of program')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        x = int(input('Please input the first number: ').strip())
        y = int(input('Please input the second number: ').strip())

        if x > y:
            print(f'{x} is greater > than {y}:')
            break

        elif x == y:
            print(f'{x} is equal to {y}:')
            break

        else:
            print(f'{x} is less < than {y}:')
            break

    except ValueError:
        print('Sorry! Integer numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
name_error_variable = 'Thank you for correcting this variable name:'

try:
    print(name_error_variabl)

except NameError:
    print('Please correct this variable name to name_error_variable:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
type_error_variable = 'Rob','Bob','Terry','Mary'

try:
    print(f'You have {len(4)} values:')

except TypeError:
    print('Please replace {len(4)} with {len(type_error_variable)}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
index_error_tuple = ('Rob','Bob','Terry','Mary')

try:
    print(index_error_tuple[4])

except IndexError:
    print(f'Please correct this index[n] number starting from index 0, through index 3:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    print(0/0)

except ZeroDivisionError:
    print('cannot divide by zero:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Below is a whole list of 68 exception handlers. The 'except Exception:
# handler right below will except all Python programming errors, but
# it's not good practice to use this all the time. Invoke the right kind
# of exception handler for the right kind of error, such as 'except
# ValueError: for example. Note: whenever your Python Idle reads back
# an error message to you after crashing, read what the error message
# says, and then use that same exception handler, like TypeError:,
# NameError: IndexError and ValueError. You will see error messages
# that display the actual exception handler to use.
'''
except Exception:  Note: the Exception: handler will except 'all' errors.

except ArithmeticError:
except AssertionError:
except AttributeError:
except BaseException:
except BlockingIOError:
except BrokenPipeError:
except BufferError:
except BytesWarning:
except ChildProcessError:
except ConnectionAbortedError:
except ConnectionError:
except ConnectionRefusedError:
except ConnectionResetError:
except DeprecationWarning:
except EOFError:
except EnvironmentError:
except Exception:
except FileExistsError:
except FileNotFoundError:
except FloatingPointError:
except FutureWarning:
except GeneratorExit:
except IOError:
except ImportError:
except ImportWarning:
except IndentationError:
except IndexError:
except InterruptedError:
except IsADirectoryError:
except KeyError:
except KeyboardInterrupt:
except LookupError:
except MemoryError:
except ModuleNotFoundError:
except NameError:
except NotADirectoryError:
except NotImplementedError:
except OSError([arg]):
except OSError(errno, strerror[, filename[, winerror[, filename2]]]):
except OverflowError:
except PendingDeprecationWarning:
except PermissionError:
except ProcessLookupError:
except RecursionError:
except ReferenceError:
except ResourceWarning:
except RuntimeError:
except RuntimeWarning:
except StopAsyncIteration:
except StopIteration:
except SyntaxError:
except SyntaxWarning:
except SystemError:
except SystemExit:
except TabError:
except TimeoutError:
except TypeError:
except UnboundLocalError:
except UnicodeDecodeError:
except UnicodeEncodeError:
except UnicodeError:
except UnicodeTranslateError:
except UnicodeWarning:
except UserWarning:
except ValueError:
except Warning:
except WindowsError:
except ZeroDivisionError:
'''
try:
     pass
except:  # Invoke the right kind of error handler for the right kind of error.
     pass
else:
     pass
finally:  # the finally statement is optional
     pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's raise some errors, via invoking the 'raise' statement along
# with the right type of exception handler with a custom message.

name_error = 'Rob'

if name_error == 'John':
    print('Hello World!')

else:
    raise NameError(f'ERROR!! My name is {name_error}:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    type_error = input('\nWhat is your name please? ').strip()

    if type_error < str([type_error]):
        raise TypeError('Sorry! Character text only please:')
            
    elif len(type_error) < 3:
        raise ValueError('Your name must be over 2 characters long:')

    elif len(type_error) > 10:
        raise ValueError('Your name must be less < than or equal = to 10 characters long:')

    else:
        print(f'\nHi {type_error.title()}. How are you?')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
password_error = input('What is the password? ').strip()

if password_error == 'open sesame':
    print('access granted:')

else:
    raise TypeError('Sorry! access denied:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        age_error = int(input('How old are you? ').strip())

        if age_error >= 21:
            print('You are old enough to drink.')
            break

        elif age_error < 21:
            raise Exception('You are much too young to drink:')

    except ValueError:
        print('Sorry! Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 3

if x != 4:
    raise ValueError(f'ERROR! {x} is the incorrect value:')

else:
    print(f'{x} is the correct value:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 1
y = 5

if x > y:
    print(f'{x} is greater > than {y}:')

elif x == y:
    print(f'{x} is equal = to {y}:')

else:
    raise ValueError(f'{x} is less < than {y}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = int(input('Please input amount: ').strip())

if x <= 2000:
    print(f'{x} is less < than or equal = to 2000:')

elif x > 2000:
    raise ValueError(f'{x} is greater > than 2000')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

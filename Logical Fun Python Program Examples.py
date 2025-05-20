# Logical Fun Python Program Examples And More:

# Created by JCR, GitHub.com

# Create Python programs that can tell you how many seconds there
# are a minute, hour, day, week, month and year. Invoke the colon :
# and the comma , (:,) to group large number units and make them
# readable. Please note: Some of these Python program examples
# are only approximations of how many minutes/seconds there are
# minutes, hours, days, weeks, months and years. However, if you
# plug in variables that include how may days there are in a month
# and such, you will find the exact number of seconds there are in
# one month. For example: a thirty day month and a thirty-one day
# month. The same goes for years, plug in the days2 variable to see
# how many seconds are in a leap year, which is 366 days long.

seconds = 60

while True:
    try:
        user_input = int(input('Please type number of minutes: ').strip())
        if user_input <= 0:
            print('No such minute exist:')
        elif user_input == 1:
            print(f'{user_input:,} minute = {user_input*seconds:,} seconds:')
            break
        else:
            print(f'{user_input:,} minutes = {user_input*seconds:,} seconds:')
            break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
seconds = 60
minutes = 60

while True:
    try:
        user_input = int(input('Please type number of hours: ').strip())
        if user_input <= 0:
            print('No such hour exist:')
        elif user_input == 1:
            print(f'{user_input:,} hour = {user_input*minutes:,} minutes = \
{user_input*minutes*seconds:,} seconds:')
            break
        else:
            print(f'{user_input:,} hours = {user_input*minutes:,} minutes = \
{user_input*minutes*seconds:,} seconds:')
            break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
seconds = 60
minute = 60
hours = 24

while True:
    try:
        user_input = int(input('Please type number of days: ').strip())
        if user_input <= 0:
            print('No such day exist:')
        elif user_input == 1:
            print(f'{user_input:,} day = {user_input*hours:,} hours = \
{user_input*hours*minutes:,} minutes = {user_input*hours*minutes*seconds:,} \
= seconds:')
            break
        else:
            print(f'{user_input:,} days = {user_input*hours:,} hours = \
{user_input*hours*minutes:,} minutes = {user_input*hours*minutes*seconds:,} \
= seconds:')
            break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
seconds = 60
minutes = 60
hours = 24
days = 7

while True:
    try:
        user_input = int(input('Please type number of weeks: ').strip())
        if user_input <= 0:
            print('No such week exist:')
        elif user_input == 1:
            print(f'{user_input:,} week = {user_input*days:,} days = \
{user_input*days*hours:,} hours = {user_input*days*hours*minutes:,} \
minutes = {user_input*days*hours*minutes*seconds:,} seconds:')
            break
        else:
            print(f'{user_input:,} weeks = {user_input*days:,} days = \
{user_input*days*hours:,} hours = {user_input*days*hours*minutes:,} \
minutes = {user_input*days*hours*minutes*seconds:,} seconds:')
            break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create variables for months that have different days, along with a
# leap year month. Select which days variable you would like use to
# see how many seconds there are in one month. For example: invoke
# the days4 variable to see how many seconds are in a leap year month.
# See the Python program example below:

seconds = 60
minutes = 60
hours = 24

# Thirty days has September, April, June, and November, All the rest have
# thirty-one, February is twenty-eight days, But a leap year adds an extra
# day; February has one extra day making it 29 days. A leap year happens
# every four years on even year numbers, evenly divisible by four.

days1 = 30  # 30 day month
days2 = 31  # 31 day month
days3 = 28  # 28 day month
days4 = 29  # leap year day month

while True:
    try:
        user_input = int(input('Please type number of months: ').strip())
        if user_input <= 0:
            print('No such month exist:')
        elif user_input == 1:
            print(f'{user_input:,} month = {user_input*days4:,} days = \
{user_input*days4*hours:,} hours = {user_input*days4*hours*minutes:,} \
minutes = {user_input*days4*hours*minutes*seconds:,} = seconds:')
            break
        else:
            print(f'{user_input:,} months = {user_input*days1:,} days = \
{user_input*days1*hours:,} hours = {user_input*days1*hours*minutes:,} \
minutes = {user_input*days1*hours*minutes*seconds:,} = seconds:')
            break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
seconds = 60
minutes = 60
hours = 24

days1 = 365
days2 = 366  # leap year day

weeks = 52
months = 12

while True:
    try:
        user_input = int(input('Please type number of years: ').strip())
        if user_input <= 0:
            print('No such year exist:')
        elif user_input == 1:
            print(f'{user_input:,} year = {user_input*months:,} \
months = {user_input*weeks:,} weeks = {user_input*days2:,} days = \
{user_input*days2*hours:,} hours = {user_input*days2*hours*minutes:,} \
minutes = {user_input*days2*hours*minutes*seconds:,} seconds:')
            break
        else:
            print(f'{user_input:,} years = {user_input*months:,} \
months = {user_input*weeks:,} weeks = {user_input*days1:,} days = \
{user_input*days1*hours:,} hours = {user_input*days1*hours*minutes:,} \
minutes = {user_input*days1*hours*minutes*seconds:,} seconds:')
            break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here's a fun, simple Python program example, which tells you how
# many seconds you have been on Earth for. Type and execute/run the
# program example below and see what happens when you type your
# age, then press the 'Enter' key. Note: this Python program example
# does not include months that have extra days or any, such leap year
# month or day. This Python program is just an approximation of how
# many seconds you have been on Earth for; not the exact seconds.

months = 12
weeks = 52
days = 365

hours_per_day = 24
minuts_per_hour = 60
seconds_per_minute = 60

string_tuple = (
    months,weeks,days,
    hours_per_day,
    minuts_per_hour,
    seconds_per_minute
    )

while True:
    try:
        age = int(input('How old are you? ').strip())
        if age <= 0:
            print('No such age exist:')
            continue
        else:
            print(f'\nYou have been on Earth for {age} years.')

            print(f'\nYou have been on Earth for {age*string_tuple[0]:,} months.')

            print(f'\nYou have been on Earth for {age*string_tuple[1]:,} weeks.')

            print(f'\nYou have been on Earth for {age*string_tuple[2]:,} days.')

            print(f'\nYou have been on Earth for {age*string_tuple[2]*string_tuple[3]:,} hours.')

            print(f'\nYou have been on Earth for \
{age*string_tuple[2]*string_tuple[3]*string_tuple[4]:,} minutes.')

        print(f'\nYou have been on Earth for \
{age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]:,} seconds.')
        break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same python program example as the one above, but
# we will use just one, single print() function for our text and text variables
# alike. Invoke three single quote marks ''' at the beginning of the print()
# function and at the end of the print() function.

months = 12
weeks = 52
days = 365

hours_per_day = 24
minuts_per_hour = 60
seconds_per_minute = 60

string_tuple = (
    months,weeks,days,
    hours_per_day,
    minuts_per_hour,
    seconds_per_minute
    )

while True:
    try:
        age = int(input('How old are you? ').strip())
        if age <= 0:
            print('No such age exist:')
            continue
        else:
            print(f'''
You have been on Earth for {age} years.

You have been on Earth for {age*string_tuple[0]:,} months.

You have been on Earth for {age*string_tuple[1]:,} weeks.

You have been on Earth for {age*string_tuple[2]:,} days.

You have been on Earth for \
{age*string_tuple[2]*string_tuple[3]:,} hours.

You have been on Earth for \
{age*string_tuple[2]*string_tuple[3]*string_tuple[4]:,} minutes.

You have been on Earth for \
{age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]:,} seconds.''')
        break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tip: If you want to express large number units in programming, you can
# invoke the _ underscore character to make the number units readable.

print(1_000_000)  # screen output: 1000000

# If you want to express large number units in programming, you can
# invoke the _ underscore character to make the number units readable.
# Also, invoke these two characters :, to get the screen output as 1,000,000
# not 1000000. Note: the print() function text only shows the programmer
# the readable number units. The _ underscore does not show readable
# number units in the screen output. And that's why we have to invoke the
# colon : and the comma , to make the screen output number units readable
# as well. You must invoke the f' string format to view the readable
# number units on the screen output at execution/run time.

print(f'{1_000_000:,}')  # screen output: 1,000,000

print(f'{1000000:,}')  # screen output: 1,000,000

LNU = 1_000_000  # create a variable and a large number value 1_000_000

print(f'{LNU:,}')  # screen output: 1,000,000 via the :, colon : and the comma ,
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's walk the dinosaur and see what it's like to go back in the early days
# of Python, way before the f' string format came along. The format()
# function was used before the f' string format came into being.

LNU = 1_000_000  # create a variable and a large number value 1_000_000

print('{}'.format(LNU)) # screen output: 1000000

print('{:,}'.format(LNU)) # screen output: 1,000,000 via the :, colon : and the comma ,
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's walk the dinosaur again and see what it's like to go back in the early
# days of Python, way before the f' string format came along. The format()
# function was used before the f' string format came into being.

first_name = 'John'
last_name = 'Smith'
age = 25

print('{} {} is {} years old using old format().'.format(first_name,last_name,age))

print('{} {} is {} years old'.format(first_name,last_name,age),'using old format().')

print('{} {} is {} years old'.format(first_name,last_name,age)+' using old format().')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's get prehistoric and visit the T-Rex Python program example, using
# the prehistoric version of how many seconds you have been on Earth for.
# This is what is called 'The Old Format' string, now depreciated in later Python
# versions; three and up. Note: you must place your variables in the correct
# order as shown in the first two, smaller examples of the old format method.

# However, 'The Old Format' string method does work very well still; it's useful
# when you have very long string variables with others, such as this illustration
# snippet of Python code shows:

# age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]

# Sometimes it's a grand idea to use 'The Old Format' string method for very
# long string variables. That way your printed text code inside print() functions
# won't have all them bulky string variables all throughout your print() function
# text code. Just make sure 'The Old Format' string variables are in ORDER
# within print() function text code, via the {} curly braces that are placeholders
# for the variables that reside within the 'The Old Format' string code section
# as illustrated below:

# .format(
#    age,age*string_tuple[0],age*string_tuple[1],
#    age*string_tuple[2],age*string_tuple[2]*string_tuple[3],
#    age*string_tuple[2]*string_tuple[3]*string_tuple[4],
#    age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]),'Optional use...')

months = 12
weeks = 52
days = 365

hours_per_day = 24
minuts_per_hour = 60
seconds_per_minute = 60

string_tuple = (
    months,weeks,days,
    hours_per_day,
    minuts_per_hour,
    seconds_per_minute
    )

while True:
    try:
        age = int(input('How old are you? ').strip())
        if age <= 0:
            print('No such age exist:')
            continue
        else:
            print('''
You have been on Earth for {} years.

You have been on Earth for {:,} months.

You have been on Earth for {:,} weeks.

You have been on Earth for {:,} days.

You have been on Earth for {:,} hours.

You have been on Earth for {:,} minutes.

You have been on Earth for {:,} seconds.'''.format(
    age,age*string_tuple[0],age*string_tuple[1],
    age*string_tuple[2],age*string_tuple[2]*string_tuple[3],
    age*string_tuple[2]*string_tuple[3]*string_tuple[4],
    age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]),'Optional use...')
        break
    except ValueError:
        print('Numbers only please:')

# Now you can clearly understand what the new f' string format does and
# what 'The Old Format' string example does. If you have lots of variables
# within print() functions, it's best to use the 'The Old Format' string method
# and keep all that bulky Python variable code within the .format() function
# part at the end of the print() function as shown.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some different ways to generate computer numbers in Python.
# We can generate computer numbers in Binary base 2, Octal base 8 and
# Hexadecimal base 16 number systems. Here are some different ways to
# generate computer number systems in Python. Note: the decimal number
# system is for us humans only; computers cannot understand our human
# decimal base 10 number system. Computers have to turn our human
# decimal number system into binary base 2, which is what computers only
# understand. Octal base 8 and Hexadecimal base 16 were once the only
# way to get computers to generate readable numbers back to the humans
# who created them and those who used them. Today, we can simply use
# our familiar human decimal base 10 number system. However, Python gave
# us the option to explore and exploit these computer based number systems
# to use within our Python programs.

print(format(255,'d'))  # 255 = 255

print(format(255,'b'))  # 11111111 = 255

print(format(255,'o'))  # 377 = 255

print(format(255,'x'))  # ff = 255

print(f'{255:d}')  # 255 = 255

print(f'{255:b}')  # 11111111 = 255

print(f'{255:o}')  #  377 = 255

print(f'{255:x}')  #  ff = 255

print(bin(255))  # 0b11111111 = 255

print(oct(255))  # 0o377 = 255

print(hex(255))  # 0xff = 255
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a small Python program that asks the user to type a
# decimal base 10 number that will be retranslated back into binary
# base 2, Octal base 8 and Hexadecimal base 16 number systems.

try:
    user_input = int(input('Please type a human decimal number: ').strip())

    print(f"bin = {format(user_input,'b')}, oct = {format(user_input,'o')}, hex = \
{format(user_input,'x')}, dec = {format(user_input,'d')}")

    print(f'bin = {user_input:b}, oct = {user_input:o}, hex = {user_input:x}, \
dec = {user_input:d}')

    print(f'bin = {bin(user_input)}, oct = {oct(user_input)}, hex = {hex(user_input)}, \
dec = {user_input}')
except ValueError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's recreate the same Python program example above, but we will
# use one print() function along with 'The Old Format' string method
# to manage all them bulky variables at the end of the entire print()
# function code as we did before. Just make sure 'The Old Format'
# string variables are in ORDER within print() function text code, via
# the {} curly braces that are placeholders for the variables that reside
# within the 'The Old Format' string code section as shown below.
# Invoke three single quote marks ''' at the beginning of the print()
# function and at the end of the print() function.

try:
    user_input = int(input('Please type a human decimal number: ').strip())

    print('''
    bin = {}, oct = {}, hex = {}, dec = {}

    bin = {}, oct = {}, hex = {}, dec = {}

    bin = {}, oct = {}, hex = {}, dec = {}'''.format(
    format(user_input,'b'),format(user_input,'o'),
    format(user_input,'x'),format(f'{user_input:,}'),

    f'{user_input:b}',f'{user_input:o}',
    f'{user_input:x}',f'{user_input:,}',

    bin(user_input),oct(user_input),
    hex(user_input),f'{user_input:,}'),'Optional use...')
except ValueError:pass

# Simply using only one print() function and six ''' ''' single quote marks
# make string concatenation and text layout much more easier to create;
# what you see is what you get, including line spaces and indentations
# alike. And with 'The Old Format' string function, we can place all our
# bulky variables neatly tucked away within the print() function at the at
# the end of it.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Make the user type an eight bit number between 0 and 255. If the user
# types any other numbers greater than 255, the computer will complain.
# If the user types negative numbers, the computer will complain. And if
# the user types letters instead of numbers, the computer will complain.

# Change the eight bit value 256 into a large sixteen bit number value.
# sixteen bits = 65,535, counting zero, you get 65,536. Likewise, eight
# bits work the same: 0 to 255 = 256 byte combinations of 'On', and 'Off',
# '1' and '0', 'Yes' and 'No'. All bits off = 00000000 = 0. All bits on =
# 11111111 = 255 and the off bits zero make up the 256 byte combinations
# of 'On' and 'Off', '1' and '0', 'Yes' and 'No', 'True' and 'False'. This is
# what the binary base 2 system is all about. 'On' and 'Off', '1' and '0',
# 'Yes' and 'No', 'True' and 'False'. Computers only understand binary
# level programming at the heart. Hexadecimal base 16 and octal base 8
# were once the only way to translate computer binary generated numbers
# into readable numbers us humans could understand, and to reconvert
# these number systems into the human decimal base 10 system we know.
# Today, we don't have to use these number systems in programming.
# However, machine assembler language compliers do dictate hexadecimal
# base 16 number notion, not decimal base 10, like higher level programming
# languages offer, such as Python, C++ and BASIC. Is BASIC still around,
# I wonder?

while True:
    try:
        user_input = int(
            input('Please type a human decimal number between 0 and 255: ').strip())
        if user_input >= 256:
            print(f'{user_input:,} is too high!')
        elif user_input < 0:
            print('No negative numbers allowed:')
        else:
            print(f'{user_input:b} = {user_input:o} = {user_input:x} = {user_input}')
            break
    except ValueError:
        print('Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Hexadecimal base 16 works just like our decimal base 10 system does.
# We humans count from 1 to 10, and sometimes from 0 to 9. Hexadecimal
# base 16 counts from 0 to 15; hexadecimal numbers turn into letters after
# the hexadecimal number 9. Here is how they count from 0 to 15:

# hexadecimal number system: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F 'F' equals decimal 15
# and 255 = 'FF'

# Just remember that hexadecimal numbers count from 0 and up to 15 or 'F'.
# binary base 2 is the same way; the bits start off at '0', not '1' hence 256 byte
# combinations from 0 to 255, not 1 to 255. We humans count from 1 to 10
# or 0 to 9 sometimes. Computers always start at '0', which is why the extra
# byte combination 255 is really 256, when you count zero as a number value
# as well.

# And finally, the octal base 8 number system starts from 0 to 7, just like our
# decimal base 10 system does. Computers always start at '0', which is why
# the extra octal combination 7 is really 8, when you count zero as a number
# value as well. Here is how this all looks from the binary perspective, the
# hexadecimal perspective and the octal perspective, as well as our own
# decimal system perspective.

# Human decimal base 10 counting system example:

# 1,2,3,4,5,6,7,8,9,10, or 0,1,2,3,4,5,6,7,8,9

# Binary base 2 counting system example:

# All bits off = 00000000, all bits on = 11111111

# Eight binary bits = one binary byte: 128,64,32,16,8,4,2,1 = 255

# Simply add up all the numbers to reach the total value of 255

# Remember that '0' is also the extra byte combination, 256 when
# all bits are set to 0, or off; computers always count from '0' and
# up. Not '1' and up.

# Hexadecimal base 16 counting system example:

# 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F 'F' equals decimal 15

# Remember that '0' is also the extra hex combination, 16 when
# all hex numbers are set to 0, or off; computers always count from
# '0' and up. Not '1' and up.

# Octal base 8 counting system example: 0,1,2,3,4,5,6,7

# Remember that '0' is also the extra octal combination, 8 when
# all octal numbers are set to 0, or off; computers always count from
# '0' and up. Not '1' and up.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a simple for-loop that will count from '0' to '255'. This will show and
# teach us how computer numbers count and show us how to understand
# their counting system pattern, similar to our own human decimal base 10
# counting system pattern alike. Note: set the for-loop to the value 256 to
# include the '0' digit count for proper computer science numbering systems.
# Always remember, that all computers always start at '0' and up. Not '1' and up.

for i in range(256):
    print('Bin = one byte =',len(f'{i:b}'),f'bits {i:b} = Hex = {i:X}, Oct = {i:o}, Dec = {i}...')

# Bin = one byte = 8 bits 11111111 = Hex = FF, Octal = 377, dec = 255

for i in range(65_536):
    print('Bin = two bytes =',len(f'{i:b}'),f'bits {i:b} = Hex = {i:X}, Oct = {i:o}, Dec = {i:,}...')

# Bin = two bytes = 16 bits 1111111111111111 = Hex = FFFF, Octal = 177777,
# dec = 65,535

for i in range(16_777_216):
    print('Bin = three bytes =',len(f'{i:b}'),f'bits {i:b} = Hex = {i:X}, Oct = {i:o}, Dec = {i:,}...')

# Bin = three bytes = 24 bits 111111111111111111111111 = Hex = FFFFFF, Octal =
# 77777777, dec = 16,777,215
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create simple for-loops that will generate all the lowercase and
# uppercase ascii code characters, as well as all the integer number
# ascii code characters 0 through 9. Invoke the chr(), character
# function to get the ascii code values.

for i in range(97,123):
    print(f'lowercase ascii code character ({chr(i)}) = {i:b} = {i:X} = {i:o} = {i}...')

for i in range(65,91):
    print(f'uppercase ascii code character ({chr(i)}) = {i:b} = {i:X} = {i:o} = {i}...')

for i in range(48,58):
    print(f'integer number ascii code character ({chr(i)}) = {i:b} = {i:X} = {i:o} = {i}...')

# You can also generate the ascii code value of the blank space charactor '32'

i = 32

print(f'blank space ascii code character ({chr(i)}) = bin: {i:b} = \
hex: {i:X} = oct: {i:o} = dec: {i}...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the ord() function to get an ascii character code value.

while True:
    try:
        user_input = input("Type a letter key or a number key, then press 'Enter': ")

        if user_input == user_input:
            print(f'The ascii code character ({user_input}) = bin: \
{ord(user_input):b} = hex: {ord(user_input):X} = oct: \
{ord(user_input):o} = dec: {ord(user_input)}...')
            break
    except TypeError:
        print('Type one character at a time please:')

# The ascii code character (A) = bin: 1000001 = hex: 41 = oct: 101 = dec: 65...

# You can also generate the ascii code number for the blank space character ' '

i = ' '

print(f'blank space ascii code number bin: {ord(i):b} = hex: {ord(i):X} = \
oct: {ord(i):o} = dec: {ord(i)}...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the chr(), character function to get an ascii code value.

while True:
    try:
        user_input = int(input("Type an ascii code number, then press 'Enter': ").strip())

        if user_input == user_input:
            print(f'The ascii code number for the ascii code character \
({chr(user_input)}) = bin: {user_input:b} = hex: {user_input:X} = \
oct: {user_input:o} = dec: {user_input}...')
            break
    except ValueError:
        print('Numbers only please:')

# The ascii code number for the ascii code character (A) = bin: 1000001 =
# hex: 41 = oct: 101 = dec: 65...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print(bin(255))  # 0b11111111 = 255
print(hex(255))  # 0xff = 255
print(oct(255))  # 0o377 = 255

print(f'{255:b}')  # 11111111 = 255
print(f'{255:x}')  # ff = 255
print(f'{255:o}')  # 377 = 255

print(chr(65))  # ascii character value for the letter 'A'
print(ord('A'))  # unicode code for the ascii character value '65'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Python program that can display hidden ascii code
# mesages. Execute/run this Python program below, and then
# copy, and then paste the screen output of all the ascii numbers
# into a tuple or list as shown below:

text_string_value = 'Learning Python is so much FUN!'

for i in text_string_value:
  print(ord(i),end=',')

# screen output: 76,101,97,114,110,105,110,103,32,80,121,
# 116,104,111,110,32,105,115,32,115,111,32,109,117,99,104,32

# After you highlight and copy the screen output, paste it
# back into a tuple of any variable name you choose. Make
# sure the Python program example above works first before
# you delete it. Create the following Python program example
# below and make hidden text messages with ascii codes only.
# Make Python create your ascii codes for you first to make
# programming ascii codes much faster. Make sure this Python
# program example below works first, then delete the first Python
# program example above after you made it create the tuple of
# ascii codes for the hidden text message, as was shown above.

ascii_code_dec_values = (  # Create a variable name for your ascii code values.
  76,101,97,114,110,105,110,103,32,80,121,116,104,111,110,
  32,105,115, 32,115,111,32,109,117,99,104,32,70,85,78,33,)  # Paste the screen output values.

for i in ascii_code_dec_values:
  print(chr(i),end='')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Display the ascii code characters in binary, hexadecimal, octal
# and decimal numbers, along with their ascii character values.

text_string_value = 'Learning Python is so much FUN!'

for i in text_string_value:
  print(f'binary value: {ord(i):b} = ascii character value ({i})')

for i in text_string_value:
  print(f'hexadecimal value: {ord(i):x} = ascii character value ({i})')

for i in text_string_value:
  print(f'octal value: {ord(i):o} = ascii character value ({i})')

for i in text_string_value:
  print(f'decimal value: {ord(i)} = ascii character value ({i})')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Display all the ascii code characters in binary, hexadecimal, octal
# and decimal numbers, along with their ascii character values.

ascii_charactors = (
  ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKL\
MNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~''')

for i in ascii_charactors:
  print(f'binary value: {ord(i):b} = ascii character value ({i})')

for i in ascii_charactors:
  print(f'hexadecimal value: {ord(i):x} = ascii character value ({i})')

for i in ascii_charactors:
  print(f'octal value: {ord(i):o} = ascii character value ({i})')

for i in ascii_charactors:
  print(f'decimal value: {ord(i)} = ascii character value ({i})')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# There are OS screen colours, which colours text. These OS screen
# colour codes colour individual text characters. Note: you must
# execute/run the program from the OS output screen, via double-
# clicking the Python program file itself. See program examples
# below:

black = '\x1b[30m'
red = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
purple = '\x1b[35m'
cyan = '\x1b[36m'
white = '\x1b[37m'

print(white+'Text Colour.')

# Invoke the f' string format to make string concatenation easy peasy.

print(f'{white}Text Colour.')

bg_red = '\x1b[41m'
bg_green = '\x1b[42m'
bg_yellow = '\x1b[43m'
bg_blue = '\x1b[44m'
bg_purple = '\x1b[45m'
bg_cyan = '\x1b[46m'
bg_white = '\x1b[47m'

print(bg_red+'Background Text Colour.')

# Invoke the f' string format to make string concatenation easy peasy.

print(f'{bg_red}Background Text Colour.')

# Create OS text styles in Python. Invoke 'The Old Format' method
# to neatly tuck away bulky variable strings. Note: you must
# execute/run the program from the OS output screen, via double-
# clicking the Python program file itself. See program example
# below:

text_style_bold = '\x1b[1m'
text_style_italic = '\x1b[3m'
text_style_underline = '\x1b[4m'
text_style_strikethrough = '\x1b[9m'

print(text_style_bold+'Text Style.')

# Invoke the f' string format to make string concatenation easy peasy.

print(f'{text_style_bold}Text Style.')

text_old_format = '{}{}{}{}{}{}'.format(
    cyan,
    bg_purple,
    text_style_bold,
    text_style_italic,
    text_style_underline,
    text_style_strikethrough)

print(text_old_format+'The Old Format text example:')

# Invoke the f' string format to make string concatenation easy peasy.

print(f'{text_old_format}The Old Format text example:')

# Create OS text styles in Python. Invoke 'The New f' string
# Format' to neatly tuck away bulky variable strings. Note:
# you must execute/run the program from the OS output
# screen, via double-clicking the Python program file itself.
# See program example below:

text_new_format = f'\
{cyan}\
{bg_purple}\
{text_style_bold}\
{text_style_italic}\
{text_style_underline}\
{text_style_strikethrough}'

print(text_new_format+"The New f' string Format text example:")

# Invoke the f' string format to make string concatenation easy peasy.

print(f"{text_new_format}The New f' string Format text example:")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# There are also OS screen colours, which also colours text. However,
# the OS screen colours are not as flexible as text colours are. For
# example, If you try to make one line of text blue and try to make the
# next line of text green. When you execute/run the program, the next
# line of text you coloured green will override the blue text, making it
# green text too. Note: you must execute/run the program from the OS
# output screen, via double-clicking the Python program file itself.

import os  # import the os module

red = 'color 4'
green = 'color 2'
yellow = 'color 6'
blue = 'color 1'
purple = 'color 5'
cyan = 'color 3'
white = 'color f'

os.system(white)

print('Text Colour.')

bg_red = 'color 40'
bg_green = 'color 20'
bg_yellow = 'color 60'
bg_blue = 'color 10'
bg_purple = 'color 50'
bg_cyan = 'color 30'
bg_white = 'color f0'

os.system(bg_red)

print('OS Background Colour.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create your very own clock Python program example:

# Python clock functions allow you to program the actual time in real time.
# Python clock functions work internally, in sync with the Windows clock.
# With Python clock functions; you can set the hour, minute, second, month,
# week, day and date. See Python clock function prefix descriptions below.
'''
'%I' 12-hour prefix
'%H' 24-hour prefix
'%M' Minutes prefix
'%S' Seconds prefix
'%p' AM/PM prefix
'%A' Day of week prefix
'%B' Month prefix
'%d' Date prefix
'%Y' Year prefix
'%U' Weeks per year prefix
'%j' Days per year prefix
'''
# Let's create a simple Python clock by invoking the Python clock function
# prefixes. First, however, we also need to import two modules; 'time' and
# 'datetime'. Type and execute/run the program example below and see
# what happens.

import time,datetime

print(datetime.datetime.now().strftime('%I:%M:%S:%p'))
print(datetime.datetime.now().strftime('%H:%M:%S'))
print(datetime.datetime.now().strftime('%A %B %d,%Y'))
print(datetime.datetime.now().strftime('Week %U'))
print(datetime.datetime.now().strftime('Day %j'))

# Remember you can reduce balky code via, using string variables. Let's
# use 'timer' as the variable and use 'datetime.datetime.now()' as the value.
# Type and execute/run the program example below and see what happens.

import time,datetime

timer = datetime.datetime.now()

print(timer.strftime('%I:%M:%S:%p'))
print(timer.strftime('%H:%M:%S'))
print(timer.strftime('%A %B %d,%Y'))
print(timer.strftime('Week %U'))
print(timer.strftime('Day %j'))

# Now, let's create a tuple variable called 'show_time' so we can reduce
# even more balky code, and also gain greater manipulative programming
# skills at the same time. Type and execute/run the program example
# below and see what happens.

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

# Now change and rearrange the tuple number values [0] through [4] in
# the program example above and re-execute/run the program and see
# what happens.

# Now, let's make our Python clock come to life. Let's also keep the code
# less balky and much more program manipulative at the same time. To
# make the Python clock come to life, we are simply going to use a while-
# loop to constantly refresh the screen output. A 'time.sleep()' function
# will also be implemented to create a one-second sleep delay in the screen
# output. Let's also implement the 'os.system()' function to clear the screen
# output right after every one-second 'time.sleep' delay. Type and execute/
# run the program example below and see what happens.

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

# Let's shorten our code by reducing our print() functions down to only one,
# using a for-loop inside the while loop.

while True:
    for i in range(5):
        timer = datetime.datetime.now()
        print(timer.strftime(show_time[i]))

    time.sleep(1)
    os.system('cls')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Auto Type Colour Text Effects with Sound Python program example:

# Note: after you save your file, you must double click this file to view its
# cool coloured text effects and layout. Next, create a folder for your typing
# sound effect wave file and your Python file so they can execute/run together.
# Note: all sound files must be wave format; Python will not execute/run
# sound files in mp3 format, without importing a Python module for that.
# And that, I do not have at this moment.

import os,time,winsound

text_colours = (
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

clear_screen = 'cls'
single_line_break = '\n'
double_line_break = '\n\n'
indent = ' '*2
wave_sound = 'TYPE'  # 'sound wave file name'

text_words = (
f"{single_line_break}{indent}This is how you do auto colour text typing \
with Python programming.{single_line_break}{indent}You can type as many \
lines of text you please by invoking the '\\'{single_line_break}{indent}backslash \
to create hard returns within the text code programming{single_line_break}\
{indent}part of the program only.",f'{clear_screen}')

length = 0

while length <= len(text_words[0]):
    for i in text_colours:
        print(i+text_words[0][:length])
        winsound.PlaySound(wave_sound,winsound.SND_ASYNC)
        time.sleep(.08)
        os.system(text_words[1])
        length += 1

print(text_colours[6]+text_words[0])

# place an input() function so you can press the Enter key to to close the program.

input(f'{double_line_break}{indent}Press Enter to exit and close the program:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Stars Game Python program example:

# Execute/run this program example and see how the while-loop only
# breaks when one of the two 'break' statements is executed. If none
# of them gets executed, the while-loop keeps on iterating. This program
# example is another great example of how the conditional 'if:' and
# 'elif:' statements work in conjunction with the logical operators.

while True:
    try:
        stars=int(input(f'How many stars would you like? ').strip())
        if stars>1:
            print(f'\n{stars} Stars: [',' * '*stars,f']\n\nI gave you {stars} \
Stars!\n\nI hope you enjoy your {stars} Stars...')
            break

        elif stars==1:
            print(f'\n{stars} Star: [','*'*stars,f']\n\nI gave you {stars} \
Star!\n\nI hope you enjoy your \'One\' and \'Only\', single Star...')
            break

        elif stars==0:
            print('\nSorry Hero! Zero doesn\'t count.\n')
    except ValueError:
        print('\nNumbers only please!\n')

# I am almost a complete Walking Human Computer Science Research Laboratory
# Machine on Two Legs... 😁

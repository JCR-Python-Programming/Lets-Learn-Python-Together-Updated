first_name = 'John'
last_name = 'Smith'
age = 25

print('{} {} is {} years old using old format().'.format(first_name,last_name,age))

print('{} {} is {} years old'.format(first_name,last_name,age),'using old format().')

print('{} {} is {} years old'.format(first_name,last_name,age)+' using old format().')

# Logical Python Fun

# Created by JCR, GitHub.com

# Create Python programs that can tell you how many seconds there
# are a minute, hour, day, week, month and year. Invoke the colon :
# and the comma , (:,) to group large number units and make them
# readable. Please note: Some of these Python program examples
# are only approximations of how many minutes/seconds there are
# minutes, hours, days, weeks, months and years. However, if you
# plug in variables that include how may days there are in a month
# and such, you will find the exact number of seconds there are
# in one month. For example: a thirty day month and a thirty-one
# day month. The same goes for years, plug in the days2 variable
# to see how many seconds are in a leap year, which is 366 days long.

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

# Thirty days has September, April, June, and November, All the rest have
# thirty-one, February is twenty-eight days, But a leap year adds an extra
# day; February has one extra day making it 29 days. A leap year happens
# every four years on even year numbers, evenly divisible by four.
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
            print(f'''\nYou have been on Earth for {age} years.

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
# Let's walk the dinosaur and see what it's like to go back in the early days
# of Python, way before the f' string format came along. The format()
# function was used before the f' string format came into being.

first_name = 'John'
last_name = 'Smith'
age = 25

print('{} {} is {} years old using old format().'.format(first_name,last_name,age))

print('{} {} is {} years old'.format(first_name,last_name,age),'using old format().')

print('{} {} is {} years old'.format(first_name,last_name,age)+' using old format().')

# I am almost a complete Walking Human Computer Science Research Laboratory
# Machine on Two Legs... 😁

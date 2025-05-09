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
seconds = 60
minutes = 60
hours = 24
days1 = 30  # 30 day month
days2 = 31  # 31 day month
days3 = 28  # 28 day month
days4 = 29  # leep year day month

while True:
    try:
        user_input = int(input('Please type number of months: ').strip())
        if user_input <= 0:
            print('No such month exist:')
        elif user_input == 1:
            print(f'{user_input:,} month = {user_input*days1:,} days = \
{user_input*days1*hours:,} hours = {user_input*days1*hours*minutes:,} \
minutes = {user_input*days1*hours*minutes*seconds:,} = seconds:')
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
days2 = 366  # leep year day
weeks = 52
months = 12

while True:
    try:
        user_input = int(input('Please type number of years: ').strip())
        if user_input <= 0:
            print('No such year exist:')
        elif user_input == 1:
            print(f'{user_input:,} year = {user_input*months:,} \
months = {user_input*weeks:,} weeks = {user_input*days1:,} days = \
{user_input*days1*hours:,} hours = {user_input*days1*hours*minutes:,} \
minutes = {user_input*days1*hours*minutes*seconds:,} seconds:')
            break
        else:
            print(f'{user_input:,} years = {user_input*months:,} \
months = {user_input*weeks:,} weeks = {user_input*days1:,} days = \
{user_input*days1*hours:,} hours = {user_input*days1*hours*minutes:,} \
minutes = {user_input*days1*hours*minutes*seconds:,} seconds:')
            break
    except ValueError:
        print('Numbers only please:')

# I am almost a complete Walking Human Computer Science Research Laboratory
# Machine on Two Legs... 😁

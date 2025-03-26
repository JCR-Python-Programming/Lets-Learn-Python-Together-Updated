# Automated List Python program examples:

# Created by Joseph C. Richardson, GitHub.com

# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. Execute/run
# the Python program example below to view your created list of values,
# along with their variable name. Simply highlight all the blue text output,
# and then copy then paste that blue Python Idle text output back into your
# Python Idle editor. Next, execute/run the pasted python code and watch
# it create a list of values, as if you had created the actual Python list and
# layout yourself.

m = 'make'

user_input_data_list_values = [ ]

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "make" to create and view your user
input data list values:''')

while True:
    while True:    
        user_input_value = input(f'\nuser input data list value = ').lower().strip()
        
        user_input_data_list_values.append(user_input_value)
        user_input_data_list_values.sort()

        if user_input_value == m:
            user_input_data_list_values.remove(user_input_value)
            break

    if len(user_input_data_list_values) < 2:
        print(f'\nYour user input data list must be over two values long.')

    else:
        print(
            f'''\nuser_input_data_list_values = {user_input_data_list_values}
\nprint('You have {len(user_input_data_list_values)} user input data list values:')
\nprint(user_input_data_list_values[0])''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. However,
# this time we are forced type text letters only. Execute/run the Python
# program example below to view your created list of values, along with
# their variable name. Simply highlight all the blue text output, and then
# copy then paste that blue Python Idle text output back into your Python
# Idle editor. Next, execute/run the pasted python code and watch it create
# a list of values, as if you had created the actual Python list and layout
# yourself.

m = 'make'

user_input_data_list_values = [ ]

text_error_message = '\ntext letters only please:'

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "make" to create and view your user
input data list values:''')

while True:
    while True:
        user_input_value = input(f'\nuser input data list value = ').lower().strip()

        user_input_data_list_values.append(user_input_value)
        user_input_data_list_values.sort()

        if user_input_value < str([user_input_data_list_values]):
            user_input_data_list_values.remove(user_input_value)
            print(text_error_message)

        elif user_input_value == m:
                user_input_data_list_values.remove(user_input_value)
                break

    if len(user_input_data_list_values) < 2:
        print(f'\nYour user input data list must be over two values long.')

    else:
        print(
            f'''\nuser_input_data_list_values = {user_input_data_list_values}
\nprint('You have {len(user_input_data_list_values)} user input data list values:')
\nprint(user_input_data_list_values[0])''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. However,
# this time we are forced type text numbers only. Execute/run the Python
# program example below to view your created list of values, along with
# their variable name. Simply highlight all the blue text output, and then
# copy then paste that blue Python Idle text output back into your Python
# Idle editor. Next, execute/run the pasted python code and watch it create
# a list of values, as if you had created the actual Python list and layout
# yourself.

m = 9999

user_input_data_list_values = [ ]

text_error_message = '\ntext numbers only please:'

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "9999" to create and view your user
input data list values:''')

while True:
    while True:        
        try:
            user_input_value = int(input(f'\nuser input data list value = ').lower().strip())

            user_input_data_list_values.append(user_input_value)
            user_input_data_list_values.sort()

            if user_input_value == m:
                user_input_data_list_values.remove(user_input_value)
                break
            
        except ValueError:
            print(text_error_message)

    if len(user_input_data_list_values) < 2:
        print(f'\nYour user input data list must be over two values long.')

    else:
        print(
            f'''\nuser_input_data_list_values = {user_input_data_list_values}
\nprint('You have {len(user_input_data_list_values)} user input data list values:')
\nprint(user_input_data_list_values[0])''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Like always, I research when I want to learn something new, or new
# to me. Since the years I've played around with Python programming,
# I never ever explored list comprehension at all. This is like killing two
# birds with one stone's throw. List comprehension shortens for loops
# down when looping through a list, using a for loop right inside the
# list[ ] brackets.

# Create a list of values using list comprehension.

text_list_values = ['dog','cat','bird','fish','turtle']

values = [value for value in text_list_values]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a list of values using list comprehension. Invoke the 'if' and
# 'else' statements that override all values, except the value 'bird'

text_list_values = ['dog','cat','bird','fish','turtle']

values = [value if value == 'bird' else 'frog' for value in text_list_values]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a list of values using list comprehension.

num_list_values = [1,2,3,4,5,6,7,8,9,10]

nums = [value for value in num_list_values]

print(nums)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create an integer number line using list comprehension.

nums = [value for value in range(-10,+11)]

print(nums)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a multi dimensional
# integer list for us with this Python program example: Execute/run
# the Python program example below to view your created list
# of values, along with their variable name. Simply highlight all
# the blue text output, and then copy then paste that blue Python
# Idle text output back into your Python Idle editor. Next, execute/run
# the pasted python code and watch it create a list of values, as
# if you had created the actual Python list and layout yourself.

auto_multi_dimensional_integer_list_creator = [ ]

print('auto_multi_dimensional_integer_list_creator = [')

for i in range(1,11):
    auto_multi_dimensional_integer_list_creator.append(i)
    print(f'{auto_multi_dimensional_integer_list_creator},')

print(']')

print('\nprint(auto_multi_dimensional_integer_list_creator[9][9])')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bonus Python program example: Make this Python program example
# ask the user their first name, last name and their age. If the user types
# incorrect data information, the program will prompt the user to type
# the correct data information allotted. Also if the user's age is less
# than nineteen years old, the program will give the user a sorry message
# that they are not old enough to drink yet.

user_first_name = '\nWhat is your first name please?: '

user_last_name = '\nWhat is your last name please?: '

user_age = 'How old are you?: '

age = 19

age_undefine = f'\nSorry! No such age. Please try again:'

old_enough = 'You are old enough to drink. Get SMASHED!'

not_old_enough = 'You are not old enough to drink yet.'

text_error_message = '\ntext letters only please:'

text_value_error_message = '\ntext numbers only please:'

text_length_message1 = '\nYour first name must be over two characters long.'

text_length_message2 = '\nYour first name must be under ten characters long.'

text_length_message3 = '\nYour last name must be over two characters long.'

text_length_message4 = '\nYour last name must be under ten characters long.'

while True:
    user_input_first_name = input(user_first_name).lower().strip()

    if user_input_first_name < str([user_input_first_name]):
        print(text_error_message)

    elif len(user_input_first_name) < 3:
        print(text_length_message1)

    elif len(user_input_first_name) > 10:
        print(text_length_message2)

    else:
        break

while True:
    user_input_last_name = input(user_last_name).lower().strip()

    if user_input_last_name < str([user_input_last_name]):
        print(text_error_message)

    elif len(user_input_last_name) < 3:
        print(text_length_message3)

    elif len(user_input_last_name) > 10:
        print(text_length_message4)

    else:
        break

while True:
    try:
        user_input_age = int(input(f'\nNice to meet you {user_input_first_name.title()} \
{user_input_last_name.title()}. {user_age}').strip())

        if user_input_age == 18:
            print(f'\nSorry {user_input_first_name.title()}. {not_old_enough} Come back \
in {age-user_input_age} year from now.')
            break

        elif user_input_age == 0:
            print(age_undefine)

        elif user_input_age < age:
            print(f'\nSorry {user_input_first_name.title()}. {not_old_enough} Come back \
in {age-user_input_age} years from now.')
            break

        else:
            print(f'\nCongrats {user_input_first_name.title()}. {old_enough}')
            break

    except ValueError:
        print(text_value_error_message)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

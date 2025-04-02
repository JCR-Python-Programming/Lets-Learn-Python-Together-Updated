# Automated Dictionary Python program examples:

# Created by Joseph C. Richardson, GitHub.com

# Let's use the Python Idle that will help us create a dictionary for us.
# You must type four dictionary keys and values to create your dictionary.
# Execute/run the Python program example below to view your created
# dictionary, along with its variable name. Simply highlight all the blue text
# output, and then copy then paste that blue Python Idle text output back
# into your Python Idle editor. Next, execute/run the pasted Python code
# and watch it create a dictionary, as if you had created the actual Python
# dictionary and layout yourself.

user_input_data_dictionary = { }

keys = user_input_data_dictionary.keys()

values = user_input_data_dictionary.values()

keys_values = 0

print('''
Let me help you create a dictionary with Python. Please
type each data dictionary key and value, one at a time,
followed by the "Enter" key:''')

while keys_values < 4:
    user_input_key = input(f'\nPlease type dictionary key{keys_values+1}: ').strip()

    user_input_value = input(f'Please type dictionary value{keys_values+1}: ').strip()

    user_input_data_dictionary.update({user_input_key:user_input_value})

    keys_values += 1

print(f'\nuser_input_data_dictionary = {user_input_data_dictionary}')

print(f'\nHere are your {keys} and {values}:')

print(f'\nYou have {len(keys)} keys and {len(values)} values:')

print(f"\n{user_input_data_dictionary.get('place key here')}")

print(f"\n{user_input_data_dictionary.get('place key here','Key not found:')}")  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a dictionary for us.
# You must type a number of dictionary keys and values to create your
# dictionary. Execute/run the Python program example below to view
# your created dictionary, along with its variable name. Simply highlight
# all the blue text output, and then copy then paste that blue Python Idle
# text output back into your Python Idle editor. Next, execute/run the
# pasted Python code and watch it create a dictionary, as if you had
# created the actual Python dictionary and layout yourself.

user_input_data_dictionary = { }

keys = user_input_data_dictionary.keys()

values = user_input_data_dictionary.values()

keys_values = 0

print('''
Let me help you create a dictionary with Python. Please
type each data dictionary key and value, one at a time,
followed by the "Enter" key:''')

while True:
    try:
        user_input_dectionary_length = int(input(
            '\nHow many keys and values would you like to create?: ').strip())
    except ValueError:
        print('\nNumbers only please: ')
        continue
    break

while keys_values < user_input_dectionary_length:
    user_input_key = input(f'\nPlease type dictionary key{keys_values+1}: ').strip()

    user_input_value = input(f'Please type dictionary value{keys_values+1}: ').strip()

    user_input_data_dictionary.update({user_input_key:user_input_value})

    keys_values += 1

print(f'\nuser_input_data_dictionary = {user_input_data_dictionary}')

print(f'\nHere are your {keys} and {values}:')

print(f'\nYou have {len(keys)} keys and {len(values)} values:')

print(f"\n{user_input_data_dictionary.get('place key here')}")

print(f"\n{user_input_data_dictionary.get('place key here','Key not found:')}")  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a dictionary for us.
# You must type a number of dictionary keys and values to create your
# dictionary. Execute/run the Python program example below to view
# your created dictionary, along with its variable name. Simply highlight
# all the blue text output, and then copy then paste that blue Python Idle
# text output back into your Python Idle editor. Next, execute/run the
# pasted Python code and watch it create a dictionary, as if you had
# created the actual Python dictionary and layout yourself.

user_input_data_dictionary = { }

keys = user_input_data_dictionary.keys()

values = user_input_data_dictionary.values()

keys_values = 0

print('''
Let me help you create a dictionary with Python. Please
type each data dictionary key and value, one at a time,
followed by the "Enter" key:''')

while True:
    try:
        user_input_dectionary_length = int(input(
            '\nHow many keys and values would you like to create?: ').strip())
        if user_input_dectionary_length < 2:
            print(f'\nYour dictionary must be at least two keys and two values long.')
            continue
        else:
            break
    except ValueError:
        print('\nNumbers only please: ')
        continue
    break

while keys_values < user_input_dectionary_length:
    user_input_key = input(f'\nPlease type dictionary key{keys_values+1}: ').strip()

    user_input_value = input(f'Please type dictionary value{keys_values+1}: ').strip()

    user_input_data_dictionary.update({user_input_key:user_input_value})

    keys_values += 1

print(f'\nuser_input_data_dictionary = {user_input_data_dictionary}')

print(f'\nHere are your {keys} and {values}:')

print(f'\nYou have {len(keys)} keys and {len(values)} values:')

print(f"\n{user_input_data_dictionary.get('place key here')}")

print(f"\n{user_input_data_dictionary.get('place key here','Key not found:')}")  # optional

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

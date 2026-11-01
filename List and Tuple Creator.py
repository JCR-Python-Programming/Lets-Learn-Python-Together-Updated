
message = (
  'Create an automated tuple or an automated list. Press "q" to quit.\n',
  'Copy and paste your automated list or tuple into your Python code.')

empty_list = [ ]

print(message[0])

while True:
  
  user_input = input('type text and/or numbers to create sorted tuple values and sorted list values: ')

  if user_input in ('q','Q'):  # lowercase/uppercase characters for Caps Lock and shift keys
    break
  
  empty_list.append(user_input)  # adds new values to tuples and lists

convert_to_set = set(empty_list)  # Get rid of duplicate values

convert_to_list = list(convert_to_set)  # cast to a list

convert_to_list.sort()  # sort the converted list

convert_to_tuple = tuple(convert_to_list)  # cast to a tuple

print('\nYou have',len(convert_to_list),'values:\n')  # assure accurate tuple and list value counts

print(message[1])

print('\nmy_tuple_helper =',convert_to_tuple)  # automated Tuple output

print('\nmy_list_helper =',convert_to_list)  # automated list output



message = (
  'Create an automated tuple or an automated list. Press "q" to quit.\n',
  'Copy and paste your automated list or tuple into your Python code.',
  'type text and/or numbers to create sorted tuple values and sorted list values: ',
  '\nmy_tuple_helper =','\nmy_list_helper =')

empty_list = [ ]

print(message[0])

while True:

  user_input = input(message[2])

  if user_input in ('q','Q'):  # lowercase/uppercase characters for Caps Lock and shift keys
    break

  empty_list.append(user_input)  # adds new values to tuples and lists

convert_to_set = set(empty_list)  # Get rid of duplicate values

convert_to_list = list(convert_to_set)  # cast to a list

convert_to_list.sort()  # sort the converted list

convert_to_tuple = tuple(convert_to_list)  # cast to a tuple

print('\nYou have',len(convert_to_list),'values:\n')  # assure accurate tuple and list value counts

print(message[1])

print(message[3],convert_to_tuple)  # automated Tuple output

print(message[4],convert_to_list)  # automated list output

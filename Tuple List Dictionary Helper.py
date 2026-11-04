
message = (
  '''
Why not become a pragmatical, lazy computer programmer?
Create automated tuples, lists and dictionaries right on the fly.
\nType 'T' or 'L' for tuples and lists, then press the Enter key
to begin. Press 'q' to guit and exit this Python program example.
Type 'D' for dictionaries, then press the Enter key to begin.''',
  '\nREADY: ','q','Q','t','T','l','L','d','D')

def tuple_and_list_helper():

  message = (
    'Create an automated tuple or an automated list. Press "q" to quit.\n',
    'type text and/or numbers to create sorted tuple values and sorted list values: ',
    'q','Q','\nYou have','values:\n','Copy and paste your automated tuple or automated list into your Python program.',
    '\nmy_tuple_helper =','\nmy_list_helper =','\nprint(my_tuple_helper[0])\n\nprint(my_list_helper[0])')

  empty_list = [ ]  # create an empty list

  print(message[0])  # message intro

  while True:

    user_input = input(message[1])  # user_input text values

    if user_input in (message[2],message[3]):break  # lowercase/uppercase characters for Caps Lock and shift keys

    empty_list.append(user_input)  # add new values to tuples and lists

  convert_to_set = set(empty_list)  # cast to a set to get rid of duplicate values

  convert_to_list = list(convert_to_set)  # cast to a mutable list

  convert_to_list.sort()  # sort the converted list

  convert_to_tuple = tuple(convert_to_list)  # cast to a immutable tuple

  print(message[4],len(convert_to_list),message[5])  # assure accurate tuple and list value counts

  print(message[6])  # copy and paste message

  print(message[7],convert_to_tuple)  # automated immutable tuple output

  print(message[8],convert_to_list)  # automated mutable list output

  print(message[9])  # print(my_tuple_helper[0], print(my_list_helper[0])
  

def dictionary_helper():

  message = (
    'Create an automated dictionary. Press "q" to quit.\n','Enter a key: ','q','Q',
    'Enter a value: ','\nYou have','dictionary keys','dictionary values:',
    '\nCopy and paste your automated dictionary into your Python program.',
    '\nmy_dictionary_helper =',"\nprint(my_dictionary_helper.get('get a key','key not found:'))")

  empty_dictionary = { }  # create an empty dictionary

  print(message[0])  # message intro

  while True:

    user_input_key = input(message[1])  # user_input keys

    if user_input_key in (message[2],message[3]):break  # lowercase/uppercase characters for Caps Lock and shift keys

    user_input_value = input(message[4])  # user_input values

    if user_input_value in (message[2],message[3]):break  # lowercase/uppercase characters for Caps Lock and shift keys

    empty_dictionary.update({user_input_key:user_input_value})  # add new keys and value pairs to dictionaries

  print(
    message[5],len(empty_dictionary.keys()),message[6],  # assure accurate key counts
    message[5],len(empty_dictionary.values()),message[7])  # assure accurate value counts

  print(message[8])  # copy and paste message

  print(message[9],empty_dictionary)  # automated dictionary output

  print(message[10])  # print(my_dictionary_helper.get('get a key','key not found:'))

print(message[0])

while True:
  user_input = input(message[1])

  if user_input in (message[2],message[3]):break

  elif user_input in (message[4],message[5],message[6],message[7]):
    tuple_and_list_helper()  

  elif user_input in (message[8],message[9]):
    dictionary_helper()
  else:continue

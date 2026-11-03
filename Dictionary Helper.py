
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

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

  empty_list.append(user_input)  # adds new values to tuples and lists

convert_to_set = set(empty_list)  # cast to a set to get rid of duplicate values

convert_to_list = list(convert_to_set)  # cast to a list

convert_to_list.sort()  # sort the converted list

convert_to_tuple = tuple(convert_to_list)  # cast to a tuple

print(message[4],len(convert_to_list),message[5])  # assure accurate tuple and list value counts

print(message[6])  # copy and paste message

print(message[7],convert_to_tuple)  # automated Tuple output

print(message[8],convert_to_list)  # automated list output

print(message[9])  # print(my_tuple_helper[0], print(my_list_helper[0])

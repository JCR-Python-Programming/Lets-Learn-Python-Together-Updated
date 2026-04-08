# You can do a lot with tuples, lists, dictionaries and sets.

default_tuple = 'Dog','Cat','Mouse','Bird'  # default tuples have no parentheses "()"

tuple_one = ('Dog','Cat','Mouse','Bird')
tuple_two = ('Frog','Toad','Turtle','Lizard')
tuple_three = ('Fly','Ant','Butterfly','Beetle')

print(default_tuple)  # check default tuple values

print(default_tuple[0])  # get a default tuple value

print(tuple_one)  # check tuple values

print(tuple_one[0])  # get tuple values by index number

# Use the enumerate() function to loop through a tuple,
# using only two lines of code; one for the for-index,
# value enumerate() function and the other for the print()
# function. Note: you can also keep the print() function
# on the same line if you like, as shown below.

for index,variable in enumerate(tuple_one):print(index,variable)

# Note: the zip() function only goes to the shortest length
# in a multi tuple. However, you can simply keep them the
# same size such as the list examples above, which shows
# three tuples called tuple_one, tuple_two and tuple_three.
# Each tuple has four values in them. This way, every value
# gets called inside one, single 'print' statement.

for variable1,variable2,variable3 in zip(tuple_one,tuple_two,tuple_three):
  print(variable1,variable2,variable3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
list_one = ['Dog','Cat','Mouse','Bird']
list_two = ['Frog','Toad','Turtle','Lizard']
list_three = ['Fly','Ant','Butterfly','Beetle']

print(list_one)  # check list values

print(list_one[0])  # get list values by index number

# Use the enumerate() function to loop through a list,
# using only two lines of code; one for the for-index,
# value enumerate() function and the other for the print()
# function. Note: you can also keep the print() function
# on the same line if you like, as shown below.

for index,variable in enumerate(list_one):print(index,variable)

# Note: the zip() function only goes to the shortest length
# in a multi list. However, you can simply keep them the
# same size such as the list examples above, which shows
# three lists called list_one, list_two and list_three.
# Each list has four values in them. This way, every value
# gets called inside one, single 'print' statement.

for variable1,variable2,variable3 in zip(list_one,list_two,list_three):
  print(variable1,variable2,variable3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dictionary_one = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}
dictionary_two = {'key1':'Frog','key2':'Toad','key3':'Turtle','key4':'Lizard'}
dictionary_three = {'key1':'Fly','key2':'Ant','key3':'Butterfly','key4':'Beetle'}

print(dictionary_one)  # check dictionary keys and values

print(dictionary_one.keys())  # check dictionary keys

print(dictionary_one.values())  # check dictionary values

print(dictionary_one.get('key1'))  # get a dictionary key

# View keys and values with the items() function.

for keys,values in dictionary_one.items():print(keys,values)

# Use the enumerate() function to loop through a dictionary,
# using only two lines of code; one for the for-key, value
# enumerate() function and the other for the print() function.
# Note: you can also keep the print() function on the same
# line if you like, as shown below.

for keys,values in enumerate(dictionary_one):print(keys,values)

# Note: the zip() function only goes to the shortest length
# in a multi dictionary. However, you can simply keep them
# the same size such as the multi dictionary examples above,
# which shows three dictionaries called dictionary_one,
# dictionary_two and dictionary_three. Each dictionary has
# four values in them. This way, every value gets called inside
# one, single 'print' statement.

# Create a Grand Zip() function to retrieve keys and values from
# multi dictionaries

for variable1,variable2,variable3,variable4,variable5,variable6 in zip(
  dictionary_one.keys(),dictionary_one.values(),
  dictionary_two.keys(),dictionary_two.values(),
  dictionary_three.keys(),dictionary_three.values()):
  print(variable1,variable2,variable3,variable4,variable5,variable6)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dict_one = dict(key1 = 'Dog',key2 = 'Cat',key3 = 'Mouse',key4 = 'Bird')
dict_two = dict(key1 = 'Frog',key2 = 'Toad',key3 = 'Turtle',key4 = 'Lizard')
dict_three = dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle')

print(dict_one)  # check dictionary keys and values

print(dict_one.keys())  # check dictionary keys

print(dict_one.values())  # check dictionary values

print(dict_one.get('key1'))  # get a dictionary key

# View keys and values with the items() function.

for keys,values in dict_one.items():print(keys,values)

# Use the enumerate() function to loop through a dict()
# function, using only two lines of code; one for the for-key,
# value enumerate() function and the other for the print()
# function. Note: you can also keep the print() function on
# the same line if you like, as shown below.

for keys,values in enumerate(dict_one):print(keys,values)

# Note: the zip() function only goes to the shortest length in
# a multi dict() constructor. However, you can simply keep them
# the same size such as the multi dict() constructor examples
# above, which shows three dict constructors called dict_one,
# dict_two and dict_three. Each dictionary has four values in
# them. This way, every value gets called inside one, single
# 'print' statement.

# Create a Grand Zip() function to retrieve keys and values from multi
# dictionary constructors

for variable1,variable2,variable3,variable4,variable5,variable6 in zip(
  dict_one.keys(),dict_one.values(),
  dict_two.keys(),dict_two.values(),
  dict_three.keys(),dict_three.values()):
  print(variable1,variable2,variable3,variable4,variable5,variable6)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
set_one = {'Dog','Cat','Mouse','Bird','Dog'}
set_two = {'Frog','Toad','Turtle','Lizard','Toad'}
set_three = {'Fly','Ant','Butterfly','Beetle','Butterfly'}

print(set_one)  # check random set values

convert_to_list = list(set_one)  # cast random set values into a list

convert_to_list.sort()  # sort converted list values

print(convert_to_list)  # check converted, sorted list values.

print(convert_to_list[0])  # get sorted, converted list values by index number

convert_to_tuple = tuple(convert_to_list)  # cast sorted list values into a tuple

print(convert_to_tuple[0])

# Use the enumerate() function to loop through a set,
# using only two lines of code; one for the for-index
# enumerate() function and the other for the print()
# function. Note: you can also keep the print() function
# on the same line if you like, as shown below.

for set_variable in enumerate(set_one):print(set_variable)

# Note: the zip() function only goes to the shortest length
# in a multi set. However, you can simply keep them the
# same size such as the set examples above, which shows
# three sets called set_one, set_two and set_three. Each
# set has four values in them. This way, every value
# gets called inside one, single 'print' statement.

for set_variable1,set_variable2,set_variable3 in zip(set_one,set_two,set_three):
  print(set_variable1,set_variable2,set_variable3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Multi-Dimensional Tuples, Lists Python Program Examples

# Create a multi-dimensional tuple, then call each index to get their values.

multi_dimensional_tuple = (
  ('Dog','Cat','Mouse','Bird'),
  ('Frog','Toad','Turtle','Lizard'),
  ('Fly','Ant','Butterfly','Beetle'))

print(multi_dimensional_tuple[0][1])  # Cat

print(multi_dimensional_tuple[0][0])  # Dog

print(multi_dimensional_tuple[2][0])  # Fly

print(multi_dimensional_tuple[1][0])  # Frog

# Use the enumerate() function to loop through a multi
# dimensional tuple, using only two lines of code; one
# for the for-index enumerate() function and the other
# for the print() function. Note: you can also keep the
# print() function on the same line if you like, as shown
# below.

for index,variable in enumerate(multi_dimensional_tuple):print(index,variable)

# Note: the zip() function only goes to the shortest length
# in a multi dimensional tuple. However, you can simply keep
# them the same size such as the tuple examples above, which
# shows the multi dimensional tuple. Each tuple has four values
# in them. This way, every value gets called inside one, single
# 'print' statement. Note: you can also keep the print() function
# on the same line if you like, as shown below.

for variable in zip(multi_dimensional_tuple):print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi-dimensional list, then call each index to get their values.

multi_dimensional_list = [
  ['Dog','Cat','Mouse','Bird'],
  ['Frog','Toad','Turtle','Lizard'],
  ['Fly','Ant','Butterfly','Beetle']]

# Create a for loop to sort out a multi-dimensional list.

for i in multi_dimensional_list:i.sort()  # sort the multi-dimensional list

print(multi_dimensional_list)  # check the sorted multi-dimensional list values

print(multi_dimensional_list[0][0])  # Bird

print(multi_dimensional_list[0][1])  # Cat

print(multi_dimensional_list[0][2])  # Dog

print(multi_dimensional_list[0][3])  # Mouse

print(multi_dimensional_list[1][0])  # Frog

print(multi_dimensional_list[1][1])  # Lizard

print(multi_dimensional_list[1][2])  # Toad

print(multi_dimensional_list[1][3])  # Turtle

print(multi_dimensional_list[2][0])  # Ant

print(multi_dimensional_list[2][1])  # Beetle

print(multi_dimensional_list[2][2])  # Butterfly

print(multi_dimensional_list[2][3])  # Fly

# Use the enumerate() function to loop through a multi
# dimensional list, using only two lines of code; one
# for the for-index enumerate() function and the other
# for the print() function. Note: you can also keep the
# print() function on the same line if you like, as shown
# below.

for index,variable in enumerate(multi_dimensional_list):print(index,variable)

# Note: the zip() function only goes to the shortest length
# in a multi dimensional list. However, you can simply keep
# them the same size such as the list examples above, which
# shows the multi dimensional list. Each list has four values
# in them. This way, every value gets called inside one, single
# 'print' statement. Note: you can also keep the print() function
# on the same line if you like, as shown below.

for variable in zip(multi_dimensional_list):print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dictionary_one = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}
dictionary_two = {'key1':'Frog','key2':'Toad','key3':'Turtle','key4':'Lizard'}
dictionary_three = {'key1':'Fly','key2':'Ant','key3':'Butterfly','key4':'Beetle'}

# Create a dictionaries variable for three, separate dictionaries.

dectionaries = [dictionary_one,dictionary_two,dictionary_three]

for keys,values in enumerate(dectionaries):print(values)

# Create a Grand Zip() function to retrieve keys and values from
# three separate dictionaries Note: you can also keep the print()
# function on the same line if you like, as shown below.

for variable in zip(dectionaries):print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Still under construction.....

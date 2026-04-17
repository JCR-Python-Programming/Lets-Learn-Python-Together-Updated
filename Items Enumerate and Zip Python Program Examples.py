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
# in a multi-dimensional tuple. However, you can simply keep
# them the same size such as the tuple examples above, which
# shows the multi-dimensional tuple. Each tuple has four values
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
# in a multi-dimensional list. However, you can simply keep
# them the same size such as the list examples above, which
# shows the multi-dimensional list. Each list has four values
# in them. This way, every value gets called inside one, single
# 'print' statement. Note: you can also keep the print() function
# on the same line if you like, as shown below.

for variable in zip(multi_dimensional_list):print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dictionary_one = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}
dictionary_two = {'key1':'Frog','key2':'Toad','key3':'Turtle','key4':'Lizard'}
dictionary_three = {'key1':'Fly','key2':'Ant','key3':'Butterfly','key4':'Beetle'}

# Create a dictionaries variable for three, separate dictionaries.

dectionaries = dictionary_one,dictionary_two,dictionary_three

# Use the enumerate() function to loop through a variable.
# Note: you can also keep the print() function on the same
# line if you like, as shownNote: you can also keep the
# print() function on the same line if you like, as shown
# below.  below.

for keys,values in enumerate(dectionaries):print(values)

# Create a Grand Zip() function to retrieve keys and values from
# three separate dictionaries Note: you can also keep the print()
# function on the same line if you like, as shown below.

for variable in zip(dectionaries):print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dict_one = dict(key1 = 'Dog',key2 = 'Cat',key3 = 'Mouse',key4 = 'Bird')
dict_two = dict(key1 = 'Frog',key2 = 'Toad',key3 = 'Turtle',key4 = 'Lizard')
dict_three = dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle')

# Create a dictionaries variable for three, separate dictionaries.

dicts = dict_one,dict_two,dict_three

# Use the enumerate() function to loop through a variable.
# Note: you can also keep the print() function on the same
# line if you like, as shownNote: you can also keep the
# print() function on the same line if you like, as shown
# below.  below.

for keys,values in enumerate(dicts):print(values)

# Create a Grand Zip() function to retrieve keys and values from
# three separate dictionaries Note: you can also keep the print()
# function on the same line if you like, as shown below.

for variable in zip(dicts):print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
set_one = {'Dog','Cat','Mouse','Bird','Dog'}
set_two = {'Frog','Toad','Turtle','Lizard','Toad'}
set_three = {'Fly','Ant','Butterfly','Beetle','Butterfly'}

# Create a sets variable for three, separate sets.

sets = set_one,set_two,set_three

# Use the enumerate() function to loop through a variable.
# Note: you can also keep the print() function on the same
# line if you like, as shownNote: you can also keep the
# print() function on the same line if you like, as shown
# below.  below.

for set_variable in enumerate(sets):print(set_variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a tuple of values using list comprehension.

tuple_one = ('Dog','Cat','Mouse','Bird')
tuple_two = ('Frog','Toad','Turtle','Lizard')
tuple_three = ('Fly','Ant','Butterfly','Beetle')

# This is like killing two birds with one stone's throw. List
# comprehension shortens for loops down when looping
# through a tuple, using a for loop right inside the tuple()
# function. You can use list comprehension with tuples.

values = tuple(value for value in tuple_one)

print(values)

# Invoke the 'if' and 'else' statements that override all values,
# except the value 'Mouse'.

values = [value if value == 'Mouse' else 'OVERRIDE ALL VALUES!' for value in tuple_one]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a list of values using list comprehension.

list_one = ['Dog','Cat','Mouse','Bird']
list_two = ['Frog','Toad','Turtle','Lizard']
list_three = ['Fly','Ant','Butterfly','Beetle']

# This is like killing two birds with one stone's throw. List
# comprehension shortens for loops down when looping
# through a list, using a for loop right inside the list [ ]
# square brackets.

values = [value for value in list_one]

print(values)

# Invoke the 'if' and 'else' statements that override all values,
# except the value 'Mouse'.

values = [value if value == 'Mouse' else 'OVERRIDE ALL VALUES!' for value in list_one]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a dictionary of values using list comprehension.

dictionary_one = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}
dictionary_two = {'key1':'Frog','key2':'Toad','key3':'Turtle','key4':'Lizard'}
dictionary_three = {'key1':'Fly','key2':'Ant','key3':'Butterfly','key4':'Beetle'}

# This is like killing two birds with one stone's throw. List
# comprehension shortens for loops down when looping
# through a dictionary, using a for loop right inside the
# dictionary { } curly braces. You can use list comprehension
# with dictionaries.

values = {value for value in dictionary_one}

print(values)

# Invoke the 'if' and 'else' statements that override all values,
# except the value 'key3'.

values = [value if value == 'key3' else 'OVERRIDE ALL VALUES!' for value in dictionary_one]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the dict() function to create a dictionary of values using list comprehension.

dict_one = dict(key1 = 'Dog',key2 = 'Cat',key3 = 'Mouse',key4 = 'Bird')
dict_two = dict(key1 = 'Frog',key2 = 'Toad',key3 = 'Turtle',key4 = 'Lizard')
dict_three = dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle')

# This is like killing two birds with one stone's throw. List
# comprehension shortens for loops down when looping
# through a dict() function, using a for loop right inside the
# dict() function { } curly braces. You can use list comprehension
# with dictionaries.

values = {value for value in dict_one}

print(values)

# Invoke the 'if' and 'else' statements that override all values,
# except the value 'key3'.

values = [value if value == 'key3' else 'OVERRIDE ALL VALUES!' for value in dict_one]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a set of values using sets for list comprehension.

set_one = {'Dog','Cat','Mouse','Bird','Dog'}
set_two = {'Frog','Toad','Turtle','Lizard','Toad'}
set_three = {'Fly','Ant','Butterfly','Beetle','Butterfly'}

# This is like killing two birds with one stone's throw. List
# comprehension shortens for loops down when looping
# through a set, using a for loop right inside the set( ) function.
# You can use list comprehension with sets.

values = set(value for value in set_one)

print(values)

# Invoke the 'if' and 'else' statements that override all values,
# except the value 'Mouse'.

values = [value if value == 'Mouse' else 'OVERRIDE ALL VALUES!' for value in set_one]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's explore two different ways to create multi-dimensional tuples and lists.

# This is what a multi-dimensional tuple looks like, also known as a 2D tuple
# by Python standards.

multi_dimensional_tuple = (
  ('Dog','Cat','Mouse','Bird'),
  ('Frog','Toad','Turtle','Lizard'),
  ('Fly','Ant','Butterfly','Beetle'))

# To get tuple values from a multi-dimensional tuple requires two indexes [n][n].
# The first index [n] gets each tuple's groups entire values, and the second index
# [n] gets each individual tuple value from these tuple groups. See the examples
# below.

print(multi_dimensional_tuple[0])  # ('Dog', 'Cat', 'Mouse', 'Bird')

print(multi_dimensional_tuple[1])  # ('Frog', 'Toad', 'Turtle', 'Lizard')

print(multi_dimensional_tuple[2])  # ('Fly', 'Ant', 'Butterfly', 'Beetle')

# Get each individual multi-dimensional tuple value example below.

print(multi_dimensional_tuple[0][0])  # Dog

print(multi_dimensional_tuple[1][0])  # Frog

print(multi_dimensional_tuple[2][0])  # Fly
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is what a multi-dimensional list looks like, also known as a 2D list
# by Python standards.

multi_dimensional_list = [
  ['Dog','Cat','Mouse','Bird'],
  ['Frog','Toad','Turtle','Lizard'],
  ['Fly','Ant','Butterfly','Beetle']]

# To get list values from a multi-dimensional list requires two indexes [n][n].
# The first index [n] gets each list's groups entire values, and the second index
# [n] gets each individual list value from these list groups. See the examples
# below.

print(multi_dimensional_list[0])  # ['Dog', 'Cat', 'Mouse', 'Bird']

print(multi_dimensional_list[1])  # ['Frog', 'Toad', 'Turtle', 'Lizard']

print(multi_dimensional_list[2])  # ['Fly', 'Ant', 'Butterfly', 'Beetle']

# Get each individual multi-dimensional list value example below.

print(multi_dimensional_list[0][0])  # Dog

print(multi_dimensional_list[1][0])  # Frog

print(multi_dimensional_list[2][0])  # Fly
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
multi_dimensional_tuple = (
  'Dog','Cat','Mouse','Bird',
  ('Frog','Toad','Turtle','Lizard'),
  'Fly','Ant','Butterfly','Beetle')

# Get each individual multi-dimensional tuple value example below.

print(multi_dimensional_tuple[0])  # Dog

print(multi_dimensional_tuple[1])  # Cat

print(multi_dimensional_tuple[2])  # Mouse

print(multi_dimensional_tuple[3])  # Bird

print(multi_dimensional_tuple[4])  # ('Frog', 'Toad', 'Turtle', 'Lizard')

print(multi_dimensional_tuple[4][0])  # Frog

print(multi_dimensional_tuple[5])  # Fly
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
multi_dimensional_list = [
  'Dog','Cat','Mouse','Bird',
  ['Frog','Toad','Turtle','Lizard'],
  'Fly','Ant','Butterfly','Beetle']

# Get each individual multi-dimensional list value example below.

print(multi_dimensional_list[0])  # Dog

print(multi_dimensional_list[1])  # Cat

print(multi_dimensional_list[2])  # Mouse

print(multi_dimensional_list[3])  # Bird

print(multi_dimensional_list[4])  # ['Frog', 'Toad', 'Turtle', 'Lizard']

print(multi_dimensional_list[4][0])  # Frog

print(multi_dimensional_list[5])  # Fly
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can create multi-dimensional highbred values all under one, single variable.
# Here are some examples of how you can create multi-dimensional highbred values
# that have tuples, lists, dictionaries and sets all under one variable name. You can
# access them all, via their index [n][n] numbers. Here are three, different ways to
# to create multi-dimensional highbred values as follows:

multi_dimensional_highbred = (
  ('Dog','Cat','Mouse','Bird'),
  ['Frog','Toad','Turtle','Lizard'],
  {'key1':'Fly','key2':'Ant','key3':'Butterfly','key4':'Beetle'},
  {'Dog','Cat','Mouse','Bird','Dog','Frog','Toad','Turtle',
   'Lizard','Fly','Ant','Butterfly','Beetle'},)  # you must use a comma ',' here

print(multi_dimensional_highbred[0])  # ('Dog', 'Cat', 'Mouse', 'Bird')

print(multi_dimensional_highbred[0][0])  # Dog

multi_dimensional_highbred[1].sort()  # invoke the sort() function to sort list values

print(multi_dimensional_highbred[1])  # ['Frog', 'Lizard', 'Toad', 'Turtle']

print(multi_dimensional_highbred[1][0])  # Frog

print(multi_dimensional_highbred[2])  # {'key1': 'Fly', 'key2': 'Ant', 'key3': 'Butterfly', 'key4': 'Beetle'}

print(multi_dimensional_highbred[2].get('key1'))  # Fly

print(multi_dimensional_highbred[3])

# {'Ant', 'Dog', 'Mouse', 'Cat', 'Turtle', 'Beetle', 'Toad', 'Butterfly', 'Fly', 'Frog', 'Lizard', 'Bird'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
multi_dimensional_highbred = (
  ('Dog','Cat','Mouse','Bird'),
  ['Frog','Toad','Turtle','Lizard'],
  dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle'),
  {'Dog','Cat','Mouse','Bird','Dog','Frog','Toad','Turtle',
   'Lizard','Fly','Ant','Butterfly','Beetle'},)  # you must use a comma ',' here

print(multi_dimensional_highbred[0])  # ('Dog', 'Cat', 'Mouse', 'Bird')

print(multi_dimensional_highbred[0][0])  # Dog

multi_dimensional_highbred[1].sort()  # invoke the sort() function to sort list values

print(multi_dimensional_highbred[1])  # ['Frog', 'Lizard', 'Toad', 'Turtle']

print(multi_dimensional_highbred[1][0])  # Frog

print(multi_dimensional_highbred[2])  # {'key1': 'Fly', 'key2': 'Ant', 'key3': 'Butterfly', 'key4': 'Beetle'}

print(multi_dimensional_highbred[2].get('key1'))  # Fly

print(multi_dimensional_highbred[3])

# {'Ant', 'Dog', 'Mouse', 'Cat', 'Turtle', 'Beetle', 'Toad', 'Butterfly', 'Fly', 'Frog', 'Lizard', 'Bird'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
multi_dimensional_highbred = (
  tuple(('Dog','Cat','Mouse','Bird')),
  list(('Frog','Toad','Turtle','Lizard')),
  dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle'),
  set(('Dog','Cat','Mouse','Bird','Dog','Frog','Toad','Turtle',
   'Lizard','Fly','Ant','Butterfly','Beetle')))  # you must leave out the comma ',' this time.

print(multi_dimensional_highbred[0])  # ('Dog', 'Cat', 'Mouse', 'Bird')

print(multi_dimensional_highbred[0][0])  # Dog

multi_dimensional_highbred[1].sort()  # invoke the sort() function to sort list values

print(multi_dimensional_highbred[1])  # ['Frog', 'Lizard', 'Toad', 'Turtle']

print(multi_dimensional_highbred[1][0])  # Frog

print(multi_dimensional_highbred[2])  # {'key1': 'Fly', 'key2': 'Ant', 'key3': 'Butterfly', 'key4': 'Beetle'}

print(multi_dimensional_highbred[2].get('key1'))  # Fly

print(multi_dimensional_highbred[3])

# {'Ant', 'Dog', 'Mouse', 'Cat', 'Turtle', 'Beetle', 'Toad', 'Butterfly', 'Fly', 'Frog', 'Lizard', 'Bird'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's put this multi-dimensional highbred variable to work and use its values.

multi_dimensional_highbred = (
  tuple(('Dog','Cat','Mouse','Bird')),
  list(('Frog','Toad','Turtle','Lizard')),
  dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle'),
  set(('Dog','Cat','Mouse','Bird','Dog','Frog','Toad','Turtle',
   'Lizard','Fly','Ant','Butterfly','Beetle')))  # you must leave out the comma ',' this time.

# Let's start with tuple values first with a simple print() function to make things simpler
# to understand. Let's also use the f' string format to make string concatenation much
# more easier. Note: tuples cannot be changed or modified; they are immutable.

print(f'I love my {multi_dimensional_highbred[0][0]} so much...')

print(f'I love my {multi_dimensional_highbred[0][1]} so much...')

print(f'I love my {multi_dimensional_highbred[0][2]} so much...')

print(f'I love my {multi_dimensional_highbred[0][3]} so much...')

print(f'My {multi_dimensional_highbred[0][0]} chases the {multi_dimensional_highbred[0][1]}.')

print(f'My {multi_dimensional_highbred[0][1]} eats the {multi_dimensional_highbred[0][2]}.')

print(f'My {multi_dimensional_highbred[0][3]} flew away on me today...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's get values from a list with the same multi-dimensional highbred variable.

multi_dimensional_highbred = (
  tuple(('Dog','Cat','Mouse','Bird')),
  list(('Frog','Toad','Turtle','Lizard')),
  dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle'),
  set(('Dog','Cat','Mouse','Bird','Dog','Frog','Toad','Turtle',
   'Lizard','Fly','Ant','Butterfly','Beetle')))  # you must leave out the comma ',' this time.

multi_dimensional_highbred[1].sort()  # sort the themulti_dimensional_highbred list

print(f'I love my {multi_dimensional_highbred[1][0]} so much...')

print(f'I love my {multi_dimensional_highbred[1][1]} so much...')

print(f'I love my {multi_dimensional_highbred[1][2]} so much...')

print(f'I love my {multi_dimensional_highbred[1][3]} so much...')

print(f'My {multi_dimensional_highbred[1][0]} chases the {multi_dimensional_highbred[1][1]}.')

print(f'My {multi_dimensional_highbred[1][1]} eats the {multi_dimensional_highbred[1][2]}.')

print(f'My {multi_dimensional_highbred[1][3]} swam away on me today...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's get values from a dictionary with the same multi-dimensional highbred variable.

multi_dimensional_highbred = (
  tuple(('Dog','Cat','Mouse','Bird')),
  list(('Frog','Toad','Turtle','Lizard')),
  dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle'),
  set(('Dog','Cat','Mouse','Bird','Dog','Frog','Toad','Turtle',
   'Lizard','Fly','Ant','Butterfly','Beetle')))  # you must leave out the comma ',' this time.

# this with double quote marks: "key1"

print(f'I love my {multi_dimensional_highbred[2].get("key1")} so much...')

# or this:

print(f"I love my {multi_dimensional_highbred[2].get('key1')} so much...")

# or these with single quote marks: 'key1'

print(f'I love my {multi_dimensional_highbred[2].get('key1')} so much...')

print(f'I love my {multi_dimensional_highbred[2].get('key2')} so much...')

print(f'I love my {multi_dimensional_highbred[2].get('key3')} so much...')

print(f'I love my {multi_dimensional_highbred[2].get('key4')} so much...')

print(f'My {multi_dimensional_highbred[2].get('key1')} \
chases the {multi_dimensional_highbred[2].get('key2')}.')  # invoke the \ for hard returns

print(f'My {multi_dimensional_highbred[2].get('key3')} \
chases the {multi_dimensional_highbred[2].get('key4')}.')  # invoke the \ for hard returns
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Lastly, let's invoke a randomized set from the same multi-dimensional highbred variable.
# Note: sets do not contain indexes [ ] and are always in random order. Sets also get rid of
# any duplicate values, which is what they are mainly used for. However, we can cast sets
# into tuples and lists with indexes [ ], via invoking the tuple() function, or the list() function
# alike. Let's cast a set into a sorted list, and then re-cast the sorted list into a sorted tuple,
# via invoking the tuple() function.

multi_dimensional_highbred = (
  tuple(('Dog','Cat','Mouse','Bird')),
  list(('Frog','Toad','Turtle','Lizard')),
  dict(key1 = 'Fly',key2 = 'Ant',key3 = 'Butterfly',key4 = 'Beetle'),
  set(('Dog','Cat','Mouse','Bird','Dog','Frog','Toad','Turtle',
   'Lizard','Fly','Ant','Butterfly','Beetle')))  # you must leave out the comma ',' this time.

type_cast_to_list = list(multi_dimensional_highbred[3])

type_cast_to_list.sort()  # sort converted list values

type_cast_to_tuple = tuple(type_cast_to_list)

print(type_cast_to_tuple[0])  # Ant

# Tip! You can invoke the sorted() function to sort a list, without sorting the actual list. For example:

my_list = ['Frog','Toad','Turtle','Lizard']

sort_my_list = sorted(my_list)

print(sort_my_list)  # ['Frog', 'Lizard', 'Toad', 'Turtle']

print(my_list)  # ['Frog', 'Toad', 'Turtle', 'Lizard']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to append a value to a list, extend a list with another list, update a
# dictionary and update a set with another set. Here are some examples:

my_list = ['Frog','Toad','Turtle','Lizard']

my_list.sort()  # sort list values

my_list.append('Snake')

print(my_list)  # ['Frog', 'Lizard', 'Toad', 'Turtle', 'Snake']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_list1 = ['Dog','Cat','Mouse','Bird']
my_list2 = ['Frog','Toad','Turtle','Lizard']

my_list1.extend(my_list2)

my_list1.sort()  # sort extended list values

print(my_list1)  # ['Bird', 'Cat', 'Dog', 'Frog', 'Lizard', 'Mouse', 'Toad', 'Turtle']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_dictionary = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}

my_dictionary.update({'key5':'Fish'})

print(my_dictionary)  # {'key1': 'Dog', 'key2': 'Cat', 'key3': 'Mouse', 'key4': 'Bird', 'key5': 'Fish'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_set1 = {'Dog','Cat','Mouse','Bird','Dog'}
my_set2 = {'Fly','Ant','Butterfly','Beetle','Ant'}

my_set1.update(my_set2)

print(my_set1)  # {'Butterfly', 'Fly', 'Cat', 'Mouse', 'Bird', 'Beetle', 'Ant', 'Dog'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Copy a list with the copy() function.

my_list = ['Dog','Cat','Mouse','Bird']

list_copy = my_list.copy()

print(list_copy)  # ['Dog', 'Cat', 'Mouse', 'Bird']

print(list_copy[0])  # Dog
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Copy a dictionary with the copy() function.

my_dictionary = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}

dictionary_copy = my_dictionary.copy()

print(dictionary_copy)  # {'key1': 'Dog', 'key2': 'Cat', 'key3': 'Mouse', 'key4': 'Bird'}

print(dictionary_copy.get('key1'))  # Dog
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Copy a set with the copy() function.

my_set = {'Dog','Cat','Mouse','Bird','Dog'}

set_copy = my_set.copy()

print(set_copy)  # {'Cat', 'Bird', 'Dog', 'Mouse'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pop the last value from a list, via invoking the pop() function.

my_list = ['Dog','Cat','Mouse','Bird']

print(my_list)  # ['Dog', 'Cat', 'Mouse', 'Bird']

my_list.pop()

print(my_list)  # ['Dog', 'Cat', 'Mouse']

# Return popped values from a list, via invoking the pop() function.

my_list = ['Dog','Cat','Mouse','Bird']

popped_value = my_list.pop()

print(popped_value)  # Bird
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pop values from a list, via invoking the pop(n) function.

my_list = ['Dog','Cat','Mouse','Bird']

print(my_list)  # ['Dog', 'Cat', 'Mouse', 'Bird']

my_list.pop(1)

print(my_list)  # ['Dog', 'Mouse', 'Bird']

# Return popped values from a list, via invoking the pop(n) function.

my_list = ['Dog','Cat','Mouse','Bird']

popped_value = my_list.pop(1)

print(popped_value)  # Cat
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Clear all values from a list, via invoking the clear() function.

my_list = ['Dog','Cat','Mouse','Bird']

print(my_list)  # ['Dog', 'Cat', 'Mouse', 'Bird']

my_list.clear()

print(my_list)  # []
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Permanently remove values from a list, via invoking the remove() function.

my_list = ['Dog','Cat','Mouse','Bird']

print(my_list)  # ['Dog', 'Cat', 'Mouse', 'Bird']

my_list.remove('Mouse')

print(my_list)  # ['Dog', 'Cat', 'Bird']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Delete an entire list, along with its name and its values alike.

my_list = ['Dog','Cat','Mouse','Bird']

print(my_list)  # ['Dog', 'Cat', 'Mouse', 'Bird']

del my_list

try:
  print(my_list)
except NameError:
  print('my_list[ ] no longer exists:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Pop values from a dictionary, via invoking the pop() function.

my_dictionary = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}

key = my_dictionary.pop('key3',None)

print(my_dictionary)  # {'key1': 'Dog', 'key2': 'Cat', 'key4': 'Bird'}

print(key)  # Mouse
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Permanently delete keys from a dictionary, via invoking del.

my_dictionary = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}

del my_dictionary['key3']

print(my_dictionary)  # {'key1': 'Dog', 'key2': 'Cat', 'key4': 'Bird'}
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Delete an entire dictionary, along with its name, keys and values alike.

my_dictionary = {'key1':'Dog','key2':'Cat','key3':'Mouse','key4':'Bird'}

del my_dictionary

try:
  print(my_list)
except NameError:
  print('my_dictionary{ } no longer exists:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Replace values inside a tuple, via invoking the replace() function.

my_tuple = ('Dog','Cat','Mouse','Bird'.replace('Bird','Fish'))

print(my_tuple)  # ('Dog', 'Cat', 'Mouse', 'Fish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Replace values inside a list, via invoking the replace() function.

my_list = ['Dog','Cat','Mouse','Bird'.replace('Bird','Fish')]

print(my_list)  # ['Dog', 'Cat', 'Mouse', 'Fish']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Replace string letters, numbers and text strings, via the replace() function.

print('I love my Cat so very much!'.replace('Cat','Dog'))

# or this:

text_string = 'I love my Cat so very much!'

print(text_string.replace('Cat','Dog'))

# or this:

text_string = 'I love my Cat so very much!'.replace('Cat','Dog')

print(text_string)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a dictionary that can loop through integer keys.

my_dictionary = {0:'Fly',1:'Ant',2:'Butterfly',3:'Beetle'}

for i in range(4):
  print(my_dictionary.get(i))

# Note: if no keys are found, the dictionary will say 'None' by default.

for i in range(5):
  print(my_dictionary.get(i))  # None

for i in range(5):
  print(my_dictionary.get(i,'key not found!'))  # optional if key is not found

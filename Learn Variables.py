# These Python programming examples are solely dedicated
# to my Nephew: Mathew, his Fiancée: Kathy and my Best
# Friend and Mentor: Brian, who's last names remain private,
# due to privacy protection rights on their part.

# Let's learn about variables in Python. Variables are like
# containers; you put stuff into them and take stuff out
# of them, as you would a real container. However, we
# call this container a variable that stores values and
# then retrieves values. You put stuff into the container
# or variable in our case, and then take stuff out of the
# container or variable.

# This Python programming topic is strictly for the beginner,
# novice programmer. We will also learn about tuples and
# lists. So let's get right into it. But first, let's learn what a
# simple print() function is, so we can learn what a variable
# is and how to use it in programming.

# Created by Joseph C. Richardson, GitHub.com

# Let's start with a simple print() function so we can have
# a much better understanding of what a variable is.

print('Hello World!')

# Let's place the value 'Hello World!' inside a variable called
# container. We have to use an equals = sign to put the value
# called 'Hello World! into our variable container. See the
# example below:

container = 'Hello World!'

print(container)

# Note: you can use single quote (' ') marks or double quote
# (" ") marks, but you cannot use (' ") or (" ') for example:

print('Hello World!')  # single quote marks

print("Hello World!")  # double quote marks

# You cannot mix single quote marks with double quote
# marks. If you run these two Python program examples
# below, you will get a syntax error message dialog box.

# print('Hello World!")

# print("Hello World!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now learn what variables are and why programmers
# use them. Variables make program code far less bulky and
# far less redundant on the programmer's part. Programmers
# want to reuse code, not recreate or repeat programming code.
# Variables also reduce text errors that the programmer might
# make, such as spelling mistakes in someone's name for
# example. Let's see some examples of variables to get a clear
# understanding of what they are and why programmers use
# them. Let's create a variable called 'container' so we can put
# some stuff into it, and then take stuff out of it, just like a real
# container is used for.

container = 'Hello World!'

print(container)

# Let's create a container, or variable that can add, subtract, multiply
# and divide number values.

num = 5

print(num+num)  # 5+5 = 10, num+num = 10

print(num-num)  # 5-5 = 0, num+num = 0

print(num*num)  # 5*5 = 25, num+num = 25

print(num/num)  # 5/5 = 1.0, num+num = 1.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what tuples are, and how they work. Tuples
# are just like the container. However, tuples can hold
# multiple values, not just one, like our first example shows.
# Tuples are immutable, meaning they cannot be changed
# or modified, whereas lists can be changed or modified,
# or both. We will get to learning all about what lists are.
# But for now, let's learn what tuples can do, and how to
# access values from them.

# This is a tuple by default, without parentheses.

tuple_container = 'Shirts','Pants','Shoes','Socks'

# This is a tuple with parentheses ( ), not a default tuple.

tuple_container = ('Shirt','Pants','Shoes','Socks')

# Let's access values from our tuple container by their index
# values, starting at zero through three.

print(tuple_container[0])  # Shirt

print(tuple_container[1])  # Pants

print(tuple_container[2])  # Shoes

print(tuple_container[3])  # Socks

# Let's check to see if all the values are in our tuple container
# without using their index values, so we can see them all.

print(tuple_container)  # ('Shirt', 'Pants', 'Shoes', 'Socks')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Although, as we learned that tuples are immutable, meaning
# they cannot be changed or modified. However, we can
# create a tuple of number values and make them add, subtract,
# multiply and divide. We just cannot change them or modify
# them in the way that lists can be changed and or modified.
# Here are some examples with numeric tuple values. Let's
# call our tuple container name 'nums'.

nums = (1,2,3,4,5,6,7,8,9,10)

print(nums[0]+nums[3])  # 1+4 = 5, nums[0]+nums[3] = 5

print(nums[3]-nums[0])  # 4-1 = 3, nums[3]-nums[0] = 3

print(nums[4]*nums[1])  # 5*2 = 10, nums[4]-nums[1] = 10

print(nums[9]/nums[1])  # 10/2 = 5.0, nums[9]/nums[1] = 5.0

# Let's check to see if all the values are in our nums variable
# without using their index values, so we can see them all.

print(nums)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what lists are, and how they work. Lists are
# just like the container. However, lists can hold multiple
# values, not just one, like our first example shows. Lists
# are mutable, meaning they can be changed or modified,
# or both, whereas tuples cannot be changed or modified.
# You can sort list values in alphabetical order. You can
# add more list values. We will explore what lists can do
# that tuples cannot do.

# This is a list with square brackets [ ], whereas tuples have
# parentheses ( ).

list_container = ['Shirt','Pants','Shoes','Socks']

# Let's access values from our list container by their index
# values, starting at zero through three.

print(list_container[0])  # Shirt

print(list_container[1])  # Pants

print(list_container[2])  # Shoes

print(list_container[3])  # Socks

# Let's check to see if all the values are in our list container
# without using their index values, so we can see them all.

print(list_container)  # ['Shirt', 'Pants', 'Shoes', 'Socks']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# With lists, not only can you change or modify them, but
# you can also sort lists, whereas tuples cannot be changed,
# modified or sorted. Let's take a look at the sort() function
# so we can sort our list container values in alphabetical
# order.

list_container = ['Shirt','Pants','Shoes','Socks']

# The sort() function alters the list container into alphabetical
# order, as shown below.

list_container.sort()  # Sort values in alphabetical order with the sort() function.

print(list_container)  # ['Pants', 'Shirt', 'Shoes', 'Socks']

# The sorted() function does not directly alter the list container
# like the sort() function does.

list_container = ['Shirt','Pants','Shoes','Socks']

temp_sort= sorted(list_container)

print(temp_sort)  # ['Pants', 'Shirt', 'Shoes', 'Socks']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's add values to our list container with the append() function.

list_container = ['Shirt','Pants','Shoes','Socks']

list_container.append('Belt')  # append() function

print(list_container)  # ['Shirt', 'Pants', 'Shoes', 'Socks', 'Belt']
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's replace text in a sentence with the replace() function.

text_container = 'I like to swim.'

print(text_container.replace('swim','fly'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's have some fun! Let's create a tuple of values that
# will be called by their indexes inside a for-loop, using
# one print() function inside the for-loop.

tuple_container = ('Shirts','Pants','Shoes','Socks')

for i in tuple_container:
    print(i)

# Let's use the prefix: end=' ' to force the print() function
# to keep all the values on one line.

for i in tuple_container:
    print(i,end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a list of values that will be called by their
# indexes inside a for-loop, using one print() function
# inside the for-loop. Let's also sort the list values by
# alphabetical order.

list_container = ['Shirts','Pants','Shoes','Socks']

list_container.sort()  # Sort values in alphabetical order with the sort() function.

for i in list_container:
    print(i)

# Let's use the prefix: end=' ' to force the print() function
# to keep all the values on one line.

for i in list_container:
    print(i,end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a sentence with a tuple, since we won't be
# changing or modifying any values. Let's create a tuple
# of people's name values. Let's invoke the f' string format
# to make string concatenation much easier, and especially
# for the beginner or novice programmer. Curly braces { }
# are used within the f' string format as shown below.

names = ('Mathew','Kathy','Brian')

print(f'Hi {names[0]}. How are you?')
print(f'Hi {names[1]}. How are you?')
print(f'Hi {names[2]}. How are you?')

# Let's create a for-loop to make our python code above
# far less redundant with just one print() function.

for i in names:
    print(f'Hi {i}. How are you?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a sentence with a list, so we can change or
# modify the list values. Let's create a list of people's name
# values. Let's invoke the f' string format to make string
# concatenation much easier, and especially for the beginner
# or novice programmer. Curly braces { } are used within
# the f' string format as shown below.

names = ['Mathew','Kathy','Brian']

names.sort()  # Sort values in alphabetical order with the sort() function.

print(f'Hi {names[0]}. How are you?')
print(f'Hi {names[1]}. How are you?')
print(f'Hi {names[2]}. How are you?')

# Let's create a for-loop to make our python code above
# far less redundant with just one print() function.

for i in names:
    print(f'Hi {i}. How are you?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a list of number values, so we can add more
# if we like.

nums = [1,2,3,4,5,6,7,8,9,10]

nums.append(11)  # append() function

# Check the values to see if they are all there, and to test
# the program to make sure it works okay.

print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Let's call some nums values by their indexes. Note: tuple
# and list indexes always start at zero. Not one.

print(nums[0])  # 1
print(nums[1])  # 2
print(nums[2])  # 3
print(nums[3])  # 4
print(nums[4])  # 5, and so on...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for-loop that will add values to our nums
# list of empty values and check to see if the added values
# are all there.

nums = []  # empty list without values

for i in range(0,11):
    nums.append(i)  # append() function

print(nums)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call a value from the empty list by its index number.

print(nums[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do something a bit more challenging with an empty
# list and an input() function. We will create a while-loop
# and an 'if' statement to allow us to break out of the while-
# loop and see all the empty list values we typed.

empty_list = []  # empty list without values

while True:
    user_input = input(
        "Type a list of values for our empty nums list, \
then press Enter or press 'q' to quit: ").lower().strip()  # strip() clears whitespace
    empty_list.append(user_input)
    if user_input == 'q':
        empty_list.remove('q')  # romove the last value in the empty list
        break

print(empty_list)  # check the values in the empty list

# Call a value from the empty list by its index number.

print(empty_list[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now create an empty list that sorts out our empty
# list values in alphabetical order with the sort() function.

empty_list = []  # empty list without values

while True:
    user_input = input(
        "Type a list of values for our empty list, \
then press Enter or press 'q' to quit: ").lower().strip()  # strip() clears whitespace
    empty_list.append(user_input)
    if user_input == 'q':
        empty_list.remove('q')  # romove the last value in the empty list
        break

empty_list.sort()  # sort the values in the empty list

print(empty_list)  # check the values in the empty list

# Call a value from the empty list by its index number.

print(empty_list[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a list of values and, then remove values we don't
# want in our animals list with the remove() function. Let's also
# add values to our animals list with the append() function.

animals = ['Dog','Cat','Bird','Fish','Bug']

print(animals)  # check the values in the animals list

animals.remove('Bug')
animals.append('Monkey')

print(animals)  # check the values in the animals list

# Call a value from the animals list by its index number.

print(animals[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's pop a value off the animals list with the pop() function.
# The pop() function pops off the very last value from the
# animals list. You can keep popping off values, until they
# are gone.

animals = ['Dog','Cat','Bird','Fish','Bug']

animals.pop()

print(animals)  # ['Dog', 'Cat', 'Bird', 'Fish']

# Pop off values by their index numbers

animals = ['Dog','Cat','Bird','Fish','Bug']

animals.pop(0)

print(animals)  # ['Cat', 'Bird', 'Fish', 'Bug']


animals = ['Dog','Cat','Bird','Fish','Bug']

animals.pop(1)

print(animals)  # ['Dog', 'Bird', 'Fish', 'Bug']


animals = ['Dog','Cat','Bird','Fish','Bug']

animals.pop(2)

print(animals)  # ['Dog', 'Cat', 'Fish', 'Bug']


animals = ['Dog','Cat','Bird','Fish','Bug']

animals.pop(3)

print(animals)  # ['Dog', 'Cat', 'Bird', 'Bug']


animals = ['Dog','Cat','Bird','Fish','Bug']

animals.pop(4)

print(animals)  # ['Dog', 'Cat', 'Bird', 'Fish']

# Return a popped value from the animals list.

animals = ['Dog','Cat','Bird','Fish','Bug']

popped_value = animals.pop(1)

print(popped_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a variable called copy_list_container, so we
# can copy the contents of our list container with the copy()
# function.

list_container = ['Shirts','Pants','Shoes','Socks']

copy_list_container = list_container.copy()

print(copy_list_container)  # check the values in the copy list container.

print(copy_list_container[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's clear out all the values in our list container with the
# clear() function.

list_container = ['Shirts','Pants','Shoes','Socks']

list_container.clear()

print(list_container)  # []
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's permanently delete our list_container as if it does not
# exist at all. If you try and run this very small Python program
# below, you will get this NameError: message, because Python
# thinks no such variable called list_container or values exist.

list_container = ['Shirts','Pants','Shoes','Socks']

del list_container

print(list_container)  # list_container' is not defined

# Traceback (most recent call last):
#   File "C:\Users\mogie54321\Desktop\Learn Variables.py", line 11, in <module>
#     print(list_container)
# NameError: name 'list_container' is not defined
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs...

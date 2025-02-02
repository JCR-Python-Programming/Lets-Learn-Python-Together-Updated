# These Python programming examples are my years, I've invested time
# and learning how to understand computers and programming in general.
# Python programming is seven years still new to me since Christmas
# day, 2017. The more I learned how to program this weird programming
# language, was the more I practiced even harder. The more I learned and
# wanted to learn, was the more I practiced ever more harder. I'm self taught
# with computer programming, which is starting to lead me into stem robotics
# and electronics alike. My fascination with computers began when I was
# twenty one years young in the late summer of 1986, when I finally bought a
# floppy diskette drive and my five and a quarter inch floppy diskettes that came
# in a box of a dozen inside for my brand new Atari computer; we had no internet
# or a mouse. You either played video games on computers back then, or you
# could program them in their programming languages, each computer brand
# had its own programming language back then. Too bad them days are gone.
# The languages were so much more flexible and you had direct random access
# memory allocation, not indirectly like today's programming languages are.
# All I can say is back in the 1980s was when a home computer used to also
# educate you into programming it. My years are catching up now. But I refuse
# to get tired of computer science. I'm almost thirty nine years into understanding
# computers in general. I have fourteen years of programming knowledge.
# I have HTML and some JavaScript experience, due to creating my very own
# website, I no longer have of course. You are all more than welcome to learn
# all I had ever learned, thus far with Python programming. To the novice/beginner,
# this might take quite awhile to learn. But with patience and a dash of practice
# each and every single day, your Python skills will soar...

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
# Let's now learn what variables are and why programmers use them.
# Variables make program code far less bulky and far less redundant
# on the programmer's part. Programmers want to reuse code, not
# recreate or repeat programming code. Variables also reduce text
# errors that the programmer might make, such as spelling mistakes
# in someone's name for example. Let's see some examples of variables
# to get a clear understanding of what they are and why programmers
# use them. Let's create a variable called 'container' so we can put
# some stuff into it, and then take stuff out of it, just like a real container
# is used for.

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
# Let's learn what tuples are, and how they work. Tuples are just like the
# container. However, tuples can hold multiple values, not just one, like
# our first example shows. Tuples are immutable, meaning they cannot
# be changed or modified, whereas lists can be changed or modified,
# or both. We will get to learning all about what lists are. But for now,
# let's learn what tuples can do, and how to access values from them.

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
# Although, as we learned that tuples are immutable, meaning they cannot
# be changed or modified. However, we can create a tuple of number values
# and make them add, subtract, multiply and divide. We just cannot change
# them or modify them in the way that lists can be changed and or modified.
# Here are some examples with numeric tuple values. Let's call our tuple
# container name 'nums'.

nums = (1,2,3,4,5,6,7,8,9,10)

print(nums[0]+nums[3])  # 1+4 = 5, nums[0]+nums[3] = 5

print(nums[3]-nums[0])  # 4-1 = 3, nums[3]-nums[0] = 3

print(nums[4]*nums[1])  # 5*2 = 10, nums[4]-nums[1] = 10

print(nums[9]/nums[1])  # 10/2 = 5.0, nums[9]/nums[1] = 5.0

# Let's check to see if all the values are in our nums variable
# without using their index values, so we can see them all.

print(nums)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what lists are, and how they work. Lists are just like the container.
# However, lists can hold multiple values, not just one, like our first example
# shows. Lists are mutable, meaning they can be changed or modified, or
# both, whereas tuples cannot be changed or modified. You can sort list values
# in alphabetical order. You can add more list values. We will explore what lists
# can do that tuples cannot do.

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
# With lists, not only can you change or modify them, but you can also sort lists,
# whereas tuples cannot be changed, modified or sorted. Let's take a look at the
# sort() function so we can sort our list container values in alphabetical order.

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
# Let's have some fun! Let's create a tuple of values that will be called by their
# indexes inside a for-loop, using one print() function inside the for-loop.

tuple_container = ('Shirts','Pants','Shoes','Socks')

for i in tuple_container:
    print(i)

# Let's use the prefix: end=' ' to force the print() function
# to keep all the values on one line.

for i in tuple_container:
    print(i,end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a list of values that will be called by their indexes inside a for-loop,
# using one print() function inside the for-loop. Let's also sort the list values by
# alphabetical order.

list_container = ['Shirts','Pants','Shoes','Socks']

list_container.sort()  # Sort values in alphabetical order with the sort() function.

for i in list_container:
    print(i)

# Let's use the prefix: end=' ' to force the print() function to keep all the values
# on one line.

for i in list_container:
    print(i,end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a sentence with a tuple, since we won't be changing or modifying
# any values. Let's create a tuple of people's name values. Let's invoke the
# f' string format to make string concatenation much easier, and especially
# for the beginner or novice programmer. Curly braces { } are used within the
# f' string format as shown below.

names = ('Mathew','Kathy','Brian')

print(f'Hi {names[0]}. How are you?')
print(f'Hi {names[1]}. How are you?')
print(f'Hi {names[2]}. How are you?')

# Let's create a for-loop to make our python code above
# far less redundant with just one print() function.

for i in names:
    print(f'Hi {i}. How are you?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a sentence with a list, so we can change or modify the list values.
# Let's create a list of people's name values. Let's invoke the f' string format to
# make string concatenation much easier, and especially for the beginner or
#vnovice programmer. Curly braces { } are used within the f' string format as
# shown below.

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
# Let's create a for-loop that will add values to our nums list of empty values
# and check to see if the added values are all there.

nums = []  # empty list without values

for i in range(0,11):
    nums.append(i)  # append() function

print(nums)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call a value from the empty list by its index number.

print(nums[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do something a bit more challenging with an empty list and an input()
# function. We will create a while-loop and an 'if' statement to allow us to break
# out of the while-loop and see all the empty list values we typed.

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
# Let's now create an empty list that sorts out our empty list values in alphabetical
# order with the sort() function.

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
# Let's create a list of values and, then remove values we don't want in our animals
# list with the remove() function. Let's also add values to our animals list with the
# append() function.

animals = ['Dog','Cat','Bird','Fish','Bug']

print(animals)  # check the values in the animals list

animals.remove('Bug')
animals.append('Monkey')

print(animals)  # check the values in the animals list

# Call a value from the animals list by its index number.

print(animals[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's pop a value off the animals list with the pop() function. The pop() function
# pops off the very last value from the animals list. You can keep popping off
# values, until they are gone.

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
# Let's create a variable called copy_list_container, so we can copy the contents
# of our list container with the copy() function.

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
# Let's permanently delete our list_container as if it does not exist at all.
# If you try and run this very small Python program below, you will get
# this NameError: message, because Python thinks no such variable
# called list_container or values exist.

list_container = ['Shirts','Pants','Shoes','Socks']

del list_container

print(list_container)  # list_container' is not defined

# Traceback (most recent call last):
#   File "C:\Users\mogie54321\Desktop\Learn Variables.py", line 11, in <module>
#     print(list_container)
# NameError: name 'list_container' is not defined
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# List Comprehension in Python

# Like always, I research when I want to learn something new, or new to me.
# Since the years I've played around with Python programming, I never ever
# explored list comprehension at all. This is like killing two birds with one stone's
# throw. I'm only experimenting with this tonight; I kept on ignoring it. But it
# shortens for loops down, when looping through a list, using a for loop right
# inside the list[ ] brackets. Believe it or not, I'm also new to this list comprehension
# thing. So you are not alone on this one. But try these out and tinker with them.
# I did that here. I just play and tinker and see what works and what won't work.
# This is what computer science is all about. Sometimes you just have to keep on
# learning and do constant research; you can only avoid something for so long,
# like I did with this headache. But like everything we learn; it gets easier over time.
# Happy researching. I'm also happily doing research with these below.

text_list = ['dog','cat','bird','fish','turtle']

words = [text for text in text_list]
print(words)

text_list = ['dog','cat','bird','fish','turtle']

words = [text if text == 'dog' else 'none' for text in text_list]
print(words[1])

num_list = [1,2,3,4,5]

nums = [num for num in num_list]
print(nums)

num_list = []

nums = [num for num in range(20)]
print(nums)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's fully understand what a 2d list is truly all about.
# A 2d list is a two dimensional array that can hold multiple
# 2d list array values under a single variable. For example:

my_2d_list=['2d list0'],['2d list0']

print(my_2d_list[0][0])
print(my_2d_list[1][0])

# If you create a really long 2d list such as this example below,
# you can force hard line-breaks, but you must use outer square
# brackets '[]' to surround the entire 2d list values. Note: you
# must use commas at the end of each 2d list array.

# Example 1:

my_2d_list=['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0']

print(my_2d_list[4][0])

# Example 2:

my_2d_list=[ # use a hard line-break make the 2d list look neat and tidy.
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0']] # use a hard line-break to add more values to the 2d list.

print(my_2d_list[4][0])

# Create a multi-2d list array like this example below illustrates.

my_multi_2d_list=['Value0','Value1','Value2'],['Value0','Value1','Value2']

print(my_multi_2d_list[0][0])
print(my_multi_2d_list[0][1])
print(my_multi_2d_list[0][2])

print(my_multi_2d_list[1][0])
print(my_multi_2d_list[1][1])
print(my_multi_2d_list[1][2])

# You can create as many multi-2d list array values as you please.
# For example:

my_multi_2d_list=[
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2','Value3'],
    ['Value0','Value1','Value2','Value3','Value4']] # neat and tidy

print(my_multi_2d_list[0][2])
print(my_multi_2d_list[1][3])
print(my_multi_2d_list[2][4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's have some multi-2d list fun using a for-loop
# and see what happens when we execute/run this multi-2d
# list, for-loop example:

my_multi_2d_list=[
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2']] # neat and tidy

for i in my_multi_2d_list:
    print(i[0],i[1],i[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a real, working multi-2d list to see what
# they are truly all about in a real Python program scenario.
# We will call our multi-2d list, 'names'. Use the (f') format
# to make the 'print' statement easier to concatenate strings.

names=[
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']] # neat and tidy

for i in names:
    print(f'{i[0]}, {i[1]} and {i[2]} went to the store.')

# Let's create a looping sentence tuple with our multi-2d list for-loop
# example and see what happens when we execute/run this Python
# program example below.

names=[
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']] # neat and tidy

sentence=(
    ('went home to have dinner.',
    'went to the store to buy some food.',
    'wanted some pizza for breakfast.',
    'wanted computers for Christmas.',
    'love their computers.'))

for i in range(4):
        print(f'{names[i][0]}, {names[i][1]} \
and {names[i][2]} {sentence[i]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what Python dictionaries are all about with these
# Python program examples.

# print out key values onto the screen output

my_dictionary = {
    'key1':'Python','key2':"Programmer's",'key3':'Glossary','key4':'Bible'}

print(my_dictionary.get('key1'))

print(my_dictionary.get('key2'))

print(my_dictionary.get('key3'))

print(my_dictionary.get('key4'))

print(my_dictionary.get('key5'))

print(my_dictionary.get('key5','Key Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# print out key values with a partial tuple within 'my_dictionary_list'

my_dictionary_tuple = {
    'key1':'Python','key2':("Programmer's",'Glossary','Bible'),'key3':'is','key4':'Great!'}

print(my_dictionary_tuple.get('key1'))

print(my_dictionary_tuple.get('key2')[0])

print(my_dictionary_tuple.get('key2')[1])

print(my_dictionary_tuple.get('key2')[2])

print(my_dictionary_tuple.get('key3'))

print(my_dictionary_tuple.get('key4'))

print(my_dictionary_tuple.get('key1','Key Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# print out key values with a partial list within 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

print(my_dictionary_list.get('key1'))

print(my_dictionary_list.get('key2')[0])

print(my_dictionary_list.get('key2')[1])

print(my_dictionary_list.get('key2')[2])

print(my_dictionary_list.get('key3'))

print(my_dictionary_list.get('key4'))

print(my_dictionary_list.get('key5','Key Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# update a key's value to change its value in 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list.update({'key1':'Book'})  # key1 value was 'Python'

print(my_dictionary_list.get('key1'))  # Book
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# update a key's value to change its value in 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list['key1'] = 'Book'  # key1 value was 'Python'

print(my_dictionary_list.get('key1'))   # Book
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'pop()' function to delete/pop 'key2' from 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list.pop('key2')

print(my_dictionary_list.get('key2','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# return a 'poopped' dictionary{ } 'key' from 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

popped = my_dictionary_list.pop('key1')

print(popped)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# completely delete a dictionary{ } 'key' from 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

del my_dictionary_list['key1']

print(my_dictionary_list.get('key1','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# clear the entire 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list.clear()

print(my_dictionary_list.get('key1','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'items()' function to view the complete 'my_dictionary_list'
# with 'keys' and 'key values'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

list_items = my_dictionary_list.items()

print(list_items)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'items()' function to view the 'my_dictionary_list' 'keys' and 'key values'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

# invoke the 'items()' function to view the 'my_dictionary_list' 'keys' only

print(my_dictionary_list.keys())

# invoke the 'items()' function to view the 'my_dictionary_list' 'values' only

print(my_dictionary_list.values())

# invoke the 'items()' function using a for loop to view the 'my_dictionary_list'
# 'keys' and 'key values'

for keys, values in my_dictionary_list.items():
  print(keys, values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# change a key's value in 'my_dictionary_list'

my_dictionary_list = {
    'key1':'Python','key2':["Programmer's",'Glossary','Bible'],'key3':'is','key4':'Great!'}

my_dictionary_list['key1'] = 'We Sure Love Python!'

print(my_dictionary_list.get('key1'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create an animals dictionary so we can use its values.

animals={
    'Dog':'Wolf',
    'Cat':'Lion',
    'Bird':'Eagle',
    'Fish':'Shark'
    }

print(animals.get('dog'))

print(animals.get('dog','Not Found!'))  # optional

print(animals.get('Dog','Not Found!'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for key,value in animals.items():
    print(key)

for key,value in animals.items():
    print(value)

for key,value in animals.items():
    print(key,value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some sentences out of our animals dictionary list.

d=animals.get('Dog')
c=animals.get('Cat')
b=animals.get('Bird')
f=animals.get('Fish')

print(f'My dog is really a {d}.')
print(f'My Cat is really a {c}.')
print(f'My Bird is really a {b}.')
print(f'My Fish is really a {f}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some sentences out of our animals dictionary list using a 'for in'
# items() function to drastically reduce lines of code and code redundancy
# in our Python program example.

for keys,values in animals.items():
    print(f'My {keys} is really a {values}.')

# Rename the key and value variables if you wish.

for my_keys,my_values in animals.items():
    print(f'My {my_keys} is really a {my_values}.')

for animal_keys,animal_values in animals.items():
    print(f'My {animal_keys} is really a {animal_values}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try this dictionary Python program example below and recap what happens
# when you type and execute/run this program.

animals={
    'Dog':'Wolf',
    'Cat':'Lion',
    'Bird':'Eagle',
    'Fish':'Shark'}

people={
    'Person1':'Tom',
    'Person2':'Bob',
    'Person3':'Rob',
    'Person4':'Ron'}

for key,value in animals.items():
    print(key,value)

for key,value in people.items():
    print(key,value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a dictionary that's also a complete list of values
# to one, single key each.

my_dictionary_list={
  'key1':['Dog,','Cat','Bird','fish'],
  'key2':['Tom','Bob','Rob','Ron']}

print(my_dictionary_list.get('key1')[0])

print(my_dictionary_list.get('key2')[0])

print(my_dictionary_list.get('key5','Sorry! Key Not Found:'))  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a dictionary that uses strings as keys and values, instead of
# of actual text, like we did before. Let's create two, simple tuples; one for
# the key tuple and one for the value tuple. We can also create them with or
# without parentheses, but a '\' backslash must be implemented in place of the
# parentheses. However, the Python programming standard shows only the
# constant use of parentheses, not backslashes, as you can see in the next
# example below.

key='dog','cat','mouse','bird','fish' # tuple by default

value=(
    'Grey Wolf','Huge Tigger',
    'Black Rat','Macaw Parrot',
    'Great White Shark') # create a tuple with '()' parentheses.

# Why use '()' parentheses when you can simply use the '\' backslash instead.
# Note: '\' is not the usual Python programming standard, but it works. Now,
# however, this only acts like a tuple by default, not a list as one would think.
# You cannot change or modify tuple values at all; they are immutable, not
# mutable like lists. Even though this works, it's not viable, especially when
# you need to create a mutable list, not an immutable tuple, as this example
# does by default. You must use either '()' parentheses for tuples, '[]' square
# brackets for lists and '{}' curly braces for dictionaries and sets alike.

key='dog','cat','mouse','bird','fish' # tuple by default

value=\
        'Grey Wolf','Huge Tigger',\
        'Black Rat','Macaw Parrot',\
        'Great White Shark' # tuple by default

dictionary={ # dictionary
    key[0]:value[0],
    key[1]:value[1],
    key[2]:value[2],
    key[3]:value[3],
    key[4]:value[4]
    }

# Non formatted examples with commas ',' and plus '+' signs

for keys,values in dictionary.items():
    print('My '+keys+' is really a '+values+'.')

for keys,values in dictionary.items():
    print('My',keys,'is really a',values+'.')

# Old formatted example: now depreciated in Python 3 and up.
# Can still be used in Python 3, thus far.

for keys,values in dictionary.items():
    print('My {} is really a {}.'.format(keys,values))

# New formatted example: Python 3 and up.

for keys,values in dictionary.items():
    print(f'My {keys} is really a {values}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# create a dictionary

print(dict(
  we='Python',sure="Programmer's",love='Glassary',Python='Bible'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'join()' function to join dictionary keys together
# with a separator '//' string. The separator string can
# be any character/characters; two backslashes '//' are
# used for this Python program example.

dictionary_join = {
    'key1':'Python','key2':"Programmer's",'key3':'Glossary','key4':'Bible'}

separater = '//'

print(separater.join(dictionary_join))

print(separater.join(dictionary_join.get('key1')))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python dictionaries are pretty neat for data manipulation. You can call keys
# to return values. You can also use integers for keys and values to completely
# manipulate data

# dictionary 'keys' return values. Note: the word key can be any name you like.
# Play with the text values and make sentences out of them.

dictionary = {
    'key 1':'Value 1','key 2':'Value 2','key 3':'Value 3',
    'key 4':'Value 4','key 5':'Value 5','key 6':'Value 6',
    'key 7':'Value 7','key 8':'Value 8'}

# use a variable if you like

key = dictionary.get('key 4')

print(key)

# or this:

key = dictionary.get('key 11','Key Not Found:')  # KNF optional

print(key)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dictionary = {
    'key 1':'Value 1','key 2':'Value 2','key 3':'Value 3',
    'key 4':'Value 4','key 5':'Value 5','key 6':'Value 6',
    'key 7':'Value 7','key 8':'Value 8'}

# loop through dictionary keys

for i in dictionary:
    print(i)

# loop through the dictionary values

for i in dictionary:
    print(dictionary.get(i))

# loop through dictionary keys and values

for i in dictionary:
    print(i,dictionary.get(i))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use integers as dictionary keys to return values

dictionary = {
    1:'Value 1',2:'Value 2',3:'Value 3',
    4:'Value 4',5:'Value 5',6:'Value 6',
    7:'Value 7',8:'Value 8'}

# use a variable if you like

key = dictionary.get(4)

print(key)

# or this:

key = dictionary.get(11,'Key Not Found:')  # KNF optional

print(key)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# this is pure data manipulation at its finest.
# Use integer numbers for keys instead of text strings

dictionary = {
    1:'Value 1',2:'Value 2',3:'Value 3',
    4:'Value 4',5:'Value 5',6:'Value 6',
    7:'Value 7',8:'Value 8'}

print(dictionary.get(1+2+5))

print(dictionary.get(2*5-2))

print(dictionary.get(16/2))

print(dictionary.get(16/2+1,'Key Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use integers for keys and values for total data manipulation

dictionary = {
    1:100,2:200,3:300,
    4:400,5:500,6:600,
    7:700,8:800}

# add up all the keys

print(sum(dictionary.keys()))

# add up all the values

print(sum(dictionary.values()))

# add up all the keys and values together

sum_num1 = sum(dictionary.keys())

sum_num2 = sum(dictionary.values())

print(sum_num1+sum_num2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# calculate the values in a dictionary. If a key is not found, the try and
# except handler will execute and the finally handler executes no matter
# the outcome.

dictionary = {
    1:100,2:200,3:300,
    4:400,5:500,6:600,
    7:700,8:800}

try:
    values = dictionary.get(8)+dictionary.get(9)

    print(values)

except TypeError:
    print('keys cannot be solved. Not enough values:')

finally:
    print('finally executes no matter the outcome.')  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Have some fun with Python Sets.

animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

animals1.update(animals2)

animals1.add('Frog')

animals1.discard('Rat')

print(animals1)

'''
.add()
.clear()
.copy()
.difference()
.difference_update()
.discard()
.intersection()
.intersection_update()
.isdisjoint()
.issubset()
.issuperset()
.pop()
.remove()
.symmetric_difference()
.symmetric_difference_update()
.union()
.update()
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use the dict() function to create a dictionary, via the screen output

make_dictionary = dict(key1='Value 1',key2='Value 2',key3='Value 3')

print(make_dictionary)  # {'key1': 'Value 1', 'key2': 'Value 2', 'key3': 'Value 3'}

print(make_dictionary.get('key1'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Have some fun with Python Sets.

animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

animals1.update(animals2)

animals1.add('Frog')

animals1.discard('Rat')

print(animals1)

'''
.add()
.clear()
.copy()
.difference()
.difference_update()
.discard()
.intersection()
.intersection_update()
.isdisjoint()
.issubset()
.issuperset()
.pop()
.remove()
.symmetric_difference()
.symmetric_difference_update()
.union()
.update()
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use the dict() function to create a dictionary, via the screen output

make_dictionary = dict(key1='Value 1',key2='Value 2',key3='Value 3')

print(make_dictionary)  # {'key1': 'Value 1', 'key2': 'Value 2', 'key3': 'Value 3'}

print(make_dictionary.get('key1'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Check to see if there are any duplicate names, using a set. Sets always display
# values in random order, such as this set_demo example below illustrates. This
# means that every time you execute/run the set_demo program example, the
# values will always be in random order. However, sets are designed to get rid
# of duplicate values. Note: sets do not use indexing, such as tuples and lists do.

set_demo={'Tom','Bob','John','Ron','Tom'}

print(set_demo)

# If you try to run this one-line 'print' statement, you will get a type error.
# message as illustrated below.

print(set_demo[1])

'''
Traceback (most recent call last):
  File "C:/Users/Brian D/Desktop/JCR/GITFiles/Sets Examples.py", line 16, in <module>
    print(set_demo[1])
TypeError: 'set' object is not subscriptable
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's convert a set into a tuple, complete with indexing.

set_demo={'Tom','Bob','John','Ron','Tom'}

convert=tuple(set_demo)

print(convert[1])

# If you re-execute/run the set_demo program example above, it will
# still return a random value from the converted set, even though it
# has an index list range. To solve this problem, we need to use the
# 'sort()' function or the 'sorted() function. Also note that tuples cannot
# be changed or sorted, but lists can be changed and sorted
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's convert a set into a sorted list, complete with indexing. The
# 'sorted()' function only affects the output of the list, not the actual list
# itself, whereas the 'sort()' function changes the actual list, such as in
# our next example shows.

set_demo={'Tom','Bob','John','Ron','Tom'}

convert=list(set_demo)

sorted_index=sorted(convert)

print(sorted_index)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is almost the very same set_demo program example as illustrated
# above but with one exception, the actual list gets sorted, which in most
# cases, that's not always what you want. Therefore, the 'sorted()' function
# is used to prevent actual list modifications.

set_demo={'Tom','Bob','John','Ron','Tom'}

convert=list(set_demo)

convert.sort()

print(convert)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The set_demo program example below does everything the above program
# example illustrated. The only difference, is that there are two sets, which
# we are going to extend both sets into one, single list. We will create two sets
# called set_demo1 and set_demo2 so we can extend them into one, single
# sorted list without duplicate values. We will also use what's called 'unpacking',
# which simply means to unpack two or more variables and two or more values,
# using just one '=' sign.

# convert1,convert2=list(set_demo1),list(set_demo2)

set_demo1={'Tom','Bob','John','Ron','Tom'}
set_demo2={'Tamy','Sandy','Mandy','Randy','Tamy'}

convert1,convert2=list(set_demo1),list(set_demo2)

convert1.extend(convert2)

sorted_index=sorted(convert1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Check the values first to make sure they are correctly sorted and such.

print(sorted_index)

# Let's create a sentence out of our sorted_index argument like this.

print(sorted_index[0],'is a great name.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for-loop to loop through our sorted_index variable, and creat a
# sentence within our for-loop.

for i in sorted_index:
    print(i,'is a great name')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

print(animals1.union(animals2)) # Union
print(animals1|animals2) # Union

print(animals1.intersection(animals2)) # Intersection
print(animals1 & animals2) # Intersection

print(animals1.difference(animals2)) # Difference
print(animals1 - animals2) # Difference

print(animals1 ^ animals2) # Symmetric Difference

x=animals1.symmetric_difference_update(animals2) # Symmetric Difference Update
print(animals1)

# Why not use these shortcuts instead.

print(animals1 | animals2)  # Union
print(animals1 & animals2)  # Intersection
print(animals1 - animals2)  # Difference
print(animals1 ^ animals2)  # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

x=animals1 | animals2
for i in x:
    print(i)

animals1.update(animals2)
for i in animals1:
    print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
animals1,animals2=(
    {'Dog','Cat','Bird','Fish','Dog','Bird'},
    {'Bat','Rat','Mouse','Monkey','Dog','Fish','Cat'})

animals1.update(animals2)

convert=list(animals1)

x=sorted(convert)
for i in x:
    print(i)

x=sorted(convert,reverse=True)
for i in x:
    print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# packing and unpacking integer sets using one equals = sign

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

print(set1,set2,set3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# add up all the integer values in each set with the sum() function,
# then add up all the sets together

set1,set2,set3 = (
    {1,2,3,4,5},  # set1 = 15
    {6,7,8,9,10},  # set2 = 40
    {11,12,13,14,15})  # set3 = 65

set_total_sum = sum(set2)+sum(set3)  # 15+40+55 = 120

print(set_total_sum)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the enumerate() function to loop through a set of values

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

for x,y in enumerate(set1):print(y)

for x,y in enumerate(set2):print(y)

for x,y in enumerate(set3):print(y)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the zip() function to loop through a set of values.
# Note: the zip() function must contain exactly the same
# number of value items; the shortest value set will cut off
# values in the other sets

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

for x,y,z in zip(set1,set2,set3):print(x,y,z)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# join two sets of values into a larger set of values

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

print(set1.union(set2)) # Union

print(set2.union(set3)) # Union
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use these shortcuts

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

print(set1|set2) # Union

print(set2|set3) # Union
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# intersect two sets; if their values have one or more values
# the same, they will be displayed. If not the same, nothing
# will be displayed

set1,set2,set3 = (
    {1,2,3,4,15},
    {7,8,9,10,15},
    {11,12,13,14,15})

print(set1.intersection(set2)) # Intersection

print(set2.intersection(set3)) # Intersection
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use these shortcuts

set1,set2,set3 = (
    {1,2,3,4,15},
    {7,8,9,10,15},
    {11,12,13,14,15})

print(set1&set2) # Intersection

print(set2&set3) # Intersection
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# the difference method will only show the values of set1 and any
# like values in set2 and set3 as well as set1 won't be diplayed on
# the screen output in set1

set1,set2,set3 = (
    {1,2,3,4,15},
    {7,8,9,10,15},
    {11,12,13,14,15})

print(set1.difference(set2)) # Difference

print(set2.difference(set3)) # Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use these shortcuts

set1,set2,set3 = (
    {1,2,3,4,15},
    {7,8,9,10,15},
    {11,12,13,14,15})

print(set1-set2) # Difference

print(set2-set3) # Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# the symmetric difference method will show the values of set1,
# set2 and set3 and any like values in set2 and set3 as well as
# set1 won't be diplayed on the screen output in all three sets

set1,set2,set3 = (
    {1,2,3,4,15},
    {7,8,9,10,15},
    {11,12,13,14,15})

print(set1.symmetric_difference(set2)) # Symmetric Difference

print(set2.symmetric_difference(set3)) # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use these shortcuts

set1,set2,set3 = (
    {1,2,3,4,15},
    {7,8,9,10,15},
    {11,12,13,14,15})

print(set1^set2) # Symmetric Difference

print(set2^set3) # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# the symmetric difference update method will remove the values
# of set1, set2 and set3

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

print(set1.symmetric_difference_update(set2)) # Symmetric Difference Update

print(set2.symmetric_difference_update(set3)) # Symmetric Difference Update
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Why not use these shortcuts instead.

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 - set2)  # Difference
print(set1 ^ set2)  # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Create three different integer sets that will combine/unionize all three sets into one
single set. Convert the single set into a list, using the list() function. Next, view the
contents of the list, along with the slice() function to set the range of list content
values to display on the screen.

Type and execute/run this Python program example below.
'''
# To reduce lines of code, create packed variables and their
# packed values.

x,y,z=(
    {1,2,3,4,9,6,7,8,5,9,10},
    {11,12,13,14,15,16,17},
    {18,19,20,21,22,23,24})

a=slice(24) # slice the set with the slice() function

# To reduce lines of code, create packed variables and their
# packed values.

length1,length2,length3=len(x),len(y),len(z)

unionize=x.union(y,z) # unionize x to y and z with the value v.union() function

convert=list(unionize) # cast the set to a list with the list() function

answer=length1,length2,length3

# Add the total values between length1, length2 and length3 with the sum()
# function.

total_sum=sum(answer) # add all three values of answer together with the sum() function

# View the contents of x, y and z in their combined, converted sets to a list.

print('View the value contents of the unionized list to check it:\n\n'+str(convert[a]))

# Create a variable called sentence_loop, along with all its values.

sentence_loop=(
    f'\nThe length of (x) = {length1}',f'The length of (y) = {length2}',
    f'The length of (z) = {length3}',f'\nThe total lengths of x+y+z = {total_sum}')

# Create a for loop that will loop through the sentence_loop variable, using a
# single print() function. The for loop will iterate until all the values are cycled
# through the sentence_loop variable.

for i in sentence_loop:print(i)

x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y).union(z)

convert=list(unionize)

a=slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y,z)

convert=list(unionize)

a=slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a=list()
for i in range(10):
    a.append(i)

b=set()
for i in range(10):
    b.add(i)

print(a)
print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference

nums1={1,1,2,3,4,5,6}
nums2={1,2,2,3,4}

print(nums1.symmetric_difference(nums2)) # Symmetric Difference

print(nums1 ^ nums2) # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1={0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2={1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2) # Union
print(nums1 & nums2) # Intersection
print(nums1 - nums2) # Difference
print(nums1 ^ nums2) # Symmetric Difference

nums1=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]
nums2=[1,2,3,1,3,4,10,5,6,6,7,8,9,10]

uniques1=set(nums1)
uniques2=set(nums2)

print(uniques1 | uniques2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# input Fibonacci Number Sequence example, using a set{}

num1,num2=0,1

fib={num1,num2}

words=(
    'is in the Fibonacci Sequence.',
    'is not in the Fibonacci Sequence.',
    'Please enter a correct Fibonacci Sequence Number: ',
    'Sorry! Numbers only.',
    'Memory Error!'
    )

try:
    x=int(input(words[2]).strip())

    for i in range(x):
        fib_num=num1+num2
        fib.add(fib_num)
        num1=num2
        num2=fib_num

    if x in fib:
        print(x,words[0])

    elif x not in fib:
        print(x,words[1])

except ValueError:
    print(words[3])

except MemoryError:
    print(words[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python sets{ } are great to use with numbers. Using numbers
# in sets won't come out in random order, whereas using text
# strings will always be in random order. Using numbers with
# sets will always be in order, no matter where values are placed
# within the set's parentheses.

num_set = {9,1,2,3,5,4,6,7,8,0}

print(num_set) # check your set values: optional

# count the values in the set with the len() function

print(len(num_set)) # there are ten values in the set, zero through nine

add_num_values = sum(num_set) # add up all values in the set

print(add_num_values) # added all ten values = 45
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is how you can find the mean of a set of numbers with Python.
# But now, I want to figure out how to find the middle number or numbers
# in the nums values. In this case, 4 and 5 are the only two that are in
# the middle of the nums values; hence ten values, zero through nine.
# The good news is, I have long ago found out how to intersect numbers,
# which is simply numbers that are the same, but from different sets
# and values or unionize them into one, larger set of values. Python sets
# also get rid of any duplicate values, such as text strings and integer
# strings. Sets also don't use indexing, whereas tuples and lists do.
# Sets display text strings in random order, whereas integer strings are
# in order and sorted as well.

nums = {0,1,2,3,4,5,6,7,8,9}

mean = len(nums)  # 10 values in nums

add_values = sum(nums)  # nums = 45

answer = add_values/mean  # 45/10 = 4.5

print(answer)  # 4.5
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# All computers, including your calculator follows the rules of BEDMAS, PEMDAS
# or BODMAS. Whatever you call these abbreviations', they still are the very same
# things. So, don't let the names of these abbreviations fool you; they are BEDMAS.
# Period!! Bedmas as I still call it means The Order of Operation. Multiplication and
# division always take dominants over addition and subtraction. Although, computers
# cannot do brackets () of any kind in Python. Python will still follow the order of
# operation regardless. Highlight and copy, then paste this Python code into your
# Python editor and see what happens when you execute/run these Python program
# examples.

# Here are the basic bracket sets you can use on paper, not in Python.

# You have to work inside the very first set of ( ) round brackets first. Next, you have to
# work inside the [ ] square backets. Then lastly, you have to work inside the curly
# braces { }

# Not shown here, you must also do any exponents if you have them in your math
# formulas. They have to be done FIRST, before any brackets get solved. After you
# break everything down. Always work from left to right. Look for any multiplication
# or division first. Then do your addition and subtraction last to get the correct answer.

# { [ ( ) ] }  {Third[Second(first)Second]Third} how this works {n+n[n(n+n)+n/n]-n*n}

bedmas_example1 = 2+3*3
bedmas_example2 = 3*3+2
bedmas_example3 = 2+3/3
bedmas_example4 = 3/3+2
bedmas_example5 = 3-2*3
bedmas_example6 = 3*3-2

print(bedmas_example1)
print(bedmas_example2)
print(bedmas_example3)
print(bedmas_example4)
print(bedmas_example5)
print(bedmas_example6)

# To create exponents in Python, you can do the following examples below:

# You can use a double asterisk **

exponent = 4**3

print(exponent)

# Or use the pow(num,num) function

exponent = pow(4,3)

print(exponent)

# Python has a square root function that finds the square root of a number.
# You have to import the math module for the sqrt() function to work. Invoke
# the integer function int() to stop floating point numbers from showing up.

import math

print(int(math.sqrt(9)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can do a lot with for loops. I practice Python every day and I'm always
# tripping onto things, just by trial and error alone. I wasn't shown this at all.
# This is one of my own happy accidents. I got really bored and did this for
# us all.

names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

for i,x,y,z in names1,names2,names3:
    print('Hello',i+'. How are you? You bought a cute',y,'I see...')
    print('Hello',x+'. How are you? You bought a cute',z,'I see...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence= 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print(sentence[0],i+sentence[1],y,sentence[2])
    print(sentence[0],x+sentence[1],z,sentence[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence = 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print('{} {} {} {}'.format(sentence[0],i+sentence[1],y,sentence[2])) # The old formated example:
    print('{} {} {} {}'.format(sentence[0],x+sentence[1],z,sentence[2]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
names1 = ['Bob','Rob','dog','cat']
names2 = ['John','Tom','bird','fish']
names3 = ['Terry','Mary','turtle','monkey']

sentence = 'Hello','. How are you? You bought a cute','I see...'

for i,x,y,z in names1,names2,names3:
    print(f'{sentence[0]} {i}{sentence[1]} {y} {sentence[2]}') # The new f' formated example:
    print(f'{sentence[0]} {x}{sentence[1]} {z} {sentence[2]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's play with the zip function()

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i)

# or this:

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i[0])

# or this:

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i[1])

# or this:

list1 = ['zip 1','zip 2','zip 3','zip 4']
list2 = ['zip 5','zip 6','zip 7','zip 8']

zip_list = zip(list1,list2)

for i in zip_list:
    print(i[0])
    print(i[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's play with the enumerate function()

list1 = ['enumerate 1','enumerate 2','enumerate 3','enumerate 4']
list2 = ['enumerate 5','enumerate 6','enumerate 7','enumerate 8']

x,y = enumerate(list1),enumerate(list2)

print(tuple(x))
print(list(y))

# or this:

list1 = ['enumerate 1','enumerate 2','enumerate 3','enumerate 4']
list2 = ['enumerate 5','enumerate 6','enumerate 7','enumerate 8']

x,y = enumerate(list1),enumerate(list2)

print(dict(x))
print(set(y))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Walrus Operator Python program example.

# Created by Joseph C. Richardson, GitHub.com

# Use the := Walrus Operator to create the following Python prgram
# examples, using tuples(), lists[] and dictionaries{}.

if my_tuple := (
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5'):pass

for value in my_tuple:print(value)

if my_list := [
    'Value 0','Value 1','Value 2',
    'Value 3','Value 4','Value 5']:pass

for value in my_list:print(value)

if my_dictionary := {
    1:'Value 1',2:'Value 2',3:'Value 3',
    4:'Value 4',5:'Value 5',6:'Value 6'}:pass

for value in my_dictionary:print(
    my_dictionary.get(value+1,f"There are no more values to loop \
through after 'Value {value}'."))

# Look what you can do with Python's print() function.

# Use three single ''' quotes to make string concatenation much easier
# and much more text oriented.

print('''That's 'GREAT' to "TRIPPLE QUOTES" ''')

# Use three double " quotes to make string concatenation much easier
# and much more text oriented.

print("""That's 'GREAT' to "TRIPPLE QUOTES" """)

# Use Python's Error Handlers to not only stop errors from occurring.
# But you can also use Error Handlers to manipulate Python code flow
# of control. As you may notice, I used the walrus := operator to write
# less lines of code. Play around with the values within these program
# examples and call wrong indexes, and wrong strings together to force
# these exception handlers to do their work, which is to stop programs
# from crashing, and they are also used for program manipulation
# purposes to change program flow control.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# The 'pass' prefix is for code place holding if you don't wish to write
# any code blocks underneath expressions that use code blocks, such
# as the Python program above shows in our first example.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Without the use of the walrus := operator.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')

# With the 'pass' prefix placeholder for code blocks.

x = (0,1,2,3,4,5)

if x == x:
    try:
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        pass

# Let's use one 'try:' and two exception handlers, alongside the walrus
# := operator. We will use one 'IndexError:' handler and one 'TypeError:'
# handler to create some programming manipulation within our Python
# program examples below.

if x := (0,1,2,3,4,5):
    try:
        print(x[6],'is in the "x" variable tuple().')
        print(x[4]+'character string')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')

# Python executes/runs its programs from the top downward, as the
# very same way you can see the code order. Each instruction is first
# to execute, is the first to be serviced. In most cases multiple exception
# handlers can only execute one or the other, depending on the code order.

if x := (0,1,2,3,4,5):
    try:
        print(x[4]+'character string text.')
        print(x[6],'is in the "x" variable tuple().')
    except IndexError:
        print('The IndexError handler stops index errors from occurring.')
    except TypeError:
        print('The TypeError handler stops Type errors from occurring.')

# Use the := Walrus Operator to temporarily check for values in tuples,
# lists, dictionaries and sets. That way, you can be a bit lazy and
# not have to write two lines of code only to check for values. Note:
# default tuples won't work with the := walrus operator for indexing.
# Python cannot seem to see the values as either strings, nor integers
# when using the := walrus operator.

print(x := 1,2,3,4,5,6,7,8,9)  # x creates a default tuple of values

print(x[0]) # TypeError: 'int' object is not subscripted

print(x := (1,2,3,4,5,6,7,8,9))  # x creates a tuple of values

print(x[0]) # tuple index[0] is the value '1'

print(x := [1,2,3,4,5,6,7,8,9])  # x creates a list of values

print(x[0]) # list index[0] is the value '1'

print(x := {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9})  # x creates a dictionary of values

print(x.get(1,'Not Found!'))

print(x := {1,2,3,4,5,6,7,8,9})  # x creates a set of values

x = sum([1,2,3,4,5,6,7,8,9])
y = sum([10,11,12,13,14,15,16,17,18,19])

print(f'x = {x} and y = {y}. x+y = {x+y}') # x = 45 and y = 145. x+y = 190

# Here is something else we can do with the Walrus := operator.
# Here are two Python program examples that will show you the
# 'if' statement, using the none walrus := operator, and the use
# of the walrus := operator with the 'if' statement.

x = 3

if x == 3:print(x)

# Notice how the very same Python code above is exactly the
# very same Python code as below. As you can clearly see, the
# walrus := operator reduces the usual two lines of Python code
# down to just one, single line of Python code.

if x := 3:print(x) # the walrus := operator makes x act as if it were named first.

# You don't have to create a variable first, to then place it within an
# 'if' statement using the walrus := operator.

# Welcome to the the split() function. This split() function has a dot '. '
# in front of it that joins the variable, 'poem' to the split() function
# using another variable called, 'text'. What the split() function does
# is turns any text paragraphs into an actual list of words, which you
# can then use their indexes [index] to pick out words within the poem.

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

# For example: the first word in the poem is 'Knowledge', which is
# index[0] with the single quote marks as in no spaces in between them
# or the word Knowledge. Any words thereafter doesn't have quote marks;
# only the title of the poem as in normal poems, sometimes you want
# quote marks in a title or word/words alike.

text = poem.split()

print(text[0]) # index[0] is the word with single quote marks: 'Knowledge'

poem = '''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''

# Here, we can use Python's Walrus Operator := to check our list of words
# within the poem right on the spot and on one, single line of Python code
# at that.

print(text := poem.split())

# Here is the old way, I taught you, as others had taught you. Let's check our
# list of words without the help of the walrus := operator and see how we have
# to use two lines of Python code to create the same thing as we did above
# using the walrus := operator. When you are happy with your list of words,
# you can throw away only one line of Python code, instead throwing away
# two lines of Python code. The walrus := operator makes this a single line
# snap that you can just throw away one line of Python code.

text = poem.split()

print(text)

# Now that I'm happy with my list. I can start picking out words, via their indexes.

print(text[1]) # index[1] is the word: is

# Let's use a for loop to call up all the words to the poem, without showing ugly
# commas ' , ' and index[ ] brackets.

for i in text:print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the ord(), ordinal function to generate ascii code values.

ordinal = (
    '0','1','2','3','4','5','6','7','8','9',

    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',

    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z')

print('lowercase a =',ord('a'),'and uppercase A =',ord('A'))

# invoke the chr(), character function to generate ascii code characters.

character = (
    '48','49','50','51','52','53','54','55','56','57',

    '97','98','99','100','101','102','103','104','105','106',
    '107','108','109','110','111','112','113','114','115','116',
    '117','118','119','120','121','122',

    '65','66','67','68','69','70','71','72','73','74',
    '75','76','77','78','79','80','81','82','83','84',
    '85','86','87','88','89','90')

print(ord('a'),'= lowercase',chr(97),'and',ord('A'),'= uppercase',chr(65))

# Invoke the new f' string format for easier string concatenation.

print(f'{ord("a")} = lowercase {chr(97)} and {ord("A")} = uppercase {chr(65)}' )
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Make the decimal base 10 number system calculate, then convert the result
# in binary base 2, hexadecimal base 16 and octal base 8 number systems.
# Note: you must invoke the f' string format to be able to do the following
# Python programming examples.

num_convert = 5+250

print(f'Binary number: {num_convert:b} = decimal number: {num_convert}...')

# Binary number: 11111111 = decimal number: 255...

print(f'Hexadecimal number: {num_convert:x} = decimal number: {num_convert}...')

# Hexadecimal number: ff = decimal number: 255...

print(f'Octal number: {num_convert:o} = decimal number: {num_convert}...')

# Octal number: 377 = decimal number: 255...

# You can also use these prefixes for generating binary base 2 numbers,
# hexadecimal base 16 numbers and octal base 8 numbers.

print(bin(255))  # 0b11111111

print(hex(255))  # 0xff

print(oct(255))  # 0o377

# See the illustration examples below:

num_convert = 5+250

print('Binary number:',bin(num_convert),'= decimal number:',str(num_convert)+'...')

# Binary number: 0b11111111 = decimal number: 255...

print('Hexadecimal number:',hex(num_convert),'= decimal number:',str(num_convert)+'...')

# Hexadecimal number: 0xff = decimal number: 255...

print('Octal number:',oct(num_convert),'= decimal number:',str(num_convert)+'...')

# Octal number: 0o377 = decimal number: 255...

# Invoke the f' string format to make string concatenation much easier if you like.

print(f'Binary number: {bin(num_convert)} = decimal number: {num_convert}...')

print(f'Hexadecimal number: {hex(num_convert)} = decimal number: {num_convert}...')

print(f'Octal number: {oct(num_convert)} = decimal number: {num_convert}...')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a working binary to hexadecimal to octal to decimal counter with
# a for loop that will count all the way up to 255, which is exactly one 8b byte:
# 11111111 = decimal: 255. We have to import the time module to use the
# time.sleep() function within our for loop.

import time

for i in range(256):
    print(f'Binary number: {i:b} = decimal number: {i}...')

    print(f'Hexadecimal number: {i:x} = decimal number: {i}...')

    print(f'Octal number: {i:o} = decimal number: {i}...')

    time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's recreate the Python program example above, but we will make it more
# articulated with how many actual bits in one binary 8 bit byte there are as
# the binary digits count on 0 through to 255, which is exactly the equivalent
# of an 8 bit binary byte. To make this possible, we will need to invoke the len(),
# length function to count out how many bits to whatever binary number
# values there are.

import time

for i in range(256):
    print(
        'Binary number bits in one 8b byte =',\
        len(f'{i:b}'),f'bits = Binary number: {i:b} = decimal number: {i}...')

    print(f'Hexadecimal number: {i:x} = decimal number: {i}...')

    print(f'Octal number: {i:o} = decimal number: {i}...')

    time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now reconstruct the very same Python program above, but we
# will drastically reduce Python code down to just one, single print()
# function.

import time

for i in range(256):
     print(
'Binary number bits in one 8b byte =',\
len(f'{i:b}'),f'bits = Binary number: {i:b} = decimal number: {i}...\n\
Hexadecimal number: {i:x} = decimal number: {i}...\n\
Octal number: {i:o} = decimal number: {i}...')

     time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a simple define function along with the print() function.

def define_function_example_one():
    print('This is a basic define function() example.')

define_function_example_one()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function with one parameter variable along with the print() function.

def define_function_example_two(argument):
    print('This is a basic define function() with an argument example.')

define_function_example_two('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function with two parameter variables along with
# the print() function.

def define_function_example_three(argument1,argument2):
    print('This is a basic define function() with two arguments example.')

define_function_example_three('argument placeholder value','argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When you are not sure of how many parameter variables to use within a define
# function, you can invoke the *args prefix to satisfy any number of argument
# placeholder values without the worry of how many are needed to satisfy the
# parameter variables.

def define_function_Class_example_four(*args):
    print('This is a basic define function() with an *args example.')

define_function_Class_example_four('argument placeholder value','argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that returns a value, via invoking one parameter
# variable, along with one argument placeholder value.

def define_function_Class_example_five(argument):
    return 'I am the actual returned value.'

print(define_function_Class_example_five(
    'This is a return define function() with an argument placeholder value.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that returns two values, via invoking
# two parameter variables, along with two argument placeholder values.

def define_function_example_six(argument1,argument2):
    return 'I am the actual returned value one.','I am the actual returned value two.'

print(define_function_example_six(
    'This is a return define function() with an argument example.',
    'This is a return define function() with an argument example.')[1])

# or this:

def define_function_example_six(argument1,argument2):
    return (
        'I am the actual returned value one.',
        'I am the actual returned value two.')

print(define_function_example_six(
    'This is a return define function() with an argument example.',
    'This is a return define function() with an argument example.')[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When you are not sure of how many parameter variables to use within
# a return define function, you can invoke the *args prefix to satisfy any
# number of argument placeholder values without the worry of how many
# are needed to satisfy the parameter variables.

def define_function_example_seven(*args):
    return 'I am the actual returned value one.','I am the actual returned value two.'

print(define_function_example_seven('This is a return define function() with an argument example.')[1])

# or this:

def define_function_example_seven(*args):
    return (
        'I am the actual returned value one.',
        'I am the actual returned value two.')

print(define_function_example_seven(
    'This is a return define function() with an argument example.')[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what **kwargs are all about. The word 'kwargs' simply means the words
# 'keyword arguments' for short. Two asterisks ** are used for **kwargs. Use **kwargs
# when you don't know how many keyword argument variables you want within your
# define function parameters. Note: you do not need to call the word '**kwargs' as
# kwargs. However, you will need to invoke two asterisks ** to make **kwargs work.
# Programmers know the word as **kwargs by standard definition, but you can use
# your own words.

def keyword_arguments(**kwargs): # one keyword argument variable
    print('I am the actual value.')

keyword_arguments(
    keyword1='keyword argument placeholder value1',
    keyword2='keyword argument placeholder value2') # two keyword argument values

# This example is without any **kwargs at all; we have to
# satisfy the exact number of keyword arguments to the
# exact number of keyword argument placeholder values.

def keyword_arguments(keyword_arg1,keyword_arg2): # two keyword argument variables
    print('I am the actual value.')

keyword_arguments(
    keyword_arg1='keyword argument placeholder value1',
    keyword_arg2='keyword argument placeholder value2') # two keyword argument values

# As shown in the define function() example above, how we needed the exact number
# of keyword argument values to the exact number of keyword argument variables.
# However, with **kwargs you no longer have to worry about how many keyword
# argument values you will need to satisfy the number of keyword argument variables
# within the define function parameters.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# define functions can also return keyword arguments. In this first example, the exact
# number of keyword arguments are required to satisfy the exact number of keyword
# argument placeholder values within the print() function.

def keyword_arguments(kwarg1,kwarg2):
    return 'I am the actual returned value one.','I am the actual returned value two.',

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))

# define functions can also return keyword arguments. In this second example, the exact
# number of keyword arguments are not required to satisfy the exact number of keyword
# argument placeholder values within the print() function.

def keyword_arguments(**kwargs):
    return 'I am the actual returned value.'

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# define functions can also return keyword arguments. In this first example, the exact
# number of keyword arguments are required to satisfy the exact number of keyword
# argument placeholder values within the print() function.

def keyword_arguments(num1,num2):
    return num1*num2

print(keyword_arguments(num1=2,num2=4))

# define functions can also return keyword arguments. In this second example, the
# exact number of keyword arguments are not required to satisfy the exact number
# of keyword argument placeholder values within the print() function.

def keyword_arguments(**kwargs):
    return 2*4

print(keyword_arguments(num1='placeholder value 1',num2='placeholder value 2'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do a quick recap about *args and **kwargs syntex only, so we can fully
# understand in a simpler way of what *args and **kwargs are all about.

def arguments(*args): # one argument variable
    print('I am the actual value.')

arguments(
    'argument placeholder value1',
    'argument placeholder value2')  # two argument values

def keyword_arguments(**kwargs): # one keyword argument variable
    print('I am the actual value.')

keyword_arguments(
    kwargs1='keyword argument placeholder value1',
    kwargs2='keyword argument placeholder value1')  # two keyword argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some define functions that act like subroutines.

# Since there are no line numbers in Python, also means that we cannot create
# any such 'go to', or 'go sub' commands at all with Python. So how can we
# create subroutines with Python?. How can we create subroutines without
# making them jump to line numbers, like we did in the old days? Well the
# answer is quite simple. Let's use define functions() with a while loop to
# create our subroutine examples, using define functions() only.

def subroutine_one():
    print('You picked subroutine one:')

def subroutine_two():
    print('You picked subroutine two:')

def subroutine_three():
    print('You picked subroutine three:')

while True:
    message=input('Please type 1, 2 or 3 to select the subroutine you wish to \
display or type (q) to quit: ').lower().strip()  # strip() clears whitespace)

    if message=='q':
        break
    while True:
        if message=='1':
            subroutine_one()
            break
        elif message=='2':
            subroutine_two()
            break
        elif message=='3':
            subroutine_three()
            break
        else:
            print('Sorry! No subroutine for that.')
            break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Global Variables in Python

# What are 'global variables'? Global variables are used within define functions()
# when you want to call a variable outside the actual define function(), you need
# the prefix 'global' to be able to call a variable outside the actual define function()
# itself. For example here is what calling a variable, using the prefix 'global' does.

def global_variable():
    global a
    a = 'global variables work outside their define functions()'

global_variable()

print(a)

# If you try to call a variable outside a define function() with no 'global' prefix
# attached to it, you will get an error such as this:

def non_global_variable():
    b = 'non global variables won\'t work outside their define functions()'

non_global_variable()

print(b)

# Traceback (most recent call last):
#   File "C:\Users\mogie54321\Downloads\Define Functions and Class Objects.py", line 257, in <module>
#    print(b)
# NameError: name 'b' is not defined

# You can, however do this if you don't want to invoke the 'global' prefix. So
# instead, we can do this:

b = 'outside variables work outside their define functions()'

def non_global_variable():
    print(b)

non_global_variable()

# Simply create a variable outside the define function and then call it in from outside
# it. Let's do more global variables to get the hang of things with a group of them.

def global_variables():
    global a
    global b
    global c

    a = 'global variable (a) works outside its define function()'
    b = 'global variable (b) works outside its define function()'
    c = 'global variable (c) works outside its define function()'

global_variables()

print(a)

# Here is one thing you should avoid doing. If you call an outside variable with the
# same name as this example below shows, you won't get the desired output you
# want. If you want outside variables outside of global variables, you must give them
# different names so they can know who is who.

a = 'oops! This outside variable (a) was overwritten by the global variable (a).'

def global_variables():
    global a
    global b
    global c

    a = 'global variable (a) works outside its define functions()'
    b = 'global variable (b) works outside its define functions()'
    c = 'global variable (c) works outside its define functions()'

global_variables()

print(a)

# Now that we used a different name for the outside variable, the global variables and the
# outside variable will know who is who, when being called upon. Note: you can also use
# an uppercase 'A' for the outside variable; computers are case sensitive: 'a' and 'A'
# are not the same to a computer. Therefore, the computer treats the variables as totally
# different names. So please keep this in mind at all times.

abc = 'Now I know which one of us variables are being called.'

def global_variables():
    global a
    global b
    global c

    a = 'global variable (a) works outside its define functions()'
    b = 'global variable (b) works outside its define functions()'
    c = 'global variable (c) works outside its define functions()'

global_variables()

print(abc)
print(a)

# The computer thinks this is a totally different variable name altogether.

A = 'I still know which one of us variables are being called.'

def global_variables():
    global a
    global b
    global c

    a = 'global variable (a) works outside its define functions()'
    b = 'global variable (b) works outside its define functions()'
    c = 'global variable (c) works outside its define functions()'

global_variables()

print(A)
print(a)

# Let's pack global variables with just one 'global' prefix to use
# them outside the define function().

def global_variables():
    global a,b,c

    a = 'pack global variable (a) works outside its define functions()'
    b = 'pack global variable (b) works outside its define functions()'
    c = 'pack global variable (c) works outside its define functions()'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's go way, way back to school. I don't mean the ABC, 123 kind either. Instead of
# going to school and going to class. Why not make school come to us, and we build
# the classrooms ourselves? In this case, we have to create class objects, much like
# the way a real classroom works. Each class in this first example will have its very
# own set of attribute properties. Let's learn to create classes using the Mom and
# Dad concept approach. Let's create a Mom class object and a Dad class object.
# Each feature of their objects are called attributes. And each attribute has its own
# property attached to it.

# Let's give Mom and Dad a name, like Jane and John.

class Mom:
    def __init__(self,name):

        self.name = name  # 1 attribute property only


class Dad:
    def __init__(self,name):

        self.name = name  # 1 attribute property only

print(Mom('Jane').name)

print(Dad('John').name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's give Mom and Dad their first names, along with their last names.

class Mom:
    def __init__(self,first_name,last_name):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2


class Dad:
    def __init__(self,first_name,last_name):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2

print(Mom('Jane','Smith').first_name)

print(Dad('John','Smith').first_name)

print(Mom('Jane','Smith').last_name)

print(Dad('John','Smith').last_name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create more class object attribute properties for Mom and Dad, such as
# their ages, their hair colour and their eye colour.

class Mom:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

print(Mom('Jane','Smith',25,'brown hair','blue eyes').first_name)

print(Mom('Jane','Smith',25,'brown hair','blue eyes').last_name)

print(Mom('Jane','Smith',25,'brown hair','blue eyes').age)

print(Mom('Jane','Smith',25,'brown hair','blue eyes').hair_colour)

print(Mom('Jane','Smith',25,'brown hair','blue eyes').eye_colour)


class Dad:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

print(Dad('John','Smith',30,'black hair','brown eyes').first_name)

print(Dad('John','Smith',30,'black hair','brown eyes').last_name)

print(Dad('John','Smith',30,'black hair','brown eyes').age)

print(Dad('John','Smith',30,'black hair','brown eyes').hair_colour)

print(Dad('John','Smith',30,'black hair','brown eyes').eye_colour)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's give Mom and Dad a child class act that will inherit both parent's attribute
# properties.

class Mom:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

class Dad:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

class Child(Dad,Mom):pass  # Child class Inherits Mom and Dad class attribute properties only

print(Mom('Jane','Smith',25,'brown hair','blue eyes').first_name)

print(Dad('John','Smith',30,'black hair','brown eyes').first_name)

print(Child('Jimmy','Smith',12,'black hair','blue eyes').first_name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# As with all children, they too have their very own set of features, attribute properties.
# So, let's make our child class act have its very own set of features, attribute properties
# as well. To do this, we need to invoke the 'super()' function, along with its '__init__' , initialize
# constructor. The super() function stops program code redundancy on the programmer's
# part; without the super() function, the Mom and Dad class attribute properties would
# have to be rewritten again into the child's new, added attribute property of its own class
# act.

class Mom:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

class Dad:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

class Child(Dad,Mom):
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour,looks,smarts):
        super().__init__(first_name,last_name,age,hair_colour,eye_colour)

        self.looks = looks
        self.smarts = smarts  # New, added attribute properties, without rewriting the Mom and Dad class attribute properties.

print(Mom('Jane','Smith',25,'brown hair','blue eyes').first_name)

print(Dad('John','Smith',30,'black hair','brown eyes').first_name)

print(Child('Jimmy','Smith',12,'black hair','blue eyes','I look GREAT!',"Wow!! I'm so smart...").first_name)

print(Child('Jimmy','Smith',12,'black hair','blue eyes','I look GREAT!',"Wow!! I'm so smart...").looks)  # new attribute property 6

print(Child('Jimmy','Smith',12,'black hair','blue eyes','I look GREAT!',"Wow!! I'm so smart...").smarts)  # new attribute property 7

# The super() function is a great way to add new attribute properties to sub class acts,
# like our child class act, without redundant program code, via the programmer's part.
# Note: you do not need to invoke the super() function if you only want to use main
# class attribute properties in sub class acts. If you wish to add new attribute properties
# into sub class acts. You will need to invoke the super() function, along eith
# the '__init__' constructor.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a Mom and Dad class act with two child class acts. Let's also make the
# two children be a boy and a girl. The boy will inherit Mom and Dad's attribute properties
# only, while the girl will inherit Mom and Dad's attribute properties plus her own set of
# unique attribute properties of her own.

class Mom:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

class Dad:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5

class Child1(Dad,Mom):pass  # Child1 class Inherits Mom and Dad class attribute properties only

class Child2(Child1,Dad,Mom):
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour,looks,smarts):
        super().__init__(first_name,last_name,age,hair_colour,eye_colour)

        self.looks = looks
        self.smarts = smarts  # New, added attribute properties, without rewriting the Mom and Dad class attribute properties.

print(Mom('Jane','Smith',25,'brown hair','blue eyes').first_name)

print(Dad('John','Smith',30,'black hair','brown eyes').first_name)

print(Child1('Jimmy','Smith',12,'black hair','blue eyes').first_name)

print(Child2('Joan','Smith',10,'brown hair','brown eyes','I look GREAT!',"Wow!! I'm so smart...").first_name)

print(Child2('Joan','Smith',10,'brown hair','brown eyes','I look GREAT!',"Wow!! I'm so smart...").looks)  # new attribute property 6

print(Child2('Joan','Smith',10,'brown hair','brown eyes','I look GREAT!',"Wow!! I'm so smart...").smarts)  # new attribute property 7
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create this very same class example as above, but this time let's give the Mom
# and Dad classes atribute properties of their own as well.

class Mom:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour,music):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5
        self.music = music                      # attribute property 6

class Dad:
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour,cars):

        self.first_name = first_name  # attribute property 1
        self.last_name = last_name   # attribute property 2
        self.age = age                           # attribute property 3
        self.hair_colour = hair_colour  # attribute property 4
        self.eye_colour = eye_colour   # attribute property 5
        self.cars = cars                            # attribute property 6

class Child1(Dad,Mom):pass  # Child1 class Inherits Mom and Dad class attribute properties only

class Child2(Child1,Dad,Mom):
    def __init__(self,first_name,last_name,age,hair_colour,eye_colour,looks,smarts,cars):  # cars attribute property
        super().__init__(first_name,last_name,age,hair_colour,eye_colour,cars)

        self.looks = looks
        self.smarts = smarts  # New, added attribute properties, without rewriting the Mom and Dad class attribute properties.

print(Mom('Jane','Smith',25,'brown hair','blue eyes','plays guitar').music)

print(Dad('John','Smith',30,'black hair','brown eyes','works with cars').cars)

print(Child1('Jimmy','Smith',12,'black hair','blue eyes','I love cars too').cars)

print(Child2('Joan','Smith',10,'brown hair','brown eyes','I look GREAT!',"Wow!! I'm so smart...",'I love painting cars').smarts)

# The child1 class and the child2 class inherit the cars attribute from the dad class only.
# The mom class has its own, unique attribute property, called 'music' that cannot be
# called through any other classes or sub class acts.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's grow up and get away from the Mom and Dad concept approach to creating
# classes and sub classes, as well as super sub classes, without Mom and Dad hanging
# around all the time. Let's relearn what we already learned about classes so far. Try
# each of these class examples below. From here onward, there are no more comments
# about classes or sub classes. The only thing different are the use of variables inside
# the print() functions. See the first, second and third class example in this class program
# example below:

class Learn_to_make_class_acts:

    def __init__(self,attribute):
        self.class_act_attribute = attribute

print(Learn_to_make_class_acts('one attribute property value').class_act_attribute)

# or this:

class Learn_to_make_class_acts:

    def __init__(self,attribute):
        self.class_act_attribute = attribute

a = Learn_to_make_class_acts('one attribute property value').class_act_attribute

print(a)

# or this:

class Learn_to_make_class_acts:

    def __init__(self,attribute):
        self.class_act_attribute = attribute

a = Learn_to_make_class_acts('one attribute property value')

print(a.class_act_attribute)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Learn_to_make_class_acts:

    def __init__(self,attribute1,attribute2):
        self.class_act_attribute1 = attribute1
        self.class_act_attribute2 = attribute2

a = Learn_to_make_class_acts(
    'attribute property value 1','attribute property value 2')

print(a.class_act_attribute1)

print(a.class_act_attribute2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Learn_to_make_class_acts:

    def __init__(self,attribute1,attribute2,attribute3):
        self.class_act_attribute1 = attribute1
        self.class_act_attribute2 = attribute2
        self.class_act_attribute3 = attribute3

a = Learn_to_make_class_acts(
    'attribute property value 1',
    'attribute property value 2',
    'attribute property value 3')

print(a.class_act_attribute1)

print(a.class_act_attribute2)

print(a.class_act_attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Learn_to_make_main_class_acts:

    def __init__(self,attribute1,attribute2,attribute3):
        self.main_class_act_attribute1 = attribute1
        self.main_class_act_attribute2 = attribute2
        self.main_class_act_attribute3 = attribute3

class Learn_to_make_sub_class_acts(Learn_to_make_main_class_acts):pass  # inherit main class attribute properties only

a = Learn_to_make_main_class_acts(
    'I am the attribute property value 1 from the main class act.',
    'I am the attribute property value 2 from the main class act.',
    'I am the attribute property value 3 from the main class act.')

b = Learn_to_make_sub_class_acts(
    'I am the inherited attribute property value 1 from the main class act.',
    'I am the inherited attribute property value 2 from the main class act.',
    'I am the inherited attribute property value 3 from the main class act.')

print(a.main_class_act_attribute2)

print(b.main_class_act_attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Learn_to_make_main_class_acts:

    def __init__(self,attribute1,attribute2,attribute3):
        self.main_class_act_attribute1 = attribute1
        self.main_class_act_attribute2 = attribute2
        self.main_class_act_attribute3 = attribute3

class Learn_to_make_super_sub_class_acts(Learn_to_make_main_class_acts):  # inherit main class attribute properties and
    def __init__(self,attribute1,attribute2,attribute3,attribute4):  # new super sub class attribute property: attribute4
        super().__init__(attribute1,attribute2,attribute3)

        self.main_class_act_attribute4 = attribute4

a = Learn_to_make_main_class_acts(
    'I am the attribute property value 1 from the main class act.',
    'I am the attribute property value 2 from the main class act.',
    'I am the attribute property value 3 from the main class act.')

b = Learn_to_make_super_sub_class_acts(
    'I am the inherited attribute property value 1 from the main class act.',
    'I am the inherited attribute property value 2 from the main class act.',
    'I am the inherited attribute property value 3 from the main class act.',
    'I am my own attribute property value 4 from the super sub class act.')

print(a.main_class_act_attribute3)

print(b.main_class_act_attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Learn_to_make_main_class_acts:

    def __init__(self,attribute1,attribute2,attribute3):
        self.main_class_act_attribute1 = attribute1
        self.main_class_act_attribute2 = attribute2
        self.main_class_act_attribute3 = attribute3

class Learn_to_make_sub_class_acts(Learn_to_make_main_class_acts):pass  # inherit main class attribute properties only

class Learn_to_make_super_sub_class_acts(
    Learn_to_make_sub_class_acts,Learn_to_make_main_class_acts):  # inherit main class attribute properties and
    def __init__(self,attribute1,attribute2,attribute3,attribute4):  # new super sub class attribute property: attribute4
        super().__init__(attribute1,attribute2,attribute3)

        self.main_class_act_attribute4 = attribute4

a = Learn_to_make_main_class_acts(
    'I am the attribute property value 1 from the main class act.',
    'I am the attribute property value 2 from the main class act.',
    'I am the attribute property value 3 from the main class act.')

b = Learn_to_make_sub_class_acts(
    'I am the inherited attribute property value 1 from the main class act.',
    'I am the inherited attribute property value 2 from the main class act.',
    'I am the inherited attribute property value 3 from the main class act.')

c = Learn_to_make_super_sub_class_acts(
    'I am the inherited attribute property value 1 from the main class act.',
    'I am the inherited attribute property value 2 from the main class act.',
    'I am the inherited attribute property value 3 from the main class act.',
    'I am my own attribute property value 4 from the super sub class act.')

print(a.main_class_act_attribute3)

print(b.main_class_act_attribute3)

print(c.main_class_act_attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Learn_to_make_main_class_acts:

    def __init__(self,attribute1,attribute2,attribute3):
        self.main_class_act_attribute1 = attribute1
        self.main_class_act_attribute2 = attribute2
        self.main_class_act_attribute3 = attribute3

class Learn_to_make_sub_class_acts(Learn_to_make_main_class_acts):pass  # inherit main class attribute properties only

class Learn_to_make_super_sub1_class_acts(
    Learn_to_make_sub_class_acts,
    Learn_to_make_main_class_acts):  # inherit main class attribute properties and
    def __init__(self,attribute1,attribute2,attribute3,attribute4):  # new super sub1 class attribute property: attribute4
        super().__init__(attribute1,attribute2,attribute3)

        self.main_class_act_attribute4 = attribute4

class Learn_to_make_super_sub2_class_acts(
    Learn_to_make_super_sub1_class_acts,
    Learn_to_make_sub_class_acts,
    Learn_to_make_main_class_acts):  # inherit main class attribute properties and
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):  # new super sub2 class attribute property: attribute5
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.main_class_act_attribute5= attribute5

a = Learn_to_make_main_class_acts(
    'I am the attribute property value 1 from the main class act.',
    'I am the attribute property value 2 from the main class act.',
    'I am the attribute property value 3 from the main class act.')

b = Learn_to_make_sub_class_acts(
    'I am the inherited attribute property value 1 from the main class act.',
    'I am the inherited attribute property value 2 from the main class act.',
    'I am the inherited attribute property value 3 from the main class act.')

c = Learn_to_make_super_sub1_class_acts(
    'I am the inherited attribute property value 1 from the main class act.',
    'I am the inherited attribute property value 2 from the main class act.',
    'I am the inherited attribute property value 3 from the main class act.',
    'I am my own attribute property value 4 from the super sub1 class act.')

d = Learn_to_make_super_sub2_class_acts(
    'I am the inherited attribute property value 1 from the main class act.',
    'I am the inherited attribute property value 2 from the main class act.',
    'I am the inherited attribute property value 3 from the main class act.',
    'I am the inherited attribute property value 4 from the super sub1 class act.',
    'I am my own attribute property value 5 from the super sub2 class act.')

print(a.main_class_act_attribute3)

print(b.main_class_act_attribute3)

print(c.main_class_act_attribute4)

print(d.main_class_act_attribute5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# If you feel up to the challenge, you can create my ultimate Monster Class
# Python program example. Please note: There are things in this Monster
# Class Python program example not shown in any of the examples above.
# Are you ready to Head Bang with me? Let's go!!

main_class = (
    'This is an instance of a main class object with three attribute properties value 1',
    'This is an instance of a main class object with three attribute properties value 2',
    'This is an instance of a main class object with three attribute properties value 3')

sub_class1 = (
    'This is an instance of a sub class1 object with three attribute properties value 1',
    'This is an instance of a sub class1 object with three attribute properties value 2',
    'This is an instance of a sub class1 object with three attribute properties value 3')

sub_class2 = (
    'This is an instance of a sub class2 object with three attribute properties value 1',
    'This is an instance of a sub class2 object with three attribute properties value 2',
    'This is an instance of a sub class2 object with three attribute properties value 3')

super_sub_class1 = (
     'This is an instance of a super sub class1 object with four attribute properties value 1',
     'This is an instance of a super sub class1 object with four attribute properties value 2',
     'This is an instance of a super sub class1 object with four attribute properties value 3',
     'This is an instance of a super sub class1 object with four attribute properties value 4')

super_sub_class2 = (
     'This is an instance of a super sub class2 object with five attribute properties value 1',
     'This is an instance of a super sub class2 object with five attribute properties value 2',
     'This is an instance of a super sub class2 object with five attribute properties value 3',
     'This is an instance of a super sub class2 object with five attribute properties value 4',
     'This is an instance of a super sub class2 object with five attribute properties value 5')

super_sub_class3 = (
     'This is an instance of a super sub class3 object with six attribute properties value 1',
     'This is an instance of a super sub class3 object with six attribute properties value 2',
     'This is an instance of a super sub class3 object with six attribute properties value 3',
     'This is an instance of a super sub class3 object with six attribute properties value 4',
     'This is an instance of a super sub class3 object with six attribute properties value 5',
     'This is an instance of a super sub class3 object with six attribute properties value 6')

super_sub_class4 = (
     'This is an instance of a super sub class4 object with seven attribute properties value 1',
     'This is an instance of a super sub class4 object with seven attribute properties value 2',
     'This is an instance of a super sub class4 object with seven attribute properties value 3',
     'This is an instance of a super sub class4 object with seven attribute properties value 4',
     'This is an instance of a super sub class4 object with seven attribute properties value 5',
     'This is an instance of a super sub class4 object with seven attribute properties value 6',
     'This is an instance of a super sub class4 object with seven attribute properties value 7')

super_sub_class5 = (
     'This is an instance of a super sub class5 object with eight attribute properties value 1',
     'This is an instance of a super sub class5 object with eight attribute properties value 2',
     'This is an instance of a super sub class5 object with eight attribute properties value 3',
     'This is an instance of a super sub class5 object with eight attribute properties value 4',
     'This is an instance of a super sub class5 object with eight attribute properties value 5',
     'This is an instance of a super sub class5 object with eight attribute properties value 6',
     'This is an instance of a super sub class5 object with eight attribute properties value 7',
     'This is an instance of a super sub class5 object with eight attribute properties value 8')

super_sub_class6 = (
     'This is an instance of a super sub class6 object with nine attribute properties value 1',
     'This is an instance of a super sub class6 object with nine attribute properties value 2',
     'This is an instance of a super sub class6 object with nine attribute properties value 3',
     'This is an instance of a super sub class6 object with nine attribute properties value 4',
     'This is an instance of a super sub class6 object with nine attribute properties value 5',
     'This is an instance of a super sub class6 object with nine attribute properties value 6',
     'This is an instance of a super sub class6 object with nine attribute properties value 7',
     'This is an instance of a super sub class6 object with nine attribute properties value 8',
     'This is an instance of a super sub class6 object with nine attribute properties value 9')

super_sub_class7 = (
     'This is an instance of a super sub class7 object with ten attribute properties value 1',
     'This is an instance of a super sub class7 object with ten attribute properties value 2',
     'This is an instance of a super sub class7 object with ten attribute properties value 3',
     'This is an instance of a super sub class7 object with ten attribute properties value 4',
     'This is an instance of a super sub class7 object with ten attribute properties value 5',
     'This is an instance of a super sub class7 object with ten attribute properties value 6',
     'This is an instance of a super sub class7 object with ten attribute properties value 7',
     'This is an instance of a super sub class7 object with ten attribute properties value 8',
     'This is an instance of a super sub class7 object with ten attribute properties value 9',
     'This is an instance of a super sub class7 object with ten attribute properties value 10')

return_values = (
    '"The Main Class Act"',
    'Sub Class Act One.',
    'Sub Class Act Two',
    'Super Sub Class Act One',
    'Super Sub Class Act Two',
    'Super Sub Class Act Three',
    'Super Sub Class Act Four',
    'Super Sub Class Act Five',
    'Super Sub Class Act Six',
    'Super Sub Class Act Seven')

class Main_class_attribute_properties:

    def return_function():
        return return_values

    def __init__(self,attribute1,attribute2,attribute3):

        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

class Sub_class1_same_attribute_properties(  # inhert main class attribute properties only
    Main_class_attribute_properties):pass

class Sub_class2_same_attribute_properties(  # inhert main class attribute properties only
    Main_class_attribute_properties):pass

class Super_sub_class1_new_attribute_properties(
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1, attribute2,attribute3)

        self.attribute4 = attribute4

class Super_sub_class2_new_attribute_properties(
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5):

        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.attribute5 = attribute5

class Super_sub_class3_new_attribute_properties(
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5)

        self.attribute6 = attribute6

class Super_sub_class4_new_attribute_properties(
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6)

        self.attribute7 = attribute7

class Super_sub_class5_new_attribute_properties(
    Super_sub_class4_new_attribute_properties,
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7)

        self.attribute8 = attribute8

class Super_sub_class6_new_attribute_properties(
    Super_sub_class5_new_attribute_properties,
    Super_sub_class4_new_attribute_properties,
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8,

        attribute9):
        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7,attribute8)

        self.attribute9 = attribute9

class Super_sub_class7_new_attribute_properties(
    Super_sub_class6_new_attribute_properties,
    Super_sub_class5_new_attribute_properties,
    Super_sub_class4_new_attribute_properties,
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8,
        attribute9,attribute10):

        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7,attribute8,
            attribute9)

        self.attribute10 = attribute10

a = Main_class_attribute_properties(main_class[0],main_class[1],main_class[2])

b = Sub_class1_same_attribute_properties(sub_class1[0],sub_class1[1],sub_class1[2])

c = Sub_class2_same_attribute_properties(sub_class2[0],sub_class2[1],sub_class2[2])

d = Super_sub_class1_new_attribute_properties(
    super_sub_class1[0],super_sub_class1[1],
    super_sub_class1[2],super_sub_class1[3])

e = Super_sub_class2_new_attribute_properties(
    super_sub_class2[0],super_sub_class2[1],
    super_sub_class2[2],super_sub_class2[3],
    super_sub_class2[4])

f = Super_sub_class3_new_attribute_properties(
    super_sub_class3[0],super_sub_class3[1],
    super_sub_class3[2],super_sub_class3[3],
    super_sub_class3[4],super_sub_class3[5])

g = Super_sub_class4_new_attribute_properties(
    super_sub_class4[0],super_sub_class4[1],
    super_sub_class4[2],super_sub_class4[3],
    super_sub_class4[4],super_sub_class4[5],
    super_sub_class4[6])

h = Super_sub_class5_new_attribute_properties(
    super_sub_class5[0],super_sub_class5[1],
    super_sub_class5[2],super_sub_class5[3],
    super_sub_class5[4],super_sub_class5[5],
    super_sub_class5[6],super_sub_class5[7])

i = Super_sub_class6_new_attribute_properties(
    super_sub_class6[0],super_sub_class6[1],
    super_sub_class6[2],super_sub_class6[3],
    super_sub_class6[4],super_sub_class6[5],
    super_sub_class6[6],super_sub_class6[7],
    super_sub_class6[8])

j = Super_sub_class7_new_attribute_properties(
    super_sub_class7[0],super_sub_class7[1],
    super_sub_class7[2],super_sub_class7[3],
    super_sub_class7[4],super_sub_class7[5],
    super_sub_class7[6],super_sub_class7[7],
    super_sub_class7[8],super_sub_class7[9])

class_attribute_tuple = (

a.attribute1,a.attribute2,a.attribute3,

b.attribute1,b.attribute2,b.attribute3,

c.attribute1,c.attribute2,c.attribute3,

d.attribute1,d.attribute2,d.attribute3,
d.attribute4,

e.attribute1,e.attribute2,e.attribute3,
e.attribute4,e.attribute5,

f.attribute1,f.attribute2,f.attribute3,
f.attribute4,f.attribute5,f.attribute6,

g.attribute1,g.attribute2,g.attribute3,
g.attribute4,g.attribute5,g.attribute6,
g.attribute7,

h.attribute1,h.attribute2,h.attribute3,
h.attribute4,h.attribute5,h.attribute6,
h.attribute7,h.attribute8,

i.attribute1,i.attribute2,i.attribute3,
i.attribute4,i.attribute5,i.attribute6,
i.attribute7,i.attribute8,i.attribute9,

j.attribute1,j.attribute2,j.attribute3,
j.attribute4,j.attribute5,j.attribute6,
j.attribute7,j.attribute8,j.attribute9,
j.attribute10)

return_value = (

    Main_class_attribute_properties.return_function(),

    Sub_class1_same_attribute_properties.return_function(),
    Sub_class2_same_attribute_properties.return_function(),

    Super_sub_class1_new_attribute_properties.return_function(),
    Super_sub_class2_new_attribute_properties.return_function(),
    Super_sub_class3_new_attribute_properties.return_function(),
    Super_sub_class4_new_attribute_properties.return_function(),
    Super_sub_class5_new_attribute_properties.return_function(),
    Super_sub_class6_new_attribute_properties.return_function(),
    Super_sub_class7_new_attribute_properties.return_function())

print(f'\n{return_value[0][0]}\n\n{a.attribute1}')

print(f'\n{return_value[0][1]}\n\n{b.attribute1}')

print(f'\n{return_value[0][2]}\n\n{c.attribute1}')

print(f'\n{return_value[0][3]}\n\n{d.attribute1}')

print(f'\n{return_value[0][4]}\n\n{e.attribute1}')

print(f'\n{return_value[0][5]}\n\n{f.attribute1}')

print(f'\n{return_value[0][6]}\n\n{g.attribute1}')

print(f'\n{return_value[0][7]}\n\n{h.attribute1}')

print(f'\n{return_value[0][8]}\n\n{i.attribute1}')

print(f'\n{return_value[0][9]}\n\n{j.attribute1}')

# That was easy... 😁
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
poem = ('''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'

                                                                                      Joseph C. Richardson''')
print(poem)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

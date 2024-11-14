# Let's have some extreme fun with for-loops and while-loops

# Created by Joseph C. Richardson, GitHub.com

# Create a right triangle shape with a for-loop, using a
# start value of 1.

for i in range(1,21):
    print('* '*i,i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a right triangle shape with a for-loop, using a
# start value of 1 and a step value of 2.

for i in range(1,21,2):
    print('* '*i,i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a numeric right triangle shape with a for-loop,
# that creates an auto multi dimensional list[], along with
# the 'append() function to increase or add more values
# within the for-loop. Change the value '11' to a higher
# or lower number to increase or decrease the values in
# the auto_multi_dimensional_list. Each list has its own
# set of square brackets '[ ]', which is why this Python
# program example is called a multi dimensional list
# example. However, the output on the screen shows
# the entire multi dimensional list, but the commas that
# join multi dimensional lists to other lists are not shown
# on the screen output. All you need to do is add the commas
# yourself, if you want to use the program for real. You can
# use a multi dimensional list, and let Python fill in the gaps.

auto_multi_dimensional_list = []

for i in range(1,11):
    auto_multi_dimensional_list.append(i)
    print(auto_multi_dimensional_list)

# Let's call a value on the screen output.

print(auto_multi_dimensional_list[3])

# Let's create a real multi dimensional list by copying, then
# pasting the fake multi dimensional list screen output and,
# then placing all the commas, that join all the separate lists
# together, that make up the multi dimensional list, as you
# can clearly see below.

real_auto_multi_dimensional_list=(
    
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# invoke the length/len() function to count how many lists you
# have within your multi dimensional list. Try these examples
# below to have a much better understanding of string concatenation
# in Python.

print('You have',len(real_auto_multi_dimensional_list),'multi dimensional lists.')

# Invoke the str(), string() function to create string concatenation

print('You have '+str(len(real_auto_multi_dimensional_list))+' multi dimensional lists.')

# The new f' string formatted example for much easier string
# concatenation; Python 3 and up.

print(f'You have {len(real_auto_multi_dimensional_list)} multi dimensional lists.')

# Old, stone age formatted example, which is now depreciated
# in the Python programming language; Python 3 and up. However,
# you can still use this old, stone age format style approach to
# Python programming.

print('You have {} multi dimensional lists.'.format(len(real_auto_multi_dimensional_list)))

# Here is how to call up multi dimensional list values.

print(real_auto_multi_dimensional_list[0][0])

print(real_auto_multi_dimensional_list[1][0])

print(real_auto_multi_dimensional_list[1][1])

print(real_auto_multi_dimensional_list[1][1])

print(real_auto_multi_dimensional_list[2][2])

print(real_auto_multi_dimensional_list[9][8])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create an Integer Number line with a for-loop, using
# a start value of 10, a stop value of 11 and a step value
# of 1

for i in range(-10,11,1):
    print(i,end=', ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
# Create a for-loop that breaks when i==10.

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in nums:
    if i==10:
        print(f'{i}: I found number "{i}" ')
        break
    print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a for-loop that continues on when i==10.

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in nums:
    if i==10:
        print(f'{i}: I found number "{i}" ')
        continue
    print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Loop through a tuple using a for-loop, along with
# a 'print' statement message 'I am number'

tuple_loop=(
    'One','Two',
    'Three','Four',
    'Five','Six',
    'Seven','Eight',
    'Nine','Ten'
    )

for i in tuple_loop:
    print('I am number '+i+'.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Loop through a tuple using a for-loop.        

tuple_loop=(
    'One','Two',
    'Three','Four',
    'Five','Six',
    'Seven','Eight',
    'Nine','Ten'
    )

for i in tuple_loop:
    print(i,end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create while-loops that can find numbers, then make them break
# or keep on incrementing 'i' until 'i=30. Type and execute/run the
# program examples below and see what happens.

i=1
while i<=30:
    print(i)
    i+=1
    if i==20:
        print(f'"{i}" I found number "{i}". I will break the loop now.')
        break
 
i=1
while i<=30:
    print(i)
    i+=1
    if i==20:
        print(f'"{i}" I found number "{i}". I will keep looping, until "i=30".')
        i+=1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a for-loop, using an 'input' statement that
# allows the user to input the number of the for-loop.

while True:
    try:
        enter_num=int(input('Please enter a number, or numbers ').strip())    
        for i in range(1,enter_num+1):
            print('* '*i,i)
        break
    except ValueError:
        print(f'Sorry! Numbers only please.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a for-loop, using an 'input' statement that
# allows the user to input the number of the for-loop.
# If a number doesn't exist, the for-loop breaks.

while True:
    try:
        enter_num=int(input('Enter any number up to 20 and I will find it. ').strip())    
        for i in nums:
            if i==enter_num:
                print(f'{i}: I found number "{i}" ')
                break
            elif enter_num<1:
                print(f'Sorry! I cannot find "{enter_num}" ')
                break
            elif enter_num>20:
                print(f'Sorry! I cannot find "{enter_num}" ')
                break
            print(i)
        break
    except ValueError:
        print('Sorry! Numbers only please.')

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs...

# "The Ultimate Python Programmer's Bible"

# Object-Oriented programming language

# Created by Joseph C. Richardson, GitHub.com

# Please note: these Python program examples are a
# mixed bag of both beginner and advanced Python
# programming skills. These Python program examples
# have no, such order of which is which. However, by
# the time you reach an understanding of Python
# Object-Oriented programing, you will be able to grasp
# the advanced Python program examples this book
# has to offer. Because great programming always
# starts with a great programmer's manual...

# All these Python program examples are from years
# of studying Python programming since Christmas day,
# 2017. To this day, I'm always learning brand new things
# about Python programming. Some of these Python
# programming examples are from my other book, called
# "Python Programmer's Glossary Bible". Please note:
# for those who are just starting to learn what Python
# programming is all about, I would suggest that you
# start with "Python Programmer's Glossary Bible", that
# teaches the programmer how to properly indent Python
# code blocks with ease, as well as how to keep Python
# programming DRY: (Don't Repeat Yourself); also shown
# in some of these Python programming examples.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpack multiple values, using just one, single "=" sign.
# Not: You must use equal variables to equal values.

a,b,c = 1,2,3

print(a,b,c)

# Add the values together.

print(a+b+c)

# Example 2:

a,b,c,d,e,f = 1,2,3,4,5,6

print(a,b,c,d,e,f)

# Add the values together.

print(a+b+c+d+e+f)

# Example 3

name1,name2,name3 = 'Bob','Rob','John'

print(name1,'and',name2,'went to',name3+"'s",'house for dinner.')

# You can use the f' string format to make the above print statement
# read like this.

print(f"{name1} and {name2} went to {name3}'s house for dinner.")

# Old format example of the print statement from earlier Python versions.

print("{} and {} went to {}'s house for dinner.".format(name1,name2,name3))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpacking multi-list example:

list_1,list_2,list_3 = [
    [0,1,2,3,4,5,6,7,8,9],
    ['a','b','c','d','e','f','g','h','i','j','k','l','m',
     'n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['"Python',"Programmer's",'Glossary','Bible"']]

print(list_1[9])
print(list_2[0])
print(list_3[0],list_3[1],list_3[2],list_3[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpacking multi-list for-loop example:

list_1,list_2,list_3 = [
    [0,1,2,3,4,5,6,7,8,9],
    ['a','b','c','d','e','f','g','h','i','j','k','l','m',
     'n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['"Python',"Programmer's",'Glossary','Bible"']
    ]

for i in list_1,list_2,list_3:
    print(i[0],i[1],i[2],i[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python scoping with strings and integer values

print(type('string'))

# <class 'str'>

print(type(2))

# <class 'int'>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# View string fuctions and string methods.

print(dir('string'))

# View integer fuctions and integer methods.

print(dir(2))

# Get the id from a string.

print(id('string'))

# Get the id from an integer.

print(id(2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These two 'print' statements below use the dunder method 'add',
# which is the same as the 'print' statements 'print(2+3)' and 'print('a'+'b')'.
# The 'int' function adds only integer numbers together, whereas the
# str' function concatenates/joins character strings together.

print(int.__add__(2,3))

# Screen output:	5

print(str.__add__('a','b'))

# Screen output:	ab
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Dunder methods assure functionality inside class functions. For
# example, you wouldn't use a dunder '__str__' method with integer
# values; likewise, you wouldn't use a dunder '__add__' method
# with character string values.

# Take a close look at these two program examples below. You notice
# there are yellow highlighted variables. These variables indicate how
# these two, very same program examples can be written. Both program
# examples do exactly the same thing, even though they look a wee bit
# different. Type and execute/run these two program examples below
# and see what happens.

# Program example 1:

class Dunder_add:
    def __init__(self,num):
        self.num = num

    def __add__(self,plus):
        return self.num+plus

a = Dunder_add(6)
b = Dunder_add(8)
c = Dunder_add(12)

print(a.num+b.num+c.num)

# Program example 2:

class Dunder_add:
    def __init__(self,num):
        self.num = num

    def __add__(self,plus):
        return self.num+plus.num

a = Dunder_add(6)
b = Dunder_add(8)
c = Dunder_add(12)

print(a+b+c.num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = {1,2,3,4,9,6,7,8,5,9}
y = {10,11,15,13,14,12,16,17,18,19,19}
z = {20,21,22,23,27,25,26,24,28,29,22}

unionize = x.union(y).union(z)

convert = list(unionize)

a = slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = {1,2,3,4,9,6,7,8,5,9}
y = {10,11,15,13,14,12,16,17,18,19,19}
z = {20,21,22,23,27,25,26,24,28,29,22}

unionize = x.union(y,z)

convert = list(unionize)

a = slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a = list()
for i in range(10):
    a.append(i)

b = set()
for i in range(10):
    b.add(i)

print(a)
print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 | nums2) # Union

print(nums1.union(nums2)) # Union

nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 & nums2) # Intersection

print(nums1.intersection(nums2)) # Intersection

nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 - nums2) # Difference

print(nums1.difference(nums2)) # Difference

nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 ^ nums2) # Symmetric Difference
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1 = {0,1,2,3,1,3,4,10,5,6,6,7,8,9,10,23}
nums2 = {1,2,7,1,3,4,10,5,6,6,7,8,9,10,11,22}

print(nums1 | nums2)
print(nums1 & nums2)
print(nums1 - nums2)
print(nums1 ^ nums2)

nums1 = [1,2,3,1,3,4,10,5,6,6,7,8,9,10]
nums2 = [1,2,3,1,3,4,10,5,6,6,7,8,9,10]

uniques1 = set(nums1)
uniques2 = set(nums2)

print(uniques1 | uniques2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums = {0,1,2,3,1,3,4,10,5,6,6,7,8,9,10}

try:
    num = int(input('Enter a number: '))
    if num in nums:
        print(f'{num} is in nums.')
    elif num not in nums:
        print(f'{num} is not in nums.')
except ValueError:
    print('Sorry! I cannot do that.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nums1 = {1,1,2,3,4,5,6}
nums2 = {1,2,2,3,4}

print(nums1 | nums2) # Union
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_set = ['Fast','Fast','Frog','Fish','Frog','Fog','Floor']

print('This unsorted list',my_set,'has duplicates in it.')

duplicate = set(my_set)

print('\nThis converted set from a list',duplicate,'has no \
duplicates in it, but is always in random order.')

duplicate = sorted(duplicate)
my_set = list(duplicate)

print('\nThis random set order converts back into a sorted, \
non-duplicated list.',duplicate,)

print(f'\nNow you can call up a sorted, non-duplicate list item \
like this "{duplicate[4]}"')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = tuple('123456789')

print(x)

x = tuple(('123456789','abcdefghij'))

print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
num1,num2 = 0,1
fib = {num1,num2}

y,a,b = 100,'is in the Fibonacci Number \
Sequence.','is not in the Fibonacci Number Sequence.'

for i in range(y):
    fib_num = num1+num2
    fib.add(fib_num)
    num1 = num2
    num2 = fib_num

while True:
    try:
        x = int(input('Please enter a correct Fibonacci Sequence Number: '))
        if x in fib:
            print(x,a)
        elif x not in fib:
            print(x,b)
    except ValueError:
        print('Sorry! Numbers only please.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# input Fibonacci Number Sequence example, using a set{}

num1,num2 = 0,1

fib = {num1,num2}

words = (
    'is in the Fibonacci Sequence.',
    'is not in the Fibonacci Sequence.',
    'Please enter a correct Fibonacci Sequence Number: ',
    'Sorry! Numbers only.',
    'Memory Error!'
    )

try:
    x = int(input(words[2]).strip())

    for i in range(x):
        fib_num = num1+num2
        fib.add(fib_num)
        num1 = num2
        num2 = fib_num

    if x in fib:
        print(x,words[0])

    elif x not in fib:
        print(x,words[1])

except ValueError:
    print(words[3])

except MemoryError:
    print(words[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os,time;os.system('')

text_colours = (
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

text_words = (
    f'\n"Python Programmer\'s Glossary Bible" by Joseph \
C. Richardson','cls'
    )

length = 0
while length <= len(text_words[0]):
    for i in text_colours:
        print(i+text_words[0][:length])
        time.sleep(.05)
        os.system(text_words[1])
        length += 1

print(i+text_words[0])

input('\nPress Enter to exit.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Random Generator Examples:

import random

print(random.randint(1,9))

print(random.randrange(1,9))

print(random.randrange(3,9,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

print(random.random())

print(random.uniform(20,60))

print(random.triangular(20,60,30))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

random_list = ['Random 1','Random 2','Random 3','Random 4']

print(random.choice(random_list))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

random_list = [
    'Random 1','Random 2',
    'Random 3','Random 4'
    ]

random.shuffle(random_list)

print(random_list[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

random_list = [
    'Random Least1','Random Least2',
    'Random Less','Random Most'
    ]

print(random.choices(random_list,weights = [5,10,25,50],k = 8))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

random.seed(10)

print(random.random())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

random.seed(10)

print(random.getstate())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

print(random.getrandbits(4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

print(random.random())

# capture the state:

state = random.getstate()

# print another random number:

print(random.random())

# restore the state:

random.setstate(state)

# and the next random number should be
# the same as when you captured the state:

print(random.random())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.randint(100)
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.rand()
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.randint(100,size = (5))
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.randint(100,size = (3,5))
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.rand(5)
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.rand(3,5)
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.choice([3,5,7,9])
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.choice([3,5,7,9], size = (3,5))
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.choice([3,5,7,9],p = [0.1,0.3,0.6,0.0],size = (100))
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random

x = random.choice([3,5,7,9],p = [0.1,0.3,0.6,0.0],size = (3,5))
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])

random.shuffle(arr)
print(arr)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5])
print(random.permutation(arr))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os,math,random
from time import sleep

while True:
    random_num = random.randint(1,10)
    if  random_num == 10:
        print(f'{random_num} is equal to 10. The loop breaks')
        break
    elif random_num != 10:
        print(f'{random_num} is not equal to 10. The loop repeats')
        sleep(1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This conditional while-loop example compares a random number
# against user input data. If the user picks the right number by luck
# alone, the while-loop will break out and the program ends. If the
# user picks the wrong number, the less (<) than or greater (>) than
# 'random_num' variable gets conditioned and the while-loop keeps
# on iterating until the right number is picked, via user input data.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order
# that Python executes/runs its program statements.

# Note: The 'import random' module must be imported first.

import random

random_num = random.randint(1,10)

while True:
    try:
        pick_num = int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())

        if pick_num < random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num > random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations! You won. "{random_num}" was the \
number I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This very same program example as above works exactly the same
# way, but with one major difference; the while loop will only iterate three
# times. If the user picks the right number, the while loop breaks. If the
# user doesn't pick the right number after three times, the 'else' statement
# executes and says 'Sorry! You lost.', which ends the program.

# Note: the 'import random' module must be imported first.

import random

random_num = random.randint(1,10)

i = 0

while i < 3:
    try:
        pick_num = int(input('\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10: ').strip())

        i += 1

        if pick_num < random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num > random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')

else:
    print('\nSorry. You lost!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Once again, this is the very same program example as above before.
# However, this time the loop iterates in reverse instead of forward and
# the user is shown how many guesses they have left before they win
# or lose.

# Note: the 'import random' module must be imported first.

import random

random_num = random.randint(1,10)

i = 3

while i > 0:
    try:
        pick_num = int(input(f'\nWhat number am I thinking of? Hint! It\'s \
between 1 and 10:\n\nYou have {i} gesses left. ').strip())

        i -= 1

        if pick_num < random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num > random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations. You won! "{random_num}" was the number \
I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')

else:
    print('\nSorry. You lost!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 10**1
print(f'{x:,}') #  = 10 (TEN)

x  =  10**2
print(f'{x:,}') #  = 100 (ONE HUNDRED)

x = 10**3
print(f'{x:,}') #  = 1,000 (ONE THOUSAND)

x = 10**4
print(f'{x:,}') #  = 10,000 (TEN THOUSAND)

x = 10**5
print(f'{x:,}') #  = 100,000 (ONE HUNDRED THOUSAND)

x = 10**6
print(f'{x:,}') #  = 1,000,000 (ONE MILLION)

x = 10**9
print(f'{x:,}') #  = 1,000,000,000 (ONE BILLION)

x = 10**12
print(f'{x:,}') #  = 1,000,000,000,000 (ONE TRILLION)

x = 10**15
print(f'{x:,}') #  = 1,000,000,000,000,000 (ONE QUADRILLION)

x = 10**18
print(f'{x:,}') #  = 1,000,000,000,000,000,000 (ONE QUINTILLION)

x = 10**21
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000 (ONE SEXTILLION)

x = 10**24
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000 (ONE SEPTILLION)

x = 10**27
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000 (ONE OCTILLION)

x = 10**30
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000 (ONE NONILLION)

x = 10**33
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000 (ONE DECILLION)

x = 10**36
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000 (ONE UNDECILLION)

x = 10**39
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE DUODECILLION)

x = 10**42
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE TREDECILLION)

x = 10**45
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE QUATTTUOR-DECILLION)

x = 10**48
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE QUINDECILLION)

x = 10**51
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE SEXDECILLION)

x = 10**54
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE SEPTEN-DECILLION)

x = 10**57
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE OCTODECILLION)

x = 10**60
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE NOVEMDECILLION)

x = 10**63
print(f'{x:,}') #  = 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 (ONE VIGINTILLION)

x = 10**303
print(f'{x:,}') #  = 303 0's (ONE CENTILLION)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import math

print(min(3,6,9))

print(max(3,6,9))

print(pow(2,3))

print(abs(-10))

print(math.sqrt(9))

print(math.floor(45.17))

print(math.ceil(45.17))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def myfunc():
  global x
  x = 'fantastic.'

myfunc()

print('Python is '+x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Super_class:
    def super1(self):
        print('Super1')

    def super2(self):
        print('Super2')

    def super3(self):
        print('Super3')

class Class_all(Super_class):
    def get_values(self):
        super().super1()
        super().super2()
        super().super3()

Class_all().get_values()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class A:
    def __init__(self):
        super().__init__()
        print('first')

class B:
    def __init__(self):
        super().__init__()
        print('second')

class C:
    def __init__(self):
        super().__init__()
        print('third')

class D:
    def __init__(self):
        super().__init__()
        print('forth')

class All(A,B,C,D):
    def __init__(self):
        super().__init__()

All()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This conditional while-loop will loop as long as the value is less (<)
# than 3, then it will stop its iteration no matter what wrong keys the
# user tries to type.

chance = 0

name = input('\nWhat is your name please? ').strip()

while chance < 3:
    try:
        age = int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print(f'\nYou have 3 chances left before the while-loop breaks out anyway!')

        chance += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This for-loop example does exactly the same thing, the above while
# -loop example shows. The only difference is, the while-loop is a
# conditional loop, whereas the for- loop is an iterate. While-loops can
# also be 'True:' or 'False:', depending on the outcome of a program's
# excution run. While-loops also compare data greater than or less
# than other data, as shown in the examples above.

name = input('\nWhat is your name please? ').strip()

for chance in range(3):
    try:
        age = int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print('\nYou have 3 chances left before the while-loop breaks out anyway!')

        chance += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This program example has three, separate conditional while-loops,
# each of them compares data against user input data. The first while
# -loop asks for the user's first name. The second while-loop asks
# for the user's last name, and the third while-loop asks for the user's
# age. In the first and second while-loop, the user's first name and
# user's last name are compared by how many letters the user types.
# The 'str([first_name])' statement makes the user type in text only,
# not integers.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order
# that Python executes/runs its program statements.

while True:
    first_name = input('\nWhat is your name please? ').strip()

    if first_name < str([first_name]):
        print('\nError: text only please!')

    elif len(first_name) < 3:
        print('\nYour first name must be over 2 characters long.')

    elif len(first_name) > 10:
        print('Your first name must be under 10 characters long.')

    else:
        break

while True:
    last_name = input(f'\nNice to meet you {first_name.title()}. \
What is your last name please? ').strip()

    if last_name < str([last_name]):
        print('\nError: text only please!')

    elif len(last_name) < 3:
        print('\nYour last name must be over 2 characters long.')

    elif len(last_name) > 10:
        print('\nYour last name must be under 10 characters long.')

    else:
        break

while True:
    try:
        age = int(input(f'\nHow old are you {first_name.title()}? ').strip())
        break

    except ValueError:
        print('\nError: integers only please!')

print(f'\nYour first name = {first_name.title()}:\nYour last name = \
{last_name.title()}:\nYour age = {age}:\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here's a fun, simple program example, which tells you how many
# seconds you have been on Earth for. Type and execute/run the
# program example below and see what happens when you type your
# age, then press the 'Enter' key. Note: this program example also
# uses the 'finally' statement to illustrate the use of the how the 'finally'
# command works. The 'finally' command will always execute, no
# matter the outcome. Also note that the 'finally' command only works
# with the 'try' and 'except' command blocks.

months = 12
weeks = 52
days = 365

hours_per_day = 24
minuts_per_hour = 60
seconds_per_minute = 60

string_tuple = (
    months,weeks,days,
    hours_per_day,
    minuts_per_hour,
    seconds_per_minute
    )

while True:

    try:
        age = int(input('How old are you? ').strip())

        print(f'\nYou have been on Earth for {age} years.')

        print(f'\nYou have been on Earth for {age*string_tuple[0]:,} months.')

        print(f'\nYou have been on Earth for {age*string_tuple[1]:,} weeks.')

        print(f'\nYou have been on Earth for {age*string_tuple[2]:,} days.')

        print(f'\nYou have been on Earth for {age*string_tuple[2]*string_tuple[3]:,} hours.')

        print(f'\nYou have been on Earth for \
{age*string_tuple[2]*string_tuple[3]*string_tuple[4]:,} minutes.')

        print(f'\nYou have been on Earth for \
{age*days*string_tuple[3]*string_tuple[4]*string_tuple[5]:,} seconds.')

        break

    except ValueError:
        print('\nSorry! Numbers only please.\n')

    finally:
        print('Finally will always execute no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This conditional while-loop example types out the words "Python
# Programmer\'s Glossary Bible". As long as 'length' is less (<) than
# 'len' starting at "0", the while-loop will keep on looping until  'length'
# is equal to 'len'. The 'os.system('cls')' function clears the screen
# each cycle through the while-loop, and the 'time.sleep(.05)' function
# delays the while-loop in between cycles. This fun, little program
# example makes the printout on the screen appear as if it were
# actualy typing letters.

# Note: Python executes/runs programs starting from the top, downward.
# Be very careful on how you place statements. Some statements cannot
# execute right, even if they work. This is simply because of the order
# that Python executes/runs its program statements.

# Note: The 'import os' module and the 'import time' module must be
# imported first.

import os
import time

letters = '\n"Python Programmer\'s Glossary Bible"'
length = 0

while length <= len(letters):
    os.system('cls')
    print(letters[:length])
    time.sleep(.05)
    length += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# See what happens when you type and execute/run this guessing game
# program example below. Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python program file itself.

# Save the Python file as 'Know Your Stuff'

import os

tc = (
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[35m',
    '\x1b[36m',
    '\x1b[37m',
    'cls'
    )

question_prompts1 = (
    f'{tc[2]}How many sides does a Triangle have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}two sides',

    f'{tc[2]}How many sides does a Square have?\n\n{tc[1]}(a) {tc[2]}Two sides\n\
{tc[1]}(b) {tc[2]}Three sides\n{tc[1]}(c) {tc[2]}Four sides',

    f'{tc[2]}How many sides does a Pentagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}Three sides',

    f'{tc[2]}How many sides does a Hexagon have?\n\n{tc[1]}(a) {tc[2]}six sides\n\
{tc[1]}(b) {tc[2]}five sides\n{tc[1]}(c) {tc[2]}two sides',

    f'{tc[2]}How many sides does a Octagon have?\n\n{tc[1]}(a) {tc[2]}four sides\n\
{tc[1]}(b) {tc[2]}six sides\n{tc[1]}(c) {tc[2]}eight sides',

    f'{tc[2]}How many sides does a Dodecagon have?\n\n{tc[1]}(a) {tc[2]}eight \
sides\n{tc[1]}(b) {tc[2]}three sides\n{tc[1]}(c) {tc[2]}twelve sides',

    f'{tc[2]}How many sides does a Hexadecagon have?\n\n{tc[1]}(a) {tc[2]}sixteen \
sides\n{tc[1]}(b) {tc[2]}eight sides\n{tc[1]}(c) {tc[2]}six sides'
    )

prompt = ('b','c','b','a','c','c','a')

score = 0
loop = 0

while loop <= 6:

    os.system(tc[7])
    button = input((tc[1])+'\nKnow Your Stuff!\n\n'+(tc[2])+'Know Your Polygons\n\n'+\
    question_prompts1[loop]+'\n\n'+(tc[0])+'READY:'+(tc[1])).strip()

    if button == (prompt[loop]):
        score += 1

    loop += 1

    os.system(tc[7])

print(f'\n{tc[2]}Know Your Polygons\n\n{tc[2]}You got \
{score}/{len(question_prompts1)} questions correct.\nCongratulations! Your total \
Prize Winnings: {tc[1]}${score*100*score:,}.00 {tc[2]}Dollars.\n\n{tc[0]}READY:')

input('\nEND OF PROGRAM! Press Enter to quit.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's have fun and learn how to raise some errors to test in Python
# programs.

try:
    print('Raising an Exception:')
    raise Exception
except Exception:
    print('Exception:')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    print('Raising a ValueError:')
    raise ValueError
except ValueError:
    print('ValueError:')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    print('Raising a TypeError:')
    raise TypeError
except TypeError:
    print('TypeError:')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    print('Raising a NameError:')
    raise NameError
except NameError:
    print('NameError:')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    print('Raising a IndexError:')
    raise IndexError
except IndexError:
    print('IndexError:')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    print('Raising a MemoryEorror:')
    raise MemoryError
except MemoryError:
    print('MemoryError:')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Raise a list of possible errors to test in Python programs.

try:
    print('Raising a list of possible errors to test:')
    raise Exception
    raise ValueError
    raise TypeError
    raise NameError
    raise IndexError
    raise MemoryError
except Exception:
    print('Exception:')
except ValueError:
    print('ValueError:')
except TypeError:
    print('TypeError:')
except NameError:
    print('NameError:')
except IndexError:
    print('IndexError:')
except MemoryError:
    print('MemoryError:')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a basic, skeletal structure of a Try: and Except: block. The 'Pass'
# statement ignores any empty code blocks, which are not used for now.
# In this case, only the skeletal structure of the program is clearly shown.
# Note:  you do not need to invoke the 'finally' statement into try: and
# Except: blocks, but they can be quite handy when you want to show
# any output on the screen, no matter the outcome of the program's
# execution/run.

try:
    pass
except Exception:
    pass
finally:
    pass

try:
    num = int(input('Type a Number: ').strip())
except ValueError:
    print('Sorry! Numbers only please.')
finally:
    print('finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a dictionary that uses strings as keys and values, instead of
# of actual text, like we did before. Let's create two, simple tuples; one for
# the key tuple and one for the value tuple. We can also create them with or
# without parentheses, but a '\' backslash must be implemented in place of the
# parentheses. However, the Python programming standard shows only the
# constant use of parentheses, not backslashes, as you can see in the next
# example below.

key = 'dog','cat','mouse','bird','fish' # tuple by default

value = (
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

key = 'dog','cat','mouse','bird','fish' # tuple by default

value =\
        'Grey Wolf','Huge Tigger',\
        'Black Rat','Macaw Parrot',\
        'Great White Shark' # tuple by default

dictionary = { # dictionary
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the dict() function to manually create a dictionary with Python

dictionary = dict(key1 = 'Value1',Key2 = 'Value2',Key3 = 'Value3')

keys = dictionary.keys()

values = dictionary.values()

print(dictionary)  # {'key1': 'Value1', 'Key2': 'Value2', 'Key3': 'Value3'}

print(dictionary.get('key1'))  # Value1

print(dictionary.get('key4','key not found:'))  # optional

print(keys)  # dict_keys(['key1', 'Key2', 'Key3'])

print(values)  # dict_values(['Value1', 'Value2', 'Value3'])

print(f'You have {len(keys)} keys and {len(values)} values: ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Things you can do with tuples and lists.

# Tuple Example:

variable_1 = 'dog','cat','bird','guppy'

variable_2 = (
    'Grey Wolf','Huge Tigger',
    'Macaw Parrot','Great White Shark')

variable_3 = 'John','Rob','Ron','Bob'

variable_4 = 'Mom','Dad','Brother','Sister'

variable_5 = 'friend','girlfriend','boyfriend','neighbour'

for var1,var2,var3,var4,var5 in zip(variable_1,variable_2,variable_3,variable_4,variable_5):
    print(f'My {var4} and my {var5} {var3} says my {var1} is really a {var2}.')

# List Example:

variable_1 = ['dog','cat','bird','guppy']

variable_2 = [
    'Grey Wolf','Huge Tigger',
    'Macaw Parrot','Great White Shark']

variable_3 = ['John','Rob','Ron','Bob']

variable_4 = ['Mom','Dad','Brother','Sister']

variable_5 = ['friend','girlfriend','boyfriend','neighbour']

for var1,var2,var3,var4,var5 in zip(variable_1,variable_2,variable_3,variable_4,variable_5):
    print(f'My {var4} and my {var5} {var3} says my {var1} is really a {var2}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Test whether a value is true or false using the logical operators:

# " ==, <, >, <=, >=, != "

a=1;b=1

print(a == a) # True
print(a < a) # False
print(a >  a) # False
print(a <= a) # True
print(a >= a) # True
print(a != a) # False

print(b == b) # True
print(b < b) # False
print(b > b) # False
print(b <= b) # True
print(b >= b) # True
print(b != b) # False

print(a == b) # True
print(a < b) # False
print(a > b) # False
print(a <= b) # True
print(a >= b) # True
print(a != b) # False

print(b == a) # True
print(b < a) # False
print(b > a) # False
print(b <= a) # True
print(b >= a) # True
print(b != a) # False

# Test whether a value is true or false using the Boolean conditionals:

# " True, False, and, or, not "

a = True;b = False

print(a and a) # True
print(b and b) # False
print(a and b) # False
print(b and a) # False

print(a and not a) # False
print(b and not b) # False
print(a and not b) # True
print(b and not a) # False

print(a or a) # True
print(b or b) # False
print(a or b) # True
print(b or a) # True

print(a or not a) # True
print(b or not b) # True
print(a or not b) # True
print(b or not a) # False

print(a is a) # True
print(b is b) # True
print(a is b) # False
print(b is a) # False

print(a is not a) # False
print(b is not b) # False
print(a is not b) # True
print(b is not a) # True

# Check to see if a variable contains a value.

numbers = 1,2,3,4,5,6,7,8,9,10

print(1 in numbers) # True
print(9 in numbers) # True
print(11 in numbers) # False
print(11 not in numbers) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's fully understand what a 2d list is truly all about.
# A 2d list is a two dimensional array that can hold multiple
# 2d list array values under a single variable. For example:

my_2d_list = ['2d list0'],['2d list0']

print(my_2d_list[0][0])
print(my_2d_list[1][0])

# If you create a really long 2d list such as this example below,
# you can force hard line-breaks, but you must use outer square
# brackets '[]' to surround the entire 2d list values. Note: you
# must use commas at the end of each 2d list array.

# Example 1:

my_2d_list = ['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0'],['2d list0']

print(my_2d_list[4][0])

# Example 2:

my_2d_list = [ # use a hard line-break make the 2d list look neat and tidy.
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0'],['2d list0'],['2d list0'],
    ['2d list0']] # use a hard line-break to add more values to the 2d list.

print(my_2d_list[4][0])

# Create a multi-2d list array like this example below illustrates.

my_multi_2d_list = ['Value0','Value1','Value2'],['Value0','Value1','Value2']

print(my_multi_2d_list[0][0])
print(my_multi_2d_list[0][1])
print(my_multi_2d_list[0][2])

print(my_multi_2d_list[1][0])
print(my_multi_2d_list[1][1])
print(my_multi_2d_list[1][2])

# You can create as many multi-2d list array values as you please.
# For example:

my_multi_2d_list = [
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2','Value3'],
    ['Value0','Value1','Value2','Value3','Value4']] # neat and tidy

print(my_multi_2d_list[0][2])
print(my_multi_2d_list[1][3])
print(my_multi_2d_list[2][4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's have some multi-2d list fun using a for-loop
# and see what happens when we execute/run this multi-2d
# list, for-loop example:

my_multi_2d_list = [
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2'],
    ['Value0','Value1','Value2']] # neat and tidy

for i in my_multi_2d_list:
    print(i[0],i[1],i[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a real, working multi-2d list to see what
# they are truly all about in a real Python program scenario.
# We will call our multi-2d list, 'names'. Use the (f') format
# to make the 'print' statement easier to concatenate strings.

names = [
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']] # neat and tidy

for i in names:
    print(f'{i[0]}, {i[1]} and {i[2]} went to the store.')

# Let's create a looping sentence tuple with our multi-2d list for-loop
# example and see what happens when we execute/run this Python
# program example below.

names = [
    ['Ron','Bob','Tom'],
    ['John','Mary','Terry'],
    ['Edie','Freddy','Teddy'],
    ['Charie','Marty','Harvey']] # neat and tidy

sentence = (
    ('went home to have dinner.',
    'went to the store to buy some food.',
    'wanted some pizza for breakfast.',
    'wanted computers for Christmas.',
    'love their computers.'))

for i in range(4):
        print(f'{names[i][0]}, {names[i][1]} \
and {names[i][2]} {sentence[i]}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Advanced List and Dictionary examples

# Please note: these list and dictionary examples don't
# have any comments, other than these seven comments
# only. However, I will be adding lots of comments to these
# advanced list and dictionary examples when I update my
# Python book: "Python Programmer's Glossary Bible". Until
# then, experiment with these list and dictionary examples.

dictionary_list = {
    'Animals':['Dog','Cat','Bird','Fish'],

    'Reptiles':['Turtle','Lizard','Snake','Frog'],

    'Insects':['Butterfly','Beetle','Ant','Bee']
    }

for values in range(4):
    print(dictionary_list['Animals'][values])

for values in range(4):
    print(dictionary_list['Reptiles'][values])

for values in range(4):
    print(dictionary_list['Insects'][values])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dictionary_list = {
    'Animals':['Dog','Cat','Bird','Fish'],

    'Reptiles':['Turtle','Lizard','Snake','Frog'],

    'Insects':['Butterfly','Beetle','Ant','Bee']
    }

for key,value in dictionary_list.items():
    print(key,value[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
min_nums_list = min(0,1,2,3,4,5,6,7,8,9)

print(min_nums_list)

max_nums_list = max(0,1,2,3,4,5,6,7,8,9)

print(max_nums_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
enumerate_list = [
    'Value index ','Value index ',

    'Value index ','Value index '
    ]

for index,value in enumerate(enumerate_list):
    print(value,index)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
search_in_list = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

print('Value 1' in search_in_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
extend_list1 = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

extend_list2 = [
    'Value 4','Value 5',

    'Value 6','Value 8'
    ]

extend_list1.extend(extend_list2)

print(extend_list1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
append_list1 = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

append_list2 = [
    'Value 4','Value 5',

    'Value 6','Value 8'
    ]

append_list1.append(append_list2)

print(append_list1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
clear_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

clear_list_value.clear()

print(clear_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
del_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

del del_list_value[2]

print(del_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
remove_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

remove_list_value.remove('Value 2')

print(remove_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
pop_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

pop_list_value.pop()

print(pop_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
insert_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

insert_list_value.insert(4,'Value 4')

print(insert_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
sort_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

sort_list_value.sort()

print(sort_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
sorted_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

sorted_list_value = sorted(sorted_list_value)

print(sorted_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
reverse_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

reverse_list_value.reverse()

print(reverse_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
reverse_list_value = [
    'Value 0','Value 1',

    'Value 2','Value 3'
    ]

reverse_list_value.sort(reverse = True)

print(reverse_list_value)

reverse_list_value.sort(reverse = False)

print(reverse_list_value)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
split_string = "Let's split up a string"

print (split_string.split('split'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
split_list = 'split split split split'

print (split_list.split('split',0))
print (split_list.split('split',1))
print (split_list.split('split',2))
print (split_list.split('split',3))
print (split_list.split('split',4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
list_set = [
    'string value1',
    'string value2',
    'string value3']

print(list_set)

join_string = '--join--'.join(list_set)

print(join_string)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a tuple list with an 'IndexError' handler. If a value is not
# found, then the 'try' and 'except IndexError' handler will execute.
# If a value is found, the 'try' and 'except IndexError' handler are
# ignored, but the 'finally' statement will always execute no matter
# the outcome.

tuple_list = (
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    )

try:
    print(tuple_list[16])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a single list with an 'IndexError' handler. If a value is not
# found, then the 'try' and 'except IndexError' handler will execute.
# If a value is found, the 'try' and 'except IndexError' handler are
# ignored, but the 'finally' statement will always execute no matter
# the outcome.

single_list = [
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

try:
    print(single_list[16])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Extend the single_list1 and the single_list2 with the '.extend()'
# function. Once again, If a value is not found, then the 'try' and
# 'except IndexError' handler will execute. If a value is found, the
# 'try' and 'except IndexError' handler are ignored, but the 'finally'
# statement will always execute no matter the outcome.

single_list1 = [
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

single_list2 = [
    'Value pos:0','Value pos:1',
    'Value pos:2','Value pos:3',
    'Value pos:4','Value pos:5',
    'Value pos:6','Value pos:7',
    'Value pos:8','Value pos:9',
    'Value pos:10','Value pos:11',
    'Value pos:12','Value pos:13',
    'Value pos:14','Value pos:15'
    ]

single_list1.extend(single_list2)

try:
    print(single_list1[32])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a multi dimensional list with an 'IndexError' handler. If a
# value is not found, then the 'try' and 'except IndexError' handler
# will execute. If a value is found, the 'try' and 'except IndexError'
# handler are ignored, but the 'finally' statement will always execute
# no matter the outcome.

multi_dim_list = (
    ['Value pos:0','Value pos:1','Value pos:2','Value pos:3'],
    ['Value pos:4','Value pos:5','Value pos:6','Value pos:7'],
    ['Value pos:8','Value pos:9','Value pos:10','Value pos:11'],
    ['Value pos:12','Value pos:13','Value pos:14','Value pos:15']
    )

try:
    print(multi_dim_list[0][4])
except IndexError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os;os.system('')

text_colours = (
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

knowledge_poem = (
f'''\n{text_colours[5]}‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.

THIS BELONGS TO EVERY MAN, WOMAN AND CHILD
Never give up your dream, no matter how far away it may seem to be, because that is when it is ever so
close to becoming true. If you dream of something long enough and strong enough, your dream will come
true, when you least expect it. Always remember, we are never too young or too old to dream and use our
imagination, for we only get one and it is ours forever. May your heart be filled with courage and
compassion, and your mind be as limitless and as wondrous as the universe itself!
If you dream it, you can be it. Believe it!\n'''
)

print(knowledge_poem)

letter = input(f'{text_colours[1]}Type a word or letter from this poem, and I will tell you how many \
times it\'s been used in it.\nNote: words and letters are case sensitive. ')

if len(letter) >=  2:
    print(f'\n{text_colours[2]}The word " {letter} " has been used {knowledge_poem.count(letter)} times in this poem.')

elif len(letter) <= 2:
    print(f'\n{text_colours[2]}The letter " {letter} " has been used {knowledge_poem.count(letter)} times in this poem.')

input(f'\n{text_colours[6]}End of knowledge_poem.count program example. Press Enter to close.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a dictionary with a 'KeyError' handler. If a value is not found,
# then the 'try' and 'except KeyError' handler will execute. If a value is
# found, the 'try' and 'except IndexError' handler are ignored, but the
# 'finally' statement will always execute no matter the outcome.

dict_key = {
    'key:0':'Value:0','key:1':'Value:1',
    'key:2':'Value:2','key:3':'Value:3',
    'key:4':'Value:4','key:5':'Value:5'
    }

try:
    print(dict_key['key:6'])
except KeyError:
    print('Value not found.')
finally:
    print('Finally always executes no matter the outcome.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The '.get()' function does exactly the same thing as the 'try' and
# 'except KeyError' handler does. However, the '.get()' function
# works with dictionaries only.

dict_key = {
    'key:0':'value:0','key:1':'value:1',
    'key:2':'value:2','key:3':'value:3',
    'key:4':'value:4','key:5':'value:5'
    }

print(dict_key.get('key:6','Value not found.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The '.update({})' function updates the dictionary's keys and values
# alike. Notice how the '.get()' function is still being used instead of
# the 'try' and 'except KeyError' handler. However, in some cases it's
# a good idea to use error handlers.

dict_key.update({
    'key:0':'New value','key:1':'value:1',
    'key:2':'value:2','key:3':'value:3',
    'key:4':'value:4','key:5':'value:5'
    })

print(dict_key.get('key:0','Value not found.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# key example 1:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example[1])
print(key_example[2])
print(key_example[3])
print(key_example[4])
print(key_example[5])
print(key_example[6])
print(key_example[7])
print(key_example[8])

# key example 2:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example[1],end=' ')
print(key_example[2],end=' ')
print(key_example[3],end=' ')
print(key_example[4],end=' ')
print(key_example[5],end=' ')
print(key_example[6],end=' ')
print(key_example[7],end=' ')
print(key_example[8],end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Get key example 1:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example.get(1))
print(key_example.get(2))
print(key_example.get(3))
print(key_example.get(4))
print(key_example.get(5))
print(key_example.get(6))
print(key_example.get(7))
print(key_example.get(8))

print(key_example.get(9))

print(key_example.get(9,'Key Not Found!'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Get key example 2:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

print(key_example.get(1),end=' ')
print(key_example.get(2),end=' ')
print(key_example.get(3),end=' ')
print(key_example.get(4),end=' ')
print(key_example.get(5),end=' ')
print(key_example.get(6),end=' ')
print(key_example.get(7),end=' ')
print(key_example.get(8),end=' ')

print(key_example.get(9),end=' ')

print(key_example.get(9,'Key Not Found!'),end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For-loop key example 1:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,9):
    print(key_example[i])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For-loop key example 2:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,9):
    print(key_example[i],end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For-loop get key example 1:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key Not Found!'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For-loop get key example 2:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key Not Found!'),end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For-loop get key example 3:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key '+str(i)+' Key Not Found!'),end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For-loop get key example 4:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,'Key {} Key Not Found!'.format(i)),end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# For-loop get key example 5:

key_example = {
    1:'Key example 1',2:'Key example 2',
    3:'Key example 3',4:'Key example 4',
    5:'Key example 5',6:'Key example 6',
    7:'Key example 7',8:'Key example 8'
    }

for i in range(1,11):
    print(key_example.get(i,f'Key {i} Key Not Found!'),end=' ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpack multi-dictionary key example:

key_nums,key_letters,key_words = (

{0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9},

{'a':'a','b':'b','c':'c','d':'d','e':'e',
 'f':'f','g':'g','h':'h','i':'i','j':'j','k':'k',
 'l':'l','m':'m','n':'n','o':'o','p':'p',
 'q':'q','r':'r','s':'s','t':'t','u':'u',
 'v':'v','w':'w','x':'x','y':'y','z':'z'},

{'P1':'"Python','P2':"Programmer's",
 'G':'Glossary','B':'Bible"'}
)

print(key_nums[5])

print(key_nums.get(5)) # Add optional custom keyword/keywords.

print(key_nums.get(5,'Not Found!'))

print(key_letters['a'])

print(key_letters.get('a')) # Add optional custom keyword/keywords.

print(key_letters.get('a','Not Found!'))

print(
    key_words['P1'],
    key_words['P2'],
    key_words['G'],
    key_words['B']
    )

print(
    key_words.get('P1','Not Found!'),
    key_words.get('P2','Not Found!'),
    key_words.get('G','Not Found!'),
    key_words.get('B','Not Found!')
    )
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpack multi-dictionary key for-loop example:

key_nums,key_letters,key_words = (

{0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9},

{'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f',
 'g':'g','h':'h','i':'i','j':'j','k':'k', 'l':'l',
 'm':'m','n':'n','o':'o','p':'p', 'q':'q','r':'r',
 's':'s','t':'t','u':'u','v':'v','w':'w','x':'x',
 'y':'y','z':'z'},

{'P1':'"Python','P2':"Programmer's",
 'G':'Glossary','B':'Bible"'}
)

for i in key_nums,key_letters,key_words:
    print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I know, I've covered this topic before, but I really want to hit it home, so you can
# fully understand how to use '*args' and '**kwargs' like a true Python Pro and why
# they can become quite the handy tools to know about and how to use the tools.

#Let's learn what '*args' are all about. The word '*args' simply means the word
# 'arguments' for short. One asterisk * is used for '*args'. Use '*args' when you
# don't know how many argument variables you want within your define function
# parameters. Note: you do not need to call the word '*args' as args. However,
# you will need to invoke the asterisk * to make '*args' work. Programmers
# know the word as '*args' by standard definition, but you can use your own words.

def book(*args): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

# Create your own '*args' function parameter variable as shown below.

def book(*my_unknown_num_arguments): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

# As shown in the other define function() examples above, how we needed the exact
# number of argument values to the exact number of argument variables. However,
# with '*args' you no longer have to worry about how many argument values you will
# need to satisfy the number of argument variables within the define function parameters.

# Let's do some more '*args' with return functions

def book(*args): # one argumant variable
    return 'Python Programmer\'s Glossary Bible'

print(book('by Joseph C. Richardson','add another unknown argument value.')) # two argument values

def nums(*args): # one argument variable
    return args

print(nums(2,3)) # two argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what '**kwargs' are all about. The word '**kwargs' simply means the words
# arguments' for short. Two asterisks ** are used for '**kwargs'. Use '**kwargs'
# when you don't know how many keyword argument variables you want within your
# define function parameters. Note: you do not need to call the word '**kwargs' as '**kwargs'.
# However, you will need to invoke two asterisks ** to make '**kwargs' work. Programmers
# know the word as '**kwargs' by standard definition, but you can use your own words.

def book(**kwargs): # one keyword argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword = 'keyword',argument = 'argument') # two keyword argument values

# This example is without any '**kwargs' at all; we have to name our keyword arguments.

def book(keyword_arg1,keyword_arg2): # two keyword argument variables
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword_arg1 = 'keyword',keyword_arg2 = 'argument') # two keyword argument values

# As shown in the define function() example above, how we needed the exact number of keyword
# argument values to the exact number of keyword argument variables. However, with '**kwargs'
# you no longer have to worry about how many keyword argument values you will need to satisfy
# the number of keyword argument variables within the define function parameters.

# Can you see the difference between '*args' and '**kwargs'? Yes, because the 'args' Python
# program example has the print() function right inside the def function(), whereas the
# '**kwargs' has the very same print() function inside the def function(). However, if you
# notice how the book(keyword value has equal = signs in the keyword variables, whereas
# the '*args' def function() doesn't use any equal = signs at all. This way, you can clearly see
# the difference between the two def functions(), '*args' and '**kwargs'

# book(keyword = 'keyword',argument = 'argument') # two keyword argument values

def book(*args): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

def book(**kwargs): # one keyword argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword = 'keyword',argument = 'argument') # two keyword argument values

# Let's make this even simpler, so we can truly understand and grasp this '*args' and
# '**kwargs' concepts.

# No matter how many arguments you use, the count just doesn't matter when using
# '*args' and '**kwargs'. And that's when these are great tools to have, once you learn them.
# Mind you, it even took me some time to learn all about how to fully understand and use
# these tools myself. Here is a simple form of these two types of tools. Take a really close
# look at these '*args' and '**kwargs' examples, they are broken up with ',' between all the worded
# text. They don't mind having missing arguments. The best part is, let's say you have a
# def function() with far too many parameters variables to keep track of. That's where '*args'
# and '**kwargs' really shines bright. Because without these wonderful Python tools, we would
# have to make sure we have all the counted arguments to satisfy all the variables in the
# def function's parameter range. Believe me, that can be a real headache to keep track of.

def book(*args): # one argument variable
    print('Python','Programmer\'s','Glossary Bible\n','by Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.')

def book(**kwargs): # one keyword argument variable
    print('Python','Programmer\'s','Glossary Bible\n','by Joseph C. Richardson')

book(keyword = 'keyword') # one keyword argument value

# Let's do a def function() far too many parameter values and you will see just what I mean.
# We won't use any '*args' at all. Not at all.

def book(arg_1,arg_2): # two parameter argument variables
    print('See how we have to make sure we have the exact number of parameter variables?')

book('argument_1','argument_2')

# Try to execute/run this Python program example below and see what doesn't happen.

def book(arg_1): # one parameter argument variable
    print('See how we have to make sure we have the exact number of parameter variables?')

book('argument_1','argument_2')

# This is what happens instead. You will get a parameter and argument error message.

# Traceback (most recent call last):
#  File "C:\Users\mogie54321\Desktop\EXP Python.py", line 11, in <module>
#    book('argument_1','argument_2')
# TypeError: book() takes 1 positional argument but 2 were given

# Now, let's do the headache set of argument parameters and see just how dreadful that is.
# to keep track of without the use of '*args'

def book(arg_1,arg_2,arg_3,arg_4,arg_5,arg_6,arg_7,arg_8,
         arg_9,arg_10,arg_11,arg_12,arg_13,arg_14,arg_15,arg_16,
         arg_17,arg_18,arg_19,arg_20):

    print("Wow! That's a lot of parameter argument variables. Now, I have a HEADACHE!")

book('argument_1','argument_2','argument_3','argument_4','argument_5',
     'argument_6','argument_7','argument_8','argument_9','argument_10',
     'argument_11','argument_12','argument_13','argument_14','argument_15',
     'argument_16','argument_17','argument_18','argument_19','argument_20')

# Now! Aren't you glad that '*args' exist? I sure am!! Here is our very same example below,
# using the '*args' for our savior to avoid headaches.

def book(*args):

    print("Wow! '*args' are so GREAT!")

book('argument_1','argument_2')

# The '*args' does not have to have a satisfied number of parameter arguments. Whereas
# without the '*args', we would be in deep doo doo if we had to keep track of a large parameters
# full of argument variables. OUCH! That hurts my head just to think about it. Now, just
# imagine what the world would be like without '**kwargs'? Imagine having to do countless
# keyword arguments and having to keep track of them all to make sure they're satisfied
# with the def functions() argument parameters. That would be a HUGE Headache.

# So now you know how to use these two, very important Python tools '*args' and '**kwargs'
# and what they are all about. I hope this helped.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what *args are all about. The word 'args' simply means the word
# 'arguments' for short. One asterisk * is used for *args. Use *args when you
# don't know how many argument variables you want within your define function
# parameters. Note: you do not need to call the word '*args' as args. However,
# you will need to invoke the asterisk * to make *args work. Programmers
# know the word as *args by standard definition, but you can use your own words.

def book(*args): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

# Create your own *args function parameter variable as shown below.

def book(*my_unknown_num_arguments): # one argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book('unknown number of argument values.','add another unknown argument value.') # two argument values

# As shown in the other define function() examples above, how we needed the exact
# number of argument values to the exact number of argument variables. However,
# with *args you no longer have to worry about how many argument values you will
# need to satisfy the number of argument variables within the define function parameters.

# Let's do some more *args with return functions

def book(*args): # one argumant variable
    return 'Python Programmer\'s Glossary Bible'

print(book('by Joseph C. Richardson','add another unknown argument value.')) # two argument values

def nums(*args): # one argument variable
    return args

print(nums(2,3)) # two argument values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what **kwargs are all about. The word 'kwargs' simply means the words
# 'keyword arguments' for short. Two asterisks ** are used for **kwargs. Use **kwargs
# when you don't know how many keyword argument variables you want within your
# define function parameters. Note: you do not need to call the word '**kwargs' as kwargs.
# However, you will need to invoke two asterisks ** to make **kwargs work. Programmers
# know the word as **kwargs by standard definition, but you can use your own words.

def book(**kwargs): # one keyword argument variable
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword = 'keyword',argument = 'argument') # two keyword argument values

# This example is without any **kwargs at all; we have to name our keyword arguments.

def book(keyword_arg1,keyword_arg2): # two keyword argument variables
    print('Python Programmer\'s Glossary Bible\nby Joseph C. Richardson')

book(keyword_arg1 = 'keyword',keyword_arg2 = 'argument') # two keyword argument values

# As shown in the define function() example above, how we needed the exact number of keyword
# argument values to the exact number of keyword argument variables. However, with **kwargs
# you no longer have to worry about how many keyword argument values you will need to satisfy
# the number of keyword argument variables within the define function parameters.

# Let's create some define functions that act like subroutines.

# Since there are no line numbers in Python, also means that we cannot create any such 'go to',
# or 'go sub' commands at all with Python. So how can we create subroutines with Python?. How
# can we create subroutines without making them jump to line numbers, like we did in the old days?
# Well the answer is quite simple. Let's use define functions() with a while loop to create our
# subroutine examples.

def subroutine1():
    print('You picked subroutine1')

def subroutine2():
    print('You picked subroutine2')

def subroutine3():
    print('You picked subroutine3')

while True:
    message = input('Please type 1, 2 or 3 to select the subroutine you wish to \
display or type (q) to quit: ').strip()

    if message == 'q':
        break
    while True:
        if message == '1':
            subroutine1()
            break
        elif message == '2':
            subroutine2()
            break
        elif message == '3':
            subroutine3()
            break
        else:
            print('Sorry! No subroutine for that.')
            break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ASCII CODES:

# American Standard Code for Information Interchange

# All modern day computers that support text characters such as
# keyboard interfaces use ASCII codes. Since computers can only
# see numbers, not actual characters, ASCII codes make it possible
# to use numbers to represent one, single character. Each character
# is seven bits long, which makes it equal to one eight-bit byte; the
# eighth, leftmost bit is the 'sign-bit'. If the number is positive, the
# 'sign-bit' will be a 'zero', and if the number is a negative number,
# the 'sign-bit will be a 'one'. Take a look at the illustration below to
# gain a better understanding.

# One eight-bit binary byte = 11111111 = 255 = 128 or -127
# One byte value 00000100 = '4'
# One byte value 1000100 = '-4'
# The 'sign-bit' can only be one of two states; either negative or positive.

# However, ASCII code values are read as human decimal numbers.
# For example, the ASCII code value for the capital later 'A' = '65'. The
# ASCII code value for the lowercase 'a' = '97'. The ASCII code value for
# the capital letter 'B' = '66', and the ASCII code value for the lowercase
# 'b' = '98'. Just remember every letter and every number on a computer
# keyboard has an ASCII code value to it. Below are some basic examples
# how to use ASCII code characters in your programs.'''

# Welcome to the binary beat in motion python program example:

from time import sleep as delay;import os;os.system('title Binary Beat')

red = '\x1b[31m'
green = '\x1b[32m'
blue = '\x1b[34m'
yellow = '\x1b[33m'
purple = '\x1b[35m'
white = '\x1b[37m'
os.system('cls')
n = 0

while True:
    print(white+'\n'+' '*6+'welcome to the binary beat in motion python program example'.title()
          +yellow+'\n\n'+' '*6+'1     1    1    1    1   1   1   1 = eight bits or one byte'
          +'\n\n'+' '*6+'128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = decimal number: 255''\n\n'+' '*2
          +'binary base: 2, octal base: 8, hexadecimal base: 16, decimal base: 10'.title()
          +'\n\n'+' '*3+yellow,len(f'{n:b}'),green+'binary digits: '.title()
          +yellow+f'{n:b} '+red+'=\n\n'+' '*3+yellow,len(f'{n:o}'),green+'octal digits: '.title()
          +yellow+f'{n:o} '+red+'=\n\n'+green+' '*3+yellow,len(f'{n:x}'),green+'hexadecimal digits: '.title()
          +yellow+f'{n:X} '+red+'= '+green+'\n\n'+' '*3+yellow,len(f'{n:d}'),green+'decimal digits: '.title()
          +red+'= '+yellow+f'{n:d}');delay(1);os.system('cls');n += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# To get the ASCII code value of any letter or number key, simply type and execute/run
# the program examples below and see what happens. Try using different letters and
# numbers to see their ASCII code values.

print(chr(65))
print(ord('A'))

print(chr(97))
print(ord('a'))

print(chr(66))
print(ord('B'))

print(chr(98))
print(ord('b'))

print('ASCII code',ord('A'),'is the uppercase letter',chr(65))
print('ASCII code',ord('a'),'is the lowercase letter',chr(97))

print('ASCII code',ord('B'),'is the uppercase letter',chr(66))
print('ASCII code',ord('b'),'is the lowercase letter',chr(98))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These simple dictionary program examples below illustrates the entire ASCII code
# alphabet character sets: uppercase and lowercase character sets. Type and
# execute/run the program examples below and see what happens.

ascii_lowercase_chars = (

    {'a':97,'b':98,'c':99,'d':100,

     'e':101,'f':102,'g':103,'h':104,

     'i':105,'j':106,'k':107,'l':108,

     'm':109,'n':110,'o':111,'p':112,

     'q':113,'r':114,'s':115,'t':116,

     'u':117,'v':118,'w':119,'x':120,

     'y':121,'z':122}
    )

ascii_uppercase_chars = (

    {'A':65,'B':66,'C':67,'D':68,

     'E':69,'F':70,'G':71,'H':72,

     'I':73,'J':74,'K':75,'L':76,

     'M':77,'N':78,'O':79,'P':80,

     'Q':81,'R':82,'S':83,'T':84,

     'U':85,'V':86,'W':87,'X':88,

     'Y':89,'Z':90}
    )

print("Uppercase 'A' = ASCII code value",
      (ascii_uppercase_chars['A']))

print("Lowercase 'a' = ASCII code value",
      (ascii_lowercase_chars['a']))

print("Uppercase 'B' = ASCII code value",
      (ascii_uppercase_chars['B']))

print("Lowercase 'b' = ASCII code value",
      (ascii_lowercase_chars['b']))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These simple dictionary program examples below illustrates the ASCII code number
# characters and the ASCII code math operators. Type and execute/run the program
# examples below and see what happens.

ascii_number_chars = (
    {'0':48,'1':49,'2':50,'3':51,'4':52,

     '5':53,'6':54,'7':55,'8':56,'9':57}
    )

ascii_math_operator_chars = (
    {'+':43,'-':45,'*':42,'/':47}
    )

print("Number character '0' = ASCII code value",(ascii_number_chars['0']))

print("Number character '1' = ASCII code value",(ascii_number_chars['1']))

print("Number character '2' = ASCII code value",(ascii_number_chars['2']))

print("Number character '3' = ASCII code value",(ascii_number_chars['3']))

print("Math operator character '+' = ASCII code value",
      (ascii_math_operator_chars['+']))

print("Math operator character '-' = ASCII code value",
      (ascii_math_operator_chars['-']))

print("Math operator character '*' = ASCII code value",
      (ascii_math_operator_chars['*']))

print("Math operator character '/' = ASCII code value",
      (ascii_math_operator_chars['/']))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Generate computer numbers in binary base 2, hexadecimal base 16 and octal base
# 8. Type in ASCII codes and see what they look like. For example: 'print(bin(65))' is
# the ASCII code value for the capital letter 'A' in bibary base 2 as: '0b1000001'. Note:
# the '0b' is Python's prefix, which simply tells Python to work with binary base 2
# numbers.

# Convert any number into a binary base 2 number.

print(bin(255))

# Convert any number into a hexadecimal base 16 number.

print(hex(255))

# Convert any number into an octal base 8 number.

print(oct(255))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run each of these program examples below and see what
# happens.

comp_nums = int(input('Please type any number to see its binary base 2 number \
value: ').strip())

print(f'The number {comp_nums} = the binary base 2 number value: \
{bin(comp_nums)}.')

comp_nums = int(input('Please type any number to see its hexadecimal base 16 \
number value: ').strip())

print(f'The number {comp_nums} = the hexadecimal base 16 number value: \
{hex(comp_nums)}.')

comp_nums = int(input('Please type any number to see its octal base 8 \
number value: ').strip())

print(f'The number {comp_nums} = the octal base 8 number value: \
{oct(comp_nums)}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Play around with these George Boole Logic
# Python program examples to gain a much
# broader perspective of what logic truly means
# in computer programming. With Boolean Logic
# a computer can make decisions according to
# data input, via user input data. However, logical
# operators such as '==', '!=', '>', '<', '>=', '<=' work
# in conjunction with for-loops and while-loops.
# With the help of the 'if', 'elif' and 'else' statements
# this can be achieved with ease.

print(True and False)
print(False and True)
print(True and True)
print(False and False)

print(True and not False)
print(False and not True)
print(True and not True)
print(False and not False)

print(True or False)
print(False or True)
print(True or True)
print(False or False)

print(True or not False)
print(False or not True)
print(True or not True)
print(False or not False)

print(True is False)
print(False is True)
print(True is True)
print(False is False)

print(True is not False)
print(False is not True)
print(True is not True)
print(False is not False)

print(bool(1 and 0))
print(bool(0 and 1))
print(bool(1 and 1))
print(bool(0 and 0))

print(bool(1 and not 0))
print(bool(0 and not 1))
print(bool(1 and not 1))
print(bool(0 and not 0))

print(bool(1 or 0))
print(bool(0 or 1))
print(bool(1 or 1))
print(bool(0 or 0))

print(bool(1 or not 0))
print(bool(0 or not 1))
print(bool(1 or not 1))
print(bool(0 or not 0))

print(bool(1 == 1))
print(bool(1 != 1))

print(bool(1 > 1))
print(bool(1 < 1))
print(bool(1 >= 1))
print(bool(1 <= 1))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the logical 'is', 'and', 'or' and 'not'
# operators. Let's also create two, packed
# variables 'a' and 'b' then set them to 'True'
# and 'False' values. The logical operators
# 'is' and 'not' simply mean equals '==' and
# not equals '!='.

a,b = True,False

print(a is b) # False
print(b is a) # False

print(a and b) # False
print(b and a) # False

print(a or b) # True
print(b or a) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print(a is not b) # True
print(b is not a) # True

print(a and not b) # True
print(b and not a) # False

print(a or not b) # True
print(b or not a) # False
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the 'in' operator to check if a value is in
# variable 'a'. Use the 'in' operator in conjunction
# with the 'not' operator to tell if a value is not in
# the variable 'a'.

a = 1,2,3,4,5,6,7,8,9,10

print(1 in a) # True
print(10 in a) # True
print(11 in a) # False

print(1 not in a) # False
print(10 not in a) # False
print(11 not in a) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The 'all()' and 'any()' functions examples:

# Displays Boolean logic 'True' and 'False'
# values only.

num = 0,1

x = all(num)
print(x) # False

x = any(num)
print(x) # True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run each of these program
# examples below to see how the logical operators
# work in conjunction with for-loops.

for i in range(1,11):
    if i == 5:
        print(i,'is equal == to 5')
    elif i == 8:
        print(i,'is equal == to 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,11):
    if i != 5:
        print(i,'is not equal != to 5')
    elif i != 8:
        print(i,'is not equal != to 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,11):
    if i < 5:
        print(i,'is less < than 5')
    elif i > 8:
        print(i,'is greater > than 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,11):
    if i <= 5:
        print(i,'is less < than or equal = to 5')
    elif i >= 8:
        print(i,'is greater > than or equal = to 8')
    else:
        print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,5):
    if i == 2 and 3:
        print(i)
    else:
        print(i,'skip!')

for i in range(1,5):
    if i == 2 and 3:
        print(bool(i))
    else:
        print(i,'skip!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(1,5):
    if i == 2 or 3:
        print(i)
    else:
        print(i,'skip!')

for i in range(1,5):
    if i == 2 or 3:
        print(bool(i))
    else:
        print(i,'skip!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run each of these program
# examples below to see how the logical operators
# work in conjunction with while-loops.

i = 1
while i < 11:
    if i == 5:
        print(i,'is equal == to 5')
    elif i == 8:
        print(i,'is equal == to 8')
    else:
        print(i)
    i += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
i = 1
while i < 11:
    if i != 5:
        print(i,'is not equal != to 5')
    elif i != 8:
        print(i,'is not equal != to 8')
    else:
        print(i)
    i += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
i = 1
while i < 11:
    if i < 5:
        print(i,'is less < than 5')
    elif i > 8:
        print(i,'is greater > than 8')
    else:
        print(i)
    i += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
i = 1
while i < 11:
    if i <= 5:
        print(i,'is less < than or equal = to 5')
    elif i >= 8:
        print(i,'is greater > than or equal = to 8')
    else:
        print(i)
    i += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now combine all the logical operators
# within a for-loop, along with more 'elif' statements.

for i in range(1,21):
    if i == 5:
        print(i,'is equal == to 5')
    elif i != 8:
        print(i,'is not equal != to 8')
    elif i > 11:
        print(i,'is greater > than 11')
    elif i < 14:
        print(i,'is less < than 14')
    elif i >= 17:
        print(i,'is greater > than or equal = to 17')
    elif i <= 20:
        print(i,'is less < than or equal = to 20')
    else:
        pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now combine all the logical operators
# within a while-loop, along with more 'elif'
# statements.

i = 1
while i < 21:
    if i == 5:
        print(i,'is equal == to 5')
    elif i != 8:
        print(i,'is not equal != to 8')
    elif i > 11:
        print(i,'is greater > than 11')
    elif i < 14:
        print(i,'is less < than 14')
    elif i >= 17:
        print(i,'is greater > than or equal = to 17')
    elif i <= 20:
        print(i,'is less < than or equal = to 20')
    else:
        pass
    i += 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Conditionals and Logical Operators: (<) (>) (<=) (>=) (==) (!=)

# Conditionals change the outcome of a program's execution run, depending
# on what the program is doing at the time. The conditionals in Python are the
# 'if:' statement, 'elif:' statement and the 'else:' statement, along with the 'True:'
# and 'False:' statements. Conditionals are mainly used in conjunction with 'input'
# statements and conditional while-loops. However, Logical operators are also used
# to test whether a condition is less than (<), greater than (>), less than (<=) or equal
# to, greater than (>=) or equal to, equals (==) equals and not (!=) equal to. For example,
# 5 is greater (>) than 4 and 4 is less (<) than 5. Here are a few examples of logical
# operators, which test integer values against other integer values within 'print'
# statements. These 'print' statement illustration examples below will either display
# on the screen output as "True" or "False", depending on the outcome of the results.

# print(4 < 5) True: 4 is less than 5
# print(4 > 5) False: 4 is not greater than 5
# print(4 <= 5) True: 4 is less than or equal to 5
# print(4 >= 5) False: 4 is not greater than or equal to 5
# print(4 == 5) False: 4 does not equal 5
# print(4 != 5) True: 4 does not equal 5

print(4 < 5)

# Screen output: True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run these 'print' statement program examples, using the (f')
# format implementer.

# The 'int' statement is for integer values only.

num = int(input('Type in a number and I will condition the result against 5 as either \
"true" or false" ').strip())

print(f'{num < 5}')
print(f'{num > 5}')
print(f'{num <= 5}')
print(f'{num >= 5}')
print(f'{num == 5}')
print(f'{num != 5}')

# Boolean Logic:

# "IF" "ELIF" "ELSE" "TRUE" "FALSE" "AND" "OR" "NOT"

# There once was a man, named 'George Boole' who was a famous mathematician. He invented
# these conditionals called Boolean Logic, which indirectly brought about the computer age we
# now live. The conditionals of George Boole are as follows.

# These conditionals are: 'IF', 'ELSE', 'TRUE', 'FALSE', 'AND', 'OR' 'NOT'

# In computer terminology, these conditionals are called "Boolean Logic". Boolean Logic is simply
# all about the concept of decision making laws, meaning if something is true, then it is not false.
# Likewise, if something is false, then it is not true.

# When it comes to program development, sometimes logical operators aren't enough alone to do
# the job. In most cases, other conditionals are needed to help the logical operators do the job. With
# the 'if:', 'elif:', 'else', 'true', 'false', 'and', 'or' and 'not' conditionals, the logical operators can do the
# job as they were designed for doing, which are to test values against other values and comparing
# data against user input data.

# Using simple 'print' statements, you can do simple True and False tests to help you
# determine the outcome of a conditional against another conditional, such as True
# and False conditionals. For example:

print(True and True)
print(False and False)
print(True and False)
print(False and True)

print(True or True)
print(False or False)
print(True or False)
print(False or True)

print(True and not True)
print(False and not False)
print(True and not False)
print(False and not True)

print(True or not True)
print(False or not False)
print(True or not False)
print(False or not True)

print(True is not True)
print(False is not False)
print(True is not False)
print(False is not True)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use operators to check to see if a value is True or False.

print(True == True)
print(False == False)
print(True != False)
print(False != True)
print(True >= False)
print(True <= False)

# Here is a prime example of how these conditionals work in conjunction with the
# logical operators. In this program example, the conditionals 'if:' and 'elif:' are
# implement along with the logical operators. The user is asked to type in a number, if
# the number is equal equals: == 5, the first conditional 'if:' statement is executed
# "print(f'True! {num} equals equals 5.')". If the number is less than 5, the first 'elif:'
# statement is executed "print(f'True! {num} is less than 5.')". If the number is greater
# than 5, the second 'elif:' statement is executed "print(f'False! {num} is not greater
# than 5.')". If the number is less than or equal to 5, the third 'elif:' statement is
# executed "print(f'True! {num} is less than or equal to 5.')". If the number is greater
# than or equal to 5, the last 'elif:' statement is executed "print(f'False! {num} is is not
# greater than or equal to 5.')".

# Note: Python executes/runs programs starting from the top, downward. Be very
# careful on how you place statements. Some statements cannot execute right, even if
# they work. This is simply because of the order that Python executes/runs its
# program statements in the background.

# Type and execute/run this program example below and see what happens.

# The 'int' statement is for integer values only.

num = int(input('Type in a number and I will condition the result against 5 as either \
"true" or false" ').strip())

if num == 5:
    print(f'True! {num} equals equals 5.')

elif num < 5:
    print(f'True! {num} is less than 5.')

elif num > 5:
    print(f'False! {num} is not greater than 5.')

elif num <= 5:
    print(f'True! {num} is less than or equal to 5.')

elif num >= 5:
    print(f'False! {num} is is not greater than or equal to 5.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# In this program example, the conditional 'else:' statement is executed only when the
# value 5 equals itself. Type and execute/run the program below and see what
# happens.

# The 'int' statement is for integer values only.

integer = int(input("Please enter an integer less than 5 or greater than 5: ").strip())

if integer < 5:
    print(f'{integer} is less then 5')

elif integer > 5:
    print(f'{integer} is greater than 5')

else:
    if integer == 5:
        print(f'True! {integer} equals equals 5.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run this program example and change the value 'num = 5' to
# different values, such as 'num = 9', 'num = -7'.....

num = 6

if num < 5:
    print(f'{num} is less than 5')

elif num > 5:
    print(f'{num} is greater than 5')

else:
    if num == 5:
        print(f'{num} equals equals 5.')

# In this program example, the conditional 'else:' statement is executed only when the
# value 5 equals itself. Type and execute/run the program below and see what
# happens.

# The 'int' statement is for integer values only.

integer = int(input("Please enter an integer less than 5 or greater than 5: ").strip())

if integer < 5:
    print(f'{integer} is less then 5')

elif integer > 5:
    print(f'{integer} is greater than 5')

else:
    if integer == 5:
        print(f'True! {integer} equals equals 5.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run this program example
# and see how the while-loop only breaks when
# one of the two 'break' statements is executed.
# If none of them gets executed, the while-loop
# keeps on iterating. This program example is
# another great example of how the conditional
# 'if:' and 'elif:' statements work in conjunction
# with the logical operators.

while True:
    try:
        asterisks = int(input(f'How many asterisks would you like? ').strip())
        if asterisks > 1:
            print(f'\n{asterisks} asterisks: [',' * '*asterisks,f']\n\nI gave you \
{asterisks} asterisks!\n\nI hope you enjoy your {asterisks} asterisks...')
            break

        elif asterisks == 1:
            print(f'\n{asterisks} asterisk: [','*'*asterisks,f']\n\nI gave you \
{asterisks} asterisk!\n\nI hope you enjoy your \'One\' \
and \'Only\', single asterisk...')
            break

        elif asterisks == 0:
            print('\nSorry Hero! Zero doesn\'t count.\n')
    except ValueError:
        print('\nNumbers only please!\n')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This conditional while-loop example compares
# a random number against user input data. If
# the user picks the right number by luck alone,
# the while-loop will break out and the program
# ends. If the user picks the wrong number, the
# less (<) than or greater (>) than 'random_num'
# variable gets conditioned and the while-loop
# keeps on iterating until the right number is
# picked, via user input data.

# Note: Python executes/runs programs starting
# from the top, downward. Be very careful on how
# you place statements. Some statements cannot
# execute right, even if they work. This is simply
# because of the order that Python executes/runs
# its program statements.

# Note: The 'import random' module must be imported
# first.

import random

random_num = random.randint(1,10)

while True:
    try:
        pick_num = int(input('\nWhat number am I thinking \
of? Hint! It\'s between 1 and 10: ').strip())

        if pick_num < random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num > random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations! You won. "{random_num}" \
was the number I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This very same program example as above
# works exactly the same way, but with one
# major difference; the while loop will only iterate
# three times. If the user picks the right number,
# the while loop breaks. If the user doesn't pick
# the right number after three times, the 'else'
# statement executes and says 'Sorry! You lost.',
# which ends the program.

# Note: the 'import random' module must be imported
# first.

import random

random_num = random.randint(1,10)

i=0

while i < 3:
    try:
        pick_num = int(input('\nWhat number am I thinking of? \
Hint! It\'s between 1 and 10: ').strip())

        i += 1

        if pick_num < random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num > random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations. You won! "{random_num}" \
was the number I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')

else:
    print('\nSorry. You lost!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Once again, this is the very same program
# example as above before. However, this time
# the loop iterates in reverse instead of forward
# and the user is shown how many guesses they
# have left before they win or lose.

# Note: the 'import random' module must be
# imported first.

import random

random_num = random.randint(1,10)

i = 3

while i > 0:
    try:
        pick_num = int(input(f'\nWhat number am I thinking of? \
Hint! It\'s between 1 and 10:\n\nYou have {i} gesses left. ').strip())

        i -= 1

        if pick_num < random_num:
            print('\nThe number I\'m thinking of is too low!')

        elif pick_num > random_num:
            print('\nThe number I\'m thinking of is too high!')

        elif pick_num == random_num:
            print(f'\nCongratulations. You won! "{random_num}" \
was the number I was thinking of.')
            break

    except ValueError:
        print('\nYou must type integers only please!')

else:
    print('\nSorry. You lost!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type and execute/run The George Boole Game
# program example to get a better understanding
# of how Boolean Logic works and why it works.
# Type different "True" and "False" combinations
# and see what Gearoge Boole does. Press 'Q' to
# quit playing.

print('\nThe George Boole Game\n')

print('George loves to play "True" or "False",\nbut \
he needs your help to play it.')

print('\nPress "Q" to quit!')

while True:
    Boole1 = input('\nType "true" or "false" for the first value. ').strip()
    if Boole1 == 'q':
        print('Thanks for playing!')
        break

    print(f'\nYou chose "{Boole1.title()}" for your first value.\n')
    Boole2 = input('\nType "True" or "False" for the second value. ').strip()

    if Boole2 == 'q':
        print('Thanks for playing!')
        break

    print(f'You chose "{Boole2.title()}" for your second value.\n')

    if Boole1 == 'true' and  Boole2 == 'true':
        print(f' "AND" is true because Boole1 is "{Boole1.title()}" \
and Bool2 is "{Boole2.title()}".\n')

    elif Boole1 == 'false' and Boole2 == 'false':
        print(f' "AND" is true because Boole1 is "{Boole1.title()}" and \
Boole2 is "{Boole2.title()}".\n')

    elif Boole1 == 'true' or Boole2 == 'true':
        print(f' "OR" is true because Boole1 is "{Boole1.title()}" and \
Boole2 is "{Boole2.title()}".\n')

    elif Boole1 == 'false' or Boole2 == 'false':
        print(f' "OR" is true because Boole1 is "{Boole1.title()}" and \
Boole2 is "{Boole2.title()}".\n')

    else:
        print('Type the right vales please!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. Execute/run
# the Python program example below to view your created list of values,
# along with their variable name. Simply highlight all the blue text output,
# and then copy then paste that blue Python Idle text output back into your
# Python Idle editor. Next, execute/run the pasted Python code and watch
# it create a list of values, as if you had created the actual Python list and
# layout yourself.

m = 'make'

user_input_data_list_values = [ ]

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "make" to create and view your user
input data list values:''')

while True:
    while True:
        user_input_value = input(f'\nuser input data list value = ').lower().strip()

        user_input_data_list_values.append(user_input_value)

        user_input_data_list_values.sort()

        if user_input_value == m:
            user_input_data_list_values.remove(user_input_value)
            break

    if len(user_input_data_list_values) < 2:
        print(f'\nYour user input data list must be over two values long.')

    else:
        print(
            f'''\nuser_input_data_list_values = {user_input_data_list_values}

print('You have {len(user_input_data_list_values)} user input data list values:')

print(user_input_data_list_values)''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. Execute/run
# the Python program example below to view your created list of values,
# along with their variable name. Simply highlight all the blue text output,
# and then copy then paste that blue Python Idle text output back into your
# Python Idle editor. Next, execute/run the pasted Python code and watch
# it create a list of values, as if you had created the actual Python list and
# layout yourself.

m = 'make'

user_input_data_list_values = [ ]

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "make" to create and view your user
input data list values:''')

while True:
    while True:
        user_input_value = input(f'\nuser input data list value = ').lower().strip()

        user_input_data_list_values.append(user_input_value)

        convert_list = set(user_input_data_list_values)

        reconvert_list = list(convert_list)

        reconvert_list.sort()

        if user_input_value == m:
                reconvert_list.remove(user_input_value)
                break

    if len(reconvert_list) < 2:
        print(f'''\nYour user input data list must be over two values long.
No duplicate values allowed.''')

    else:
        print(
            f'''\nuser_input_data_list_values = {reconvert_list}

print('You have {len(reconvert_list)} user input data list values:')

print(reconvert_list)''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. However,
# this time we are forced type text letters only. Execute/run the Python
# program example below to view your created list of values, along with
# their variable name. Simply highlight all the blue text output, and then
# copy then paste that blue Python Idle text output back into your Python
# Idle editor. Next, execute/run the pasted Python code and watch it create
# a list of values, as if you had created the actual Python list and layout
# yourself.

m = 'make'

user_input_data_list_values = [ ]

text_error_message = '\ntext letters only please:'

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "make" to create and view your user
input data list values:''')

while True:
    while True:
        user_input_value = input(f'\nuser input data list value = ').lower().strip()

        user_input_data_list_values.append(user_input_value)

        user_input_data_list_values.sort()

        if user_input_value < str([user_input_data_list_values]):
            user_input_data_list_values.remove(user_input_value)
            print(text_error_message)

        elif user_input_value == m:
                user_input_data_list_values.remove(user_input_value)
                break

    if len(user_input_data_list_values) < 2:
        print(f'\nYour user input data list must be over two values long.')

    else:
        print(
            f'''\nuser_input_data_list_values = {user_input_data_list_values}

print('You have {len(user_input_data_list_values)} user input data list values:')

print(user_input_data_list_values)''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. However,
# this time we are forced type text numbers only. Execute/run the Python
# program example below to view your created list of values, along with
# their variable name. Simply highlight all the blue text output, and then
# copy then paste that blue Python Idle text output back into your Python
# Idle editor. Next, execute/run the pasted Python code and watch it create
# a list of values, as if you had created the actual Python list and layout
# yourself.

m = 9999

user_input_data_list_values = [ ]

text_error_message = '\ntext numbers only please:'

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "9999" to create and view your user
input data list values:''')

while True:
    while True:
        try:
            user_input_value = int(input(f'\nuser input data list value = ').lower().strip())

            user_input_data_list_values.append(user_input_value)

            user_input_data_list_values.sort()

            if user_input_value == m:
                user_input_data_list_values.remove(user_input_value)
                break

        except ValueError:
            print(text_error_message)

    if len(user_input_data_list_values) < 2:
        print(f'\nYour user input data list must be over two values long.')

    else:
        print(
            f'''\nuser_input_data_list_values = {user_input_data_list_values}

print('You have {len(user_input_data_list_values)} user input data list values:')

print(user_input_data_list_values)''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a list of values for us.
# You must type two or more values to start creating your list. However,
# this time we are forced type text numbers only. Execute/run the Python
# program example below to view your created list of values, along with
# their variable name. Simply highlight all the blue text output, and then
# copy then paste that blue Python Idle text output back into your Python
# Idle editor. Next, execute/run the pasted Python code and watch it create
# a list of values, as if you had created the actual Python list and layout
# yourself.

m = 9999

user_input_data_list_values = [ ]

text_error_message = '\ntext numbers only please:'

print('''
Let me help you create a sorted list of values with Python.
Please type each data list value, one at a time, followed by
the "Enter" key. Type "9999" to create and view your user
input data list values:''')

while True:
    while True:
        try:
            user_input_value = int(input(f'\nuser input data list value = ').lower().strip())

            user_input_data_list_values.append(user_input_value)

            convert_list = set(user_input_data_list_values)

            reconvert_list = list(convert_list)

            reconvert_list.sort()

            if user_input_value == m:
                reconvert_list.remove(user_input_value)
                break

        except ValueError:
            print(text_error_message)

    if len(reconvert_list) < 2:
        print(f'''\nYour user input data list must be over two values long.
No duplicate values allowed.''')

    else:
        print(
            f'''\nuser_input_data_list_values = {reconvert_list}

print('You have {len(reconvert_list)} user input data list values:')

print(reconvert_list)''')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is so neat! I just made this up to see if it would work.
# Watch this Python program execution/run example:

# Change one of the values, then re-execute/run the Python program.

logical_list_values = ['Value','Value','Value','Value']

user_message1 = f'''All values are the same.
\n{logical_list_values[0]} {logical_list_values[1]} \
{logical_list_values[2]} {logical_list_values[3]}:
\nYou have {len(logical_list_values)} logical list values.'''

user_message2 = f'''All values are NOT the same.
\n{logical_list_values[0]} {logical_list_values[1]} \
{logical_list_values[2]} {logical_list_values[3]}:
\nYou have {len(logical_list_values)} logical list values.'''

if logical_list_values[0] is logical_list_values[1]\
   is logical_list_values[2] is logical_list_values[3]:
    print(user_message1)

else:
    print(user_message2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Automated Dictionary Python program examples:

# Let's use the Python Idle that will help us create a dictionary for us.
# You must type four dictionary keys and values to create your dictionary.
# Execute/run the Python program example below to view your created
# dictionary, along with its variable name. Simply highlight all the blue text
# output, and then copy then paste that blue Python Idle text output back
# into your Python Idle editor. Next, execute/run the pasted Python code
# and watch it create a dictionary, as if you had created the actual Python
# dictionary and layout yourself.

user_input_data_dictionary = { }

keys = user_input_data_dictionary.keys()

values = user_input_data_dictionary.values()

keys_values = 0

print('''
Let me help you create a dictionary with Python. Please
type each data dictionary key and value, one at a time,
followed by the "Enter" key:''')

while keys_values < 4:
    user_input_key = input(f'\nPlease type dictionary key{keys_values+1}: ').strip()

    user_input_value = input(f'Please type dictionary value{keys_values+1}: ').strip()

    user_input_data_dictionary.update({user_input_key:user_input_value})

    keys_values += 1

print(f'\nuser_input_data_dictionary = {user_input_data_dictionary}')

print(f'\nHere are your {keys} and {values}:')

print(f'\nYou have {len(keys)} keys and {len(values)} values:')

print(f"\n{user_input_data_dictionary.get('place key here')}")

print(f"\n{user_input_data_dictionary.get('place key here','Key not found:')}")  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a dictionary for us.
# You must type a number of dictionary keys and values to create your
# dictionary. Execute/run the Python program example below to view
# your created dictionary, along with its variable name. Simply highlight
# all the blue text output, and then copy then paste that blue Python Idle
# text output back into your Python Idle editor. Next, execute/run the
# pasted Python code and watch it create a dictionary, as if you had
# created the actual Python dictionary and layout yourself.

user_input_data_dictionary = { }

keys = user_input_data_dictionary.keys()

values = user_input_data_dictionary.values()

keys_values = 0

print('''
Let me help you create a dictionary with Python. Please
type each data dictionary key and value, one at a time,
followed by the "Enter" key:''')

while True:
    try:
        user_input_dectionary_length = int(input(
            '\nHow many keys and values would you like to create?: ').strip())
    except ValueError:
        print('\nNumbers only please: ')
        continue
    break

while keys_values < user_input_dectionary_length:
    user_input_key = input(f'\nPlease type dictionary key{keys_values+1}: ').strip()

    user_input_value = input(f'Please type dictionary value{keys_values+1}: ').strip()

    user_input_data_dictionary.update({user_input_key:user_input_value})

    keys_values += 1

print(f'\nuser_input_data_dictionary = {user_input_data_dictionary}')

print(f'\nHere are your {keys} and {values}:')

print(f'\nYou have {len(keys)} keys and {len(values)} values:')

print(f"\n{user_input_data_dictionary.get('place key here')}")

print(f"\n{user_input_data_dictionary.get('place key here','Key not found:')}")  # optional
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a dictionary for us.
# You must type a number of dictionary keys and values to create your
# dictionary. Execute/run the Python program example below to view
# your created dictionary, along with its variable name. Simply highlight
# all the blue text output, and then copy then paste that blue Python Idle
# text output back into your Python Idle editor. Next, execute/run the
# pasted Python code and watch it create a dictionary, as if you had
# created the actual Python dictionary and layout yourself.

user_input_data_dictionary = { }

keys = user_input_data_dictionary.keys()

values = user_input_data_dictionary.values()

keys_values = 0

print('''
Let me help you create a dictionary with Python. Please
type each data dictionary key and value, one at a time,
followed by the "Enter" key:''')

while True:
    try:
        user_input_dectionary_length = int(input(
            '\nHow many keys and values would you like to create?: ').strip())
        if user_input_dectionary_length < 2:
            print(f'\nYour dictionary must be at least two keys and two values long.')
            continue
        else:
            break
    except ValueError:
        print('\nNumbers only please: ')
        continue
    break

while keys_values < user_input_dectionary_length:
    user_input_key = input(f'\nPlease type dictionary key{keys_values+1}: ').strip()

    user_input_value = input(f'Please type dictionary value{keys_values+1}: ').strip()

    user_input_data_dictionary.update({user_input_key:user_input_value})

    keys_values += 1

print(f'\nuser_input_data_dictionary = {user_input_data_dictionary}')

print(f'\nHere are your {keys} and {values}:')

print(f'\nYou have {len(keys)} keys and {len(values)} values:')

print(f"\n{user_input_data_dictionary.get('place key here')}")

print(f"\n{user_input_data_dictionary.get('place key here','Key not found:')}")  # optional

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Like always, I research when I want to learn something new, or new
# to me. Since the years I've played around with Python programming,
# I never ever explored list comprehension at all. This is like killing two
# birds with one stone's throw. List comprehension shortens for loops
# down when looping through a list, using a for loop right inside the
# list [ ] brackets.

# Create a list of values using list comprehension.

text_list_values = ['dog','cat','bird','fish','turtle']

text_list_values.sort()

values = [value for value in text_list_values]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a list of values using list comprehension. Invoke the 'if' and
# 'else' statements that override all values, except the value 'bird'.

text_list_values = ['dog','cat','bird','fish','turtle']

text_list_values.sort()

values = [value if value == 'bird' else 'frog' for value in text_list_values]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a list of values using list comprehension.

num_list_values = [6,2,5,1,3,4,8,7,10,9]

num_list_values.sort()

values = [value for value in num_list_values]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a list of values using list comprehension. Invoke the 'if' and
# 'else' statements that override all values, except the value '9'.

num_list_values = [6,2,5,1,3,4,8,7,10,9]

num_list_values.sort()

values = [value if value == 9 else 100 for value in num_list_values]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create an integer number line using list comprehension.

values = [value for value in range(-10,+11)]

print(values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the Python Idle that will help us create a multi dimensional
# integer list for us with this Python program example: Execute/run
# the Python program example below to view your created list
# of values, along with their variable name. Simply highlight all
# the blue text output, and then copy then paste that blue Python
# Idle text output back into your Python Idle editor. Next, execute/run
# the pasted Python code and watch it create a list of values, as
# if you had created the actual Python list and layout yourself.

auto_multi_dimensional_integer_list_creator = [ ]

print('auto_multi_dimensional_integer_list_creator = [')

for i in range(1,11):
    auto_multi_dimensional_integer_list_creator.append(i)
    print(f'{auto_multi_dimensional_integer_list_creator},')

print(']')

print('\nprint(auto_multi_dimensional_integer_list_creator[9][9])')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bonus Python program example: Make this Python program example
# ask the user their first name, last name and their age. If the user types
# incorrect data information, the program will prompt the user to type
# the correct data information allotted. Also if the user's age is less
# than nineteen years old, the program will give the user a sorry message
# that they are not old enough to drink yet.

user_first_name = '\nWhat is your first name please?: '

user_last_name = '\nWhat is your last name please?: '

user_age = 'How old are you?: '

age = 19

age_undefine = f'\nSorry! No such age. Please try again:'

old_enough = 'You are old enough to drink. Get SMASHED!'

not_old_enough = 'You are not old enough to drink yet.'

text_error_message = '\ntext letters only please:'

text_value_error_message = '\ntext numbers only please:'

text_length_message1 = '\nYour first name must be over two characters long.'

text_length_message2 = '\nYour first name must be under ten characters long.'

text_length_message3 = '\nYour last name must be over two characters long.'

text_length_message4 = '\nYour last name must be under ten characters long.'

while True:
    user_input_first_name = input(user_first_name).lower().strip()

    if user_input_first_name < str([user_input_first_name]):
        print(text_error_message)

    elif len(user_input_first_name) < 3:
        print(text_length_message1)

    elif len(user_input_first_name) > 10:
        print(text_length_message2)

    else:
        break

while True:
    user_input_last_name = input(user_last_name).lower().strip()

    if user_input_last_name < str([user_input_last_name]):
        print(text_error_message)

    elif len(user_input_last_name) < 3:
        print(text_length_message3)

    elif len(user_input_last_name) > 10:
        print(text_length_message4)

    else:
        break

while True:
    try:
        user_input_age = int(input(f'\nNice to meet you {user_input_first_name.title()} \
{user_input_last_name.title()}. {user_age}').strip())

        if user_input_age == 18:
            print(f'\nSorry {user_input_first_name.title()}. {not_old_enough} Come back \
in {age-user_input_age} year from now.')
            break

        elif user_input_age == 0:
            print(age_undefine)

        elif user_input_age < age:
            print(f'\nSorry {user_input_first_name.title()}. {not_old_enough} Come back \
in {age-user_input_age} years from now.')
            break

        else:
            print(f'\nCongrats {user_input_first_name.title()}. {old_enough}')
            break

    except ValueError:
        print(text_value_error_message)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Fibonacci Natural Number Sequence Python program example.

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

import os,time,winsound

os.system(f'title Fibonacci Natural Number Sequence')

text_colours = (
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

text_words = (
    f'{text_colours[1]}Fibonacci Natural Number Sequence in Action...',

    f'\n\n{text_colours[2]}Fibonacci Natural Number Sequence example: \
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610...]',

    f'\n\n{text_colours[5]}Fibonacci Natural Numbers go on forever!',
    f'\n\nFibonacci Natural Numbers can only be found in \
nature, such as plants and animals...'
    )

sounds = ('Ring03','Speech Off')

def Fib_Num():
    winsound.PlaySound(sounds[0],winsound.SND_ASYNC)

    for i in range(25):
        print('\n',' '*i,text_words[0])
        time.sleep(.25)
        os.system('cls')

    num1 = 0
    num2 = 1
    fib = [num1,num2]

    while True:
        num3 = num1+num2
        fib.append(num3)
        num1 = num2
        num2 = num3
        clock = (time.asctime())

        print('\n',' '*25,text_words[0],text_words[1],text_words[2])

        print(f'\nFibonacci Natural Number Sequence: {text_colours[2]}\
{num1} {text_colours[5]}+ {text_colours[2]}{num2}{text_colours[5]} = \
({text_colours[0]}{num1+num3}{text_colours[5]}){text_colours[5]}\n\n\
Fibonacci Natural Numbers: "{text_colours[0]}{num1+num3:,}{text_colours[5]}\
"\n\n{text_colours[0]}Date & Time:\n\n{clock}')

        winsound.PlaySound(sounds[1],winsound.SND_ALIAS)
        os.system('cls')

Fib_Num()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is for advanced Python programmers, who want something a little bit saltier.
# Create this Fibonary Bits In Action! Python program using a single print() function.
# Use the backslash '\' to create line breaks within the print() function.

# Type and execute/run this Python program example below and see what happens.

# Note: after you save your file, you must double click this file to view it's cool coloured
# text and layout.

import os;os.system('title fibonary bits in action! 3'.title())
from time import sleep as delay

red = '\x1b[31m'
green = '\x1b[32m'
blue = '\x1b[34m'
yellow = '\x1b[33m'
purple = '\x1b[35m'
white = '\x1b[37m'

title_text = f'fibonary bits in action! 3'.title(),'fibonacci natural number sequence'.title()
text = (' binary digits: ',' octal digits: ',' hexadecimal digits: ',' decimal digits:',
      ' fibonacci digits: '.title())

lb = '\n';lbb = '\n\n';elb = ' =\n';eq = ' = ';sp = ' '

num1 = 0;num2 = 1
fib = [num1,num2]

pause = 1

while True:
    os.system('cls')
    num3 = num1+num2
    fib.append(num3)
    num1 = num2;num2 = num3

    b = f'{num3:b}';o = f'{num3:o}'
    x = f'{num3:X}';d = f'{num3:d}'

# old string formatted print() function example:

    print('{}{}{}{}{}{}{}{}{}{}{}'.format(
        white+lb+sp*16+title_text[0]+lb+red+lb+sp*4,
        len(b),green+text[0].title()+yellow+b+blue+elb+sp*4+
        green+red,len(o),green,text[1].title()+yellow+o+blue+
        elb+sp*4+green+red,len(x),green+text[2].title()+yellow+
        x,blue+eq+green+lb+sp*4+red,len(d),green+text[3].title()+
        blue+eq+yellow+d+lbb+white+sp*11+title_text[1]+lbb+green+
        sp*3+text[4]+yellow+f'{num3:,d}'))
    delay(pause)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# input Fibonacci Number Sequence example, using a set{}

num1,num2 = 0,1

fib = {num1,num2}

words = (
    'is in the Fibonacci Sequence.',
    'is not in the Fibonacci Sequence.',
    'Please enter a correct Fibonacci Sequence Number: ',
    'Sorry! Numbers only.',
    'Memory Error!'
    )

try:
    x = int(input(words[2]).strip())

    for i in range(x):
        fib_num = num1+num2
        fib.add(fib_num)
        num1 = num2
        num2 = fib_num

    if x in fib:
        print(x,words[0])

    elif x not in fib:
        print(x,words[1])

except ValueError:
    print(words[3])

except MemoryError:
    print(words[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This little flip flop game is a great example of how the conditional while-loop works.
# The 'else' statement executes/runs when the user types the wrong keys, and the
# while-loop iterates/repeats over again while ignoring the 'break' statement.

print('\nWelcome to the Flip Flop Game')

print('\nPlease type the words "flip" or "flop", then press (ENTER)')

print('\nWhen you get bored, press (ENTER) to quit playing Flip Flop')

while True:
    flip_flop = input('\nFlip? or Flop? ').strip()

    if flip_flop == 'flip':
        print('\nFlop')

    elif flip_flop == 'flop':
        print('\nFlip')

    elif flip_flop == '':
        print('\nThanks for playing Flip! Flop!')
        break

    else:
        print('\nYou can\'t cheat now! Do you flip? or do you flop?')

input('\nEnd of program. Press Enter to quit.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn some deep Python programming skills with define functions
# and class objects. These Python programming examples are not for the
# beginner/novice Python programmer. To those, who are starting into
# computer programming, do not start off with these Python program
# examples. You will quickly get lost trying to understand such examples
# as these. These Python programming examples are for advanced
# programmers only. However, if you are brave enough to try these Python
# programming examples, I say. Why not!! But you might become lost
# and quickly confused if you are just starting fresh into computer
# programming at large...

# Most of these Python programming examples will go into both robots.
# I have a Robomaster S1 robot and a brand new Robomaster EP Core
# robot. Both are from dji. The EP Core robot is coming in the not too
# distant future from now. So be looking out for it.

# Created by Joseph C. Richardson, GitHub.com

# Create a simple define function along with the print() function.

def define_function_example_one():
    print('This is a basic define function() example.')

define_function_example_one()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function with one parameter variable along with
# the print() function.

def define_function_example_two(argument):
    print('This is a basic define function() with an argument example.')

define_function_example_two('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function with two parameter variables along with
# the print() function.

def define_function_example_three(argument1,argument2):
    print('This is a basic define function() with two arguments example.')

define_function_example_three('argument placeholder value','argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When you are not sure of how many parameter variables to use
# within a define function, you can invoke the *args prefix to satisfy
# any number of argument placeholder values without the worry of
# how many are needed to satisfy the parameter variables.

def define_function_Class_example_four(*args):
    print('This is a basic define function() with an *args example.')

define_function_Class_example_four('argument placeholder value','argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that returns a value, via invoking one
# parameter variable, along with one argument placeholder value.

def define_function_Class_example_five(argument):
    return 'I am the actual returned value.'

print(define_function_Class_example_five(
    'This is a return define function() with an argument placeholder value.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that returns two values, via invoking two
# parameter variables, along with two argument placeholder values.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When you are not sure of how many parameter variables to use
# within a return define function, you can invoke the *args prefix to
# satisfy any number of argument placeholder values without the
# worry of how many are needed to satisfy the parameter variables.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what **kwargs are all about. The word 'kwargs' simply means
# the words 'keyword arguments' for short. Two asterisks ** are used for
# **kwargs. Use **kwargs when you don't know how many keyword argument
# variables you want within your define function parameters. Note: you do
# not need to call the word '**kwargs' as kwargs. However, you will need to
# invoke two asterisks ** to make **kwargs work. Programmers know the word
# as **kwargs by standard definition, but you can use your own words.

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

# As shown in the define function() example above, how we
# needed the exact number of keyword argument values to the
# exact number of keyword argument variables. However, with
# **kwargs you no longer have to worry about how many keyword
# argument values you will need to satisfy the number of keyword
# argument variables within the define function parameters.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# define functions can also return keyword arguments. In this
# first example, the exact number of keyword arguments are
# required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(kwarg1,kwarg2):
    return 'I am the actual returned value one.','I am the actual returned value two.',

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))

# define functions can also return keyword arguments. In this
# second example, the exact number of keyword arguments are
# not required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(**kwargs):
    return 'I am the actual returned value.'

print(keyword_arguments(kwarg1='placeholder value 1',kwarg2='placeholder value 2'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# define functions can also return keyword arguments. In this
# first example, the exact number of keyword arguments are
# required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(num1,num2):
    return num1*num2

print(keyword_arguments(num1=2,num2=4))

# define functions can also return keyword arguments. In this
# second example, the exact number of keyword arguments are
# not required to satisfy the exact number of keyword argument
# placeholder values within the print() function.

def keyword_arguments(**kwargs):
    return 2*4

print(keyword_arguments(num1='placeholder value 1',num2='placeholder value 2'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do a quick recap about *args and **kwargs syntex only,
# so we can fully understand in a simpler way of what *args and
# **kwargs are all about.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some define functions that act like subroutines.

# Since there are no line numbers in Python, also means that we
# cannot create any such 'go to', or 'go sub' commands at all with
# Python. So how can we create subroutines with Python?. How
# can we create subroutines without making them jump to line
# numbers, like we did in the old days? Well the answer is quite
# simple. Let's use define functions() with a while loop to create
# our subroutine examples, using define functions() only.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Global Variables in Python

# What are 'global variables'? Global variables are used within
# define functions() when you want to call a variable outside the
# actual define function(), you need the prefix 'global' to be able
# to call a variable outside the actual define function() itself. For
# example here is what calling a variable, using the prefix 'global'
# does.

def global_variable():
    global a
    a = 'global variables work outside their define functions()'

global_variable()

print(a)

# If you try to call a variable outside a define function() with no
# 'global' prefix attached to it, you will get an error such as this:

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

# Simply create a variable outside the define function and then
# call it in from outside it. Let's do more global variables to get
# the hang of things with a group of them.

def global_variables():
    global a
    global b
    global c

    a = 'global variable (a) works outside its define function()'
    b = 'global variable (b) works outside its define function()'
    c = 'global variable (c) works outside its define function()'

global_variables()

print(a)

# Here is one thing you should avoid doing. If you call an outside
# variable with the same name as this example below shows, you
# won't get the desired output you want. If you want outside variables
# outside of global variables, you must give them different names so
# they can know who is who.

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

# Now that we used a different name for the outside variable, the
# global variables and the outside variable will know who is who,
# when being called upon. Note: you can also use an uppercase 'A'
# for the outside variable; computers are case sensitive: 'a' and 'A'
# are not the same to a computer. Therefore, the computer treats
# the variables as totally different names. So please keep this in
# mind at all times.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some ways to create return define functions in
# Python. Please note: there are no comments about these
# Python program experiments below. This is how I do most
# of my computer programming experiments in Python. I
# don't always place comments into programs I create, until
# I'm happy with my computer programming experiments
# first. As for right now, I'm just too darn lazy to write a
# bunch of comments about what these Python program
# experiments do. I'll leave that all up to YOU to tinker with
# these Python program experiments for yourself. Because,
# this is what computer programming is truly all about; it's
# all about trial and error and some extreme insanity...

def return_function_name_values():

    return 'Rob','Bob','Terry','Mary'

try:

    print(return_function_name_values()[0])

    print(return_function_name_values()[1])

    print(return_function_name_values()[2])

    print(return_function_name_values()[3])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_name_values(name1,name2,name3,name4):

    return 'Rob','Bob','Tom','Terry','Mary'

try:

    print(return_function_name_values(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[3])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_name_values(name1,name2,name3,name4):

    return 'Rob','Bob','Terry','Mary'

tuple_var = return_function_name_values(
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value')

try:

    print(f'Hi {tuple_var[3]}. How are you?')

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_name_values(name1,name2,name3,name4):

    return 'Rob','Bob','Terry','Mary'

tuple_var = return_function_name_values(
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value')

for i in tuple_var:
    print(f'Hi {i}. How are you?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values():

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    print(mega_return_function_text_values()[17])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values():

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values()[i])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(argument_parameter):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values('argument placeholder value')[i])

except IndexError:pass
except TypeError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(argument_parameter1,argument_parameter2):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values(
            'argument placeholder value',
            'argument placeholder value')[i])

except IndexError:pass
except TypeError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(*args):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values()[i])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(*args):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values(
            'argument placeholder value',
            'argument placeholder value',
            'argument placeholder value')[i])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(keyword_argument_parameter):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values(
            keyword_argument_parameter='keyword argument placeholder value')[i])

except IndexError:pass
except TypeError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(
    keyword_argument_parameter1,
    keyword_argument_parameter2):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values(
            keyword_argument_parameter1='keyword argument placeholder value',
            keyword_argument_parameter2='keyword argument placeholder value')[i])

except IndexError:pass
except TypeError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(**kwargs):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values()[i])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def mega_return_function_text_values(**kwargs):

    return (
        'I am returned Value 1','I am returned Value 2','I am returned Value 3',
        'I am returned Value 4','I am returned Value 5','I am returned Value 6',
        'I am returned Value 7','I am returned Value 8','I am returned Value 9',
        'I am returned Value 10','I am returned Value 11','I am returned Value 12',
        'I am returned Value 13','I am returned Value 14','I am returned Value 15',
        'I am returned Value 16','I am returned Value 17','I am returned Value 18'
        )

try:

    for i in range(18):
        print(mega_return_function_text_values(
            keyword_argument_parameter1='keyword argument placeholder value',
            keyword_argument_parameter2='keyword argument placeholder value')[i])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values():

    return 1+2,2-1,5*2,10/5

print(return_function_number_values()[0])

print(int(return_function_number_values()[0]))

print(float(return_function_number_values()[0]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2*num3+num4-num5

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2*num3

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2*num3+num4-num5+num4-num1

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2**num3/num2

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return int(num3**num2+num3-num4+num1*num5*2/num2)

tuple_var = return_function_number_values(1,2,3,4,5)

print(tuple_var)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return float(num3**num2+num5)

tuple_var = return_function_number_values(1,2,3,4,5)

print(tuple_var)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num5

print(return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num1,bin_num2,bin_num3,bin_num4,bin_num5

print(return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}')[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num1,bin_num2,bin_num3,bin_num4,bin_num5

binary_num = return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}')[4]

print(binary_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num1,bin_num2,bin_num3,bin_num4,bin_num5

binary_num = return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}')

print(binary_num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num5

print(return_function_hexadecimal_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num1,hex_num2,hex_num3,hex_num4,hex_num5

print(return_function_hexadecimal_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}')[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num1,hex_num2,hex_num3,hex_num4,hex_num5

hexadecimal_num = return_function_binary_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}')[4]

print(hexadecimal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num1,hex_num2,hex_num3,hex_num4,hex_num5

hexadecimal_num = return_function_binary_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}')

print(hexadecimal_num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num5

print(return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num1,oct_num2,oct_num3,oct_num4,oct_num5

print(return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}')[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num1,oct_num2,oct_num3,oct_num4,oct_num5

octal_num = return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}')[4]

print(octal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num1,oct_num2,oct_num3,oct_num4,oct_num5

octal_num = return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}')

print(octal_num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num5

binary_num = return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{250+5:b}')

print(binary_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num5

hexadecimal_num = return_function_hexadecimal_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{250+5:x}')

print(hexadecimal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num5

octal_num = return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{250+5:o}')

print(octal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_global_value():

    global a,b,c,d

    a,b,c,d = 'John','Ron','Rob','Bob'

    return f'Hi {a}. Hi {b}. Hi {c}. Hi {d}'

print(return_global_value())

print(f'The values {a}, {b}, {c} and {d} can be called \
outside the def function through global variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_global_value(argument_parameter):

    global a,b,c,d

    a,b,c,d = 'John','Ron','Rob','Bob'

    return f'Hi {a}. Hi {b}. Hi {c}. Hi {d}'

print(return_global_value('argument placeholder value'))

print(f'The values {a}, {b}, {c} and {d} can be called \
outside the def function through global variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_global_value(keyword_argument_parameter):

    global a,b,c,d

    a,b,c,d = 'John','Ron','Rob','Bob'

    return f'Hi {a}. Hi {b}. Hi {c}. Hi {d}'

print(return_global_value(keyword_argument_parameter = 'keyword argument placeholder value'))

print(f'The values {a}, {b}, {c} and {d} can be called \
outside the def function through global variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_global_value(*args):

    global a,b,c,d

    a,b,c,d = 'John','Ron','Rob','Bob'

    return f'Hi {a}. Hi {b}. Hi {c}. Hi {d}'

print(return_global_value())

print(f'The values {a}, {b}, {c} and {d} can be called \
outside the def function through global variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_global_value(**kwargs):

    global a,b,c,d

    a,b,c,d = 'John','Ron','Rob','Bob'

    return f'Hi {a}. Hi {b}. Hi {c}. Hi {d}'

print(return_global_value())

print(f'The values {a}, {b}, {c} and {d} can be called \
outside the def function through global variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_global_value():

    global a,b,c,d

    a,b,c,d = 'John','Ron','Rob',('Bob','Tom')

    return f'Hi {a}. Hi {b}. Hi {c}. Hi {d[1]}'

print(return_global_value())

print(f'The values {a}, {b}, {c}, {d[0]} and {d[1]} can be called \
outside the def function through global variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_global_value():

    global a,b,c,d

    a,b,c,d = 'John','Jane',('Ron','Rob'),('Bob','Tom')

    return f'Hi {a}. Hi {b}. Hi {c[1]}. Hi {d[1]}'

print(return_global_value())

print(f'The values {a}, {b}, {c[1]}, {d[0]} and {d[1]} can be called \
outside the def function through global variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
crazy_tuple = (
    ('value1','value2'),
    ('value3','value4'),
    ('value5','value6'))

try:

    print(crazy_tuple[0][0])

    print(crazy_tuple[0][1])

    print(crazy_tuple[1][0])

    print(crazy_tuple[1][1])

    print(crazy_tuple[2][0])

    print(crazy_tuple[2][1])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
crazy_list = (
    ['value1','value2'],
    ['value3','value4'],
    ['value5','value6'])

try:

    print(crazy_list[0][0])

    print(crazy_list[0][1])

    print(crazy_list[1][0])

    print(crazy_list[1][1])

    print(crazy_list[2][0])

    print(crazy_list[2][1])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
crazy_dictionary = (
    {'key1':'value1','key2':'value2'},
    {'key3':'value3','key4':'value4'},
    {'key5':'value5','key6':'value6'})

try:

    print(crazy_dictionary[0].get('key1','key not found:'))

    print(crazy_dictionary[0].get('key2','key not found:'))

    print(crazy_dictionary[1].get('key3','key not found:'))

    print(crazy_dictionary[1].get('key4','key not found:'))

    print(crazy_dictionary[2].get('key5','key not found:'))

    print(crazy_dictionary[2].get('key6','key not found:'))

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a,b,c,d = (
    ('value1','value2'),
    ('value3','value4'),
    ('value5','value6'),
    ('value7','value8'))

try:

    print(a[0])

    print(a[1])

    print(b[0])

    print(b[1])

    print(c[0])

    print(c[1])

    print(d[0])

    print(d[1])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a,b,c,d = (
    ['value1','value2'],
    ['value3','value4'],
    ['value5','value6'],
    ['value7','value8'])

try:

    print(a[0])

    print(a[1])

    print(b[0])

    print(b[1])

    print(c[0])

    print(c[1])

    print(d[0])

    print(d[1])

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a,b,c,d = (
    {'key1':'value1','key2':'value2'},
    {'key3':'value3','key4':'value4'},
    {'key5':'value5','key6':'value6'},
    {'key7':'value7','key8':'value8'})

try:

    print(a.get('key1','key not found:'))

    print(a.get('key2','key not found:'))

    print(b.get('key3','key not found:'))

    print(b.get('key4','key not found:'))

    print(c.get('key5','key not found:'))

    print(c.get('key6','key not found:'))

    print(d.get('key7','key not found:'))

    print(d.get('key8','key not found:'))

except IndexError:pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what class objects are all about with simple class attribute
# properties, so we can start to have an understanding of what class
# object attribute property values are all about, as well as how many
# argument placeholder values each class object needs to satisfy for
# their argument values and visa versa.

class Class_attribute_properties_example_one:

    def __init__(self,var):
        self.class_var=var

a = Class_attribute_properties_example_one(
    'This is an instance of a single class object with one attribute property.').class_var

print(a)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_attribute_properties_example_two:

    def __init__(self,var1,var2):
        self.class_var1=var1
        self.class_var2=var2

b = Class_attribute_properties_example_two(
    'This is an instance of a single class object with two attribute properties.',
    'This is an instance of a single class object with two attribute properties.').class_var2

print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_attribute_properties_example_three:

    def __init__(self,var1,var2,var3):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

c = Class_attribute_properties_example_three(
    'This is an instance of a single class object with three attribute properties.',
    'This is an instance of a single class object with three attribute properties.',
    'This is an instance of a single class object with three attribute properties.').class_var3

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_attribute_properties_example_four:

    def __init__(self,var1,var2,var3,var4):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3
        self.class_var4=var4

d = Class_attribute_properties_example_four(
    'This is an instance of a single class object with four attribute properties.',
    'This is an instance of a single class object with four attribute properties.',
    'This is an instance of a single class object with four attribute properties.',
    'This is an instance of a single class object with four attribute properties.').class_var4

print(d)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a class with three parameter variables, including the 'self'
# variable. Create three print() functions outside the class that will
# display the three class values on the screen output, when executed.

class Class_example_one:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

print(Class_example_one('John','Smith',23).first_name)
print(Class_example_one('John','Smith',23).last_name)
print(Class_example_one('John','Smith',23).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a class with three parameter variables, including the 'self'
# variable. Create three print() functions inside the class that will
# display the three class values on the screen output, when executed.
# be sure to invoke the 'self' variable within the  three print() functions.

class Class_example_two:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_two('John','Smith',23)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same class example as the one above. The only difference
# is, that a separate return function is also created within the class object by
# itself, inside a print() function, called 'pets'.

class Class_example_three:

    def pets(pet1,pet2,pet3,pet4):
        return 'Dog','Cat','Bird','Fish'

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_three('John','Smith',23)

print(Class_example_three.pets(
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value')[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same class example as the one above. The only
# difference is, that the *args prefix is invoked. When you are not
# sure of how many parameter variables to use within a return define
# function, you can invoke the *args prefix to satisfy any number of
# argument placeholder values without the worry of how many are
# needed to satisfy the parameter variables.

class Class_example_four:

    def pets(*args):
        return 'Dog','Cat','Bird','Fish'

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_four('John','Smith',23)

print(Class_example_four.pets('argument placeholder value')[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same class example as the one above. The only
# difference is, a variable is used to store the class name and the
# return function name, 'pets'.

class Class_example_five:

    def pets(*args):
        return 'Dog','Cat','Bird','Fish'

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

Class_example_five('John','Smith',23)

return_function = Class_example_five.pets('argument placeholder value')[2]

print(return_function)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's, this time create a Main class and a Sub class so we can
# inherit all attribute properties from the main class to the subclass.

class Main_class_example_one:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

class Sub_class_example_one(Main_class_example_one):  # inherit all attribute properties from the main class
    pass

Main_class_example_one('John','Smith',23)

Sub_class_example_one('Jane','Smith',22)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a small example of the 'super()' function to show how
# it works. The 'super()' function not only inherits all attribute
# properties from the main class, but it also carries its very own
# sub class attribute properties as well. This way, we can create
# different sub class attribute properties as you will clearly notice
# in the next class example.

class Main_class_example_two:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

class Sub_class_example_two(Main_class_example_two):  # inherit all attribute properties from the main class

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)

Main_class_example_two('John','Smith',23)

Sub_class_example_two('Jane','Smith',22)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This sub class act has the exact, but redundant attribute properties
# that are the very same attribute properties within the Main class act.

class Main_class_attributes:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class_attributes:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

print(Main_class_attributes('Jane','Smith',22).first_name)

print(Sub_class_attributes('John','Smith',23).first_name)

# Let's fix this redundant attribute property problem, once and for all
# with the super() function.

class Main_class_attributes:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class_attributes(Main_class_attributes):

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)

print(Main_class_attributes('Jane','Smith',22).first_name)

print(Sub_class_attributes('John','Smith',23).first_name)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now we can reach a much better understanding of what the super()
# function does. We can create a sub class with its very own atribute
# properties, without having to create redundancy on our programming
# part. We have to invoke all the main class atribute properties into the
# super() function, along with the sub class attribute properties. But we
# don't have to recreate main class atribute property redundancy at all.

class Main_class_example_three:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(self.first_name)
        print(self.last_name)
        print(self.age)

# Inherit all attribute properties from the main class.

class Sub_class_example_three(Main_class_example_three):

# inherit all attribute properties from the main class to the sub class, without
# redundancy while, only creating the sub class attribute properties of their
# very own set of atribute properties only. In this example, we are creating
# four pet attribute properties. Note: You cannot call sub class atrubes, which
# are different to those that are in the main class, unless you use the super()
# function. Always invoke the __init__ constructor, which initalizes all the
# atribute properites from the main class, while we can add some new class
# atribute properties to the sub class act, without recreating all the attribute
# properties of the main class act.

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print(self.dog)
        print(self.cat)
        print(self.bird)
        print(self.fish)

Main_class_example_three('John','Smith',23)

Sub_class_example_three('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same main class Python program example as
# shown above. The only difference is, the print() functions are
# all outside from the two classes: main class and the sub class
# acts.

class Main_class_example_four:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

class Sub_class_example_four(Main_class_example_four):

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

# All print() functions are outside from the main class and the sub
# class acts.

print(Main_class_example_four('John','Smith',23).first_name)
print(Main_class_example_four('John','Smith',23).last_name)
print(Main_class_example_four('John','Smith',23).age)

print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').first_name)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').last_name)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').age)

print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').dog)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').cat)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').bird)
print(Sub_class_example_four('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').fish)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now take all that we've learned so far and start to have some
# serious Python programming fun! Let's create some text strings
# to make the Python program be a piece of programming art, as
# well as taking a huge step into computer science in general.
# Believe it or not!

class Main_class_example_five:

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

# Keep all the print() functions inside the main class.

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_five(Main_class_example_five):

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

# Keep all the print() functions inside the sub class.

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

# Now, simply call up the two class names alone, along with
# their argument placeholder values, without invoking the
# print() function outside the classes as we did before in the
# last example, shown above; thus creating longer Python
# command code on the programmer's part.

Main_class_example_five('John','Smith',23)

Sub_class_example_five('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')

# or this:

# Break up all Python commands so they won't disappear off
# the left edge of the screen.

Main_class_example_five('John','Smith',23)

Sub_class_example_five(
    'Jane','Smith',22,'German Shepherd',
    'Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's ratchet things up a bit and take all we've learned about
# classes and return functions, along with learning what the
# super() function does, along with its __init__ constructor,
# which initializes all the attribute properties from the main
# class to the sub class, without having to recreate main class
# attribute properties, when we want the sub class to have its
# very own, unique set of attribute properties, while being able
# to inherit the main class attribute properties without redundancy
# on the programmer's part.

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

# Call the 'main_class_example_six' variable, followed by its
# return function, called 'number_one_example'.

print(Main_class_example_six.number_one_example(2,5))

# Call the 'main_class_example_six' variable, followed by its
# return function, called 'number_two_example'.

print(Sub_class_example_six.number_two_example(2,5))

# Lastly, call the two classes, the main class and the sub class
# acts, along their own, unique argument placeholder values.

Main_class_example_six('John','Smith',23)

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same Python program example as the one above.
# The only difference is, this time we have all the print() functions
# inside the two classes. All we need to do is call the two classes
# without having to call the separate return functions outside the
# classes as we did before.

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

    print(Main_class_example_six.number_one_example(2,5))
    print(Sub_class_example_six.number_two_example(2,5))

Main_class_example_six('John','Smith',23)

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same Python program example as the one above.
# Let's just imagine that the super() function does not exist at all.
# Imagine the redundancy of the attribute properties of the main
# class to the sub class? The sub class has redundant Python code
# related to the main class which, without the super() function, we
# have to repeat this bit of Python code illustrated below:

#  self.first_name=fname
#  self.last_name=lname
#  self.age=age

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print('Hi. My first name is',self.first_name+'. What is your first name?')
        print('My last name is',self.last_name+'. What is your last name?')
        print('My age is',str(self.age)+'. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):

# redundant Python code from the main class attribute properties:

        self.first_name=fname
        self.last_name=lname
        self.age=age

# sub class attribute properties

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print('I have a',self.dog)
        print('I have a',self.cat)
        print('I have a',self.bird)
        print('I have a',self.fish)

    print(Main_class_example_six.number_one_example(2,5))
    print(Sub_class_example_six.number_two_example(2,5))

Main_class_example_six('John','Smith',23)

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish')

# Now you know why the super() function is invoked into classes,
# who's sub classes have different attribute properties of their very
# own. The super() function stops upper class attribute property
# redundancy on the programmer's part.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bonus Python String Concatenation Tips:

# Create a tuple called 'tuple_varianble', so we can use its values in
# text trings.

tuple_variable = 'Dog','Cat','Bird','Fish'

# Non formatted string concatenation example:

print('I love my',tuple_variable[0],'and my',tuple_variable[1],'so very much!')

print('I love my '+tuple_variable[0]+' and my '+tuple_variable[1]+' so very much!')

# old formatted string concatenation example:

print('I love my {} and my {} so very much!'.format(tuple_variable[0],tuple_variable[1]))

# New f' string concatenation format:

print(f'I love my {tuple_variable[0]} and my {tuple_variable[1]} so very much!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# When it comes to computer programming, text strings and
# integer strings do not mix at all. To tackle this string concatenation
# problem, we invoke the 'str()' string function, so we can mix
# them both together with ease, while doing real calculations
# with integer strings, within text strings.

# Non formatted string concatenation example:

print('Invoke the str() function to concatenate text and integer strings together:',3+4,'just like that.')

print('Invoke the str() function to concatenate text and integer strings together: '+str(3+4)+' just like that.')

# New f' string concatenation format:

print(f'Invoke the str() function to concatenate text and integer strings together: {str(3+4)} just like that.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the ( \ ) backslash in print() function text to force a hard
# line break to make Python print() function text code be on multiple
# lines.

print('This is a paragraph inside a print() function, using the \
backslash to create a hard line break. We can keep on typing \
as many lines of text we need inside a print() function.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the ( \n ) backslash 'n' to force a line break in the printed
# screen output text on multiple lines.

print('This is a paragraph inside a print() function, using the \
backslash to create a hard line break.\nWe can keep on typing \
as many lines of text we need inside a print() function.\nWe can \
force printed screen output text on multiple lines.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try another way to create printed text paragraphs, without
# invoking the ( \ ) backslash and the ( \n ) backslash 'n'.
# Let's use three single ( ''' ''' ) quote marks instead.

print('''This is a paragraph inside a print() function, using the
backslash to create a hard line break. We can keep on typing
as many lines of text we need inside a print() function. We can
force printed screen output text on multiple lines.''')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a variable to store the above print() function text code.

text_string_variable = 'This is a paragraph inside a print() function, \
using the backslash to create a hard line break.\nWe can keep on typing \
as many lines of text we need inside a print() function.\nWe can \
force printed screen output text on multiple lines.'

print(text_string_variable)  # prints out the value inside the variable called 'text'

# or this without the ( \ ) backslash and the ( \n ) backslash 'n'

text_string_variable = '''This is a paragraph inside a print() function,
using the backslash to create a hard line break. We can keep on typing
as many lines of text we need inside a print() function. We can
force printed screen output text on multiple lines.'''

print(text_string_variable)  # prints out the value inside the variable called 'text
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke index values within print() functions

print('Hello World!')  # Hello World!

print('Hello World!'[0])  # H

print('Hello World!'[-1])  # !

print('Hello World!'[0:5])  # Hello

print('Hello World!'[6:12])  # World!

print('Hello World!'[::-1],'is backwards.')  # !dlroW olleH is backwards.

# or this:

print('Hello World!'[::-1]+' is backwards.')  # !dlroW olleH is backwards.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len(), length function to count how many characters their
# are, including any spaces in between print() function text strings.

print(
    'There are',len('Hello World!'),
    'characters, including spaces.')  # There are 12 characters, including spaces.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len() length function to count how many tuple values
# there are.

tuple_value_length = ('value 1','value 2','value 3','value 4','value 5')

print('There are',len(tuple_value_length),'tuple values.')  # There are 5 tuple values.

# or this:

print('There are '+str(len(tuple_value_length))+' tuple values.')  # There are 5 tuple values.

# or this:

print(f'There are {len(tuple_value_length)} tuple values.')  # There are 5 tuple values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len() length function to count how many list values
# there are.

list_value_length = ['value 1','value 2','value 3','value 4','value 5']

print('There are',len(list_value_length),'list values.')  # There are 5 list values.

# or this:

print('There are '+str(len(list_value_length))+' list values.')  # There are 5 list values.

# or this:

print(f'There are {len(list_value_length)} list values.')  # There are 5 list values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Invoke the len() length function to count how many dictionary
# values there are.

dictionary_value_length = {'key1':'value 1','key2':'value 2','key3':'value 3','key4':'value 4','key5':'value 5'}

print('There are',len(dictionary_value_length),'dictionary values.')  # There are 5 dictionary values.

# or this:

print('There are '+str(len(dictionary_value_length))+' dictionary values.')  # There are 5 dictionary values.

# or this:

print(f'There are {len(dictionary_value_length)} dictionary values.')  # There are 5 dictionary values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's take all we've learned about string concatenation and
# recreate this very same class act, we've learned also, as well.
# Let's invoke the f' string format to make string concatenation
# much easier to create, instead of invoking commas ',' or
# plus '+' signs to concatenate strings together.

class Main_class_example_six:

    def number_one_example(num1,num2):
        return num1+num2

    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age

        print(f'Hi. My first name is {self.first_name}. What is your first name?')
        print(f'My last name is {self.last_name}. What is your last name?')
        print(f'My age is {str(self.age)}. How old are you?')

class Sub_class_example_six(Main_class_example_six):

    def number_two_example(num1,num2):
        return num1*num2

    def __init__(self,fname,lname,age,dog,cat,bird,fish):
        super().__init__(fname,lname,age)

        self.dog=dog
        self.cat=cat
        self.bird=bird
        self.fish=fish

        print(f'I have a {self.dog}')
        print(f'I have a {self.cat}')
        print(f'I have a {self.bird}')
        print(f'I have a {self.fish}')

    print(Main_class_example_six.number_one_example(2,5))
    print(Sub_class_example_six.number_two_example(2,5))

# this:

Main_class_example_six('John','Smith',23).first_name

Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').dog

# or this:

a = Main_class_example_six('John','Smith',23).first_name

b = Sub_class_example_six('Jane','Smith',22,'German Shepherd','Tabby Cat','Parrot','Angelfish').dog

print(a)
print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Bonus Mega Superclass Python Program Exercise

class Main_class_attribute_properties:

    def __init__(self,cars,boats,planes):
        self.cars=cars
        self.boats=boats
        self.planes=planes

class Sub_class1_attribute_properties(Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters):
        super().__init__(cars,boats,planes)

        self.helicopters=helicopters

class Sub_class2_attribute_properties(
    Sub_class1_attribute_properties,Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones):
        super().__init__(cars,boats,planes,helicopters)

        self.drones=drones

class Sub_class3_attribute_properties(
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones,starships):
        super().__init__(cars,boats,planes,helicopters,drones)

        self.starships=starships

class Sub_class4_attribute_properties(
    Sub_class3_attribute_properties,
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones,starships,submarines):
        super().__init__(cars,boats,planes,helicopters,drones,starships)

        self.submarines=submarines

# The Sub_class5_attribute_properties have the exact same attribute
# properties as the Sub_class4_attribute_properties. No other new class
# attribute properties exist in the Sub_class5_attribute_properties.

class Sub_class5_attribute_properties(
    Sub_class4_attribute_properties,
    Sub_class3_attribute_properties,
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,cars,boats,planes,helicopters,drones,starships,submarines):
        super().__init__(cars,boats,planes,helicopters,drones,starships,submarines)

main_class = Main_class_attribute_properties('My car','My boat','My plane').planes

sub_class1 = Sub_class1_attribute_properties(
    'My car','My boat','My airplane','My helicopter').helicopters

sub_class2 = Sub_class2_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone').drones

sub_class3 = Sub_class3_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone','My starship').starships

sub_class4 = Sub_class4_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone','My starship','My submarine').submarines

# The Sub_class5_attribute_properties have the exact same attribute
# properties as the Sub_class4_attribute_properties. No other new class
# attribute properties exist in the Sub_class5_attribute_properties.

sub_class5 = Sub_class5_attribute_properties(
    'My car','My boat','My airplane','My helicopter','My drone','My starship','My submarine').submarines

# Create a variable called 'auto_class' to store all six class object values.

auto_class = (
    main_class,sub_class1,
    sub_class2,sub_class3,
    sub_class4,sub_class5)

for i in auto_class:print(i)

# Now, we can clearly see how this all pans out to be. We've come such a
# very long way, as we've learned so much about how to create define functions,
# return define functions and classes, along with the super() function and
# string concatenation. Let's now take a much needed break! But practice,
# practice and more practice, practice; we must constantly practice at anything
# we strive to become. Even while being great at what we do, we should
# always continue to practice, practice, practice and more practice, practice,
# practice to keep on top of our game. No matter what it takes!
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These are my own, different ways of how I practice with Python
# programming. I always start from the ground and then up to
# be able to understand Python programming. When I did BASIC:
# (Beginner's All-purpose Symbolic Instruction Code) back in
# the good old days, I always started from the ground and then
# up. I never started off with hard things; instead, I would dissect
# these hard things. And with trial and error, I soon began to teach
# myself these hard things. You will quickly notice how I show
# each and every step of how to learn some of these hard Python
# programming examples, I illustrate here. In everything I teach
# about Python programming, I always show the learner how to
# dissect and break down hard Python code, so the learner can
# then learn Python much quicker like I do.

# Create a define function that have no arguments to be satisfied.

def non_arguments():
    print('I do not need any argument values at all. Thank you...')

non_arguments()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that have arguments to be satisfied.

def arguments(arg1,arg2,arg3):
    print('I need these three argument values to be satisfied. Thank you...')

arguments(
    'argument placeholder value1',
    'argument placeholder value2',
    'argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that have keyword arguments to be satisfied.

def keyword_arguments(kwarg1,kwarg2,kwarg3):
    print('I need these three keyword argument values to be satisfied. Thank you...')

keyword_arguments(
    kwarg1='keyword argument placeholder value1',
    kwarg2='keyword argument placeholder value2',
    kwarg3='keyword argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that have no arguments to be satisfied.

def return_non_arguments():
    return 'I do not need any return argument values at all. Thank you...'

print(return_non_arguments())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that have arguments to be satisfied.

def return_arguments(arg1,arg2,arg3):
    return 'I need these three return argument values to be satisfied. Thank you...'

argument_placeholder_values = return_arguments(
    'return argument placeholder value1',
    'return argument placeholder value2',
    'return argument placeholder value3')

print(argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that have keyword arguments
# to be satisfied.

def return_keyword_arguments(kwarg1,kwarg2,kwarg3):
    return 'I need these three return keyword argument values to be satisfied. Thank you...'

keyword_argument_placeholder_values = return_keyword_arguments(
    kwarg1='return keyword argument placeholder value1',
    kwarg2='return keyword argument placeholder value2',
    kwarg3='return keyword argument placeholder value3')

print(keyword_argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that invokes the *args prefix to satisfy
# any number of argument values.

def args_arguments(*args):
    print('I do not need the exact argument values to be satisfied. Thank you...')

args_arguments(
    '*args argument placeholder value1',
    '*args argument placeholder value2',
    '*args argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a define function that invokes the **kwargs prefix to satisfy
# any number of keyword argument values.

def kwargs_arguments(**kwargs):
    print('I do not need the exact keyword argument values to be satisfied. Thank you...')

kwargs_arguments(
    kwarg1='keyword argument placeholder value1',
    kwarg2='keyword argument placeholder value2',
    kwarg3='keyword argument placeholder value3')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that invokes the *args prefix to satisfy
# any number of argument values.

def return_args_arguments(*args):
    return 'I do not need the exact argument values to be satisfied. Thank you...'

return_args_argument_placeholder_values = return_args_arguments(
    'return *args argument placeholder value1',
    'return *args argument placeholder value2',
    'return *args argument placeholder value3')

print(return_args_argument_placeholder_values)

# You can also cheat in Python with the *args prefix this example shows.

def return_args_arguments(*args):
    return 'I do not need the exact argument values to be satisfied. Thank you...'

return_args_argument_placeholder_values = return_args_arguments()

print(return_args_argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a return define function that invokes the **kwargs prefix to satisfy
# any number of keyword argument values.

def return_kwargs_arguments(**kwargs):
    return 'I do not need the exact keyword argument values to be satisfied. Thank you...'

return_kwargs_argument_placeholder_values = return_kwargs_arguments(
    kwarg1='return **kwargs argument placeholder value1',
    kwarg2='return **kwargs argument placeholder value2',
    kwarg3='return **kwargs argument placeholder value3')

print(return_kwargs_argument_placeholder_values)

# You can also cheat in Python with the **kwargs prefix this example shows.

def return_kwargs_arguments(**kwargs):
    return 'I do not need the exact keyword argument values to be satisfied. Thank you...'

return_kwargs_argument_placeholder_values = return_kwargs_arguments()

print(return_kwargs_argument_placeholder_values)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a single class object with one attribute
# property.

class Single_class:

    def __init__(self,var1):
        self.class_var1=var1

print(Single_class('This is a single class object with attribute class_var1..').class_var1)

# Let's use a variable inside the print() function instead.

variable = Single_class('This is a single class object with attribute class_var1..').class_var1

print(variable)

# Let's do this if we like.

variable = Single_class('This is a single class object with attribute class_var1.')

print(variable.class_var1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a single class object with two attribute
# properties.

class Single_class:

    def __init__(self,var1,var2):
        self.class_var1=var1
        self.class_var2=var2

print(Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.').class_var2)

# Let's use a variable inside the print() function instead.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.').class_var2

print(variable)

# Let's do this if we like.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.')

print(variable.class_var2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create a single class object with three attribute
# properties.

class Single_class:

    def __init__(self,var1,var2,var3):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

print(Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.').class_var3)

# Let's use a variable inside the print() function instead.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.').class_var3

print(variable)

# Let's do this if we like.

variable = Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.')

print(variable.class_var3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Inherit the properties of the main class into all sub classses.
# Invoke the 'pass' statement to tell Python that you do not
# want anymore indented code blocks below.

class Main_class_attribute_properties:

    def __init__(self,var1,var2,var3):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

class Sub_class1_attribute_properties(  # inhert main class properties
    Main_class_attribute_properties):pass

class Sub_class2_attribute_properties(  # inhert sub class1 and main class properties
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):pass

class Sub_class3_attribute_properties(  # inhert sub class2, sub class1 and main class properties
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):pass

class Sub_class4_attribute_properties(  # inhert sub class3, sub class2, sub class1 and main class properties
    Sub_class3_attribute_properties,
    Sub_class2_attribute_properties,
    Sub_class1_attribute_properties,
    Main_class_attribute_properties):pass

a = Main_class_attribute_properties(
    'This is an instance of a main class object with three attribute properties 1',
    'This is an instance of a main class object with three attribute properties 2',
    'This is an instance of a main class object with three attribute properties 3')

b = Sub_class1_attribute_properties(
    'This is an instance of a sub class1 object with three attribute properties 1',
    'This is an instance of a sub class1 object with three attribute properties 2',
    'This is an instance of a sub class1 object with three attribute properties 3')

c = Sub_class2_attribute_properties(
    'This is an instance of a sub class2 object with three attribute properties 1',
    'This is an instance of a sub class2 object with three attribute properties 2',
    'This is an instance of a sub class2 object with three attribute properties 3')

d = Sub_class3_attribute_properties(
    'This is an instance of a sub class3 object with three attribute properties 1',
    'This is an instance of a sub class3 object with three attribute properties 2',
    'This is an instance of a sub class3 object with three attribute properties 3')

e = Sub_class4_attribute_properties(
    'This is an instance of a sub class3 object with three attribute properties 1',
    'This is an instance of a sub class3 object with three attribute properties 2',
    'This is an instance of a sub class3 object with three attribute properties 3')

# Print out all individual class attribute property values.

print(a.class_var1)
print(b.class_var1)
print(c.class_var1)
print(d.class_var1)
print(e.class_var1)

print(a.class_var2)
print(b.class_var2)
print(c.class_var2)
print(d.class_var2)
print(e.class_var2)

print(a.class_var3)
print(b.class_var3)
print(c.class_var3)
print(d.class_var3)
print(e.class_var3)

# Here are some different ways to concatenate strings together.

# Non formatted string concatenation example one.

print(a.class_var1,'\n',a.class_var2,'\n',a.class_var3)

print(b.class_var1,'\n',b.class_var2,'\n',b.class_var3)

print(c.class_var1,'\n',c.class_var2,'\n',c.class_var3)

print(d.class_var1,'\n',d.class_var2,'\n',d.class_var3)

# Non formatted string concatenation example two.

print(a.class_var1+'\n'+a.class_var2+'\n'+a.class_var3)

print(b.class_var1+'\n'+b.class_var2+'\n'+b.class_var3)

print(c.class_var1+'\n'+c.class_var2+'\n'+c.class_var3)

print(d.class_var1+'\n'+d.class_var2+'\n'+d.class_var3)

# Old formatted string concatenation example three.

print('{}\n{}\n{}'.format(a.class_var1,a.class_var2,a.class_var3))

print('{}\n{}\n{}'.format(b.class_var1,b.class_var2,b.class_var3))

print('{}\n{}\n{}'.format(c.class_var1,c.class_var2,c.class_var3))

print('{}\n{}\n{}'.format(d.class_var1,d.class_var2,d.class_var3))

# New formatted f' string concatenation example four.

print(f'{a.class_var1}\n{a.class_var2}\n{a.class_var3}')

print(f'{b.class_var1}\n{b.class_var2}\n{b.class_var3}')

print(f'{c.class_var1}\n{c.class_var2}\n{c.class_var3}')

print(f'{d.class_var1}\n{d.class_var2}\n{d.class_var3}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do a super class with sub super classes that have their
# very own attribute properties. The super() function stops
# redundant class attribute properties, while new attribute
# properties can be added to sub super classes, without having
# to rewrite the main class attribute properties again, just to
# add new ones to each sub super class object. Let's also
# create some return functions within the main super class
# so we can call them through it. These return functions have
# no argument variables and no keyword argument variables.
# However, you can create some of your own if you like.

class Main_super_class_attribute_properties:

    def return_pet():
        return 'Dog','Cat','Bird','Fish'

    def return_pet_care():
        return 'Leash','Litter box','Cage','Aquarium'

    def return_pet_toys():
        return 'Ball','Mouse toy','Bells','Air stone'

    def return_pet_cost():
        return 10,20,8,100

    def __init__(self,var1,var2,var3):

        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

class Sub_super_class1_attribute_properties(
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4):
        super().__init__(var1,var2,var3)

        self.class_var4=var4

class Sub_super_class2_attribute_properties(
    Sub_super_class1_attribute_properties,
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3,var4)

        self.class_var5=var5

class Sub_super_class3_attribute_properties(
    Sub_super_class2_attribute_properties,
    Sub_super_class1_attribute_properties,
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4,var5,var6):
        super().__init__(var1,var2,var3,var4,var5)

        self.class_var6=var6

class Sub_class4_same_attribute_properties(
    Sub_super_class3_attribute_properties,
    Sub_super_class2_attribute_properties,
    Sub_super_class1_attribute_properties,
    Main_super_class_attribute_properties):pass

a = Main_super_class_attribute_properties(
    'This is an instance of a main super class object with three attribute properties 1',
    'This is an instance of a main super class object with three attribute properties 2',
    'This is an instance of a main super class object with three attribute properties 3').class_var3

b = Sub_super_class1_attribute_properties(
    'This is an instance of a sub super class1 object with four attribute properties 1',
    'This is an instance of a sub super class1 object with four attribute properties 2',
    'This is an instance of a sub super class1 object with four attribute properties 3',
    'This is an instance of a sub super class1 object with four attribute properties 4').class_var4

c = Sub_super_class2_attribute_properties(
    'This is an instance of a sub super class2 object with five attribute properties 1',
    'This is an instance of a sub super class2 object with five attribute properties 2',
    'This is an instance of a sub super class2 object with five attribute properties 3',
    'This is an instance of a sub super class2 object with five attribute properties 4',
    'This is an instance of a sub super class2 object with five attribute properties 5').class_var5

d = Sub_super_class3_attribute_properties(
    'This is an instance of a sub super class3 object with six attribute properties 1',
    'This is an instance of a sub super class3 object with six attribute properties 2',
    'This is an instance of a sub super class3 object with six attribute properties 3',
    'This is an instance of a sub super class3 object with six attribute properties 4',
    'This is an instance of a sub super class3 object with six attribute properties 5',
    'This is an instance of a sub super class3 object with six attribute properties 6').class_var6

e = Sub_class4_same_attribute_properties(
    'This is an instance of a sub class4 object with six attribute properties 1',
    'This is an instance of a sub class4 object with six attribute properties 2',
    'This is an instance of a sub class4 object with six attribute properties 3',
    'This is an instance of a sub class4 object with six attribute properties 4',
    'This is an instance of a sub class4 object with six attribute properties 5',
    'This is an instance of a sub class4 object with six attribute properties 6').class_var6

# Print out all individual class attribute property values.

print(a)

print(b)

print(c)

print(d)

print(e)

# Print out returned values within the main super class object.

f = (
    Main_super_class_attribute_properties.return_pet()[0],
    Main_super_class_attribute_properties.return_pet()[1],
    Main_super_class_attribute_properties.return_pet()[2],
    Main_super_class_attribute_properties.return_pet()[3])

g = (
    Main_super_class_attribute_properties.return_pet_care()[0],
    Main_super_class_attribute_properties.return_pet_care()[1],
    Main_super_class_attribute_properties.return_pet_care()[2],
    Main_super_class_attribute_properties.return_pet_care()[3])

h = (
    Main_super_class_attribute_properties.return_pet_toys()[0],
    Main_super_class_attribute_properties.return_pet_toys()[1],
    Main_super_class_attribute_properties.return_pet_toys()[2],
    Main_super_class_attribute_properties.return_pet_toys()[3])

i = (
    Main_super_class_attribute_properties.return_pet_cost()[0],
    Main_super_class_attribute_properties.return_pet_cost()[1],
    Main_super_class_attribute_properties.return_pet_cost()[2],
    Main_super_class_attribute_properties.return_pet_cost()[3])

print(f[3])

print(g[3])

print(h[3])

print(i[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tip: If you invoke the plus + sign instead of a comma, you may
# have to use the str(), string function in some cases. For example,
# you might want to add or subtract integer numbers, while wanting
# to use the plus + sign to concatenate strings with integer numbers.
# Here are two examples of both types, using commas and plus +
# signs, along with one str(), string function when plus + signs are
# invoked instead of commas such as in our second example.

num1 = 10
num2 = 5

print("Let's add some numbers together:",num1+num2,'like this.')

print("Let's subtract some numbers:",num1-num2,'like this.')

# Or this when invoking plus + signs to concatenate strings together
# with integer numbers, via invoking the str(), string function.

print("Let's add some numbers together: "+str(num1+num2)+' like this.')

print("Let's subtract some numbers: "+str(num1-num2)+' like this.')

# Invoke the new f' string format to make string concatenation much easier.

print(f"Let's add some numbers together: {num1+num2} like this.")

print(f"Let's subtract some numbers: {num1-num2} like this.")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do some experimenting with define functions and see
# what we can conjure up. Let's create an outer and inner
# define function. Note: you cannot directly call inner
# define functions. You must call the inner define function
# within the outer define function to gain access to the inner
# function at execution/run time.

def outer_define_function():
    print('Outer define function.')

    def inner_define_function():
        print('Inner define function.')

    inner_define_function()

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the very same define function experiment as the example
# above; all we did was add more inner define functions inside the
# outer define function block.

def outer_define_function():
    print('Outer define function.')

    def inner_define_function1():
        print('Inner define function one.')

    def inner_define_function2():
        print('Inner define function two.')

    def inner_define_function3():
        print('Inner define function three.')

    inner_define_function1()
    inner_define_function2()
    inner_define_function3()

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try some inner return define functions within an outer define
# function.

def outer_define_function():

    def inner_define_function1():
        return 'Return inner define function one.'

    def inner_define_function2():
        return 'Return inner define function two.'

    def inner_define_function3():
        return 'Return inner define function three.'

    print(inner_define_function1())
    print(inner_define_function2())
    print(inner_define_function3())

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try some more inner return define functions within an outer
# define function. Let's create multiple return values within each
# inner define function. Let's also invoke the " \ " backslash to force
# hard line breaks.

def outer_define_function():

    def inner_define_function1():

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2():

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3():

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    print(inner_define_function1()[2])
    print(inner_define_function2()[2])
    print(inner_define_function3()[2])

outer_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's pack global variables to be called outside the outer define
# function. Invoke the " \n " backslash 'n' to create line breaks in
# the screen output at execution/run time.

def outer_define_function():

    global a,b,c

    def inner_define_function1():

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2():

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3():

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1()[2]
    b = inner_define_function2()[2]
    c = inner_define_function3()[2]

outer_define_function()

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will
# create argument variables to satisfy argument placeholder values.

def outer_define_function(argument_variable):

    global a,b,c

    def inner_define_function1(argument_variable):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(argument_variable):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(argument_variable):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1('argument placeholder value')[2]
    b = inner_define_function2('argument placeholder value')[2]
    c = inner_define_function3('argument placeholder value')[2]

outer_define_function('agument placeholder value')

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will
# create multiple argument variables to satisfy multiple argument
# placeholder values.

def outer_define_function(
    argument_variable1,
    argument_variable2,
    argument_variable3):

    global a,b,c

    def inner_define_function1(
        argument_variable1,
        argument_variable2,
        argument_variable3):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(
        argument_variable1,
        argument_variable2,
        argument_variable3):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(
        argument_variable1,
        argument_variable2,
        argument_variable3):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    b = inner_define_function2(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    c = inner_define_function3(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

outer_define_function(
    'agument placeholder value',
    'agument placeholder value',
    'agument placeholder value')

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will
# create multiple keyword argument variables to satisfy multiple
# keyword argument placeholder values.

def outer_define_function(
    keyword_argument_variable1,
    keyword_argument_variable2,
    keyword_argument_variable3):

    global a,b,c

    def inner_define_function1(
        keyword_argument_variable1,
        keyword_argument_variable2,
        keyword_argument_variable3):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(
        keyword_argument_variable1,
        keyword_argument_variable2,
        keyword_argument_variable3):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(
        keyword_argument_variable1,
        keyword_argument_variable2,
        keyword_argument_variable3):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    b = inner_define_function2(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    c = inner_define_function3(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

outer_define_function(
    keyword_argument_variable1 = 'argument placeholder value',
    keyword_argument_variable2 = 'argument placeholder value',
    keyword_argument_variable3 = 'argument placeholder value',)

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will invoke
# the *args prefix to satisfy any number argument placeholder values,
# without the worry of how many argument placeholder values are
# needed to be satisfied.

def outer_define_function(*args):

    global a,b,c

    def inner_define_function1(*args):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(*args):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(*args):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    b = inner_define_function2(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

    c = inner_define_function3(
        'argument placeholder value',
        'argument placeholder value',
        'argument placeholder value',)[2]

outer_define_function(
    'agument placeholder value',
    'agument placeholder value',
    'agument placeholder value')

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same program example below, but we will invoke
# the **kwargs prefix to satisfy any number keyword argument placeholder
# values, without the worry of how many keyword argument placeholder
# values are needed to be satisfied.

def outer_define_function(**kwargs):

    global a,b,c

    def inner_define_function1(**kwargs):

        return\
                'Return inner define function1 value one.',\
                'Return inner define function1 value two.',\
                'Return inner define function1 value three'

    def inner_define_function2(**kwargs):

        return\
                'Return inner define function2 value one.',\
                'Return inner define function2 value two.',\
                'Return inner define function2 value three'

    def inner_define_function3(**kwargs):

        return\
                'Return inner define function3 value one.',\
                'Return inner define function3 value two.',\
                'Return inner define function3 value three'

    a = inner_define_function1(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    b = inner_define_function2(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

    c = inner_define_function3(
        keyword_argument_variable1 = 'argument placeholder value',
        keyword_argument_variable2 = 'argument placeholder value',
        keyword_argument_variable3 = 'argument placeholder value',)[2]

outer_define_function(
    keyword_argument_variable1 = 'argument placeholder value',
    keyword_argument_variable2 = 'argument placeholder value',
    keyword_argument_variable3 = 'argument placeholder value',)

# Non string format examples.

print(a,'\n',b,'\n',c)

print(a+'\n'+b+'\n'+c)

# Old string format example.

print('{}\n{}\n{}'.format(a,b,c))

# Invoke the new f' string format for easier string concatenation.

print(f'{a}\n{b}\n{c}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Have some fun with these return define function examples.

def return_variable(name='John'):

    return f'Hello {name} and welcome to Python programming!'

print(return_variable())

print(return_variable('Jack'))

print(return_variable('Jim'))

print(return_variable('Bob'))

print(return_variable('Rob'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion'))

print(return_variable('ostrich'))

print(return_variable('shark'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1} and my {pet2} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion','tiger'))

print(return_variable('ostrich','shoebill'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1}, {pet2} and my {pet3} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion','tiger'))

print(return_variable('ostrich','shoebill','vulture'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_variable(pet1='dog',pet2='cat',pet3='bird',pet4='fish'):

    return f'I love my {pet1}, {pet2}, {pet3} and my {pet4} so very much.'

print(return_variable())

print(return_variable('wolf'))

print(return_variable('lion','tiger'))

print(return_variable('ostrich','shoebill','vulture'))

print(return_variable('octopus','squid','cuttlefish','sea monster'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create define functions that return integer number calculations.
# Let's also invoke the int(), integer function to create integer number
# calculations only.

def int_num_cal(nums):
    return int(nums+nums)

print(int_num_cal(5))  # 5+5 = 10
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(nums):
    return int(nums-nums)

print(int_num_cal(5))  # 5-5 = 0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(nums):
    return int(nums*nums)

print(int_num_cal(5))  # 5*5 = 25
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(nums):
    return int(nums/nums)

print(int_num_cal(5))  # 5/5 = 1
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1+num2)

print(int_num_cal(10,5))  # 10+5 = 15
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1-num2)

print(int_num_cal(10,5))  # 10-5 = 5
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1*num2)

print(int_num_cal(10,5))  # 10*5 = 50
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1/num2)

print(int_num_cal(10,5))  # 10/5 = 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create define functions that return floating point number
# calculations. Let's also invoke the float(), floating point function
# to create floating point number calculations only.

def float_num_cal(nums):
    return float(nums+nums)

print(float_num_cal(5))  # 5+5 = 10.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(nums):
    return float(nums-nums)

print(float_num_cal(5))  # 5-5 = 0.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(nums):
    return float(nums*nums)

print(float_num_cal(5))  # 5*5 = 25.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(nums):
    return float(nums/nums)

print(float_num_cal(5))  # 5/5 = 1.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1+num2)

print(float_num_cal(10,5))  # 10+5 = 15.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1-num2)

print(float_num_cal(10,5))  # 10-5 = 5.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1*num2)

print(float_num_cal(10,5))  # 10*5 = 50.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1/num2)

print(float_num_cal(10,5))  # 10/5 = 2.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try a couple of more return function math calculations
# with more argument values to be satisfied and calculated.

def int_num_cal(num1,num2,num3,num4):
    return int(num1*num2+num3-num4)

print(int_num_cal(10,5,3,2))  # 10*5+3-2 = 51
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2,num3,num4):
    return float(num1*num2+num3-num4)

print(float_num_cal(10,5,3,2))  # 10*5+3-2 = 51.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# We can also reuse Python code over and over again and again.

def int_num_cal(num1,num2,num3,num4):
    return int(num1*num2+num3-num4+num1/num4)

print(int_num_cal(10,5,3,2))  # 10*5+3-2+10/2 = 56
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2,num3,num4):
    return float(num1*num2+num3-num4+num1/num4)

print(float_num_cal(10,5,3,2))  # 10*5+3-2+10/2 = 56.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create exponents in Python, via invoking a
# double ** asterisk to create exponents. Exponents are numbers
# that are multiplied by the same number. For example: 2*2 = 4

def int_num_cal(num1,num2):
    return int(num1**num2)

print(int_num_cal(10,2))  # 10*10 = 100
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1**num2)

print(float_num_cal(10,2))  # 10*10 = 100.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn how to create cube exponents in Python, via invoking
# a double ** asterisk to create cube exponents. Cube exponents are
# numbers that are multiplied by the same number three times.
# For example: 2*2*2 = 8

def int_num_cal(num1,num2):
    return int(num1**num2)

print(int_num_cal(10,3))  # 10*10*10 = 1000
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1**num2)

print(float_num_cal(10,3))  # 10*10*10 = 1000.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_num_cal(num1,num2):
    return int(num1**num2)

print(int_num_cal(10,4))  # 10*10*10*10 = 10000
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def float_num_cal(num1,num2):
    return float(num1**num2)

print(float_num_cal(10,4))  # 10*10*10*10 = 10000.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can create exponents with the pow(), power function.

print(int(10**2))   # 10*10 = 100

# or this example:

print(int(pow(10,2)))   # 10*10 = 100

# Or this if you want floating point number calculations.

print(float(10**2))   # 10*10 = 100.0

# or this example:

print(float(pow(10,2)))   # 10*10 = 100.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python has a square root function that finds the square root of a
# number. You have to import the math module for the sqrt() function
# to work. Invoke the int(), integer function to create integer number
# calculations only.

import math

print(int(math.sqrt(9)))  # 9 squared = 3

# Or this if you want floating point number calculations.

print(float(math.sqrt(9)))  # 9 squared = 3.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some little tidbits, I've picked up along my Python
# programming journey over seven years since Christmas day, 2017.

# When writing large numbers in Python code, you can do this to
# break down large number units like this example:

print(2_000_000_000)  # 2000000000

# If you want the output screen to display broken-down number
# units in Python, you can simply do this example:

# Note: you must invoke the f' string format to be able to do the
# following Python programming examples.

print(f'{2000000000:,}')  # 2,000,000,000

# or this example:

print(f'{2_000_000_000:,}')  # 2,000,000,000
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Make the decimal base 10 number system calculate, then convert
# the result in binary base 2, hexadecimal base 16 and octal base 8
# number systems. Note: you must invoke the f' string format to be
# able to do the following Python programming examples.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a working binary to hexadecimal to octal to decimal
# counter with a for loop that will count all the way up to 255, which
# is exactly one 8b byte: 11111111 = decimal: 255. We have to import
# the time module to use the time.sleep() function within our for loop.

import time

for i in range(256):
    print(f'Binary number: {i:b} = decimal number: {i}...')

    print(f'Hexadecimal number: {i:x} = decimal number: {i}...')

    print(f'Octal number: {i:o} = decimal number: {i}...')

    time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's recreate the Python program example above, but we will make
# it more articulated with how many actual bits in one binary 8 bit byte
# there are as the binary digits count on 0 through to 255, which is exactly
# the equivalent of an 8 bit binary byte. To make this possible, we will
# need to invoke the len(), length function to count out how many bits
# to whatever binary number values there are.

import time

for i in range(256):
    print(
        'Binary number bits in one 8b byte =',\
        len(f'{i:b}'),f'bits = Binary number: {i:b} = decimal number: {i}...')

    print(f'Hexadecimal number: {i:x} = decimal number: {i}...')

    print(f'Octal number: {i:o} = decimal number: {i}...')

    time.sleep(1)  # one second delay
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# also create a problem, purposely to know that I'm starting to understand
# something in programming code, and why it works like it does. Here are
# some examples of what I keep, so I can gain instant copy and paste to reuse
# the code, instead of having to always start fresh, when I know I will use this
# code again down the road. So why not create programming layers to make
# programming much faster on your part, when you can have tons of Python
# programming snippets over time. It sure does pay off in spades to kep them...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is an easy to understand define function example, I kept, so I could
# reuse it again down the road for another Python program, I create.

def my_define_function():
    print('Python is Great!!')

my_define_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example of a simple return define function, I kept.

def my_return_argument_value():
    return 'I need no return argument values to be satisfied. Thank you...'

print(my_return_argument_value())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example of a return define function with one argument value,
# I kept.

def my_return_argument_value(argument):
    return 'I need one return argument value to be satisfied. Thank you...'

print(my_return_argument_value('one return argument placeholder value.'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a default class setup, I created, so I could reuse it someday down the
# road, whenever I might need to use it again for another program, I create.

class Single_class:

    def __init__(self,arg):
        self.arg=arg

print(Single_class('Hello World!').arg)

# or this goofy ha ha class example:

class Single_class:

    def __init__(me_myself_and_i,arg):
        me_myself_and_i.goofy=arg

print(Single_class('Python goes Goofy!').goofy)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is another class program snippet, I kept. I break things down
# to where and when I can start to finally understand what the Python
# code is all about and why it works the way it does.

class Single_class:

    def __init__(self,var1,var2,var3):
        self.class_var1=var1
        self.class_var2=var2
        self.class_var3=var3

print(Single_class(
    'This is a single class object with attribute class_var1.',
    'This is a single class object with attribute class_var2.',
    'This is a single class object with attribute class_var3.').class_var3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a main class and a sub class Python program snippet, I kept
# so I could reuse it down the road for another Python program, I create.

class Main_class_attribute_properties:

    def __init__(self,var1,var2,var3):
        self.var1=var1
        self.var2=var2
        self.var3=var3

class Sub_class_attribute_properties(  # inhert main class properties
    Main_class_attribute_properties):pass

print(Main_class_attribute_properties('I am value1','I am value2','I am value3').var3)

print(Sub_class_attribute_properties('I am value1','I am value2','I am value3').var3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a main super class and a sub super class Python program snippet,
# I kept so I could reuse it down the road for another Python program, I create.

class Main_super_class_attribute_properties:

    def __init__(self,var1,var2,var3):
        self.var1=var1
        self.var2=var2
        self.var3=var3

class Sub_super_class_attribute_properties(
    Main_super_class_attribute_properties):

    def __init__(self,var1,var2,var3,var4,var5):
        super().__init__(var1,var2,var3)

        self.var4=var4
        self.var5=var5

print(Main_super_class_attribute_properties('I am value1','I am value2','I am value3').var3)

print(Sub_super_class_attribute_properties(
    'I am value1','I am value2','I am value3','I am value4','I am value5').var5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# List Comprehension in Python

# Like always, I research when I want to learn something new, or new to me.
# Since the years I've played around with Python programming, I never ever
# explored list comprehension at all. This is like killing two birds with one
# stone's throw. I'm only experimenting with this tonight; I kept on ignoring it.
# But it shortens for loops down, when looping through a list, using a for loop
# right inside the list[ ] brackets. Believe it or not, I'm also new to this list
# comprehension thing. So you are not alone on this one. But try these out and
# tinker with them. I did that here. I just play and tinker and see what works and
# what won't work. This is what computer science is all about. Sometimes you
# just have to keep on learning and do constant research; you can only avoid
# something for so long, like I did with this headache. But like everything we
# learn; it gets easier over time. Happy researching. I'm also happily doing
# research with these below.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the enumerate() function to loop through a list, using
# only two lines of code; one for the for-index enumerate()
# function and the other for the 'print' statement.

name_list=['John','Bob','Rob','Tom']

# Here is a simple for-loop that will loop through the name_list
# values starting with index 0, followed by index 1 and then
# index 2, and finally index 3.

for index in name_list:
    print(index)

# The for-loop example above is fine, but it has its limitations
# when it comes to multi indexing through a tuple or list alike.
# With the enumerate() function, such things are possible.
# Try these enumerate() function Python program examples
# below and see what happens when you experiment with them.

for index,name in enumerate(name_list):
    print(index)

for index,name in enumerate(name_list):
    print(name)

for index,name in enumerate(name_list):
    print(index,name)

for index,name in enumerate(name_list,start=1):
    print(index,name)

name=['John','Bob','Rob','Tom']
pet=['Dog','Cat','Bird','Fish']
computer=['Desktop','Laptop','Cellphone','Notebook']

# Note: the zip() function only goes to the shortest length
# in a multi list. However, you can simply keep them the
# same size such as the list examples above, which shows
# three lists called name, pet and computer. Each list has
# four values in them. This way, every value gets called inside
# one, single 'print' statement. Try these different examples
# below. Note: you can rename the words 'index1, index2 and
# index3' to any names you wish. You can also rename the
# name variable if you like.

for index1,index2,index3 in zip(name,pet,computer):
    print(index1)

for index1,index2,index3 in zip(name,pet,computer):
    print(index2)

for index1,index2,index3 in zip(name,pet,computer):
    print(index3)

for index1,index2,index3 in zip(name,pet,computer):
    print(index1,index2,index3)

# Let's try the enumerate() function with a 2d-list.

my_2d_list=[
    ['John','Bob','Rob','Tom'],
    ['Desktop','Laptop','Cellphone','Notebook']]

for index,name in enumerate(my_2d_list):
    print(index)

for index,name in enumerate(my_2d_list):
    print(name[0])

for index,name in enumerate(my_2d_list):
    print(index,name[0])

for index,name in enumerate(my_2d_list,start=1):
    print(index,name[0])

# Let's try the zip() function with a 2d-list.

my_2d_list=[
    ['John','Bob','Rob','Tom'],
    ['Desktop','Laptop','Cellphone','Notebook']]

for index in zip(my_2d_list):
    print(index[0][0])

for index in zip(my_2d_list):
    print(index[0][0],index[0][1],index[0][2],index[0][3])

# Let's try some fun experiment examples with some of what
# we've learned so far about the enumerate() function. Let's
# create a program that uses a sentence for each value in the
# fun_list1,  fun_list2 and fun_list3 lists. Let's use the f' format
# to make string concatenations much easier to create.

fun_list1=['John','Bob','Rob','Tom']
fun_list2=['Dog','Cat','Bird','Fish']
fun_list3=['Desktop','Laptop','Cellphone','Notebook']

for index,name in enumerate(fun_list1):
    print(f"My name is {name}. I'm the value from the fun_list1, position {index}")

for index,name in enumerate(fun_list2):
    print(f"I am a {name}. I'm the value from the fun_list2, position {index}")

for index,name in enumerate(fun_list3):
    print(f"I am a {name}. I'm the value from the fun_list3, position {index}")

# These enumerate() function examples are great, but let's beef it up just a lot
# more with the zip() function, so we can create complex actions with all our
# fun_lists combined into complete, separate sentences, just simply using two
# lines of code. See what happens when you type and execute/run this Python
# program example below:

for list1,list2,list3 in zip(fun_list1,fun_list2,fun_list3):
    print(f"My name is {list1} and I have a {list2} picture on my {list3} screen.")

# The zip() function is very useful, but it can only reach as far as its shortest
# list length. That means, if you have two, three or more lists, the shortest list
# out of the three or more lists values will be cut off from the rest if one or more
# lists have extra values inside them. To avoid this from occurring, make all your
# lists the same size in each of their values. take a look at the example below:

fun_list1=['John','Bob','Rob','Tom'] # four values
fun_list2=['Dog','Cat','Bird','Fish'] # four values
fun_list3=['Desktop','Laptop','Cellphone','Notebook'] # four values

# The zip() function is sometimes better than a simple for-loop or a
# simple enumerate() function, in that it uses less lines of code and
# it can also achieve a far better programming style approach over
# program code redundancy on the programmer's part.

# Let's try one more example to prove this to be true. let's create another
# fun_list, zip() function Python program example. Type and execute/run
# this Python program below and see what happens with the output.

fun_list1=['John','Bob','Rob','Tom']
fun_list2=['Dog','Cat','Bird','Fish']
fun_list3=['Desktop','Laptop','Cellphone','Notebook']
fun_list4=['loves my','hates my','found my','lost my']
fun_list5=['fed his',"didn't feed his",'plays with his',"doesn't play with his"]

for list1,list2,list3,list4,list5 in zip(fun_list1,fun_list2,fun_list3,fun_list4,fun_list5):
    print(f'{list1} {list4} {list3} and {list5} {list2}.')

# Well, I think we pretty much learned what the enumerate() and zip()
# functions do. Now, it's practice, practice and more practice, practice...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sometimes if you are going to be using and reusing small bits of
# Python code over and over again, you might want to consider using
# the 'exec()' function. The 'exec()' function can be used in such
# examples as these examples below.

redundant_code='''
print("Python Programmer's Glossary Bible")
print('This block of code can be used and reused again and again.')
'''
# Call the 'exec()' function as many times as you please.

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example, using a for-loop to call the 'exec()' function.

for i in range(3):
    exec(redundant_code)

# Let's create a for loop inside an exec() function and see what happens
# when execute/run this Python program example:

reuse_code='''
for i in range(10):print(i)
'''
exec(reuse_code) # call the exec() function as many times as you wish
exec(reuse_code)
exec(reuse_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# BONUS! Flip Flop Game Python program example:

# This little flip flop game is a great example of how the conditional
# while-loop works. The 'else' statement executes/runs when the user
# types the wrong keys, and the while-loop iterates/repeats over again
# while ignoring the 'break' statement.

print('\nWelcome to the Flip Flop Game')

print('\nPlease type the words "flip" or "flop", then press (ENTER)')

print('\nWhen you get bored, press (ENTER) to quit playing Flip Flop')

while True:
    flip_flop=input('\nFlip? or Flop? ').strip()

    if flip_flop=='flip':
        print('\nFlop')

    elif flip_flop=='flop':
        print('\nFlip')

    elif flip_flop=='':
        print('\nThanks for playing Flip! Flop!')
        break

    else:
        print('\nYou can\'t cheat now! Do you flip? or do you flop?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I Never ever use these myself, but they are another tool I might one
# day have a usefulness for. But here is some researching I had done
# with 'lambda functions() These are, what they call anonymous functions,
# because you use them, then throw them away; whatever that means
# is still unclear to me at this time. So every time I learn something new,
# I always try to expand on it myself with different approaches to whatever
# it is, I might be wanting to learn or understand. Python has so many
# bells and whistles, that I won't in my entire lifetime live to be able to use
# them all, or even understand them all. I'm an almost a Pythonista programmer,
# but I'm not God either. But this is stuff I had learned but I might never
# ever use such bells and whistles at all. But, sometimes we all have to
# learn new tricks in our fields of interests even if we never use such things
# in our fields, whatever they might be. Every field of interest has their own
# fair share of bells and whistles, just like my chosen field of interest does.
# I love robots, computer science, and had also developed a keen ability to
# do breadboard electronics with a Raspberry Pi 4, since the last two years.
# Anyway, have some fun with these lambda functions(), or not. lol

lambda_func = lambda x:x + 2

print(lambda_func(5))

lambda_func = lambda x:x - 2

print(lambda_func(7))

lambda_func = lambda x,y:x + y

print(lambda_func(5,2))

lambda_func = lambda x,y:x - y

print(lambda_func(7,2))

lambda_func = lambda x,y,z:x + y + z

print(lambda_func(4,2,1))

lambda_func = lambda x,y,z:x - y + z

print(lambda_func(7,5,3))

lambda_func = lambda x,y,z:x - y + z + 2

print(lambda_func(7,5,3))

lambda_func = lambda first,middle,last:first+middle+last

print(lambda_func('Joseph',' C.',' Richardson'))

lambda_func = lambda first,middle,last,science:first+middle+last+science

print(lambda_func('Joseph',' C.',' Richardson',' is into Computer Science.'))

lambda_func = lambda x:True if x> 2 else False

print(lambda_func(2))

lambda_func = lambda x:'Thank you.' if x> 2 else 'I want a higher number than two!'

print(lambda_func(2))

lambda_func = lambda x:True if x> 2 else False

print(lambda_func(2))

lambda_func = lambda x:True if x>= 2 else False
print(lambda_func(2))

lambda_func = lambda x:'Thank you.' if x>= 2 else 'I want a number to equal two or \
higher than two!'

print(lambda_func(2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Backward Poem Text Python program example:

# This poem was written by Joseph C. Richardson

poem = ('''‘Knowledge’
is a free invention of the heart and of the mind itself!
The only textbooks needed, are the heart and the mind.
The only exam to be written is the key to ponder into wonder.
For the heart and the mind hold the key to the greatest diploma of all,
the dream’s creation of our imagination.
For the heart and the mind are thus, the greatest teachers of us…
Believe in yourself! For you are their greatest student.'''[::-1],

'''.tneduts tsetaerg rieht era uoy roF !flesruoy ni eveileB
…su fo srehcaet tsetaerg eht ,suht era dnim eht dna traeh eht roF
.noitanigami ruo fo noitaerc s’maerd eht
,lla fo amolpid tsetaerg eht ot yek eht dloh dnim eht dna traeh eht roF
.rednow otni rednop ot yek eht si nettirw eb ot maxe ylno ehT
.dnim eht dna traeh eht era ,dedeen skoobtxet ylno ehT
!flesti dnim eht fo dna traeh eht fo noitnevni eerf a si
’egdelwonK‘'''[::-1])

print(poem[0])

print(poem[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Well folks, it looks like the end of the line. We've covered such a lot
# about Python programming. We learned how to dissect and break
# down hard Python programming examples with a step-by-step approach.

# What I've illustrated here are ways, I learn and retain knowledge about
# Python programming in general. I keep Python program snippets to
# quickly recall and reuse them down the road. Keeping snippets of Python
# code makes creating the next Python program even faster than one
# would without snippets of Python code to reuse down the road.

# Also most importantly is writing down comments about the Python program
# or Python code you want to remember how to write, should you forget
# how to write it over a period of time. Please keep this in mind at all times.
# Get into the habit of writing down comments about Python programs and/or
# Python programming code alike.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try and except Error Handler Python program examples:

while True:
    number = int(input('\nGive me "10" please: ').strip())
    if number == 10:
        print(f'\nYou gave me "{number}", so I broke out of the \
conditonal while-loop example.')
        break

    elif number < 10:
        print(f'\nOops! You gave me "{number}", which is too small.\
I won\'t stop this condional while-loop example, until you give me "10".')

    elif number > 10:
        print(f'\nOops! You gave me "{number}", which is too big. \
I won\'t stop this condional while-loop example, until you give me "10".')

print('This is the end of the entire conditional while-loop example:')

# This Python program below is exactly the same as the Python
# program above, but with one exception. The Python program
# below has an error handler called 'try:' and 'except:' whereas
# the very same code above does not have an error handler at all.
# This spells disaster when you want the user to type numbers
# only. Without an error handler, if the user types a letter instead
# of a number, the program will crash leaving the user very unhappy
# with your newly developed software. It's imperative that in some
# situations, error handlers must be implemented into the program
# to prevent unwanted errors from occurring, such as in these 'try'
# and 'except' error handler Python program examples. From here
# onward, any 'input' statements with numeric examples given will
# contain 'try:' and 'except:' error handlers, along with some different
# 'try:' and 'except:' error handlers that deal with incorrect variable
# names, incorrect index[ ] values and incorrect typing code error
# handlers.

while True:
    try:
        number = int(input('\nGive me "10" please: ').strip())
        if number == 10:
            print(f'\nYou gave me "{number}", so I broke out of the \
conditonal while-loop example.')
            break

        elif number < 10:
            print(f'\nOops! You gave me "{number}", which is too small.\
I won\'t stop this condional while-loop example, until you give me "10".')

        elif number > 10:
            print(f'\nOops! You gave me "{number}", which is too big. \
I won\'t stop this condional while-loop example, until you give me "10".')

    except ValueError:
        print('\nThe \'try:\' and \'except ValueErorr:\' handlers prevent \
any unwanted value errors from occurring, via user input data.')

        print('\nIf the user presses any letter keys instead of pressing \
number keys, the \'try:\' and \'except:\'block executes/runs.')

print('This is the end of the entire conditional while-loop example:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a basic layout of the 'try and except', 'finally' program
# example. The program does work fine, but it does nothing.
# The program example below simply shows the basic layout
# of the 'try and except', 'finally' statements. The 'finally' statement
# is executed no matter the outcome the 'try and except' handler
# block does. Note: you can also leave out the 'finally' statement
# if you like, but it can come in handy if you want the final outcome
# to execute no matter what the 'try and except' handler block
# does. The 'pass' statements are just empty placeholders for the
# empty code blocks until they are needed, via the programmer.

try:
     pass
except:   # Invoke the right kind of error handler for the right kind of error.
     pass
else:
     pass
finally:  # the finally statement is optional
     pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is the very same 'try and except' program example below.
# Type and execute/run the program and see what happens.

try:
     message = int(input('Pick a number. ').strip())

except ValueError:
     print('Numbers only please.')

else:
     print('You picked a number.')

finally:
     print("'finally' executed no matter what.")

# The 'finally' statement is executed no matter the outcome the
# 'try and except' handler block does.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# These two 'input' statements in this program example asks the
# user their name and their age, using the 'try:' and 'except:' error
# handlers.

name = input('\nWhat is your name please? ').strip()

try:
    age = int(input(f'\nHow old are you {name}? ').strip())
    print(f'\n{name}. You are {age} years old.')

except ValueError:
    print('\nThe \'try:\' and \'except ValueError:\' block executes/runs \
whenever a letter key is pressed instead of a number key.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, put this very same program code above into a conditional
# while-loop and see what happens when the user tries to type
# letters, instead of typing numbers for their age. When the 'try:'
# block is executed, the 'break' statement causes the conditional
# while-loop to break out and the 'print' function statement ('End
# of program') is then ran/executed.

name = input('\nWhat is your name please? ').strip()

while True:
    try:
        age = int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print('\nThe \'try:\' and \'except ValueError:\' block executes/runs \
whenever a letter key is pressed instead of a number key.')

print('End of program')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        x = int(input('Please input the first number: ').strip())
        y = int(input('Please input the second number: ').strip())

        if x > y:
            print(f'{x} is greater > than {y}:')
            break

        elif x == y:
            print(f'{x} is equal to {y}:')
            break

        else:
            print(f'{x} is less < than {y}:')
            break

    except ValueError:
        print('Sorry! Integer numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
name_error_variable = 'Thank you for correcting this variable name:'

try:
    print(name_error_variabl)

except NameError:
    print('Please correct this variable name to name_error_variable:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
type_error_variable = 'Rob','Bob','Terry','Mary'

try:
    print(f'You have {len(4)} values:')

except TypeError:
    print('Please replace {len(4)} with {len(type_error_variable)}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
index_error_tuple = ('Rob','Bob','Terry','Mary')

try:
    print(index_error_tuple[4])

except IndexError:
    print(f'Please correct this index[n] number starting from index 0, through index 3:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
try:
    print(0/0)

except ZeroDivisionError:
    print('cannot divide by zero:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Below is a whole list of 68 exception handlers. The 'except Exception:
# handler right below will except all Python programming errors, but
# it's not good practice to use this all the time. Invoke the right kind
# of exception handler for the right kind of error, such as 'except
# ValueError: for example. Note: whenever your Python Idle reads back
# an error message to you after crashing, read what the error message
# says, and then use that same exception handler, like TypeError:,
# NameError: IndexError and ValueError. You will see error messages
# that display the actual exception handler to use.
'''
except Exception:  Note: the Exception: handler will except 'all' errors.

except ArithmeticError:
except AssertionError:
except AttributeError:
except BaseException:
except BlockingIOError:
except BrokenPipeError:
except BufferError:
except BytesWarning:
except ChildProcessError:
except ConnectionAbortedError:
except ConnectionError:
except ConnectionRefusedError:
except ConnectionResetError:
except DeprecationWarning:
except EOFError:
except EnvironmentError:
except Exception:
except FileExistsError:
except FileNotFoundError:
except FloatingPointError:
except FutureWarning:
except GeneratorExit:
except IOError:
except ImportError:
except ImportWarning:
except IndentationError:
except IndexError:
except InterruptedError:
except IsADirectoryError:
except KeyError:
except KeyboardInterrupt:
except LookupError:
except MemoryError:
except ModuleNotFoundError:
except NameError:
except NotADirectoryError:
except NotImplementedError:
except OSError([arg]):
except OSError(errno, strerror[, filename[, winerror[, filename2]]]):
except OverflowError:
except PendingDeprecationWarning:
except PermissionError:
except ProcessLookupError:
except RecursionError:
except ReferenceError:
except ResourceWarning:
except RuntimeError:
except RuntimeWarning:
except StopAsyncIteration:
except StopIteration:
except SyntaxError:
except SyntaxWarning:
except SystemError:
except SystemExit:
except TabError:
except TimeoutError:
except TypeError:
except UnboundLocalError:
except UnicodeDecodeError:
except UnicodeEncodeError:
except UnicodeError:
except UnicodeTranslateError:
except UnicodeWarning:
except UserWarning:
except ValueError:
except Warning:
except WindowsError:
except ZeroDivisionError:
'''
try:
     pass
except:  # Invoke the right kind of error handler for the right kind of error.
     pass
else:
     pass
finally:  # the finally statement is optional
     pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's raise some errors, via invoking the 'raise' statement along
# with the right type of exception handler with a custom message.

name_error = 'Rob'

if name_error == 'John':
    print('Hello World!')

else:
    raise NameError(f'ERROR!! My name is {name_error}:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    type_error = input('\nWhat is your name please? ').strip()

    if type_error < str([type_error]):
        raise TypeError('Sorry! Character text only please:')

    elif len(type_error) < 3:
        raise ValueError('Your name must be over 2 characters long:')

    elif len(type_error) > 10:
        raise ValueError('Your name must be less < than or equal = to 10 characters long:')

    else:
        print(f'\nHi {type_error.title()}. How are you?')
        break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
password_error = input('What is the password? ').strip()

if password_error == 'open sesame':
    print('access granted:')

else:
    raise TypeError('Sorry! access denied:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        age_error = int(input('How old are you? ').strip())

        if age_error >= 21:
            print('You are old enough to drink.')
            break

        elif age_error < 21:
            raise Exception('You are much too young to drink:')

    except ValueError:
        print('Sorry! Numbers only please:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 3

if x != 4:
    raise ValueError(f'ERROR! {x} is the incorrect value:')

else:
    print(f'{x} is the correct value:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 1
y = 5

if x > y:
    print(f'{x} is greater > than {y}:')

elif x == y:
    print(f'{x} is equal = to {y}:')

else:
    raise ValueError(f'{x} is less < than {y}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = int(input('Please input amount: ').strip())

if x <= 2000:
    print(f'{x} is less < than or equal = to 2000:')

elif x > 2000:
    raise ValueError(f'{x} is greater > than 2000')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python Clock Functions:

# Python clock functions allow you to program the actual time in real time.
# Python clock functions work internally, in sync with the Windows clock.
# With Python clock functions; you can set the hour, minute, second, month,
# week, day and date. See Python clock function prefix descriptions below.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE
'''
'%I' 12-hour prefix
'%H' 24-hour prefix
'%M' Minutes prefix
'%S' Seconds prefix
'%p' AM/PM prefix
'%A' Day of week prefix
'%B' Month prefix
'%d' Date prefix
'%Y' Year prefix
'%U' Weeks per year prefix
'%j' Days per year prefix
'''
# Let's create a simple Python clock by invoking the Python clock function
# prefixes. First, however, we also need to import two modules; 'time' and
# 'datetime'. Type and execute/run the program example below and see
# what happens.

import time
import datetime

print(datetime.datetime.now().strftime('%I:%M:%S:%p'))
print(datetime.datetime.now().strftime('%H:%M:%S'))
print(datetime.datetime.now().strftime('%A %B %d,%Y'))
print(datetime.datetime.now().strftime('Week %U'))
print(datetime.datetime.now().strftime('Day %j'))

# Remember you can reduce balky code via, using string variables. Let's
# use 'timer' as the variable and use 'datetime.datetime.now()' as the value.
# Type and execute/run the program example below and see what happens.

import time
import datetime

timer=datetime.datetime.now()

print(timer.strftime('%I:%M:%S:%p'))
print(timer.strftime('%H:%M:%S'))
print(timer.strftime('%A %B %d,%Y'))
print(timer.strftime('Week %U'))
print(timer.strftime('Day %j'))

# Now, let's create a tuple variable called 'show_time' so we can reduce
# even more balky code, and also gain greater manipulative programming
# skills at the same time. Type and execute/run the program example
# below and see what happens.

import time
import datetime

show_time=(
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

timer=datetime.datetime.now()

print(timer.strftime(show_time[0]))
print(timer.strftime(show_time[1]))
print(timer.strftime(show_time[2]))
print(timer.strftime(show_time[3]))
print(timer.strftime(show_time[4]))

# Now change and rearrange the tuple number values [0] through [4] in
# the program example above and re-execute/run the program and see
# what happens.

# Now, let's make our Python clock come to life. Let's also keep the code
# less balky and much more program manipulative at the same time. To
# make the Python clock come to life, we are simply going to use a while-
# loop to constantly refresh the screen output. A 'time.sleep()' function
# will also be implemented to create a one-second sleep delay in the screen
# output. Let's also implement the 'os.system()' function to clear the screen
# output right after every one-second 'time.sleep' delay. Type and execute/
# run the program example below and see what happens.

import os
import time
import datetime

show_time=(
    '%I:%M:%S:%p',
    '%H:%M:%S',
    '%A %B %d,%Y',
    'Week %U',
    'Day %j'
    )

while True:
    timer=datetime.datetime.now()
    print(timer.strftime(show_time[0]))
    print(timer.strftime(show_time[1]))
    print(timer.strftime(show_time[2]))
    print(timer.strftime(show_time[3]))
    print(timer.strftime(show_time[4]))

    time.sleep(1)
    os.system('cls')

# Let's shorten our code by reducing our print() functions down to only one,
# using a for loop inside the while loop.

while True:
    for i in range(5):
        timer=datetime.datetime.now()
        print(timer.strftime(show_time[i]))

    time.sleep(1)
    os.system('cls')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TIMERNATOR Python Program Example

# Try this fun Timernator Clock Python program example.

# Note: you must execute/run the program from the
# OS output screen, via double-clicking the Python
# program file itself.

import os,datetime,asyncio,winsound
from time import sleep as timernator

os.system('title TIMERNATOR')

text_colour = (
    '\x1b[31m',  # index 0 = red
    '\x1b[32m',  # index 1 = green
    '\x1b[33m',  # index 2 = yellow
    '\x1b[36m'   # index 3 = light blue
    )

special_fx = (
    f'{text_colour[0]}TIMERNATOR', # index 0 = special_fx

    'Speech Off',  # index 1 = special_fx

    'cls','\n','\n\n',' '  # index 2 = special_fx
    )

time_fx = (
f'{text_colour[2]}12 Hour {text_colour[0]}%I\
{text_colour[1]}:{text_colour[0]}%M{text_colour[1]}\
:{text_colour[0]}%S {text_colour[2]}%p',  # index 0 = time_fx

f'{text_colour[2]}24 Hour {text_colour[0]}%H{text_colour[1]}:\
{text_colour[0]}%M{text_colour[1]}:{text_colour[0]}%S',  # index 1 = time_fx

f'{text_colour[2]}%A %B {text_colour[0]}%d{text_colour[1]}:\
{text_colour[0]}%Y',f'{text_colour[2]}Week{text_colour[1]}:\
{text_colour[0]}%U {text_colour[2]}Day{text_colour[1]}:\
{text_colour[0]}%j'  # index 2 = time_fx
    )

text_fx = (
    f'{text_colour[3]}You\'re TIMERNATED!',  # index 0 = text_fx

    f'{text_colour[3]}Look at me if you want the time.',  # index 1 = text_fx

    f'{text_colour[3]}I need your hours, your minutes and your seconds.',  # index 2 = text_fx

    f'{text_colour[3]}I swear I will tell the time.',  # index 3 = text_fx

    f'{text_colour[3]}I cannot self timernate.'  # index 4 = text_fx
    )

redundant_code1 = '''
print(
    special_fx[3],
    special_fx[5]*1,
    special_fx[0],
    special_fx[4],
    special_fx[5]*1,
    text_fx[x]
    )
'''
redundant_code2 = '''
print(
    special_fx[3],
    special_fx[5]*1,
    timer.strftime(time_fx[y])
    )
'''
while True:
    for x in range(4):
        os.system(special_fx[2])
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer = datetime.datetime.now()
            exec(redundant_code2)

        timernator(1)

        os.system(special_fx[2])

        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer = datetime.datetime.now()
            exec(redundant_code2)

        timernator(1)

        os.system(special_fx[2])

        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer = datetime.datetime.now()
            exec(redundant_code2)

        timernator(1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The exc() Function Python program examples

# Sometimes if you are going to be using and reusing small bits of Python code
# over and over again, you might want to consider using the 'exec()' function.
# The 'exec()' function can be used in such examples as these examples below.

redundant_code='''
print("Python Programmer's Glossary Bible")
print('This block of code can be used and reused again and again.')
'''

# Call the 'exec()' function as many times as you please.

exec(redundant_code)
exec(redundant_code)
exec(redundant_code)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is an example, using a for-loop to call the 'exec()' function.

for i in range(3):
    exec(redundant_code)

# Let's create a for loop inside an exec() function and see what happens when
# execute/run this Python program example:

reuse_code='''
for i in range(10):print(i)
'''
exec(reuse_code) # call the exec() function as many times as you wish
exec(reuse_code)
exec(reuse_code)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

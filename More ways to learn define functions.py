# Here are more ways to create and use define functions in Python.
# This Python programming topic does not include many comments
# about each define function example. However, if you study any
# of my Python videos about define functions, I explain in full detail
# about what they are and what they do. Everything I teach in
# Python, I do it in the form of programmer's manuals. Not through
# actual Python teaching videos, where the person teaching is also
# viewed. Yet, what I teach in the form of manuals are complete,
# hands-on learning for hours on end. You can take your time and
# truly learn Python programming. Programmer's manuals have
# always been a stern must. Especially in the old days, when the
# Internet wasn't even a thought in the minds of most people
# including myself, which also made information about computer
# programming hard to find, except in a library or if you bought a
# home computer back then that came with a thick programmer's
# manual. That was the only way to learn computer programming,
# if you couldn't afford to go to college or university; that was, until
# the wonderful Internet of all things came into being. Now we
# have the grand privilege to become self taught programmers
# of any computer programming language we wish to learn, right
# at our fingertips. Imagine that? Let's go!!

# Created by Joseph C. Richardson, GitHub.com

def define_funct():
    print('John and Jane')

define_funct()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def define_funct(arg):
    print('John and Jane')

define_funct('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def define_funct(arg1,arg2):
    print('John and Jane')

define_funct('argument placeholder value','argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct():
    return 'John'

print(return_funct())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct(arg):
    return 'John'

print(return_funct('argument placeholder value'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct():
    return 'John','Jane'

print(return_funct()[0])

print(return_funct()[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct(arg):
    return 'John','Jane'

print(return_funct('argument placeholder value')[0])

print(return_funct('argument placeholder value')[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct(arg1,arg2):
    return 'John','Jane'

print(return_funct('argument placeholder value','argument placeholder value')[0])

print(return_funct('argument placeholder value','argument placeholder value')[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct(num1,num2):
    return num1+num2

print(return_funct(2,1))

print(int(return_funct(2,1)))

print(float(return_funct(2,1)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct(num1,num2):
    return num1+num2,num1-num2

print(return_funct(2,1)[0])

print(return_funct(2,1)[1])


print(int(return_funct(2,1)[0]))

print(int(return_funct(2,1)[1]))


print(float(return_funct(2,1)[0]))

print(float(return_funct(2,1)[1]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try this return define function Python program example:

def return_funct():
    return\
           'John','Jane','Bob','Ron',\
           'ball','dolls','cars','trucks',\
           8+3,5+3,19-10,2*5

# Pack some variables and some returned values by their index number.

a,b,c,d,e,f,g,h,i,j,k,l = (
    return_funct()[0],return_funct()[4],       # returned vaues: John and ball
    return_funct()[1],return_funct()[5],       # returned values: Jane and dolls
    return_funct()[2],return_funct()[6],       # returned values: Bob and cars
    return_funct()[3],return_funct()[7],       # returned values: Ron and trucks
    return_funct()[8],return_funct()[9],       # returned values: 8+3 and 5+3
    return_funct()[10],return_funct()[11])   # returned values: 19-10 and 2*5

print(f'My name is {a}. I like to play base{b}. I am {i} years old.')

print(f'My name is {c}. I like to play with my {d}. I am {j} years old.')

print(f'My name is {e}. I like to play with my {f}. I am {k} years old.')

print(f'My name is {g}. I like to play with my {h}. I am {l} years old.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try this return define function with three argument parameters
# Python program example:

def return_funct(arg1,arg2,arg3):
    return\
           'John','Jane','Bob','Ron',\
           'ball','dolls','cars','trucks',\
           8+3,5+3,19-10,2*5

# Pack some variables and some returned values by their index number.

a,b,c,d,e,f,g,h,i,j,k,l = (
    return_funct('aphv','aphv','aphv')[0],return_funct('aphv','aphv','aphv')[4],       # returned vaues: John and ball
    return_funct('aphv','aphv','aphv')[1],return_funct('aphv','aphv','aphv')[5],       # returned values: Jane and dolls
    return_funct('aphv','aphv','aphv')[2],return_funct('aphv','aphv','aphv')[6],       # returned values: Bob and cars
    return_funct('aphv','aphv','aphv')[3],return_funct('aphv','aphv','aphv')[7],       # returned values: Ron and trucks
    return_funct('aphv','aphv','aphv')[8],return_funct('aphv','aphv','aphv')[9],       # returned values: 8+3 and 5+3
    return_funct('aphv','aphv','aphv')[10],return_funct('aphv','aphv','aphv')[11])   # returned values: 19-10 and 2*5

print(f'My name is {a}. I like to play base{b}. I am {i} years old.')

print(f'My name is {c}. I like to play with my {d}. I am {j} years old.')

print(f'My name is {e}. I like to play with my {f}. I am {k} years old.')

print(f'My name is {g}. I like to play with my {h}. I am {l} years old.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try this return define function with three keyword argument
# parameters Python program example:

def return_funct(kwarg1,kwarg2,kwarg3):
    return\
           'John','Jane','Bob','Ron',\
           'ball','dolls','cars','trucks',\
           8+3,5+3,19-10,2*5

# Pack some variables and some returned values by their index number.

a,b,c,d,e,f,g,h,i,j,k,l = (
    return_funct('kwaphv','kwaphv','kwaphv'),return_funct('kwaphv','kwaphv','kwaphv'),   # returned vaues: John and ball
    return_funct('kwaphv','kwaphv','kwaphv'),return_funct('kwaphv','kwaphv','kwaphv'),   # returned values: Jane and dolls
    return_funct('kwaphv','kwaphv','kwaphv'),return_funct('kwaphv','kwaphv','kwaphv'),   # returned values: Bob and cars
    return_funct('kwaphv','kwaphv','kwaphv'),return_funct('kwaphv','kwaphv','kwaphv'),   # returned values: Ron and trucks
    return_funct('kwaphv','kwaphv','kwaphv'),return_funct('kwaphv','kwaphv','kwaphv'),   # returned values: 8+3 and 5+3
    return_funct('kwaphv','kwaphv','kwaphv'),return_funct('kwaphv','kwaphv','kwaphv'))   # returned values: 19-10 and 2*5

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[0])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[1])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[2])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[3])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[4])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[5])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[6])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[7])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try this return define function *args Python program example:

def return_funct(*args):
    return\
           'John','Jane','Bob','Ron',\
           'ball','dolls','cars','trucks',\
           8+3,5+3,19-10,2*5

# Pack some variables and some returned values by their index number.

a,b,c,d,e,f,g,h,i,j,k,l = (
    return_funct('aphv','aphv','aphv')[0],return_funct('aphv','aphv','aphv')[4],       # returned vaues: John and ball
    return_funct('aphv','aphv','aphv')[1],return_funct('aphv','aphv','aphv')[5],       # returned values: Jane and dolls
    return_funct('aphv','aphv','aphv')[2],return_funct('aphv','aphv','aphv')[6],       # returned values: Bob and cars
    return_funct('aphv','aphv','aphv')[3],return_funct('aphv','aphv','aphv')[7],       # returned values: Ron and trucks
    return_funct('aphv','aphv','aphv')[8],return_funct('aphv','aphv','aphv')[9],       # returned values: 8+3 and 5+3
    return_funct('aphv','aphv','aphv')[10],return_funct('aphv','aphv','aphv')[11])   # returned values: 19-10 and 2*5

# or with and without argument placeholder values, due to the *args prefix

a,b,c,d,e,f,g,h,i,j,k,l = (
    return_funct('aphv')[0],return_funct()[4],
    return_funct()[1],return_funct()[5],
    return_funct()[2],return_funct()[6],
    return_funct('aphv','aphv')[3],return_funct()[7],
    return_funct()[8],return_funct()[9],
    return_funct()[10],return_funct()[11])

print(f'My name is {a}. I like to play base{b}. I am {i} years old.')

print(f'My name is {c}. I like to play with my {d}. I am {j} years old.')

print(f'My name is {e}. I like to play with my {f}. I am {k} years old.')

print(f'My name is {g}. I like to play with my {h}. I am {l} years old.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try this return define function **kwargs Python program example:

def return_funct(**kwargs):
    return\
           'John','Jane','Bob','Ron',\
           'ball','dolls','cars','trucks',\
           8+3,5+3,19-10,2*5

# Pack some variables and some returned values by their index number.

a,b,c,d,e,f,g,h,i,j,k,l = (
    return_funct(),return_funct(),   # returned vaues: John and ball
    return_funct(),return_funct(),   # returned values: Jane and dolls
    return_funct(),return_funct(),   # returned values: Bob and cars
    return_funct(),return_funct(),   # returned values: Ron and trucks
    return_funct(),return_funct(),   # returned values: 8+3 and 5+3
    return_funct(),return_funct())   # returned values: 19-10 and 2*5

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[0])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[1])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[2])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[3])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[4])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[5])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[6])

print(return_funct(kwarg1='placeholder value 1',kwarg2='placeholder value 2',kwarg3='placeholder value 3')[7])

# or with and without keyword argument placeholder values, due to the **kwargs prefix

print(return_funct()[0])

print(return_funct(kwargs1='placeholder value 1')[1])

print(return_funct()[2])

print(return_funct(kwargs1='placeholder value 1',kwargs2='placeholder value 2')[3])

print(return_funct()[4])

print(return_funct()[5])

print(return_funct()[6])

print(return_funct()[7])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def define_funct(name1='John',name2='Jane'):
    print('Hello',name1)
    
    print('Hello',name2)

define_funct()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def define_funct(self,name1='John',name2='Jane'):
    print('Hello',name1)
    
    print('Hello',name2)

define_funct('argument placeholder value')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct(self,name1='John',name2='Jane'):
    return name1,name2

print('Hello',return_funct('argument placeholder value')[0])

print('Hello',return_funct('argument placeholder value')[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_funct(self,num1=8,num2=4):
    return num1,num2

print(return_funct('argument placeholder value')[0]+return_funct('argument placeholder value')[1])

print(return_funct('argument placeholder value')[0]-return_funct('argument placeholder value')[1])

print(return_funct('argument placeholder value')[0]*return_funct('argument placeholder value')[1])

print(return_funct('argument placeholder value')[0]/return_funct('argument placeholder value')[1])


print(int(return_funct('argument placeholder value')[0]+return_funct('argument placeholder value')[1]))

print(int(return_funct('argument placeholder value')[0]-return_funct('argument placeholder value')[1]))

print(int(return_funct('argument placeholder value')[0]*return_funct('argument placeholder value')[1]))

print(int(return_funct('argument placeholder value')[0]/return_funct('argument placeholder value')[1]))


print(float(return_funct('argument placeholder value')[0]+return_funct('argument placeholder value')[1]))

print(float(return_funct('argument placeholder value')[0]-return_funct('argument placeholder value')[1]))

print(float(return_funct('argument placeholder value')[0]*return_funct('argument placeholder value')[1]))

print(float(return_funct('argument placeholder value')[0]/return_funct('argument placeholder value')[1]))

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

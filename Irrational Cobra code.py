
# Let's turn rational Python programming code into irrational
# Cobra programming code. Please note: these Python
# programming examples might be a bit advanced for the
# beginner/novice Python programmer. However, these
# Python programming examples are not too hard to
# understand; even for the beginner/novice Python programmer.

# Please note: This kind of programming is not recommended for
# programming practice, whatsoever. Please do not create actual
# Python programs like these examples show. These Python program
# examples are for pure fun only; they are not meant to be practical,
# although they work just fine, nonetheless.

# Created by Joseph C. Richardson, GitHub.com

# Let's see what we can do with the print() function, starting with its
# single quote (' ') and double quote (" ") marks. Let's see how many
# of each can work inside a print() function.

print(''''Irrational Cobra Programming Code is so much FUN!''''''''''''''')  # single quote (' ') marks

print('''''''''''''''Irrational Cobra Programming Code is so much FUN!''''')  # single quote (' ') marks

print(""""Irrational Cobra Programming Code is so much FUN!""""""""""""""")  # double quote (" ") marks

print("""""""""""""""Irrational Cobra Programming Code is so much FUN!.""")  # double quote (" ") marks
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create reversed text inside a print() function with indexing [::-1]

print('This text is reversed.'[::-1])  # .desrever si txet sihT

print('.desrever si txet sihT'[::-1])  # This text is reversed.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's store the print() function inside a variable called 'print_text'
# and use it as the print() function instead.

print_text = print

print_text('Irrational Cobra Programming Code is so much FUN!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's store the input() function inside a variable called 'input_text'
# and use it as the input() function instead.

input_text = input

message = input_text('What is your name? ').title().strip()  # strip() clears whitespace

print(f'Hello {message}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's store the int(), integer function inside a variable called 'integer_num'
# and use it as the int() function instead.

integer_num = int

print(integer_num(5.0))  # 5

# Let's store the float(), function inside a variable called 'floating_point_num'
# and use it as the float() function instead.

floating_point_num = float

print(floating_point_num(5))  # 5.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's store the range() function inside a variable called 'loop'.
# and use it as the range() function instead.

loop = range

for i in loop(10):
    print('Irrational Cobra Programming Code is so much FUN!')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's store the sorted() function inside a variable called 'sorted_values'.
# and use it as the sorted() function instead.

sorted_values = sorted

abc = [
    'A','B','J','C','D','E',
    'F','G','K','H','L','U',
    'O','N','M','P','S','R',
    'Q','V','T','Y','X','Z','W']

alphabet = sorted_values(abc)

print(alphabet)  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Let's store the len(), length function inside a variable called 'number_of_values'
# and use it as the len() function instead.

number_of_values = len

print(number_of_values(alphabet))  # 0 through 25

# Let's call a value by its index number,

print(alphabet[0])  # A
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create an 'if', 'elif' and 'else' example without Python code underneath
# it. Let's place a print() function right after the colon (:) instead.

a = 'A'

if a == 'A':print('I am A'),print('Same line example.')
elif a == 'B':print('I am B'),print('Same line example.')
elif a == 'C':print('I am C'),print('Same line example.')
else:print('Sorry Nothing found:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a while loop with 'if', 'elif' and 'else', along with
# a colon on the same lines, including the 'break' statement,
# via invoking the semicolon (;) to join it onto one line of Python
# code, as shown below.

a = 'A'

while True:
    if a == 'A':print('I am A'),print('Same line example.');break
    elif a == 'B':print('I am B'),print('Same line example.');break
    elif a == 'C':print('I am C'),print('Same line example.');break
    else:print('Sorry Nothing found:');break
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a while loop without indented Python code underneath
# it. Let's place a print() function right after the colon (:) instead.

while True:print('This will repeat forever!'),print('Same line example.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for loop without indented Python code underneath
# it. Let's place a print() function right after the colon (:) instead.

for i in range(1,11):print(f'Number {i}:'),print('Same line example.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tip: You can create a variable and use any name you please.
# You cannot place numbers before letters, but you can place
# numbers after letters.

I_am_a_variable_call_me_anything_you_like = 'Perfect!!'

print(I_am_a_variable_call_me_anything_you_like)

I_am_a_variable3_call_me_4_anything_you_like = 'Perfect!!'

print(I_am_a_variable3_call_me_4_anything_you_like)

# You cannot do this:

# 4_am_a_variable_call_me_anything_you_like = 'Wrong!!'

# 4am_a_variable_call_me_anything_you_like = 'Wrong!!'

# 4_am_a_variable3_call_me_4_anything_you_like = 'Wrong!!'

# 4am_a_variable3_call_me_4_anything_you_like = 'Wrong!!'

# Here is the correct ways we create variables in programming.
# If you wish to use numbers combined with letters, you must
# create letters first, and then create numbers afterward.

variable1 = 'a'

variable2 = 'b'

print(variable1)

# or this:

variable_1 = 'a'

variable_2 = 'b'

print(variable_1)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs...

# Here are some extensive hands-on, in depth Python program examples.

# Use three single quote marks at the beginning and
# at the end of the print() function text.

print('''print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please.''')

# Use three double quote marks at the beginning and
# at the end of the print() function text.

print("""print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please.""")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use one variable to satisfy the print() function.

my_text = '''print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please.'''

print(my_text)

my_text = """print things on different lines with just one print()
function. That way you don't have create more print()
functions. All you need to do is press Enter to begin
a new line of text within your one and only print()
function. You can type as much text as you please."""

print(my_text)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create two packed variables with different text paragraphs
# in them.

my_text1,my_text2 =  ("""Don't be afraid of making mistakes, they are our greatest
lessons through life. When we learn from them, they become our greatest teachers
through life and we become their greatest, lifelong student...""",

"""Science is not just for smart people from a university. Science can and often
does happen for anyone. All you really need is a bit of imagination and a whole
lot of trial and error. Anyone can achieve anything they so wish. All you have to
do is believe in yourself, while you make all kinds of mistakes along the way.
Sooner or later, what doesn't work now will eventually work out, when you least
expect it. Science and discovery is all about trial and error. So don't become
discouraged when something won't work out right. Give it some time, before you
know it, you will start to see the sparks fly...""")

# use a plus '+' sign after the double '\n\n' line break

print(my_text1,'\n\n'+my_text2)

# or use plus '+' signs before and after the double '\n\n' line break

print(my_text1+'\n\n'+my_text2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpack multiple values, using just one, single "=" sign.
# Note: You must use equal variables to equal values.

a,b,c=1,2,3

print(a,b,c)

# Add the values together.

print(a+b+c)

# Example 2:

a,b,c,d,e,f=1,2,3,4,5,6

print(a,b,c,d,e,f)

# Add the values together.

print(a+b+c+d+e+f)

# Example 3

name1,name2,name3='Bob','Rob','John'

print(name1,'and',name2,'went to',name3+"'s",'house for dinner.')

# You can use the 'f' format to make the above print statement
# read like this.

print(f"{name1} and {name2} went to {name3}'s house for dinner.")

# Old format example of the print statement from earlier Python versions.

print("{} and {} went to {}'s house for dinner.".format(name1,name2,name3))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what Python tuples are all about with these
# Python program examples.

# print out tuple values onto the screen output

my_tuple = ('Python',"Programmer's",'Glossary','Bible')

print(my_tuple[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# this is a tuple( ) by default, without the parantheses '( )'

default_tuple = 'Python',"Programmer's",'Glossary','Bible'

print(default_tuple)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# access 'my_tuple' values 1 through 4 without printing
# the value 'Python'

my_tuple = ('Python',"Programmer's",'Glossary','Bible')

print(my_tuple[1:4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# access 'my_tuple' values 1 through 4 without printing
# the value 'Python'

my_tuple = ('Python',"Programmer's",'Glossary','Bible')

print(my_tuple[1:])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# access three of my_tuple values 0 through 3 without printing
# the value 'Bible'

my_tuple = ('Python',"Programmer's",'Glossary','Bible')

print(my_tuple[:3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# unpack tuple or list values; both examples will work the same
# way. Refer to learning and creating lists

my_tuple = ('Python',"Programmer's",'Glossary','Bible')

(we,sure,love,Python) = my_tuple

print(we,sure,love,Python)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# unpack and assign tuple or list values with an asterisk ' * ',
# both examples will work the same  way. Refer to learning
# and creating lists.

my_tuple = ('Python',"Programmer's",'Glossary','Bible')

(we,sure,*love,Python) = my_tuple

print(we,sure,love,Python)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# create a variable to join 'my_tuple1' with 'my_tuple2'

my_tuple1 = ('Python',"Programmer's",'Glossary','Bible')

my_tuple2 = ('We','sure','love','Python')

tuple_join = my_tuple1+my_tuple2

print(tuple_join)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the asterisk key ' * ' to duplicate all values in 'my_tuple' by three,
# followed by an integer count duplicator value ' 3 ', which multiplies
# the entire tuple values three times

my_tuple = ('Python',"Programmer's",'Glossary','Bible')

print(my_tuple*3)  # assign any integer number value
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# place a tuple within another tuple, while each tuple set
# returns their own indexed values

my_tuple = (('Python',"Programmer's",'Glossary','Bible'),('We','love','Python'))

print(my_tuple[0])

print(my_tuple[1])

print(my_tuple[1][1])

print(my_tuple[0][0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# create a multi-dimensional tuple

multi_dim_tuple = (
    ('Python',"Programmer's",'Glossary','Bible'),
    ('We','Love','Python!'),('Python','is','Greate!'))

print(multi_dim_tuple[0][0])

print(multi_dim_tuple[2][1])

print(multi_dim_tuple[2][2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'join( )' function to join tuple items together
# with a separator '//' string. The separator string can
# be any character/characters; two backslashes '//' are
# used for this Python program example.

tuple_join = ('Python',"Programmer's",'Glossary','Bible')

separater = '//'

print(separater.join(tuple_join))

print(separater.join(tuple_join[1]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what Python lists are all about with these
# Python program examples.

# print out list values onto the screen output

my_list = ['Python',"Programmer's",'Glossary','Bible']

print(my_list[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# change 'my_list' value 'Bible' to the value 'Book'

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list[3] = 'Book'

print(my_list[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# insert three new values into 'my_list' with indexing

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list[2:0] = ['Fun','Greate','Book']

print(my_list[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# add the value 'Book' to 'my_list' with the append( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.append('Book')

print(my_list[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# insert a new value 'Book' into 'my_list' at index[3]
# with the 'insert( )' function

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.insert(3,'Book')

print(my_list[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# remove the last value at the end of 'my_list' with the
# pop( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

# create a variable called popped, so you can see the
# value that was removed or popped off 'my_list', via the pop()
# function

popped = my_list.pop()

print(popped)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# remove the second value of 'my_list' with the pop( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

# create a variable called popped, so you can see the
# value that was removed or popped off 'my_list', via the pop()
# function

popped = my_list.pop(1)

print(popped)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# remove a value from 'my_list' with the remove( ) function

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.remove("Programmer's")

print(my_list[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# empty all values in 'my_list' with the clear( ) function,
# without deleting the 'my_list' variable

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.clear()

print(my_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# delete the entire 'my_list' variable and values, via
# invoking the 'del' prefix. Note: when you type and
# execute/run this Python program example, the program
# will cause and error and crash the program. This is
# simply because 'my_list' doesn't exist anymore

my_list = ['Python',"Programmer's",'Glossary','Bible']

del my_list

print(my_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# delete the 'my_list' value at index[1], via invoking the 'del'
# prefix

my_list = ['Python',"Programmer's",'Glossary','Bible']

del my_list[1]

print(my_list[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# copy all the values in 'my_list' to the items_list with the
# copy( ) function, then check the two lists to view them
# on the screen output at program execution time

my_list = ['Python',"Programmer's",'Glossary','Bible']

items_list = my_list.copy()

print(items_list)

print(my_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# create a variable to join 'my_list1' with 'my_list2'

my_list1 = ['Python',"Programmer's",'Glossary','Bible']

my_list2 = ['We','sure','love','Python']

list_join = my_list1+my_list2

print(list_join)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# join two lists together with the extend( ) function, then
# check 'my_list1' to view them on the screen output at
# execution time

my_list1 = ['Python',"Programmer's",'Glossary','Bible']

my_list2 = ['We','Sure','Love','Python','Programming']

my_list1.extend(my_list2)

print(my_list1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# unpack list or tuple values; both examples will work the same
# way. Refer to learning and creating tuples

my_list = ['Python',"Programmer's",'Glossary','Bible']

(we,sure,love,Python) = my_list

print(we,sure,love,Python)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# unpack and assign list or tuple values with an asterisk ' * ',
# both examples will work the same  way. Refer to learning
# and creating tuples

my_list = ['Python',"Programmer's",'Glossary','Bible']

(we,sure,*love,Python) = my_list

print(we,sure,love,Python)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the sorrt( ) function to sort 'my_list' values in
# alphabetical order

my_list = ['Python',"Programmer's",'Glossary','Bible']

my_list.sort()

print(my_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the sorted( ) function to temporarily sort 'my_list'
# values without sorting the actual 'my_list' values

my_list = ['Python',"Programmer's",'Glossary','Bible']

sorted_list = sorted(my_list)

print(sorted_list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the asterisk key ' * ' to duplicate all values in 'my_list' by three,
# followed by an integer count duplicator value ' 3 ', which multiplies
# the entire list values three times

my_list = ['Python',"Programmer's",'Glossary','Bible']

print(my_list*3)  # assign any integer number value
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# place a list within another list, while each list set
# returns their own indexed values

my_list = [['Python',"Programmer's",'Glossary','Bible'],['We','love','Python']]

print(my_list[0])

print(my_list[1])

print(my_list[1][1])

print(my_list[0][0])
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
# create a multi-dimensional list

multi_dim_list = (
    ['Python',"Programmer's",'Glossary','Bible'],
    ['We','Love','Python!'],['Python','is','Greate!'])

print(multi_dim_list[0][0])

print(multi_dim_list[2][1])

print(multi_dim_list[2][2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpacking multi-list example:

list_1,list_2,list_3=[
    [0,1,2,3,4,5,6,7,8,9],
    ['a','b','c','d','e','f','g','h','i','j','k','l','m',
     'n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['"Python',"Programmer's",'Glossary','Bible"']]

print(list_1[9])
print(list_2[0])
print(list_3[0],list_3[1],list_3[2],list_3[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unpacking multi-list for-loop example:

list_1,list_2,list_3=[
    [0,1,2,3,4,5,6,7,8,9],
    ['a','b','c','d','e','f','g','h','i','j','k','l','m',
     'n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['"Python',"Programmer's",'Glossary','Bible"']]

for i in list_1,list_2,list_3:
    print(i[0],i[1],i[2],i[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Things you can do with tuples and lists.

# Tuple Example:

variable_1='dog','cat','bird','guppy'

variable_2=(
    'Grey Wolf','Huge Tigger',
    'Macaw Parrot','Great White Shark')

variable_3='John','Rob','Ron','Bob'

variable_4='Mom','Dad','Brother','Sister'

variable_5='friend','girlfriend','boyfriend','neighbour'

for var1,var2,var3,var4,var5 in zip(variable_1,variable_2,variable_3,variable_4,variable_5):
    print(f'My {var4} and my {var5} {var3} says my {var1} is really a {var2}.')

# List Example:

variable_1=['dog','cat','bird','guppy']

variable_2=[
    'Grey Wolf','Huge Tigger',
    'Macaw Parrot','Great White Shark']

variable_3=['John','Rob','Ron','Bob']

variable_4=['Mom','Dad','Brother','Sister']

variable_5=['friend','girlfriend','boyfriend','neighbour']

for var1,var2,var3,var4,var5 in zip(variable_1,variable_2,variable_3,variable_4,variable_5):
    print(f'My {var4} and my {var5} {var3} says my {var1} is really a {var2}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let Python help you create a list of values faster with this Python program example

empty_list = []

while True:
    user_input = input("Let's create a list of values for 'empty_list': ").lower().strip()

    empty_list.append(user_input)

    if user_input == 'quit':
        break
    elif user_input == '':
        empty_list.pop(0)

empty_list.pop() # removes the very last value 'quit' in the empty_list

# check your 'empty_list' values that you created

print(f"\nPython helped you create your 'empty_list' values:\n{empty_list}")

# call an 'empty_list' value with its index value range

try:
    print(empty_list[0])
except IndexError:
    print('index out of range:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the 'join( )' function to join list items together
# with a separator '//' string. The separator string can
# be any character/characters; two backslashes '//' are
# used for this Python program example.

list_join = ['Python',"Programmer's",'Glossary','Bible']

separater = '//'

print(separater.join(list_join))

print(separater.join(list_join[1]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# You can use Emojis in Python. I just discovered this on my own, just to see if
# it would work. And it does work! WOW!! Use YouTube Emojis in your very own
# Python program examples. Use them for creating logical programs that if
# the user doesn't press the right key, you can program the Emojis to make
# an angry face. If the user does what he wants, them make the Emojis make
# a happy face and so on. Who knows? I just might create us a Python program
# to do such. Copy and then paste this program into your Python App and
# execute/run it and see what happens. Double click the file to open it so you
# can see the colour of the Emojis face. Save the file as Emojis and run it.

print('I am almost a complete Walking Human Computer Science \
Research Laboratory Machine on Two Legs. 😁')

input('Press Enter to exit the program')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are 90 emojis you can use within your Python programs.
# Please note: these were not easy to create. The emojis can't
# be copied into a list as easy as ordinary Python lists. If
# you add any of your own, make sure you don't make any mistakes.
# Python's undo button and or ctrl+z does not work; you have
# to keep undoing the mistake or the ones you don't want in the
# list, and emojis you add to the Python list. As I said, these
# weren't easy to create at all. I think 90 emojis is more than
# a great start. Don't you?

# Save the file as Emojis and then double click the Python file's
# icon to see the emojis in colour as shown in the Python program
# example. Please note: These emojis in the actual Python idle are
# green and outlined, not coloured as shown on this YouTube
# community page.

emojis_list = [
    '😀','😄','😁','😆','😅','🤣','😂','🙂','🙃','😉',
    '😊','😇','🥰','😍','🤩','😘','😗','😚','🥲','😋',
    '😛','😜','🤪','😝','🤑','🤗','🤭','🤫','🤔','🤐',
    '🤨','😐','😑','😶','😶‍🌫','😏','😒','🙄','😬','😮‍💨',
    '🤥','😌','😔','😪','🤤','😴','😷','🤒','🤕','🤢',
    '🤧','🥵','🥶','🥴','😵','😵‍💫','🤯','🤠','🥳','🥸',
    '😎','🤓','🧐','😕','😟','🙁','😮','😯','😲','😳',
    '🥺','😦','😧','😨','😰','😥','😢','😭','😱','😖',
    '😣','😞','😓','😩','😫','🥱','😤','😡','😠','🤬']

print(emojis_list[2])

input('Press Enter to exit the program.')
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
# invoke the 'pop( )' function to delete/pop 'key2' from 'my_dictionary_list'

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
# Let's create some sentences out of our animals dictionary list
# using a 'for in' items() function to drastically reduce lines of
# code and code redundancy in our Python program example.

for keys,values in animals.items():
    print(f'My {keys} is really a {values}.')

# Rename the key and value variables if you wish.

for my_keys,my_values in animals.items():
    print(f'My {my_keys} is really a {my_values}.')

for animal_keys,animal_values in animals.items():
    print(f'My {animal_keys} is really a {animal_values}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try this dictionary Python program example below and recap
# what happens when you type and execute/run this program.

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
# invoke the 'join( )' function to join dictionary keys together
# with a separator '//' string. The separator string can
# be any character/characters; two backslashes '//' are
# used for this Python program example.

dictionary_join = {
    'key1':'Python','key2':"Programmer's",'key3':'Glossary','key4':'Bible'}

separater = '//'

print(separater.join(dictionary_join))

print(separater.join(dictionary_join.get('key1')))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python dictionaries are pretty neat for data manipulation.
# You can call keys to return values. You can also use integers
# for keys and values to completely manipulate data

# dictionary 'keys' return values. Note: the word key can be any
# name you like. Play with the text values and make sentences
# out of them

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# use the dict( ) function to create a dictionary, via the screen output

make_dictionary = dict(key1='Value 1',key2='Value 2',key3='Value 3')

print(make_dictionary)  # {'key1': 'Value 1', 'key2': 'Value 2', 'key3': 'Value 3'}

print(make_dictionary.get('key1'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Check to see if there are any duplicate names, using a set.
# Sets always display values in random order, such as this set_demo
# example below illustrates. This means that every time you execute/run
# the set_demo program example, the values will always be in random
# order. However, sets are designed to get rid of duplicate values.
# Note: sets do not use indexing, such as tuples and lists do.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
# add up all the integer values in each set with the sum( ) function,
# then add up all the sets together

set1,set2,set3 = (
    {1,2,3,4,5},  # set1 = 15
    {6,7,8,9,10},  # set2 = 40
    {11,12,13,14,15})  # set3 = 65

set_total_sum = sum(set2)+sum(set3)  # 15+40+55 = 120

print(set_total_sum)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the enumerate( ) function to loop through a set of values

set1,set2,set3 = (
    {1,2,3,4,5},
    {6,7,8,9,10},
    {11,12,13,14,15})

for x,y in enumerate(set1):print(y)

for x,y in enumerate(set2):print(y)

for x,y in enumerate(set3):print(y)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# invoke the zip( ) function to loop through a set of values.
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x={1,2,3,4,9,6,7,8,5,9}
y={10,11,15,13,14,12,16,17,18,19,19}
z={20,21,22,23,27,25,26,24,28,29,22}

unionize=x.union(y,z)

convert=list(unionize)

a=slice(20)

print(convert[a])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a=list()
for i in range(10):
    a.append(i)

b=set()
for i in range(10):
    b.add(i)

print(a)
print(b)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

# count the values in the set with the len( ) function

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
'''
For those who are very new to Python programming or just programming
at all. If you are getting into Python, you will often hear the word called:
'def functions' short for (define function) and functions. Now here is where
I also became confused. Any type of functions you see, they are simply Python
commands that use parentheses () right after the Python command. Here
are examples of most of them, and what they do. Lastly, I will talk about def
functions and what they do.

int() is the integer function for turning number values into integer numbers
instead of default floating point numbers.

float() is the floating point function for turning integer numbers into floating
point numbers.

print() is the print function that allows you to type text inside the parentheses

input() is input function for allowing text to be used to ask for user data.

These are just some of the basic functions that always proceed parentheses at
the very end of the Python command line.

Now, let's explain what 'define functions' are. These type of functions are really
cool. You can create programming inside the def function block, and then when
you call up the def function's name, you simply type the name of whatever you
want to call the def function. Note: you cannot rename any functions that are
the kind above this text paragraph. With def functions, you can create any name
you wish. Here are some examples, using easy Python commands for the new
people, such was myself. And in a way, I'm still a newbie because I always find
something else in Python through their updates on the programming of it.
'''
def my_first_function():
    print("I'm the def function you created. I executed/ran when I was called.") # print() function

# Let's call up the def function, my_first_function() without the 'def' part.

my_first_function()

def my_second_function():
    print("I'm the other def funciton you created.") # print() function
    print('You can create yoru own code inside the def functions.')  # print() function

my_second_function()

def my_third_function():
    for i in range(5):
        print("def functions can also play for loops and while loops inside them.") # print() function
        print('You can create your own Python code inside def functions.')  # print() function

my_third_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# TIP: After using the colon : in a def function, just press your Enter Key on your keyboard
# and the spacebar will be automatically indented for you. Keep all the indents the same.
# On the next press of he Enter key, if you have other commands you want inside your
# def functions, you just keep pressing Enter and the indented new line will let you type
# your code without the worry of how much you need to have proper indentation within
# your Python code. For loops and while loops also use colons : Colons always indicate
# that your code will be indented every time you press the Enter key. So, instead let the
# curser do all the indentation work for you.

def return_logical_num_value(num):
    return f'{num+2:b}'

num = return_logical_num_value(8)

print(num)  # addition: 8 + 2 = 10
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num-2:b}'

num = return_logical_num_value(8)

print(num)  # subtraction: 8 - 2 = 6
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num*2:b}'

num = return_logical_num_value(8)

print(num)  # multiplication: 8 * 2 = 16
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num//2:b}'

num = return_logical_num_value(8)

print(num)  # division: 8 / 2 = 4
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num**2:b}'

num = return_logical_num_value(8)

print(num)  # **exponent: 8 ** 2 = 64
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_num_value(num):
    return f'{num//2:b}'

num = return_logical_num_value(8)

print(int(num))  # division: 8 / 2 = 4

# Use the floating point float() functions.

def return_logical_num_value(num):
    return f'{num//2:b}'

num = return_logical_num_value(8)

print(float(num))  # division: 8 / 2 = 4.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return f'{num1+num2:b}',f'{num1-num2:b}'

num = return_logical_nums_tuple_values(10,5)

print(num[0])
print(num[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return f'{num1*num2:b}',f'{num1//num2:b}'

num = return_logical_nums_tuple_values(10,5)

print(num[0])
print(num[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_logical_nums_tuple_values(num1,num2):
    return\
             (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(num[0],num[1],num[2],num[3],num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the integer int() functions.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(int(num[0]))
print(int(num[1]))
print(int(num[2]))
print(int(num[3]))
print(int(num[4]))

# Use the floating point float() functions.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(float(num[0]))
print(float(num[1]))
print(float(num[2]))
print(float(num[3]))
print(float(num[4]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Print everything on one line, separated with commas between argument variables.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

print(int(num[0]),int(num[1]),int(num[2]),int(num[3]),int(num[4]))

print(float(num[0]),float(num[1]),float(num[2]),float(num[3]),float(num[4]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a for loop, using the variable name 'num' as part of the for loop
# to count through the index values [n] in the 'num' variable indexes.

def return_logical_nums_tuple_values(num1,num2):
    return\
            (f'{num1+num2:b}',
             f'{num1-num2:b}',
             f'{num1*num2:b}',
             f'{num1//num2:b}',
             f'{num1**num2:b}')

num = return_logical_nums_tuple_values(10,5)

for i in num:
    print(i)

# or:

for i in num:
    print(int(i))

# or:

for i in num:
    print(float(i))

# or:

for i in num:
    print(int(i))
    print(float(i))

# or:

for i in num:
    print(int(i),float(i))

# You can leave out the int() and float() functions if you like; a floating point
# number by default is what the value will be in some cases.

for i in num:
    print(i,i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here are some easy ways to create math operations with return functions.

def addition(num1,num2):
    return num1 + num2 # num1 = 5, and num2 = 4

print(addition(5,4)) # These are the actual vaules

def subtraction(num1,num2):
    return num1 - num2 # num1 = 5, and num2 = 4

print(subtraction(5,4)) # These are the actual vaules

def addition(num1,num2):
    return num1 + num2 # num1 = 5, and num2 = 4

print(addition(5,4)) # These are the actual vales

def multiplication(num1,num2):
    return num1 * num2 # num1 = 5, and num2 = 4

print(multiplication(5,4)) # These are the actual vales

def division(num1,num2):
    return num1 / num2 # num1 = 5, and num2 = 4

print(division(5,4)) # These are the actual vales

def exponents(num1,num2):
    return num1 ** num2 # num1 = 5, and num2 = 4

print(exponents(5,4)) # These are the actual vales. five to the same power of four (5 * 5 * 5 * 5) = 625

# You can also use the pow() function instead of the double asterisks **

def pow_expon(num1,num2):
    return pow(num1,num2) # num1 = 5, and num2 = 4

print(pow_expon(5,4)) # These are the actual vales. five to the same power of four (5 * 5 * 5 * 5) = 625

# The sum() function can only be used with a tuple or a list. This tuple below
# is a 'default tuple'; parentheses are not used with default tuples. Any list of
# anything, text or numbers without parentheses is a tuple by default, regardless.
# Tuples are not mutable; they cannot be changed or modified in the same way
# lists[ ] can. Therefore, tuples are immutable; they cannot be changed or modified.

add_nums = 1,2,3,4,5,6,7,8,9  # default tuple
print(sum(add_nums))  # equals '45'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these Python program return function examples.

def my_first_return_value(book): # (one variable parameter)
    return "I am the actual value called 'Python'"

print(my_first_return_value(
    "placeholder argument value for the variable \
'book' that contains the value 'Python' "))


def my_second_return_value(book,python): # (two variable parameters)
    return "I am the actual value called 'Python'"

print(my_second_return_value(
    "placeholder argument value for the variable 'book'",
    "placeholder argument value for the variable 'Python'"))


def my_third_return_value(book,python,program): # (three variable parameters)
    return "I am the actual value called 'Python'"

print(my_third_return_value(
    "placeholder argument value for the variable 'book'",
    "placeholder argument value for the variable 'Python'",
    "placeholder argument value for the variable 'program'"))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn some def functions that return number values

def my_first_return_num(num): # (one variable parameter)
    return 1 # I am the actual value called 1

print(my_first_return_num("placeholder argument value for the variable 'num1'"))


def my_second_return_num(num1,num2): # (two variable parameters)
    return 2 # I am the actual values called 2

print(my_second_return_num(
    "placeholder argument value for the variable 'num1'",
    "placeholder argument value for the variable 'num2'"))


def my_third_return_num(num1,num2,num3): # (three variable parameters)
    return 3 # I am the actual values called 3

print(my_third_return_num(
    "placeholder argument value for the variable 'num1'",
    "placeholder argument value for the variable 'num2'",
    "placeholder argument value for the variable 'num3'"))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these example Python programs out. Refer to the post below of what functions and
# def functions are all about.

def my_first_funtion_variable(variable): # (one variable parameter)
    print('One parameter variable inside the def function.') # print() function

# call me up to use me!

my_first_funtion_variable('placeholder argument variable')

def my_second_function_variables(variable1,variable2): # (two variable parameters)
    print('Two parameter variables inside the def function.') # print() function

# call me up to use me!

my_second_function_variables('placeholder argument variable1','placeholder argument variable2') # three values

def my_third_function_variables(variable1,variable2,variable3): # (three variable parameters)
    print('Three parameter variables inside the def function.') # print() function

# call me up to use me!

my_third_function_variables(
    'placeholder argument variable1', # value 1
    'placeholder argument variable2', # value 2
    'placeholder argument variable3') # value 3
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some argument def function( ) examples.

def arg_funct(fname,lname,age):
    print(fname,lname,age)

arg_funct('John','Smith',30)

# return one value with the return statement.

def arg_funct(fname,lname,age):
    return fname  # return each argument variable one at a time

print(arg_funct('John','Smith',30))

def arg_funct(fname,lname,age):
    return lname  # return each argument variable one at a time

print(arg_funct('John','Smith',30))

def arg_funct(fname,lname,age):
    return age  # return each argument variable one at a time

print(arg_funct('John','Smith',30))

# create a variable 'x' to return one value with the return statement.

def arg_funct(fname,lname,age):
    return fname  # return each argument variable one at a time as shown above

x = arg_funct('John','Smith',30)

print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a continuation of the use of def fuctions(). We are doing
# the very same things we did before, but we are now going to
# create a for loop that will iterate all through the tuple() indexes
# instead of calling each one at a time by human hand. Let's use
# a for loop to make things happen, without the help of human hands.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_tuple = (function_one,function_two,function_three)

for i in my_functions_tuple:
    i()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, but with a list[].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_list = [function_one,function_two,function_three]

for i in my_functions_list:
    i()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, but with a dictionary{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_dictionary = {1:function_one,2:function_two,3:function_three}

for i in my_functions_dictionary:
    my_functions_dictionary.get(i)()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, using a casting tuple() function with a set{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_set = {function_one,function_two,function_three}

my_cast = tuple(my_functions_set) # use the casting tuple function

for i in my_cast:
    i()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's do the very same thing, using a casting list() function with a set{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_set = {function_one,function_two,function_three}

my_cast = list(my_functions_set) # use the casting tuple function

for i in my_cast:
    i()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
If you are too lazy to create an integer number line, let Python create one for you.
Simply execute/run this Python program example and then highlight and copy
the screen output and paste it into whatever you need this integer number line
for.
'''
for i in range(-10,11):
    print(i,end=', ')

# screen output: -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,

# Let's use variables this time, including for the 'print()' function. Let's also reduce
# Python code by creating a for loop that is just one, single line of code. However,
# this only works if the for loop does not contain any other code blocks; should
# you add more code blocks, this will not work but give you an error.

integers = -10,11
comma_space = ', '
integer_number_line = print

for i in range(integers[0],integers[1]):integer_number_line(i,end = comma_space)

# screen output: -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I use def functions() most of the time. These are used for either
# calling code through them, or they can be used as simple subroutines.
# You can also use them within lists, which is what these Python
# program examples shows. You can create a list[] of function
# calls, a tuple() a dictionary{} and a set{}. Note: sets{} do not use
# indexing like tuples and lists do. Sets{} only get rid of duplicate
# values, whereas lists[], tuples and dictionaries don't. We learn
# all of the above with these Python program def functions() examples.

# Let's create three def functions() called 'function_one', 'function_two'
# and 'function_three'.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

# Let's call each def function, one by one so we can see what's going on.
# To call a function, you have to call it like this:

function_one()     # do not use the colon : to call functions

function_two()     # do not use the colon : to call functions

function_three()  # do not use the colon : to call functions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a tuple().
# Remember that tuples and lists always start at index[0].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_tuple = (function_one,function_two,function_three)

my_functions_tuple[0]()  # index[0] is function_one

my_functions_tuple[1]()  # index[1] is function_two

my_functions_tuple[2]()  # index[2] is function_three

# When calling up a function through a tuple(), do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the index[]()
# box: my_functions_tuple[0](). Now, let's move onto using def functions() within
# a list[], which is similar to a tuple(). But tuples() are not mutible, wheras lists[]
# are mutible, meaning they can be changed or modified; tuples cannot be
# changed or modified at all, meaning they are not mutible.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a list[].
# Remember that tuples and lists always start at index[0].

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_list = [function_one,function_two,function_three]

my_functions_list[0]()  # index[0] is function_one

my_functions_list[1]()  # index[1] is function_two

my_functions_list[2]()  # index[2] is function_three

# When calling up a function through a list[], do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the index[]()
# box: my_functions_list[0](). Now, let's move onto using def functions() within
# a dictionary{} of values.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a dictionary{}.
# The dictionary 'keys' will be numbers or text if you like. But we are going to
# use numbers for the 'key's and make the values be the names of the functions
# we are using so the 'keys' will '.get' each of the values we call up, within our
# dictionary{}.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_dictionary = {1:function_one,2:function_two,3:function_three}

my_functions_dictionary.get(1)()  # "I'm Function One."

my_functions_dictionary.get(2)()  # "I'm Function Two."

my_functions_dictionary.get(3)()  # "I'm Function Three"

# When calling up a function through a dictionary{}, do not include the () parentheses
# right after the function call. The () parentheses go at the very end of the .get(n)(),
# my_functions_dictionary.get(1)(). Now, let's move onto using def functions() within
# a set of values. Note: sets{} get rid of duplicate values. They will also be in random
# order when using text values, instead of number values. Set{} do not produce
# output directly onto the screen at execute/run time. Instead you have to cast the
# values to a built-in tuple(), a built-in list() or a built-in dict() function.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's try placing these same functions inside a set{} in which we have to
# cast into a tuple() function, or a list() function.

def function_one():  # use the colon : to create functions
    print("I'm Function One.")

def function_two():  # use the colon : to create functions
    print("I'm Function Two.")

def function_three(): # use the colon : to create functions
    print("I'm Function Three.")

my_functions_set = {function_one,function_two,function_three}

my_cast = tuple(my_functions_set)

my_cast[0]()

my_cast[1]()

my_cast[2]()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_functions_set = {function_one,function_two,function_three}

my_cast = list(my_functions_set)

my_cast[0]()

my_cast[1]()

my_cast[2]()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

input()

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the := Walrus Operator to tempararly check for values in tuples,
# lists, dictionaries and sets. That way, you can be a bit lazy and
# not have to write two lines of code only to check for values. Note:
# default tuples won't work with the := walrus operator for indexing.
# Python cannot seem to see the values as either strings, nor integers
# when using the := walrus operator.

print(x := 1,2,3,4,5,6,7,8,9)  # x creates a default tuple of values

print(x[0]) # TypeError: 'int' object is not subscriptable

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The 'is' and 'not' prefixes are the very same things as '==' and '!='.
# The prefix 'is' is a literal '==', meaing that 'is' is goes deeper into
# Python's scope of the '==' prefix. The 'not' prefix simply means
# 'not' equal to, which is exactly the same as the '!=' prefix. These
# prefixes are mainly used for logical expressions as these Python
# program examples clearly shows. Note: you will get a SyntaxWarning
# message. This is because Python is asking you if you mean this '=='
# or 'is', which is used only for logical expressions. Remember that
# the 'is' prefix goes deeper into the Python scope than '==' does.

# Warning (from warnings module):
#   File "C:\Users\mogie54321\Desktop\How To Copy.py", line 17
#    print(2 is y) # True because y = 2
# SyntaxWarning: "is" with a literal. Did you mean "=="?

x = 1
y = 2

print(1 == x) # True because x = 1
print(2 == y) # True because y = 2

print(1 is x) # True because x = 1
print(2 is y) # True because y = 2

print(1 != x) # False because x = 1
print(2 != y) # False because y = 2

print(not x) # False because x = 1
print(not y) # False because y = 2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Check the 'animals' variable list of values to see how many values
# contain like 'letters'. For example, the letter 'i' is in three values:
# Bird, Fish and Lizard. The for loop will only show text output with
# letters that also belong inside the other values, as shown in this
# Python program example.

animals = ['Cat','Dog','Bird','Fish','Lizard']

for i in animals:
    if 'k' in i:
        print(f'The word "{i}" has {len(i)} letters in it.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The logical 'in' is great to use if you want to know if a value
# is 'in' a list[ ], a tuple( ), a dictionary{ }, a set() and a print( ) function.
# in our first example, we are only using logical text as a single
# value placeholder for the 'abc' variable. If a letter or value does
# not belong to the 'abc' variable, the 'else:' clause will execute.
# If a letter or value does belong to the 'abc' variable, the 'if'
# clause will execute.

abc = 't' # change the value 't' and re-execute this Python program example.

if abc in 'If a letter appears in this logical text.':  # logical text won't show screen output
    print(abc,'appears in the logical text.')

else:
    print(abc,'does not appear in the logical text.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use the logical 'in' to check if a tuple value is present or not.
# Note: when creating tuples( ), a default tuple is a tuple without ( )
# parentheses. That means you cannot modify, change the tuple
# values in logical expressions. Whereas lists[ ] can be changed,
# modified; meaning tuples are immutable and lists are mutable.

my_default_tuple = 'text',1,3,4,5,'more text'  # change the values and re-execute the program.

if 'more text' in my_default_tuple:
    print('appears in the default tuple.')

else:
    print('does not appear in the default tuple.')

# This is a tuple( ). Not a default tuple.

my_tuple = ('text',1,3,4,5,'more text')  # change the values and re-execute the program.

if 'more text' in my_tuple:
    print('appears in the tuple.')

else:
    print('does not appear in the tuple.')

# Let's create a list of values and check them with the logical 'in'.

my_list = ['text',1,3,4,5,'more text']  # change the values and re-execute the program.

if 'more text' in my_list:
    print('appears in the list.')

else:
    print('does not appear in the list.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is something else we can do with the Walrus := operator.
# Here are two Python program examples that will show you the
# 'if' statement, using the none walrus := operator, and the use
# of the walrus := operator with the 'if' statement.

x = 3

if x == 3:print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Notice how the very same Python code above is exactly the
# very same Python code as below. As you can clearly see, the
# walrus := operator reduces the usual two lines of Python code
# down to just one, single line of Python code.

if x := 3:print(x) # the walrus := operator makes x act as if it were named first.

# You don't have to create a variable first, to then place it within an
# 'if' statement using the walrus := operator.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
# or the word Knowledge. Any words therafter dosen't have quote marks;
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

print(text[1]) # index[1] is the word: is

# Let's use a for loop to call up all the words to the poem, without showing ugly
# commas ' , ' and index[ ] brackets.

for i in text:print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a basic layout of the 'try and except', 'finally' program
# example. The program does work fine, but it does nothing.
# The program example below simply shows the basic layout
# of the 'try and except', 'finally' statements. The 'finally' statement
# is executed no matter the outcome the 'try and except' handler
# block does. Note: you can also leave out the 'finally' statement
# if you like, but it can come in handy if you want the final outcome
# to execute no matter what the 'try and except' handler block does.
# The 'pass' statements are just empty placeholders for the empty
# code blocks until they are needed, via the programmer.

try:
     pass
except:
     pass
else:
     pass
finally:
     pass

# Here is the very same 'try and except' program example below.
# Type and execute/run the program and see what happens.

try:
     message=int(input('Pick a number. ').lower().strip())
except ValueError:
     print('Numbers only please.')
else:
     print('You picked a number.')
finally:
     print("'finally' executed no matter what.")

# The 'finally' statement is executed no matter the outcome the
# 'try and except' handler block does.

# These two 'input' statements in this program example asks the
# user their name and their age, using the 'try:' and 'except:' error
# handlers.

name=input('\nWhat is your name please? ').lower().strip()

try:
    age=int(input(f'\nHow old are you {name}? ').lower().strip())
    print(f'\n{name}. You are {age} years old.')

except ValueError:
    print('\nThe \'try:\' and \'except ValueError:\' block executes/runs whenever a letter \
key is pressed instead of a number key.')

# Now, put this very same program code above into a conditional
# while-loop and see what happens when the user tries to type letters,
# instead of typing numbers for their age. When the 'try:' statement is
# executed, the 'break' statement causes the conditional while-loop to
# break out and the 'print' statement ('End of program') is then executed.

name=input('\nWhat is your name please? ').lower().strip()

while True:
    try:
        age=int(input(f'\nHow old are you {name}? ').lower().strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print('\nThe \'try:\' and \'except ValueError:\' block executes/runs whenever a \
letter key is pressed instead of a number key.')

# This little flip flop game is a great example of how the conditional while-
# loop works. The 'else' statement executes/runs when the user types the
# wrong keys, and the while-loop iterates/repeats over again while ignoring
# the 'break' statement.

print('\nWelcome to Flip! Flop!')

print('\nPlease type the words "flip" or "flop", then press (ENTER)')

print('\nWhen you give up, press (ENTER) to quit playing Flip! Flop!')

while True:
    flip=input('\nFlip? or Flop? ').strip()

    if flip=='flip':
        print('\nFlop!')

    elif flip=='flop':
        print('\nFlip!')

    elif flip=='':
        print('\nThanks for playing Flip! Flop!')
        break

    else:
        print('\nYou can\'t cheat now! Do you flip? or do you flop?')

# This conditional while-loop will loop as long as the value is less (<)
# than 3, then it will stop its iteration no matter what wrong keys the
# user tries to type.

chance=0

name=input('\nWhat is your name please? ').strip()

while chance<3:
    try:
        age=int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print(f'\nYou have 3 chances left before the while-loop breaks out anyway!')

        chance+=1

# This for-loop example does exactly the same thing, the above
# while-loop example shows. The only difference is, the while-loop
# is a conditional loop, whereas the for-loop is an iterate. While-
# loops can also be 'True:' or 'False:', depending on the outcome
# of a program's execution run. While-loops also compare data
# greater than or less than other data, as shown in the examples
# above.

name=input('\nWhat is your name please? ').strip()

for chance in range(3):
    try:
        age=int(input(f'\nHow old are you {name}? ').strip())
        print(f'\n{name}. You are {age} years old.')
        break

    except ValueError:
        print('\nYou have 3 chances left before the while-loop breaks out anyway!')

        chance+=1
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Did you know you can create variables for some of these Python
commands/functions? This will give us much more opertunities
to use variables as Python code in a for loop that loops through
a list of values, which are actual Python commands/functions.
You can create two or more Python commands/functions with
just one for loop alone. Let's explore what these variables can
do for us, using actual Python code itself.
'''
absolute_num = abs
add_nums = sum
ascii_character = ascii
ascii_character_num = ord
ascii_character_value = chr
binary_base_2 = bin
character_string = str
convert_to_list = list
convert_to_set = set
convert_to_tuple = tuple
dictionary = dict
float_num = float
George_Boole = bool
hexadecimal_base_16 = hex
index_error = IndexError
integer_num = int
maximum_num = max
memory_error = MemoryError
minimum_num = min
redundant_code = exec
round_num = round
super_function = super
text_input = input
text_print = print
value_error = ValueError
value_length = len
you_quitter = quit
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try a simple print() command/function and see what this does
# We will also create a variable to be a text placeholder, so we don't
# have to keep rewriting text sentences over and over again.

text = "This was Python's print() command/function."

# this:

print("This was Python's print() command/function.")

# or this:

text_print(text) # use variables instead if you like
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try a few more to get the hange of things. Let's add some numbers
# together with the sum() command/function, we renamed to 'add_nums'
# using a variable to store the actual sum() command/function. We also
# need to create a variable we'll call nums, so we can store a default tuple
# of numbers without any parenthesese, ie: (1,2,3,4,5,6,7,8,9)

nums = 1,2,3,4,5,6,7,8,9 # this is a tuple by default, without parentheses ' () '

# this:

print(sum(nums))

# or this:

text_print(add_nums(nums))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's try a simple input() command/function and see what this does We will
# create a variable to be a text placeholder, so we don't have to keep rewriting
# text sentences over and over again. We also have to create an 'user_input'
# variable so the user can type into it.

input_text = "This was Python's input() command/function."

# this:

user_input = input("This was Python's input() command/function.")

# or this:

user_input = text_input(input_text)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's use a for loop to loop through a tuple of variables, which are actual Python
# commands/functions. Let's creat our tuple called loop.

loop = integer_num,binary_base_2,hexadecimal_base_16

for i in loop:
    text_print(f'{i(255)}. You only need one print statement with a list of variables.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# If you create classes with just print( ) functions inside them,
# they run as if nothing was used but a simple print( ) function.
# These classes will not wait to be run. They look as if they don't
# matter at all. So if you get into creating classes, don't do it this
# way.

class Print:
    print('This prints out as if nothing happens')

class Print2:
    print('This also prints out as if nothing happens')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create a single class.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

print(Single_class('argument1','argument2','argument3').arg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create a single class without
# attributes but only a def function( ) inside it.

class Single_class:
    def inner_function():
        print('Add me to the Single class.')

Single_class.inner_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create a single class with
# attributes and a def function( ) inside it. Note: you cannot call
# the def function, 'inner_function( )' at the same time you call
# the 'Single_class' attributes. Instead, you have to call each
# one separately.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute
    def inner_function():
        print('Add me to the Single class.')

print(Single_class('argument1','argument2','argument3').arg1)

Single_class.inner_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# It does not matter the order of how you place the inner def
# function( ) and the Single_class attributes. However, you still
# cannot call both at the same time. The example above is less
# confusing looking than the example shown here.

class Single_class:
    def inner_function():
        print('Add me to the Single class.')
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

print(Single_class('argument1','argument2','argument3').arg1)

Single_class.inner_function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a def function with a return statement inside the
# Single_class act. Once again, you cannot call both the Single_class
# attributes and the inner def function( ) at the same time. However,
# in this example below, it does matter about the order you place
# the single class attributes in. Once you create a return function,
# the cursor will automatically jump right out of the indented
# class Python code when the 'Enter key' is pressed.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute
    def inner_function(self):
        return 'Return me to the Single class.'

print(Single_class('argument1','argument2','argument3').arg1)

print(Single_class.inner_function('argument placeholder value'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a 'Super_class' and invoke the 'super( ) function so we
# don't have to repeat any attributes with in our super_function_class.

class Super_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The super( ) function reduces redundant Python code, so you can keep
# Python code nice and 'DRY!' ( "Don't Repeat Yourself!" )

class Super_function_class(Super_class):
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

print(Super_function_class('argument1','argument2','argument3').arg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create the same 'Super_class' act, but let's now expand/add to the
# 'Super_function_class' act with attributes of its own, while not having
# to repeat the attributes from the 'Super_class' act.

class Super_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Super_function_class(Super_class):
    def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6):
        self.arg4=arg4  # attribute
        self.arg5=arg5  # attribute
        self.arg6=arg6  # attribute
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

print(Super_function_class(
    'argument1','argument2','argument3','argument4','argument5','argument6').arg5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# It does not matter the order of how you place the Super_function_class
# attributes. You can place the super( ) function before the Super_function_class
# attributes. However, the example above is less confusing looking than the
# example shown here.

class Super_function_class(Super_class):
    def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method
        self.arg4=arg4  # attribute
        self.arg5=arg5  # attribute
        self.arg6=arg6  # attribute

print(Super_function_class(
    'argument1','argument2','argument3','argument4','argument5','argument6').arg5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Lastly, if we create a class with just a simple 'print( )' function, it won't really do
# anything, but print out text inside the print( ) function as if we didn't even create
# a class at all; there is simply nothing to call. So the class is practically ignored;
# the print( ) function executes/runs anyway. So avoid stuff like this if you want
# your Python classes to work properly. Classes love 'ATTRIBUTES' and proper
# classes need attributes to work correctly, so we call them when we want to
# call them. Not when they want to be called. Remember! We're the Boss, not
# the classes. The class attributes make sure that they obey the Boss's orders.
# Not the other way around.

class Single_class:
    print("I don't really do anything, but show printed text.")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create a single class, using variables.
# Next, we will get into for loops, using a tuple( ) for our class argument
# values. Tuples are immutable; they cannot be changed or modified.
# Tuple indexes[ ] always start at zero, not one. Let's create a tuple( ) that
# will hold all our class attribute argument values

class_arguments_tuple = ('argument1','argument2','argument3')

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

# If you don't have enough room to see the whole print( ) function text and or
# variables on one line, you can do the following.

print(
    Single_class(
    class_arguments_tuple[0],  # index[0]
    class_arguments_tuple[1],  # index[1]
    class_arguments_tuple[2]   # index[2]
    ).arg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is the very same print( ) function that's all on one line. When you type this
# out, you won't be able to see all the Python code inside the print( ) function
# without having to scroll your cursor all the way to the end, until you can see the
# text and or variables at the end of the entire print( ) function. So to keep things
# like this from occurring, we will always use the above example for our print( )
# functions

print(Single_class(class_arguments_tuple[0],class_arguments_tuple[1],class_arguments_tuple[2]).arg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for loop that will loop through all the class argument variables
# and show all the class argument values on the screen with only one print( )
# function. Again, we will use a tuple, and then use the tuple's variable name
# to count the actual for loop values. We can also do this all with one, single
# line of Python code. We can place the print( ) function right after the for loop's
# colon : on the same line as the for loop. However, this will only work if you
# don't have any other code blocks within the for loop. This will not work if you
# have other indented Python commands within the for loop.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

tuple_loop = (
    Single_class('argument1','argument2','argument3').arg1,
    Single_class('argument1','argument2','argument3').arg2,
    Single_class('argument1','argument2','argument3').arg3)

# See how we drastically reduced our Python code, using a tuple( )?
# Also, we used the tuple's variable name 'tuple_loop' to do the counting
# of the tuple_loop values for us automatically without the worry of how
# high we have to make the for loop count.

for i in tuple_loop:print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's create a list[ ] and do exactly the same as we did before with
# with our tuple( ). Lists are mutable, meaning they can be changed or
# modified, whereas tuples cannot be changed or modified. In most
# cases, it's a good idea to use a list[ ] if you want your list of values to
# change over time throughout your Python program.

class_arguments_list = ['argument1','argument2','argument3']

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

# If you don't have enough room to see the whole print( ) function text and or
# variables on one line, you can do the following.

print(
    Single_class(
    class_arguments_list[0],  # index[0]
    class_arguments_list[1],  # index[1]
    class_arguments_list[2]   # index[2]
    ).arg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for loop that will loop through all the class argument variables
# and show all the class argument values on the screen with only one print( )
# function. Again, we will use a list, and then use the list's variable name
# to count the actual for loop values. We can also do this all with one, single
# line of Python code. We can place the print( ) function right after the for loop's
# colon : on the same line as the for loop. However, this will only work if you
# don't have any other code blocks within the for loop. This will not work if you
# have other indented Python commands within the for loop.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

list_loop = [
    Single_class('argument1','argument2','argument3').arg1,
    Single_class('argument1','argument2','argument3').arg2,
    Single_class('argument1','argument2','argument3').arg3]

# See how we drastically reduced our Python code, using a list[ ]?
# Also, we used the list's variable name 'list_loop' to do the counting
# of the list_loop values for us automatically without the worry of how
# high we have to make the for loop count.

for i in list_loop:print(i)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Now, let's create a dictionary{ } and do exactly the same as we did
# before with our tuple( ) and our list[ ] Python program examples.
# We are about to get our feet just a wee bit more wet this time.

class_arguments_dictionary = {1:'argument1',2:'argument2',3:'argument3'}

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

# If you don't have enough room to see the whole print( ) function text and or
# variables on one line, you can do the following.

print(
    Single_class(
    class_arguments_dictionary.get(1),  # dictionary key 1
    class_arguments_dictionary.get(2),  # dictionary key 2
    class_arguments_dictionary.get(3)   # dictionary key 3
    ).arg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a for loop that will loop through all the class argument variables
# and show all the class argument values on the screen with only one print( )
# function. Again, we will use a dictionary. However, we need to use the 'range( )
# function this time. The variable ' i ' won't work within the .get() function part,
# so we have to use the variable 'dictionary_loop.get(i+1)'. Why the variable ' i '
# does not work for the variable dictionary_loop is a complete mystery? However,
# this will only work if you don't have any other code blocks within the for loop.
# This will not work if you have other indented Python commands within the for
# loop.

class Single_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

dictionary_loop = (
    {1:Single_class('argument1','argument2','argument3').arg1,
     2:Single_class('argument1','argument2','argument3').arg2,
     3:Single_class('argument1','argument2','argument3').arg3})

# See how we drastically reduced our Python code, using a dictionary{ }
# with a for loop?

for i in range(3):print(dictionary_loop.get(i+1))

# I hope this helped you understand how to create classes with for loops
# using one, single 'print( )' function, which drastically reduces redundant
# Python code.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create classes with sub classes,
# along with a child class act. Keep this class scheme as something
# to easily memorize, which will help you when you need to refer to
# it. Note: you can create just one class if you like as well. This class
# scheme shows you the complete class sets, should you wish to use
# them all. I hope this will help those who are new to creating classes,
# such as myself am; I'm still pretty new to adapting to creating classes.
# You can also create as many sub classes as you please. Just make
# sure you give the child class act all the sub classes you create, along
# with the Main class, which comes first in your child class inheritance
# variables. Other than this, go Crazy and create your own class acts.

class Main_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class1:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class2:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class3:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class4:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class All_classes(
    Main_class,Sub_class1,
    Sub_class2,Sub_class3,
    Sub_class4): # Multi Inheritance

    def __init__(self,arg1,arg2,arg3):
        Main_class.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class1.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class2.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class3.__init__(self,arg1,arg2,arg3)  # inheritance
        Sub_class4.__init__(self,arg1,arg2,arg3)  # inheritance

print(Main_class('argument1','argument2','argument3').arg1)
print(Main_class('argument1','argument2','argument3').arg2)
print(Main_class('argument1','argument2','argument3').arg3)

print(Sub_class1('argument1','argument2','argument3').arg1)
print(Sub_class1('argument1','argument2','argument3').arg2)
print(Sub_class1('argument1','argument2','argument3').arg3)

print(Sub_class2('argument1','argument2','argument3').arg1)
print(Sub_class2('argument1','argument2','argument3').arg2)
print(Sub_class2('argument1','argument2','argument3').arg3)

print(Sub_class3('argument1','argument2','argument3').arg1)
print(Sub_class3('argument1','argument2','argument3').arg2)
print(Sub_class3('argument1','argument2','argument3').arg3)

print(Sub_class4('argument1','argument2','argument3').arg1)
print(Sub_class4('argument1','argument2','argument3').arg2)
print(Sub_class4('argument1','argument2','argument3').arg3)

print(All_classes('argument1','argument2','argument3').arg1)
print(All_classes('argument1','argument2','argument3').arg2)
print(All_classes('argument1','argument2','argument3').arg3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is a skeletal scheme of how to create classes with sub classes,
# along with a child class act. Keep this class scheme as something
# to easily memorize, which will help you when you need to refer to
# it. Note: you can create just one class if you like as well. This class
# scheme shows you the complete class sets, should you wish to use
# them all. I hope this will help those who are new to creating classes,
# such as myself am; I'm still pretty new to adapting to creating classes.
# You can also create as many sub classes as you please.

# The super( ) function reduces redundant Python code, so you can keep
# Python code nice and 'DRY!' ( "Don't Repeat Yourself!" )

class Main_class:
    def __init__(self,arg1,arg2,arg3):
        self.arg1=arg1  # attribute
        self.arg2=arg2  # attribute
        self.arg3=arg3  # attribute

class Sub_class1(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class Sub_class2(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class Sub_class3(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class Sub_class4(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

class All_classes(Main_class):  # class inheritance variable
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1,arg2,arg3)  # super() calls the __init__ method

print(Sub_class1('argument1','argument2','argument3').arg1)
print(Sub_class1('argument1','argument2','argument3').arg2)
print(Sub_class1('argument1','argument2','argument3').arg3)

print(Sub_class2('argument1','argument2','argument3').arg1)
print(Sub_class2('argument1','argument2','argument3').arg2)
print(Sub_class2('argument1','argument2','argument3').arg3)

print(Sub_class3('argument1','argument2','argument3').arg1)
print(Sub_class3('argument1','argument2','argument3').arg2)
print(Sub_class3('argument1','argument2','argument3').arg3)

print(Sub_class4('argument1','argument2','argument3').arg1)
print(Sub_class4('argument1','argument2','argument3').arg2)
print(Sub_class4('argument1','argument2','argument3').arg3)

print(All_classes('argument1','argument2','argument3').arg1)
print(All_classes('argument1','argument2','argument3').arg2)
print(All_classes('argument1','argument2','argument3').arg3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a class inheritance using only the class name 'Parent'.
# This will allow us to inherit properties from the Parent class to the
# inherited class called 'Inherit'. Any attributes in the Parent or main
# class are all passed onto the inherited class called 'Inherit'

class Person:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # fname attribute
        self.last_name=lname  # lname attribute
        self.age=age  # age attribute

# All we need to do is place the Person class name inside parentheses
# of the Inherit class act. If you don't want to use any code blocks within
# the Inherit class, simply invoke the 'pass' statement. Not shown here,
# but you can create as many inherited sub classes as you please. However,
# you must give them different names such as Inherit1 and Inherit2; you
# can name your classes any names you wish, but the first letter is always
# capitalized by Python programming standard, but you don't have to
# capitalize anything if you don't want to. Just keep the other square
# programmers happy and capitalize your class names so you don't get in
# trouble from the square boss.

class Inherit(Person):
    pass

my_variable1 = Person('John','Smith',23).first_name

my_variable2 = Inherit('Joe','Swift',23).first_name

print(my_variable1,my_variable2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Person:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # fname attribute
        self.last_name=lname  # lname attribute
        self.age=age  # age attribute

person1 = Person('John','Smith',32)
person2 = Person('Jane','Swift',29)
person3 = Person('Joan','White',26)

print(person1.first_name,person1.last_name,person1.age)

print(person2.first_name,person2.last_name,person2.age)

print(person3.first_name,person3.last_name,person3.age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a class that has def function( ) with attributes in it.
# Use the __init__( ) initialize constructor to be able to use the
# def function's attributes: self, fname, lname and age within
# the My_first_class_act Python program example. Note: you
# can call the word 'self' any name you wish, but Python
# programmers always, always use 'self' as a standard. The
# 'self' variable calls the def function( ) attributes. Thus, the
# def function( ) calls itself back up with 'self', along with its
# class attributes, which are inside the def function( ).

class My_first_class_act:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # fname attribute
        self.last_name=lname  # lname attribute
        self.age=age  # age attribute

print(My_first_class_act('John','Smith',19).first_name)

print(My_first_class_act('John','Smith',19).last_name)

print(My_first_class_act('John','Smith',19).age)

# Let's shorten some of these bulky print( ) functions using variables.

my_variable = My_first_class_act('John','Smith',19)

print(my_variable.first_name)

print(my_variable.last_name)

print(my_variable.age)

# Now we can keep things short and sweet with just one print( ) function.

print(my_variable.first_name,my_variable.last_name,my_variable.age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Grandmother class with other classes that can share her
# attributes. Use the super( ) function so you don't repeat any Python
# code inside other classes that share the same attribute variables
# alike. Also, you can create return def functions( ) that allow the
# other classes to use them as well. Note: return def functions( ) are
# optional; you don't need to use them with classes. But it's great
# to know that you can if you like, which also adds more functionality
# in your Python programs.

class Grandmother:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def grandmother(self):
        return 'I love you all!'
    def dog(self):
        return "Grandma's dog, Sparky."

class Mom(Grandmother):  # Mom class inherits Grandmother class
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

    def mom(self):
        return 'We love you two Mom!'
    def cat(self):
        return "Mom's fluffy cat."

class Daughter(Mom):  # Daughter class inherits Mom class
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

    def daughter(self):
        return 'High Grandma!'
    def fish(self):
        return "Daughter's Goldfish."

class Son(Daughter):   # Son class inherits Daughter class
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

    def son(self):
        return 'I love you Grandma!'
    def bird(self):
        return "Son's parrot."

# gain access to first_name attributes

print(Grandmother('Joan','Smith').first_name)

print(Mom('Jane','Smith').first_name)

print(Daughter('Jean','Smith').first_name)

print(Son('John','Smith').first_name)

# gain access to last_name attributes

print(Grandmother('Joan','Smith').last_name)

print(Mom('Jane','Smith').last_name)

print(Daughter('Jean','Smith').last_name)

print(Son('John','Smith').last_name)

# call def function( ) return values

print(Grandmother.grandmother('returned value'))

print(Mom.mom('returned value'))

print(Daughter.daughter('returned value'))

print(Son.son('returned value'))

# call def function( ) return values

print(Grandmother.grandmother('returned value'))

print(Mom.grandmother('returned value'))

print(Daughter.grandmother('returned value'))

print(Son.grandmother('returned value'))

# call def function( ) return values

print(Grandmother.grandmother('returned value'))

print(Mom.grandmother('returned value'))

print(Daughter.mom('returned value'))

print(Son.mom('returned value'))

print(Son.daughter('returned value'))

# call def function( ) return values

print(Grandmother.dog('returned value'))

print(Mom.cat('returned value'))

print(Daughter.fish('returned value'))

print(Son.bird('returned value'))

# call def function( ) return values

print(Grandmother.dog('returned value'))

print(Mom.dog('returned value'))

print(Daughter.dog('returned value'))

print(Son.dog('returned value'))

# call def function( ) return values

print(Grandmother.dog('returned value'))

print(Mom.dog('returned value'))

print(Daughter.cat('returned value'))

print(Son.cat('returned value'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create classes with return def functions() inside them and call each one up.

class Return_result_addition:
    def class_return_result_addition(num1,num2):
        return int(num1 + num2)

    addition = class_return_result_addition

print(Return_result_addition.addition(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_subtraction:
    def class_return_result_subtraction(num1,num2):
        return int(num1 - num2)

    subtraction = class_return_result_subtraction

print(Return_result_subtraction.subtraction(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_multiplication:
    def class_return_result_multiplication(num1,num2):
        return int(num1 * num2)

    multiplication = class_return_result_multiplication

print(Return_result_multiplication.multiplication(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_division:
    def class_return_result_division(num1,num2):
        return int(num1 / num2)

    division = class_return_result_division

print(Return_result_division.division(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_exponent:
    def class_return_result_exponent(num1,num2):
        return int(num1 ** num2)

    exponent = class_return_result_exponent

print(Return_result_exponent.exponent(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_power:
    def class_return_result_pow(num1,num2):
        return int(pow(num1,num2))

    power = class_return_result_pow

print(Return_result_power.power(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Child class that inherits all the other def functions of the
# upper parent class attributes.

class Inherit_return_result(
    Return_result_addition,
    Return_result_subtraction,
    Return_result_multiplication,
    Return_result_division,
    Return_result_exponent,
    Return_result_power):pass

print(Inherit_return_result.addition(8,2))  # call me up
print(Inherit_return_result.subtraction(8,2))  # call me up
print(Inherit_return_result.multiplication(8,2))  # call me up
print(Inherit_return_result.division(8,2))  # call me up
print(Inherit_return_result.exponent(8,2))  # call me up
print(Inherit_return_result.power(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's get lazy and shorten some Python code within the print() function
# with a tuple( ). Note: you can also create a list[ ] if you like, but a tuple( )
# is what we are using in our Python program example below.

class Inherit_return_result(
    Return_result_addition,
    Return_result_subtraction,
    Return_result_multiplication,
    Return_result_division,
    Return_result_exponent,
    Return_result_power):pass

class_inherit = (
              Inherit_return_result.addition,
              Inherit_return_result.subtraction,
              Inherit_return_result.multiplication,
              Inherit_return_result.division,
              Inherit_return_result.exponent,
              Inherit_return_result.power)

num1,num2 = 8,2  # variable and value packing with one equals = sign

print(class_inherit[0](num1,num2))  # call me up
print(class_inherit[1](num1,num2))  # call me up
print(class_inherit[2](num1,num2))  # call me up
print(class_inherit[3](num1,num2))  # call me up
print(class_inherit[4](num1,num2))  # call me up
print(class_inherit[5](num1,num2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's get real lazy and shorten some more Python code within the print( )
# function using a for loop to iterate through the 'class_inherit( ) tuple.

class Inherit_return_result(
    Return_result_addition,
    Return_result_subtraction,
    Return_result_multiplication,
    Return_result_division,
    Return_result_exponent,
    Return_result_power):pass

class_inherit = (
              Inherit_return_result.addition,
              Inherit_return_result.subtraction,
              Inherit_return_result.multiplication,
              Inherit_return_result.division,
              Inherit_return_result.exponent,
              Inherit_return_result.power)

num1,num2 = 8,2  # variable and value packing with one equals = sign

for i in class_inherit:print(i(num1,num2))  # call me up in a for loop

# Tip: remember to keep it DRY (Don't Repeat Yourself). Use a for loop
# to allow the use of just one print( ) function. That way, you can
# easily change your num1 and num2 values on the fly instead of
# having to change values in a bunch of repeated print( ) functions.

# Create classes with def functions() inside them and call each one up.

class Grandpa:
    def first_def_function_grandpa():
        print("I'm the first def function() within the Grampa class")
    def second_def_function_grandpa():
        print("I'm the second def function() within the Grandpa class")
    def third_def_function_grandpa():
         print("I'm the third def function() within the Grandpa class")

Grandpa.first_def_function_grandpa()  # call me up
Grandpa.second_def_function_grandpa()  # call me up
Grandpa.third_def_function_grandpa()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Grandma:
    def first_def_function_grandma():
        print("I'm the first def function() within the Grandma class")
    def second_def_function_grandma():
        print("I'm the second def function() within the Grandma class")
    def third_def_function_grandma():
        print("I'm the third def function() within the Grandma class")

Grandma.first_def_function_grandma()  # call me up
Grandma.second_def_function_grandma()  # call me up
Grandma.third_def_function_grandma()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Dad:
    def first_def_function_dad():
        print("I'm the first def function() within the Dad class")
    def second_def_function_dad():
        print("I'm the second def function() within the Dad class")
    def third_def_function_dad():
        print("I'm the third def function() within the Dad class")

Dad.first_def_function_dad()  # call me up
Dad.second_def_function_dad()  # call me up
Dad.third_def_function_dad()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Mom:
    def first_def_function_mom():
        print("I'm the first def function() within the Mom class")
    def second_def_function_mom():
        print("I'm the second def function() within the Mom class")
    def third_def_function_mom():
        print("I'm the third def function() within the Mom class")

Mom.first_def_function_mom()  # call me up
Mom.second_def_function_mom()  # call me up
Mom.third_def_function_mom()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a Child class that inherits all the other def functions of the
# upper parent class attributes.

class Child(Grandpa,Grandma,Dad,Mom): # four inherited variable parameters
    pass

Child.first_def_function_grandpa()  # call me up
Child.second_def_function_grandpa()  # call me up
Child.third_def_function_grandpa()  # call me up

Child.first_def_function_grandma()  # call me up
Child.second_def_function_grandma()  # call me up
Child.third_def_function_grandma()  # call me up

Child.first_def_function_dad()  # call me up
Child.second_def_function_dad()  # call me up
Child.third_def_function_dad()  # call me up

Child.first_def_function_mom()  # call me up
Child.second_def_function_mom()  # call me up
Child.third_def_function_mom()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's shorten these Python commands down using variables.

gpf1 = Child.first_def_function_grandpa
gpf2 = Child.second_def_function_grandpa
gpf3 = Child.third_def_function_grandpa

gpf1()  # call me up
gpf2()  # call me up
gpf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
gmf1 = Child.first_def_function_grandma
gmf2 = Child.second_def_function_grandma
gmf3 = Child.third_def_function_grandma

gmf1()  # call me up
gmf2()  # call me up
gmf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
df1 = Child.first_def_function_dad
df2 = Child.second_def_function_dad
df3 = Child.third_def_function_dad

df1()  # call me up
df2()  # call me up
df3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
mf1 = Child.first_def_function_mom
mf2 = Child.second_def_function_mom
mf3 = Child.third_def_function_mom

mf1()  # call me up
mf2()  # call me up
mf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create an immutable default tuple for loop of our class def functions, using the
# hard return backslash ' \ ' instead of using parentheses ' ( ) '

class_def_functions = \
                    Child.first_def_function_grandpa,\
                    Child.second_def_function_grandpa,\
                    Child.third_def_function_grandpa

for i in class_def_functions:
    i()

class_def_functions = \
                    Child.first_def_function_grandma,\
                    Child.second_def_function_grandma,\
                    Child.third_def_function_grandma

for i in class_def_functions:
    i()

class_def_functions = \
                    Child.first_def_function_dad,\
                    Child.second_def_function_dad,\
                    Child.third_def_function_dad

for i in class_def_functions:
    i()

class_def_functions = \
                    Child.first_def_function_mom,\
                    Child.second_def_function_mom,\
                    Child.third_def_function_mom

for i in class_def_functions:
    i()

class Grandma:
    def gm():
        print("I'm the Grandma class")

class Dad:
    def d():
        print("I'm the Dad class")

class Mom:
    def m():
        print("I'm the Mom class")

class Child(Grandpa,Grandma,Dad,Mom):
     def c():
         print('I\'m the Child class act')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Class inheritance with the print() function

class Grandpa:
    gp="I'm the Grandpa class"

class Grandma:
    gm="I'm the Grandma class"

class Dad:
    d="I'm the Dad class"

class Mom:
    m="I'm the Mom class"

class Child(Grandpa,Grandma,Dad,Mom):
     c='I\'m the Child class. I inherit all the other classes above me, as well as my own.'

print(Grandpa.gp)
print(Grandma.gm)
print(Dad.d)
print(Mom.m)

print(Child.gp)
print(Child.gm)
print(Child.d)
print(Child.m)
print(Child.c,"I have a copy of my own D&A")

# Use the 'pass' statement if you don't want any code blocks
# inside your Child class act.

class Grandpa:
    gp="I'm the Grandpa class"

class Grandma:
    gm="I'm the Grandma class"

class Dad:
    d="I'm the Dad class"

class Mom:
    m="I'm the Mom class"

class Child(Grandpa,Grandma,Dad,Mom):
     pass

print(Grandpa.gp)
print(Grandma.gm)
print(Dad.d)
print(Mom.m)

print(Child.gp)
print(Child.gm)
print(Child.d)
print(Child.m)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Class inheritance with the def function()

class Grandpa:
    def gp():
        print("I'm the Grandpa class")

class Grandma:
    def gm():
        print("I'm the Grandma class")

class Dad:
    def d():
        print("I'm the Dad class")

class Mom:
    def m():
        print("I'm the Mom class")

class Child(Grandpa,Grandma,Dad,Mom):
     def c():
         print('I\'m the Child class act')

Grandpa.gp()
Grandma.gm()
Dad.d()
Mom.m()

Child.gp()
Child.gm()
Child.d()
Child.m()
Child.c()

# Use the 'pass' statement if you don't want any code blocks
# inside your Child class act.

class Grandpa:
    def gp():
        print("I'm the Grandpa class")

class Grandma:
    def gm():
        print("I'm the Grandma class")

class Dad:
    def d():
        print("I'm the Dad class")

class Mom:
    def m():
        print("I'm the Mom class")

class Child(Grandpa,Grandma,Dad,Mom):
     pass

Grandpa.gp()
Grandma.gm()
Dad.d()
Mom.m()

Child.gp()
Child.gm()
Child.d()
Child.m()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a simple way to learn multi class inheritance. The first example will
# demonstrate this without the use of the super( ) function, and the next example
# will demonstrate the use of the super( ) function with class inheritance.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Child(Mom,Dad): # Multi Inheritance
    def __init__(self,name,age):
        Mom.__init__(self,name,age)  # inheritance
        Dad.__init__(self,name,age)  # inheritance

print(Mom('Jan',30).name)
print(Dad('John',35).age)

print(Child('Jan',30).name)
print(Child('John',35).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unlike the class example above, the super( ) function is very useful in that you
# don't have to repeat your class attributes in the 'Dad' class and the 'Child' class act.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad(Mom):  # class inheritance variable
     def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

class Child(Mom):  # class inheritance variable
    def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

print(Mom('Jan',30).name)
print(Dad('John',35).age)

print(Child('Jan',30).name)
print(Child('Joh',35).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Here is a simple way to learn multi class inheritance. The first example will
# demonstrate this without the use of the super( ) function, and the next example
# will demonstrate the use of the super( ) function with class inheritance.
# We will use variables this time for the print( ) functions.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Child(Mom,Dad): # Multi Inheritance
    def __init__(self,name,age):
        Mom.__init__(self,name,age)  # inheritance
        Dad.__init__(self,name,age)  # inheritance

variable1 = Mom('Jan',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jan',30).name
variable4 = Child('John',35).age

print(variable1)
print(variable2)
print(variable3)
print(variable4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Unlike the class example above, the super( ) function is very useful in that you
# don't have to repeat your class attributes in the 'Dad' class and the 'Child' class act.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute

class Dad(Mom):  # class inheritance variable
     def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

class Child(Mom):  # class inheritance variable
    def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method

variable1 = Mom('Jan',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jan',30).name
variable4 = Child('John',35).age

print(variable1)
print(variable2)
print(variable3)
print(variable4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This is the simplest way I could explain what the super( ) function does.
# Take a look at the two examples and you will see how the super( ) function
# makes it so you don't have to repeat all the class attributes in the Dad class

# Without the super( ) function, you would have to repeat your code.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28).first_name)

# This is much better as not to repeat your code using the super( ) function.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad(Mom):  # inheritance variable 'Mom'

    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)  # no repeated attributes

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28).first_name)

print(Mom('Jane','Smith',23).last_name)

print(Dad('John','Smith',28).last_name)

print(Mom('Jane','Smith',23).age)

print(Dad('John','Smith',28).age)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# As we did before, you can also add brand new attributes to the
# Dad class.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad(Mom):  # inheritance variable 'Mom'

    def __init__(self,fname,lname,age,fishing):
        super().__init__(fname,lname,age)
        self.fishing=fishing  # one brand new attribute

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28,'Trout').fishing)

print(Mom('Jane','Smith',23).last_name)

print(Dad('John','Smith',28,'Bass').fishing)

print(Mom('Jane','Smith',23).age)

print(Dad('John','Smith',28,'Pike').fishing)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a multiple inheritance class, called 'Child'. However,
# we cannot use the super( ) function here. In the Child class we
# only need to call the def __init__ parameters, without repeating
# our code. Although, we do have to repeat the Mom and Dad class
# code as shown below.

class Mom:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

class Dad:  # inheritance variable 'Mom'

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

# Make the Child class have one attribute of its own. However,
# the new Child class attribute 'playing' will only work with
# the Child class. If you try to make the attribute 'playing' work
# in the Mom and Dad class, it will not work. The Child class
# has its own attributes that will only work within that class act.

class Child(Mom,Dad):
    def __init__(self,fname,lname,age,play):
        Mom.__init__(self,fname,lname,age)
        Dad.__init__(self,fname,lname,age)
        self.playing=play  # one brand new attribute

print(Mom('Jane','Smith',23).first_name)

print(Dad('John','Smith',28).first_name)

print(Child('Tommy','Smith',3,'Toy Cars').first_name)

print(Child('Tommy','Smith',3,'Toy Cars').playing)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these class acts Python program examples with return statements.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute
    def mom(self):
        return "I'm still your Mom Son!"

class Dad:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute
    def dad(self):
        return "I'm still your Dad Son!"

class Child(Mom,Dad): # Multi Inheritance
    def __init__(self,name,age):
        Mom.__init__(self,name,age)  # inheritance
        Dad.__init__(self,name,age)  # inheritance
    def child(self):
        return "I'm still your Child, Mom and Dad!"

variable1 = Mom('Jane',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jane',30).name
variable4 = Child('John',35).age

variable5 = Mom('Jane',30).mom()
variable6 = Dad('John',35).dad()
variable7 = Child('Jane',30).mom()
variable8 = Child('John',35).dad()
variable9 = Child('George',10).child()

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable6)
print(variable7)
print(variable8)
print(variable9)

# You can also use these, via the return statements.

print(Mom.mom('placeholder'))  # return argument placeholder value
print(Dad.dad('placeholder'))  # return argument placeholder value
print(Child.mom('placeholder'))  # return argument placeholder value
print(Child.dad('placeholder'))  # return argument placeholder value
print(Child.child('placeholder'))  # return argument placeholder value

# Let's use variables to shrink down our print( ) functions.

variable1 = Mom.mom('placeholder')  # return argument placeholder value
variable2 = Dad.dad('placeholder')  # return argument placeholder value
variable3 = Child.mom('placeholder')  # return argument placeholder value
variable4 = Child.dad('placeholder')  # return argument placeholder value
variable5 = Child.child('placeholder')  # return argument placeholder value

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these class acts Python program examples with return statements.
# and the super( ) function. Note: the Child class has to call up the Dad class
# when using return statements and the super( ) function. The Child class
# calls up the Dad class and the Dad class calls up the Mom class. This allows
# the Child class to have full access to the Mom and Dad class; the Child calls
# the Dad class and the Dad class calls the Mom class.

class Mom:
    def __init__(self,name,age):
        self.name=name  # attribute
        self.age=age  # attribute
    def mom(self):
        return "I'm still your Mom Son!"

class Dad(Mom):  # call the Mom class inheritance variable
     def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method
     def dad(self):
         return "I'm still your Dad Son!"

class Child(Dad):  # call the Dad class inheritance variable
    def __init__(self,name,age):
        super().__init__(name,age)  # super() calls the __init__ method
    def child(self):
        return "I'm still your Child, Mom and Dad!"

# Let's use variables to shrink down our print( ) functions.

variable1 = Mom('Jan',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jan',30).name
variable4 = Child('John',35).age

print(variable1)
print(variable2)
print(variable3)
print(variable4)

# Let's use variables to shrink down our print( ) functions.

variable1 = Mom('Jane',30).name
variable2 = Dad('John',35).age
variable3 = Child('Jane',30).name
variable4 = Child('John',35).age

variable5 = Mom('Jane',30).mom()
variable6 = Dad('John',35).dad()
variable7 = Child('Jane',30).mom()
variable8 = Child('John',35).dad()
variable9 = Child('George',10).child()

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable6)
print(variable7)
print(variable8)
print(variable9)

# You can also use these, via the return statements.
# Let's use variables to shrink down our print( ) functions.

variable1 = Mom.mom('placeholder')  # return argument placeholder value
variable2 = Dad.dad('placeholder')  # return argument placeholder value
variable3 = Child.mom('placeholder')  # return argument placeholder value
variable4 = Child.dad('placeholder')  # return argument placeholder value
variable5 = Child.child('placeholder')  # return argument placeholder value

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with argument def function( ) examples.

class Function:
    def arg_funct(fname,lname,age):
        print(fname,lname,age)

Function.arg_funct('John','Smith',30)

# return one value with the return statement.

class Function:
    def arg_funct(fname,lname,age):
        return fname  # return each argument variable one at a time

print(Function.arg_funct('John','Smith',30))

class Function:
    def arg_funct(fname,lname,age):
        return lname  # return each argument variable one at a time

print(Function.arg_funct('John','Smith',30))

class Function:
    def arg_funct(fname,lname,age):
        return age  # return each argument variable one at a time

print(Function.arg_funct('John','Smith',30))

# create a variable 'x' to return one value with the return statement.

class Function:
    def arg_funct(fname,lname,age):
        return fname  # return each argument variable one at a time as shown above

x = Function.arg_funct('John','Smith',30)

print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with attributes and return argument
# def functions( ), along with a 'child' class act Python program example.

class Return_class_function1:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct1(fname,lname,age):
        return fname  # return each argument variable one at a time

class Return_class_function2:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct2(fname,lname,age):
        return lname  # return each argument variable one at a time

class Return_class_function3:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct3(fname,lname,age):
        return age  # return each argument variable one at a time

class Return_all_class_functions(
    Return_class_function1,
    Return_class_function2,
    Return_class_function3):

    def __init__(self,fname,lname,age):
        Return_class_function1.__init__(first_name,last_name,age)  # inheritance
        Return_class_function2.__init__(first_name,last_name,age)  # inheritance
        Return_class_function3.__init__(first_name,last_name,age)  # inheritance

# print out each individual class by themselves

print(Return_class_function1.arg_funct1('Jane','Smith',30))
print(Return_class_function2.arg_funct2('John','Smith',35))
print(Return_class_function3.arg_funct3('Ron','Smith',10))

# print out the Return_all_class_functions child class acts

print(Return_all_class_functions.arg_funct1('Jane','Smith',30))
print(Return_all_class_functions.arg_funct2('John','Smith',35))
print(Return_all_class_functions.arg_funct3('Ron','Smith',10))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with attributes and return argument
# def functions( ), along with a 'child' class act Python program example.

class Return_class_function1:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct1(fname,lname,age):
        return fname  # return each argument variable one at a time

class Return_class_function2:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct2(fname,lname,age):
        return lname  # return each argument variable one at a time

class Return_class_function3:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct3(fname,lname,age):
        return age  # return each argument variable one at a time

class Return_all_class_functions(
    Return_class_function1,
    Return_class_function2,
    Return_class_function3):

    def __init__(self,fname,lname,age):
        Return_class_function1.__init__(first_name,last_name,age)  # inheritance
        Return_class_function2.__init__(first_name,last_name,age)  # inheritance
        Return_class_function3.__init__(first_name,last_name,age)  # inheritance
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now create three tuples called fnames, lnames and ages to use within
# 'zip( )' functions. Here are three separate zip( ) function examples for the three
# individual classes.

fnames = 'Jane','John','Ron'
lnames = 'Smith','Smith','Smith'
ages = 30,35,10

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function1.arg_funct1(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function2.arg_funct2(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function3.arg_funct3(index1,index2,index3))

# Here are three separite zip( ) function examples for the three child class acts.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct1(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct2(index1,index2,index3))

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct3(index1,index2,index3))

# Let's shrink down these Python program examples, using just one zip( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_class_function1.arg_funct1(index1,index2,index3))
    print(Return_class_function2.arg_funct2(index1,index2,index3))
    print(Return_class_function3.arg_funct3(index1,index2,index3))

# Let's shrink down these Python program examples, using just one zip( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(Return_all_class_functions.arg_funct1(index1,index2,index3))
    print(Return_all_class_functions.arg_funct2(index1,index2,index3))
    print(Return_all_class_functions.arg_funct3(index1,index2,index3))

# Let's shrink down this Python program even more, with just one print( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(
        Return_class_function1.arg_funct1(index1,index2,index3),
        Return_class_function2.arg_funct2(index1,index2,index3),
        Return_class_function3.arg_funct3(index1,index2,index3))

# Let's shrink down this Python program even more, with just one print( ) function.

for index1,index2,index3 in zip(fnames,lnames,ages):
    print(
        Return_all_class_functions.arg_funct1(index1,index2,index3),
        Return_all_class_functions.arg_funct2(index1,index2,index3),
        Return_all_class_functions.arg_funct3(index1,index2,index3))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some classes with attributes and return argument
# def functions( ), along with a 'child' class act Python program example.

class Return_class_function1:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct1(fname,lname,age):
        return fname  # return each argument variable one at a time

class Return_class_function2:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct2(fname,lname,age):
        return lname  # return each argument variable one at a time

class Return_class_function3:

    def __init__(self,fname,lname,age):
        self.first_name=fname  # attribute
        self.last_name=lname  # attribute
        self.age=age  # attribute

    def arg_funct3(fname,lname,age):
        return age  # return each argument variable one at a time

class Return_all_class_functions(
    Return_class_function1,
    Return_class_function2,
    Return_class_function3):

    def __init__(self,fname,lname,age):
        Return_class_function1.__init__(first_name,last_name,age)  # inheritance
        Return_class_function2.__init__(first_name,last_name,age)  # inheritance
        Return_class_function3.__init__(first_name,last_name,age)  # inheritance
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's now create three tuples called fnames, lnames and ages to use within
# 'enumerate( )' functions. Here are three separate enumerate( ) function examples
# for the three individual classes.

fnames = 'Jane','John','Ron'
lnames = 'Smith','Smith','Smith'
ages = 30,35,10

for index,fname_lname_age in enumerate(fnames):
    print(Return_class_function1.arg_funct1(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(lnames):
    print(Return_class_function2.arg_funct2(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(ages):
    print(Return_class_function3.arg_funct3(
        fname_lname_age,fname_lname_age,fname_lname_age))

# Let's use the child class acts to do as we did in the examples above.

for index,fname_lname_age in enumerate(fnames):
    print(Return_class_function1.arg_funct1(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(lnames):
    print(Return_class_function2.arg_funct2(
        fname_lname_age,fname_lname_age,fname_lname_age))

for index,fname_lname_age in enumerate(ages):
    print(Return_class_function3.arg_funct3(
        fname_lname_age,fname_lname_age,fname_lname_age))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python scoping with strings and integer values

# Python can show you what 'type' of string, integer and float values
# you are using to help you understand what 'str', 'int', and 'float values
# are.

print(type('text string'))  # <class 'str'>

print(type(1))  # <class 'int'>

print(type(1.0))  # <class 'float'>
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Python scoping with strings and integer values

# The 'dir( )' function shows you the complete directory of what you can
# use within Python programs you create. Type and execute/run these
# simple Python program examples and study the screen output.

print(dir('text string'))

print(dir(1))

print(dir(1.0))

# Get the id from a string.

print(id('string'))

# Get the id from an integer.

print(id(2))

# Type help() for interactive help, or help(object) for help about object.

print(help)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the 'dir( ) function with nothing inside the parentheses

print(dir())

# screen output:
'''
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__']
'''
# Use the 'dir( ) function with a number inside the parentheses

print(dir(1))

# screen output:
'''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__',
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__',
'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
'__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
'__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
'__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
'__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
'__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
'imag', 'numerator', 'real', 'to_bytes']
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use the __str__ dunder method for text strings.

print(str.__str__('text string'))

# Use the __repr__ dunder method to represent integer and float strings.

print(int.__repr__(8+2))

print(float.__repr__(8.0+2.0))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Use these dunder methods to calculate numbers, such as integers and floats.

print(int.__add__(8,2))  # equals 10

print(int.__sub__(8,2))  # equals 6

print(int.__mul__(8,2))  # equals 16

print(int.__floordiv__(8,2))  # equals 4

print(int.__pow__(8,2))  # equals 64


print(float.__add__(8.0,2.0))  # equals 10.0

print(float.__sub__(8.0,2.0))  # equals 6.0

print(float.__mul__(8.0,2.0))  # equals 16.0

print(float.__floordiv__(8.0,2.0))  # equals 4.0

print(float.__pow__(8.0,2.0))  # equals 64.0
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy Python program practice examples for those who might be stuck
# with some Python program examples I've demonstrated. Experiment
# with these Python program practice examples for yourself and refer to
# any of my Python programming research to expand your Python
# programming skills. However, these Python program examples do get
# harder as you learn them. Because, after all, that's what any type of
# computer programming skills are all about. I started you off in shallow
# waters, but I gradually take you into much deeper waters. Soon, we will
# venture into the Mariana's Trench; into the Abyss. Are you ready to
# jump into infinity? I know I am. Shall we go!?

print("Python Programmer's Glossary Bible")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
variable = "Python Programmer's Glossary Bible"

print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print(1+2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
variable = 1+2

print(variable)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_tuple = ('Python',"Programmer's",'Glossary','Bible')

print(my_tuple[0],my_tuple[1],my_tuple[2],my_tuple[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_list = ['Python',"Programmer's",'Glossary','Bible']

print(my_list[0],my_list[1],my_list[2],my_list[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
my_dictionary = {
    'key1':'Python','key2':"Programmer's",'key3':'Glossary','key4':'Bible'}

print(my_dictionary.get('key1'))

print(my_dictionary.get('key5','Key Not Found!'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def book():
    print("Python Programmer's Glossary Bible")

book()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_book(self):
    return "Python Programmer's Glossary Bible"

print(return_book('by Joseph C. Richardson'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_sum(self):
    return 1+2

print(return_sum("Python Programmer's Glossary Bible"))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_sum(num1,num2):
    return num1+num2

print(return_sum(1,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Book:
    def book():
        print("Python Programmer's Glossary Bible")

Book.book()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Sum:
    def addition():
        print(1+2)

Sum.addition()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Book:
    def return_book(self):
        return "Python Programmer's Glossary Bible"

print(Book.return_book('by Joseph C. Richardson'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Sum:
    def return_sum(self):
        return 1+2

print(Sum.return_sum("Python Programmer's Glossary Bible"))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Sum:
    def return_sum(num1,num2):
        return num1+num2

print(Sum.return_sum(1,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute

print(Attributes('argument1','argument2','argument3').attribute1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute
    def return_book(name):
        return "Python Programmer's Glossary Bible"

print(Attributes('argument1','argument2','argument3').attribute1)

print(Attributes.return_book('by Joseph C. Richardson'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute
    def return_sum(num1,num2):
        return num1+num2

print(Attributes('argument1','argument2','argument3').attribute1)

print(Attributes.return_sum(1,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes1:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute

class Attributes2:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute

class Inheritance(Attributes1,Attributes2):  # inheritance variables
    def __init__(self,attribute1,attribute2,attribute3):
        Attributes1.__init__(self,attribute1,attribute2,attribute3)  # inheritance
        Attributes2.__init__(self,attribute1,attribute2,attribute3)  # inheritance

print(Attributes1('argument1','argument2','argument3').attribute1)

print(Attributes2('argument1','argument2','argument3').attribute2)

print(Inheritance('argument1','argument2','argument3').attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes1:
    def __init__(self,attribute1,attribute2,attribute3):  # inheritance variables
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute
    def return_book(name):
        return "Python Programmer's Glossary Bible"

class Attributes2:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute
    def return_sum(num1,num2):
        return num1+num2

class Inheritance(Attributes1,Attributes2):
    def __init__(self,attribute1,attribute2,attribute3):
        Attributes1.__init__(self,attribute1,attribute2,attribute3)  # inheritance
        Attributes2.__init__(self,attribute1,attribute2,attribute3)  # inheritance

print(Attributes1('argument1','argument2','argument3').attribute1)

print(Attributes2('argument1','argument2','argument3').attribute2)

print(Inheritance('argument1','argument2','argument3').attribute3)

print(Attributes1.return_book('by Joseph C. Richardson'))

print(Attributes2.return_sum(1,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes1:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute

class Attributes2(Attributes1):  # inheritance variable
    def __init__(self,attribute1,attribute2,attribute3):
        super().__init__(attribute1,attribute2,attribute3)  # super() calls the __init__ method

print(Attributes1('argument1','argument2','argument3').attribute1)

print(Attributes2('argument1','argument2','argument3').attribute2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes1:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute
    def return_book(name):
        return "Python Programmer's Glossary Bible"

class Attributes2(Attributes1):  # inheritance variable
    def __init__(self,attribute1,attribute2,attribute3):
        super().__init__(attribute1,attribute2,attribute3)  # super() calls the __init__ method

print(Attributes1('argument1','argument2','argument3').attribute1)

print(Attributes2('argument1','argument2','argument3').attribute2)

print(Attributes1.return_book('by Joseph C. Richardson'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Attributes1:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1=attribute1  # attribute
        self.attribute2=attribute2  # attribute
        self.attribute3=attribute3  # attribute
    def return_sum(num1,num2):
        return num1+num2

class Attributes2(Attributes1):  # inheritance variable
    def __init__(self,attribute1,attribute2,attribute3):
        super().__init__(attribute1,attribute2,attribute3)  # super() calls the __init__ method

print(Attributes1('argument1','argument2','argument3').attribute1)

print(Attributes2('argument1','argument2','argument3').attribute2)

print(Attributes1.return_sum(1,2))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
Python clock functions allow you to program the actual time in real time.
Python clock functions work internally, in sync with the Windows clock.
With Python clock functions; you can set the hour, minute, second, month,
week, day and date. See Python clock function prefix descriptions below.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# To get the ASCII code value of any letter or number key, simply type and
# execute/run the program examples below and see what happens. Try using
# different letters and numbers to see their ASCII code values.

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# express binary, octal and hexadecimal numbers with these Python
# program examples

print(bin(255))  # 0b11111111

print(oct(255))  # 0o377

print(hex(255))  # 0xff

# or these:

print(f'{255:b}')  # 11111111

print(f'{255:o}')  # 377

print(f'{255:x}')  # ff
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Things you can do with digital computer numbers. Use these
# with tuples, lists, dectionaries and sets.

digital_dictionary = {'bin1': f'{0:b}','bin2': f'{15:b}','bin3': f'{255:b}'}

print(digital_dictionary.get('bin1'))  # 0 bytes

print(digital_dictionary.get('bin2'))  # 1111 = 15, half byte

print(digital_dictionary.get('bin3'))  # 11111111 = 255, one full eight bit byte

# prefixes:

# f'{255:b}' binary

# f'{255:x}' hexadecimal

# f'{255:o}' octal

# and these if you like:

# bin(255) binary

# hex(255) hexadecimal

# oct(255) octal
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
digital_set = {f'{0:b}',f'{15:b}',f'{255:b}'}

print(digital_set)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type any number, or numbers you wish and Python will translate them
# into binary, hexadecimal, octal to human readable decimal numbers.
# For brand new programmers, this is a must to learn, so let Python teach
# you how to read computer numbers.

redundant_code='''
question = input('Do you wish to continue? Enter for Y, N for No: ').lower().strip()'''

while True:
    try:
        user_input = int(input('Type any number and I will translate it for you: ').strip())

        if user_input == 0:
            print('zero bits')
            exec(redundant_code)
        elif user_input == 1:
            print(len(f'{user_input:b}'),
                  f'bit = {user_input:b} = {user_input:x} = {user_input:o} = decimal: {user_input}')
            exec(redundant_code)
        elif user_input > 1:
            print(len(f'{user_input:b}'),
                  f'bits = {user_input:b} = {user_input:x} = {user_input:o} = decimal: {user_input}')
            exec(redundant_code)
        if question == 'n':
            break
        else:
            continue
   
    except ValueError:
        print('Numbers only please: ')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Type any number, or numbers you wish and Python will translate them
# into binary, hexadecimal, octal to human readable decimal numbers.
# For brand new programmers, this is a must to learn, so let Python teach
# you how to read computer numbers.

# define function( ) example:

def digital_translator():
    
    while True:
        try:
            user_input = int(input('Type any number and I will translate it for you: ').strip())

            if user_input == 0:
                print('zero bits')
                question = input('Do you wish to continue? Enter for Y, N for No: ').lower().strip()
            elif user_input == 1:
                print(len(f'{user_input:b}'),
                      f'bit = {user_input:b} = {user_input:x} = {user_input:o} = decimal: {user_input}')
                question = input('Do you wish to continue? Enter for Y, N for No: ').lower().strip()
            elif user_input > 1:
                print(len(f'{user_input:b}'),
                      f'bits = {user_input:b} = {user_input:x} = {user_input:o} = decimal: {user_input}')
                question = input('Do you wish to continue? Enter for Y, N for No: ').lower().strip()
            if question == 'n':
                break
            else:
                continue
       
        except ValueError:
            print('Numbers only please: ')
            
digital_translator()  # call the digital_translator() function
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Welcome to the Binary Beat in Motion Python program example:

from time import sleep as delay;import os;os.system('title Binary Beat')

red='\x1b[31m'
green='\x1b[32m'
blue='\x1b[34m'
yellow='\x1b[33m'
purple='\x1b[35m'
white='\x1b[37m'
os.system('cls')
n=0

while True:
    print(white+'\n'+' '*6+'welcome to the binary beat in motion python program example'.title()
          +yellow+'\n\n'+' '*6+'1     1    1    1    1   1   1   1 = eight bits or one byte'
          +'\n\n'+' '*6+'128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = decimal number: 255''\n\n'+' '*2
          +'binary base: 2, octal base: 8, hexadecimal base: 16, decimal base: 10'.title()
          +'\n\n'+' '*3+yellow,len(f'{n:b}'),green+'binary digits: '.title()
          +yellow+f'{n:b} '+red+'=\n\n'+' '*3+yellow,len(f'{n:o}'),green+'octal digits: '.title()
          +yellow+f'{n:o} '+red+'=\n\n'+green+' '*3+yellow,len(f'{n:x}'),green+'hexadecimal digits: '.title()
          +yellow+f'{n:X} '+red+'= '+green+'\n\n'+' '*3+yellow,len(f'{n:d}'),green+'decimal digits: '.title()
          +red+'= '+yellow+f'{n:d}');delay(1);os.system('cls');n+=1

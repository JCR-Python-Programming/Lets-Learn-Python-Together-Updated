# Here are some ways to create return define functions in
# Python. Please note: there are no comments about these
# Python program experiments below. This is how I do most
# of my computer programming experiments in Python. I
# don't always place comments into programs I create, until
# I'm happy with my computer programming experiments
# first. As for right now, I'm just too darn lazy to write a bunch
# comments about what these Python program experiments
# do. I'll leave that all up to YOU to tinker with these Python
# program experiments for yourself.

def return_function_name_values(name1,name2,name3,name4,name5):

    return 'Rob','Bob','Tom','Terry','Mary'

print(return_function_name_values(
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',)[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_name_values(name1,name2,name3,name4,name5):

    return 'Rob','Bob','Tom','Terry','Mary'

tuple_var = return_function_name_values(
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value')

print(f'Hi {tuple_var[0]}. How are you?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_name_values(name1,name2,name3,name4,name5):

    return 'Rob','Bob','Tom','Terry','Mary'

tuple_var = return_function_name_values(
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value',
    'argument placeholder value')

for i in tuple_var:
    print(f'Hi {i}. How are you?')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values():

    return 1+2,2-1,5*2,10/5

print(return_function_number_values()[0])

print(int(return_function_number_values()[0]))

print(float(return_function_number_values()[0]))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2*num3+num4-num5

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2*num3

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2*num3+num4-num5+num4-num1

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return num1+num2**num3/num2

print(return_function_number_values(1,2,3,4,5))

print(int(return_function_number_values(1,2,3,4,5)))

print(float(return_function_number_values(1,2,3,4,5)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return int(num3**num2+num3-num4+num1*num5*2/num2)

tuple_var = return_function_number_values(1,2,3,4,5)

print(tuple_var)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_number_values(num1,num2,num3,num4,num5):

    return float(num3**num2+num5)

tuple_var = return_function_number_values(1,2,3,4,5)

print(tuple_var)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num5

print(return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num1,bin_num2,bin_num3,bin_num4,bin_num5

print(return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}')[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num1,bin_num2,bin_num3,bin_num4,bin_num5

binary_num = return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}')[4]

print(binary_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num1,bin_num2,bin_num3,bin_num4,bin_num5

binary_num = return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{5:b}')

print(binary_num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num5

print(return_function_hexadecimal_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num1,hex_num2,hex_num3,hex_num4,hex_num5

print(return_function_hexadecimal_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}')[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num1,hex_num2,hex_num3,hex_num4,hex_num5

hexadecimal_num = return_function_binary_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}')[4]

print(hexadecimal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num1,hex_num2,hex_num3,hex_num4,hex_num5

hexadecimal_num = return_function_binary_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{5:x}')

print(hexadecimal_num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num5

print(return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num1,oct_num2,oct_num3,oct_num4,oct_num5

print(return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}')[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num1,oct_num2,oct_num3,oct_num4,oct_num5

octal_num = return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}')[4]

print(octal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num1,oct_num2,oct_num3,oct_num4,oct_num5

octal_num = return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{5:o}')

print(octal_num[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_binary_number_values(bin_num1,bin_num2,bin_num3,bin_num4,bin_num5):

    return bin_num5

binary_num = return_function_binary_number_values(f'{1:b}',f'{2:b}',f'{3:b}',f'{4:b}',f'{250+5:b}')

print(binary_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_hexadecimal_number_values(hex_num1,hex_num2,hex_num3,hex_num4,hex_num5):

    return hex_num5

hexadecimal_num = return_function_hexadecimal_number_values(f'{1:x}',f'{2:x}',f'{3:x}',f'{4:x}',f'{250+5:x}')

print(hexadecimal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def return_function_octal_number_values(oct_num1,oct_num2,oct_num3,oct_num4,oct_num5):

    return oct_num5

octal_num = return_function_octal_number_values(f'{1:o}',f'{2:o}',f'{3:o}',f'{4:o}',f'{250+5:o}')

print(octal_num)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

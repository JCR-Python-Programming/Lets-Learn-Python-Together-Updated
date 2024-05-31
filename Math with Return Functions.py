# Here are some easy ways to create math operations with return functions.

def addition(num1,num2):
    return num1 + num2 # num1 = 5, and num2 = 4

print(addition(5,4)) # These are the actual values

def subtraction(num1,num2):
    return num1 - num2 # num1 = 5, and num2 = 4

print(subtraction(5,4)) # These are the actual values

def addition(num1,num2):
    return num1 + num2 # num1 = 5, and num2 = 4

print(addition(5,4)) # These are the actual values

def multiplication(num1,num2):
    return num1 * num2 # num1 = 5, and num2 = 4

print(multiplication(5,4)) # These are the actual values

def division(num1,num2):
    return num1 / num2 # num1 = 5, and num2 = 4

print(division(5,4)) # These are the actual values

def exponents(num1,num2):
    return num1 ** num2 # num1 = 5, and num2 = 4

print(exponents(5,4)) # These are the actual values. five to the same power of four (5 * 5 * 5 * 5) = 625

# You can also use the pow() function instead of the double asterisks **

def pow_expon(num1,num2):
    return pow(num1,num2) # num1 = 5, and num2 = 4

print(pow_expon(5,4)) # These are the actual values. five to the same power of four (5 * 5 * 5 * 5) = 625

# The sum() function can only be used with a tuple or a list. This tuple below
# is a 'default tuple'; parentheses are not used with default tuples. Any list of
# anything, text or numbers without parentheses is a tuple by default, regardless.
# Tuples are not mutable; they cannot be changed or modified in the same way
# lists[ ] can. Therefore, tuples are immutable; they cannot be changed or modified.

add_nums = 1,2,3,4,5,6,7,8,9  # default tuple
print(sum(add_nums))  # equals '45'

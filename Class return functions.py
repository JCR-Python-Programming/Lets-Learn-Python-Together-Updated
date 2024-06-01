# Create classes with return def functions() inside them and call each one up.

class Return_result_addition:
    def class_return_result_addition(num1,num2):
        return int(num1 + num2)

    addition = class_return_result_addition

print(Return_result_addition.addition(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_subtraction:
    def class_return_result_subtraction(num1,num2):
        return int(num1 - num2)

    subtraction = class_return_result_subtraction

print(Return_result_subtraction.subtraction(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_multiplication:
    def class_return_result_multiplication(num1,num2):
        return int(num1 * num2)

    multiplication = class_return_result_multiplication

print(Return_result_multiplication.multiplication(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_division:
    def class_return_result_division(num1,num2):
        return int(num1 / num2)

    division = class_return_result_division

print(Return_result_division.division(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_exponent:
    def class_return_result_exponent(num1,num2):
        return int(num1 ** num2)

    exponent = class_return_result_exponent

print(Return_result_exponent.exponent(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Return_result_power:
    def class_return_result_pow(num1,num2):
        return int(pow(num1,num2))

    power = class_return_result_pow

print(Return_result_power.power(8,2))  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Create a child class that inherits all the other def functions of the
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

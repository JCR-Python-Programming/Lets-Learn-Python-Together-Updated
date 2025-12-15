import math

class Addition:
    def addition(num1,num2):
        print('Addition',end=f': {num1} + {num2} = ')
        return num1+num2

class Subtraction:
    def subtraction(num1,num2):
        print('Subtraction',end=f': {num1} - {num2} = ')
        return num1-num2

class Multiplication:
    def multiplication(num1,num2):
        print('Multiplication',end=f': {num1} x {num2} = ')
        return num1*num2

class Division:
    def division(num1,num2):
        print('Division',end=f': {num1} / {num2} = ')
        return num1/num2

class Exponent:
    def exponent(num1,num2):
        print('Exponent',end=f': {num1} exp {num2} = ')
        return num1**num2

class Root:
    def root(num):
        print('Root',end=f': {num} = ')
        return math.sqrt(num)

print(Addition.addition(4,2))

print(Subtraction.subtraction(4,2))

print(Multiplication.multiplication(4,2))

print(Division.division(4,2))

print(Exponent.exponent(4,2))

print(Root.root(4))

class Math(
    Addition,Subtraction,
    Multiplication,Division,
    Exponent,Root):pass

print(Math.addition(4,2))

print(Math.subtraction(4,2))

print(Math.multiplication(4,2))

print(Math.division(4,2))

print(Math.exponent(4,2))

print(Math.root(4))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
      user_input = int(input('Give me an odd or even number: ').strip())

      if user_input%2 == 0:
        print(f'{user_input} is an even number.')
        break
      else:
        print(f'{user_input} is an odd number.')
        break
    except ValueError:
      print('Numbers only please:')

# Let's create a class inheritance using only the class name 'Person'.
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

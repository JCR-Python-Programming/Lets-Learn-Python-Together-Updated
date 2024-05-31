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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's shorten these Python commands down using variables

gpf1 = Child.first_def_function_grandpa
gpf2 = Child.second_def_function_grandpa
gpf3 = Child.third_def_function_grandpa

gpf1()  # call me up
gpf2()  # call me up
gpf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
gmf1 = Child.first_def_function_grandma
gmf2 = Child.second_def_function_grandma
gmf3 = Child.third_def_function_grandma

gmf1()  # call me up
gmf2()  # call me up
gmf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
df1 = Child.first_def_function_dad
df2 = Child.second_def_function_dad
df3 = Child.third_def_function_dad

df1()  # call me up
df2()  # call me up
df3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
mf1 = Child.first_def_function_mom
mf2 = Child.second_def_function_mom
mf3 = Child.third_def_function_mom

mf1()  # call me up
mf2()  # call me up
mf3()  # call me up
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create an immutable default tuple for loop of our class def functions, using
# the hard return backslash ' \ ' instead of using parentheses ' ( ) '

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

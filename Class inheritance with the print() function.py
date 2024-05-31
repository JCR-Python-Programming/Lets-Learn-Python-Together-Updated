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

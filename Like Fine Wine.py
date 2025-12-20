
class Main:

    def __init__(self,par1,par2,par3):

        self.parameter1 = par1
        self.parameter2 = par2
        self.parameter3 = par3

    def Testing1():
        print('Testing1, Testing1')

class Super1(Main):

    def __init__(self,parameter1,parameter2,parameter3,par4):
        super().__init__(parameter1,parameter2,parameter3)

        self.parameter4 = par4

class Super2(Super1):

    def __init__(self,parameter1,parameter2,parameter3,parameter4,par5):
        super().__init__(parameter1,parameter2,parameter3,parameter4)

        self.parameter5 = par5

class Super3(Super2):

    def __init__(self,parameter1,parameter2,parameter3,parameter4,parameter5,par6):
        super().__init__(parameter1,parameter2,parameter3,parameter4,parameter5)

        self.parameter6 = par6

class Super4(Super3):

    def __init__(self,parameter1,parameter2,parameter3,parameter4,parameter5,parameter6,par7):
        super().__init__(parameter1,parameter2,parameter3,parameter4,parameter5,parameter6)

        self.parameter7 = par7

class Sub:
    def Testing2():
        print('Testing2, Testing2')

class Child(Sub,Main):
    pass

text1 = Main('parameter1','parameter2','parameter3').parameter3

text2 = Super1('parameter1','parameter2','parameter3','parameter4').parameter4

text3 = Super2('parameter1','parameter2','parameter3','parameter4','parameter5').parameter5

text4 = Super3('parameter1','parameter2','parameter3','parameter4','parameter5','parameter6').parameter6

text5 = Super4('parameter1','parameter2','parameter3','parameter4','parameter5','parameter6','parameter7').parameter7

Child.Testing1()
Child.Testing2()

text6 = Main

print(text1)

print(text2)

print(text3)

print(text4)

print(text5)

print([cls.__name__ for cls in Super4.mro()])

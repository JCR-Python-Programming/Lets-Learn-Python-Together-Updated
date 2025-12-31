
class Main:
    def __init__(self,*args):

        self.args = args

class sub(Main):pass

print(Main('argument1','argument2','argument3').args[0])

print(sub('argument1','argument2','argument3').args[1])

class Main:
    def __init__(self,**kwargs):

        self.kwargs = kwargs        

class sub(Main):pass

lazy1 = Main(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

print(lazy1.kwargs.get('kw_arg4','Attribute does not exist'))


class Main:
    def __init__(self,**kwargs):

        self.__dict__.update(kwargs)

class Sub(Main):pass

lazy2 = Main(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')
 
print(lazy2.kw_arg1)


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

'''
0 EOR 0 = 0 (They are the same)
1 EOR 1 = 0 (They are different!)
1 EOR 0 = 1 (They are the same)
0 EOR 1 = 1 (They are different!)
'''

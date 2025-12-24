
class Mom:
    def __init__(self, mom1, mom2, mom3):
        self.mom1 = mom1
        self.mom2 = mom2
        self.mom3 = mom3

class Dad:
    def __init__(self, dad1, dad2, dad3):
        self.dad1 = dad1
        self.dad2 = dad2
        self.dad3 = dad3

class Child(Dad, Mom):
    def __init__(self, dad1, dad2, dad3, mom1, mom2, mom3):
        Dad.__init__(self, dad1, dad2, dad3)
        Mom.__init__(self, mom1, mom2, mom3)

mom = Mom('Test1', 'Test2', 'Test3')

dad = Dad('Test1', 'Test2', 'Test3')

child = Child('Test1', 'Test2', 'Test3','Test4', 'Test5', 'Test6')

print(mom.mom1)

print(dad.dad1)

print(child.dad1)

print(child.mom1)

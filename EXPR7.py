class Mom:
    def __init__(self, mom1,mom2,mom3):
        self.mom1 = mom1
        self.mom2 = mom2
        self.mom3 = mom3

class Dad:
    def __init__(self,dad1,dad2,dad3):
        self.dad1 = dad1
        self.dad2 = dad2
        self.dad3 = dad3

class Child(Mom):
    def __init__(self,dad1,dad2,dad3,mom1,mom2,mom3):
        Mom.__init__(self,mom1,mom2,mom3)
        Dad.__init__(self,dad1,dad2,dad3)

mom = Mom('Mom1','Mom2','Mom3')

dad = Dad('Dad1', 'Dad2','Dad3')

child = Child('Dad1','Dad2','Dad3','Mom1', 'Mom2','Mom3')

print(mom.mom1)

print(dad.dad2)

print(child.mom1)

print(child.dad2)

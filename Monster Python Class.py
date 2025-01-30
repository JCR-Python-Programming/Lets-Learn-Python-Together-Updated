main_class = (
    'This is an instance of a main class object with three attribute properties value 1',
    'This is an instance of a main class object with three attribute properties value 2',
    'This is an instance of a main class object with three attribute properties value 3')

sub_class1 = (
    'This is an instance of a sub class1 object with three attribute properties value 1',
    'This is an instance of a sub class1 object with three attribute properties value 2',
    'This is an instance of a sub class1 object with three attribute properties value 3')

sub_class2 = (
    'This is an instance of a sub class2 object with three attribute properties value 1',
    'This is an instance of a sub class2 object with three attribute properties value 2',
    'This is an instance of a sub class2 object with three attribute properties value 3')

super_sub_class1 = (
     'This is an instance of a super sub class1 object with four attribute properties value 1',
     'This is an instance of a super sub class1 object with four attribute properties value 2',
     'This is an instance of a super sub class1 object with four attribute properties value 3',
     'This is an instance of a super sub class1 object with four attribute properties value 4')

super_sub_class2 = (
     'This is an instance of a super sub class2 object with five attribute properties value 1',
     'This is an instance of a super sub class2 object with five attribute properties value 2',
     'This is an instance of a super sub class2 object with five attribute properties value 3',
     'This is an instance of a super sub class2 object with five attribute properties value 4',
     'This is an instance of a super sub class2 object with five attribute properties value 5')

super_sub_class3 = (
     'This is an instance of a super sub class3 object with six attribute properties value 1',
     'This is an instance of a super sub class3 object with six attribute properties value 2',
     'This is an instance of a super sub class3 object with six attribute properties value 3',
     'This is an instance of a super sub class3 object with six attribute properties value 4',
     'This is an instance of a super sub class3 object with six attribute properties value 5',
     'This is an instance of a super sub class3 object with six attribute properties value 6')

super_sub_class4 = (
     'This is an instance of a super sub class4 object with seven attribute properties value 1',
     'This is an instance of a super sub class4 object with seven attribute properties value 2',
     'This is an instance of a super sub class4 object with seven attribute properties value 3',
     'This is an instance of a super sub class4 object with seven attribute properties value 4',
     'This is an instance of a super sub class4 object with seven attribute properties value 5',
     'This is an instance of a super sub class4 object with seven attribute properties value 6',
     'This is an instance of a super sub class4 object with seven attribute properties value 7')

super_sub_class5 = (
     'This is an instance of a super sub class5 object with eight attribute properties value 1',
     'This is an instance of a super sub class5 object with eight attribute properties value 2',
     'This is an instance of a super sub class5 object with eight attribute properties value 3',
     'This is an instance of a super sub class5 object with eight attribute properties value 4',
     'This is an instance of a super sub class5 object with eight attribute properties value 5',
     'This is an instance of a super sub class5 object with eight attribute properties value 6',
     'This is an instance of a super sub class5 object with eight attribute properties value 7',
     'This is an instance of a super sub class5 object with eight attribute properties value 8')

super_sub_class6 = (
     'This is an instance of a super sub class6 object with nine attribute properties value 1',
     'This is an instance of a super sub class6 object with nine attribute properties value 2',
     'This is an instance of a super sub class6 object with nine attribute properties value 3',
     'This is an instance of a super sub class6 object with nine attribute properties value 4',
     'This is an instance of a super sub class6 object with nine attribute properties value 5',
     'This is an instance of a super sub class6 object with nine attribute properties value 6',
     'This is an instance of a super sub class6 object with nine attribute properties value 7',
     'This is an instance of a super sub class6 object with nine attribute properties value 8',
     'This is an instance of a super sub class6 object with nine attribute properties value 9')

super_sub_class7 = (
     'This is an instance of a super sub class7 object with ten attribute properties value 1',
     'This is an instance of a super sub class7 object with ten attribute properties value 2',
     'This is an instance of a super sub class7 object with ten attribute properties value 3',
     'This is an instance of a super sub class7 object with ten attribute properties value 4',
     'This is an instance of a super sub class7 object with ten attribute properties value 5',
     'This is an instance of a super sub class7 object with ten attribute properties value 6',
     'This is an instance of a super sub class7 object with ten attribute properties value 7',
     'This is an instance of a super sub class7 object with ten attribute properties value 8',
     'This is an instance of a super sub class7 object with ten attribute properties value 9',
     'This is an instance of a super sub class7 object with ten attribute properties value 10')

return_values = (
    '"The Main Class Act"',
    'Sub Class Act One.',
    'Sub Class Act Two',
    'Super Sub Class Act One',
    'Super Sub Class Act Two',
    'Super Sub Class Act Three',
    'Super Sub Class Act Four',
    'Super Sub Class Act Five',
    'Super Sub Class Act Six',
    'Super Sub Class Act Seven')

class Main_class_attribute_properties:

    def return_function():
        return return_values

    def __init__(self,attribute1,attribute2,attribute3):

        self.attribute1=attribute1
        self.attribute2=attribute2
        self.attribute3=attribute3

class Sub_class1_same_attribute_properties(  # inhert main class attribute properties only
    Main_class_attribute_properties):pass
    
class Sub_class2_same_attribute_properties(  # inhert main class attribute properties only
    Main_class_attribute_properties):pass

class Super_sub_class1_new_attribute_properties(
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1, attribute2,attribute3)

        self.attribute4=attribute4        

class Super_sub_class2_new_attribute_properties(
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5):
        
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.attribute5=attribute5

class Super_sub_class3_new_attribute_properties(
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6):
        
        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5)

        self.attribute6=attribute6

class Super_sub_class4_new_attribute_properties(
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7):
        
        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6)

        self.attribute7=attribute7

class Super_sub_class5_new_attribute_properties(
    Super_sub_class4_new_attribute_properties,
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8):
        
        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7)

        self.attribute8=attribute8

class Super_sub_class6_new_attribute_properties(
    Super_sub_class5_new_attribute_properties,
    Super_sub_class4_new_attribute_properties,
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8,
        
        attribute9):
        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7,attribute8)

        self.attribute9=attribute9

class Super_sub_class7_new_attribute_properties(
    Super_sub_class6_new_attribute_properties,
    Super_sub_class5_new_attribute_properties,
    Super_sub_class4_new_attribute_properties,
    Super_sub_class3_new_attribute_properties,
    Super_sub_class2_new_attribute_properties,
    Super_sub_class1_new_attribute_properties,
    Sub_class2_same_attribute_properties,
    Sub_class1_same_attribute_properties,
    Main_class_attribute_properties):

    def __init__(
        self,attribute1,attribute2,attribute3,attribute4,
        attribute5,attribute6,attribute7,attribute8,
        attribute9,attribute10):
        
        super().__init__(
            attribute1,attribute2,attribute3,attribute4,
            attribute5,attribute6,attribute7,attribute8,
            attribute9)

        self.attribute10=attribute10

a = Main_class_attribute_properties(main_class[0],main_class[1],main_class[2])

b = Sub_class1_same_attribute_properties(sub_class1[0],sub_class1[1],sub_class1[2])

c = Sub_class2_same_attribute_properties(sub_class2[0],sub_class2[1],sub_class2[2])

d = Super_sub_class1_new_attribute_properties(
    super_sub_class1[0],super_sub_class1[1],
    super_sub_class1[2],super_sub_class1[3])

e = Super_sub_class2_new_attribute_properties(
    super_sub_class2[0],super_sub_class2[1],
    super_sub_class2[2],super_sub_class2[3],
    super_sub_class2[4])

f = Super_sub_class3_new_attribute_properties(
    super_sub_class3[0],super_sub_class3[1],
    super_sub_class3[2],super_sub_class3[3],
    super_sub_class3[4],super_sub_class3[5])

g = Super_sub_class4_new_attribute_properties(
    super_sub_class4[0],super_sub_class4[1],
    super_sub_class4[2],super_sub_class4[3],
    super_sub_class4[4],super_sub_class4[5],
    super_sub_class4[6])

h = Super_sub_class5_new_attribute_properties(
    super_sub_class5[0],super_sub_class5[1],
    super_sub_class5[2],super_sub_class5[3],
    super_sub_class5[4],super_sub_class5[5],
    super_sub_class5[6],super_sub_class5[7])

i = Super_sub_class6_new_attribute_properties(
    super_sub_class6[0],super_sub_class6[1],
    super_sub_class6[2],super_sub_class6[3],
    super_sub_class6[4],super_sub_class6[5],
    super_sub_class6[6],super_sub_class6[7],
    super_sub_class6[8])

j = Super_sub_class7_new_attribute_properties(
    super_sub_class7[0],super_sub_class7[1],
    super_sub_class7[2],super_sub_class7[3],
    super_sub_class7[4],super_sub_class7[5],
    super_sub_class7[6],super_sub_class7[7],
    super_sub_class7[8],super_sub_class7[9])

class_attribute_tuple = (

a.attribute1,a.attribute2,a.attribute3,

b.attribute1,b.attribute2,b.attribute3,

c.attribute1,c.attribute2,c.attribute3,

d.attribute1,d.attribute2,d.attribute3,
d.attribute4,

e.attribute1,e.attribute2,e.attribute3,
e.attribute4,e.attribute5,

f.attribute1,f.attribute2,f.attribute3,
f.attribute4,f.attribute5,f.attribute6,

g.attribute1,g.attribute2,g.attribute3,
g.attribute4,g.attribute5,g.attribute6,
g.attribute7,

h.attribute1,h.attribute2,h.attribute3,
h.attribute4,h.attribute5,h.attribute6,
h.attribute7,h.attribute8,

i.attribute1,i.attribute2,i.attribute3,
i.attribute4,i.attribute5,i.attribute6,
i.attribute7,i.attribute8,i.attribute9,

j.attribute1,j.attribute2,j.attribute3,
j.attribute4,j.attribute5,j.attribute6,
j.attribute7,j.attribute8,j.attribute9,
j.attribute10)
 
return_value = (
    
    Main_class_attribute_properties.return_function(),
    
    Sub_class1_same_attribute_properties.return_function(),
    Sub_class2_same_attribute_properties.return_function(),
    
    Super_sub_class1_new_attribute_properties.return_function(),
    Super_sub_class2_new_attribute_properties.return_function(),
    Super_sub_class3_new_attribute_properties.return_function(),
    Super_sub_class4_new_attribute_properties.return_function(),
    Super_sub_class5_new_attribute_properties.return_function(),
    Super_sub_class6_new_attribute_properties.return_function(),
    Super_sub_class7_new_attribute_properties.return_function())

print(f'\n{return_value[0][0]}\n\n{a.attribute1}')

print(f'\n{return_value[0][1]}\n\n{b.attribute1}')

print(f'\n{return_value[0][2]}\n\n{c.attribute1}')

print(f'\n{return_value[0][3]}\n\n{d.attribute1}')

print(f'\n{return_value[0][4]}\n\n{e.attribute1}')

print(f'\n{return_value[0][5]}\n\n{f.attribute1}')

print(f'\n{return_value[0][6]}\n\n{g.attribute1}')

print(f'\n{return_value[0][7]}\n\n{h.attribute1}')

print(f'\n{return_value[0][8]}\n\n{i.attribute1}')

print(f'\n{return_value[0][9]}\n\n{j.attribute1}')

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

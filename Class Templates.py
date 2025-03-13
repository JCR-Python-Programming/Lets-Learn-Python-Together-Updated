# Class Templates with physical print() function value examples:

# Created by Joseph C. Richardson, GitHub.com

class Objects:
    
    def __init__(self,attribute):
        
        self.my_attribute = attribute
        
print(Objects('I am the class object attribute property value.').my_attribute)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects:
    
    def __init__(self,attribute1,attribute2):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        
print(Objects(
    'I am the class object attribute1 property value 1.',
    'I am the class object attribute2 property value 2.').my_attribute2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects:
    
    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3
        
print(Objects(
    'I am the class object attribute1 property value 1.',
    'I am the class object attribute2 property value 2.',
    'I am the class object attribute3 property value 3.').my_attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

print(Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.').my_attribute3)

print(Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.').my_attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_super_sub(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

print(Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.').my_attribute3)

print(Objects_super_sub(
    'I am the super sub class object attribute1 property value 1.',
    'I am the super sub class object attribute2 property value 2.',
    'I am the super sub class object attribute3 property value 3.',
    'I am the super sub class object attribute4 property value 4.').my_attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

class Objects_super_sub(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

print(Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.').my_attribute3)

print(Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.').my_attribute3)

print(Objects_super_sub(
    'I am the super sub class object attribute1 property value 1.',
    'I am the super sub class object attribute2 property value 2.',
    'I am the super sub class object attribute3 property value 3.',
    'I am the super sub class object attribute4 property value 4.').my_attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

class Objects_super_sub1(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

class Objects_super_sub2(Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.my_attribute5 = attribute5

print(Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.').my_attribute3)

print(Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.').my_attribute3)

print(Objects_super_sub1(
    'I am the super sub1 class object attribute1 property value 1.',
    'I am the super sub1 class object attribute2 property value 2.',
    'I am the super sub1 class object attribute3 property value 3.',
    'I am the super sub1 class object attribute4 property value 4.').my_attribute4)

print(Objects_super_sub2(
    'I am the super sub2 class object attribute1 property value 1.',
    'I am the super sub2 class object attribute2 property value 2.',
    'I am the super sub2 class object attribute3 property value 3.',
    'I am the super sub2 class object attribute4 property value 4.',
    'I am the super sub2 class object attribute5 property value 5.').my_attribute5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

class Objects_super_sub1(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

class Objects_super_sub2(Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.my_attribute5 = attribute5

class Objects_super_sub3(Objects_super_sub2,Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5)

        self.my_attribute6 = attribute6

print(Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.').my_attribute3)

print(Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.').my_attribute3)

print(Objects_super_sub1(
    'I am the super sub1 class object attribute1 property value 1.',
    'I am the super sub1 class object attribute2 property value 2.',
    'I am the super sub1 class object attribute3 property value 3.',
    'I am the super sub1 class object attribute4 property value 4.').my_attribute4)

print(Objects_super_sub2(
    'I am the super sub2 class object attribute1 property value 1.',
    'I am the super sub2 class object attribute2 property value 2.',
    'I am the super sub2 class object attribute3 property value 3.',
    'I am the super sub2 class object attribute4 property value 4.',
    'I am the super sub2 class object attribute5 property value 5.').my_attribute5)

print(Objects_super_sub3(
    'I am the super sub3 class object attribute1 property value 1.',
    'I am the super sub3 class object attribute2 property value 2.',
    'I am the super sub3 class object attribute3 property value 3.',
    'I am the super sub3 class object attribute4 property value 4.',
    'I am the super sub3 class object attribute5 property value 5.',
    'I am the super sub3 class object attribute6 property value 6.').my_attribute6)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub1(Objects_main):pass

class Objects_sub2(Objects_main):pass

class Objects_super_sub1(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

class Objects_super_sub2(Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.my_attribute5 = attribute5

class Objects_super_sub3(Objects_super_sub2,Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5)

        self.my_attribute6 = attribute6

class Objects_super_sub4(
    Objects_super_sub3,Objects_super_sub2,
    Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5,attribute6)

        self.my_attribute7 = attribute7

print(Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.').my_attribute3)

print(Objects_sub1(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.').my_attribute3)

print(Objects_sub2(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.').my_attribute3)

print(Objects_super_sub1(
    'I am the super sub1 class object attribute1 property value 1.',
    'I am the super sub1 class object attribute2 property value 2.',
    'I am the super sub1 class object attribute3 property value 3.',
    'I am the super sub1 class object attribute4 property value 4.').my_attribute4)

print(Objects_super_sub2(
    'I am the super sub2 class object attribute1 property value 1.',
    'I am the super sub2 class object attribute2 property value 2.',
    'I am the super sub2 class object attribute3 property value 3.',
    'I am the super sub2 class object attribute4 property value 4.',
    'I am the super sub2 class object attribute5 property value 5.').my_attribute5)

print(Objects_super_sub3(
    'I am the super sub3 class object attribute1 property value 1.',
    'I am the super sub3 class object attribute2 property value 2.',
    'I am the super sub3 class object attribute3 property value 3.',
    'I am the super sub3 class object attribute4 property value 4.',
    'I am the super sub3 class object attribute5 property value 5.',
    'I am the super sub3 class object attribute6 property value 6.').my_attribute6)

print(Objects_super_sub4(
    'I am the super sub4 class object attribute1 property value 1.',
    'I am the super sub4 class object attribute2 property value 2.',
    'I am the super sub4 class object attribute3 property value 3.',
    'I am the super sub4 class object attribute4 property value 4.',
    'I am the super sub4 class object attribute5 property value 5.',
    'I am the super sub4 class object attribute6 property value 6.',
    'I am the super sub4 class object attribute7 property value 7.').my_attribute7)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Class Templates with non-physical print() function value examples:

class Objects:
    
    def __init__(self,attribute):
        
        self.my_attribute = attribute

class_object_attribute = Objects('I am the class object attribute property value.')    
        
print(class_object_attribute.my_attribute)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects:
    
    def __init__(self,attribute1,attribute2):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        
class_object_attributes = Objects(
    'I am the class object attribute1 property value 1.',
    'I am the class object attribute2 property value 2.')

print(class_object_attributes.my_attribute2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects:
    
    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3
        
class_object_attributes = Objects(
    'I am the class object attribute1 property value 1.',
    'I am the class object attribute2 property value 2.',
    'I am the class object attribute3 property value 3.')

print(class_object_attributes.my_attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

main_class_object_attributes = Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.')

sub_class_object_attributes = Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.')

print(main_class_object_attributes.my_attribute3)

print(sub_class_object_attributes.my_attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_super_sub(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

main_class_object_attributes = Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.')

super_sub_class_object_attributes = Objects_super_sub(
    'I am the super sub class object attribute1 property value 1.',
    'I am the super sub class object attribute2 property value 2.',
    'I am the super sub class object attribute3 property value 3.',
    'I am the super sub class object attribute4 property value 4.')

print(main_class_object_attributes.my_attribute3)

print(super_sub_class_object_attributes.my_attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

class Objects_super_sub(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

main_class_object_attributes = Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.')

sub_class_object_attributes = Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.')

super_sub_class_object_attributes = Objects_super_sub(
    'I am the super sub class object attribute1 property value 1.',
    'I am the super sub class object attribute2 property value 2.',
    'I am the super sub class object attribute3 property value 3.',
    'I am the super sub class object attribute4 property value 4.')

print(main_class_object_attributes.my_attribute3)

print(sub_class_object_attributes.my_attribute3)

print(super_sub_class_object_attributes.my_attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

class Objects_super_sub1(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

class Objects_super_sub2(Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.my_attribute5 = attribute5

main_class_object_attributes = Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.')

sub_class_object_attributes = Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.')

super_sub1_class_object_attributes = Objects_super_sub1(
    'I am the super sub1 class object attribute1 property value 1.',
    'I am the super sub1 class object attribute2 property value 2.',
    'I am the super sub1 class object attribute3 property value 3.',
    'I am the super sub1 class object attribute4 property value 4.')

super_sub2_class_object_attributes = Objects_super_sub2(
    'I am the super sub2 class object attribute1 property value 1.',
    'I am the super sub2 class object attribute2 property value 2.',
    'I am the super sub2 class object attribute3 property value 3.',
    'I am the super sub2 class object attribute4 property value 4.',
    'I am the super sub2 class object attribute5 property value 5.')

print(main_class_object_attributes.my_attribute3)

print(sub_class_object_attributes.my_attribute3)

print(super_sub1_class_object_attributes.my_attribute4)

print(super_sub2_class_object_attributes.my_attribute5)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub(Objects_main):pass

class Objects_super_sub1(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

class Objects_super_sub2(Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.my_attribute5 = attribute5

class Objects_super_sub3(Objects_super_sub2,Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5)

        self.my_attribute6 = attribute6

main_class_object_attributes = Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.')

sub_class_object_attributes = Objects_sub(
    'I am the sub class object attribute1 property value 1.',
    'I am the sub class object attribute2 property value 2.',
    'I am the sub class object attribute3 property value 3.')

super_sub1_class_object_attributes = Objects_super_sub1(
    'I am the super sub1 class object attribute1 property value 1.',
    'I am the super sub1 class object attribute2 property value 2.',
    'I am the super sub1 class object attribute3 property value 3.',
    'I am the super sub1 class object attribute4 property value 4.')

super_sub2_class_object_attributes = Objects_super_sub2(
    'I am the super sub2 class object attribute1 property value 1.',
    'I am the super sub2 class object attribute2 property value 2.',
    'I am the super sub2 class object attribute3 property value 3.',
    'I am the super sub2 class object attribute4 property value 4.',
    'I am the super sub2 class object attribute5 property value 5.')

super_sub3_class_object_attributes = Objects_super_sub3(
    'I am the super sub3 class object attribute1 property value 1.',
    'I am the super sub3 class object attribute2 property value 2.',
    'I am the super sub3 class object attribute3 property value 3.',
    'I am the super sub3 class object attribute4 property value 4.',
    'I am the super sub3 class object attribute5 property value 5.',
    'I am the super sub3 class object attribute6 property value 6.')

print(main_class_object_attributes.my_attribute3)

print(sub_class_object_attributes.my_attribute3)

print(super_sub1_class_object_attributes.my_attribute4)

print(super_sub2_class_object_attributes.my_attribute5)

print(super_sub3_class_object_attributes.my_attribute6)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub1(Objects_main):pass

class Objects_sub2(Objects_main):pass

class Objects_super_sub1(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

class Objects_super_sub2(Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.my_attribute5 = attribute5

class Objects_super_sub3(Objects_super_sub2,Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5)

        self.my_attribute6 = attribute6

class Objects_super_sub4(
    Objects_super_sub3,Objects_super_sub2,
    Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5,attribute6)

        self.my_attribute7 = attribute7

main_class_object_attributes = Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.')

sub1_class_object_attributes = Objects_sub1(
    'I am the sub1 class object attribute1 property value 1.',
    'I am the sub1 class object attribute2 property value 2.',
    'I am the sub1 class object attribute3 property value 3.')

sub2_class_object_attributes = Objects_sub2(
    'I am the sub2 class object attribute1 property value 1.',
    'I am the sub2 class object attribute2 property value 2.',
    'I am the sub2 class object attribute3 property value 3.')

super_sub1_class_object_attributes = Objects_super_sub1(
    'I am the super sub1 class object attribute1 property value 1.',
    'I am the super sub1 class object attribute2 property value 2.',
    'I am the super sub1 class object attribute3 property value 3.',
    'I am the super sub1 class object attribute4 property value 4.')

super_sub2_class_object_attributes = Objects_super_sub2(
    'I am the super sub2 class object attribute1 property value 1.',
    'I am the super sub2 class object attribute2 property value 2.',
    'I am the super sub2 class object attribute3 property value 3.',
    'I am the super sub2 class object attribute4 property value 4.',
    'I am the super sub2 class object attribute5 property value 5.')

super_sub3_class_object_attributes = Objects_super_sub3(
    'I am the super sub3 class object attribute1 property value 1.',
    'I am the super sub3 class object attribute2 property value 2.',
    'I am the super sub3 class object attribute3 property value 3.',
    'I am the super sub3 class object attribute4 property value 4.',
    'I am the super sub3 class object attribute5 property value 5.',
    'I am the super sub3 class object attribute6 property value 6.')

super_sub4_class_object_attributes = Objects_super_sub4(
    'I am the super sub4 class object attribute1 property value 1.',
    'I am the super sub4 class object attribute2 property value 2.',
    'I am the super sub4 class object attribute3 property value 3.',
    'I am the super sub4 class object attribute4 property value 4.',
    'I am the super sub4 class object attribute5 property value 5.',
    'I am the super sub4 class object attribute6 property value 6.',
    'I am the super sub4 class object attribute7 property value 7.')

print(main_class_object_attributes.my_attribute3)

print(sub1_class_object_attributes.my_attribute3)

print(sub2_class_object_attributes.my_attribute3)

print(super_sub1_class_object_attributes.my_attribute4)

print(super_sub2_class_object_attributes.my_attribute5)

print(super_sub3_class_object_attributes.my_attribute6)

print(super_sub4_class_object_attributes.my_attribute7)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a real, working class using the above Objects class example.
# All we will do is change some variable names, along with their values.

class Objects_main:

    def __init__(self,attribute1,attribute2,attribute3):
        
        self.my_attribute1 = attribute1
        self.my_attribute2 = attribute2
        self.my_attribute3 = attribute3

class Objects_sub1(Objects_main):pass

class Objects_sub2(Objects_main):pass

class Objects_super_sub1(Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4):
        super().__init__(attribute1,attribute2,attribute3)

        self.my_attribute4 = attribute4

class Objects_super_sub2(Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3,attribute4)

        self.my_attribute5 = attribute5

class Objects_super_sub3(Objects_super_sub2,Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5)

        self.my_attribute6 = attribute6

class Objects_super_sub4(
    Objects_super_sub3,Objects_super_sub2,
    Objects_super_sub1,Objects_main):
    
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5,attribute6)

        self.my_attribute7 = attribute7

main_class_object_attributes = Objects_main(
    'I am the main class object attribute1 property value 1.',
    'I am the main class object attribute2 property value 2.',
    'I am the main class object attribute3 property value 3.')

sub1_class_object_attributes = Objects_sub1(
    'I am the sub1 class object attribute1 property value 1.',
    'I am the sub1 class object attribute2 property value 2.',
    'I am the sub1 class object attribute3 property value 3.')

sub2_class_object_attributes = Objects_sub2(
    'I am the sub2 class object attribute1 property value 1.',
    'I am the sub2 class object attribute2 property value 2.',
    'I am the sub2 class object attribute3 property value 3.')

super_sub1_class_object_attributes = Objects_super_sub1(
    'I am the super sub1 class object attribute1 property value 1.',
    'I am the super sub1 class object attribute2 property value 2.',
    'I am the super sub1 class object attribute3 property value 3.',
    'I am the super sub1 class object attribute4 property value 4.')

super_sub2_class_object_attributes = Objects_super_sub2(
    'I am the super sub2 class object attribute1 property value 1.',
    'I am the super sub2 class object attribute2 property value 2.',
    'I am the super sub2 class object attribute3 property value 3.',
    'I am the super sub2 class object attribute4 property value 4.',
    'I am the super sub2 class object attribute5 property value 5.')

super_sub3_class_object_attributes = Objects_super_sub3(
    'I am the super sub3 class object attribute1 property value 1.',
    'I am the super sub3 class object attribute2 property value 2.',
    'I am the super sub3 class object attribute3 property value 3.',
    'I am the super sub3 class object attribute4 property value 4.',
    'I am the super sub3 class object attribute5 property value 5.',
    'I am the super sub3 class object attribute6 property value 6.')

super_sub4_class_object_attributes = Objects_super_sub4(
    'I am the super sub4 class object attribute1 property value 1.',
    'I am the super sub4 class object attribute2 property value 2.',
    'I am the super sub4 class object attribute3 property value 3.',
    'I am the super sub4 class object attribute4 property value 4.',
    'I am the super sub4 class object attribute5 property value 5.',
    'I am the super sub4 class object attribute6 property value 6.',
    'I am the super sub4 class object attribute7 property value 7.')

print(main_class_object_attributes.my_attribute3)

print(sub1_class_object_attributes.my_attribute3)

print(sub2_class_object_attributes.my_attribute3)

print(super_sub1_class_object_attributes.my_attribute4)

print(super_sub2_class_object_attributes.my_attribute5)

print(super_sub3_class_object_attributes.my_attribute6)

print(super_sub4_class_object_attributes.my_attribute7)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a real working multi class act, by which the Son class
# and the Daughter class inherits their individual Mom and Dad class
# attributes. The Mom and Dad classes each have one attribute that is
# different from the other. The Mom class has the attribute 'doctor' and
# Dad class has the attribute 'firefighter'. The Son class inherits the
# 'firefighter' attribute and the Daughter class inherits the 'doctor'
# attribute. The Son class has all its Dad class attributes and the
# Daughter class has all its Mom class attributes. Note: do not invoke
# the super() function if you want Mom and Dad classes to have one
# or more of their own, unique attribute properties such as the 'doctor'
# attribute from the Mom class, and the 'firefighter' attribute from the
# Dad class.

class Mom:

    def __init__(self,fname,lname,age,doctor):
        
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.doctor = doctor  # Note: the different attribute property 'doctor'

class Dad:

    def __init__(self,fname,lname,age,firefighter):
        
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.firefighter = firefighter  # Note: the different attribute property 'firefighter'

class Son(Dad):pass  # inherits all the Dad class attribute properties only

class Daughter(Mom):pass  # inherits all the Mom class attribute properties only

mom = Mom('Jane','Smith',40,'Doctor')

daughter = Daughter('Jean','Smith',21,'Doctor')

dad = Dad('John','Smith',45,'Firefighter')

son = Son('Jack','Smith',18,'Firefighter')

# Invoke the f' string format to make string concatenation much easier.

print(f'My name is {mom.first_name} {mom.last_name}. I am a {mom.age} year old {mom.doctor}.')

print(f'My name is {daughter.first_name} {daughter.last_name}. I am a {daughter.age} year old {daughter.doctor}.')

print(f'My name is {dad.first_name} {dad.last_name}. I am a {dad.age} year old {dad.firefighter}.')

print(f'My name is {son.first_name} {son.last_name}. I am a {son.age} year old {son.firefighter}.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a tuple of class attribute values, along with a for loop and
# one print() function to create the same multi class example above.

class Mom:

    def __init__(self,fname,lname,age,doctor):
        
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.doctor = doctor

class Dad:

    def __init__(self,fname,lname,age,firefighter):
        
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.firefighter = firefighter

class Son(Dad):pass

class Daughter(Mom):pass

mom = Mom('Jane','Smith',40,'Doctor')

daughter = Daughter('Jean','Smith',21,'Doctor')

dad = Dad('John','Smith',45,'Firefighter')

son = Son('Jack','Smith',18,'Firefighter')

# Invoke the f' string format to make string concatenation much easier.

family = (
    f'My name is {mom.first_name} {mom.last_name}. I am a {mom.age} year old {mom.doctor}.',
    f'My name is {daughter.first_name} {daughter.last_name}. I am a {daughter.age} year old {daughter.doctor}.',
    f'My name is {dad.first_name} {dad.last_name}. I am a {dad.age} year old {dad.firefighter}.',
    f'My name is {son.first_name} {son.last_name}. I am a {son.age} year old {son.firefighter}.')

for i in family:
    print(i)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

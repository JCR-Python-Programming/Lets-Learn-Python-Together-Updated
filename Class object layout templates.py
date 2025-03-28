# Class Object Layout Templates Python program examples:

# Created by Joseph C. Richardson, GitHub.com

class Class_object_layout_template:

    def __init__(self,value):
        self.value = value  # one attribute

print(Class_object_layout_template('value').value)  # one attribute value extension

variable = Class_object_layout_template('value').value  # one attribute value extension

print(variable)

variable = Class_object_layout_template('value')

print(variable.value)  # one attribute value extension
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_object_layout_template:

    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2  # two attributes

print(Class_object_layout_template('value1','value2').value1)
print(Class_object_layout_template('value1','value2').value2)  # two attribute value extensions

variable1 = Class_object_layout_template('value1','value2').value1
variable2 = Class_object_layout_template('value1','value2').value2  # two attribute value extensions

print(variable1)
print(variable2)

variable1 = Class_object_layout_template('value1','value2')
variable2 = Class_object_layout_template('value1','value2')

print(variable1.value1)
print(variable2.value2)  # two attribute value extensions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_object_layout_template:

    def __init__(self,value1,value2,value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3  # three attributes

print(Class_object_layout_template('value1','value2','value3').value1)
print(Class_object_layout_template('value1','value2','value3').value2)
print(Class_object_layout_template('value1','value2','value3').value3)  # three attribute value extensions

variable1 = Class_object_layout_template('value1','value2','value3').value1
variable2 = Class_object_layout_template('value1','value2','value3').value2
variable3 = Class_object_layout_template('value1','value2','value3').value3  # three attribute value extensions

print(variable1)
print(variable2)
print(variable3)

variable1 = Class_object_layout_template('value1','value2','value3')
variable2 = Class_object_layout_template('value1','value2','value3')
variable3 = Class_object_layout_template('value1','value2','value3')

print(variable1.value1)
print(variable2.value2)
print(variable3.value3)  # three attribute value extensions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_object_layout_template:

    def __init__(self,value1,value2,value3,value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4  # four attributes

print(Class_object_layout_template('value1','value2','value3','value4').value1)
print(Class_object_layout_template('value1','value2','value3','value4').value2)
print(Class_object_layout_template('value1','value2','value3','value4').value3)
print(Class_object_layout_template('value1','value2','value3','value4').value4)  # four attribute value extensions

variable1 = Class_object_layout_template('value1','value2','value3','value4').value1
variable2 = Class_object_layout_template('value1','value2','value3','value4').value2
variable3 = Class_object_layout_template('value1','value2','value3','value4').value3
variable4 = Class_object_layout_template('value1','value2','value3','value4').value4  # four attribute value extensions

print(variable1)
print(variable2)
print(variable3)
print(variable4)

variable1 = Class_object_layout_template('value1','value2','value3','value4')
variable2 = Class_object_layout_template('value1','value2','value3','value4')
variable3 = Class_object_layout_template('value1','value2','value3','value4')
variable4 = Class_object_layout_template('value1','value2','value3','value4')

print(variable1.value1)
print(variable2.value2)
print(variable3.value3)
print(variable4.value4)  # four attribute value extensions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Super Class Object Layout Templates Python program examples:

class Super_class_object_layout_template:

    def __init__(self,value1):
        self.value1 = value1  # one attribute

class Super_class_object(Super_class_object_layout_template):

    def __init__(self,value1,value2):
        super().__init__(value1)

        self.value2 = value2  # one unique attribute

print(Super_class_object_layout_template('value1').value1)  # one attribute value extension

print(Super_class_object('value1','value2').value1)  # one inherited attribute value extension

print(Super_class_object('value1','value2').value2)  # one unique attribute value extension
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Super_class_object_layout_template:

    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2  # two attributes

class Super_class_object(Super_class_object_layout_template):

    def __init__(self,value1,value2,value3):
        super().__init__(value1,value2)

        self.value3 = value3  # one unique attribute

print(Super_class_object_layout_template('value1','value2').value1)  # one attribute value extension

print(Super_class_object_layout_template('value1','value2').value2)  # one attribute value extension


print(Super_class_object('value1','value2','value3').value1)  # one inherited attribute value extension

print(Super_class_object('value1','value2','value3').value2)  # one inherited attribute value extension


print(Super_class_object('value1','value2','value3').value3)  # one unique attribute value extension
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Super_class_object_layout_template:

    def __init__(self,value1,value2,value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3  # three attributes

class Super_class_object(Super_class_object_layout_template):

    def __init__(self,value1,value2,value3,value4):
        super().__init__(value1,value2,value3)

        self.value4 = value4  # one unique attribute

print(Super_class_object_layout_template('value1','value2','value3').value1)  # one attribute value extension

print(Super_class_object_layout_template('value1','value2','value3').value2)  # one attribute value extension

print(Super_class_object_layout_template('value1','value2','value3').value3)  # one attribute value extension


print(Super_class_object('value1','value2','value3','value4').value1)  # one inherited attribute value extension

print(Super_class_object('value1','value2','value3','value4').value2)  # one inherited attribute value extension

print(Super_class_object('value1','value2','value3','value4').value3)  # one inherited attribute value extension


print(Super_class_object('value1','value2','value3','value4').value4)  # one unique attribute value extension

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

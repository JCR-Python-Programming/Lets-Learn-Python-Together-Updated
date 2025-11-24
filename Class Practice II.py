
# Practice, practice and more practice, practice.

class Class_act:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1  # attribute1 property:

    self.attribute2 = attribute2  # attribute2 property:

  def return_value(variable_value):
    return 'Returned Variable Value from Class_act.'

class Superclass1(Class_act):  # inherit the 'Class_act' attribute properties:

  # no redundant attribute properties:

  def __init__(self,attribute1,attribute2):
    super().__init__(attribute1,attribute2)

# inherit the 'Class_act' attribute properties and create two new attribute properties:

class Superclass2(Class_act):

  def __init__(
    self,attribute1,attribute2,attribute3,attribute4):
    super().__init__(attribute1,attribute2)

    self.attribute3 = attribute3  # new attribute3 property:

    self.attribute4 = attribute4  # new attribute4 property:

class_attribute_values = Class_act(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')  # two argument values:

superclass1_attribute_values = Superclass1(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')  # two argument values:

superclass2_attribute_values = Superclass2(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2',
  'I am the attribute property value of attribute3',
  'I am the attribute property value of attribute4')  # four argument values:

a = Class_act.return_value('argument placeholder')

b = Superclass1.return_value('argument placeholder')

c = Superclass2.return_value('argument placeholder')

print(class_attribute_values.attribute1)  # attribute1 property from Class_act:
print(class_attribute_values.attribute2)  # attribute2 property from Class_act:

print(superclass1_attribute_values.attribute1)  # same attribute1 property from Class_act:
print(superclass1_attribute_values.attribute2)  # same attribute2 property from Class_act:

print(superclass2_attribute_values.attribute1)  # same attribute1 property from Class_act:
print(superclass2_attribute_values.attribute2)  # same attribute2 property from Class_act:

print(superclass2_attribute_values.attribute3)  # new attribute3 property from superclass2_attribute_values:
print(superclass2_attribute_values.attribute4)  # new attribute4 property from superclass2_attribute_values:

print(a)
print(b)
print(c)

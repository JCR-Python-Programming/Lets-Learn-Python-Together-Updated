
# Practice, practice and more practice, practice III

class Class_act:

  def __init__(self,attribute1,attribute2):

    self.a = attribute1  # attribute1 property:

    self.b = attribute2  # attribute2 property:

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

    self.c = attribute3  # new attribute3 property:

    self.d = attribute4  # new attribute4 property:

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

return_value1 = Class_act.return_value('argument placeholder')

return_value2 = Superclass1.return_value('argument placeholder')

return_value3 = Superclass2.return_value('argument placeholder')

print(class_attribute_values.a)  # attribute1 property from Class_act:
print(class_attribute_values.b)  # attribute2 property from Class_act:

print(superclass1_attribute_values.a)  # same attribute1 property from Class_act:
print(superclass1_attribute_values.b)  # same attribute2 property from Class_act:

print(superclass2_attribute_values.a)  # same attribute1 property from Class_act:
print(superclass2_attribute_values.b)  # same attribute2 property from Class_act:

print(superclass2_attribute_values.c)  # new attribute3 property from superclass2_attribute_values:
print(superclass2_attribute_values.d)  # new attribute4 property from superclass2_attribute_values:

print(return_value1)
print(return_value2)
print(return_value3)

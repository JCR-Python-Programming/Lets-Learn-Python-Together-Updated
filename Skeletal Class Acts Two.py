
class Main_super_class_skeleton_structure:
  def __init__(self,one,two,three):
    self.one = one
    self.two = two
    self.three = three

class Sub_super_class_skeleton_structure(Main_super_class_skeleton_structure):
  def __init__(self,one,two,three):
    super().__init__(one,two,three)

print(Main_super_class_skeleton_structure('One','Two','Three').one)

print(Sub_super_class_skeleton_structure('One','Two','Three').two)

print(Sub_super_class_skeleton_structure('One','Two','Three').three)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,one,two,three):
    self.one = one
    self.two = two
    self.three = three

  def return_main_value(self):
    return 1,2,3,4,'a','b','c','d'

  def return_main_addition_value(num1,num2):
    return num1 + num2

  def return_main_subtraction_value(num1,num2):
    return num1 - num2

  def return_main_multiplication_value(num1,num2):
    return num1 * num2

  def return_main_division_value(num1,num2):
    return round(num1 / num2,2)

class Sub_super_one(Main):
  def __init__(self,one,two,three):
    super().__init__(one,two,three)

  def return_sub_super_one_value(self):
    return 'Returned sub super one value.'

class Sub_super_two(Main):
  def __init__(self,one,two,three):
    super().__init__(one,two,three)

  def return_sub_super_two_value(self):
    return 'Returned sub super two value.'

class Sub_super_three(Main):
  def __init__(self,one,two,three,four):
    super().__init__(one,two,three)

    self.four = four

  def return_sub_super_three_value(self):
    return 'Returned sub super three value.'

class Child(Sub_super_three,Main):

  def child_return_value(self):
    return 'Returned Child Class value.'

# Main class, sub super classes and child class values:

print(Main('One','Two','Three').one)

print(Sub_super_one('One','Two','Three').two)

print(Sub_super_two('One','Two','Three').three)

print(Sub_super_three('One','Two','Three','four').four)

print(Child('One','Two','Three','four').four)

# Child class values:

print(Child('One','Two','Three','four').one)

print(Child('One','Two','Three','four').two)

print(Child('One','Two','Three','four').three)

print(Child('One','Two','Three','four').four)

# Returned main class values:

print(Main.return_main_value('argument placeholder value')[0])

print(Main.return_main_addition_value(5,3))

print(Main.return_main_subtraction_value(5,3))

print(Main.return_main_multiplication_value(5,3))

print(Main.return_main_division_value(5,3))

# Returned sub super class values:

print(Sub_super_one.return_sub_super_one_value('argument placeholder value'))

print(Sub_super_two.return_sub_super_two_value('argument placeholder value'))

print(Sub_super_three.return_sub_super_three_value('argument placeholder value'))

# Returned child class values:

print(Child.return_main_value('argument placeholder value')[0])

print(Child.return_main_addition_value(5,3))

print(Child.return_main_subtraction_value(5,3))

print(Child.return_main_multiplication_value(5,3))

print(Child.return_main_division_value(5,3))

print(Child.return_main_division_value(5,3))

print(Child.child_return_value('argument placeholder value'))

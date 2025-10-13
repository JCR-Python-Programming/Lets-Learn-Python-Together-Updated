
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

class Sub_super_one(Main):
  def __init__(self,one,two,three):
    super().__init__(one,two,three)

class Sub_super_two(Sub_super_one):
  def __init__(self,one,two,three):
    super().__init__(one,two,three)

class Sub_super_three(Sub_super_two):
  def __init__(self,one,two,three,four):
    super().__init__(one,two,three)

    self.four = four

class Child(Sub_super_three,Main):pass

print(Main('One','Two','Three').one)

print(Sub_super_one('One','Two','Three').two)

print(Sub_super_two('One','Two','Three').three)

print(Sub_super_three('One','Two','Three','four').four)

print(Child('One','Two','Three','four').four)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

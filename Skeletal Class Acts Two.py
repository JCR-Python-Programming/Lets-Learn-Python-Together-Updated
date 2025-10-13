
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

  def return_function(self):
    return 1,2,3,4

class Sub_super_one(Main):
  def __init__(self,one,two,three):
    super().__init__(one,two,three)

class Sub_super_two(Main):
  def __init__(self,one,two,three):
    super().__init__(one,two,three)

class Sub_super_three(Main):
  def __init__(self,one,two,three,four):
    super().__init__(one,two,three)

    self.four = four

class Child(Sub_super_three,Main):pass

print(Main('One','Two','Three').one)

print(Sub_super_one('One','Two','Three').two)

print(Sub_super_two('One','Two','Three').three)

print(Sub_super_three('One','Two','Three','four').four)

print(Child('One','Two','Three','four').four)

# Return function calls:

print(Main.return_function('return argument placeholder value')[0])

print(Sub_super_one.return_function('return argument placeholder value')[1])

print(Sub_super_two.return_function('return argument placeholder value')[2])

print(Child.return_function('return argument placeholder value')[3])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

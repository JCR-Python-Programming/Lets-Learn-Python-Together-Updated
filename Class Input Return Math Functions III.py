import math

class Math:
  def __init__(self,user_input1,user_input2):

    self.user_input1 = user_input1  # attribute1 property:

    self.user_input2 = user_input2  # attribute2 property:

  def return_answer(self):
    return (
      self.user_input1+self.user_input2,
      self.user_input1-self.user_input2,
      self.user_input1*self.user_input2,
      self.user_input1/self.user_input2,
      self.user_input1**self.user_input2,
      pow(self.user_input1,self.user_input2),
      math.sqrt(self.user_input2))

class Great_work(Math):

  def __init__(self,user_input1,user_input2,user_input3):
    super().__init__(user_input1,user_input2)

    self.user_input3 = user_input3  # super attribute3 property:

  def return_super(self):
    return self.user_input3

message = (
  'Please type a number, the press enter: ',
  'Please type a second number, then press enter: ',
  'Numbers only please:','Great Work!!')

while True:

  try:
    user_input1 = int(input(message[0]).strip())
    user_input2 = int(input(message[1]).strip())
    break

  except ValueError:
    print(message[2])

answer = Math(user_input1,user_input2).return_answer()
great_work = Great_work(user_input1,user_input2,message[3]).return_super()

for i in range(7):print(answer[i])

print(great_work)

# Let's have some extreme fun with basic class objects. This time
# we won't follow all the rules, but most Python commands do
# have to have proper syntax rules in order to work right, without
# getting errors in Python code text. Let's make the 'self' word
# inside class constructers be whatever variable name we like,
# other than the boring word, 'self'.

# proper syntax rule standard:

class Class_attributes:

    def __init__(self,text):
        self.text=text

print(Class_attributes('This is an instance of a class object.').text)

# also a proper syntax rule standard:

class Class_attributes:

    def __init__(self,text):
        self.my_anything_name_I_want=text

print(Class_attributes('This is an instance of a class object.').my_anything_name_I_want)

# improper syntax rule standard: 

class class_attributes:  # non capitalized

    def __init__(cobra,text):  # incorrect standard for 'self'
        cobra.snake=text  # incorrect standard for 'self'

print(class_attributes("This works, but your Boss will 'F' you for it...").snake)        

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

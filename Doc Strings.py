def function_one():
  """ Doc String function_one """

  print('function one')

def function_two():
  """ Doc String function_two """

  print('function two')

def function_three():
  """ Doc String function_three """

  print('function three')

def function_four():
  """ Doc String function_four """

  print('function four')

doc_strings = (
  function_one,
  function_two,
  function_three,
  function_four)

def_functs = (
  function_one,
  function_two,
  function_three,
  function_four)

for i in def_functs:
    print(i.__doc__);i()

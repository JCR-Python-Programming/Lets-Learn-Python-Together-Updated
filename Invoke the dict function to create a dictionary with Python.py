# Invoke the dict() function to manually create a dictionary with Python

# Created by Joseph C. Richardson, GitHub.com

dictionary = dict(key1 = 'Value1',Key2 = 'Value2',Key3 = 'Value3')

keys = dictionary.keys()

values = dictionary.values()

print(dictionary)  # {'key1': 'Value1', 'Key2': 'Value2', 'Key3': 'Value3'}

print(dictionary.get('key1'))  # Value1

print(dictionary.get('key4','key not found:'))  # optional

print(keys)  # dict_keys(['key1', 'Key2', 'Key3'])

print(values)  # dict_values(['Value1', 'Value2', 'Value3'])

print(f'You have {len(keys)} keys and {len(values)} values: ')

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁

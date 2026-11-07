# The dict() function takes keyword arguments.

my_dict = dict(key1 = 'value1',key2 = 'value2')

print(my_dict)  # screen output: {'key1': 'value1', 'key2': 'value2'}

print(my_dict.get('key1','Sorry! key not found:'))  # screen output: value1

my_dict.update(key3 = 'value3',key4 = 'value4') 

print(my_dict)  # screen output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

print(my_dict.get('key4','Sorry! key not found:'))  # screen output: value4

my_dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

my_dictionary.update({'key5':'value5'})

print(my_dictionary)  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

print(my_dictionary.get('key5','Sorry! key not found:'))  # screen output: value5

print(my_dictionary.keys())  # dict_keys(['key1', 'key2', 'key3', 'key4', 'key5'])

print(my_dictionary.values())  # dict_values(['value1', 'value2', 'value3', 'value4', 'value5'])

print('You have',len(my_dictionary.keys()),'keys','and',len(my_dictionary.values()),'values.')  # You have 5 keys and 5 values.

# or invoke the developer depreciated old string format example:

print('You have {} keys and {} values.'.format(len(my_dictionary.keys()),len(my_dictionary.values())))  # You have 5 keys and 5 values.

# or invoke the new f' string format example:

print(f'You have {len(my_dictionary.keys())} keys and {len(my_dictionary.values())} values.')  # You have 5 keys and 5 values.

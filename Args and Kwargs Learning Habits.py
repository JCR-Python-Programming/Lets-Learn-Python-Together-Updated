def print_positional_args(*args):

    return 'text value 1','text value 2'

print(print_positional_args('argument placeholder value','argument placeholder value','argument placeholder value')[0])

def print_keyword_args(**kwargs):

    return 'text value 1','text value 2'

print(print_keyword_args(kwargs1 = 'argument placeholder',kwargs2 = 'argument placeholder')[0])




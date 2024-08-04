def print_params(a = 1, b = 'строка', c = True, *args, **kwargs):
    return print(a, b, c)


values_list = [23, True, 1.1]
values_dict = {'a': 1, 'b': 'string', 'c': False}
values_list_2 = [54.32, 'Строка']

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(False, 2, 'asdas')
print_params(b=123, c='str')
print_params(c=False, a='rts')
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [58, 12, 5]
values_dict = {'a': 2.5, 'b': 'b', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [58, 'str']
print_params(*values_list_2, 42)

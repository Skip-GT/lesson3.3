def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(33)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(7, "str", False)

values_list = [11, "list", 3.55]
values_dict = {'a': 222, 'b': "int", 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [532, "asd"]
print_params(*values_list_2, 33)

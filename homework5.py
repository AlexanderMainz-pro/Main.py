immutable_var = (1, 2, 3, True, "string")
print(immutable_var)
#После того как кортеж создан, в него нельзя добавлять элементы, а также изменять их или удалять
mutable_list = [1, 2, 3.0, True]
mutable_list[3:] = [False]
print((mutable_list))

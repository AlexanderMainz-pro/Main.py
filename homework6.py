my_dict = {"Alexander" : 1988,
           "Broneslav" : 1989,
           "Igor"      : 1990
           }
print(my_dict)
my_dict["Viktor"] = 1991
print(my_dict.get("Alexander"), my_dict["Viktor"])
my_dict["Anatoly"] = 1992
my_dict["Basil"] = 1993
a = my_dict.pop("Igor")
print(a)
print(my_dict.get("Igor", 1990))
print(my_dict)

my_set = {1, 2.0, 2.0, False, "str",(1, 2, 3)}
print(my_set)
my_set.update([True, 3])
my_set.remove(False)
print(my_set)












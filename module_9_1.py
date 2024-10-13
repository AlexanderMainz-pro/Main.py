def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


int_list = [3, 1, 4, 1, 5, 9, 2, 6]


results = apply_all_func(int_list, min, max, len, sum, sorted)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
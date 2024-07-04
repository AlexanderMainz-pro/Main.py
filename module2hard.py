for i in range(3, 21):
    print(i, end=' ')
    for j in range(3, 21):
        f = j // 10
        s = j % 10
        if i % (f + s) == 0:
            print(j, end=' ')
    print()

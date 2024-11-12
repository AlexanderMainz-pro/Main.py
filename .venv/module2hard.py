a = int(input("Введите число: "))
l = []
for i in range(1, 21):
    for j in range(1, 21):
        if a % (i + j) == 0 and i < j:
            l.append(i)
            l.append(j)
    print(l)

result = []
n = int(input("Введите число от 3 до 20 :"))
for m in range(1, n):
    for a in range(m + 1, n):
        if n % (m + a) == 0:
            result.append(m)
            result.append(a)


print(result)



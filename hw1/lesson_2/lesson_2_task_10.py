def bank(x, y):
    total = x
    for i in range(y):
        total += total * 0.10
    return total

x = int(input("Введите размер вклада: "))
y = int(input("Введите срок вклада в годах: "))
result = bank(x, y)
print("Сумма на счету спустя", y, "лет будет равна", result, "рублей.")
def month_to_season(num):
    if 1 <= num < 3 or num == 12:
        print("Зима")
    if 3 <= num <= 5:
        print("Весна")
    if 6 <= num <= 8:
        print("Лето")
    if 9 <= num <= 11:
        print("Осень")
    if  num == 0:
        print('Такого месяца не существует')

try:
    num = int(input("Введите число месяца: "))
    month_to_season(num)
except ValueError: 
    print("Это не число.")
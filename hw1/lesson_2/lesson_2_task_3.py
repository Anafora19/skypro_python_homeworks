def square(a):
    S = a ** 2
    if a % 1 == 0:
        print('Площадь=', S)
    else:  print('Площадь=', round(S))

square(4)
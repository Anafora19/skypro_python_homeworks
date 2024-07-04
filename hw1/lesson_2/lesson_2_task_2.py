import calendar

year = 2021
is_leap = calendar.isleap(year)

if is_leap:
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год")
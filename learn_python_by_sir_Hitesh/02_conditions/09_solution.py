year = 2024


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "this is leap year")
else:
    print(year, "this is not leap year")
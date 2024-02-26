'''2. Determining if a year is a leap year
year = 2024
formula to find leap year (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)'''


year=int(input("enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#if year % 4 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
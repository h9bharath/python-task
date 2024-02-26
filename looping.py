# while loop
#i="exit"
while True:
    a=input("enter 'exit' to stop the loop: ")
    if a.lower() == 'exit':
        break
    year=int(input("enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#if year % 4 == 0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")


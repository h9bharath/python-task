'''
4. Finding the maximum of three numbers

a, b, c = 10, 5, 8'''

a=int(input("enter first value"))
b=int(input("enter second value"))
c=int(input("enter third number"))
if a>b and a>c:
    print(f"{a} is maximum")
elif b>c and b>a:
    print(f"{b} is maximum")
else:
    print(f"{c} is maximum ")

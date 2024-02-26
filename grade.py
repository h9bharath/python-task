'''6. Grading System

score = 75


conditions
if score is greater than or equal to 90 then it return grade A,
if score is greater than 50 but less than or equal to 89 then it return grade B,

if score is greater than or equal to 35 but less than or equal to 50 then it return grade C,

if score is  less then 35 it return grade F,'''

marks=int(input("enter a value: "))
if marks >= 90:
    print("grade A")
elif marks>=50 and marks<=89:
    print("grade B")
elif marks >= 35 and marks < 50:
    print("grade C")
else:
    print("grade F")











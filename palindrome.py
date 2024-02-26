#MADAM=MADAM
'''a="MADAM"
b=" "
print(a)
print(len(a))
i=len(a)-1
print(i)
if i>0:
    b=b+a[i]
    i=i-1
print(b)
if a==b:
    print(a,"is a paliondrome")
else:
    print(a,"is not polindrome")'''


a=input("enter the input: ")
print(a)
b=(a[::-1])
if a==b:
    print("is palindrome")
else:
    print("is not palindrome")










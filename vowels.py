'''5. Determining if a character is a vowel or consonant:
text = ['a', 'e', 'k', 'e', 'y']'''

'''t=['a','e','k']
v=['a','e','i','o','u']
i=0
j=0
if t[i] in v[j]:
    print("vowel")
    i=i+1
else:
    print("consonant")
j=j+1'''



'''if (t=='a' or t=='e'or t=="i" or t=="o" or t=="u"):

    print("vowel")
else:
    print("consonant")'''

#v=['a','e','i','o','u']
alphabet = str(input("enter a value:  "))
vowels = ['a','e','i','o','u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
if alphabet.lower() in vowels:

#if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
    print(f"{alphabet} is a vowel")
elif alphabet.lower() in consonants:
    print(f"{alphabet} is consonant")
else:
    print("enter valid input")
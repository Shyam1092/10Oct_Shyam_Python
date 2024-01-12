a = {'A':1,'B':2,'C':3,'D':4}

print(a)

b = input("Enter key to check : ")

if b in a.keys():
    print("Key is present : ", a[b])
else:
    print("Key is not present")
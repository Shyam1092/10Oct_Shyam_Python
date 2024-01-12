a = {'A':1,'B':2,'C':3,'D':4}

print(a)

b = input("Enter key to check : ")

if b in a:
    print(f"The key {b} exists.")
else:
    print(f"the key {b} is not exist.")
def a(b):
    if(b == b[::-1]):
        return"This sring is pelindrom"
    else:
        return"This sring is not pelindrom"

b = input("Enter your string : ")
print(a(b))
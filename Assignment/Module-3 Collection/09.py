def aa(a ,b):
    c = "Common Element not found"

    for i in a:
        for o in b:
            if i == o:
                c = "Common Element Found"
                return c
    return c

a=list()
b=list()

n = int(input("Enter size of your first list : "))
print("Enter the element of the first list : ")
for i in range(int(n)):
    k = int(input(""))
    a.append(k)

m = int(input("Enter size of your second list : "))
print("Enter the element of the second list : ")
for i in range(int(n)):
    k = int(input(""))
    b.append(k)

print("Result = ", aa(a,b))
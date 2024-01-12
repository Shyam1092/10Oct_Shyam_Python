li = []

n = int(input("Enter number of elements : "))

for i in range(0,n):
    b = (input("Enter your elements : "))
    li.append(b)

c = tuple(li)
print(c)
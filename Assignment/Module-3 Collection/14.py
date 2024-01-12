li = []
n = int(input("Enter number of elements : "))
for i in range(1, n+1):
    a = int(input("Enter your elements : "))
    li.append(a)
li.sort()

print("the second smallest number is : ",li[1])
a = int(input("How many numbers you have to add : "))
li = []

for i in range(a):
    li.append(input("Enter your number : "))

li2 = []
for i in range(a):
    if li[i] not in li2:
        li2.append(li[i])

print("\nNew list is : ",li2)
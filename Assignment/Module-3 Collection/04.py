a = []
b = int(input("How many numbers you have to add : "))

for i in range(b):
    c = int(input("Enter your numbers : "))
    a.append(c)

print("Maximum number is : ",max(a))
print("Minimum number is : ",min(a))
print("Sum of all numbers is : ",sum(a))
n = int(input("Enter your number : "))
a = 0

for i in range(1,n):
    if (n % i == 0):
        a = a +i
if (a == n):
            print("The number is a perfect number")
else:
            print("The number is not a perfect number")
def a(n):
    if n>=10 and n<=99:
        print(n,"The number is in the range")
    else:
        print(n,"The number is not in the range")

print("Enter number between 10 to 99")
b = int(input("Enter your number : "))
a(b)
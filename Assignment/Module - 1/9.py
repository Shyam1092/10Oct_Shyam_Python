a=int(input("Enter your first Value : "))
b=int(input("Enter your second Value : "))
c=int(input("Enter your third Value : "))

if a==b or b==c or c==a:
    print("The answer is 0")
else:
    print(f"The answer is {a+b+c}")
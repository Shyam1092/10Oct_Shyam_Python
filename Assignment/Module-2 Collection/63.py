n = int(input("Enter your number : "))

div =[1]

for i in range(2,n):
    if (n % i)==0:
        div.append(i)
print("sum of All divisors : ",sum(div))
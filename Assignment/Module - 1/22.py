a = input("Enter you string : ")
b=0

for i in a:
    b=b+1
c=a[0:2]+a[b-2:b]
print("Your output is : ",c)
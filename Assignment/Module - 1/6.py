#Swap without variables

a=int(input("Enter your first Value"))
b=int(input("Enter your second Value"))

a,b=b,a

print(a)
print(b)


#Swap with variables

a=int(input("Enter your first Value"))
b=int(input("Enter your second Value"))

c=a
a=b
b=c

print(a)
print(b)
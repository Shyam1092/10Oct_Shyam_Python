'''n = int(input("Enter your line nuber to read : "))
f = open("text.txt","r")
for i in range(n):
    print(f.readline())'''

with open("text.txt","r")as a:
    b=a.readlines()
print(b[-1])
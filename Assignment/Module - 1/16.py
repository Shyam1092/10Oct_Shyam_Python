a=input("Enter your string : ")
b=input("Enter your word : ")
c=[]
d=0

c=a.split(" ")

for i in range (0,len(c)):
    if (b==c[i]):
        d=d+1
print("Count of the word is : ")
print(d)
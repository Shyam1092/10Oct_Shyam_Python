a=input("Enter your string : ")

b={}

for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

print("number of string charaters is : " + str(b))
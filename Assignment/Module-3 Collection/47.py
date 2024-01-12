a = input("Enter your string : ")

b = {}

for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

for key in b:
    print(key,":",b[key])
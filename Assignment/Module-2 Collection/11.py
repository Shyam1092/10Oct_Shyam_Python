def a(aa):
    num=[]
    for j in aa:
        if j not in num:
            num.append(j)
    
    print("Unique elementes is : ", num)

aa=[]
n = int(input("Enter number of elements : "))
for i in range(0,n):
    bb = int(input(""))
    aa.append(bb)

print("The list is : ",aa)
a(aa)
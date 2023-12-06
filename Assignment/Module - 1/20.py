a = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    b=input('Enter your Elements : ' + str (i+1) )
    a.append(b)

c=len(a[0])
d=a[0]
for j in a:
    if(len(j)>c):
        c=len(j)
        d=j
print("the longest word is : ", d)
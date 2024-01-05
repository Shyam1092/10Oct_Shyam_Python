a = {'a':23,'b':56,'c':34,'d':76,'e':78,'f':14,'g':68,'h':89,'i':47,'j':93}
print(a)

print("3 highest value : ")

x = list(a.values())
d = dict()
x.sort(reverse=True)
x=x[:3]
for i in x:
    for j in a.keys():
        if(a[j]==i):
            print(str(j)+" : "+str(a[j]))
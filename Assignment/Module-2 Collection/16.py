li1 = [1,2,3,4,5,6]
li2 = [1,2]

print("Original list : " + str(li1))
print("Sub list : " + str(li2))

b = 0
if((set(li2)&set(li1))==set(li2)):
    b = 1

if (b):
    print("List have sub list")
else:
    print("List don't have sub list")
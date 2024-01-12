a = {'B':2,'D':4,'C':3,'A':1}

l = list(a.items())

dict=dict(l)
print("Dictonary : ",dict)

l.sort()
print("Ascending order is : ",l)

l = list(a.items())
l.sort(reverse=True)
print("Descending order : ",l)
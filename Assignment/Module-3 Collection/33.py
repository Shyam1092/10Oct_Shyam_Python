a =  {'A':1,'B':2}
b =  {'C':3,'D':4}
c =  {'E':5,'F':6}

e = {}

for d in(a,b,c):
    e.update(d)

print("Before : ",a,b,c)
print("After : ",e)
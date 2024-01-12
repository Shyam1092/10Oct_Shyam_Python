d1 =  {'a':100,'b':200, 'c':300}
d2 =  {'a':300,'b':200, 'd':400}

a = {}

for key,value in d1.items():
    a[key] = a.get(key, 0) + value

for key, value in d2.items():
    a[key] = a.get(key, 0) + value

print(d1)
print(d2)
print(a)
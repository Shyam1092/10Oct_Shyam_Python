n = [('A',1),('A',2),('A',3),('B',1),('B',2)]

d = {}

for a, b in n:
    d.setdefault(a,[]).append(b)

print("Before : ", n)
print("After : ", d)
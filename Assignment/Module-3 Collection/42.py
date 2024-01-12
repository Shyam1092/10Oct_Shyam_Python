a = [{'a':100},{'b':200}, {'c':300},{'a':300},{'b':200}, {'d':400}]

print("Original list is : ", a)

b = set(n for m in a for n in m.values())

print("After : ", b)
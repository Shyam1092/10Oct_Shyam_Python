with open("text.txt")as f:
    a = f.readlines()

print(a)

a = [x.strip() for x in a]
print(a)
import random

lines = open('file.txt').read().splitlines()
myline =random.choice(lines)
print(myline)
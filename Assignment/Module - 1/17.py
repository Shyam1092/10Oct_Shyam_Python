a = input('Enter your frist string : ')
b = input('Enter your second string : ')

c = b[:2] + a[2:]
d = a[:2] + b[2:]

e = c + " " + d

print("Your string is : ", e)
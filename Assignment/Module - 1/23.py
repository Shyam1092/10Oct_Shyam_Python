a = input("Enter your string : ")
b = input("Enter your word that you have to add : ")

c = len(a)//2

d = a [:c] + b + a [c:]

print(d)
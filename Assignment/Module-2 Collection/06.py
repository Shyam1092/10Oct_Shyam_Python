def a(b):
    c=0
    for i in b:
        if len(i) >= 2 and i[0] == i[-1]:
            c +=1
            return c
        
d = input("Enter your list : ")
e = d.split(',')
g = a(e)

print(f"Number of the strings with the same first and last character : {g}")

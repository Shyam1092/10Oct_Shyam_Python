a = "text.txt"
with open(a,"r") as b:
    w = b.read().split()
    c = len(max(w, key=len))
    r = [t for t in w if len(t)==c]

print("The longest word is : ",r)

b.close()
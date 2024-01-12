f = open("text.txt","r")
s=" "

for i in range(0,100):
    s=s + f.read(i)

print(s)
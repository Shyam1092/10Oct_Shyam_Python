with open("text.txt","r") as a, open("abcd.txt","a")as b:
    for l in a:
        b.write(l)

print("Task is done")
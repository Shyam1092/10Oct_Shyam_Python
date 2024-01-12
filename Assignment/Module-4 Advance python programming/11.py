l = ["abcd","efgh","ijhk"]

with open("text.txt","a+") as f:
    for i in l:
        f.write("%s\n"%i)
    print("File written successfully")

f.close()
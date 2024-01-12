t = open("text.txt","r")

d = dict()

for li in t:
    li = li.strip()

    li = li.lower()


    w = li.split(" ")

    for wo in w:
        if wo in d:
            d[wo] = d[wo] + 1
        else:
            d[wo] = 1

for key in list(d.keys()):
    print(key,":", d[key])
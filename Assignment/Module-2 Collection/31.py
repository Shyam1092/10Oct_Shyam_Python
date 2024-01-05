n = (('A',1),('B',2),('C',3),('D',4))
print("Before : ", n)

a = dict((x, y) for x,y in n)
print("After : ", a)
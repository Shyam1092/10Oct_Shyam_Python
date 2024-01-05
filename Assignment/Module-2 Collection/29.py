a = [('A',1),('B',2),('C',3),('D',4)]

print("Before : ", a)

b = [[i for i, j in a],[j for i,j in a]]

print("After : ", b)
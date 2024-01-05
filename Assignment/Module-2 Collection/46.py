a = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]

b = {}
c = 0
for i in a:
    if i['item'] not in b:
        b[i['item']]=i['amount']
        
print(b)
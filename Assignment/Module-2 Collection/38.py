a = {'name': 'hansaben','subject':'python','ID':'101'}

print(a.keys() >= {'name', 'subject'})
print(a.keys() >= {'name', 'hansaben'})
print(a.keys() >= {'subject', 'ID'})
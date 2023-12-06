a = input("Enter your string : ")

count = a.count(a)
if 'poor' in a:
    print(a.replace("poor", "good"))
elif 'not' in a:
    print(a.replace("not", "good"))
else:
    print(a)
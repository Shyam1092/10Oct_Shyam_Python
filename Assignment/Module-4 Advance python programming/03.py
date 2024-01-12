a = open("text.txt", "w")

b= ("this is python/n this is not python")
a.writelines(b)
print(b)
a.close()
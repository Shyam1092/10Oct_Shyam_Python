class rectangle():
    def __init__(self, b, l):
        self.b = b
        self.l = l

    def area(self):
        return self.b*self.l
    
y = int(input("Enter lenght of rectangle : "))
z = int(input("Enter wight of rectangle : "))

n = rectangle(y, z)
print("Area of rectangle is : ",n.area())
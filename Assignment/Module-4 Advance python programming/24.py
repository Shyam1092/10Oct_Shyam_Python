class circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r**2*3.14
    
    def p(self):
        return 2*self.r*3.14
    
a = int(input("Enter your number : "))
n = circle(a)
print(n.area())
print(n.p())
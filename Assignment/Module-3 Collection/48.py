def a(n):
    if n == 0:
        return 1
    else:
        return n * a (n-1)
    
n = int(input("Enter your number : "))

print(a(n))
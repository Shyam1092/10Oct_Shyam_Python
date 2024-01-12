try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")


try:
    file = open("text.txt", "r")
    contents = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File contents:", contents)
finally:
    if file:
        file.close()
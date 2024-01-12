try:
    u = int(input("Enter odd number : "))
    if  u % 2 == 0:
        raise ValueError ("Even numbers are not allowed")
    else:
        print("You enter :",u)
except ValueError as e:
    print(f"Error : {e}")
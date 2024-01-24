da = {}

def a1():
    print("\nFruit market manager")

def a2():
    print("\nCustomer panel")

def f():
                
    key = input("Enter your Fruit name  : ")
    value1 = int(input("Enter your quantity (in kg) : "))
    value2 = int(input("Enter your price (for kg): "))
    da[key] = value1,value2

def bbb():
    print("\n1) Add fruit Stock")
    print("2) View fruit Stock")
    print("3) Update fruit Stock\n")

    a2 = int(input("Enter your Choice : "))

    if a2 == 1:
        print("\nAdd fruit Stock\n")
        
        f()

        j = input("\nDo you want to perform more options : press y for yes and n for no : ")
        if j == 'y':
            f()
        else:
            bbb()
                
    elif a2 == 2:
        print("View fruit Stock\n")
        print(da)

    elif a2 == 3:
        print("Update fruit Stock\n")
        
        f()

    else:
        print("Invelid Choice...Enter valid choice")


def ccc():
    print("\n1) Add fruit Stock")
    print("2) View fruit Stock")
    print("3) Update fruit Stock\n")

    a2 = int(input("Enter your Choice : "))

    if a2 == 1:
        print("\nAdd fruit Stock\n")
        
        f()

        j = input("\nDo you want to perform more options : press y for yes and n for no : ")
        if j == 'y':
            f()
        else:
            bbb()
                
    elif a2 == 2:
        print("View fruit Stock\n")
        print(da)

    elif a2 == 3:
        print("Update fruit Stock\n")
        
        f()

    else:
        print("Invelid Choice...Enter valid choice")
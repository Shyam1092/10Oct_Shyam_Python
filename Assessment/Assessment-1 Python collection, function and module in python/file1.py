from file2 import *

da = {}

print("Welcome to the fruit market\n")
print("1) Manager")
print("2) Customer\n")
b1 = int(input("Select your Role : "))

if b1 == 1:
    a1()

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

        p = input("\nDo you want to perform more options : press y for yes and n for no : ")
        if p == 'y':
            f()
        else:
            ccc()
                
    elif a2 == 2:
        print("View fruit Stock\n")
        print(da)

        e = input("\nDo you want to perform more options : press y for yes and n for no : ")
        if e == 'y':
            f()
        else:
            bbb()

        w = input("\nDo you want to perform more options : press y for yes and n for no : ")
        if w == 'y':
            f()
        else:
            ccc()

    elif a2 == 3:
        print("Update fruit Stock\n")
        
        f()

        i = input("\nDo you want to perform more options : press y for yes and n for no : ")
        if i == 'y':
            f()
        else:
            bbb()

        u = input("\nDo you want to perform more options : press y for yes and n for no : ")
        if u == 'y':
            f()
        else:
            ccc()

    else:
        print("Invelid Choice...Enter valid choice")

elif b1 == 2:
    a2()

else:
    print("Invelid Choice...Enter valid choice")
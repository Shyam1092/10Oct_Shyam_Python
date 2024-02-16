import random
import sqlite3

print("Billing Software\n")
print("Coustomer details\n")


class main():

    def a(self):
    #coustomer name = cn
    #coustomer phone number =  cp
    #bill no = bn
        self.cn = input("Coustomer Name : ")
        self.cp = int(input("Enter your phone number : "))
        self.bn = random.randint(11111,99999)
        print("Bill No. : ",self.bn)

    def b(self):
        print("\nCosmetics")
        self.co1 = int(input("Bath Soap : "))
        self.co2 = int(input("Face Cream : "))
        self.co3 = int(input("Face Wash : "))
        self.co4 = int(input("Hair Spray : "))
        self.co5 = int(input("Body Lotion : "))

        #for  printing gro
        #gr 1 to 5 is for grocery
        print("\nGrocery")
        self.gr1 = int(input("Rice : "))
        self.gr2 = int(input("Food Oil : "))
        self.gr3 = int(input("Daal : "))
        self.gr4 = int(input("Wheat : "))
        self.gr5 = int(input("Suagr : "))

        #for printing oth
        #ot 1 to 5 is for others
        print("\nOthers")
        self.ot1 = int(input("Maza : "))
        self.ot2 = int(input("Coke : "))
        self.ot3 = int(input("Frooti : "))
        self.ot4 = int(input("Nimkos : "))
        self.ot5 = int(input("Biscits : "))

    def c(self):
        # cos is sum of cosmetics
        #cost is fianl total of cosmetics
        self.cos1 = self.co1 * 40
        self.cos2 = self.co2 * 140
        self.cos3 = self.co3 * 240
        self.cos4 = self.co4 * 230
        self.cos5 = self.co5 * 260
        self.cost = self.cos1 + self.cos2 + self.cos3 + self.cos4 + self.cos5
        self.cost1 = (self.cost * 5)/100
        #cost1 = cost(cost*80/100)

        # grs is sum of grocery
        # grst is final total of grocety
        self.grs1 = self.gr1 * 180
        self.grs2 = self.gr2 * 90
        self.grs3 = self.gr3 * 80
        self.grs4 = self.gr4 * 60
        self.grs5 = self.gr5 * 170
        self.grst = self.grs1 + self.grs2 + self.grs3 + self.grs4 + self.grs5
        self.grst1 = (self.grst * 5)/100
        #grst1 = grst-(grst*80/100)

        # ots is sum of others 
        #otst is final sum of others
        self.ots1 = self.ot1 * 15
        self.ots2 = self.ot2 * 50
        self.ots3 = self.ot3 * 60
        self.ots4 = self.ot4 * 20
        self.ots5 = self.ot5 * 20
        self.otst = self.ots1 + self.ots2 + self.ots3 + self.ots4 + self.ots5
        self.otst1 = (self.otst * 5)/100
    #otst1 = otst(otst*80/100)
        
    def d(self):
        print("\n\nBill Area\n")
        print("Welcome to hsnsn's Retail\n")
        print("Bill No. : ",self.bn)
        print("Coustomer Name : ",self.cn)
        print("Coustomer Phone No. : ",self.cp)

    def e(self):

        print("\npoduct name, Quantity, Price\n")
        
        if self.co1 >= 1:
            print("Bath Soap", self.co1, self.cos1)

        if self.co2 >= 1:
            print("Face cream", self.co2, self.cos2)

        if self.co3 >= 1:
            print("Face wash", self.co3, self.cos3)

        if self.co4 >= 1:
            print("Hair Spray", self.co4, self.cos4)

        if self.co5 >= 1:
            print("Body Lotion", self.co5, self.cos5)


        # foe grocerys
        if self.gr1 >= 1:
            print("Rice", self.gr1, self.grs1)

        if self.gr2 >= 1:
            print("food oil", self.gr2, self.grs2)

        if self.gr3 >= 1:
            print("Daal", self.gr3, self.grs3)

        if self.gr4 >= 1:
            print("Wheat", self.gr4, self.grs4)

        if self.gr5 >= 1:
            print("Sugar", self.gr5, self.grs5)


        # for others
        if self.ot1 >= 1:
            print("Maza", self.ot1, self.ots1)

        if self.ot2 >= 1:
            print("Coke", self.ot2, self.ots2)

        if self.ot3 >= 1:
            print("Frooti", self.ot3, self.ots3)

        if self.ot4 >= 1:
            print("Nimkos",self.ot4, self.ots4)

        if self.ot5 >= 1:
            print("Biscuits", self.ot5, self.ots5)

        print("\nTotat of cosmetics is : ",self.cost)
        print("Tax of cosmatics",self.cost1)
        print("Total of grocery",self.grst)
        print("Tax of grocery",self.grst1)
        print("Total of others",self.otst)
        print("Tax of others",self.otst1)
        self.total = self.cost + self.cost1 + self.grst + self.grst1 + self.otst + self.otst1
        print("\n\nYour total Bill is : ",self.total)

    def f(self):
        # sql part

        try:
            db=sqlite3.connect("shop1.db")
            #print("Database connected successfully")
        except Exception as e:
            print(e)

        tbl_create="create table shop1(ID integer primary key autoincrement, Customer_Name text, phone_Number integer, Bill_No integer, Bath_Soap integer, Face_Cream integer, Face_Wash integer, Hair_Spray integer, Body_Lotion integer, Rice integer, Food_Oil integer, Daal integer, Wheat integer, Sugar integer, Maza integer, Coke integer, Frooti integer, Nimkos integer, Biscuits integer, Total_Cosmetics integer, Total_Grocery integer, Othre_Total integer, Cosmetics_Tax integer, Grocery_Tax integer, Others_Tax integer, Grand_Total integer)"
        try:
            db.execute(tbl_create)
            #print("Table created...")
        except Exception as e:
            print()

        try:
            db.execute("insert into shop1(Customer_Name, phone_Number, Bill_No, Bath_Soap, Face_Cream, Face_Wash, Hair_Spray, Body_Lotion, Rice, Food_Oil, Daal, Wheat, Sugar, Maza, Coke, Frooti, Nimkos, Biscuits, Total_Cosmetics, Total_Grocery, Othre_Total, Cosmetics_Tax, Grocery_Tax, Others_Tax, Grand_Total)values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(self.cn, self.cp, self.bn, self.co1, self.co2, self.co3, self.co4, self.co5, self.gr1, self.gr2, self.gr3, self.gr4, self.gr5, self.ot1, self.ot2, self.ot3, self.ot4, self.ot5, self.cost, self.grst, self.otst, self.cost1, self.grst1, self.otst1, self.total))
            db.commit()
            #print("Data inserted!")
        except Exception as e:
            print(e)

    def g(self):
        try:
            ab.a()
            ab.b()

            j = input("\nIf you want to clear all then press c \nFor Generate your bill Press g : ")
            if j == 'c':
                ab.a()
                ab.b()
            elif j == 'g':
                ab.c()
                ab.d()
                ab.e()
                ab.f()
            else:
                jj = input("\nIf you want to continue then Press c to continue \nfor exit press e : ")
                if jj == 'c':
                    print("\nInvalide input try again with proper input : ")
                    ab.g()
                else:
                    exit()
        except Exception as h:
            print(h)
            o = input("\nIf you want to continue then Press c to continue \nfor exit press e : ")
            if o == 'c':
                ab.g()

# a = to take coustomer information
# b = is for input
# c = for sum of all
# d = for coustomer information
# e = for last show and billing
# f = sql part
try:
    ab = main()
    ab.a()
    ab.b()

    j = input("\nIf you want to clear all then press c \nFor Generate your bill Press g : ")
    if j == 'c':
        ab.a()
        ab.b()
    elif j == 'g':
        ab.c()
        ab.d()
        ab.e() 
        ab.f()
    else:
        jj = input("\nIf you want to continue then Press c to continue \nfor exit press e : ")
        if jj == 'c':
            print("\nInvalide input try again with proper input : ")
            ab.g()
        else:
            exit()
except Exception as h:
    print(h)
    o = input("\nIf you want to continue then Press c to continue \nfor exit press e : ")
    if o == 'c':
        ab.g()
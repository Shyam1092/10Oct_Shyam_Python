s1=int(input ("Enter your subject 1 marks"))
s2=int(input ("Enter your subject 2 marks"))
s3=int(input ("Enter your subject 3 marks"))
s4=int(input ("Enter your subject 4 marks"))

if s1>=40 and s2>=40 and s3>=40 and s4>= 40:

    total = s1+s2+s3+s4
    print("your total is :",total)

    pr=total/4
    print("your pr is:", pr)

    if pr >=70:
        print("you get A+")
    elif pr >=60:
        print("you get A")
    elif pr>=50:
        print("you get B")
    elif pr>=40:
        print("you get C")
else:
    print("you are fail")
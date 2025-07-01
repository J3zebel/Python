'''if 10>5:
   print("10 is less than 5")

if 10<5:
    pass
else:
    print("10 is less than 5")

name = input("Enter Your Name:")
print("Welcome" +name)

x = input("Enter Any Number:\n")
if type(x)==str:
    num=int(x)
    print(num+10)'''


x=6
if x>5:
    print("x is greter than 5")
    if x>7:
        print("x is greter than 7")
        if x>10:
            print("x is greater than 10")
        elif x == 10:
            print("x is equal to 10")
        else:
            print("x is less than 10")
    else:
        print("x is less than 7")
else:
    print("x is less than 5")
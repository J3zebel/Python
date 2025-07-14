print("1.Login")
print("2.Register")
print("3.Dashboard")
print("4.Exit")
n = int(input("Choose any one from above:"))

if n == 1 :
    s = input("E-mail   : ")
    d= input("Password : ")
        
    print("Email    : ",s)
    print("Password : ",d)

elif n == 2:
    name = input("Enter your name:")
    email = input("Enter your email:")
    password = input("Enter your password:")

    print("Name     : ",name)
    print("Email    : ",email)
    print("Password : ",password)

elif n == 3:
    print("Welcome Dashboard")
else:
    print("Thankyou")
        

    
    

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.balan = 0
        
    def welcome(self):
        print(f"Welcome {self.name}")
        print("your email : ",self.email)
        print("your password : ",self.password)

    def balance(self):
        print("Your Balance is  : ",self.balan)
        
def user():
    name = input("Enter Your name:")
    email = input("Enter Your email:")
    password = input("Enter Your password:")
    
    user1 = User(name,email,password)
    user1.welcome()
    user1.balance()

user()


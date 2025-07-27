from Bank import User

def checkuser(users):
    email = input("Enter email:")
    password = input("Enter password:")
    for i in users:
        if i.getEmailId() == email and i.getPassword() == password:
            print(i.getusername())
        
def checkpassword(users):
    password = input("Enter password:")
    for i in users:
        if i.getPassword() == password:
            print("valid password")
        else:
            print("Invalid password")


def main():
    users = []

    for i in range(2):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = User(name,email,password)
        users.append(user)

    print(users)

    checkuser(users)
    checkpassword(users)
    

if __name__ == "__main__":
    main()
from Bank import User,Bank

def checkuser(users):
    email = input("Enter email:")
    password = input("Enter password:")
    for i in users:
        if i.getEmailId() == email and i.getPassword() == password:
            print(i.getusername())
        
def createuser():
    name = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    new_user = User(name, email, password)
    print("You are registered")
    return new_user



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
    new_user = createuser()
    users.append(new_user)

    

if __name__ == "__main__":
    main()
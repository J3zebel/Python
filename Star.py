n = int(input("Enter a number: ")) 
for i in range(1, n+1):          
    print("* " * i)


n = int(input("Enter a number:"))
for i in range(n+1):
    print("",end="")
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
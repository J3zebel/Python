n=5
m="-----------------"                       #5 * in 1 line
print("*"*n)
print(m)



n=5
for i in range (n):
    for j in range (n):                         #5 * IN 5 LINE
        print("*", end=" ")
    print()
print(m)



n=5
for i in range (n):
    for j in range (i+1):
        print("*", end=" ")                 #right triangle
    print()
print(m)


n=5
for i in range (n):
    for j in range (i,n):
        print("*", end=" ")                 #inverted right triangle
    print()
print(m)

n=5
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")               # left triangle
    for j in range(i+1):                
        print("*",end=" ")    
    print()
print(m)


n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")                  #inverted left triangle
    for j in range(i,n):
        print("*",end=" ") 
    print()
print(m)


n=5
for i in range(n):
    for j in range (i,n):
        print(" ",end=" ")
    for j in range (i):                         # Hill pattern
        print("*",end=" ")
    for j in range(i+1):
            print("*",end=" ")
    print()
print(m)


n=5
for i in range (n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):                      #Inverted Hill pattern
        print("*",end=" ")
    for j in range (i,n):
        print("*",end=" ")
    print()
print(m)


n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")                      #pyramid
    for j in range(i):
        print("*",end="   ")
    print()
print(m)


n=5
for i in range (n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i):
        print("*",end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print()
for i in range (n):                         #diamond
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()


myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

list1 = [1, 2, 4, 5, 6]
Tuple = tuple(list1)
print("\nTuple using List:", Tuple)

Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nElements of set: ") 
for i in Set: 
    print(i) 
print()


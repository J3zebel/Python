#Conditional Statement
if 10>5:
   print("10 is less than 5")                   #if

if 10<5:
    pass
else:                                           #if...else
    print("10 is less than 5")

name = input("Enter Your Name:")
print("Welcome" +name)                      #string concatenation

x = input("Enter Any Number:\n")
if type(x)==str:
    num=int(x)                              #str to int => typecasting
    print(num+10)


x=6
if x>5:
    print("x is greter than 5")
    if x>7:
        print("x is greter than 7")
        if x>10:
            print("x is greater than 10")
        elif x == 10:                               #nested if
            print("x is equal to 10")
        else:
            print("x is less than 10")
    else:
        print("x is less than 7")
else:
    print("x is less than 5")

#Loops
x=4
while x < 10:
    print(x)                #while
    x=x+1
else:
    print(x)

#for 
for i in range(10):       #range
    print(i)

for i in range(1,11):       # start,end
    print(i)

for i in range(11,0,-2):     #start,end,iteration   default=>+1
    print(i)
else:
    print("Loops end")       #we can use else in both for and while

#Nested loop
for i in range(1,6):
    for j in range(1,4):
        print("(",i,",",j,")")
    print("1st loop "+str(i))
else:
    print("All loops are over")

for i in range(1,11):
    print(i)
    if i == 5:
        break                   #break or stop the loop


for i in range(1,11):
    if i == 5:
        continue                #skips
    print(i)

for i in "Anish":
    print(i,end=(" "))          #print i with space

string = "Helloworld"
print(len(string))                  #calculate string length

char = "A"
print(ord(char))                    # char to ascii value
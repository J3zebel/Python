# n = int(input("Enter a number:"))
# for i in range(1,11):
#     print(i,"*",n,"=",i*n)




def mul(a,b):
    if a > 10:
        return 
    print(f"{a} * {b} = {a*b}")
    mul(a+1,b)

b = int(input("Enter a value:"))
obj = mul(1,b)      
obj
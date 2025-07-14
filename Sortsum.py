list = [1,2,3,3,5,10,20,10,22,8,18]
#for i in range(len(list)):
i = 0
x = True
while x:
    for j in range(i+1,len(list)):
        if list[i]+list[j] == 20:
            print([i],[j])
            x = False
    i += 1
    
    
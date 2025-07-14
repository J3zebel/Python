a = [3,4,56,7,2,67,8,5,6,3,6]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print(a)
    
    
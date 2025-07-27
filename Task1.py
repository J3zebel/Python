list = [1,2,4]
list2 = [1,3,4]
a = list + list2
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print(a)
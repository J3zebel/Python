list1 = [1,1,3,3,4,4,4,5,6,7,7]
r = list(set(list1))
if len(list1) == len(r):
    print(r)
else:
    for i in range(len(r),len(list1)):
        r.append("_")
    print(r)
  
     
a = [1,1,3,4,4,4,5,6,7,7]
s = []
for i in range(len(a)):
    if a[i] in s:
        pass
    else:
        s.append(a[i])
for i in range(len(s),len(a)):
    s.append("_")
print(s)
             

a = [1,1,3,4,4,4,5,6,7,7]
if a[0] == a[1]:
    a.remove(a[1])
print(a)
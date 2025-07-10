u = input("Enter a string:")
ans = ""
for i in u:
    ans = i + ans 
print(ans)


u = input("Enter a string:")
ans = ""
arr = u.split()
for i in arr:
    rev =" "
    for j in i:
        rev = j + rev
    ans += rev
print(ans)

n = input("Enter anything:").lower()
ans = ""
for a in n:
    if a.isalpha():
        ans = ans + a
i = 0
j = len(ans)-1
while i<j:
    if ans[i] != ans[j]:
        print("Its not palindrome")
        break
    i+=1
    j-=1
else:
    print("Its palindrome")



n = input("Enter anything:")
ans = ""
for i in n:
    if i.isalpha():
        ams = ans + i
rev=""
for i in ans :
    rev = i + rev
if rev == ans:
    print("This is Palindrome")
else:
    print("This is not palindrome")

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

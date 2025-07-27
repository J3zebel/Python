def Vowels():
    list1 = ["flight","flower","flag"]
    list2 = ["a","e","i","o","u"]
    count = 0
    for i in list1:
        for j in i:
            if j in list2:
                count += 1
    return count

vowels = Vowels()
print(vowels)
dob=input("Enter your Birth year:")
age=2025-int(dob)
print(age)
if age <= 12:
    print("Child")
elif age < 18:
        print("Teenage")
elif age == 18:
        print("Teenage & Eligible for voting")
elif age == 19:
        print("Teenage & eligible for voting")
elif age >= 20 and age < 40:
        print("Adult & eligible for voting")
elif age >= 40 and age < 60:
        print("Citizen & eligible for voting")
else:
        print("Senior Citizen & eligible for voting")
 
        
        

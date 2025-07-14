print("Hello world")

x=10
print(type(x))

x=10.9
print(type(x))

x=True
print(type(x))


x="Swathi"
print(type(x))

#Getting input and converting it
#You'd run this in a terminal, not Code Runner, to enter input
value_str = input("Enter a number: ")
value_int = int(value_str)
print(f"Your number + 1 is: {value_int + 1}")
        
#Demonstrating conversions
print(int("10"))
print(float("3.14"))
print(str(123))


print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(""))
print(bool("hello"))
print(bool(None))
        
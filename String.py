course = "Python Programming"
print(course.upper())           # converts all characters in a string to uppercase. 
print(course.lower())           # converts all characters in a string to lowercase. 


phrase = "hello world"          #capitalizes the first letter of every word in a string.
print(phrase.title())

user_input = "   Python Programming   "
print(user_input)
print(user_input.strip())       #removes any whitespace from both the beginning and end of a string. 
print(user_input.lstrip())      #removes whitespace from the beginning.
print(user_input.rstrip())      #removes whitespace from the end.


course = "Python Programming"           #locate a character or a sequence,it returns index no
print(course.find("Pro"))
print(course.find("pro"))  #Case-sensitive, returns -1

course = "Python Programming"
print(course.replace("Python", "Java"))     #swap out characters or sequences
print(course.replace("P", "J"))   #Replaces all 'P's

course = "Python Programming"
print("Python" in course)       #in checks if a substring is present.
print("swift" not in course)    #not in checks if a substring is *not* present.

name = "Alice"
print(name[0])      #indexing-get individual characters
print(name[-1])

course = "Python Programming"
print(course[0:6])  #Characters from index 0 up to (but not including) 6
print(course[7:])   #From index 7 to the end
print(course[:6])   #From the beginning up to (but not including) 6
print(course[:])    #A copy of the entire string


text = "Hello"
print(len(text))        #number of characters in a string

message = "Python \"Programming\" is fun."   #To include a double quote inside a double-quoted string.
print(message)

message = 'Python \'Programming\' is fun.'   #To include a single quote inside a single-quoted string.
print(message)

path = "C:\\Users\\User\\Documents"         #To include an actual backslash.
print(path)

multiline = "Hello\nWorld"                  #For a new line. 
print(multiline)

#Formatted strings offer a super clean and modern way to embed variables 
#and expressions directly into string literals. You just put an f (or F) before the opening quote. 
#you use curly braces {} to place any valid Python expression, and it will be evaluated and inserted into the string at runtime. 
first = "John"
last = "Doe"
full_name = f"{first} {last}"
print(full_name)

x = 5
y = 3
calculation = f"The sum of {x} and {y} is {x + y}."
print(calculation)

integer_num = 10
float_num = 3.14
complex_num = 1 + 2j
print(type(integer_num))
print(type(float_num))
print(type(complex_num))        # Numbers in the form a+bj



print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)       #always returns a float
print(10 // 3)      #returns an integer
print(10 % 3)
print(10 ** 3)      #left to the power of right
        

# This is my favorite food :)
# print("I like roasted chicken!")
# print("It's really sweet!")

# Variable = Container of value (string, integer, float, and boolean)
# String ( sequential of characters)
first_name = "Ziha"
food = "Roasted chicken"
email = "something@ziha.io"

# Use formatted string
# print(f"Hello {first_name}, how are you today?")
# print(f"You like {food}")
# print(f"Your email is: {email}")


# Integers
age = 25
quantity = 6
num_of_students = 22

# print(f"You are {age} years old!")
# print(f"You're buying {quantity} of items today.")
# print(f"Your group has {num_of_students} students.")

# Float (Number with decimal portion)
price = 6.99
gpa = 4.7
distance = 20.5

# print(f"The price is ${price}")
# print(f"I graduated with a GPA of {gpa} in IT at IUEA.")
# print(f"We covered a {distance}Km today!")

# Boolean(True or False)
is_under_age = False
is_macbook_m4_in_stock = False
is_online = True

# print(f"Are you a miner?: {is_under_age}")

# if(is_under_age):
#     print("Yes, I am 17 years old! :(")
# else:
#     print("Your are NOT a child.")


# if(is_macbook_m4_in_stock):
#     print("MacBook M4 pro is available at a good price! :)")
# else:
#     print("Sorry, MacBook M4 pro is out of stock! :(")


# if is_online:
#     print("He is online :)")
# else:
#     print("He is offline :(")

# ####################################################################

# Typecasting
name = ""
age = 26
gpa = 4.7
is_student = False

# print(type(name))  # str
# print(type(age))  # int
# print(type(gpa))  # float
# print(type(is_student))  # bool


int_gpa = int(gpa)
# print(int_gpa)

float_age = float(age)
# print(float_age)

str_age = str(age)
# print(f"The type of str_age is: {type(str_age)} {str_age}")

str_age += "1"

# print(str_age)

bool_name = bool(name)
# print(bool_name)

# input() function
# goal = input("What is your gaol in IT Security?: ")
# age = int(input("How old are you now?: "))

# print(f"Ziha is goal in IT is: {goal}")
# print(f"We are in 2024 and you are {age} years old.")
# age = age + 2
# print(f"I only see the positive, with Hard work, focus and pray you will achieve your goal by the age of {age} years old.")

# Exercise 1 Rectangle Area Calc
# A = wl (w: width and l: Height)

# length = float(input("Enter the length of the Rectangle: "))
# length = input("Enter the length of the Rectangle: ")
# width = float(input("Enter the width of the Rectangle: "))
# width = input("Enter the width of the Rectangle: ")
# area = length * width
# print(f"The length is {length} cm and the width is {width} cm therefore the Area of the rectangle is {area} cm")

# Exercise 2 Shopping Cart Program
# item = input("What item would like to buy for Christmas seasons?: ")
# price = float(input("What is the price of the item?: "))
# quantity = int(input("How many would you like?: "))
# total_price = price * quantity

# print(f"For Christmas I want {quantity} {item} which cost ${price} per item, so the total price is ${total_price}. :)")


# Arithmetic Operators
friends = 10

# augmented assignment operator
# friends += 1 .
# friends -= 1
# friends *= 5
# friends /= 2
# friends **=2 # exponentiation
remainder = friends % 3    # modulus = the remainder of any division

# print(f"friends: {friends} and remainder: {remainder}")

# Built In Math related functions
x = 3.14
# y = -4
y = 4
z = 5

# result = round(x) # Round to the Nearest whole number
# result = abs(y) # absolute value = distance away from zero as a whole number
# result = pow(4, 3) # power function(base , exponent)
# result = max(x, y, z) # max function find the maximum value of various value
result = min(x, y, z)

# print(result)

# Import Math functions
import math

PI = math.pi
# print(PI)

e = math.e # exponentiation constant
# print(e)

# x = 15.1
x = 3.9

# result = math.sqrt(x) #square route
# result = math.ceil(x) # round floating number up
result = math.floor(x) # round floating number down

# print(result)

# Exercise = Calc the Circumference of a circle
# formula (c = 2*PI* r) r: radius
# radius = float(input("Enter the radius of a circle: "))

# circumference = round(2 * PI * radius, 2) # round to 2 digits
# print(f"A circle with radius:{radius}, its circumference is: {circumference}cm")


# Exercise 2 = Calc the Area of a circle
# formula = A = PI*r^^2

# radius = float(input("Enter radius: "))

# area = round(PI * pow(radius, 2), 2)
# print(f"A circle with radius:{radius} ita Area is: {area} cm^2")

# Exercise = Find the Hypotenuse of Right triangle
# formula => c = sqrt(pow(a, 2) + pow(b, e))

# length_a = float(input("Enter the length of side a: "))
# length_b = float(input("Enter the length of side b: "))

# hypotenuse = math.sqrt(pow(length_a, 2) + pow(length_b, 2))
# print(f"The Hypotenuse of Side a: {length_a}cm and side b: {length_b}cm, is: {hypotenuse}cm")

# ########################################################################

# IF-ELSE Statements
#  Do some code only IF some condition is True Else do something else
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible for a credit card.")
# elif age >=16:
#     print("Almost there! Wait til you become 18+ years old! :)")
# else:
#     print("You are NOT eligible for a credit card, You must be 18+! :(")


# response = input("Do you want food for lunch (Y/N)?: ")

# if response == "Y":
#     print("It's lunch time have some food 🤭")
# else:
#     print("OOOh okay! 😞")


# name = input("Enter your name: ")

# if name == "":
#     print("You failed to enter your name 👿")
# else:
#     print(f"Good afternoon, {name} 👋")


##############################################################################

# Logical Operators = Evaluate multiple conditions (or, and, not)
#   or = at least one condition must be True
#   and = bot condition must be True
#   not = inverts the condition not False, not True

# or operator
# temp = 32
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The Event is cancelled! 😢")
# else:
#     print("The Event is on schedule")

# and operator
# temp = 22
# is_sunny = True

# if temp >= 27 and is_sunny:
#     print("It's a pretty HOT outside! 🥵")
#     print("IT'S SUNNY 🌞")
# elif temp < 0 and is_sunny:
#     print("It cold outside 🥶")
# elif 28 > temp > 0 and is_sunny:
#     print("It's a good weather outside 😎")
#     print("IT'S SUNNY 🌞")


# not operator
temp = 22
is_sunny = True

# if temp >= 27 and not is_sunny:
#     print("It's a pretty HOT outside! 🥵")
#     print("IT'S Cloudy ☁")
# elif temp < 0 and  not is_sunny:
#     print("It cold outside 🥶")
# elif 28 > temp > 0 and not is_sunny:
#     print("It's a good weather outside 😎")
#     print("IT'S cloudy ☁")
# else:
#     print("The weather is some how!")

# print(not is_sunny)

####################################################################################

# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition 
# X if condition else Y

num = 7
a = 6
b = 7
age = 25
temp = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# print("Even! 😊" if num % 2 == 0 else "Odd! 😡")
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult 👴" if age > 18 else "Miner/Child 👶"
# weather = "HOT 🥵" if temp > 20 else "COLD 🥶"
access_credential = "Full Access 🔑" if user_role == "admin" else "Limited Access 🛅"

# print(access_credential)

# ###########################################################################

# String validation
# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# result = len(name) # length of a sting
# result = name.find(" ") # returns the 1st occurrence of a given character
# result = name.rfind("K") # returns the last occurrence of a given character (rfind: reverse)
# name = name.capitalize()
# name = name.upper() # capitalize of the characters
# name = name.lower() 
# result = name.isdigit() # return a boolean if a string only contains digits
# result = name.isalpha() # return a boolean if the string only contains alphabetical characters

# print(f"Your name contains {result} characters.")
# print(result)

# result = phone_number.count("-") # return an integer, count how many characters are in the string
# phone_number = phone_number.replace("-", "") # replace any occurrence of a character with another


# print(phone_number)

# HELP
# print(help(str))

# Exercise 1
# Validate user input exercise:
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter username: ")

# if len(username) > 12 and username.isalpha():
#     print(f"Your username is {username} 👍")
# else:
#     print(f"Incorrect username: {username} ❌")

# if len(username) > 12:
#     print("username should no be more than 12 characters ❌")
# elif username.count(" ") > 0:
#     print("username must not contain spaces ❌")
# elif not username.isalpha():
#     print("username must not contain digits ❌")
# else:
#     print(f"Your username is {username}, welcome on board Mr. {username}! 👍")


# ##########################################################################

# INDEXING
# = accessing elements of a sequence using [] (indexing operator)
#   [start : end : step] 
# the starting index is inclusive
#  the ending index is exclusive

debit_number = "1224-1320-1256-0986"

# print(debit_number[0:4])
# print(debit_number[:4])
# print(debit_number[5:9])
# print(debit_number[5:])

# print(debit_number[::3]) # no print every 2nd character in the string

# last_digits = debit_number[-4:]
# print(f"****-****-****-{last_digits}")

# credit_number = debit_number[::-1]

# print(credit_number)

# ##################################################################################

# FORMAT SPECIFIERS
# {value :flags} format a value based on what flags are inserted

price1 = 6567.9837
price2 = -299282.3637
price3 = 3532822.99

# print(f"Price 1 is UGX{price1: .2f}") # f means floating point number
# print(f"Price 2 is UGX{price2: .2f}")
# print(f"Price 3 is UGX{price3: .1f}")

# print(f"Price 1 is UGX{price1:10}") # Allocating space
# print(f"Price 2 is UGX{price2:10}")
# print(f"Price 3 is UGX{price3:10}")

# print(f"Price 1 is UGX{price1:010}") # O padded number
# print(f"Price 2 is UGX{price2:010}")
# print(f"Price 3 is UGX{price3:010}")

# print(f"Price 1 is UGX{price1: <10}") # Justify left <, Justify right with >
# print(f"Price 2 is UGX{price2: <10}")
# print(f"Price 3 is UGX{price3: <10}")


# print(f"Price 1 is UGX{price1: ^10}") # Center align
# print(f"Price 2 is UGX{price2: ^10}")
# print(f"Price 3 is UGX{price3: ^10}")


# print(f"Price 1 is UGX{price1:>10,.2f}") # comma
# print(f"Price 2 is UGX{price2:>10,.2f}")
# print(f"Price 3 is UGX{price3:>10,.2f}")

# #################################################################################

# WHILE LOOP
# = execute some code WHILE come condition remain True

# name = input("Enter your name: ")

# while not name:
#     print("Invalid input! ❌")
#     name = input("Enter your name: ")

# print(f"Merry Christmas to you {name}")


# age = int(input("Enter your age: "))

# while age < 0:
#     print("Invalid age ❌")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old!")


# food = input("Enter the food you like (press q to quite): ")

# while not food == "q":
#     print(f"You like {food} 😋")
#     food = input("Enter another food you like (press q to quite): ")


# num = int(input("Enter a number btw 1 and 10: "))

# while 1 > num < 10:
#     print(f"{num} is an invalid number ❌")
#     num = int(input("Enter a number btw 1 and 10: "))

# print(f"Your number is {num} 👍")

# ##################################################################################

# FOR LOOP
# = execute a block of code a fixed  number of times.
# You can iterate over a range, string, sequence, etc.

# for counter in range(1, 11): # range(start, end)
#     print(counter)

# print("Happy New Year 2025 🎉🎊😁😍")

# for counter in reversed(range(1, 11)): # count backward
#     print(counter)
    
# print("Happy New Year 2025 🎉🎊😁😍")

# for counter in range(1, 11, 2): # range(start, end, step)
#     print(counter)

# print("Happy New Year 2025 🎉🎊😁😍")

# credit_number = "9827-2356-8468-1243"

# for x in credit_number:
#     print(f"X in credit card: {x}")


# for count in range(1, 21):
#     if count == 13:
#         continue # continue keyword used to skip over an iteration
#     else:
#         print(count)


# for count in range(1, 21):
#     if count == 13:
#         break # break keyword used to break out of the loop
#     else:
#         print(count)


# #####################################################################################

# NESTED LOOP
# = A loop within another loop (outer, inner)
#   outer loop:
#       inner

# for count in range(3): # inner loop get executed 3 times
#     for x in range(1, 10):
#         print(x, end="") # print on the same line
#     print()


# Exercise 

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter a symbol to use: ")

# for count in range(rows):
#     for x in range(columns):
#         print(symbol, end="")
#     print()


# #############################################################################

# COLLECTION
# = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates Ok
#   Set = {} unordered and immutable, but Add/Remove Ok. No Duplicates
#   Tuple = () ordered and unchangeable. Duplicate OK. FASTER

fruits = ["🍏", "🍓", "🍉", "🥑"]

# print(fruits[:3]) # [start: end: step]
# print(fruits[::2]) # [start: end: step]
# print(fruits[::-1]) # [start: end: step]

# for fruit in fruits:
#     print(fruit)

# print(dir(fruits)) # dir() contains all the methods we can use on collections
# print(help(fruits)) # help() gives you the description of all the methods of the collection.

# print(len(fruits))
# print("🥝" in fruits) # False
# print("🍏" in fruits) # True


# fruits[0] = "🍐"
fruits.append("🍒") # append at the end
# fruits.remove("🥑")
# fruits.insert(1, "🍋") # insert a value at given index insert(index, value)
# fruits.sort() # sort in alphabetic order
# fruits.reverse()
# fruits.clear()
# print(fruits.index("🍓")) # return the index
# print(fruits.index("🥧")) # return the index
print(fruits.count("🍓"))

for fruit in fruits:
    print(fruit, end="")






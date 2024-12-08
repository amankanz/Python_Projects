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

# num = 7
# a = 6
# b = 7
# age = 25
# temp = 30
# user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# print("Even! 😊" if num % 2 == 0 else "Odd! 😡")
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult 👴" if age > 18 else "Miner/Child 👶"
# weather = "HOT 🥵" if temp > 20 else "COLD 🥶"
# access_credential = "Full Access 🔑" if user_role == "admin" else "Limited Access 🛅"

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

# LIST []
# fruits = ["🍏", "🍓", "🍉", "🥑"]

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
# fruits.append("🍒") # append at the end
# fruits.remove("🥑")
# fruits.insert(1, "🍋") # insert a value at given index insert(index, value)
# fruits.sort() # sort in alphabetic order
# fruits.reverse()
# fruits.clear()
# print(fruits.index("🍓")) # return the index
# print(fruits.index("🥧")) # return the index
# print(fruits.count("🍓"))

# for fruit in fruits:
#     print(fruit, end="")

# SET {}

# fruits = {"🍏", "🍓", "🍉", "🥑", "🍉"}

# print(dir(fruits)) # dir() contains all the methods we can use on collections
# print(help(fruits)) # help() gives you the description of all the methods of the collection.

# print(len(fruits))
# print("🥝" in fruits) # False
# print("🍏" in fruits) # True


# fruits.add("🍑")
# fruits.remove("🍉")
# fruits.pop() # remove the 1st element
# fruits.clear()

# print(fruits)

# TUPLE ()

fruits = ("🍏", "🍓", "🍉", "🥑", "🍉")

# print(dir(fruits)) # dir() contains all the methods we can use on collections
# print(help(fruits)) # help() gives you the description of all the methods of the collection.

# print(len(fruits))
# print("🥝" in fruits) # False
# print("🍏" in fruits) # True



# print(fruits.index("🍏"))
# print(fruits.count("🍉"))

# for fruit in fruits:
#     print(fruit)

# #####################################################################################

# 2 D List
#  2 dimension list = is a list made of lists [[1], [2], [3], ...]

# vegetables = ["🍒", "🍍", "🥙", "🍆", "🍠", "🍓"]
# snacks = ["🥐", "🍜", "🥪", "🍕"]
# meats = ["🍖", "🥩", "🐟", "🍗"]

# groceries = [
#     ["🍒", "🍍", "🥙", "🍆", "🍠", "🍓"], 
#     ["🥐", "🍜", "🥪", "🍕"], 
#     ["🍖", "🥩", "🐟", "🍗"]
#     ]

groceries = [
    ("🍒", "🍍", "🥙", "🍆", "🍠", "🍓"), 
    ("🥐", "🍜", "🥪", "🍕"), 
    ("🍖", "🥩", "🐟", "🍗")
    ]

# print(groceries[0][1])

# for collection in groceries:
#     # print(collection)
#     print(f"collection {groceries.index(collection) + 1}: ")
#     for food in collection:
#         print(food, end=" ")
#     print()


# EXERCISE
num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
    ) # 2D Tuple


# for row in num_pad:
#     # print(row)
#     for num in row:
#         print(num, end=" ")
#     print()

# #######################################################################################

# DICTIONARY
# = A collection of {key: value} pairs
#   ordered and changeable. No duplicates

capitals = {
    "Rwanda": "Kigali",
    "Uganda": "Kampala",
    "Kenya": "Nairobi",
    "Tanzania": "Darisalam",
    "DRCongo": "Kinshasa"
    }

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Rwanda"))
# print(capitals.get("Burundi"))

# if capitals.get("Burundi"):
#     print("🆗")
# else:
#     print("Country not available in the database! ❌")

# capitals.update({"Burundi": "Bujumbura"})
# capitals.update({"Rwanda": "Higoranyi"})
# capitals.pop("DRCongo")
# capitals.popitem() # remove the latest item added
# capitals.clear()

# print(capitals)

keys = capitals.keys()
# print(keys)

# for key in keys:
#     print(key, end=" ")

# values = capitals.values()

# print(values)

items = capitals.items() # return 2D List of tuples [(), (), ()]

# print(items)

# for key, value in items:
#     print(f"{key}: {value}")
    

# #####################################################################################

# RANDOM NUMBER
import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "As"]

# number = random.randint(low, high) # range(start, end)
# float_number = random.random()
# option = random.choice(options)
# random.shuffle(cards)
# print(cards)

# #####################################################################################

# FUNCTION
# = A block of reusable code
#   place () after the function name to invoke it

def happy_new_year(name, year):
    print(f"Happy New year of {year} Mr. {name} 😍🎉")
    print(f"Success and Health upon our life this {year} 💰👑🤑")
    print("The grind is mine, but glory is His 😇🙌")


# happy_new_year("Ziha", 2025)

def display_invoice(username, amount, due_date):
    print(f"Hello, happy new year {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")


# display_invoice("ziha.aman", 3000, "01 Dec 2024")


# return = statement use to end a function
#   and send a result back to the caller

def add(num1, num2):
    return num1 + num2

# result = add(1, 2)

# print(result)

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z


# print(add(12, 24))
# print(subtract(12, 24))
# print(multiply(12, 24))
# print(divide(12, 24))
# print(divide(13, 20))

def create_name(first_name, last_name, other_name):
    first_name = first_name.capitalize()
    last_name = last_name.upper()
    other_name = other_name.capitalize()

    return(f"My name is: {first_name} ({other_name}) {last_name}")

# full_name = create_name("aman", "mulume", "kaneza")
# full_name = create_name("Amani", "Zihalirwa", "")

# print(full_name)
# print()

# ######################################################################################

# DEFAULT ARGUMENT
# = A default value for certain parameters
#   default is used when that argument is omitted
#   make your functions more flexible, reduces number of arguments
#   1. positional, 2. DEFAULT, 3.keyword, 4.arbitrary


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(1000))
# print(net_price(1000, 0.1))

import time

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE! 🛑")


# count(5)
# count(20, 15)

# ###################################################################################

# KEYWORD ARGUMENT
#   = an argument preceded by an identifier
#       helps with readability
#       order of arguments doesn't matter
#       1. positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting}, {title}{first} {last}")

# hello("Good night", "Rehemah", "Mm. ", "Kashiling") # Positional arguments
# hello(first="Rehemah", greeting="Good night", title="Mm. ", last="Kashiling") # Keyword arguments

# for z in range(1, 5):
#     print(z, end=" ")
# print("1", "2", "3", "4", "5", sep="-")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country="256", area="78", first="510", last="2650")

# print(phone_number)

# ###############################################################################

# *args
#   = allows you to pass multiple  non-key arguments
#   **kwargs = allows you to pass multiple keyword-arguments
#       * unpacking operator
#       1. positional 2. default 3. keyword 4. ARBITRARY(varying amount of arguments)

# def add(a, b):
#     return a + b

# print(add(1, 2, 3))

# def add(*args):
#     # print(type(args))
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# def add(*nums):
#     # print(type(nums))
#     total = 0
#     for num in nums:
#         total += num
#     return total


# print(add(1, 4, 2))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")


# display_name("Hacker", "Ziha", "zihalirwa")

# ### **kwargs

def print_address(**kwargs):
    # print(type(kwargs))
    # for value in kwargs.values():
    #     print(value)
    # for key in kwargs.keys():
    #     print(key)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print_address(street="Buziga Street",
#                 city="Kampala", 
#                 state="Uganda", 
#                 zip="00256")


# EXERCISE:
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# shipping_label("Mr. ", "Zion", "The Hacker","👨‍💻",
#                 street="Anonymous",
#                 apt = "Buzziga Ziha Estate # 1224",
#                 pobox = "PO BOX 123 ug",
#                 city="Online",
#                 state="unknown",
#                 zip="VPN")

# ####################################################################################

# ITERABLES
#   = An object/collection that can return its elements one at a time,
#       allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5, 6] # lists are considered iterables

# for number in numbers:
#     print(number, end=" ")

# for number in reversed(numbers):
#     print(number, end=" ")

# letters = ("a", "b", "c", "d", "e") # Tuples are also iterables

# for letter in letters:
#     print(letter, end=" ")

fruits = {"🍅", "🍈", "🥧", "🍏", "🍑"} # Sets are iterables but not redressable.

# for fruit in fruits:
#     print(fruit, end=" ")

name = "Zion Ziha Aman" # strings are iterables

# for chr in name:
#     print(chr, end="")

# for chr in reversed(name):
#     print(chr, end="")

# my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# for key in my_dictionary:
#     print(key)

# for value in my_dictionary.values():
#     print(value)

# for key, value in my_dictionary.items():
#     print(f"{key}: {value}")


# ##################################################################################

# MEMBERSHIP OPERATORS
#   = used to test whether a value or variable is found in a sequence
#       (string, list, set, or dictionary)
#       1. in
#       2. not in

word = "VICTORY"

# user_guess = input("Guess a letter in the secret word: ").upper()

# if user_guess in word:
#     print("🤗 congrats, yor guess is CORRECT 👍")
#     print(f"The '{user_guess}' is in the secret word.")
# else:
#     print("😬 yor guess is WRONG! 0️⃣")

# if user_guess not in word:
#     print("😬 yor guess is WRONG! 0️⃣")
# else:
#     print("🤗 congrats, yor guess is CORRECT 👍")
#     print(f"The '{user_guess}' is in the secret word.")


students_class_a = {"Ziha", "Majolera", "Kaneza"}

# student = input("Enter a name of a student: ").capitalize()

# if student in students_class_a:
#     print(f"The student {student} 🙍‍♂️ belong to class A")
# else:
#     print(f"Student {student} was not found! ❌")

grades = {"ziha": "A+", 
            "majolera": "B+", 
            "kaneza": "B", 
            "kashiling": "A+", 
            "muhabura": "A"}

# student = input("Enter the name of the student: ")

# if student in grades:
#     print(f"Student {student}'s grade is {grades[student]}")
# else:
#     print(f"Student {student} was not found! ❌")

# email = input('Enter a valid email: ')

# if "@" in email and "." in email:
#     print(f"Your '{email}' is a valid email! 🆗")
# else:
#     print(f"The '{email}' is invalid, must contained (@ .)! ❌")

# ####################################################################################

# LIST COMPREHENSION
#   = A concise way to create lists in Python
#       Compact and easier to read than tradition loops
#       [expression for value in iterable if condition]

# doubles = []

# for x in range(1, 5):
#     doubles.append(x * 2)

# print(doubles)

# doubles = [x * 2 for x in range(1, 5)]
# triples = [y * 3 for y in range(1, 9)]
# squares = [z * z for z in range(1, 5)]

# print(squares)

fruits = ["apple", "orange", "bananas", "pineapple"]

# fruits_upper = [fruit.upper() for fruit in fruits]
# fruit_chars = [fruit[0] for fruit in fruits]

# print(fruit_chars)

# numbers = [0, 1, -3, 6, -4, -12, 8, -19]
# positive_num = [num for num in numbers if num >= 0]
# negative_num = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2 == 0]

# print(even_num)

grades = [30, 46, 95, 84, 75, 62]
passing_grades = [grade for grade in grades if grade >= 60]

# print(passing_grades)

# #########################################################################

# MATCH-CASE STATEMENT (SWITCH):
#   = An alternative to using many 'elif' statements
#       Execute some code if a value matches a 'case'
#       Benefits: cleaner and syntax is more readable


# def days_of_week(day):
#     match day:
#         case 1:
#             return "It's Sunday 🌞"
#         case 2:
#             return "It's Monday 💻"
#         case 3:
#             return "It's Tuesday 😎"

#         case _:
#             return "Not a valid day! ❌"


# print(days_of_week(""))


# def is_weekend(day):
#     match day:
#         case "sunday":
#             return "True, It's Sunday 🌞"
#         case "monday":
#             return "No, It's Monday 💻"
#         case "saturday":
#             return "Yes, It's Saturday 😎"

#         case _:
#             return "Not a valid day! ❌"


# print(is_weekend("saturday"))


def is_weekend(day):
    match day:
        case "sunday" | "saturday":
            return "True, It's weekend 🌞"
        case "monday" | "tuesday" | "wednesday" | "thursday":
            return "No, It's week day 💻"
        case "Friday":
            return "Yes, It's Friday 🙏 😎"

        case _:
            return "Not a valid day! ❌"


# print(is_weekend("saturday"))

# #########################################################################

# MODULE
#       = A file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program reusable separate files


# print(help("modules"))

# import math
# import math as m
# from math import pi
# from math import e

# print(pi)

a, b, c, d, e = 1, 2, 3, 4, 5

# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)

# import modules.example as example
import modules.example as example

# result = example.pi
# result = example.square(2)
# result = example.cube(3)


# print(result)

# ###############################################################################

# VARIABLE SCOPE
#       = Where a variable is visible and accessible
# SCOPE RESOLUTION
#       = (LEGB) lOCAL -> Enclosed -> Global -> Built-in

# LOCAL
# def func1(): # variable declared in function have local scope, a is local to func1
#     x = 3
#     print(x)



# def func2():
#     x = 2
#     print(x)

# ENCLOSED

# def func1(): 
#     x = 3
#     def func2():
#         # x = 2
#         print(x)
#     func2()


# func1()

# GLOBAL

# def func1():
#     print(x)



# def func2():
#     print(x)

# x = 7

# func1()
# func2()

# from math import e

# def func1():
#     print(e)

# e = 8

# func1()

# ##################################################################################

# if __name___ == __main___:  (this statement can be imported OR run standalone)
#                             Functions and classes in this module can be reused
#                               without the main block of code executing
#       GO CHECK script1 & 2
#       
# Good practice (code is modular,
#                   helps readability,
#                   avoid unintended execution)


def main():
    # program code goes here
    pass

if __name__ == "__main__":
    main()










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
item = input("What item would like to buy for Christmas seasons?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many would you like?: "))
total_price = price * quantity

# print(f"For Christmas I want {quantity} {item} which cost ${price} per item, so the total price is ${total_price}. :)")





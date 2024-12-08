# if __name___ == __main___:  (this statement can be imported OR run standalone)
#                             Functions and classes in this module can be reused
#                               without the main block of code executing
#       GO CHECK script1 & 2
#       
# Good practice (code is modular,
#                   helps readability,
#                   avoid unintended execution)


# from script2 import *

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script 1")
    favorite_food("Chicken Burger 🍔")
    print("Happy weekend!😎")

# # print(__name__)

if __name__ == "__main__":
    main()

# print("This is script 1")
# favorite_food("Chicken Burger 🍔")
# print("Happy weekend!😎")


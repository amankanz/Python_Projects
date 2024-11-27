# Python Shopping Cart 

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item  to buy 🛒 (press q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food} item to buy 💲💲💲: $"))
        foods.append(food)
        prices.append(price)

print("------ YOUR CART 🛒 ------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price


print()
print(f"Total bill of all the items is 💲{total}")

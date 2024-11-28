# Python Concession Stand Program

# Dictionary {key: value}
menu = {
    "popcorn": 5.00,
    "hot dog": 3.50,
    "nachos": 4.25,
    "candy": 2.00,
    "soda": 1.75,
    "water": 1.50,
    "pretzel": 3.00,
    "ice cream": 2.50,
    "pizza slice": 4.00,
    "coffee": 2.25
}

cart = []
total = 0

print("------- MENU 📃---------")
for key, value in menu.items():
    print(f"{key.title():13}: ${value: .2f}")

print("------ 💖 THANKS FOR SUPPORTING 🙏 -------")

while True:
    customer_order = input("Place your order now!🥰 (Press q to quit): ").lower()
    if customer_order == "q":
        break
    elif menu.get(customer_order) is not None:
        cart.append(customer_order)
        print(f"Added {customer_order.title()} to your cart.")
    else:
        print(f"{customer_order.title()} is Out of stock, sorry! 😔🙏")


print("------- ORDER --------")
for item in cart:
    total += menu.get(item)
    print(f"{item}", end=", ")

print()
print(f"Your bill is ${total: .2f} 💰")
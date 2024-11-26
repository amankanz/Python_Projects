# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the Principle amount: "))
#     if principle <= 0:
#         print("Principle should be greater than 0! ❌")
# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("rate should be greater than 0❌")
# while time <= 0:
#     time = int(input("Enter ⏳ time: "))
#     if time <= 0:
#         print("time should be greater than 0 ❌")


while True:
    principle = float(input("Enter the Principle amount: "))
    if principle < 0:
        print("Principle should be greater than 0! ❌")
    else:
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("rate should be greater than 0❌")
    else:
        break
while True:
    time = int(input("Enter ⏳ time: "))
    if time < 0:
        print("time should be greater than 0 ❌")
    else:
        break



# print(f"${principle:,} 💰")
# print(f"{rate}% 🔢")
# print(f"{time} years ⏳")

total = principle * pow((1 + rate / 100), time)

print(f"Actual Balance after {time} years with an amount of ${principle:,} and annual interest rate of {rate}% it is ${total:,.2f} 💰")

# Python Banking Program

def show_balance(balance):
    print("***********************")
    print(f"Your current balance is ${balance:.2f}")
    print("***********************")

def deposit():
    print("***********************")
    amount = float(input("Enter an amount to be deposited: $"))
    print("***********************")

    if amount < 0:
        print("***********************")
        print("Invalid amount ❌")
        print("***********************")
        return 0
    else:
        print("***********************")
        print(f"You've successfully deposited ${amount:.2f} 💰")
        print("***********************")
        return amount

def withdraw(balance):
    print("***********************")
    withdraw_amount = float(input('Enter amount to withdraw: $'))
    print("***********************")

    if withdraw_amount > balance:
        print("***********************")
        print("   Insufficient funds! ⛔   ")
        print("***********************")
        return 0
    elif withdraw_amount < 0:
        print("***********************")
        print('    Withdraw amount must be greater than 0❗❗❗    ')
        print("***********************")
        return 0
    else:
        return withdraw_amount


def banking():
    balance = 0
    is_running = True

    while is_running:
        print("***********************")
        print("      Ziha Bank 🏦     ")
        print("***********************")
        print("1. Show Balance 🔢")
        print("2. Deposit 💵")
        print("3. Withdraw 💰")
        print("4. Exit 🏃❎")

        user_choice = input("Enter an option (1-4): ")

        if user_choice == "1":
            show_balance(balance)
        elif user_choice == "2":
            balance += deposit()
        elif user_choice == "3":
            balance -= withdraw(balance)
            print("*********************")
            print(f"Your remaining balance is ${balance}")
            print("*********************")
        elif user_choice == "4":
            is_running = False
        else:
            print("*********************")
            print("Enter a valid input! 1️⃣ - 4️⃣")
            print("*********************")

    print("******************************************")
    print('   Thank you for your transaction! 🙋‍♂️     ')
    print("******************************************")


if __name__ == "__main__":
    banking()
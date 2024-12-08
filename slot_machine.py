# Python Slot Machine

def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def slot_machine():
    balance = 1224

    print("***************")
    print("     WELCOME! 🎄😁    ")
    print("  🐍 Slot Machine 💰  ")
    print("Signs: 🍉 🍋 🍎 🔔 ⭐")
    print("***************")

    while balance > 0:
        print(f"Your current balance is ${balance}")

        bet = input("💰 Place your bet amount: $")


if __name__ == "__main__": # This program can be imported or Standalone 
    slot_machine()
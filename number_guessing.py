# Python Number Guessing Game
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("----- 🐍 🔢 Guessing Game 🤔 -----")
print()
player = input("Player what's your name?: ").title()
print(f"Enter a number between {lowest_num} and {highest_num}: ")

while is_running:
    guess = input(f"{player} Enter your guess 🔢 😃: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if lowest_num > guess or guess > highest_num:
            print("That's out of range! 🤮")
            print(f"Enter a number between {lowest_num} and {highest_num}: ")
        elif guess < answer:
            print("That's too low, Try again! 😁")
        elif guess > answer:
            print("That's too high, Try again! 😮")
        else:
            print(f"CORRECT! The answer was {answer}. 🎉 🙌 👍")
            print(f"Number of guesses: {guesses}")
            is_running = False

    
    else:
        print(f"{player}, {guess} is not valid guess 😪: ")
        print(f"Enter a number between {lowest_num} and {highest_num}: ")
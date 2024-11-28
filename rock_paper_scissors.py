# Python ROCK PAPER SCISSORS Game
import random

# options = ("rock", "paper", "scissors")
# answer = random.choice(options)
# moves = 0


# is_running = True

# print("----- Rock Paper Scissors Game 👊 🖐 ✌ -----")
# print()
# player = input("Player what's your name?: ").title()
# print(f"Enter a move, ROCK PAPER OR SCISSORS 👊 🖐 ✌, break a leg! 🤗: ")


# while is_running:
#     user_move = input("Enter you move, 👊 🖐 or ✌:  ").lower()
#     if user_move.isalpha():
#         moves += 1
#         if user_move == answer:
#             print(f"Winner 🥇! {user_move.upper()} is the correct move! 🙌😊")
#             print(f"Total number of Moves: {moves}")
#             is_running = False
#         else:
#             print(f"You Failed! ❌ Try again! 🤞")
#             print(f"Enter a move, ROCK PAPER OR SCISSORS 👊 🖐 ✌!")
#     else:
#         print(f"{player}, {user_move} is not valid move 😪: ")
#         print(f"Enter a move, ROCK PAPER OR SCISSORS 👊 🖐 ✌!")



options = ("rock", "paper", "scissors")
playing_round = 0
playing = True
player_wins = 0
computer_wins = 0

print("----- Rock Paper Scissors Game 👊 🖐 ✌ -----")
print()
player_name = input("Player what's your name?: ").title()
print(f"{player_name} enter a move, ROCK PAPER OR SCISSORS 👊 🖐 ✌, break a leg! 🤗: ")
print()

while playing:
    player = None
    computer = random.choice(options)
    playing_round +=1

    while player not in options:
        player = input("Enter your choice ROCK PAPER OR SCISSORS 👊 🖐 ✌: ").lower()

    print(f"{player_name}'s choice is {player}")
    print(f"🤖 choice is {computer}")


    if computer == player:
        print("It's a Tier!")
    elif computer == "scissors" and player == "rock":
        print(f"WINNER {player_name}! 👍") 
        player_wins +=1
    elif computer == "rock" and player == "paper":
        print(f"WINNER {player_name}! 👍")
        player_wins +=1
    elif computer == "paper" and player == "scissors":
        print(f"WINNER {player_name}! 👍")
        player_wins +=1
    else:
        print("You LOSE, 🤖 WINS!")
        computer_wins +=1

    if playing_round == 3:
        if not input("Do wish to continue playing (Y/N): ").upper() == "Y":
            playing = False


print(f"THANKS FOR PLAYING! 🤖 wins: {computer_wins} and {player_name} wins: {player_wins}")

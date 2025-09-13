import random

moves = ["rock", "paper", "scissors"]
n = int(input("Enter the number of rounds: "))
user_score = 0
computer_score = 0
for round_num in range(1, n + 1):
    print(f"\nRound {round_num}")
    user_move = input("Choose rock, paper, or scissors: ").lower()    
    while user_move not in moves:
        print("Invalid move! Please choose rock, paper, or scissors.")
        user_move = input("Choose rock, paper, or scissors: ").lower()
    computer_move = random.choice(moves)
    print(f"Computer chose {computer_move}.")
    if user_move == computer_move:
        print(f"Round {round_num} is a draw!")
        user_score += 1
        computer_score += 1
    elif (user_move == "rock" and computer_move == "scissors") or (user_move == "scissors" and computer_move == "paper") or (user_move == "paper" and computer_move == "rock"):
        print(f"You have won round {round_num}!")
        user_score += 2
    else:
        print(f"The computer has won round {round_num}!")
        computer_score += 2

print("\nGame Over!")
print(f"Your score: {user_score}")
print(f"Computer's score: {computer_score}")
if user_score > computer_score:
    print("You win the game!")
elif user_score < computer_score:
    print("Computer wins the game!")
else:
    print("It's a tie!")
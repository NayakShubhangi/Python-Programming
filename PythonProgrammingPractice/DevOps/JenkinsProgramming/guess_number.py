import random

print("Welcome to the guessing game")
num_players = int(input("Enter how many players will be playing (as a digit): "))
players = []

for i in range(num_players):
    player_name = input(f"Enter the name for player {i + 1}: ")
    players.append(player_name)

current_player_index = 0
while True:
    ready = input(f"{players[current_player_index]}, are you ready to start? (yes/no): ").strip().lower()
    if ready == "yes":
        break
    current_player_index = (current_player_index + 1) % num_players

start_index = current_player_index
for i in range(num_players):
    player = players[(start_index + i) % num_players]
    randomnum = random.randrange(0, 10)
    print(f"\n{player}'s turn:")
    chance_count = 0
    while chance_count < 3:
        guess = int(input(f"Enter a number between 0 and 9: "))
        if guess != randomnum:
            if guess < randomnum:
                print(f"The number you guessed, {guess}, is less than the secret number.")
            elif guess > randomnum:
                print(f"The number you guessed, {guess}, is greater than the secret number.")
        if guess == randomnum:
            print(f"Congratulations, {player}. You guessed the secret number. It was {randomnum}.")
            break
        chance_count += 1
    if chance_count == 3:
        print(f"{player}, you were unable to guess the secret number. It was {randomnum}.")

print("Game over. Thanks for playing.")
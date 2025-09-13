numOfPlayers = int(input("Enter the number of players: "))
playerNames = []
for i in range(numOfPlayers):
    name = input(f"Player {i+1}, enter your name: ")
    playerNames.append(name)
locatorVal = int(input("Enter the locator value: "))
multiplesOf = int(input("Enter a number to get the multiples of it: "))

def numberGame(playerNames, locatorVal, multiplesOf):
    totalMaxTurns = 50
    totalTurnsHad = 0
    currentPlayerIndex = 0
    while totalTurnsHad < totalMaxTurns and len(playerNames) > 1:
        currentPlayer = playerNames[currentPlayerIndex]
        playerGuess = int(input(f"{currentPlayer}, enter a number: "))
        totalTurnsHad += 1
        if totalTurnsHad % locatorVal == 0:
            if playerGuess % multiplesOf != 0:
                print(f"{currentPlayer} has been eliminated...")
                playerNames.pop(currentPlayerIndex)
                if currentPlayerIndex >= len(playerNames):
                    currentPlayerIndex = 0
                continue
        currentPlayerIndex += 1
        if currentPlayerIndex >= len(playerNames):
            currentPlayerIndex = 0
    if len(playerNames) == 1:
        print(f"{playerNames[0]} has won...")
    else:
        print("The maximum turns has been reached... Game Over... Everyone left wins!")
        print("Remaining Players Left:", ', '.join(playerNames))

numberGame(playerNames, locatorVal, multiplesOf)
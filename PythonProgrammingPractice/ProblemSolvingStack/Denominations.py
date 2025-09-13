# TASK FOUR
# Explain...
# How many ways can you make change with coins and a total amount?
# We need to create a function that takes a list of coin denominations and total amounts and returns the number of ways we can make the change. 
# In the example, we have provided coin denominations [1, 2, 5] and the total amount of 5.
# In return, we got four ways we can make the change.
# OUTPUT: 5 -> [1, 1, 1, 1, 1], [2, 2, 1], [1, 1, 1, 2], [5]

# denominations_coin = list(input("Enter the coin denominations: "))
# total_amount = int(input("Enter the total amount: "))

def solve_coin_change(denominations, amount):
    solution = [0] * (amount + 1)
    solution[0] = 1
    for den in denominations:
        for i in range(den, amount + 1):
            solution[i] += solution[i - den]
    return solution[len(solution) - 1]

denominations = [1,2,5]
amount = 5
solve_coin_change(denominations,amount)
# 4

# The list solution has (amount + 1) number of items, and all values set to 0 except for solution[0],
# which is set to 1 because there is one way to make a total of 0, which is to use no coins.
# solution[i] is updated in the for loops by adding solution[i-den], which will show how many ways you can get i when den is used.
# solution[len(solution) - 1] gives the ways you can make the total amount.
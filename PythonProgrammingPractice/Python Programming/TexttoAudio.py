import pyttsx3

engine = pyttsx3.init()
text = "This is in python and this is a very long sentence."
engine.say(text)
engine.runAndWait()

# TASK ONE: (DONE)
# put this into the project:
# "welcome to the restaurant" goes in audio now, & customer is thanked at the end of the program, WITH the customer name
# make a function to make it easier
# thanking the customer is blocked due to error before that, which i couldn't fix


# TASK TWO: (DONE)
# The customer who comes to the restaurant,
# make a discount table for roles and give appropriate discounts: (DONE)
#  -Role
#  -Discount (for role)
# make ONE function that could be repurposed for all of them
# ASK IF THEY HAVE SOME KIND OF ROLE     *decide where it should be put*-> BEFORE BILL GENERATION
# if they say that they are a *placeholder*:
#      - Apply additional *some*% discount based on whether they are in the database

# EXAMPLE
# student:
#     - Apply additional 10% discount


# TASK THREE:
# Refactor and make the code as efficient as possible
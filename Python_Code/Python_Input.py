# TODO TASK TWO: (DONE)
# Get (argv / command line) input from the user (refer to Command_Line_Arguments.py)
# and display it in a function
# Create a new workflow (Run_python_with_Inputs.yml) and take string input,
# then pass it into the python call
import sys

def Display_Input(user_input: str):
    print(user_input)

user_input = sys.argv[1]
Display_Input(user_input)
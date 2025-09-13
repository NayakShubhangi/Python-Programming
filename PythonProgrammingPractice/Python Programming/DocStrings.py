# A docstring is written in triple double/single quotes and should be placed immediately after the function definition

# Basic Structure of Function Docstring
# Well formatted docstring typically has:
# 1. Short description
# 2. Detailed description (optional)
# 3. Parameters
# 4. Return value
# 5. Raises (optional)

def addTwo(a, b):
    """
    Adds two numbers and returns the result

    Parameters:
    a (int/float): The first number to add
    b (int/float): The second number to add

    Returns:
    Integer/Float: The sum of a and b
    """
    return a + b

# print(help(addTwo))
print(addTwo.__doc__)
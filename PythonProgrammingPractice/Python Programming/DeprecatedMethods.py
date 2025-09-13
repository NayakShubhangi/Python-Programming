from deprecated import deprecated

# Deprecated decorator can have a custom message,
# and when the function is run, the terminal shows that the function will be deprecated soon, like a warning,
# along with the custom message that was specified in the deprecated decorator.
@deprecated("This function may not last much longer... Plan to revise before next month...")
def sumOfTwoNumbers(a: int, b: int):
    print(a + b)


if __name__ == "__main__":
    sumOfTwoNumbers(2, 3)
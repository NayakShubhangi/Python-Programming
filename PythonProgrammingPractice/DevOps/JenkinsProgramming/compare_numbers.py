import sys

def compare_numbers(number1, number2):
    num1 = int(number1)
    num2 = int(number2)
    if num1 > num2:
        print(f"The greater number is: {num1}")
    elif num2 > num1:
        print(f"The greater number is: {num2}")
    else:
        print("Both numbers are equal.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_numbers.py <number1> <number2>")
        sys.exit(1)
    number1 = sys.argv[1]
    number2 = sys.argv[2]
    compare_numbers(number1, number2)
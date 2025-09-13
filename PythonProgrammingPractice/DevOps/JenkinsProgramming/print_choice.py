import sys

def print_choice(choice):
    print(f"You selected: {choice}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python print_choice.py <choice>")
        sys.exit(1)
    
    choice = sys.argv[1]
    print_choice(choice)
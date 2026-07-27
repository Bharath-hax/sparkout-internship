value = input("Enter a number: ")

try:
    number = int(value)
    print("Valid Integer:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
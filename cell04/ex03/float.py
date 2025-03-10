number = input("Enter a number: ")

try:
    float_number = float(number)
    if '.' in number:
        print("The entered number is a decimal.")
    else:
        print("The entered number is not a decimal.")
except ValueError:
    print("That's not a valid number.")

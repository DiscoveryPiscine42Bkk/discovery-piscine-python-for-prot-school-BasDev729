import sys

if len(sys.argv) != 2:
    print("none")
else:
    parameter = sys.argv[1]
    user_input = input("Enter a word: ")

    if user_input == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")

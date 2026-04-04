letter_input = input("Enter a letter to verify your gender (F or M): ")
if letter_input.upper() == "F":
    print("You are female.")
elif letter_input.upper() == "M":
    print("You are male.")
else:
    print("Invalid input, please type 'F' for female and 'M' for male.")
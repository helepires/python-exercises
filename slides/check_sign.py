value_input = float(input("Type here a value (it can be positive, negative or even equal to 0): "))

if (value_input < 0):
    print(f"The value {value_input} is negative!")
elif (value_input == 0):
    print(f"The value {value_input} is equal to 0!")
else:
    print(f"The value {value_input} is positive!")
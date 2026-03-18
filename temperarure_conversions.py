celsius_user_input = float(input("Type the temperature in C°, please: "))
converting_to_fahrenheit = (celsius_user_input * 9/5) + 32
print(f"We converted it, so the temperature now is: {converting_to_fahrenheit:.2f}F°")

# Agora, o oposto!

fahrenheit_user_input = float(input("Type the temperature in F°, please: "))
converting_to_celsius = (fahrenheit_user_input - 32) * (5/9)
print(f"We converted it, so the temperature now is: {converting_to_celsius:.2f}C°")

how_many_liters = int(input("How many liters have been selled? "))
which_fuel = input("Type from which fuel here (A for Alcohol and G for Gasoline: ")

if which_fuel.upper() == "G":
    if how_many_liters <= 20:
        price_gasoline = (how_many_liters * 5.57) - (how_many_liters * 0.04)
        print(f"Your gasoline price will be: R${price_gasoline:.2f}")
    elif how_many_liters > 20:
        price_gasoline = (how_many_liters * 5.57) - (how_many_liters * 0.06)
        print(f"Your gasoline price will be: R${price_gasoline:.2f}")

if which_fuel.upper() == "A":
    if how_many_liters <= 20:
        price_alcohol = (how_many_liters * 4.98) - (how_many_liters * 0.02)
        print(f"Your alcohol price will be: R${price_alcohol:.2f}")
    elif how_many_liters > 20:
        price_alcohol = (how_many_liters * 4.98) - (how_many_liters * 0.05)
        print(f"Your alcohol price will be: R${price_alcohol:.2f}")
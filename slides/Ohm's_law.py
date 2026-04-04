volts_input = float(input("Type here the voltage value (in Volts - V): "))
ampere_input = float(input("Type here the current value (in Ampere - I): "))
ohms_input = float(input("Type here the resistance value (in Ohms - Ω):"))

voltage_count = ampere_input * ohms_input

if volts_input == voltage_count:
    print("The component obeys Ohm's Law.")
else:
    print("The component does not obey Ohm's law.")
value_input = int(input("Type here a value (decimal): "))

oct_converted_value = oct(value_input)
print(f"The octal value of {value_input} is: {oct_converted_value[2:]}")

bin_converted_value = bin(value_input)
print(f"The binary value of {value_input} is: {bin_converted_value[2:]}")

hex_converted_value = hex(value_input)
print(f"The hexadecimal value of {value_input} is: {hex_converted_value[2:]}")
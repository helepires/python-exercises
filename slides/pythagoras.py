import math

cathet_input = int(input("Type here the first cathet: "))
second_cathet_input = int(input("Type here the second cathet: "))

hipotenuse_formula = math.sqrt(math.pow(cathet_input,2) + math.pow(second_cathet_input,2))
print("The hipotenuse is:",hipotenuse_formula)
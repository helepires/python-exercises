number_x = int(input("Digite aqui um valor para x: "))
number_y = int(input("Digite aqui um valor para y: "))

try:
    z_count = (number_x**2 + number_y**2)/(number_x - number_y)
    print("O resultado é:",z_count)
except ZeroDivisionError:
    print("Os dois números devem ser diferentes!!")
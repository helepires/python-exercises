import math
radius_one = float(input("Digite a medida de um raio: "))
radius_two = float(input("Digite a medida de outro raio: "))

while (radius_two >= radius_one):
    print("ERRO! Os raios não podem ser iguais entre si, e o segundo não pode ser maior do que o primeiro!")
    
    radius_one = float(input("Digite a medida de um raio: "))
    radius_two = float(input("Digite a medida de outro raio: "))
    
circular_crown_count = math.pi * (radius_one**2 - radius_two**2)
print(f"A área da coroa circular é: {circular_crown_count:.2f}")

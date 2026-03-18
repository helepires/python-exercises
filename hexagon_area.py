import math

radius_input = float(input("Digite aqui o valor de um raio: "))
square_root = math.sqrt(3)
hexagon_area = 6 * (radius_input**2) * (square_root) / (4) 
print(f"A área do hexagono é de: {hexagon_area:.2f}")

circle_radius = float(input("Digite o raio da circunferência: "))
import math 
print(f"O valor previsto de pi é: {math.pi:.2f}")
perimeter_count = 2 * math.pi * circle_radius
print(f"O perímetro dessa circunferência é de: {perimeter_count:.2f}")
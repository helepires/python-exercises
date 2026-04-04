import math
tube_diameter_input = float(input("Digite o diâmetro interno do tubo (m): "))
tube_radius = tube_diameter_input / 2 
tube_area_section = math.pi * (tube_radius**2)
fluid_velocity = float(input("Digite a velocidade do fluido (m/s): "))
flow_rate = tube_area_section * fluid_velocity
print("A vazão do tubo é de: %.2f metros cúbicos por segundo" % flow_rate)

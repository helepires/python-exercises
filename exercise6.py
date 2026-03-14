object_steps = float(input("Digite o deslocamento do seu objeto em metros: "))
print(object_steps)
time_seconds = int(input("Digite o tempo em segundos: "))
print(time_seconds)
velocity = object_steps / time_seconds
print(f"A velocidade média conforme a variação de deslocamento {object_steps} é de: {velocity}")

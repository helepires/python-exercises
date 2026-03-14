height_input = float(input("Digite aqui sua altura: "))
weight_input = float(input("Digite aqui seu peso: "))
IMC_rate = weight_input / (height_input**2)
print(f"Seu IMC é de: {IMC_rate:.2f}")
if (IMC_rate < 18.5):
    print("Abaixo do peso")
elif(18.5 <= IMC_rate < 24.9):
    print("Peso normal")
elif(25 <=IMC_rate < 29.9):
    print("Sobrepeso")
else: 
    print("Obesidade")

pv = float(input("Digite aqui o valor inicial investido: "))
n = int(input("Digite o número de meses em que o investimento ficará aplicado: "))
i = float(input("Digite a rentabilidade mensal do investimento: "))

i = i / 100

fv = pv * (1 + i)**n

print(f"O resultado final do investimento é de: R$ {fv:.2f}") # usando f string pra alterar
                                                             # o numero de casas decimais mostradas


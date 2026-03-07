fv = float(input("Digite aqui o valor final do seu investimento: "))
i = float(input("Digite aqui a rentabilidade mensal do seu investimento: "))
n = int(input("Digite quantos meses o investimento ficou aplicado: "))

i = i /100

pv = fv / (1 + i)**n

print(f"O valor inicial investido por você foi de: R$ {pv:.2f}")
original_price = float(input("Qual o preço original do produto? "))
discount_gained_percent = original_price * 0.80 
discount_real_value = original_price - (discount_gained_percent)
print(f"O valor do seu desconto é de R${discount_real_value:.2f}")
print("O novo valor do seu produto é:","R$", discount_gained_percent)


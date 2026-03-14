original_price = float(input("Qual o preço original do produto? "))
input_discount = float(input("Qual disconto será recebido? (%) "))
discount_real_value = original_price * input_discount/100
discount_gained_percent = original_price - (discount_real_value)
print(f"O valor do seu desconto é de R${discount_real_value:.2f}")
print("O novo valor do seu produto é:","R$", discount_gained_percent)

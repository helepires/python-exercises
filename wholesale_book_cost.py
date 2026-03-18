X= int(input("Quantos livros serão solicitados: "))

book_cover_discount = 24.95 * 0.65 * X
print(f"O desconto inicial para livrarias resultou em: R$ {book_cover_discount:.2f}")

transport_price_addicional = (X - 1) * 0.75 + 3
print(f"O preço cobrado pelo transporte resultou em: R$ {transport_price_addicional:.2f}")

total_value = transport_price_addicional + book_cover_discount
print(f"O valor total da sua compra é de: R$ {total_value:.2f}")

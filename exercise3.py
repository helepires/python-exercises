X= int(input("Quantos livros serão solicitados: "))

bookCoverDiscount = 24.95 * 0.65 * X
print(f"O desconto inicial para livrarias resultou em: R$ {bookCoverDiscount:.2f}")

transportPriceAddicional = (X - 1) * 0.75 + 3
print(f"O preço cobrado pelo transporte resultou em: R$ {transportPriceAddicional:.2f}")

totalValue = transportPriceAddicional + bookCoverDiscount
print(f"O valor total da sua compra é de: R$ {totalValue:.2f}")

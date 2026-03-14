how_much_money = float(input("Quanto está disposto a gastar?"))
how_many_liters = how_much_money / 4.95
print(f"Seu tanque, com R${how_much_money:.2f}, poderá ter {how_many_liters:.2f} litros")
km_per_liter = how_many_liters * 20
print(f"Seu carro andará {km_per_liter:.2f} km")
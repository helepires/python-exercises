how_much_per_hour = float(input("How much do you make per hour? "))
how_many_hours_per_month = float(input("How many hours do you work per month? "))
gross_pay = how_many_hours_per_month * how_much_per_hour
print(f"Your gross pay is R${gross_pay:.2f}.")          # SALÁRIO BRUTO!

income_tax_discount = gross_pay * 0.11
print(f"You paid R${income_tax_discount:.2f} to the income tax.")                 # Imposto de renda!
discount_INSS = gross_pay * 0.08                       # INSS!
print(f"You paid R${discount_INSS:.2f} to the INSS.")
discount_union = gross_pay * 0.05                      # Sindicato!
print(f"You paid R${discount_union:.2f} to the union.")

net_pay = gross_pay - (income_tax_discount + discount_INSS + discount_union)
print(f"Your net pay is R${net_pay:.2f}.")
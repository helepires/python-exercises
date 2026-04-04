discount_value = float(input("Enter the discount percentage (value between 0 and 1): "))
original_price = float(input("Enter the original price: "))
discount_amount = original_price * discount_value
paid_value = original_price - discount_amount
print(f"Your final price is: R${paid_value:,.2f}")
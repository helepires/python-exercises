user_name = input("Type your full name here (all lower): ")
name_title = user_name.title()
print(name_title)

# Agora a entrada é com todos os caracteres maiusculos!

user_name2 = input("Type your full name here (all upper): ")
user_lower = user_name2.lower()
final_name = user_lower.title()
print(final_name)
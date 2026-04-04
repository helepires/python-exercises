year_input = int(input("Enter a year (ex, 2000): "))

if year_input % 4 == 0 and year_input % 100 != 0:
    print(f"The year {year_input} is leap!")
elif year_input % 400 == 0:
    print(f"The year {year_input} is leap!")
else:
    print(f"The year {year_input} is not leap, sorry!")
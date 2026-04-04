FISHING_REGULATIONS = 50  # Maximum allowed weight of fish in kg
weight_of_fish = float(input("Enter the weight of the fish in kg: "))
excess_weight = weight_of_fish - FISHING_REGULATIONS
if weight_of_fish <= FISHING_REGULATIONS:
    print("This weight is allowed without having to pay any fine.")
else:
    fine = excess_weight * 4 
    print(f"Excess weight: {excess_weight:.2f}kg")
    print(f"The fine you must pay is R${fine:.2f}")
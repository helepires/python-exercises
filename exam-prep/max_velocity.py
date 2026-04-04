MAX_VELOCITY = float(input("Enter the maximum velocity allowed on the road: "))
velocity_input = float(input("Enter the velocity of the car when you were driving: "))
if MAX_VELOCITY < velocity_input <= MAX_VELOCITY + 10:
    traffic_ticket = 85.13
    ticket_category = "Mild"
    license_points = 3
    print(f"You have been issued a {ticket_category} traffic ticket of R$85.13 and received {license_points} points on your license.")

elif MAX_VELOCITY + 11 <= velocity_input <= MAX_VELOCITY + 30:
    traffic_ticket = 127.69
    ticket_category = "Moderate"
    license_points = 5
    print(f"You have been issued a {ticket_category} traffic ticket of R$127.69 and received {license_points} points on your license.")

elif velocity_input >= MAX_VELOCITY + 31:
    traffic_ticket = 574.62
    ticket_category = "Severe"
    license_points = 7
    print(f"You have been issued a {ticket_category} traffic ticket of R$574.62 and received {license_points} points on your license.")
else:
    print("Normal driving. No traffic ticket issued.")

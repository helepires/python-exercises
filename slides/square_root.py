import math 

x1_input = int(input("Enter the x value of the first point:"))
y1_input = int(input("Enter the y value of the first point:"))
x2_input = int(input("Enter the x value of the second point:"))
y2_input = int(input("Enter the y value of the second point:"))

P1 = (x1_input, y1_input)
P2 = (x2_input, y2_input)
print("The first point is:", P1)
print("The second point is:", P2)

distance = math.sqrt(math.pow(x2_input - x1_input, 2) + math.pow(y2_input - y1_input, 2))
print(f"The distance between the two points is: {distance:.2f}")
import math

NUMBER_PI = 3.14159
radius = float(input("Type here a radius value for the circle: "))
if radius < 0:
    print("Error: Invalid radius! Impossible to calculate. Try again.")
else:
    circle_area = NUMBER_PI * math.pow(radius, 2)
    print(f"The area of the circle with a radius of {radius} units is {circle_area:.3f} units.")
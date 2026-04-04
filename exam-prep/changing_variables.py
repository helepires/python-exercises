first_variable = int(input("Type here the first variable: "))
print("Your value is:",first_variable)
second_variable = int(input("Type here the second variable: "))
print("Your value is:",second_variable)
first_variable, second_variable = second_variable, first_variable
print("The first variable has been sucessfully changed:",first_variable)
print("The second variable has been sucessfully changed:",second_variable)
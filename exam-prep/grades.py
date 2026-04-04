first_grade = float(input("Type here your first grade: "))
second_grade = float(input("Type here your second grade: "))
average = (first_grade + second_grade) / 2
print("Your score is :", average)

if average == 10.0:
    print("Passed with Distinction.")
elif average >= 7.0:
    print("Passed.")
elif average < 7.0:
    print("Failed.")
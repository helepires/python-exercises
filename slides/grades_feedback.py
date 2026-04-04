first_grade_input = float(input("Type your first grade here: "))
second_grade_input = float(input("Type your second grade here: "))
third_grade_input = float(input("Type your third grade here: "))

average_score = (first_grade_input + second_grade_input + third_grade_input) / 3
print(f"Your score is: {average_score:.1f}")

if average_score > 10:
    print("Invalid grades!")
elif average_score >= 7.0:
    print("Congrats! Your score is high!")
elif average_score >= 5.0:
    print("Your score is medium.")
else:
    print("Your score is low. It's a better chance for you to improve.")
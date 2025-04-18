student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

student_grades = {}
for student in student_scores:
    grade = student_scores[student]
    if grade >= 91:
        student_grades[student] = "Outstanding"
    elif grade >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif grade >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

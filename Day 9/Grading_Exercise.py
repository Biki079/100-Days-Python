student_score = {
    "Bikash" : 91,
    "Rijan" : 92,
    "Giriraj": 80,
    "Hari": 78,
    "Gita": 70,
    "Rita": 60
}
student_grade = {}
for student in student_score:
    score = student_score[student]
    if score>90:
        student_grade[student] = "Outstanding"
    elif score >80:
         student_grade[student] ="Exceeds Expectations"
    elif score>70:
         student_grade[student] ="Acceptable"
    else:
         student_grade[student] ="Fails"

print(student_grade)


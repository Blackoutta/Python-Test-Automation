student_1 = {"grades": (1,2,3)}
student_2 = {"grades": (0,0,0)}
student_3 = {"grades": (2,10,55)}
student_list = [student_1, student_2, student_3]

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])

    return total / count

output = average_grade_all_students(student_list)
print(output)

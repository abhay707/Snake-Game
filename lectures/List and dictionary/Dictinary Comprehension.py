import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_score = {students: random.randint(1, 100) for students in names}

passed_student = {students: score for (students, score) in students_score.items() if score >= 60}
# print(passed_student)

student_dict = {
    "student": ["Abhay", "james", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# #Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Abhay":
        print(row.score)
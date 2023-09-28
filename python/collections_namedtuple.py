from collections import namedtuple

Student = namedtuple('Student', 'ID MARKS CLASS NAME')

num_students = int(input())

column_names = input().split()

id_idx = column_names.index('ID')
marks_idx = column_names.index('MARKS')
class_idx = column_names.index('CLASS')
name_idx = column_names.index('NAME')


students = []

for _ in range(num_students):
    data = input().split()
    student = Student(ID=int(data[id_idx]), MARKS=int(data[marks_idx]), CLASS=data[class_idx], NAME=data[name_idx])
    students.append(student)

total_marks = sum(student.MARKS for student in students)
average_marks = total_marks / num_students

print(f'{average_marks:.2f}')

if __name__ == '__main__':
    student_info = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_info.append([name, score])

    sorted_students = sorted(student_info, key=lambda x: x[1])

    second_lowest_grade = sorted(set(s[1] for s in sorted_students))[1]

    second_lowest_students = [student[0] for student in sorted_students if student[1] == second_lowest_grade]

    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)

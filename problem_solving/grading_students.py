import os


def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if grade < 38:
            final_grades.append(grade)
        else:
            rounded_num = ((grade + 4) // 5) * 5
            if rounded_num - grade < 3:
                final_grades.append(rounded_num)
            else:
                final_grades.append(grade)
    return final_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

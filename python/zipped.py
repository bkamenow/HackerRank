m, n = map(int, input().split())

student_marks = []

for _ in range(n):
    student_marks.append(list(map(float, input().split())))

total_marks_by_student = [sum(x) for x in zip(*student_marks)]


result = [x / n for x in total_marks_by_student]

print(*result, sep='\n')

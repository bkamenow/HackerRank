if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    a = student_marks[query_name][0]
    b = student_marks[query_name][1]
    c = student_marks[query_name][2]

    average_score = (a + b + c) / len(student_marks[query_name])
    print(f'{average_score:.2f}')

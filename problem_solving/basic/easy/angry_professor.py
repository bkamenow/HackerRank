def angryProfessor(k, a):
    on_time_std = []
    late_std = []

    for i in a:
        if i <= 0:
            on_time_std.append(i)
        else:
            late_std.append(i)

    if len(on_time_std) >= k:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        print(result)
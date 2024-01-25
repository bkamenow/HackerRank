def squares(a, b):
    square_numbers_count = 0

    i = 1
    while i ** 2 <= b:
        if i ** 2 >= a:
            square_numbers_count += 1
        i += 1

    return square_numbers_count










if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(result)

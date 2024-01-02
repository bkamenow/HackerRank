def superDigit(n, k):
    sum = 0

    for c in n:
        sum += int(c)

    sum = sum * k
    sum = str(sum)
    if len(sum) == 1:
        return sum
    else:
        return superDigit(sum, 1)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)

def beautifulDays(i, j, k):
    beautiful_count = 0

    for day in range(i, j + 1):
        reversed_day = int(str(day)[::-1])
        difference = abs(day - reversed_day)

        if difference % k == 0:
            beautiful_count += 1

    return beautiful_count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    i = int(first_multiple_input[0])
    j = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
    print(result)

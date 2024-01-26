def repeatedString(s, n):
    count_in_single = s.count('a')

    full_repetitions = n // len(s)

    remaining_chars = n % len(s)

    count_in_remainder = s[:remaining_chars].count('a')

    total_count = count_in_single * full_repetitions + count_in_remainder

    return total_count


if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)

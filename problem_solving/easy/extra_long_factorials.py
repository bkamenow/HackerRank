def extraLongFactorials(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * extraLongFactorials(n - 1)


if __name__ == '__main__':
    n = int(input().strip())

    result = extraLongFactorials(n)

    print(result)

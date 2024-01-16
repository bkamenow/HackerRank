def findDigits(n):
    divisors = 0
    number_str = str(n)

    digits = [int(digit) for digit in number_str]

    for i in digits:
        if i == 0:
            pass
        elif n % i == 0:
            divisors += 1

    return divisors


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)

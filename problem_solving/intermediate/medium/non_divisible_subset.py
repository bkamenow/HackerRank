def nonDivisibleSubset(k, s):
    counts = [0] * k

    for num in s:
        counts[num % k] += 1

    res = min(counts[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            res += max(counts[i], counts[k - i])

    if k % 2 == 0:
        res += min(counts[k // 2], 1)

    return res


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)

def pickingNumbers(a):
    c = []
    nums = set(a)
    for i in nums:
        c.append(a.count(i) + a.count(i - 1))
    return max(c)


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)

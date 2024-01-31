def minimumBribes(q):
    bribes = 0

    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            return 'Too chaotic'

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    return bribes


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        res = minimumBribes(q)

        print(res)
def minimumBribes(q):
    s = 0

    while q != sorted(q):
        for i in range(len(q) - 1):
            if q[i] - (i + 1) > 2:
                print("Too chaotic")
                return

            if q[i] > q[i + 1]:
                s += 1
                q[i], q[i + 1] = q[i + 1], q[i]

    print(s)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

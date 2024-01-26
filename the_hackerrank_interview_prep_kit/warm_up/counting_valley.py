def countingValleys(steps, path):
    v = 0
    sl = 0

    for s in range(steps):
        m = path[s]

        if m == 'U':
            sl += 1
        elif m == 'D':
            sl -= 1

        if m == 'U' and sl == 0:
            v += 1

    return v


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)

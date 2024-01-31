def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = 0

    max_distance = max(max_distance, c[0])

    for i in range(1, len(c)):
        max_distance = max(max_distance, (c[i] - c[i - 1]) // 2)

    max_distance = max(max_distance, n - 1 - c[-1])

    return max_distance



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)

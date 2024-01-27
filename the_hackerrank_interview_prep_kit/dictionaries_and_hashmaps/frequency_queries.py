def freqQuery(queries):
    data = {}
    res = []

    for q, v in queries:
        if q == 1:
            if v in data:
                data[v] += 1
            else:
                data[v] = 1
        elif q == 2:
            if v in data and data[v] > 0:
                data[v] -= 1
        elif q == 3:
            if v in data.values():
                res.append(1)
            else:
                res.append(0)
    return res


if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print(ans)

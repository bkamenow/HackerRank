def pageCount(n, p):
    from_front = p // 2
    from_end = (n // 2) - (p // 2)

    return min(from_front, from_end)


if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
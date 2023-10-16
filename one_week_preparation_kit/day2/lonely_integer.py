def lonelyinteger(a):
    lonely = 0
    for num in a:
        lonely ^= num
    return lonely

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)
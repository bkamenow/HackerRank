def sockMerchant(n, ar):
    sock_dict = {}
    for sock in ar:
        if sock not in sock_dict:
            sock_dict[sock] = 1
        else:
            sock_dict[sock] += 1

    count_of_pairs = 0
    for value in sock_dict.values():
        count_of_pairs += value // 2

    return count_of_pairs

if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

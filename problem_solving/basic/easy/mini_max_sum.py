def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    idx = 0
    minimum_value = []
    maximum_value = []
    for i in sorted_arr:
        if idx < 4:
            minimum_value.append(i)
        if idx > 0:
            maximum_value.append(i)
        idx += 1
    print(f'{sum(minimum_value)} {sum(maximum_value)}')


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

def diagonalDifference(arr):
    left_to_right_sum = 0
    right_to_left_sum = 0
    n = len(arr)

    for i in range(n):
        left_to_right_sum += arr[i][i]
        right_to_left_sum += arr[i][n - 1 - i]

    return abs(left_to_right_sum - right_to_left_sum)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

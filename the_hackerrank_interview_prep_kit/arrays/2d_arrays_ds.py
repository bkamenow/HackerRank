def hourglassSum(arr):
    pattern = (
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (2, 0),
        (2, 1),
        (2, 2),
    )

    max_sum = float('-inf')

    for i in range(4):
        for j in range(4):
            if i + 2 < 6 and j + 2 < 6:
                current_sum = sum(arr[i + x][j + y] for x, y in pattern)

                max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)

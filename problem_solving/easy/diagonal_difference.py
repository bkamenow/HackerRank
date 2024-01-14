import os


def diagonalDifference(arr):
    left, right = 0, 0
    arr_len = len(arr)
    for i in range(0, arr_len):
        left += arr[i][i]
        right += arr[i][n - i - 1]

    return abs(left - right)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

def countingSort(arr):
    count = [0] * 100

    for num in arr:
        count[num] += 1

    return count


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(result)

def findMedian(arr):
    n = len(arr)

    arr.sort()

    middle_index = n // 2

    return arr[middle_index]



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(result)
def cutTheSticks(arr):
    result = []
    while arr:
        result.append(len(arr))
        min_length = min(arr)
        arr = [stick - min_length for stick in arr if stick - min_length > 0]
    return result

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print(result)

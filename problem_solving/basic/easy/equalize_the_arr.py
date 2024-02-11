from collections import Counter


def equalizeArray(arr):
    counts = Counter(arr)
    most_common = counts.most_common(1)[0][0]

    items_for_remove = [x for x in arr if x != most_common]

    return len(items_for_remove)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)

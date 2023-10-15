def plusMinus(arr):
    n = len(arr)
    positive = 0
    negative = 0
    zero = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1

    print(f"{positive / n:.6f}")
    print(f"{negative / n:.6f}")
    print(f"{zero / n:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

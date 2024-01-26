def minimumSwaps(arr):
    n = len(arr)
    swaps = 0

    position_dict = {value: index for index, value in enumerate(arr)}

    for i in range(n):
        correct_value = i + 1

        if arr[i] != correct_value:
            correct_position = position_dict[correct_value]

            arr[i], arr[correct_position] = arr[correct_position], arr[i]

            position_dict[arr[correct_position]] = correct_position
            position_dict[arr[i]] = i

            swaps += 1

    return swaps


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

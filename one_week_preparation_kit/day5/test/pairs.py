def pairs(k, arr):
    num_of_pairs = 0
    unique_elements = set(arr)

    for element in unique_elements:
        if element + k in unique_elements:
            num_of_pairs += 1

    return num_of_pairs


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)

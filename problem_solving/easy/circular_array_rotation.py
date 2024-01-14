def circularArrayRotation(a, k, queries):
    n = len(a)
    rotated_array = a[-k % n:] + a[:-k % n]

    final_arr = [rotated_array[i] for i in queries]

    return final_arr

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print(result)
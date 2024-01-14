def findSum(numbers, queries):
    n = len(numbers)

    prefix_sum = [0] * n
    zero_sum = 0

    for i in range(n):
        prefix_sum[i] = numbers[i]
        if numbers[i] == 0:
            zero_sum += 1
        if i > 0:
            prefix_sum[i] += prefix_sum[i - 1]

    results = []

    for query in queries:
        start_idx, end_idx, x = query
        total_sum = prefix_sum[end_idx - 1]

        if start_idx > 1:
            total_sum -= prefix_sum[start_idx - 2]

        total_sum += zero_sum * x
        results.append(total_sum)

    return results


if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    print(result)

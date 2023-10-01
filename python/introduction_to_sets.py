def average(array):
    distinct_heights = set(array)
    a = sum(distinct_heights)
    b = len(distinct_heights)
    average_sum = a / b
    return average_sum


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

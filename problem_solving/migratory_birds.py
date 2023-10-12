def migratoryBirds(arr):
    bird_counts = {}

    for bird in arr:
        if bird in bird_counts:
            bird_counts[bird] += 1
        else:
            bird_counts[bird] = 1

    max_count = max(bird_counts.values())
    most_frequent_birds = [bird for bird, count in bird_counts.items() if count == max_count]

    return min(most_frequent_birds)


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
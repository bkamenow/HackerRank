def efficientJanitor(weight):
    weight.sort()
    trips = 0

    while len(weight) > 0:
        current_trip_weight = 0

        for i in range(len(weight) - 1, -1, -1):
            if current_trip_weight + weight[i] <= 3.00:
                current_trip_weight += weight[i]
                weight.pop(i)

        trips += 1

    return trips


if __name__ == '__main__':
    weight_count = int(input().strip())

    weight = []

    for _ in range(weight_count):
        weight_item = float(input().strip())
        weight.append(weight_item)

    result = efficientJanitor(weight)

    print(result)

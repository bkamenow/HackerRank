def truckTour(petrolpumps):
    total_petrol = 0
    current_petrol = 0
    starting_point = 0

    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        total_petrol += petrol
        current_petrol += petrol - distance


        if current_petrol < 0:
            starting_point = i + 1
            current_petrol = 0

    if total_petrol >= 0:
        return starting_point
    else:
        return -1


if __name__ == '__main__':
    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    print(result)

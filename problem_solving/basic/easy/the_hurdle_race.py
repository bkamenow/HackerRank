def hurdleRace(k, height):
    max_hurdle_height = max(height)

    potion_needed = max_hurdle_height - k

    if potion_needed <= 0:
        return 0
    else:
        return potion_needed

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
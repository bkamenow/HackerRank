def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_fall = [x + a for x in apples]
    oranges_fall = [x + b for x in oranges]
    output_apples = 0
    output_oranges = 0
    for apple in apples_fall:
        if s <= apple <= t:
            output_apples += 1

    for orange in oranges_fall:
        if s <= orange <= t:
            output_oranges += 1

    print(output_apples)
    print(output_oranges)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
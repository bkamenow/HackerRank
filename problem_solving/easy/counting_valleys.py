def countingValleys(steps, path):
    path = [-1 if i == "D" else 1 for i in path]
    level = 0
    valley = 0
    for i in path:
        level += i
        if i > 0 and level == 0:
            valley += 1
    return valley


if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)

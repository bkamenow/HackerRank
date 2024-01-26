def jumpingOnClouds(c):
    jump = 2

    moves = 0

    while len(c) > 1:
        if len(c) >= 3:
            if c[jump] == 0 or c[jump - 1 ] == 1:
                c = c[2:]
            elif c[jump] == 1:
                c = c[1:]
        else:
            c = c[2:]
        moves += 1

    return moves


if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

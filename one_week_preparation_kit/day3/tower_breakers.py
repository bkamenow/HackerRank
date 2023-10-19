def towerBreakers(n, m):
    towers = []
    for i in range(n):
        towers.append(m)

    player1 = True

    for index, num in enumerate(towers):
        if num != 1:
            towers[index] = num // 2
            player1 = not player1
    if player1 is True:
        return 2
    else:
        return 1


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        print(result)

def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    obstacle_set = set((r, c) for r, c in obstacles)

    def is_within_board(r, c):
        return 1 <= r <= n and 1 <= c <= n

    count = 0

    for dr, dc in directions:
        r, c = r_q, c_q

        while is_within_board(r + dr, c + dc) and (r + dr, c + dc) not in obstacle_set:
            r += dr
            c += dc
            count += 1

    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

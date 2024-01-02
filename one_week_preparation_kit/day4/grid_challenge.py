def gridChallenge(grid):
    sorted_grid = []

    for row in grid:
        sorted_grid.append(sorted(row))
    cols = [True if list(i) == sorted(i) else False for i in zip(*sorted_grid)]
    if all(cols):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)

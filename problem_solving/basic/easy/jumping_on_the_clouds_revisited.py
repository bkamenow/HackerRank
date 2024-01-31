def jumpingOnClouds(c, k):
    energy = 100
    position = 0
    visited = set()

    while position not in visited:
        visited.add(position)

        if c[position] == 0:
            energy -= 1
        else:
            energy -= (1 + 2)

        position = (position + k) % len(c)

    return energy


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)

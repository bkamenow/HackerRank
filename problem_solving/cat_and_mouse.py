def catAndMouse(x, y, z):
    diff_x = abs(z - x)
    diff_y = abs(z - y)

    winner = ''
    if diff_x < diff_y:
        winner = 'Cat A'
    elif diff_x > diff_y:
        winner = 'Cat B'
    else:
        winner = 'Mouse C'

    return winner


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)

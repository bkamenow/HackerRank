def create_door_mat(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome = 'WELCOME'.center(M, '-')
    return '\n'.join(pattern + [welcome] + pattern[::-1])


if __name__ == '__main__':
    N, M = map(int, input().split())
    door_mat = create_door_mat(N, M)
    print(door_mat)

def staircase(n):
    spaces = n - 1
    for i in range(1, n + 1):
        print(f'{" " * spaces + "#" * i}')
        spaces -= 1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

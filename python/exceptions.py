T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        try:
            print(a // b)
        except ZeroDivisionError as err:
            print(f'Error Code: {err}')
    except ValueError as err:
        print(f'Error Code: {err}')

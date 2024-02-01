import re


def detector(p, i):
    match = re.match(p, i)

    if match:
        return True
    else:
        return False


if __name__ == '__main__':
    pattern = r'^[+\-.]?\d*\.\d+$|^([+\-.]?\d+)?\.\d+$'

    n = int(input())

    for _ in range(n):
        i = input()

        print(detector(pattern, i))

import math
from functools import reduce


def getTotalX(a, b):
    l = reduce(math.lcm, a)
    g = reduce(math.gcd, b)

    count = 0
    for i in range(l, int(g) + 1, l):
        if int(g) % i == 0:
            count += 1
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

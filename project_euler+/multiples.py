import sys


def sum_of_multiples(m, n):
    n -= 1
    num_multiples = n // m
    return m * num_multiples * (num_multiples + 1) // 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = (
            sum_of_multiples(3, n)
            + sum_of_multiples(5, n)
            - sum_of_multiples(15, n)
    )
    print(result)

from itertools import product

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
result = product(A, B)

print(*result)

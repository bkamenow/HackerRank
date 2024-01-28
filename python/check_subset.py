def is_subset(A, B):
    return set(A).issubset(set(B))

t = int(input())

for _ in range(t):
    m = int(input())
    set_A = list(map(int, input().split()))

    n = int(input())
    set_B = list(map(int, input().split()))

    result = is_subset(set_A, set_B)
    print(result)

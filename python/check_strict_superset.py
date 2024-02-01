def check_strict_superset(a, n):
    for s in n:
        is_subset = set(s).issubset(set(a))
        if not is_subset:
            return False

    return True


if __name__ == "__main__":
    A = list(map(int, input().split()))
    n = int(input())

    N = []
    for _ in range(n):
        N.append(list(map(int, input().split())))

    result = check_strict_superset(A, N)

    print(result)

from itertools import product


def maximize_value(m, lists):
    combinations = product(*lists)

    max_value = max(sum(x ** 2 for x in combination) % m for combination in combinations)

    return max_value


if __name__ == "__main__":
    n, m = map(int, input().split())

    lists = []
    for _ in range(n):
        elements = list(map(int, input().split()[1:]))
        lists.append(elements)

    result = maximize_value(m, lists)

    print(result)

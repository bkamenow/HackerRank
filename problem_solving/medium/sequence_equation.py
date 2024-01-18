def permutationEquation(p):
    result = []

    for x in range(1, len(p) + 1):
        index_of_x = p.index(x) + 1

        index_of_result = p.index(index_of_x) + 1

        result.append(index_of_result)

    return result


if __name__ == '__main__':
    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(result)

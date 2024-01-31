def permutationEquation(p):
    all_y = []

    for x in range(1, len(p) + 1):
        index_of_x = p.index(x) + 1

        index_of_result = p.index(index_of_x) + 1

        all_y.append(index_of_result)

    return all_y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(result)

import re


def find_indices_of_start_and_end(s, k):
    pattern = re.compile(k)
    indices = []
    for i in range(len(S)):
        result = pattern.match(s, i)
        if result:
            indices.append((result.start(), result.end() - 1))

    return indices


if __name__ == "__main__":
    S = input()
    k = input()
    result = find_indices_of_start_and_end(S, k)

    if result:
        print(*result, sep='\n')
    else:
        print((-1, -1))

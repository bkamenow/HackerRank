from collections import defaultdict


def countTriplets(arr, r):
    triplet_count = 0
    potential_middle = defaultdict(int)
    potential_end = defaultdict(int)

    for i in arr:
        if i % (r * r) == 0:
            triplet_count += potential_end[i // r]
        if i % r == 0:
            potential_end[i] += potential_middle[i // r]
        potential_middle[i] += 1

    return triplet_count


if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)

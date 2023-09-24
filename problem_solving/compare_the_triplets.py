import os


def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for x, y in zip(a, b):
        if x > y:
            a_points += 1
        elif x < y:
            b_points += 1

    return a_points, b_points


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

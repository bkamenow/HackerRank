def bigSorting(unsorted):
    return sorted(unsorted,key=lambda x: (len(x),x))


if __name__ == '__main__':

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print(result)

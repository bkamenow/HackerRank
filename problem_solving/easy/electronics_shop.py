def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()

    list_of_sums = []

    if keyboards[0] + drives[0] > b:
        return -1
    else:
        for i in keyboards:
            for j in drives:
                list_of_sums.append(i + j)

    list_of_sums.sort()

    for i in range(len(list_of_sums)):
        if list_of_sums[i] == b:
            return list_of_sums[i]

        elif list_of_sums[i] > b:
            return list_of_sums[i - 1]


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)

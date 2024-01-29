def maxPairs(skillLevel, minDiff):
    skillLevel.sort()
    n = len(skillLevel)
    i = 0
    x = []

    for j in range(n // 2):
        while i < n and skillLevel[i] - skillLevel[j] < minDiff:
            i += 1
        if i >= n:
            break
        x.append(i)
    x = x[:(n // 2)]

    pairs = 0
    k = n - 1
    for y in reversed(x):
        if y <= k:
            pairs += 1
            k -= 1

    return pairs

if __name__ == '__main__':
    skillLevel_count = int(input().strip())

    skillLevel = []

    for _ in range(skillLevel_count):
        skillLevel_item = int(input().strip())
        skillLevel.append(skillLevel_item)

    minDiff = int(input().strip())

    result = maxPairs(skillLevel, minDiff)

    print(result)

from itertools import groupby

S = input()
result = []

for key, group in groupby(S):
    result.append(tuple((len(list(group)), int(key))))

print(*result)

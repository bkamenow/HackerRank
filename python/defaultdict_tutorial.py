from collections import defaultdict

x1, x2 = map(int, input().split())

A = defaultdict(list)
B = []
for i in range(1, x1 + x2 + 1):
    value = input()
    if i <= x1:
        A[value].append(i)
    else:
        B.append(value)

for word in B:
    if word in A:
        positions = A[word]
        print(" ".join(map(str, positions)))
    else:
        print("-1")
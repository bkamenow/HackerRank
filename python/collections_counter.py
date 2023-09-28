from collections import Counter

X = int(input())
shoe_sizes = [int(x) for x in input().split()]
shoe_sizes = Counter(shoe_sizes)
N = int(input())

total_price = 0

for i in range(N):
    x, price = input().split()
    x = int(x)
    if x in shoe_sizes:
        if shoe_sizes[x] != 0:
            total_price += int(price)
            shoe_sizes[x] -= 1

print(total_price)

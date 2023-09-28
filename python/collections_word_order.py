n = int(input())

word_counts = {}

word_order = []

for _ in range(n):
    word = input().strip()
    if word not in word_counts:
        word_counts[word] = 0
        word_order.append(word)
    word_counts[word] += 1

print(len(word_counts))

occurrences = [word_counts[word] for word in word_order]
print(" ".join(map(str, occurrences)))

from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

count_a = letters.count('a')

total_combinations = list(combinations(range(n), k))

combinations_without_a = [combo for combo in total_combinations if all(letters[i] != 'a' for i in combo)]

prob_at_least_one_a = 1 - len(combinations_without_a) / len(total_combinations)

print(f"{prob_at_least_one_a:.4f}")

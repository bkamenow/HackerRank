from itertools import permutations

input_string, num = input().split()

permutations_list = list(permutations(input_string, int(num)))
permutations_list.sort()

for perm in permutations_list:
    print(''.join(perm))
    
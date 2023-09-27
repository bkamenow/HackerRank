from itertools import combinations

input_string, num = input().split()
input_string = ''.join(sorted(input_string))
num = int(num)

for i in range(1, num + 1):
    combinations_list = list(combinations(input_string, i))
    combinations_list.sort()

    for combo in combinations_list:
        print(''.join(combo))

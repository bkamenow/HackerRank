from itertools import combinations_with_replacement

input_string, num = input().split()
input_string = ''.join(sorted(input_string))  # Sort the input string lexicographically
num = int(num)

combinations_with_replacement_list = list(combinations_with_replacement(input_string, num))


for combo in combinations_with_replacement_list:
    print(''.join(combo))

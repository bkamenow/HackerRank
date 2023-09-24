def is_palindrome(num):
    return str(num) == str(num)[::-1]


n = int(input())
int_list = [int(x) for x in input().split()]

for num in int_list:
    if is_palindrome(num) and all(val > 0 for val in int_list):
        print(True)
        break
else:
    print(False)

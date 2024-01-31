def appendAndDelete(s, t, k):
    common_length = 0

    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    total_operations = len(s) + len(t) - 2 * common_length
    if total_operations <= k and (total_operations - k) % 2 == 0 or len(s) + len(t) < k:
        return 'Yes'
    elif len(s) + len(t) <= k:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)

#
# hackerhappy
# hackerrank
# 9
def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered_string = [c for c in s if c == char1 or c == char2]
                if is_alternating(filtered_string):
                    max_length = max(max_length, len(filtered_string))

    return max_length


def is_alternating(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True


if __name__ == '__main__':
    l = int(input().strip())

    s = input()

    result = alternate(s)

    print(result)

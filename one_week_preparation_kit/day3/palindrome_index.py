def is_palindrome(s):
    return s == s[::-1]


def palindromeIndex(s):
    if is_palindrome(s):

        return -1

    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:

            without_left = s[:i] + s[i + 1:]
            without_right = s[:-(i + 1)] + s[-i:]

            if is_palindrome(without_left):
                return len(s) - i - 1
            if is_palindrome(without_right):
                return i


    return -1


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)

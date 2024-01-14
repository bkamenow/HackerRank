def isBalanced(s):
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for bracket in s:
        if bracket in bracket_mapping.values():
            stack.append(bracket)
        elif bracket in bracket_mapping.keys():
            if not stack or stack.pop() != bracket_mapping[bracket]:
                return "NO"
        else:
            return "NO"

    return "YES" if not stack else "NO"


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)
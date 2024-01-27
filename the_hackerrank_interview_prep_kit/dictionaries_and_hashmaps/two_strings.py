def twoStrings(s1, s2):
    res = 'NO'
    for i in s1:
        if i in s2:
            res = 'YES'
            break
    return res

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)

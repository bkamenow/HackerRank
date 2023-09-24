if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for l in s:
        if l.isalnum():
            alnum = True
        if l.isalpha():
            alpha = True
        if l.isdigit():
            digit = True
        if l.islower():
            lower = True
        if l.isupper():
            upper = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

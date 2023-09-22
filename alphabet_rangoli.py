import string


def print_rangoli(size):
    width = n * 4 - 3
    re_alpha = list(string.ascii_lowercase[0:size][::-1])

    for i in range(n):
        row = re_alpha[:(i + 1)] + re_alpha[:i][::-1]
        print("-".join(row).center(width, "-"))

    for i in range(size - 2, -1, -1):
        row = re_alpha[:(i + 1)] + re_alpha[:i][::-1]
        print("-".join(row).center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

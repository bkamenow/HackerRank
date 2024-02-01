def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            num = l[i][-10:]
            l[i] = f'+91 {num[:5]} {num[5:]}'
        f(l)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

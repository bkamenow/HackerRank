from dateutil import parser


def time_delta(t1, t2):
    delta = parser.parse(t1) - parser.parse(t2)
    return "{:.0f}".format(abs(delta.total_seconds()))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)

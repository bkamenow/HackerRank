import math


def viralAdvertising(n):
    shared_to = 5
    total_ppl = 0

    for i in range(n):
        n = math.floor(shared_to / 2)
        total_ppl += n
        shared_to = n * 3

    return total_ppl



if __name__ == '__main__':


    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sorted_arr = sorted(arr, reverse=True)
    for score in sorted_arr:
        if score < sorted_arr[0]:
            print(score)
            break




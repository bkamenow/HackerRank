if __name__ == '__main__':
    s = input()
    result = {}
    for ch in s:
        if ch not in result:
            result[ch] = 1
        else:
            result[ch] += 1

    sorted_dict = sorted(result.items(), key=lambda item: (-item[1], item[0]))
    for i in range(3):
        print(*sorted_dict[i])
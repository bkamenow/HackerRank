def merge_the_tools(string, k):
    str_list = [string[i:i + k] for i in range(0, len(string), k)]
    for i in str_list:
        print(''.join(sorted(set(i), key=i.index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

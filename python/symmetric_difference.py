def difference(a, b):
    a = set(sorted(a))
    b = set(sorted(b))
    diff = b.symmetric_difference(a)
    result = []
    for i in diff:
        result.append(i)
    return '\n'.join(map(str, result))




if __name__ == '__main__':
    n1 = int(input())
    set_a = list(map(int, input().split()))
    n2 = int(input())
    set_b = list(map(int, input().split()))
    result = difference(set_a, set_b)
    print(result)

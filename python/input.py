def polynomial(p, k, polynomial_str):
    evaluated_polynomial = polynomial_str.replace('x', str(p))

    if eval(evaluated_polynomial) == k:
        return True
    else:
        return False


if __name__ == '__main__':
    p, k = map(int, input().split())
    polynomial_str = input()

    res = polynomial(p, k, polynomial_str)

    print(res)

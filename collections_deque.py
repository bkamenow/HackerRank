from collections import deque


def perform_deque_operations(operations):
    d = deque()
    output = []

    for op in operations:
        operation, *args = op.split()
        if operation == 'append':
            d.append(int(args[0]))
        elif operation == 'appendleft':
            d.appendleft(int(args[0]))
        elif operation == 'pop':
            d.pop()
        elif operation == 'popleft':
            d.popleft()

    output = ' '.join(map(str, d))
    return output


if __name__ == "__main__":
    n = int(input())
    operations = [input() for _ in range(n)]

    result = perform_deque_operations(operations)
    print(result)

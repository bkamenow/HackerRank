if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        command = input()

        if command == 'print':
            print(arr)
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
        elif command.split()[0] == 'append':
            _, n = command.split()
            arr.append(int(n))
        elif command.split()[0] == 'remove':
            _, n = command.split()
            arr.remove(int(n))
        elif command.split()[0] == 'insert':
            _, idx, n = command.split()
            arr.insert(int(idx), int(n))


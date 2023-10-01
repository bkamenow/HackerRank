n = int(input())
s = set(map(int, input().strip().split()))
n_commands = int(input())

for _ in range(n_commands):
    command = input().strip().split()
    if command[0] == 'pop':
        if s:
            s.pop()
    elif command[0] == 'remove':
        element = int(command[1])
        if element in s:
            s.remove(element)
    elif command[0] == 'discard':
        element = int(command[1])
        if element in s:
            s.discard(element)

print(sum(s))

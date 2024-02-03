import re

pattern = r'^(?!.*(\d)(?:-?\1){3})[4-6]\d{3}(?:-?\d{4}){3}$'

n = int(input())

for _ in range(n):
    card = input()

    match = re.match(pattern, card)

    if match:
        print('Valid')
    else:
        print('Invalid')

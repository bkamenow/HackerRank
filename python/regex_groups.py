import re

input_string = input().strip()

match = re.search(r'([a-zA-Z0-9])\1', input_string)

if match:
    print(match.group(1))
else:
    print(-1)

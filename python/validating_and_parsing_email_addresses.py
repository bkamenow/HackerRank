import re
import email.utils


def validate_email(e, pattern):
    match = re.match(pattern, e)

    if match:
        return True
    else:
        return False


if __name__ == '__main__':
    pattern = r'^[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

    n = int(input())

    for _ in range(n):
        user_data = input()

        _, user_email = email.utils.parseaddr(user_data)

        if validate_email(user_email, pattern):
            print(user_data)

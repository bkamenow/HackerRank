import re


def validate_uid(uid_list):
    pattern = (
        r'^(?!.*(.).*\1)'  # No repeating characters
        r'(?=.*[A-Z].*[A-Z])'  # At least 2 uppercase English alphabet characters
        r'(?=.*\d.*\d.*\d)'  # At least 3 digits (0-9)
        r'^[A-Za-z0-9]{10}$'  # Exactly 10 alphanumeric characters
    )

    for uid in uid_list:
        result = ''

        if re.match(pattern, uid):
            result = 'Valid'
        else:
            result = 'Invalid'
        print(result)


if __name__ == '__main__':
    uid_list = []

    for _ in range(int(input())):
        uid_list.append(input())

    validate_uid(uid_list)

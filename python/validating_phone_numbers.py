import re


def phone_number_validator(number):
    pattern = r'^[789]\d{9}$'
    validate = re.fullmatch(pattern, number)
    if validate:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        phone_number = input()
        print(phone_number_validator(phone_number))

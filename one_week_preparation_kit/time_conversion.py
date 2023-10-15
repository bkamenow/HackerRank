def timeConversion(s):
    period = s[8:]
    hh = int(s[:2])
    ms = s[2:8]

    time = ''
    if hh == 12:
        if period == 'PM':
            time = f'{hh}{ms}'
        elif period == 'AM':
            time = f'00{ms}'
    elif period == 'PM':
        hh += 12
        time = f'{hh}{ms}'
    elif period == 'AM':
        time = f'0{hh}{ms}'

    return time


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)

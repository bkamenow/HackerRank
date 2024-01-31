def is_julian_leap_year(year):
    return year % 4 == 0


def is_gregorian_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def dayOfProgrammer(year):
    if year < 1918:
        if is_julian_leap_year(year):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year > 1918:
        if is_gregorian_leap_year(year):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    else:  # Year 1918
        return f"26.09.{year}"


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)

def timeInWords(h, m):
    hours = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

    minutes = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
        "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine", "half"
    ]

    time_in_words = ''

    if m == 0:
        time_in_words = f"{hours[h]} o' clock"
    elif m == 1:
        time_in_words = f"{minutes[m]} minute past {hours[h]}"
    elif m == 15 or m == 30:
        time_in_words = f"{minutes[m]} past {hours[h]}"
    elif m == 45:
        time_in_words = f"{minutes[60 - m]} to {hours[(h + 1) % 12]}"
    elif m < 30:
        time_in_words = f"{minutes[m]} minutes past {hours[h]}"
    else:
        time_in_words = f"{minutes[60 - m]} minutes to {hours[(h + 1) % 12]}"

    return time_in_words


if __name__ == '__main__':
    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result)

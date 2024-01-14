import os


def timeConversion(s):
    time_parts = s.split(":")
    hour = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2][:2])
    meridian = time_parts[2][-2:]

    if meridian == "AM" and hour == 12:
        hour = 0
    elif meridian == "PM" and hour != 12:
        hour += 12

    time_24_hour = "{:02d}:{:02d}:{:02d}".format(hour, minutes, seconds)
    return time_24_hour


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

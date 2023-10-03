import calendar

mm, dd, year = map(int, input().strip().split())

day_of_week = calendar.weekday(year, mm, dd)

day_name = calendar.day_name[day_of_week].upper()

print(day_name)

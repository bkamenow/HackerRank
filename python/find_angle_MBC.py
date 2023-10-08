import math

ab = int(input())
bc = int(input())

theta = round(math.degrees(math.atan(ab / bc)))

print(f"{theta}{chr(176)}")

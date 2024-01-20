from collections import Counter

K = int(input())

rooms = list(map(int, input().split()))


count_rooms = Counter(rooms)

capitan_room = [num for num, count in count_rooms.items() if count == 1]

print(*capitan_room)

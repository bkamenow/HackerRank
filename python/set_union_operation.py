n = int(input())
english_subscribers = set(map(int, input().split()))
m = int(input())
french_subscribers = set(map(int, input().split()))

total_subscribers = len(english_subscribers.union(french_subscribers))

print(total_subscribers)

from collections import OrderedDict

N = int(input())

ordered_dict = OrderedDict()

for _ in range(N):
    items = input().split()
    item_name = ' '.join(items[:-1])
    item_price = int(items[-1])

    if item_name in ordered_dict:
        ordered_dict[item_name] += item_price
    else:
        ordered_dict[item_name] = item_price

for name, price in ordered_dict.items():
    print(name, price)

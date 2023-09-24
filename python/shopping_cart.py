import os


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add(self, item):
        self.cart.append(item)

    def total(self):
        return sum(item.price for item in self.cart)

    def __len__(self):
        return len(self.cart)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)

    fptr.close()

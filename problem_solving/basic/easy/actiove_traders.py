def mostActive(customers):
    traders_activity = {}
    total_trades = len(customers)

    for customer in customers:
        if customer not in traders_activity:
            traders_activity[customer] = 1
        else:
            traders_activity[customer] += 1

    threshold = 0.05 * total_trades

    active_traders = [customer for customer, count in traders_activity.items() if count >= threshold]

    sorted_active_traders = sorted(active_traders)

    return sorted_active_traders


if __name__ == '__main__':

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    print(result)

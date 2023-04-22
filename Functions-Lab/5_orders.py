order = input()
order_count = int(input())


def total_price_calculator(quantity, count):
    if quantity == "coffee":
        return count * 1.50
    elif quantity == "water":
        return count * 1.00
    elif quantity == "coke":
        return count * 1.40
    elif quantity == "snacks":
        return count * 2.00


total_price = total_price_calculator(order, order_count)
print(f"{total_price:.2f}")

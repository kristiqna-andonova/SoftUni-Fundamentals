orders = int(input())

total_orders = 0

for _ in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsules = int(input())

    if capsule_price < 0.01 or capsule_price > 100.00:
        continue

    if days < 1 or days > 31:
        continue

    if capsules < 1 or days > 2000:
        continue

    order_price = capsule_price * days * capsules
    total_orders += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_orders:.2f}")

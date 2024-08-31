fruit_price = [25, 10, 45, 30, 60, 15, 15]


def maxCustom(fruit_price):
    max_price = 0
    for price in fruit_price:
        if price > max_price:
            max_price = price
    return max_price

print("The max is", max(fruit_price))
print("The min is", min(fruit_price))

print(maxCustom(fruit_price))
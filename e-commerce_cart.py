def calculate_total(cart_items):
    if not cart_items:
        return "Cart is empty!"
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total -= total * 0.10
    return f"Total Price: {total:.2f}"

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calculate_total(cart_items))

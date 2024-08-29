order_size = "Medium"
extra_shot = False

if extra_shot:
    coffee = order_size + " " + "Coffee with an extra shot"
else:
    coffee = order_size + " "+ "coffee"

print("order", coffee)

items = ["apple", "orange", "banana", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
      print("Duplicate item", item )
      break
    unique_item.add(item)
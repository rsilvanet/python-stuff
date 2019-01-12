iterations = 20
items = [0, 1]

for i in range(iterations):
    items.append(items[i] + items[i + 1])

print(items)
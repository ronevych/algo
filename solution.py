def place_items(items):
    items = sorted(items)[::-1]
    most_expensive_items = items[:len(items) // 3 + 1]
    rest_items = items[len(items) // 3:]
    res = []
    for i in range(len(items)):
        if i % 3 == 2:
            res.append(most_expensive_items.pop(0))
        else:
            res.append(rest_items.pop(0))
    return res

items = [10000, 1000, 2323, 4004, 6000, 5432, 11111, 10000, 10000, 10000, 20000, 123, 1432, 3244]
place_items(items)
print(place_items(items))

def calculate_minimal_cost(items, discount):
    items = place_items(items)
    res = 0
    for i in range(len(items)):
        if i % 3 == 2:
            res += items[i] * (100 - discount) / 100 # визначення відсотка знижки
        else:
            res += items[i]
    return round(res, 2)

print(calculate_minimal_cost(items, 10))
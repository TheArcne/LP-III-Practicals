def fractional_knapsack(items, capacity):
    n = int(input("Enter the number of items: "))
    items = []
    for i in range(n):
        print(f"For item {i + 1}:")
        weight = float(input("Enter the weight: "))
        value = float(input("Enter the value: "))
        items.append((weight, value))

    capacity = float(input("Enter the capacity of the knapsack: "))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    
    total_value = 0.0
    knapsack = []

    for item in items:
        weight, value = item
        if capacity >= weight:
            total_value += value
            knapsack.append((weight, value))
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += fraction * value
            knapsack.append((fraction*weight, fraction * value))
            break

    return total_value, knapsack

max_value, selected_items = fractional_knapsack(items, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)

def max_weight_greedy(weights, max_capacity):
    weights.sort(reverse=True)
    total_weight = 0
    for weight in weights:
        if total_weight + weight <= max_capacity:
            total_weight += weight
        else:
            break
    return total_weight

# Test Case 1
n = 5
weights = [10, 20, 30, 40, 50]
max_capacity = 60

max_weight = max_weight_greedy(weights, max_capacity)
print("Maximum Weight:", max_weight)

def min_containers_greedy(weights, max_capacity):
    weights.sort(reverse=True)
    num_containers = 0
    current_capacity = 0
    for weight in weights:
        if current_capacity + weight > max_capacity:
            num_containers += 1
            current_capacity = 0
        current_capacity += weight
    if current_capacity > 0:
        num_containers += 1
    return num_containers

# Test Case 1
n = 7
weights = [5, 10, 15, 20, 25, 30, 35]
max_capacity = 50

num_containers = min_containers_greedy(weights, max_capacity)
print("Minimum Number of Containers:", num_containers)

def maxmin(numbers):
    if not numbers:
        return None, None
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum
numbers = [3, 5, 1, 8, 2]
max_value, min_value = maxmin(numbers)
print("Maximum:", max_value)
print("Minimum:", min_value)

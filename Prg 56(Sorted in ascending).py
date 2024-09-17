def find_max_min(arr):
    max_val = arr[-1]
    min_val = arr[0]

    return max_val, min_val

arr = [2, 4, 6, 8, 10, 12, 14, 18]
max_val, min_val = find_max_min(arr)

print("Maximum value:", max_val)
print("Minimum value:", min_val)

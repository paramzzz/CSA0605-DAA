def find_max_min(arr):
    # Initialize max and min values with the first element of the array
    max_val = arr[0]
    min_val = arr[0]

    # Iterate over the array to find the max and min values
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    # Return the max and min values
    return max_val, min_val

# Test the function with an example array
arr = [5,7,3,4,9,12,6,2]
max_val, min_val = find_max_min(arr)

# Print the max and min values
print("Maximum value:", max_val)
print("Minimum value:", min_val)

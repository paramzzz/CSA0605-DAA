def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Initialize a flag to track if any swaps were made in the current pass
        swapped = False
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True to indicate that a swap was made
                swapped = True
        # If no swaps were made in the current pass, the list is already sorted
        if not swapped:
            break
    return arr

# Test Cases
print("Test Case 1:")
print("Input: [64, 25, 12, 22, 11]")
print("Expected Output: [11, 12, 22, 25, 64]")
print("Actual Output:", bubble_sort([64, 25, 12, 22, 11]))

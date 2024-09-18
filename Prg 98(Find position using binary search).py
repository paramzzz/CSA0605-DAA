def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            print("Comparisons:", comparisons)
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print("Comparisons:", comparisons)
    return -1  # not found

print("Test Case 1:")
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
target = 20
print("Original Array:", arr)
index = binary_search(arr, target)
if index != -1:
    print("Element", target, "found at index", index)
else:
    print("Element", target, "not found")


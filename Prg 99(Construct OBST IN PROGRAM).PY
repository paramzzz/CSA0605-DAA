def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        print("Low:", low, "High:", high, "Mid:", mid)
        print("Mid element:", arr[mid])
        if arr[mid] == target:
            print("Comparisons:", comparisons)
            return mid
        elif arr[mid] < target:
            print("Target is greater than mid element, moving to right half")
            low = mid + 1
        else:
            print("Target is less than mid element, moving to left half")
            high = mid - 1

    print("Comparisons:", comparisons)
    return -1  # not found


print("Test Case 1:")
arr = [3, 9, 14, 19, 25, 31, 42, 47, 53]
target = 31
print("Original Array:", arr)
index = binary_search(arr, target)
if index != -1:
    print("Element", target, "found at index", index)
else:
    print("Element", target, "not found")


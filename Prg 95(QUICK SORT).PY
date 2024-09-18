def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    print("Pivot:", pivot)
    print("Less:", less)
    print("Greater:", greater)
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Test Cases
print("Test Case 1:")
arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print("Original Array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)


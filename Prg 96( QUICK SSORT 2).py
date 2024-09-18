def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("Pivot:", pivot)
    print("Left:", left)
    print("Middle:", middle)
    print("Right:", right)
    return quick_sort(left) + middle + quick_sort(right)

# Test Case
arr = [19, 72, 35, 46, 58, 91, 22, 31]
print("Original Array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)

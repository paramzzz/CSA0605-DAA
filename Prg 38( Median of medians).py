def median_of_medians(arr, k):
    if len(arr) < 10:
        return sorted(arr)[k]
    sublists = [arr[j:j + 5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    pivot = median_of_medians(medians, len(medians) // 2)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    k_pivot = len(low)
    if k < k_pivot:
        return median_of_medians(low, k)
    elif k > k_pivot:
        return median_of_medians(high, k - k_pivot - 1)
    else:
        return pivot
arr = [3, 6, 2, 8, 7, 5, 1, 4]
k = 3  
result = median_of_medians(arr, k)
print(result)

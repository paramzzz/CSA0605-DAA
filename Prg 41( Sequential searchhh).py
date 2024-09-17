def findKthPositive(arr, k):
    arr_set = set(arr)
    
    missing_count = 0
    
    current = 1
    
    while True:
        if current not in arr_set:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1

arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))  # Output: 9

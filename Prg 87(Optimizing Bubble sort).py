def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

print("Test Case 1:")
print("Input: []")
print("Expected Output: []")
print("Actual Output:", selection_sort([]))


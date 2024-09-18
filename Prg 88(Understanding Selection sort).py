def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

input_array = [5, 2, 9, 1, 5, 6]
output_array = selection_sort(input_array)
print("Input:", input_array)
print("Output:", output_array)

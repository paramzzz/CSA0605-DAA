def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

input_array = [4, 3, 5, 1]
output_array = insertion_sort(input_array)
print("Input:", input_array)
print("Output:", output_array)

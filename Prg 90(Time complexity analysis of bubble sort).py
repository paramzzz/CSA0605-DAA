def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

input_array = [3, 1, 4, 2, 5]
output_array = bubble_sort(input_array)
print("Input:", input_array)
print("Output:", output_array)

innput_array = [1, 2, 3, 4, 5]
ooutput_array = bubble_sort(innput_array)
print("Input:", innput_array)
print("Output:", ooutput_array)

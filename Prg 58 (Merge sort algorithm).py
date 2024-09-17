def merge_sort(arr, comparisons=0):
    if len(arr) <= 1:
        return arr, comparisons

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left, comparisons = merge_sort(left, comparisons)
    right, comparisons = merge_sort(right, comparisons)

    result, comparisons = merge(left, right, comparisons)

    return result, comparisons

def merge(left, right, comparisons):
    result = []
    while len(left) > 0 and len(right) > 0:
        comparisons += 1
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result, comparisons

arr = [12, 4, 78, 23, 45, 67, 89, 1]
arr, comparisons = merge_sort(arr)

print("Sorted array:", arr)
print("Number of comparisons:", comparisons)

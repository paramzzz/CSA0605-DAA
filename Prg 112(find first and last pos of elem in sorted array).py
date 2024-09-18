def search_range(nums, target):
    def binary_search(arr, target, find_first):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first_occurrence = binary_search(nums, target, True)
    if first_occurrence == -1:
        return [-1, -1]
    last_occurrence = binary_search(nums, target, False)
    return [first_occurrence, last_occurrence]
nums = [5, 7, 7, 8, 8, 10]
target = 8
output = search_range(nums, target)
print(output)  # [3, 4]

def search_rotated_array(nums, target):
    """
    Find the index of the target element in a rotated sorted array.

    Args:
        nums: A rotated sorted array of distinct integers.
        target: The target element to search for.

    Returns:
        The index of the target element if it is in nums, or -1 if it is not in nums.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # If the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Example
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
index = search_rotated_array(nums, target)
print(f"Index of {target}: {index}")  # Output: 4

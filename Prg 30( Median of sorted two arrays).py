def findMedianSortedArrays(nums1, nums2):
        
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    total_length = len(nums1) + len(nums2)
    
    half_length = total_length // 2
    
    left, right = 0, len(nums1) - 1
    
    while True:
        i = (left + right) // 2
        
        j = half_length - i - 2
        
        nums1_left = nums1[i] if i >= 0 else float('-infinity')
        nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')
        nums2_left = nums2[j] if j >= 0 else float('-infinity')
        nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')
        
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if total_length % 2:
                return min(nums1_right, nums2_right)
            else:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5

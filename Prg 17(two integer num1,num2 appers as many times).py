def intersect(nums1, nums2):
    from collections import Counter
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    intersection = count1 & count2
    return list(intersection.elements())
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersect(nums1, nums2)
print(result) 

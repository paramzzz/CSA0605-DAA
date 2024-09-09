def maxSubarraySumCircular(nums):

    total_sum = sum(nums)
    
    max_ending_here = nums[0]
    max_so_far = nums[0]
    
    min_ending_here = nums[0]
    min_so_far = nums[0]
    
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
        
        min_ending_here = min(num, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)
    
    if total_sum == min_so_far:
        return max_so_far
    else:
        return max(max_so_far, total_sum - min_so_far)

nums = [5, -3, 5]
print(maxSubarraySumCircular(nums))  # Output: 10

nums = [1, -2, 3, -2]
print(maxSubarraySumCircular(nums))  # Output: 3

nums = [-3, -2, -1]
print(maxSubarraySumCircular(nums))  # Output: -1

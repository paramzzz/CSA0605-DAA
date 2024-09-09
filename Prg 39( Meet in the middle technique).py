def meet_in_middle(target, nums):
    def subsets_sum(nums):
        res = []
        for i in range(1 << len(nums)):
            subset = [nums[j] for j in range(len(nums)) if (i & (1 << j)) > 0]
            res.append(subset)
        return res
    first_half = subsets_sum(nums[:len(nums)//2])
    second_half = subsets_sum(nums[len(nums)//2:])
    first_half_sums = [sum(subset) for subset in first_half]
    second_half_sums = [sum(subset) for subset in second_half]
    second_half_sums.sort()
    result = 0
    for sum1 in first_half_sums:
        left = target - sum1
        low, high = 0, len(second_half_sums) - 1
        while low < len(second_half_sums) and high >= 0:
            sum2 = second_half_sums[low] + second_half_sums[high]
            if sum2 <= left:
                result = max(result, sum1 + sum2)
                low += 1
            else:
                high -= 1
    return result
target_sum = 20
numbers = [10, 5, 2, 7]
print(meet_in_middle(target_sum, numbers))

def numIdenticalPairs(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    good_pairs = 0
    for num in count:
        n = count[num]
        good_pairs += n * (n - 1) // 2
    
    return good_pairs

print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # Output: 4
print(numIdenticalPairs([1, 1, 1, 1]))  # Output: 6
print(numIdenticalPairs([1, 2, 3]))  # Output: 0

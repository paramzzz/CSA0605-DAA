def sort_array_by_parity_II(nums):
    odd_indices = [num for i, num in enumerate(nums) if i % 2 == 1]
    even_indices = [num for i, num in enumerate(nums) if i % 2 == 0]
    
    odd_indices.sort()
    even_indices.sort()
    
    result = []
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(even_indices.pop(0))
        else:
            result.append(odd_indices.pop(0))
    
    return result
nums = [4, 5, 2, 7]
print(sort_array_by_parity_II(nums))

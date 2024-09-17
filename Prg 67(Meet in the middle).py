def meet_in_the_middle(arr, target):
    
    n = len(arr)
    mid = n // 2

    left_subsets = []
    for i in range(2**mid):
        subset = []
        for j in range(mid):
            if (i & (1 << j)):
                subset.append(arr[j])
        left_subsets.append(subset)

    right_subsets = []
    for i in range(2**(n - mid)):
        subset = []
        for j in range(n - mid):
            if (i & (1 << j)):
                subset.append(arr[mid + j])
        right_subsets.append(subset)

    closest_sum = float('inf')
    closest_subset = []
    for left in left_subsets:
        for right in right_subsets:
            total_sum = sum(left) + sum(right)
            if abs(total_sum - target) < abs(closest_sum - target):
                closest_sum = total_sum
                closest_subset = left + right

    return closest_subset

b = [1, 3, 2, 7, 4, 6]
target_b = 10
print("Closest subset to", target_b, ":", meet_in_the_middle(b, target_b))

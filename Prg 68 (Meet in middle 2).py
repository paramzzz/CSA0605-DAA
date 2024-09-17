def meet_in_the_middle(arr, exact_sum):
    """
    Function to determine if there is a subset that sums exactly to the exact sum using the Meet in the Middle technique.

    Args:
    arr (list): The given array of integers.
    exact_sum (int): The exact sum.

    Returns:
    bool: True if there is a subset that sums exactly to the exact sum, otherwise False.
    """
    n = len(arr)
    mid = n // 2

    # Generate all possible subsets of the first half
    left_subsets = []
    for i in range(2**mid):
        subset = []
        for j in range(mid):
            if (i & (1 << j)):
                subset.append(arr[j])
        left_subsets.append(subset)

    # Generate all possible subsets of the second half
    right_subsets = []
    for i in range(2**(n - mid)):
        subset = []
        for j in range(n - mid):
            if (i & (1 << j)):
                subset.append(arr[mid + j])
        right_subsets.append(subset)

    # Find the pair of subsets that sums up to the exact sum
    for left in left_subsets:
        for right in right_subsets:
            if sum(left) + sum(right) == exact_sum:
                return True

    return False


# Example usage
E = [1, 3, 9, 2, 7, 12]
exact_sum = 15
print("Is there a subset that sums exactly to", exact_sum, ":", meet_in_the_middle(E, exact_sum))

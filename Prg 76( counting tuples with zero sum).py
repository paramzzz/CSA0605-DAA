def count_zero_sum_tuples(A, B, C, D):
    """
    Function to count the number of tuples (i, j, k, l) such that A[i] + B[j] + C[k] + D[l] is zero.

    Args:
    A (list): The first list of integers.
    B (list): The second list of integers.
    C (list): The third list of integers.
    D (list): The fourth list of integers.

    Returns:
    int: The number of tuples with zero sum.
    """
    # Create a hashmap to store the sums of pairs from A and B
    AB_sums = {}
    for a in A:
        for b in B:
            sum_ab = a + b
            if sum_ab not in AB_sums:
                AB_sums[sum_ab] = 0
            AB_sums[sum_ab] += 1

    # Initialize the count of tuples with zero sum
    count = 0

    # Iterate over the pairs from C and D
    for c in C:
        for d in D:
            sum_cd = -c - d  # Note the negative sign
            if sum_cd in AB_sums:
                count += AB_sums[sum_cd]

    return count


# Example usage
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print("The number of tuples with zero sum is:", count_zero_sum_tuples(A, B, C, D))

def generate_subsets(S):
    
    subsets = [[]]

    for elem in sorted(S):
        subsets.extend([subset + [elem] for subset in subsets])

    return subsets


A = [1, 2, 3]
print("Subsets of", A, ":", generate_subsets(A))

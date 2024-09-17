import itertools

def generate_subsets_with_element(E, x):
    subsets = []
    for r in range(1, len(E) + 1):
        for subset in itertools.combinations(E, r):
            if x in subset:
                subsets.append(list(subset))
    return subsets

E = [2, 3, 4, 5]
x = 3
print("Subsets of", E, "containing", x, ":", generate_subsets_with_element(E, x))

def median_of_medians(arr, k):
    
    if len(arr) == 1:
        return arr[0]

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    medians = [sorted(group)[len(group)//2] for group in groups]

    if len(medians) > 1:
        median_of_medians_val = median_of_medians(medians, len(medians)//2 + 1)
    else:
        median_of_medians_val = medians[0]

    left = [x for x in arr if x < median_of_medians_val]
    middle = [x for x in arr if x == median_of_medians_val]
    right = [x for x in arr if x > median_of_medians_val]

    if k <= len(left):
        return median_of_medians(left, k)
    elif k <= len(left) + len(middle):
        return middle[0]
    else:
        return median_of_medians(right, k - len(left) - len(middle))


arr = [12, 3, 5, 7, 19]
k = 2
print("The {}-th smallest element is: {}".format(k, median_of_medians(arr, k)))

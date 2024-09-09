import heapq
import math

def kClosest(points, k):
    distances = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in points]

    return [point for distance, point in heapq.nsmallest(k, distances)]

points = [[1, 3], [-2, 2]]
k = 1
print(kClosest(points, k))  # Output: [[-2, 2]]

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(kClosest(points, k))  # Output: [[3, 3], [-2, 4]]

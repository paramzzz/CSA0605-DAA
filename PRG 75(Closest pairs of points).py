import math

def k_closest_points(points, k):
   
    distances = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in points]

    distances.sort()

    return [point for distance, point in distances[:k]]


points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print("The {} closest points to the origin are: {}".format(k, k_closest_points(points, k)))

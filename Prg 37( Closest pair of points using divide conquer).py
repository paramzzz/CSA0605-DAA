import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def closest_pair(points):
    points.sort(key=lambda x: x[0])
    return closest_pair_util(points)

def closest_pair_util(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)
    mid = n // 2
    mid_point = points[mid]
    left_min_dist = closest_pair_util(points[:mid])
    right_min_dist = closest_pair_util(points[mid:])
    min_dist = min(left_min_dist, right_min_dist)
    strip = [point for point in points if abs(point[0] - mid_point[0]) < min_dist]
    strip.sort(key=lambda x: x[1])
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(points))  # Output: 1.4142135623730951

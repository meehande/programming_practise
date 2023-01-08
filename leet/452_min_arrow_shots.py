from typing import List

def overlap(diameter1, diameter2):
    # return true if diameter2 is overlaps diameter 1
    return (diameter2[0] >= diameter1[0]) and (diameter2[0] <= diameter1[1])


def find_min_arrow_shots(points: List[List[int]]) -> int:
    # [[10,16],[2,8],[1,6],[7,12]]
    if not points:
        return 0
    points.sort()
    """
    sort the input
    keep reference to current intersect = the range to pass through if overlaps with previous point(s)
    for each point:
        if point intersects with current_intersect, 
            update the intersect to the min range (update the first point on it)
        else:
            add to counter, set intersect = this point
    
    
    """
    
    intersect = points[0]
    arrow_count = 1
    for point in points:
        if overlap(intersect, point):
            intersect = [max(intersect[0], point[0]), min(intersect[1], point[1])]
        else:
            arrow_count += 1
            intersect = point
    return arrow_count




find_min_arrow_shots([[10,16],[2,8],[1,6],[7,12]]) == 2
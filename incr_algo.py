#incremental algorithm : O(n log n).
import utils 
import time

#new_point: [x0,y0]
#hull: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
#returns left turn hull taking into consideration the new point
def left_turn_hull(hull, new_point):
        while len(hull) > 1 and utils.orientation(hull[-2], hull[-1], new_point) != 1:
            hull.pop()
        if not len(hull) or hull[-1] != new_point:
            hull.append(new_point)
        return hull

#points: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
#returns convex hull and computing time
#using incremental algorithm 
def incremental_algo(points):
    if len(points) < 3:
         return [], 0
    start = time.time()
    points = sorted(points)
    l = [points[0], points[1]]
    for i in range(2,len(points)):
        l = left_turn_hull(l, points[i])
    u = [points[-1], points[-2]]
    for i in range(len(points)-1, -1, -1):
        u = left_turn_hull(u, points[i])

    u.pop(0)
    u.pop(len(u)-1)
    l.extend(u)
    end = time.time()
    return l, end-start
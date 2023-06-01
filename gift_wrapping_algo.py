#Gift wraping algorithm : O(n^2)
import utils
import numpy as np
import time

#points: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
#finds the most left and down point 
#returns this points and its index
def left_down_most_point(points):
  first_point_idx = 0
  first_point = points[0]
  for i in range(1, len(points)):
    if points[i][0] < first_point[0] or (points[i][0] == first_point[0] and points[i][1] < first_point[1]):
      first_point = points[i]
      first_point_idx = i
  return first_point_idx, first_point

#points: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
##returns convex hull and computing time
#using gift wraping algorithm
def gift_wraping_algo(points):
    if len(points) < 3:
       return [], 0
    start = time.time()
    start_point_idx, r =  left_down_most_point(points)
    r_idx = start_point_idx
    ch=[r]
    while (True):
        t_idx = (r_idx + 1) % len(points)
        for u_idx in range(len(points)):
            if u_idx == r_idx:
                continue
            d = utils.orientation(points[r_idx], points[u_idx], points[t_idx])
            if d == utils.TURN_LEFT or (d == utils.TURN_NONE and np.linalg.norm(np.array(points[u_idx]) - np.array(points[r_idx])) > np.linalg.norm(np.array(points[t_idx]) - np.array(points[r_idx]))):
                t_idx = u_idx
        r_idx = t_idx
        if r_idx == start_point_idx:
            break
        ch.append(points[t_idx])

    end = time.time()
    return ch, end-start



#Gift wraping algorithm : O(n^2)
import utils
import numpy as np

def left_down_most_point(points):
  first_point_idx = 0
  first_point = points[0]
  for i in range(1, len(points)-1):
    if points[i][0] < first_point[0] or (points[i][0] == first_point[0] and points[i][1] < first_point[1]):
      first_point = points[i]
      first_point_idx = i
  return first_point_idx, first_point

def gift_wraping_algo(points):
    start_point_idx, r =  left_down_most_point(points)
    r_idx = start_point_idx
    ch=[r]
    while (True):
        t_idx = (r_idx + 1) % len(points)
        for u_idx in range(len(points)):
            if u_idx == r_idx:
                continue
            d = utils.orientation(points[r_idx], points[u_idx], points[t_idx])
            if d == 1 or (d == 0 and np.linalg.norm(np.array(points[u_idx]) - np.array(points[r_idx])) > np.linalg.norm(np.array(points[t_idx]) - np.array(points[r_idx]))):
                t_idx = u_idx
        r_idx = t_idx
        if r_idx == start_point_idx:
            break
        ch.append(points[t_idx])

    return ch

def plot_convex_hull(points, ch, full_close = False):
    utils.plot_points_ch(points, ch, full_close)



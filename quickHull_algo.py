import numpy as np
from scipy.spatial import ConvexHull
import time

#points: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
#returns convex hull and computing time
#using quickHull algorithm 
def quickHull_algo(points):
    if len(points) < 3:
      return [], 0
    points = np.array(points)
    start = time.time()
    ch = ConvexHull(points)
    end = time.time()
    return q_ch_to_list(ch, points), end-start

#points: numpy array
#ch: convex hull of 2d points returned by scipy ConvexHull
#returns the convex hull in list
def q_ch_to_list(ch, points):
  ch_list = []
  for x, y in zip(points[ch.vertices,0], points[ch.vertices,1]):
    ch_list.append([x,y])
  return ch_list
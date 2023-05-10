import numpy as np
from scipy.spatial import ConvexHull
import utils 

#points: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
def quickHull_algo(points):
    points = np.array(points)
    ch = ConvexHull(points)
    return q_ch_to_list(ch, points)

#points: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
#ch: convex hull of 3d points returned by scipy
# def plot_convex_hull(points, ch):
#     #ch = q_ch_to_list(ch, points)
#     #points = points.tolist()
#     utils.plot_polygon_ch(points, ch)

#points: numpy array
#ch: convex hull of 3d points returned by scipy
def q_ch_to_list(ch, points):
  ch_list = []
  for x, y in zip(points[ch.vertices,0], points[ch.vertices,1]):
    ch_list.append([x,y])
  return ch_list
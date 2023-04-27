import numpy as np
from scipy.spatial import ConvexHull
import utils 

def quickHull_algo(points):
    np_points = np.array(points)
    ch = ConvexHull(np_points)
    return ch

def plot_points_q_ch(np_points, ch):
    ch = utils.q_ch_to_list(ch, np_points)
    points = np_points.tolist()
    utils.plot_polygon_ch(points, ch)

def q_ch_to_list(ch, np_points):
  ch_list = []
  for x, y in zip(np_points[ch.vertices,0], np_points[ch.vertices,1]):
    ch_list.append([x,y])
  return ch_list
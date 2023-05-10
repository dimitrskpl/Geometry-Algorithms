import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

#points: list of the form [[x0,y0],[x1,y1],...,[xn,yn]]
def ch_3d_algo(points):
    points = np.array(points)
    return ConvexHull(points)
    
#points: numpy array
#ch: convex hull of 3d points returned by scipy
def plot_convex_hull(ch, points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    for p in points:
        ax.scatter3D(p[0], p[1], p[2], color = "blue")
    for s in ch.simplices:
        s = np.append(s, s[0]) 
        ax.plot(points[s, 0], points[s, 1], points[s, 2], "r-")
        ax.scatter3D(points[s, 0], points[s, 1], points[s, 2], color="red")

    for i in ["x", "y", "z"]:
        eval("ax.set_{:s}label('{:s}')".format(i, i))

    plt.show()
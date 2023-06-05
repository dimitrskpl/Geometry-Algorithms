import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

#returns and plots the voronoi diagram
#and delaunay triangulation of points
#points: numpy array
def voronoi_delaunay(points):
    tri = Delaunay(points)
    vor = Voronoi(points)
    print(vor.vertices)
    #subplot voronoi, delaunay
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    ax1.set_title('Voronoi Diagram')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    voronoi_plot_2d(vor, ax=ax1, line_colors='darkorange')

    ax2.set_title('Delaunay Triangulation')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.triplot(points[:, 0], points[:, 1], tri.simplices, color='r')
    ax2.plot(points[:, 0], points[:, 1], 'o', color='g')

    plt.tight_layout()

    #single plot voronoi, delaunay
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_title('Voronoi Diagram - Delaunay Triangulation')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    voronoi_plot_2d(vor, ax=ax, line_colors='darkorange')

    ax.triplot(points[:, 0], points[:, 1], tri.simplices, color='r')
    ax.plot(points[:, 0], points[:, 1], 'o', color='g')

    plt.tight_layout()
    plt.show()
    
    return vor.vertices, points[tri.simplices]

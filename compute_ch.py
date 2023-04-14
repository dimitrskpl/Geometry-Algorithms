from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
# from scipy.spatial import ConvexHull, convex_hull_plot_2d
# import numpy as np

def read_points(file_name):
    f = open(file_name, "r")
    f.readline() 
    f.readline()

    points = []
    for line in f:
        fields = line.split()
        x = int(fields[1])
        y = int(fields[2])
        p = Point(x,y)
        points.append(p)

    return points
    f.close()

def plot_polygon(poly):
    x,y = poly.exterior.xy
    plt.plot(x,y)
    plt.show()

def print_points(points, msg=''):
    if msg:
        print(msg)
    for p in points:
        print(p)
    print()

def incremental_algo(points):
    ch = points[-3:]

    print_points(ch, 'Convex Hull:')

    n = len(points)

    for i in range(n-4, -1, -1):
        p = points[i]
        print(f'p: {p}')
        p_prev=points[i+1]
        print(f'p_prev: {p_prev}')

def main():
    points = read_points('../data/images/euro-night-0000010.instance')
    points = sorted(points, key=lambda p: p.x)
    print_points(points, 'Points:')
    incremental_algo(points)


    # points = np.array(points)
    # print(points)
    # hull = ConvexHull(points)
    
    # plt.plot(points[:,0], points[:,1], 'o')
    # for simplex in hull.simplices:
    #     plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    # plt.show()

    #plot_polygon(poly)

if __name__ == "__main__":
    main()


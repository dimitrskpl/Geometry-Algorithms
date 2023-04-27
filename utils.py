import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import numpy as np
import quickHull_algo
from scipy.spatial import ConvexHull

#code from https://www.geeksforgeeks.org/check-if-given-polygon-is-a-convex-polygon-or-not/
############################################################

def CrossProduct(A):
     
    # Stores coefficient of X
    # direction of vector A[1]A[0]
    X1 = (A[1][0] - A[0][0])
 
    # Stores coefficient of Y
    # direction of vector A[1]A[0]
    Y1 = (A[1][1] - A[0][1])
 
    # Stores coefficient of X
    # direction of vector A[2]A[0]
    X2 = (A[2][0] - A[0][0])
 
    # Stores coefficient of Y
    # direction of vector A[2]A[0]
    Y2 = (A[2][1] - A[0][1])
 
    # Return cross product
    return (X1 * Y2 - Y1 * X2)
 
# Function to check if the polygon is
# convex polygon or not
def isConvex(points):
     
    # Stores count of
    # edges in polygon
    N = len(points)
 
    # Stores direction of cross product
    # of previous traversed edges
    prev = 0
 
    # Stores direction of cross product
    # of current traversed edges
    curr = 0
 
    # Traverse the array
    for i in range(N):
         
        # Stores three adjacent edges
        # of the polygon
        temp = [points[i], points[(i + 1) % N],
                           points[(i + 2) % N]]
 
        # Update curr
        curr = CrossProduct(temp)
 
        # If curr is not equal to 0
        if (curr != 0):
             
            # If direction of cross product of
            # all adjacent edges are not same
            if (curr * prev < 0):
                return False
            else:
                 
                # Update curr
                prev = curr
 
    return True

############################################################

def read_points(file_name):
    f = open(file_name, "r")
    f.readline() 
    f.readline()

    points = []
    for line in f:
        fields = line.split()
        x = float(fields[1])
        y = float(fields[2])
        points.append([x,y])

    return points
    f.close()

#plot functions
############################################################

def plot_poly(points):
    xx,yy = get_coords(points)
    plt.plot(xx,yy, 'b')
    plt.scatter(xx,yy)
    plt.show()


#plots points as points and the convex hull ch
#as polygon
#points, ch: coordinates of the form [[x0,y0],...,[xn,yn]]
#full_close: True to show figure in full screen
# and close after pause for 1 second
def plot_points_ch(points, ch, full_close = False):
    xx1, yy1 = get_coords(points)
    xx2, yy2 = get_coords(ch)

    plt.plot(xx2, yy2, 'r')
    plt.scatter(xx1,yy1, color='b')    

    if full_close:
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    else:
        plt.show()

############################################################

#geometry functions
############################################################
def cmp(a, b):
        return (a > b) - (a < b)

#returns
# 1 for left turn 
#-1 for right turn
# 0 for collinear
def orientation(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

#points: coordinates of the form [[x0,y0],...,[xn,yn]]
#returns 2 lists containing all x and all y
#y coordinates correspondingly
def get_coords(points):
  xx = []
  yy = []
  for p in points:
    xx.append(p[0])
    yy.append(p[1])
  xx.append(points[0][0])
  yy.append(points[0][1])
  return xx ,yy

def first_same_idx(poly1, poly2):
  for i in range(len(poly2)):
    if poly2[i] == poly1[0]:
      return i
  return -1

#start the check based on poly1
def same_polygons(poly1, poly2):
  if len(poly1) != len(poly2):
    return False
  poly2_offset = first_same_idx(poly1, poly2)
  if poly2_offset == -1:
    return False
  for i in range(len(poly1)):
    poly2_idx = (i+poly2_offset) % len(poly2)
    if poly1[i] != poly2[poly2_idx]:
      return False

  return True

def test(path, ch_algo, plot=False):
  print(path)
  dir_list = os.listdir(path)
  for file in dir_list:
    if file[0] == '.':
      dir_list.remove(file)
  for i in tqdm (range (len(dir_list)),desc="Loading…",ascii=False, ncols=75):  
    file = dir_list[i]
    file = path + file
    points = read_points(file)
    ch = ch_algo(points)
    if plot:
      plot_points_ch(points, ch, True)
    
    np_points = np.array(points)
    correct_ch = ConvexHull(np_points)
    correct_ch_list = quickHull_algo.q_ch_to_list(correct_ch, np_points)
    if not same_polygons(ch, correct_ch_list):
      print(f'Failed in file {file}')
      return
    
  print('Success')

def test2(path,plot=False):
  dir_list = os.listdir(path)
  for file in dir_list:
    if file[0] == '.':
      dir_list.remove(file)
  for i in tqdm (range (len(dir_list)),desc="Loading…",ascii=False, ncols=75):  
    file = dir_list[i]
    file = path + file

    points = read_points(file)
    np_points = np.array(points)
    ch = quickHull_algo.quickHull_algo(np_points)
    ch = quickHull_algo.q_ch_to_list(ch, np_points)
    
    if not isConvex(ch):
      print(f'Failed in file {file}')
      return
    if plot:
       plot_points_ch(points, ch, True)
    
  print('Success')



############################################################
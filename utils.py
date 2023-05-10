import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import numpy as np
import quickHull_algo

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
#plots points as points and the convex hull ch
#as polygon
#points, ch: coordinates of the form [[x0,y0],...,[xn,yn]]
#full_close: True to show figure in full screen
# and close after pause for 1 second
def plot_points_ch(points, ch, full_close = False):
    xxp, yyp = get_coords(points)
    xxc, yyc = get_coords(ch)

    plt.plot(xxc, yyc, 'r')
    plt.scatter(xxp,yyp, color='b')    
    plt.scatter(xxc,yyc, color='r')    
    
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
TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)


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

def correct_ch(points, ch):
  correct_ch = quickHull_algo.quickHull_algo(points)
  #correct_ch = quickHull_algo.q_ch_to_list(correct_ch, np.array(points))
  return same_polygons(ch, correct_ch)

def test(path, ch_algo, plot=False):
  print(path)
  dir_list = os.listdir(path)
  for file in dir_list:
    if file[0] == '.':
      dir_list.remove(file)
  succ = True
  for i in tqdm (range (len(dir_list)),desc="Loading…",ascii=False, ncols=75):  
    file = dir_list[i]
    file = path + file
    #print(f'File: {file}')
    points = read_points(file)
    ch = ch_algo(points)
    if plot:
      plot_points_ch(points, ch, False)
    
    if not correct_ch(points, ch):
      print(f'Failed in file {file}')
      succ = False
      break
    
  if succ:
    print('Success')
  else:
    print('Failed')


def test_rand_psets(points_sets, ch_algo, plot=False):
  #for i in tqdm(range(len(points_sets)),desc="Loading…",ascii=False, ncols=75):  
  for i in range(len(points_sets)):
    points = points_sets[i]
    #print(points)
    ch = ch_algo(points)#,plot=True, full_close=False)

    if plot:
      plot_points_ch(points, ch, False)
    
    if not correct_ch(points, ch):
      cor_ch = quickHull_algo.quickHull_algo(np.array(points))
      cor_ch = quickHull_algo.q_ch_to_list(cor_ch, np.array(points))
      print(f'Real sz: {len(cor_ch)}, computed sz: {len(ch)}')
      print(f'Failed for point set sz: {len(points)}')
      print(ch)
      print(cor_ch)
      #print(points)
      plot_points_ch(points, ch)
      


      break
  print('Success')
############################################################
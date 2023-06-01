import random

#Returns size random collinear 2D points in range [min,max]
#if collinear_ratio > 0 then this ratio of size points will 
#be collinear. If dix_x_coords=True then all points will
#have different x coordinate. If cannot generate size points 
#based on min, max and parameters returns [] 
def gen_2D_points(min=0, max=1000, size=10, dif_x_coords = False, collinear_ratio=0):
    points = []
    if collinear_ratio == 0:
      total_range = max-min+1
      total_pos_comb = total_range ** 2
      if dif_x_coords:
          total_pos_comb = total_range
      if size > total_pos_comb:
          return []

      x_coords = []
      while len(points) < size:
          x = random.randint(min, max)
          y = random.randint(min, max)
          p = [x,y]
          if p not in points:
              if not dif_x_coords:
                  points.append(p)
              elif dif_x_coords and p[0] not in x_coords:
                  x_coords.append(p[0])
                  points.append(p)
    else:
      points = gen_2D_coll_points(min, max, size, collinear_ratio)

    return points 

#Returns size random collinear 2D points in range [min,max]
#The collinear points will either have same x coord, or same 
#y coord or be of the form (x,x)
#If cannot generate size points based on min, max returns [] 
def gen_only_collinear(min=0,max=1000,size=10):
  if max-min+1 < size:
    return []
  
  coll_type = random.randint(0,2)
  points = []

  if coll_type == 0: 
    while len(points) < size:
        x = random.randint(min, max)
        p = [x,x]
        if p not in points:
          points.append(p)
  else:
    a = random.randint(min, max)
    while len(points) < size:
      b = random.randint(min, max)
      if coll_type == 1: #same x coords
        p = [a, b]
      else: #same y coords
        p = [b, a]
      if p not in points:
        points.append(p)
        
  return points

#Returns size random 2D points in range [min,max] with 
#the collinear_ratio of size being collinear. 
#If cannot generate size points based on min, max returns [] 
def gen_2D_coll_points(min=0, max=1000, size=10, collinear_ratio=0.5):
  coll_size = collinear_ratio*size
  points = gen_only_collinear(min, max, coll_size)
  total_range = max-min+1
  pos_points = total_range ** 2 - coll_size
  if points == [] or pos_points < size-coll_size:
    return []

  while len(points) < size:
      x = random.randint(min,max)
      y = random.randint(min,max)
      p = [x,y]
      if p not in points:
        points.append([x, y])
  return points

#Returns random size 3D points with x,y,z coordinates 
#in range min,max. If cannot generate size points
#based on min, max returns [] 
def gen_3D_points(min=0, max=100, size=10):
    total_range = max-min+1
    total_pos_comb = total_range ** 3
    if size > total_pos_comb:
        return []
    
    points = []
    while len(points) < size:
        x = random.randint(min, max)
        y = random.randint(min, max)
        z = random.randint(min, max)
        p = [x,y,z]
        if p not in points:
            points.append(p)
    return points

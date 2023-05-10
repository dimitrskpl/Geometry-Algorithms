import random

def gen_2D_points(min=0, max=100, dif_x_coords = False, size=10):
    total_range = max-min+1
    total_pos_comb = total_range ** 2
    if dif_x_coords:
        total_pos_comb = total_range
    if size > total_pos_comb:
        return []
    


    points = []
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

    return points 

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

# def gen_2D_points(min, max, size=10):
    
#     points = []
#     x_coords = []
#     while len(points) < size:
#         x = random.randint(min, max)
#         y = random.randint(min, max)
#         p = [x,y]
#         if p not in points and p[0] not in x_coords:
#             x_coords.append(p[0])
#             points.append(p)
#     return points 
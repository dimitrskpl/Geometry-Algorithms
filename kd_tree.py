import math
import matplotlib.pyplot as plt


class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None


def newNode(point):
    return Node(point)


k=2 #KD for 2 dimensions
class KD_Tree:
    def __init__(self, points):
        self.points = points
        self.tree = None
    
    def construct_rec(self, points, depth):
        cd = depth % k 
        if len(points) == 0:
            return None
        if len(points) == 1:
            return newNode(points[0])
            
        points = sorted(points, key=lambda point: point[cd])
        if len(points) % 2 == 0:
            med_idx = int(len(points)/2) - 1
        else:
            med_idx = math.floor((len(points)/2))

        #l = points[med_idx][cd]

        node = newNode(points[med_idx])
        node.left = self.construct_rec(points[0:med_idx], depth+1)
        node.right = self.construct_rec(points[med_idx+1:], depth+1)
        return node
    
    def construct(self, points):
        self.tree = self.construct_rec(self.points, depth=0)

    def print2DUtil(self, root, space):
        if (root == None):
            return
        space += 10  
        self.print2DUtil(root.right, space)
    
        print()
        for i in range(10, space):
            print(end=" ")
        print(root.point)
        self.print2DUtil(root.left, space)

    #prints the kd tree
    def print2D(self):
        self.print2DUtil(self.tree, 0)


    #returns true if p lies in the box 
    #with corners (xx[0], yy[0]), (xx[1], yy[1]). 
    def in_box(self, p, box):
        p_x = p[0]
        p_y = p[1]
        return (p_x <= box[1][0] and p_x >= box[0][0] and p_y <= box[1][1] and p_y >= box[0][1])


    def search_box_rec(self, root, box, depth):
        if root is None:
            return []

        res = []
        if self.in_box(root.point, box):
            res = [root.point]
        
        cd = depth % k 

        res1 = []
        res2 = []

        if root.point[cd] >= box[0][cd]:
            res1 = self.search_box_rec(root.left, box, depth + 1)
        if root.point[cd] <= box[1][cd]:
            res2 = self.search_box_rec(root.right, box, depth + 1)

        return res+res1+res2 
    
    #returns the points that lie in the box
    def search_box(self, box):
        return self.search_box_rec(self.tree, box, 0)
    

    def plot_points_and_box(self, box, points_in_box):
        x_initial = [point[0] for point in self.points]
        y_initial = [point[1] for point in self.points]
        
        x_in_box = [point[0] for point in points_in_box]
        y_in_box = [point[1] for point in points_in_box]
        
        plt.scatter(x_initial, y_initial, color='blue')        
        plt.scatter(x_in_box, y_in_box, color='red')
        
        x_min, y_min = box[0]
        x_max, y_max = box[1]
        plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min],
                 color='green')

        plt.title('Points in Bounding Box')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.show()



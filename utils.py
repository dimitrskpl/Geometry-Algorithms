import matplotlib.pyplot as plt

#plot functions
############################################################
#plots points as points and the convex hull ch
#as polygon
#points, ch: coordinates of the form [[x0,y0],...,[xn,yn]]
#full_close: True to show figure in full screen
# and close after pause for 1 second
def plot_points_ch(points, ch, title = '', full_close = False):
    xxp, yyp = get_coords(points)
    xxc, yyc = get_coords(ch)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
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

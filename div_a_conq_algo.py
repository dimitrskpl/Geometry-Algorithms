import incr_algo
import utils 
import matplotlib.pyplot as plt
import time

def left_most_point(points):
  left_most_p_idx = 0
  left_most_p = points[0]
  for i in range(1, len(points)-1):
    if points[i][0] < left_most_p[0]:
      left_most_p = points[i]
      left_most_p_idx = i
  return left_most_p_idx 

def right_most_point(points):
  right_p_idx = 0
  right_p = points[0]
  for i in range(1, len(points)-1):
    if points[i][0] > right_p[0]:
      right_p = points[i]
      right_p_idx = i
  return right_p_idx

def prev_point_idx(idx, sz):
    return (sz-1 if idx == 0 else idx - 1)

def nxt_point_idx(idx, sz):
   return (idx + 1) % sz

def line_crosses_poly(p, q, ch, turn):
    for r in ch:
       if r == q:
          continue
       orient = utils.orientation(p,q,r)
       if orient != turn and orient != utils.TURN_NONE:
          return True
    return False


#l_ch, r_ch: two polygons having points in CCW
#all points of l_ch have smaller x coordinates than r_ch
#l_ch_r_p_idx: the right most point of l_ch
#r_ch_l_p_idx: the left most point of right ch
#returns indexes corresponding to l_ch, r_ch
#forming the upper tangent
def upper_tangent(l_ch, r_ch, l_ch_r_p_idx, r_ch_l_p_idx, plot=False, full_close=False):
    l_ch_up_tan_idx = l_ch_r_p_idx
    r_ch_up_tan_idx = r_ch_l_p_idx
    l_ch_up_tan_p = l_ch[l_ch_up_tan_idx] 
    r_ch_up_tan_p = r_ch[r_ch_up_tan_idx]
    if plot:
        plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_up_tan_p, r_ch_up_tan_p]], title='Candidate upper tangent', full_close=full_close)
    
    while (True):
        no_changes = True
        while(line_crosses_poly(l_ch_up_tan_p, r_ch_up_tan_p, r_ch, utils.TURN_RIGHT)):
            #The point on r_ch moves up
            no_changes = False
            r_ch_up_tan_idx = prev_point_idx(r_ch_up_tan_idx, len(r_ch)) #L <- L' : the point on b moves up.
            r_ch_up_tan_p = r_ch[r_ch_up_tan_idx]
            if plot:
                plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_up_tan_p, r_ch_up_tan_p]], title='Candidate upper tangent', full_close=full_close)

        while(line_crosses_poly(r_ch_up_tan_p, l_ch_up_tan_p, l_ch, utils.TURN_LEFT)):
            #The point on l_ch moves up.
            no_changes = False
            l_ch_up_tan_idx = nxt_point_idx(l_ch_up_tan_idx, len(l_ch)) #L <- L' : the point on b moves up.
            l_ch_up_tan_p = l_ch[l_ch_up_tan_idx]
            if plot:
                plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_up_tan_p, r_ch_up_tan_p]], title='Candidate upper tangent', full_close=full_close)
        
        if no_changes:
            l_nxt_idx = nxt_point_idx(l_ch_up_tan_idx, len(l_ch))
            l_nxt = l_ch[l_nxt_idx]
            r_prev_idx = prev_point_idx(r_ch_up_tan_idx, len(r_ch))
            r_prev = r_ch[r_prev_idx]
            collinear = False

            if utils.orientation(r_prev, r_ch_up_tan_p, l_ch_up_tan_p) == utils.TURN_NONE:
               collinear = True
               r_ch_up_tan_idx = r_prev_idx
               r_ch_up_tan_p = r_prev
               if plot:
                   plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_up_tan_p, r_ch_up_tan_p]], title='Candidate upper tangent', full_close=full_close)
            if utils.orientation(r_ch_up_tan_p, l_ch_up_tan_p, l_nxt) == utils.TURN_NONE:
               collinear = True
               l_ch_up_tan_idx = l_nxt_idx
               l_ch_up_tan_p = l_nxt
               if plot:
                   plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_up_tan_p, r_ch_up_tan_p]], title='Candidate upper tangent', full_close=full_close)

            if plot:
                plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_up_tan_p, r_ch_up_tan_p]], title='Final upper tangent', full_close=full_close)
            return l_ch_up_tan_idx, r_ch_up_tan_idx


#l_ch, r_ch: two polygons having points in CCW
#all points of l_ch have smaller x coordinates than r_ch
#l_ch_r_p_idx: the right most point of l_ch
#r_ch_l_p_idx: the left most point of right ch
#returns indexes corresponding to l_ch, r_ch
#forming the lower tangent
def lower_tangent(l_ch, r_ch, l_ch_r_p_idx, r_ch_l_p_idx, plot=False, full_close=False):
    l_ch_low_tan_idx = l_ch_r_p_idx
    r_ch_low_tan_idx = r_ch_l_p_idx
    l_ch_low_tan_p = l_ch[l_ch_low_tan_idx] 
    r_ch_low_tan_p = r_ch[r_ch_low_tan_idx]
    if plot:
        plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_low_tan_p, r_ch_low_tan_p]], title='Candidate lower tangent', full_close=full_close)
    
    while (True):
        no_changes = True
        while(line_crosses_poly(l_ch_low_tan_p, r_ch_low_tan_p, r_ch, utils.TURN_LEFT)):
            #The point on r_ch moves down
            no_changes = False
            r_ch_low_tan_idx = nxt_point_idx(r_ch_low_tan_idx, len(r_ch)) #L <- L' : the point on b moves up.
            r_ch_low_tan_p = r_ch[r_ch_low_tan_idx]
            if plot:
                plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_low_tan_p, r_ch_low_tan_p]], title='Candidate lower tangent', full_close=full_close)

        while(line_crosses_poly(r_ch_low_tan_p, l_ch_low_tan_p, l_ch, utils.TURN_RIGHT)):
            #The point on l_ch moves down
            no_changes = False
            l_ch_low_tan_idx = prev_point_idx(l_ch_low_tan_idx, len(l_ch)) #L <- L' : the point on b moves up.
            l_ch_low_tan_p = l_ch[l_ch_low_tan_idx]
            if plot:
                plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_low_tan_p, r_ch_low_tan_p]], title='Candidate lower tangent', full_close=full_close)
        
        if no_changes:
            l_prev_idx = prev_point_idx(l_ch_low_tan_idx, len(l_ch))
            l_prev = l_ch[l_prev_idx]
            r_nxt_idx = nxt_point_idx(r_ch_low_tan_idx, len(r_ch))
            r_nxt = r_ch[r_nxt_idx]
            collinear = False

            if utils.orientation(r_nxt, r_ch_low_tan_p, l_ch_low_tan_p) == utils.TURN_NONE:
                collinear = True
                r_ch_low_tan_idx = r_nxt_idx
                r_ch_low_tan_p = r_nxt
                if plot:
                    plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_low_tan_p, r_ch_low_tan_p]], title='Candidate lower tangent', full_close=full_close)
            if utils.orientation(r_ch_low_tan_p, l_ch_low_tan_p, l_prev) == utils.TURN_NONE:
                collinear = True
                l_ch_low_tan_idx = l_prev_idx
                l_ch_low_tan_p = l_prev
                if plot:
                    plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_low_tan_p, r_ch_low_tan_p]], title='Candidate lower tangent', full_close=full_close)

            if plot:
               plot_ch_lines(l_ch=l_ch, r_ch=r_ch, lines=[[l_ch_low_tan_p, r_ch_low_tan_p]], title='Final lower tangent', full_close=full_close)
               
            return l_ch_low_tan_idx, r_ch_low_tan_idx

def same_x_coord(points):
    x_coords = set()
    for p in points:
        x = p[0]  
        if x in x_coords:
            return True
        x_coords.add(x)
    
    return False

def merge(left_ch, right_ch, plot=False, full_close=False):
    merged_ch = []
    # if same_x_coord(left_ch+right_ch):
    #     l_ch_min_y = min(left_ch, key=lambda p:p[1])
    #     l_ch_r_p_idx = left_ch.index(l_ch_min_y)
    #     r_ch_min_y = max(right_ch, key=lambda p:p[1])
    #     r_ch_l_p_idx = right_ch.index(r_ch_min_y)
    #     merged_ch = [left_ch[l_ch_r_p_idx], right_ch[r_ch_l_p_idx]]
    # else:
    l_ch_r_p_idx  = right_most_point(left_ch)
    r_ch_l_p_idx = left_most_point(right_ch)
    l_ch_up_tan_idx, r_ch_up_tan_idx = upper_tangent(left_ch, right_ch, l_ch_r_p_idx, r_ch_l_p_idx, plot, full_close)
    l_ch_low_tan_idx, r_ch_low_tan_idx = lower_tangent(left_ch, right_ch, l_ch_r_p_idx, r_ch_l_p_idx, plot, full_close)

    if plot:
        up_line = [left_ch[l_ch_up_tan_idx], right_ch[r_ch_up_tan_idx]]
        low_line = [left_ch[l_ch_low_tan_idx], right_ch[r_ch_low_tan_idx]]
        plot_ch_lines(l_ch=left_ch, r_ch=right_ch, lines=[up_line, low_line], title='Final Tangents', full_close=full_close)

    idx = l_ch_up_tan_idx
    while True:
        merged_ch.append(left_ch[idx])
        if idx == l_ch_low_tan_idx:
            break
        idx = nxt_point_idx(idx, len(left_ch))

    idx = r_ch_low_tan_idx
    while True:
        merged_ch.append(right_ch[idx])
        if idx == r_ch_up_tan_idx:
            break
        idx = nxt_point_idx(idx, len(right_ch))
    
    return merged_ch 

def div_and_qonquer_algo(points, plot=False, full_close=False):
    start = time.time()

    if len(points) < 3 or same_x_coord(points):
        return [], 0
    
    points = sorted(points) 
    ch = compute_ch(points, plot, full_close)
    end = time.time()
    if plot:
        utils.plot_points_ch(points=points, ch=ch, title='Divide & Conquer Convex Hull')
    return ch, end-start


def compute_ch(points, plot=False, full_close=False):
    if len(points) <= 5:
        ch, _= incr_algo.incremental_algo(points)
        if plot:
            utils.plot_points_ch(points=points, ch=ch, title='Base case', full_close=full_close)
        return ch
    
    mid = int(len(points)/2)
    left_points = points[0:mid]
    right_points = points[mid:]
 
    if plot:
        plot_divided_point_sets(left_points=left_points, right_points=right_points, title='Dataset Division', full_close=full_close)
    
    left_ch = compute_ch(left_points, plot, full_close)
    right_ch = compute_ch(right_points, plot, full_close)

    if plot:
        plot_ch_points(left_points=left_points, right_points=right_points, left_ch=left_ch, right_ch=right_ch, title='Divided Convex Hulls', full_close=full_close)
    ch = merge(left_ch, right_ch, plot, full_close)
    if plot:
        utils.plot_points_ch(points=points, ch=ch, title='Merged Convex Hull', full_close=full_close)
    return ch

def plot_ch_points(left_points, right_points, left_ch, right_ch, title='', full_close=False):#points=None):
    xlp, ylp = utils.get_coords(left_points)
    xlc, ylc = utils.get_coords(left_ch)
    xrp, yrp = utils.get_coords(right_points)
    xrc, yrc = utils.get_coords(right_ch)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.scatter(xlp, ylp, color='b')
    plt.scatter(xrp, yrp, color='b')

    plt.plot(xlc, ylc, 'r')
    plt.scatter(xlc,ylc, color='r')    
    plt.plot(xrc, yrc, 'r')
    plt.scatter(xrc,yrc, color='r')    
    if full_close:
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    else:
        plt.show()

def plot_ch_lines(l_ch, r_ch, lines, title='', full_close= False):
    xlc, ylc = utils.get_coords(l_ch)
    xrc, yrc = utils.get_coords(r_ch)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.plot(xlc, ylc, 'r')
    plt.scatter(xlc, ylc, color= 'r')
    plt.plot(xrc, yrc, 'r')
    plt.scatter(xrc, yrc, color='r')
    for line in lines:
        xxp, yyp = utils.get_coords(line)
        plt.plot(xxp,yyp, 'black')

    if full_close:
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    else:
        plt.show()

def min_max_y(points):
    min_y = points[0][1]
    max_y = points[0][1]
    for i in range(1,len(points)):
        p_y = points[i][1]
        if p_y < min_y:
            min_y = p_y
        if p_y > max_y:
            max_y = p_y
    return min_y, max_y

def plot_divided_point_sets(left_points, right_points, title='', full_close=False):
    xxl, yyl = utils.get_coords(left_points)
    xxr, yyr = utils.get_coords(right_points)
    plt.scatter(xxl,yyl, color='g')
    plt.scatter(xxr, yyr, color='r')
    min_y, max_y = min_max_y(left_points+right_points)
    mid_x = int((xxl[-2]+xxr[0])/2)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.plot([mid_x, mid_x],[min_y, max_y],color='b', linestyle='dashed')
    if full_close:
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()
        plt.show(block=False)
        plt.pause(1)
        plt.close()
    else:
        plt.show()

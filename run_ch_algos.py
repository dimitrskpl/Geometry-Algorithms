import incr_algo
import utils
import gift_wrapping_algo
import quickHull_algo
import div_a_conq_algo
import ch_3d_algo
import points_generator
from tabulate import tabulate

# Finds convex hulls using ch_algo for all point set
# in psets and. Returns the convex hulls and the
# execution time for each of them as 2 lists. 
def ch_multi_psets(ch_algo, p_sets):
    chs = []
    times = []
    for points in p_sets:
        ch, time = ch_algo(points)
        if ch == []:
            time = '-'
        else:
            time = "{:.5f}".format(time)

        chs.append(ch)
        times.append(time)
    return chs, times

# Finds convex hull for each algorihm and for each points set
# in p_sets. Displays the time for each combination as table
def ch_times_table(p_sets):
    _, incr_times = ch_multi_psets(incr_algo.incremental_algo, p_sets)
    _, javis_times = ch_multi_psets(gift_wrapping_algo.gift_wraping_algo, p_sets)
    _, div_conq_times = ch_multi_psets(div_a_conq_algo.div_and_conquer_algo, p_sets)
    _, qHull_times = ch_multi_psets(quickHull_algo.quickHull_algo, p_sets)
    table = [['Incremental'] + incr_times, 
    ['Jarvis'] + javis_times, 
    ['Divide & Conquer'] + div_conq_times,
    ['QuickHull (2D)'] + qHull_times]

    p_sets_sz = []
    for p_set in p_sets:
        p_sets_sz.append(len(p_set))
    col_names  =['Total Points'] + p_sets_sz
    print(tabulate(table, headers=col_names, tablefmt='fancy_grid'))

# Convex Hull Algorithms executed for 2D random points 
# Returns one list with the convex hull and one with their
# execution times with the order: incremental, jarvis, 
# quickhull, divide and conquer. If print_ch=True,
# prints convex hulls and if plot=True plots them
def all_2D_algos_ch(points, print_ch=False, plot=False):
    ch_incr, time_incr = incr_algo.incremental_algo(points)
    time_incr = "{:.5f}".format(time_incr)
    if print_ch:
            print('Incremental convex hull:')
            print(ch_incr)
    if ch_incr == []:
        time_incr='-'
    elif plot:
         utils.plot_points_ch(points=points, ch=ch_incr, title = 'Incremental: Convex Hull')
        

    ch_jarvis, time_jarvis = gift_wrapping_algo.gift_wraping_algo(points)
    time_jarvis = "{:.5f}".format(time_jarvis)
    if print_ch:
            print('Jarvis convex hull:')
            print(ch_jarvis)
    if ch_jarvis == []:
        time_jarvis='-'
    elif plot:
         utils.plot_points_ch(points=points, ch=ch_jarvis, title = 'Jarvis: Convex Hull')

    ch_qHull, time_qHull = quickHull_algo.quickHull_algo(points)
    time_qHull = "{:.5f}".format(time_qHull)
    if print_ch:
            print('Quick Hull convex hull')
            print(ch_qHull)

    if ch_qHull == []:
        time_qHull='-'
    elif plot:
         utils.plot_points_ch(points=points, ch=ch_qHull, title = 'Quick Hull: Convex Hull')
    
    ch_div_conq, time_div_conq = div_a_conq_algo.div_and_conquer_algo(points)
    time_div_conq = "{:.5f}".format(time_div_conq)
    if print_ch:
            print('Divide & Conquer convex hull:')
            print(ch_div_conq)

    if ch_qHull == []:
        time_qHull='-'
    elif plot:
         utils.plot_points_ch(points=points, ch=ch_div_conq, title = 'Divide & Conquer: Convex Hull')

    if ch_div_conq == []:
        time_div_conq='-'

    return [ch_incr, ch_jarvis, ch_qHull, ch_div_conq], [time_incr, time_jarvis, time_qHull, time_div_conq]
  


# Shows in table the execution time for each convex hull algorithm (2D)
# for each random point set with sizes 10,100,1000,10000
# including collinear points
def ch_algos_collinear():
    p_sets_sz = [10, 100, 1000, 10000]
    p_sets_2D_collinear = []
    for sz in p_sets_sz:
        p_set_2D_collinear = points_generator.gen_2D_points(min=0, max=1000000, size=sz, collinear_ratio=0.4)
        p_sets_2D_collinear.append(p_set_2D_collinear)
        
    title = "Convex Hull Algorithms: Time/NoOfPoints - Collinear Points"
    print(" "*6 + title)
    ch_times_table(p_sets_2D_collinear)

# Convex Hull Algorithms executed for 80 2D random points 
# The results are printed and plotted
def all_algo_ch_80():
    points = points_generator.gen_2D_points(min=0, max=1000000, size=80)
    all_2D_algos_ch(points=points, print_ch=True, plot=True)

## Visualization of divide and conquer steps for 20 random poins
def div_conquer_visualize():
    points = points_generator.gen_2D_points(min=0, max=10000, size=20, dif_x_coords=True)
    ch_div_conq, _ = div_a_conq_algo.div_and_conquer_algo(points=points, plot=True, full_close=True)
    print(ch_div_conq)


# Shows in 2 tables the execution time for each convex hull algorithm (2D)
# for each random point set with sizes 10,100,1000,10000. 
# The one table corresponds to points sets with different x coords
def compare_2D_ch_algos():
    p_sets_sz = [10, 100, 1000, 10000]
    p_sets_2D = []
    p_sets_2D_dif_x = []
    for sz in p_sets_sz:
        p_set_2D = points_generator.gen_2D_points(min=0, max=1000000, size=sz)
        p_sets_2D.append(p_set_2D)
        
        p_set_2D_dif_x = points_generator.gen_2D_points(min=0, max=1000000, size=sz, dif_x_coords=True)
        p_sets_2D_dif_x.append(p_set_2D_dif_x)
        
    title = "Convex Hull Algorithms: Time/NoOfPoints"
    print(" "*8 + title)
    ch_times_table(p_sets_2D)

    print()

    title = "Convex Hull Algorithms: Time/NoOfPoints - Different X Coords"
    print(title)
    ch_times_table(p_sets_2D_dif_x)

# Computes, prints and plots convex hull for 50 random 3D points
def ch_50_3D():
    points_3D = points_generator.gen_3D_points(min=0, max=10000, size=50)
    ch_3D,_ = ch_3d_algo.ch_3d_algo(points=points_3D, plot=True)
    print(ch_3D)
import incr_algo
import utils
import gift_wrapping_algo
import quickHull_algo
import os
import div_a_conq_algo
from scipy.spatial import ConvexHull
import numpy as np
import ch_3d_algo

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import points_generator

def main():
    #path = "../data/examples2/"
    #ch_algo = quickHull_algo.quickHull_algo
    #ch_algo = incr_algo.incremental_algo
    #utils.test(path, ch_algo,False)
    #paths = ["../data/images/", "../data/uniform/"]
    # ch_algo = div_a_conq_algo.div_and_qonquer_algo

    # for path in paths:
    #     utils.test(path, ch_algo)

    # file = "../data/images/euro-night-0000020.instance"
    # points = utils.read_points(file)
    # ch = div_a_conq_algo.div_and_qonquer_algo(points, plot=True, full_close=True)
    # print(f'Is_correct: {utils.correct_ch(points, ch)}')
    
    p_sets_sz = [10, 100, 1000, 10000]#, 100000]
    p_sets_2D = []
    p_sets_2D_dif_x = []
    p_sets_3D = []
    for sz in p_sets_sz:
        p_set_2D = points_generator.gen_2D_points(min=0, max=1000, size=sz)
        p_sets_2D.append(p_set_2D)
        p_set_2D_dif_x = points_generator.gen_2D_points(min=0, max=1000, dif_x_coords=True, size=sz)
        p_sets_2D_dif_x.append(p_set_2D_dif_x)
        p_set_3D = points_generator.gen_3D_points(min=0, max=10000, size=sz)
        p_sets_3D.append(p_set_3D)

    print('Running incremental algorithm')
    utils.test_rand_psets(p_sets_2D, incr_algo.incremental_algo)

    print('Running gift wraping algorithm')
    utils.test_rand_psets(p_sets_2D, gift_wrapping_algo.gift_wraping_algo)

    print('Running quickhull algorithm')
    utils.test_rand_psets(p_sets_2D, quickHull_algo.quickHull_algo)

    print('Running divide and conquer algorithm')
    utils.test_rand_psets(p_sets_2D_dif_x, div_a_conq_algo.div_and_qonquer_algo)

    # points = points_generator.generate_2D_points(0,10, 100)
    # points = [[1, 5], [9, 5], [5, 8], [4, 7], [7, 6], [1, 7], [9, 4], [7, 1], [4, 0], [0, 3], [4, 1], [6, 8], [5, 4], [9, 8], [3, 3], [10, 6], [5, 1], [1, 9], [3, 2], [3, 10], [5, 9], [10, 3], [2, 10], [6, 5], [0, 5], [8, 1], [7, 9], [8, 7], [8, 4], [3, 1], [9, 3], [7, 8], [10, 1], [2, 6], [3, 8], [5, 7], [1, 8], [2, 2], [2, 7], [8, 6], [4, 3], [1, 3], [4, 9], [6, 3], [10, 7], [4, 5], [2, 9], [1, 1], [10, 10], [5, 6], [4, 6], [9, 10], [8, 9], [8, 10], [3, 9], [6, 1], [10, 8], [7, 10], [9, 1], [0, 6], [5, 3], [6, 0], [7, 7], [0, 8], [6, 2], [2, 8], [8, 3], [8, 5], [0, 7], [2, 1], [2, 5], [10, 2], [9, 0], [7, 4], [9, 2], [5, 10], [0, 4], [6, 6], [6, 4], [7, 0], [0, 10], [1, 10], [3, 0], [1, 6], [7, 3], [9, 9], [2, 0], [7, 2], [1, 4], [6, 9], [10, 5], [1, 2], [5, 0], [5, 2], [3, 5], [4, 10], [4, 2], [5, 5], [9, 7], [0, 0]]
    # points_sets_2D = [points]
    # utils.test_rand_psets(points_sets_2D, div_a_conq_algo.div_and_qonquer_algo)


if __name__ == "__main__":
    main()


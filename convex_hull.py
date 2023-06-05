import run_ch_algos
import numpy as np
import voronoi_delaunay
import points_generator
import kd_tree

def main():
    run_ch_algos.ch_algos_collinear()
    run_ch_algos.all_algo_ch_80()
    run_ch_algos.div_conquer_visualize()
    run_ch_algos.compare_2D_ch_algos()
    run_ch_algos.ch_50_3D()

    points = points_generator.gen_2D_points(min=1,max=100,size=50)
    points = np.array(points)
    vor, delan = voronoi_delaunay.voronoi_delaunay(points)
    print(f'Voronoi Diagram: {vor}')
    print(f'Delanunay Triangulation: {delan}')


    points = points_generator.gen_2D_points(min=1,max=1000,size=60)
    box = points_generator.box_generator(points)
    
    kd_t = kd_tree.KD_Tree(points)
    kd_t.construct(points)

    points_in_box = kd_t.search_box(box)
    print('Points in box:')
    for p in points_in_box:
        print(p)

    kd_t.plot_points_and_box(box, points_in_box)


if __name__ == "__main__":
    main()



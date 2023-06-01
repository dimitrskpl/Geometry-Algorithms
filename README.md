# Convex-Hull-Algorithms
Given a set of points in the plane, the convex hull of the set is the smallest convex polygon that contains all the points of it. In this project we implemented khown convex hull algorithms for 2D and 3D points. More specifically for 2D points we used the incremental, the Jarvis, the Divide & Conquer and the Quick Hull algorithms for computing the convex hull of 2D points datasets. The Quick Hull was used for the computation of convex hull of 3D points dataset too. We compare each method based on the quality of the results and the execution time needed to compute the convex hull.

## Algorithms Comparison  
In the below table we can see the execution time of each convex hull algorithm for each points dataset. The datasets where randomly generated and include collinear points. We observe the Divide & Conquer algorithm was not successfully executed as the datasets included points with same X coordinates.  
<br>
**Convex Hull Algorithms: Time/NoOfPoints - Collinear Points**
| Total Points | 10 | 100 | 1000 | 10000 | 100000 | 
| --- | --- | --- | --- | --- | --- |
| Incremental | 0 | 0.00000 | 0.01806 | 0.01681 | 1.80719 |   
| Jarvis | 0 | 0.01642 | 0.12860 | 1.10671 | 10.88858 |
| Divide & Conquer | - | - | - | - | - |
| Quick Hull | 0 | 0.00000 | 0.00757 | 0.00665 | 0.04001 |

In the below table we can see the execution time of each convex hull algorithm for each points dataset. The datasets where randomly generated.   
<br>
**Convex Hull Algorithms: Time/NoOfPoints**
| Total Points | 10 | 100 | 1000 | 10000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| Incremental | 0 | 0 | 0.00000 | 0.04847 | 0.44675 |
| Jarvis | 0 | 0.007 | 0.00800 | 0.16059 | 2.18975 | 
| Divide & Conquer | 0 | 0 | - | - | - |
| Quick Hull | 0 | 0.00801 | 0.00000 | 0.00000 | 0.01634 |

In the below table we can see the execution time of each convex hull algorithm for each 2D points dataset. The datasets where randomly generated and have the constraint not to include points with same x coordinate to ensure the successful execution of Divide & Conquer algorithm.   
<br>
**Convex Hull Algorithms: Time/NoOfPoints - Different X Coords**
| Total Points | 10 | 100 | 1000 | 10000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| Incremental | 0 | 0 | 0 | 0.04002 | 0.50217 |  
| Jarvis | 0 | 0.00085 | 0.0075 | 0.23282  | 2.07023 | 
| Divide & Conquer | 0 | 0 | 0.016 | 0.13892 | 1.76016 |
| Quick Hull | 0 | 0 | 0 | 0 | 0.01557 |

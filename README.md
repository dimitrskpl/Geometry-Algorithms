# Convex-Hull-Algorithms
Given a set of points in the plane, the convex hull of the set is the smallest convex polygon that contains all the points of it. In this project we implemented well-known convex hull algorithms for 2D and 3D points. More specifically for 2D points we used the incremental, the Jarvis, the Divide & Conquer and the Quick Hull algorithms to compute the convex hull of 2D point datasets. The Quick Hull was used for the computation of convex hull of 3D points dataset too. We compare each method based on the quality of the results and the runtime required to compute the convex hull.

## Convex Hull Visualizations
In the image below we see the convex hull computed for 80 random 2D points. Obviously the result was the same for all the algorithms.
![Alt](Figures/convex_hull_2D.png)

In the image below we can see the convex hull computed for 50 random 3D points using Quick Hull algorithm.
![Alt](Figures/3D_convex_hull.png)

## Algorithms Comparison  
In the  table below we see the execution time of each convex hull algorithm for each points dataset. The datasets where randomly generated and include collinear points. We observe the Divide & Conquer algorithm was not successfully executed as the datasets included points with same X coordinates.  
<br>

**Convex Hull Algorithms: Time/NoOfPoints - Collinear Points**
| Total Points | 10 | 100 | 1000 | 10000 | 100000 | 
| --- | --- | --- | --- | --- | --- |
| Incremental | 0 | 0.00000 | 0.01806 | 0.01681 | 1.80719 |   
| Jarvis | 0 | 0.01642 | 0.12860 | 1.10671 | 10.88858 |
| Divide & Conquer | - | - | - | - | - |
| Quick Hull | 0 | 0.00000 | 0.00757 | 0.00665 | 0.04001 |

<br>   

In the table below we see the execution time of each convex hull algorithm for each points dataset. The datasets where randomly generated.     


<br>

**Convex Hull Algorithms: Time/NoOfPoints**
| Total Points | 10 | 100 | 1000 | 10000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| Incremental | 0 | 0 | 0.00000 | 0.04847 | 0.44675 |
| Jarvis | 0 | 0.007 | 0.00800 | 0.16059 | 2.18975 | 
| Divide & Conquer | 0 | 0 | - | - | - |
| Quick Hull | 0 | 0.00801 | 0.00000 | 0.00000 | 0.01634 |

<br>


In the table below we see the execution time of each convex hull algorithm for each 2D point dataset. The datasets where randomly generated and are constrained not to include points with same x coordinate to ensure successful execution of the Divide & Conquer algorithm.      


<br>

**Convex Hull Algorithms: Time/NoOfPoints - Different X Coords**
| Total Points | 10 | 100 | 1000 | 10000 | 100000 |
| --- | --- | --- | --- | --- | --- |
| Incremental | 0 | 0 | 0 | 0.04002 | 0.50217 |  
| Jarvis | 0 | 0.00085 | 0.0075 | 0.23282  | 2.07023 | 
| Divide & Conquer | 0 | 0 | 0.016 | 0.13892 | 1.76016 |
| Quick Hull | 0 | 0 | 0 | 0 | 0.01557 |
<br>


In the table below we see the time complexity in the worst case for each algorithm. **n** is the number of points of the initial dataset and **h** is the number of convex hull's points.      


<br>

**Convex Hull Algorithms: Time Comlexity/Algorithm**
| Incremental | Jarvis | Divide & Conquer | Quick Hull | 
| --- | --- | --- | --- | 
| $O(nlogn)$ | $O(nh)$ | $O(nlogn)$ | $O(n^2)$ | 

<br>

All of these 2D algorithms discussed above can accomplish what they intend to output. However, they have different time complexity with the fastest Graham scan and divide and conquer algorithm. Although Quick Hull has $O(n^2)$ time complexity it seems to be realy fast as its average time complexity is $O(nlogn)$. Regarding the implementation of the algorithms, divide & conquer was the most difficult and the most time consuming to implement.

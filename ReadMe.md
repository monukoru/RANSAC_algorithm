-RANSAC algorithm-

## 🧠 What it is ##
:This is an algorithm designed for an autonomous drone for a competition held in 2025. 
:The drone had a depth camera which creates a stream of point cloud, and then sends it to the processor which applies this algo makes some decisions and tells the safest spot to land on the ground 

## 🔍 Working ##
1)RANSAC_basic:- This python code is the core idea of the RANSAC regressor. Once, you get through this code you will be able to understand the main working 
2)RANSAC_2D:- This jupyter code uses the actual RANSAC regressor and performs the action on randomly genrated points(2d)
3)RANSAC_3D:- This jupyter code actually scraps the point cloud in a particular range converts it to 2 dimensions and then applies the Regressor to find the safest spot possible 

## 📸 Extras  ##
: Green spots denotes the good spots for landing 
: Blue spots are safest spot possible as they are marked upon by the most densest region of green spots 
: The sample of the point clouds are given. You can add yours own do a bit of adjustment and see it work

                                                               #################### This code is for learning purpose ####################
                                                                    ###################### Thank You ######################

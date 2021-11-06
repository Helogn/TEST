# this module use point cloud to show a lung!
# He Jiang
# 2021/10/23

import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d
dataset = sitk.ReadImage('D:/Test/biyesheji/biyesheji/mhd/landmark/VESSEL12_01.mhd')
# dataset = sitk.ReadImage('D:/Test/biyesheji/biyesheji/mhd/original_data/1.mhd')
data = sitk.GetArrayFromImage(dataset)
frame_num, width, height = data.shape
# TEST =data[data>0].index(data)
# TEST = data>0
# b = TEST.ravel()
A = np.array(np.where(data>0))

#---------------------------
# X = A % (height * width)
# Y = A %(height * frame_num)
# Z = A % (width * frame_num)
# X1 = X[::10000]    # resample for array
# Y1 = Y[::10000]
# Z1 = Z[::10000]
#-----------------------------

M = 2000
X1 = A[0][::M]
Y1 = A[1][::M]
Z1 = A[2][::M]
# V = A[1]
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

#-------------------
# ss = 1:300
# print(Z[20000:20300])
# ax.scatter(Z[20000:21300], Y[20000:21300],X[20000:21300], zdir='z', s=20, c=None, depthshade=True)
#-----------------

# ax.scatter(Z1, X1, Y1, zdir='z', s=20, c=None, depthshade=True)
# plt.show( )

#--------------------------------
# TEST.index(0)
# TEST_list = TEST.tolist()
# TEST_list.index(0)
# print(data)
# ax.scatter(q, f, d, zdir='z', s=20, c=None, depthshade=True)
# plt.show( )
#-----------------------------------


#-------------------open 3d--------------------------
print(len(A[0]))
# C = A[::19000]
point_cloud = []
B = len(X1)
for n in range(B):
    # point_cloud[n][0] = A[0][n]
    # point_cloud[n][1] = A[1][n]
    # point_cloud[n][2] = A[2][n]
    # point_cloud = point_cloud + [[C[0][n],C[1][n],C[2][n]]]
    point_cloud = point_cloud + [[X1[n],Y1[n],Z1[n]]]
    # print(point_cloud)
# point_cloud = A
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud)
# pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
# pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
# pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])

# o3d.visualization.draw_geometries([pcd])  # show image

# 点云法线估计

print("Downsample the point cloud with a voxel of 0.05")
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
o3d.visualization.draw_geometries([downpcd])
#Vertex normal estimation
print("Recompute the normal of the downsampled point cloud")
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid( radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd])

# distances = pcd.compute_nearest_neighbor_distance()
# avg_dist = np.mean(distances)
# radius = 3 * avg_dist

# bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))

# dec_mesh = mesh.simplify_quadric_decimation(100000)
# dec_mesh.remove_degenerate_triangles()
# dec_mesh.remove_duplicated_triangles()
# dec_mesh.remove_duplicated_vertices()
# dec_mesh.remove_non_manifold_edges()

# o3d.visualization.draw_geometries([pcd])